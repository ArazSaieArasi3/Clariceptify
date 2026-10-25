"""Reject source/report identity drift and unsupported completion claims."""
from pathlib import Path
import shutil
import tempfile
import unittest
import yaml
from check_related_reviews import check, ROOT


class ReviewBoundaries(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for folder in ['evidence/related-work', 'evaluation/related-work']:
            shutil.copytree(ROOT / folder, self.root / folder)
        (self.root / 'model').mkdir()
        shutil.copy(ROOT / 'model/concepts.yaml', self.root / 'model/concepts.yaml')

    def tearDown(self):
        self.temp.cleanup()

    def edit(self, path, edit):
        p = self.root / path
        record = yaml.safe_load(p.read_text())
        edit(record)
        p.write_text(yaml.safe_dump(record))

    def test_valid_records(self):
        self.assertEqual(check(self.root)['closure_ready_deliverables'], 5)

    def test_changed_source_identity(self):
        self.edit('evidence/related-work/artifacts/cDnS.yaml', lambda x: x.update(artifact_sha256='0' * 64))
        with self.assertRaisesRegex(ValueError, 'identity'):
            check(self.root)

    def test_changed_report(self):
        p = self.root / 'evaluation/related-work/artifacts/DUL.json'
        p.write_text(p.read_text().replace('1917', '9999'))
        with self.assertRaisesRegex(ValueError, 'Changed inspection'):
            check(self.root)

    def test_missing_locator(self):
        self.edit('evidence/related-work/reviews/DnS.yaml', lambda x: x['observations'][0].update(locator=''))
        with self.assertRaisesRegex(ValueError, 'locator'):
            check(self.root)

    def test_unavailable_chapter_cannot_be_promoted(self):
        self.edit('evidence/related-work/reviews/DUL.yaml', lambda x: x['access'].update(state='FULL_TEXT_REVIEWED'))
        with self.assertRaisesRegex(ValueError, 'Unavailable'):
            check(self.root)


if __name__ == '__main__':
    unittest.main()
