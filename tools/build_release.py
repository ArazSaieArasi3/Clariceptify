"""Build an exact preparation-only package; never publish or manufacture RC approval."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,io,json,zipfile
import yaml
ROOT=Path(__file__).resolve().parents[1]
MANIFEST_PATH='releases/v0.1.0-rc.1/manifest.yaml'

def digest(data):return hashlib.sha256(data).hexdigest()
def encode(value):return (json.dumps(value,indent=2,sort_keys=True)+'\n').encode()
def safe_path(name):
    p=PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or '\\' in name or str(p)!=name or not name or name=='.' or '\x00' in name or ':' in p.parts[0]:raise ValueError('Unsafe member path: '+name)
    return p

def build(root,manifest_path,output):
    root=Path(root).resolve();output=Path(output).resolve()
    if output.is_relative_to(root):raise ValueError('Keep generated package outside its source tree')
    raw=Path(manifest_path).read_bytes();manifest=yaml.safe_load(raw)
    if manifest['stage']!='preparation_only' or manifest['publication_eligible'] is not False:
        raise ValueError('This adapter builds preparation packages only; final RC authorization is separate')
    files={}
    for row in manifest['members']:
        name=row['path'];safe_path(name)
        if name in files:raise ValueError('Duplicate manifest member')
        source=root/name
        if source.is_symlink() or not source.resolve().is_relative_to(root):raise ValueError('Symlink/path escape is not a payload file')
        data=source.read_bytes()
        if digest(data)!=row['sha256'] or len(data)!=row['bytes']:raise ValueError('Input differs from manifest: '+name)
        files[name]=data
    if MANIFEST_PATH in files or 'PACKAGE-MANIFEST.json' in files or 'SHA256SUMS' in files:raise ValueError('Recursive/envelope member in source inventory')
    package={'schema_version':'1.0','package_kind':'local_engineering_preparation','source_manifest_sha256':digest(raw),'publication_eligible':False,'base_source_commit':manifest['base_source_commit'],'snapshot_binding':manifest['snapshot_binding'],'model_version':manifest['artifact_versions']['model'],'diagram_version':manifest['artifact_versions']['diagram'],'members':manifest['members'],'excluded_families':manifest['excluded_families'],'pending_gates':manifest['pending_gates']}
    files[MANIFEST_PATH]=raw
    files['PACKAGE-MANIFEST.json']=encode(package)
    files['SHA256SUMS']=''.join(digest(data)+'  '+name+'\n' for name,data in sorted(files.items())).encode()
    stream=io.BytesIO()
    with zipfile.ZipFile(stream,'w',compression=zipfile.ZIP_STORED) as archive:
        for name,data in sorted(files.items()):
            info=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_STORED;info.external_attr=0o100644<<16
            archive.writestr(info,data)
    output.mkdir(parents=True,exist_ok=True)
    archive_path=output/'clariceptify-r1-preparation.zip';archive_path.write_bytes(stream.getvalue())
    (output/'PACKAGE-MANIFEST.json').write_bytes(files['PACKAGE-MANIFEST.json'])
    (output/'SHA256SUMS').write_text(digest(archive_path.read_bytes())+'  '+archive_path.name+'\n'+digest(files['PACKAGE-MANIFEST.json'])+'  PACKAGE-MANIFEST.json\n')
    return {'status':'PASS','publication_status':'BLOCKED','stage':'preparation_only','members':len(manifest['members']),'source_manifest_sha256':digest(raw),'archive_sha256':digest(archive_path.read_bytes()),'archive_bytes':archive_path.stat().st_size,'pending_gates':manifest['pending_gates']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--manifest',type=Path,default=ROOT/MANIFEST_PATH);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    print(json.dumps(build(a.root,a.manifest,a.output),indent=2))
