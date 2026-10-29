"""Prevent false completion of large class glossaries and descriptive claims."""
import copy,unittest
from check_cognitiveatlas_review import load,validate,check
from build_corpus_descriptives import calculate


class ReviewBoundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.original=load()
    def setUp(self):self.r,self.c,self.d,self.rows,self.defs=copy.deepcopy(self.original)
    def reject(self,fn):
        fn()
        with self.assertRaises(ValueError):validate(self.r,self.c,self.d,self.rows,self.defs)
    def test_current(self):self.assertEqual(check()['status'],'PASS')
    def test_missing_class(self):self.reject(lambda:self.rows.pop())
    def test_duplicate_class(self):self.reject(lambda:self.rows.append(self.rows[0]))
    def test_missing_definition(self):self.reject(lambda:self.defs.pop())
    def test_invented_paraphrase(self):self.reject(lambda:self.rows[0]['reviewer_definition'].update(text='invented'))
    def test_hidden_collisions(self):self.reject(lambda:self.c['counts'].update(ambiguous_multi_identifier_classes=0))
    def test_profile_promoted(self):self.reject(lambda:self.d['semantic'].update(owl2_dl_profile_pass=True))
    def test_generator_execution_invented(self):self.reject(lambda:self.d['static'].update(generator_execution='PASS'))
    def test_source_definition_relicensed(self):self.reject(lambda:self.defs[0].update(license_url='MIT'))
    def test_human_acceptance_invented(self):self.reject(lambda:self.r['boundary'].update(independent_expert_review='PASS'))
    def test_relation_unit_substitution(self):self.reject(lambda:self.d['census']['counts'].update(local_declared_object_properties=2825))
    def test_no_corpus_class_total(self):
        s=calculate();self.assertEqual(s['counts']['full_paper_reviews'],18);self.assertEqual(s['counts']['limited_summary_reviews'],1)
        self.assertNotIn('total_classes',s['counts']);self.assertEqual(s['counts']['module_rows'],12)
        self.assertEqual(sum(p['indexed_relation_groups'] is None for p in s['papers']),3)


if __name__=='__main__':unittest.main()
