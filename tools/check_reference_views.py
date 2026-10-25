"""Reject stale source/output projections without regenerating away a failure."""
from pathlib import Path
import hashlib,json,csv,io
import yaml
ROOT=Path(__file__).resolve().parents[1]

def check(root=ROOT):
    counts={}
    for part in ('concepts','relations'):
        report=json.loads((root/'evaluation'/('reference-'+part+'.json')).read_text())
        for p,h in {**report['input_sha256'],**report['output_sha256']}.items():
            if hashlib.sha256((root/p).read_bytes()).hexdigest()!=h:raise ValueError('Stale reference binding: '+p)
        if hashlib.sha256((root/'tools/build_reference_pages.py').read_bytes()).hexdigest()!=report['generator_sha256']:raise ValueError('Changed reference adapter; regenerate and reassess')
        counts[part]=len(report['output_sha256'])
    for name in ('concepts','domains','relations','generalizations','constraints'):
        source=yaml.safe_load((root/'model'/f'{name}.yaml').read_text())['records']
        exported=list(csv.DictReader(io.StringIO((root/'docs/reference/exports'/f'{name}.csv').read_text())))
        if len(source)!=len(exported):raise ValueError('CSV record count mismatch: '+name)
        for actual,expected in zip(exported,source):
            for k,v in expected.items():
                value=actual[k] if isinstance(v,str) else json.loads(actual[k])
                if value!=v:raise ValueError('CSV source value mismatch: '+name+'/'+k)
    return {'status':'PASS','scope':'Current generator/source/output digests and direct model CSV correspondence; not semantic review','outputs':counts}

if __name__=='__main__':print(json.dumps(check(),indent=2))
