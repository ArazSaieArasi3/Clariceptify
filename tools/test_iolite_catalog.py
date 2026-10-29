"""Adverse checks for complete source-bound IOLite and shared import accounting."""
import copy,json,unittest,tempfile
from pathlib import Path
from check_iolite_catalog import load,validate,check,NS,inspect
class IOLiteTests(unittest.TestCase):
 def setUp(self):self.cat,self.source,self.census=load()
 def reject(self):
  with self.assertRaises((ValueError,KeyError)):validate(self.cat,self.source,self.census)
 def test_complete_public_record(self):self.assertEqual(check()['status'],'PASS')
 def test_missing_class(self):self.cat['classes'].pop();self.reject()
 def test_duplicate_class(self):self.cat['classes'][-1]=copy.deepcopy(self.cat['classes'][0]);self.reject()
 def test_wrong_source(self):self.cat['modules'][0]['source_sha256']='0'*64;self.reject()
 def test_invented_missing_definition(self):
  r=next(r for r in self.cat['classes'] if r['iri']==NS+'Gesture');r['reviewer_definition']={'text':'Invented','basis':'REVIEWER_PARAPHRASE'};self.reject()
 def test_lost_paraphrase(self):self.cat['classes'][0]['reviewer_definition']['text']=None;self.reject()
 def test_changed_annotation_hash(self):self.cat['classes'][0]['source_definition']['annotation_sha256']='0'*64;self.reject()
 def test_changed_hierarchy(self):self.cat['classes'][0]['named_superclasses']=[];self.reject()
 def test_missing_constraint_pointer(self):self.cat['classes'][0]['constraint_ref']='somewhere';self.reject()
 def test_external_promoted_to_local(self):self.source['populations']['external_redeclarations'].pop();self.reject()
 def test_inferred_count_invented(self):self.source['modules'][0]['inferred_class_count']=79;self.reject()
 def test_unresolved_import(self):self.source['unresolved_imports']=['unknown'];self.reject()
 def test_missing_builtin(self):self.source['modules'][-1]['asserted_closure_class_iris'].remove('http://www.w3.org/2002/07/owl#Thing');self.reject()
 def test_duplicate_closure_class(self):self.source['modules'][-1]['asserted_closure_class_iris'].append(self.source['modules'][-1]['asserted_closure_class_iris'][0]);self.reject()
 def test_wrong_foundation(self):self.cat['foundation']['edition']='BFO1';self.reject()
 def test_historical_equivalence_invented(self):self.cat['historical_paper_fidelity']='ESTABLISHED';self.reject()
 def test_census_constraints_removed(self):self.census['classes'].pop();self.reject()
 def test_wrong_generator_digest(self):self.source['generator']['sha256']='0'*64;self.reject()
 def test_bad_bytes_rejected_before_parser_import(self):
  with tempfile.TemporaryDirectory() as tmp:
   (Path(tmp)/'DUL-http.owl').write_text('not the retained source')
   with self.assertRaises(ValueError):inspect(Path(tmp))
if __name__=='__main__':unittest.main()
