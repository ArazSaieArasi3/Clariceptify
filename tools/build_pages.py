"""Build mutable current docs and frozen routes using each route's exact source."""
from pathlib import Path
import argparse,hashlib,io,json,re,subprocess,sys,tarfile,tempfile
import yaml
from build_documentation import build,encoded,digest

ROOT=Path(__file__).resolve().parents[1]
def build_pages(root,output,source_ref):
    root=Path(root).resolve();output=Path(output).resolve()
    if output.is_relative_to(root):raise ValueError('Keep generated Pages outside source')
    config=yaml.safe_load((root/'docs/publication/versions.yaml').read_text())
    current=build(root,output/'current',source_ref,config['current_documentation_version'])
    frozen=[]
    for item in config['frozen']:
        ref=item['source_commit']
        if not re.fullmatch('[0-9a-f]{40}',ref):raise ValueError('Frozen documentation requires an immutable commit')
        with tempfile.TemporaryDirectory() as temp:
            raw=subprocess.check_output(['git','-C',str(root),'archive','--format=tar',ref])
            with tarfile.open(fileobj=io.BytesIO(raw)) as archive:archive.extractall(temp,filter='data')
            folder=output/'releases'/item['version']
            subprocess.run([sys.executable,str(Path(temp)/'tools/build_documentation.py'),'--root',temp,'--output',str(folder),'--source-ref',ref,'--version',item['version']],check=True,capture_output=True,text=True)
        manifest=json.loads((folder/'publication-manifest.json').read_text())
        frozen.append({'version':item['version'],'source_commit':ref,'route':'releases/'+item['version']+'/','manifest_sha256':digest((folder/'publication-manifest.json').read_bytes()),'source_path_digest_sha256':manifest['source_path_digest_sha256']})
    output.mkdir(parents=True,exist_ok=True)
    (output/'.nojekyll').write_text('')
    links=''.join('<li><a href="'+x['route']+'index.html">Frozen '+x['version']+'</a></li>' for x in frozen)
    (output/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0; url=current/index.html"><title>Clariceptify documentation</title></head><body><h1>Clariceptify documentation</h1><p><a href="current/index.html">Current documentation</a></p><ul>'+links+'</ul></body></html>')
    record={'schema_version':'1.0','artifact_state':'BUILT','scientific_core':'v0.1.0','current':{'version':config['current_documentation_version'],'source_commit':source_ref,'route':'current/','manifest_sha256':digest((output/'current/publication-manifest.json').read_bytes()),'source_path_digest_sha256':current['source_path_digest_sha256']},'frozen':frozen,'publication_boundary':'The actual deployment/run and public readback establish publication; this manifest binds the built artifacts.'}
    (output/'publication-manifest.json').write_bytes(encoded(record));return record

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--output',type=Path,required=True);p.add_argument('--source-ref',required=True);a=p.parse_args();print(json.dumps(build_pages(a.root,a.output,a.source_ref),indent=2))
