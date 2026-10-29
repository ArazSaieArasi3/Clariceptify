"""Adverse checks for complete source coverage and bounded semantic claims."""
import copy,unittest
from check_dns235 import load,validate,check
class Boundaries(unittest.TestCase):
 def setUp(self):self.r,self.d=load()
 def reject(self,f):
  f(self.r,self.d)
  with self.assertRaises(ValueError):validate(self.r,self.d)
 def test_current(self):self.assertEqual(check()['status'],'PASS')
 def test_missing_class(self):self.reject(lambda r,d:d['catalog']['classes'].pop())
 def test_duplicate_class(self):self.reject(lambda r,d:d['catalog']['classes'].append(d['catalog']['classes'][0]))
 def test_false_history(self):self.reject(lambda r,d:r['identity'].update(historical_2003_fidelity='PROVED'))
 def test_source_substitution(self):self.reject(lambda r,d:r['identity'].update(sha256='0'*64))
 def test_population_inflation(self):self.reject(lambda r,d:d['census']['counts'].update(local_classes=95))
 def test_hidden_definition_gap(self):self.reject(lambda r,d:next(x for x in d['catalog']['classes'] if x['iri'].endswith('#non-agentive-figure'))['source_definition'].update(state='PRESENT_COMMENT_CANDIDATE'))
 def test_false_formula_solver(self):self.reject(lambda r,d:r['execution'].update(FOL_formula14_solver='PASS'))
 def test_false_mapping(self):self.reject(lambda r,d:r['model_comparison_candidates'][0].update(status='ACCEPTED_EQUIVALENCE'))
 def test_false_expert(self):self.reject(lambda r,d:r['boundary'].update(independent_expert_review='PASS'))
 def test_missing_case(self):self.reject(lambda r,d:d['semantic']['tests'].pop())
 def test_wrong_case(self):self.reject(lambda r,d:d['semantic']['tests'][0].update(observed_consistent=False))
 def test_changed_constraint(self):self.reject(lambda r,d:d['catalog']['classes'][0].update(axiom_sha256='0'*64))
 def test_hidden_import(self):self.reject(lambda r,d:d['census']['imports'].pop())
if __name__=='__main__':unittest.main()
