"""Adverse tests for unsupported review closure and evidence promotion."""
import copy
import unittest
import yaml
from check_deep_reviews import ROOT, BASE, validate_dossier


class ReviewBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.base = ROOT / BASE
        self.register = yaml.safe_load((self.base / 'register.yaml').read_text())
        self.entry = self.register['acquired_papers'][0]
        self.dimensions = yaml.safe_load((self.base / 'protocol.yaml').read_text())['dimensions']
        self.dossier = yaml.safe_load((self.base / self.entry['id'] / 'review.yaml').read_text())

    def reject(self, mutate):
        d = copy.deepcopy(self.dossier)
        mutate(d)
        with self.assertRaises(ValueError):
            validate_dossier(d, self.entry, self.dimensions)

    def test_source_substitution(self):
        self.reject(lambda d: d['source'].update(sha256='0' * 64))

    def test_incomplete_reading(self):
        self.reject(lambda d: d['coverage']['read_pages'].pop())

    def test_dangling_evidence(self):
        self.reject(lambda d: d['findings'][0].update(evidence=['MISSING']))

    def test_missing_shared_dimension(self):
        self.reject(lambda d: d['dimensions'].pop(next(iter(self.dimensions))))

    def test_model_adoption_promotion(self):
        self.reject(lambda d: d['boundary'].update(adoption='AUTOMATICALLY_APPLIED'))

    def test_false_executed_claim(self):
        self.reject(lambda d: d['findings'][0].update(basis='EXECUTED'))

    def test_unreviewed_unit(self):
        self.reject(lambda d: d['coverage']['units'][0].update(status='PENDING'))

    def test_unbound_artifact_task(self):
        self.reject(lambda d: d['artifact'].update(issue=999999))


if __name__ == '__main__':
    unittest.main()
