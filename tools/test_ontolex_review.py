"""Adverse checks for document coverage and unsupported research promotion."""
import copy,tempfile,unittest
from pathlib import Path
from check_ontolex_review import load,validate,check,ROOT
from inspect_ontolex_document import inspect
class ReviewTests(unittest.TestCase):
 def setUp(self):self.r,self.d=copy.deepcopy(load())
 def rejected(self):
  with self.assertRaises(ValueError):validate(self.r,self.d)
 def test_valid(self):self.assertEqual(validate(self.r,self.d)['status'],'PASS')
 def test_complete_files(self):self.assertEqual(check()['status'],'PASS')
 def test_wrong_source(self):self.r['identity']['source_sha256']='0'*64;self.rejected()
 def test_fake_standard(self):self.r['identity']['w3c_standard']=True;self.rejected()
 def test_fake_doi(self):self.r['identity']['doi']='10.example/invented';self.rejected()
 def test_missing_section(self):self.r['coverage']['numbered_sections'].pop();self.rejected()
 def test_duplicate_section(self):self.r['coverage']['numbered_sections'][-1]=self.r['coverage']['numbered_sections'][0];self.rejected()
 def test_unread_section(self):self.r['coverage']['numbered_sections'][0]['state']='QUEUED';self.rejected()
 def test_fake_class_count(self):self.r['coverage']['local_owl_classes']=23;self.rejected()
 def test_semantic_promotion(self):self.r['boundary']['reasoner_execution']='PASS';self.rejected()
 def test_artifact_completion(self):self.r['boundary']['artifact_review_completed']=True;self.rejected()
 def test_paper_denominator(self):self.r['boundary']['full_paper_denominator_change']=1;self.rejected()
 def test_missing_image(self):self.d['images']['images'].pop();self.rejected()
 def test_unseen_image(self):self.d['images']['images'][0]['visual_inspection']='ALT_TEXT_ONLY';self.rejected()
 def test_wrong_image_url(self):self.d['images']['images'][0]['url']='https://example.com/other.png';self.rejected()
 def test_private_path(self):self.d['images']['images'][0]['path']='/workspace/private';self.rejected()
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
