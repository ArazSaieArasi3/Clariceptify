"""Require exact accepted scientific bytes and actual scope acceptance for v0.1.0."""
from pathlib import Path
import hashlib,json
import yaml

ROOT=Path(__file__).resolve().parents[1]
RC_MANIFEST_SHA='48c4dc97578233d3a7b124e17e0f14db4dbe1db432a60ff4a9becedc0b0e3a83'
RC_ARCHIVE_SHA='b27b14c9ec602734085762c4472938e55c2b33614ccd1fe0ea7240720efac7c7'

def scientific_path(name):
    return name.startswith(('model/','requirements/','evidence/','traceability/','docs/reference/','docs/examples/','docs/research/','evaluation/fixtures/','evaluation/diagrams/')) or name in {'docs/decisions/r1-scope.md','evaluation/conceptualization-fixtures.json','evaluation/conceptualization-positive.json'}

def check(root=ROOT):
    raw=(root/'releases/v0.1.0-rc.1/manifest.yaml').read_bytes()
    if hashlib.sha256(raw).hexdigest()!=RC_MANIFEST_SHA:raise ValueError('Accepted RC manifest identity differs')
    manifest=yaml.safe_load(raw)
    disposition=yaml.safe_load((root/'evaluation/release/scope-disposition.yaml').read_text())
    if disposition.get('status')!='ACCEPTED' or not disposition.get('actual_owner_decision') or disposition.get('archive_sha256')!=RC_ARCHIVE_SHA or disposition.get('manifest_sha256')!=RC_MANIFEST_SHA:
        raise ValueError('Actual exact-candidate scope acceptance is required')
    decision=root/disposition['actual_decision_record']
    if not decision.is_file() or RC_ARCHIVE_SHA not in decision.read_text():raise ValueError('Actual acceptance record missing exact identity')
    rows=[r for r in manifest['members'] if scientific_path(r['path'])]
    for row in rows:
        if hashlib.sha256((root/row['path']).read_bytes()).hexdigest()!=row['sha256']:raise ValueError('Accepted scientific bytes changed: '+row['path'])
    return {'status':'PASS','accepted_candidate':'v0.1.0-rc.1','accepted_archive_sha256':RC_ARCHIVE_SHA,'accepted_manifest_sha256':RC_MANIFEST_SHA,
            'scientific_members_unchanged':len(rows),'scientific_files_sha256':{r['path']:r['sha256'] for r in rows},
            'scope':'Exact original scientific bytes; actual owner package scope acceptance, not independent semantic/expert acceptance.'}

if __name__=='__main__':print(json.dumps(check(),indent=2))
