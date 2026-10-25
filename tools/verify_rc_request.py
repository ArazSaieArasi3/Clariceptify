"""Build/check an already reviewed exact RC request before separate publication."""
from pathlib import Path
import argparse,json,shutil,subprocess
import yaml
from build_release import build,digest,MANIFEST_PATH
from readback_release import verify,CHECKERS

def prepare(metadata,source,output,ci_record):
    metadata=Path(metadata).resolve();source=Path(source).resolve();output=Path(output).resolve()
    station=metadata/'releases/v0.1.0-rc.1'
    request=json.loads((station/'request.json').read_text())
    manifest=yaml.safe_load((station/'manifest.yaml').read_text())
    readiness=yaml.safe_load((metadata/'evaluation/release/rc-readiness.yaml').read_text())
    actual=subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD'],text=True).strip()
    if actual!=request['source_commit'] or actual!=manifest['source_commit']:raise ValueError('Source commit differs from reviewed request')
    if subprocess.check_output(['git','-C',str(source),'status','--porcelain'],text=True).strip():raise ValueError('Source checkout is dirty')
    if digest((station/'manifest.yaml').read_bytes())!=request['manifest_sha256']:raise ValueError('Manifest differs from reviewed request')
    if digest((metadata/'evaluation/release/rc-readiness.yaml').read_bytes())!=request['readiness_sha256']:raise ValueError('Readiness differs from reviewed request')
    if readiness['status']!='PASS_FOR_RC' or readiness['source_commit']!=actual or readiness['rc_blockers']:raise ValueError('Readiness gate does not permit this RC')
    ci=json.loads(Path(ci_record).read_text())
    if ci['id']!=request['source_ci_run_id'] or ci['head_sha']!=actual or ci['name']!='Public integrity' or ci['event']!='push' or ci['head_branch']!='main' or ci['conclusion']!='success':raise ValueError('Actual source CI does not match the request')
    result=build(source,station/'manifest.yaml',output)
    archive=output/'clariceptify-v0.1.0-rc.1.zip'
    if result['archive_sha256']!=request['archive_sha256']:raise ValueError('Rebuilt archive differs from reviewed archive')
    readback=verify(archive,station/'manifest.yaml')
    if set(readback['checks'])!=set(CHECKERS) or any(x['status']!='PASS' for x in readback['checks'].values()):raise ValueError('Readback did not run every declared check')
    (output/'READBACK.json').write_text(json.dumps(readback,indent=2)+'\n')
    shutil.copyfile(station/'manifest.yaml',output/'SOURCE-MANIFEST.yaml')
    shutil.copyfile(metadata/'evaluation/release/rc-readiness.yaml',output/'RC-READINESS.yaml')
    (output/'SOURCE-CI.json').write_text(json.dumps(ci,indent=2)+'\n')
    files=sorted(p for p in output.iterdir() if p.name!='SHA256SUMS')
    (output/'SHA256SUMS').write_text(''.join(digest(p.read_bytes())+'  '+p.name+'\n' for p in files))
    return {'status':'PASS','source_commit':actual,'archive_sha256':result['archive_sha256'],'checks':len(CHECKERS),'publication':'not performed by this command'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--metadata',type=Path,required=True);p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--ci-record',type=Path,required=True);a=p.parse_args()
    print(json.dumps(prepare(a.metadata,a.source,a.output,a.ci_record),indent=2))
