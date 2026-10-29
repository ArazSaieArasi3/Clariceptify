"""Reject misleading source populations, successful-test claims and source substitutions."""
import copy
import unittest
from check_bdi2026_review import load, validate, check


class EvidenceBoundaries(unittest.TestCase):
    def setUp(self):
        self.review, self.catalog, self.data = copy.deepcopy(load())

    def reject(self, mutate):
        mutate()
        with self.assertRaises(ValueError):
            validate(self.review, self.catalog, self.data)

    def test_current_record(self):
        self.assertEqual(check()['status'], 'PASS')

    def test_partial_glossary(self):
        self.reject(lambda: self.catalog['classes'].pop())

    def test_false_alignment_completion(self):
        self.reject(lambda: self.catalog['import_closure'].update(imported_definitions_complete=True))

    def test_invented_metadata_definition(self):
        row = next(x for x in self.catalog['classes'] if not x['annotation_records'])
        self.reject(lambda: row['reviewer_definition'].update(text='Invented external definition'))

    def test_profile_failure_hidden(self):
        self.reject(lambda: self.data['semantic'].update(core_profile_in_OWL2_DL=True))

    def test_author_data_repaired(self):
        row = next(x for x in self.data['semantic']['tests'] if 'source_dataset' in x)
        self.reject(lambda: row.update(observed_consistent=True))

    def test_false_all_queries_pass(self):
        self.reject(lambda: self.data['cqs']['summary'].update(matches=36, mismatches=0))

    def test_missing_cq(self):
        self.reject(lambda: self.data['cqs']['executions'].pop())

    def test_source_substitution(self):
        self.reject(lambda: self.data['census']['modules']['bdi/bdi.ttl'].update(source_sha256='0' * 64))

    def test_modified_fixture(self):
        self.reject(lambda: self.data['semantic']['tests'][1].update(fixture_nt='changed'))

    def test_unexecuted_application_claim(self):
        self.reject(lambda: self.data['application'].update(execution='PASS'))

    def test_invented_independent_acceptance(self):
        self.reject(lambda: self.review['boundary'].update(independent_expert_review='PASS'))


if __name__ == '__main__':
    unittest.main()
