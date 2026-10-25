"""Boundary tests for the exact preparation manifest and untrusted archive bytes."""
from pathlib import Path
import hashlib,json,shutil,tempfile,unittest,zipfile
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

    def rc_record(self):
        source=Path(__file__).resolve().parents[1]
        paths=['CITATION.cff','LICENSE','LICENSE-MIT','LICENSE-CC-BY-4.0','THIRD-PARTY-NOTICES.md',
               'docs/decisions/release-license.md','docs/decisions/artifact-creators.md','tools/vendor/cff-1.2.0.schema.json']
        for name in paths:
            target=self.root/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source/name,target)
        citation=self.root/'CITATION.cff';record=yaml.safe_load(citation.read_text());record['version']='0.1.0-rc.1';citation.write_text(yaml.safe_dump(record))
        members=[]
        for name in paths:
            data=(self.root/name).read_bytes()
            members.append({'path':name,'bytes':len(data),'sha256':digest(data),'git_blob_sha':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),'origin':'exact_source_commit_member','license':'CC-BY-4.0'})
        self.record.update(stage='rc_candidate',publication_eligible=True,target_station='v0.1.0-rc.1',source_commit='a'*40,snapshot_binding='exact_registered_source_commit',members=members,
                           member_path_digest_sha256=digest(json.dumps({r['path']:r['sha256'] for r in members},sort_keys=True,separators=(',',':')).encode()))
        self.manifest.write_text(yaml.safe_dump(self.record))

    def test_registered_rc_roundtrip(self):
        self.rc_record();build(self.root,self.manifest,self.out)
        self.assertEqual(verify(self.out/'clariceptify-v0.1.0-rc.1.zip',self.manifest,False)['stage'],'rc_candidate')

    def test_rc_git_identity_rejected(self):
        self.rc_record();self.record['members'][0]['git_blob_sha']='b'*40;self.manifest.write_text(yaml.safe_dump(self.record))
        with self.assertRaisesRegex(ValueError,'Git member identity'):build(self.root,self.manifest,self.out)

    def test_rc_changed_creator_rejected(self):
        self.rc_record();p=self.root/'CITATION.cff';p.write_text(p.read_text().replace('Hassan','Wrong'))
        for row in self.record['members']:
            if row['path']=='CITATION.cff':
                data=p.read_bytes();row.update(bytes=len(data),sha256=digest(data),git_blob_sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
        self.record['member_path_digest_sha256']=digest(json.dumps({r['path']:r['sha256'] for r in self.record['members']},sort_keys=True,separators=(',',':')).encode())
        self.manifest.write_text(yaml.safe_dump(self.record))
        with self.assertRaisesRegex(ValueError,'creator names/order'):build(self.root,self.manifest,self.out)

    def stable_record(self):
        from check_stable_promotion import scientific_path,RC_ARCHIVE_SHA
        self.rc_record();source=Path(__file__).resolve().parents[1]
        accepted=yaml.safe_load((source/'releases/v0.1.0-rc.1/manifest.yaml').read_text())
        extra=[r['path'] for r in accepted['members'] if scientific_path(r['path'])]
        extra+=['releases/v0.1.0-rc.1/manifest.yaml','evaluation/release/scope-disposition.yaml','docs/decisions/r1-scope-acceptance.md','CITATION.cff']
        for name in extra:
            target=self.root/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source/name,target)
        self.record.update(stage='accepted_stable',target_station='v0.1.0',accepted_candidate={'status':'ACCEPTED','archive_sha256':RC_ARCHIVE_SHA})
        self.refresh_stable_members()

    def refresh_stable_members(self):
        members=[]
        for path in sorted(p for p in self.root.rglob('*') if p.is_file()):
            data=path.read_bytes();members.append({'path':path.relative_to(self.root).as_posix(),'bytes':len(data),'sha256':digest(data),'git_blob_sha':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),'origin':'exact_source_commit_member','license':'CC-BY-4.0'})
        self.record['members']=members;self.record['member_path_digest_sha256']=digest(json.dumps({r['path']:r['sha256'] for r in members},sort_keys=True,separators=(',',':')).encode())
        self.manifest.write_text(yaml.safe_dump(self.record))

    def test_accepted_stable_roundtrip(self):
        self.stable_record();build(self.root,self.manifest,self.out)
        self.assertEqual(verify(self.out/'clariceptify-v0.1.0.zip',self.manifest,False)['stage'],'accepted_stable')

    def test_stable_without_acceptance_rejected(self):
        self.stable_record();self.record['accepted_candidate']['status']='NOT_ASSESSED';self.manifest.write_text(yaml.safe_dump(self.record))
        with self.assertRaisesRegex(ValueError,'exact accepted candidate'):build(self.root,self.manifest,self.out)

    def test_rehashed_scientific_change_rejected(self):
        self.stable_record();path=self.root/'model/concepts.yaml';path.write_bytes(path.read_bytes()+b'\n');self.refresh_stable_members()
        with self.assertRaisesRegex(ValueError,'Accepted scientific bytes changed'):build(self.root,self.manifest,self.out)

if __name__=='__main__':unittest.main()
