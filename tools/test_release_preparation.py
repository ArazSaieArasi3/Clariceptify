"""Boundary tests for the exact preparation manifest and untrusted archive bytes."""
from pathlib import Path
import json,tempfile,unittest,zipfile
import yaml
from build_release import build,digest
from readback_release import verify

class PreparationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.folder=Path(self.temp.name)
        self.root=self.folder/'source';self.root.mkdir();(self.root/'example.txt').write_bytes(b'example\n')
        self.manifest=self.folder/'manifest.yaml'
        self.record={'stage':'preparation_only','publication_eligible':False,'base_source_commit':'0'*40,'snapshot_binding':'synthetic test only','artifact_versions':{'model':'test','diagram':'test'},'excluded_families':['private inputs'],'pending_gates':['actual owner decision'],'members':[{'path':'example.txt','bytes':8,'sha256':digest(b'example\n')}]}
        self.manifest.write_text(yaml.safe_dump(self.record))
        self.out=self.folder/'output';build(self.root,self.manifest,self.out)
        self.archive=self.out/'clariceptify-r1-preparation.zip'
    def tearDown(self):self.temp.cleanup()
    def test_exact_roundtrip(self):self.assertEqual(verify(self.archive,self.manifest,False)['status'],'PASS')
    def test_changed_source_rejected(self):
        (self.root/'example.txt').write_bytes(b'changed\n')
        with self.assertRaisesRegex(ValueError,'differs from manifest'):build(self.root,self.manifest,self.out)
    def test_unregistered_escape_rejected(self):
        with zipfile.ZipFile(self.archive,'a') as z:z.writestr('../escape.txt','bad')
        with self.assertRaisesRegex(ValueError,'membership'):verify(self.archive,self.manifest,False)
    def test_changed_member_rejected(self):
        replacement=self.folder/'changed.zip'
        with zipfile.ZipFile(self.archive) as old,zipfile.ZipFile(replacement,'w') as new:
            for info in old.infolist():new.writestr(info,b'changed\n' if info.filename=='example.txt' else old.read(info.filename))
        with self.assertRaisesRegex(ValueError,'digest differs'):verify(replacement,self.manifest,False)
    def test_rc_promotion_rejected(self):
        self.record['stage']='rc';self.record['publication_eligible']=True;self.manifest.write_text(yaml.safe_dump(self.record))
        with self.assertRaisesRegex(ValueError,'preparation packages only'):build(self.root,self.manifest,self.out)

if __name__=='__main__':unittest.main()
