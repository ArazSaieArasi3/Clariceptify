"""Validate exact membership/bytes before extracting and checking a preparation package."""
from pathlib import Path
import argparse,hashlib,importlib.metadata,json,os,site,subprocess,sys,tempfile,zipfile
import yaml
from build_release import safe_path,digest,MANIFEST_PATH,package_record
ROOT=Path(__file__).resolve().parents[1]
CHECKERS=['check_repository_language','check_schemas','check_model_structure','check_requirements','check_source_support','check_traceability','check_bootstrap','check_reference_views','check_conceptualization_fixtures','check_review_state','check_publication_metadata']

def verify(archive_path,manifest_path,run_checks=True):
    raw=Path(manifest_path).read_bytes();manifest=yaml.safe_load(raw)
    registered={r['path']:r for r in manifest['members']}
    if len(registered)!=len(manifest['members']):raise ValueError('Duplicate trusted manifest member')
    expected=set(registered)|{MANIFEST_PATH,'PACKAGE-MANIFEST.json','SHA256SUMS'}
    with zipfile.ZipFile(archive_path) as archive:
        names=archive.namelist()
        if len(names)!=len(set(names)) or set(names)!=expected:raise ValueError('Unexpected, missing or duplicate archive membership')
        for info in archive.infolist():
            safe_path(info.filename)
            if info.external_attr>>16!=0o100644:raise ValueError('Unexpected member mode')
        files={name:archive.read(name) for name in names}
    if files[MANIFEST_PATH]!=raw:raise ValueError('Embedded source manifest differs from the trusted manifest')
    envelope=json.loads(files['PACKAGE-MANIFEST.json'])
    if envelope!=package_record(manifest,raw):raise ValueError('Package envelope mismatch')
    for name,row in registered.items():
        if digest(files[name])!=row['sha256'] or len(files[name])!=row['bytes']:raise ValueError('Member digest differs: '+name)
    expected_sums=''.join(digest(data)+'  '+name+'\n' for name,data in sorted(files.items()) if name!='SHA256SUMS').encode()
    if files['SHA256SUMS']!=expected_sums:raise ValueError('Internal checksum inventory differs')
    results={}
    if run_checks:
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)/'source';root.mkdir();home=Path(temp)/'empty-home';home.mkdir()
            for name,data in files.items():
                target=root/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
            # No Git checkout, raw input access, connector/session lookup or network call.
            env={k:v for k,v in os.environ.items() if k not in ('PYTHONPATH','PYTHONHOME','GITHUB_TOKEN','GH_TOKEN')}
            env.update(HOME=str(home),PYTHONUSERBASE=site.USER_BASE)
            # The current interpreter's declared installed dependencies are reused.
            # Reuse the explicitly declared runtime dependency location while
            # keeping HOME empty; this is not a fresh OS/runtime assertion.
            for name in CHECKERS:
                command=[sys.executable,str(root/'tools'/f'{name}.py')]
                if name=='check_repository_language':command+=sorted(files)
                run=subprocess.run(command,cwd=root,env=env,capture_output=True,text=True,timeout=180)
                try:record=json.loads(run.stdout)
                except json.JSONDecodeError:raise ValueError(name+': '+(run.stderr or run.stdout)[-2000:])
                if run.returncode or record.get('status')!='PASS':raise ValueError('Extracted check failed: '+name)
                results[name]={'status':'PASS','result_sha256':digest(run.stdout.encode())}
    return {'status':'PASS','stage':manifest['stage'],'publication_status':'NOT_ASSERTED_BY_READBACK','archive_sha256':digest(Path(archive_path).read_bytes()),'source_manifest_sha256':digest(raw),'registered_source_members':len(registered),'archive_members':len(files),'checks':results,'environment':'Fresh temporary extraction and empty HOME; no Git/private raw inputs/network; declared dependencies already installed in current Python runtime','runtime':{'python':sys.version.split()[0],'PyYAML':importlib.metadata.version('PyYAML'),'jsonschema':importlib.metadata.version('jsonschema')},'limitations':['Archive verification does not establish actual publication or final owner acceptance.','Fresh file tree is not a newly provisioned operating system or independent expert validation.']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('archive',type=Path);p.add_argument('--manifest',type=Path,default=ROOT/MANIFEST_PATH);p.add_argument('--output',type=Path);a=p.parse_args();result=verify(a.archive,a.manifest)
    content=json.dumps(result,indent=2)+'\n'
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(content)
    print(content)
