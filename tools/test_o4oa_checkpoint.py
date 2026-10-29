"""Adverse guards for a document-only, deliberately incomplete technical checkpoint."""
import copy,unittest
from pathlib import Path
from check_o4oa_checkpoint import load,validate,check,ROOT
class Boundaries(unittest.TestCase):
 def setUp(self):self.r,self.d=load()
 def reject(self,fn):
  fn(self.r,self.d)
  with self.assertRaises(ValueError):validate(self.r,self.d)
 def test_baseline(self):self.assertEqual(validate(self.r,self.d)['status'],'PASS')
 def test_issue_closure(self):self.reject(lambda r,d:r.update(issue_completion=True))
 def test_complete_status(self):self.reject(lambda r,d:r.update(status='COMPLETE'))
 def test_model_change(self):self.reject(lambda r,d:r['boundary'].update(model_change='ADOPTED'))
 def test_reasoning_claim(self):self.reject(lambda r,d:r['boundary'].update(reasoner_execution='PASS'))
 def test_machine_count(self):self.reject(lambda r,d:r['populations'].update(local_machine_classes=138))
 def test_source_replacement(self):self.reject(lambda r,d:r['identity'].update(source_sha256='0'*64))
 def test_version_silent_fix(self):self.reject(lambda r,d:r['identity'].update(reference_ontology_version_in_conclusion='2.6'))
 def test_invented_root(self):self.reject(lambda r,d:r['identity'].update(formal_root='O4OA.owl'))
 def test_global_absence(self):self.reject(lambda r,d:d['discovery'].update(global_absence_claim=True))
 def test_access_promoted(self):self.reject(lambda r,d:next(x for x in d['discovery']['retrievals'] if x['id']=='reference-tree').update(status=200))
 def test_missing_term(self):self.reject(lambda r,d:d['terms']['rows'].pop())
 def test_duplicate_label(self):self.reject(lambda r,d:d['terms']['rows'][1].update(source_label=d['terms']['rows'][0]['source_label']))
 def test_invented_iri(self):self.reject(lambda r,d:d['terms']['rows'][0].update(machine_class_iri='http://example.com/Class'))
 def test_filled_missing_stereotype(self):self.reject(lambda r,d:next(x for x in d['terms']['rows'] if x['source_label']=='XML DTDs').update(source_stereotype='subkind'))
 def test_label_only_promoted(self):self.reject(lambda r,d:next(x for x in d['terms']['rows'] if x['definition_status']=='LABEL_ONLY').update(definition_status='DESCRIPTIVE_SOURCE_CANDIDATE'))
 def test_missing_visual(self):self.reject(lambda r,d:d['reading']['figures'].pop())
 def test_missing_page(self):self.reject(lambda r,d:d['reading']['read_pages'].pop())
 def test_missing_finding(self):self.reject(lambda r,d:r['findings'].pop())
 def test_q_pass(self):self.reject(lambda r,d:r['questions'][0].update(status='PASS'))
 def test_false_solver_case(self):self.reject(lambda r,d:r['conceptual_adverse_cases'][0].update(execution='SOLVER_PASS'))
 def test_open_gate_removed(self):self.reject(lambda r,d:r['closure'].update(decision='CLOSE'))
 def test_private_locator(self):self.reject(lambda r,d:r['findings'][0].update(judgment='See https://chatgpt.com/c/private'))
 def test_default_check(self):self.assertFalse(check()['issue_completion'])
if __name__=='__main__':unittest.main()
