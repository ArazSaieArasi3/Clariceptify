"""Adverse guards for a negative profile and unperformed semantic execution."""
import unittest
from check_cdns267 import load,validate,check
class Boundaries(unittest.TestCase):
 def setUp(self):self.r,self.e=load()
 def reject(self,fn):
  fn(self.r,self.e)
  with self.assertRaises(ValueError):validate(self.r,self.e)
 def test_current(self):self.assertEqual(check()['status'],'PASS')
 def test_profile_promoted(self):self.reject(lambda r,e:e['profile'].update(in_profile=True))
 def test_consistent_claim(self):self.reject(lambda r,e:e['reasoner_attempt'].update(consistent=True))
 def test_inconsistent_claim(self):self.reject(lambda r,e:e['reasoner_attempt'].update(consistent=False))
 def test_unperformed_scenario(self):self.reject(lambda r,e:r['execution_summary'].update(executed_consistency_scenarios=8))
 def test_source_stripping(self):self.reject(lambda r,e:e['policy'].update(axioms_deleted=1))
 def test_silent_import(self):self.reject(lambda r,e:e['imports'].append('http://example.org/extension'))
 def test_missing_query(self):self.reject(lambda r,e:e['asserted_queries'].pop())
 def test_wrong_result(self):self.reject(lambda r,e:e['asserted_queries'][0].update(observed_ask=False))
 def test_wrong_source(self):self.reject(lambda r,e:r['source'].update(sha256='0'*64))
 def test_missing_question(self):self.reject(lambda r,e:r['questions'].pop())
 def test_duplicate_question(self):self.reject(lambda r,e:r['questions'][1].update(id='Q01'))
 def test_missing_finding(self):self.reject(lambda r,e:r['findings'].pop())
 def test_adoption(self):self.reject(lambda r,e:r['boundary'].update(adoption='ACCEPTED'))
 def test_extension_execution(self):self.reject(lambda r,e:r['selected_scope'].update(mapped_extension_reasoning='PASS'))
 def test_history_promotion(self):self.reject(lambda r,e:r['source'].update(historical_2008_fidelity='PROVED'))
if __name__=='__main__':unittest.main()
