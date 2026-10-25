"""Reject broken reader paths and stale evidence in the publication pipeline."""
from pathlib import Path
import shutil,tempfile,unittest
from build_documentation import build,inventory
from check_documentation import check

ROOT=Path(__file__).resolve().parents[1]
class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.folder=Path(self.temp.name);self.root=self.folder/'source';self.root.mkdir()
        for name,p in inventory(ROOT).items():
            target=self.root/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
    def tearDown(self):self.temp.cleanup()
    def test_broken_reader_path_rejected(self):
        p=self.root/'docs/guide/Home.md';p.write_text(p.read_text()+'\n[Broken evidence](../../missing-evidence.yaml)\n')
        with self.assertRaisesRegex(ValueError,'Source link target missing'):build(self.root,self.folder/'site','synthetic-test')
    def test_stale_vveaa_profile_rejected(self):
        p=self.root/'evaluation/vveaa-profile.yaml';p.write_bytes(p.read_bytes()+b'\n')
        with self.assertRaisesRegex(ValueError,'Stale profile report'):check(self.root)

if __name__=='__main__':unittest.main()
