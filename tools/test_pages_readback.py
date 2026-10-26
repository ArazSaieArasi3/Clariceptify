"""Recover transient HTTP errors without accepting incorrect published bytes."""
from pathlib import Path
from urllib.error import HTTPError
from unittest.mock import MagicMock, patch
import hashlib
import json
import tempfile
import unittest
import yaml
import readback_pages


class ReadbackTests(unittest.TestCase):
    def response(self, payload=b'expected', status=200):
        response = MagicMock()
        response.__enter__.return_value = response
        response.status = status
        response.read.return_value = payload
        return response

    def http_error(self, status):
        return HTTPError('https://example.invalid/site/', status, 'synthetic', None, None)

    @patch('readback_pages.time.sleep')
    @patch('readback_pages.urlopen')
    def test_transient_503_recovers(self, open_url, sleep):
        open_url.side_effect = [self.http_error(503), self.response()]
        self.assertEqual(readback_pages.fetch('https://example.invalid', 'site/index.html'), b'expected')
        self.assertEqual(open_url.call_count, 2)
        sleep.assert_called_once_with(1)

    @patch('readback_pages.time.sleep')
    @patch('readback_pages.urlopen')
    def test_persistent_503_exhausts(self, open_url, sleep):
        open_url.side_effect = [self.http_error(503) for _ in range(4)]
        with self.assertRaisesRegex(ValueError, 'HTTP 503'):
            readback_pages.fetch('https://example.invalid', 'site/index.html')
        self.assertEqual(open_url.call_count, 4)
        self.assertEqual([c.args[0] for c in sleep.call_args_list], [1, 2, 4])

    @patch('readback_pages.time.sleep')
    @patch('readback_pages.urlopen')
    def test_permanent_404_fails_immediately(self, open_url, sleep):
        open_url.side_effect = self.http_error(404)
        with self.assertRaisesRegex(ValueError, 'HTTP 404'):
            readback_pages.fetch('https://example.invalid', 'missing.html')
        self.assertEqual(open_url.call_count, 1)
        sleep.assert_not_called()

    @patch('readback_pages.urlopen')
    def test_unexpected_success_status_rejected(self, open_url):
        open_url.return_value = self.response(status=201)
        with self.assertRaisesRegex(ValueError, 'Unexpected public response'):
            readback_pages.fetch('https://example.invalid', 'index.html')

    @patch('readback_pages.fetch')
    def test_wrong_page_bytes_rejected(self, fetch):
        manifest = json.dumps({'source_commit': 'synthetic', 'output_sha256': {
            'index.html': hashlib.sha256(b'expected').hexdigest()}}).encode()
        publication = json.dumps({'current': {'route': 'current/', 'source_commit': 'synthetic',
            'manifest_sha256': hashlib.sha256(manifest).hexdigest()}, 'frozen': []}).encode()
        fetch.side_effect = [publication, manifest, b'incorrect']
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / 'publication-manifest.json').write_bytes(publication)
            with self.assertRaisesRegex(ValueError, 'Public byte mismatch'):
                readback_pages.readback(tmp, 'https://example.invalid')

    @patch('readback_pages.time.sleep')
    @patch('readback_pages.fetch')
    def test_stale_deployment_manifest_rejected(self, fetch, sleep):
        fetch.return_value = b'stale-generation'
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / 'publication-manifest.json').write_bytes(b'expected-generation')
            with self.assertRaisesRegex(ValueError, 'deployment manifest differs'):
                readback_pages.readback(tmp, 'https://example.invalid', attempts=2)
        self.assertEqual(fetch.call_count, 2)

    def test_rerun_artifact_name_is_unique_and_matched(self):
        root = Path(__file__).resolve().parents[1]
        workflow = yaml.safe_load((root / '.github/workflows/pages.yml').read_text())
        steps = workflow['jobs']['deploy']['steps']
        upload = next(s for s in steps if s.get('with', {}).get('path') == '${{ runner.temp }}/artifact.tar')
        deploy = next(s for s in steps if s.get('id') == 'deployment')
        name = upload['with']['name']
        self.assertIn('${{ github.run_id }}', name)
        self.assertIn('${{ github.run_attempt }}', name)
        self.assertEqual(name, deploy['with']['artifact_name'])


if __name__ == '__main__':
    unittest.main()
