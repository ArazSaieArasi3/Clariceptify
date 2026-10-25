"""Reproduce an exact dispositioned stable request before separate publication."""
from pathlib import Path
import argparse,json,shutil,subprocess
import yaml
from build_release import build,digest
from readback_release import verify,CHECKERS
from check_stable_promotion import check as check_promotion

def prepare(metadata,source,output,ci_record):
    metadata=Path(metadata).resolve();source=Path(source).resolve();output=Path(output).resolve()
    station=metadata/'releases/v0.1.0'
    request=json.loads((station/'request.json').read_text())
    manifest=yaml.safe_load((station/'manifest.yaml').read_text())
    readiness=yaml.safe_load((metadata/'evaluation/release/stable-readiness.yaml').read_text())
    actual=subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD'],text=True).strip()
    if actual!=request['source_commit'] or actual!=manifest['source_commit']:raise ValueError('Source differs from reviewed request')
    if subprocess.check_output(['git','-C',str(source),'status','--porcelain'],text=True).strip():raise ValueError('Source checkout is dirty')
    if digest((station/'manifest.yaml').read_bytes())!=request['manifest_sha256']:raise ValueError('Manifest differs from request')
    if digest((metadata/'evaluation/release/stable-readiness.yaml').read_bytes())!=request['readiness_sha256']:raise ValueError('Readiness differs from request')
    if readiness['status']!='PASS_FOR_STABLE' or readiness['source_commit']!=actual or readiness['blockers']:raise ValueError('Stable readiness has blockers')
    ci=json.loads(Path(ci_record).read_text())
    if ci['id']!=request['source_ci_run_id'] or ci['head_sha']!=actual or ci['name']!='Public integrity' or ci['event']!='push' or ci['head_branch']!='main' or ci['conclusion']!='success':raise ValueError('Actual source CI differs')
    promotion=check_promotion(source)
    result=build(source,station/'manifest.yaml',output)
    if result['archive_sha256']!=request['archive_sha256']:raise ValueError('Rebuilt archive differs from reviewed archive')
    readback=verify(output/'clariceptify-v0.1.0.zip',station/'manifest.yaml')
    if set(readback['checks'])!=set(CHECKERS) or any(x['status']!='PASS' for x in readback['checks'].values()):raise ValueError('Incomplete readback checks')
    (output/'READBACK.json').write_text(json.dumps(readback,indent=2)+'\n')
    (output/'PROMOTION.json').write_text(json.dumps(promotion,indent=2)+'\n')
    (output/'SOURCE-CI.json').write_text(json.dumps(ci,indent=2)+'\n')
    for original,name in [(station/'manifest.yaml','SOURCE-MANIFEST.yaml'),(metadata/'evaluation/release/stable-readiness.yaml','STABLE-READINESS.yaml'),(source/'evaluation/release/scope-disposition.yaml','SCOPE-DISPOSITION.yaml'),(source/'CITATION.cff','CITATION.cff')]:shutil.copyfile(original,output/name)
    files=sorted(p for p in output.iterdir() if p.name!='SHA256SUMS')
    (output/'SHA256SUMS').write_text(''.join(digest(p.read_bytes())+'  '+p.name+'\n' for p in files))
    return {'status':'PASS','source_commit':actual,'archive_sha256':result['archive_sha256'],'scientific_members_unchanged':promotion['scientific_members_unchanged'],'checks':len(CHECKERS),'publication':'not performed by this command'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--metadata',type=Path,required=True);p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--ci-record',type=Path,required=True);a=p.parse_args()
    print(json.dumps(prepare(a.metadata,a.source,a.output,a.ci_record),indent=2))
