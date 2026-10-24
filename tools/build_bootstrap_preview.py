"""Build and read back the frozen engineering checkpoint, without publication."""
from pathlib import Path
import argparse,json,hashlib,subprocess,tempfile,zipfile,io

ROOT=Path(__file__).resolve().parents[1]


def git(*args):return subprocess.check_output(['git','-C',str(ROOT),*args])


def build(request_path,output):
    request=json.loads(Path(request_path).read_text())
    sha=request['source_commit'];tag=request['tag']
    if tag!='v0.1.0-alpha.1' or sha!='223df578777afa38743fa20c8c33ace78a8fbfd6':
        raise ValueError('This builder is restricted to the approved first engineering checkpoint')
    tree=git('rev-parse',sha+'^{tree}').decode().strip()
    if tree!=request['source_tree']:raise ValueError('Source tree mismatch')
    names=git('ls-tree','-r','--name-only',sha).decode().splitlines()
    if len(names)!=32:raise ValueError('Unexpected bootstrap membership')
    files={name:git('show',sha+':'+name) for name in names}
    if any(name.startswith('/') or '..' in Path(name).parts or name.endswith(('.docx','.pdf','.svg','.html')) for name in files):
        raise ValueError('Unexpected path or raw document in engineering checkpoint')
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)
        for name,content in files.items():
            p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(content)
        run=subprocess.run(['python',str(root/'tools/check_bootstrap.py')],check=True,capture_output=True,text=True)
        check=json.loads(run.stdout)
        if check['status']!='PASS':raise ValueError('Frozen-source check failed')
    manifest={'tag':tag,'source_commit':sha,'source_tree':tree,'package_kind':'engineering-bootstrap-prerelease',
              'semantic_model_records_included':False,'stable_semantic_release':False,'doi':None,
              'scope':'R1 contracts, schemas and candidate migration preparation only',
              'limits':['no accepted conceptual-model release','no formal or independent validation','raw inputs not redistributed','reuse license remains pending'],
              'frozen_check':{'status':check['status'],'checks_passed':check['checks_passed']},
              'files':{name:hashlib.sha256(content).hexdigest() for name,content in sorted(files.items())}}
    manifest_bytes=(json.dumps(manifest,indent=2,sort_keys=True)+'\n').encode()
    files['PACKAGE-MANIFEST.json']=manifest_bytes
    files['SHA256SUMS']=(''.join(hashlib.sha256(b).hexdigest()+'  '+name+'\n' for name,b in sorted(files.items()))).encode()
    stream=io.BytesIO()
    with zipfile.ZipFile(stream,'w',compression=zipfile.ZIP_STORED) as z:
        for name,content in sorted(files.items()):
            info=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_STORED;info.external_attr=0o100644<<16
            z.writestr(info,content)
    payload=stream.getvalue()
    with zipfile.ZipFile(io.BytesIO(payload)) as z:
        if z.testzip() is not None or set(z.namelist())!=set(files):raise ValueError('Archive readback failed')
        if any(z.read(name)!=value for name,value in files.items()):raise ValueError('Archive byte mismatch')
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    assets={f'clariceptify-{tag}-bootstrap.zip':payload,'PACKAGE-MANIFEST.json':manifest_bytes}
    for name,b in assets.items():(output/name).write_bytes(b)
    (output/'SHA256SUMS').write_text(''.join(hashlib.sha256(b).hexdigest()+'  '+name+'\n' for name,b in sorted(assets.items())))
    return {'status':'PASS','tag':tag,'source_commit':sha,'files':len(names),'archive_members':len(files),
            'checks_passed':check['checks_passed'],'assets':{name:hashlib.sha256((output/name).read_bytes()).hexdigest() for name in [*assets,'SHA256SUMS']}}


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('request');ap.add_argument('output');a=ap.parse_args()
    print(json.dumps(build(a.request,a.output),indent=2))
