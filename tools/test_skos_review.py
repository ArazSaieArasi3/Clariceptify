"""Reject incomplete document evidence and unperformed semantic claims."""
import copy,tempfile,unittest
from pathlib import Path
from check_skos_review import load,validate,check
from inspect_skos_document import inspect
class ReviewTests(unittest.TestCase):
 def setUp(self):self.r,self.d=copy.deepcopy(load())
 def rejected(self):
  with self.assertRaises(ValueError):validate(self.r,self.d)
 def test_valid(self):self.assertEqual(validate(self.r,self.d)['status'],'PASS')
 def test_complete_files(self):self.assertEqual(check()['status'],'PASS')
 def test_wrong_source(self):self.r['identity']['source_sha256']='0'*64;self.rejected()
 def test_wrong_edition(self):self.r['identity']['date']='2004-02-01';self.rejected()
 def test_primer_substitution(self):self.r['identity']['primer_review']='COMPLETE';self.rejected()
 def test_fake_paper(self):self.r['identity']['document_type']='Journal Article';self.rejected()
 def test_fake_doi(self):self.r['identity']['doi']='10.example/invented';self.rejected()
 def test_missing_section(self):self.r['coverage']['sections'].pop();self.rejected()
 def test_duplicate_section(self):self.r['coverage']['sections'][-1]=self.r['coverage']['sections'][0];self.rejected()
 def test_unread_section(self):self.r['coverage']['sections'][0]['state']='QUEUED';self.rejected()
 def test_fake_class_count(self):self.r['coverage']['local_owl_classes']=5;self.rejected()
 def test_semantic_promotion(self):self.r['boundary']['reasoner_execution']='PASS';self.rejected()
 def test_artifact_completion(self):self.r['boundary']['artifact_review_completed']=True;self.rejected()
 def test_paper_denominator(self):self.r['boundary']['full_paper_denominator_change']=1;self.rejected()
 def test_missing_condition(self):self.d['reading']['statements'].pop();self.rejected()
 def test_changed_condition_binding(self):self.d['reading']['statements'][0]['normalized_row_sha256']='0'*64;self.rejected()
 def test_wrong_integrity_type(self):self.d['reading']['statements'][47]['classification']='CLASS_PROPERTY_DEFINITION_OR_INFERENCE_CONDITION';self.rejected()
 def test_missing_example(self):self.d['reading']['examples'].pop();self.rejected()
 def test_source_example_promoted(self):self.d['reading']['examples'][0]['result_origin']='HERMlT_PASS';self.rejected()
 def test_missing_diagram(self):self.d['reading']['text_diagrams'].pop();self.rejected()
 def test_badge_promoted(self):self.d['document']['images'][0]['role']='SUBSTANTIVE_FIGURE';self.rejected()
 def test_missing_erratum(self):self.d['errata']['entries'].pop();self.rejected()
 def test_wrong_errata_source(self):self.d['errata']['sha256']='0'*64;self.rejected()
 def test_errata_changes_source(self):self.d['errata']['primary_source_unchanged']=False;self.rejected()
 def test_private_link(self):self.r['source_synopsis']['text']='https://chatgpt.com/c/private';self.rejected()
 def test_missing_finding(self):self.r['findings'].pop();self.rejected()
 def test_wrong_anchor(self):self.r['findings'][0]['locator']+='missing';self.rejected()
 def test_adoption(self):self.r['decision']['disposition']='ADOPTED';self.rejected()
 def test_unperformed_experiment(self):self.r['adverse_cases'][0]['execution']='REASONER_PASS';self.rejected()
 def test_invented_permission(self):self.r['rights']['legal_permission_assessment']='APPROVED';self.rejected()
 def test_bad_input_before_parsing(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'bad';p.write_bytes(b'not selected source')
   with self.assertRaisesRegex(ValueError,'Wrong source bytes'):inspect(p)
if __name__=='__main__':unittest.main()
