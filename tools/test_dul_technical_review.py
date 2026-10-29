"""Reject stale DUL evidence, unsupported closure and modified case receipts."""
import copy,json,shutil,tempfile,unittest,yaml
from pathlib import Path
from check_dul_technical_review import check,ROOT
class DULTechnicalEvidence(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
  for folder in ['evidence/related-work','evaluation/related-work','tools']:shutil.copytree(ROOT/folder,self.root/folder)
 def tearDown(self):self.tmp.cleanup()
 def mutate(self,fn):
  p=self.root/'evidence/related-work/artifacts/DUL-technical-review.yaml';r=yaml.safe_load(p.read_text());fn(r);p.write_text(yaml.safe_dump(r))
 def test_valid(self):self.assertEqual(check(self.root)['questions'],8)
 def test_source_substitution(self):
  self.mutate(lambda r:r['source_root'].update(sha256='0'*64))
  with self.assertRaisesRegex(ValueError,'root source'):check(self.root)
 def test_missing_question(self):
  self.mutate(lambda r:r['questions'].pop())
  with self.assertRaisesRegex(ValueError,'eight-question'):check(self.root)
 def test_acceptance_promotion(self):
  self.mutate(lambda r:r['boundary'].update(scientific_acceptance='APPROVED'))
  with self.assertRaisesRegex(ValueError,'acceptance'):check(self.root)
 def test_changed_execution(self):
  p=self.root/'evaluation/related-work/dul/semantic-cases.json';p.write_text(p.read_text().replace('"passed": 29','"passed": 99'))
  with self.assertRaisesRegex(ValueError,'evidence binding'):check(self.root)
 def test_changed_runner(self):
  p=self.root/'tools/inspect_dul_semantics.py';p.write_text(p.read_text()+'\n# modified\n')
  with self.assertRaisesRegex(ValueError,'executed generator'):check(self.root)
 def test_untracked_finding(self):
  self.mutate(lambda r:r['findings'][0].update(next_issue=None))
  with self.assertRaisesRegex(ValueError,'Untracked'):check(self.root)
if __name__=='__main__':unittest.main()
