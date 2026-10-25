"""Reject missing-text concealment, phantom archive saves and evidence drift."""
from pathlib import Path
import json
import shutil
import tempfile
import unittest
import yaml
from check_corpus_access import check, ROOT


class CorpusAccessBoundaries(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for folder in ['evidence/related-work', 'evaluation/related-work']:
            shutil.copytree(ROOT / folder, self.root / folder)

    def tearDown(self):
        self.temp.cleanup()

    def test_current_inventory(self):
        self.assertEqual(check(self.root)['original_candidate_labels'], 19)

    def test_hidden_access_gap(self):
        p = self.root / 'evidence/related-work/corpus/download-requests.yaml'
        d = yaml.safe_load(p.read_text()); d['requests'].pop(); p.write_text(yaml.safe_dump(d))
        with self.assertRaisesRegex(ValueError, 'request population'):
            check(self.root)

    def test_unissued_archive(self):
        p = self.root / 'evidence/related-work/corpus/archive-record.json'
        d = json.loads(p.read_text()); d['availability'] = 'PREPARED_ONLY'; p.write_text(json.dumps(d))
        with self.assertRaisesRegex(ValueError, 'not saved'):
            check(self.root)

    def test_changed_LMM_evidence(self):
        p = self.root / 'evaluation/related-work/lmm/LMM_L2.json'
        p.write_text(p.read_text().replace('154', '999'))
        with self.assertRaisesRegex(ValueError, 'evidence changed'):
            check(self.root)

    def test_changed_archive_manifest(self):
        p = self.root / 'evidence/related-work/corpus/source-file-manifest.json'
        p.write_text(p.read_text() + '\n')
        with self.assertRaisesRegex(ValueError, 'manifest identity'):
            check(self.root)


if __name__ == '__main__':
    unittest.main()
