"""Negative regression checks for the source-bound DUL glossary contract."""
import copy
import tempfile
from pathlib import Path
import unittest
import yaml
from check_dul_class_catalog import PATH, validate, digest, inspect_source


class DULCatalogTests(unittest.TestCase):
    def setUp(self):
        self.data = yaml.safe_load(PATH.read_text())

    def reject(self):
        self.assertEqual(validate(self.data)['status'], 'FAIL')

    def test_complete_public_record(self):
        self.assertEqual(validate(self.data)['status'], 'PASS')

    def test_missing_class(self):
        self.data['classes'].pop(); self.reject()

    def test_duplicate_class(self):
        self.data['classes'][-1] = copy.deepcopy(self.data['classes'][0]); self.reject()

    def test_fabricated_class_with_rehashed_inventory(self):
        self.data['classes'][0]['iri'] += 'Invented'
        self.data['populations']['local_declared_named_class_iris'][0] += 'Invented'
        self.data['class_iri_set_sha256'] = digest(self.data['populations']['local_declared_named_class_iris'])
        self.reject()

    def test_false_source_digest(self):
        self.data['source']['sha256'] = '0'*64; self.reject()

    def test_changed_axiom(self):
        self.data['classes'][0]['constraints'].pop(); self.reject()

    def test_missing_supported_paraphrase(self):
        self.data['classes'][0]['reviewer_definition'] = None; self.reject()

    def test_invented_missing_definition(self):
        row=next(x for x in self.data['classes'] if x['iri'].endswith('#BiologicalObject'))
        row['reviewer_definition'] = 'An invented definition'; self.reject()

    def test_label_only_promoted(self):
        row=next(x for x in self.data['classes'] if x['iri'].endswith('#Norm'))
        row['source_definition']['status']='DESCRIPTIVE_COMMENT_REVIEWED'
        row['reviewer_definition']='An invented adequate definition'; self.reject()

    def test_false_provenance_hash(self):
        self.data['classes'][0]['annotation_records'][0]['text_sha256']='bad'; self.reject()

    def test_false_counts(self):
        self.data['counts']['accepted_descriptive_comment_classes']=78; self.reject()

    def test_incorrect_source_bytes_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'fake.ttl'; p.write_text('not the selected source')
            with self.assertRaises(ValueError):inspect_source(p)


if __name__ == '__main__':unittest.main()
