"""Validate declared candidate citation and license scope, not human acceptance."""
from pathlib import Path
import hashlib,json,re
import jsonschema,yaml

ROOT=Path(__file__).resolve().parents[1]
CREATORS=['Araz Saie Arasi','Hassan Haghighi','Hossein azgomi']
SCHEMA_SHA='0b8d22140da702d766df318dcff3a91af2f39521298dcf36d76315fd99cc169b'

def check(root=ROOT):
    schema_path=root/'tools/vendor/cff-1.2.0.schema.json'
    if hashlib.sha256(schema_path.read_bytes()).hexdigest()!=SCHEMA_SHA:
        raise ValueError('CFF schema differs from the attributed upstream bytes')
    citation=yaml.safe_load((root/'CITATION.cff').read_text())
    jsonschema.Draft7Validator(json.loads(schema_path.read_text()),format_checker=jsonschema.FormatChecker()).validate(citation)
    names=[' '.join([a['given-names'],a['family-names']]) for a in citation['authors']]
    if names!=CREATORS:raise ValueError('Citation creator names/order differ from owner decision')
    if citation['title']!='Clariceptify: An Ontology for Representing Conceptualization Knowledge':raise ValueError('Citation title mismatch')
    if citation['version']!='0.1.0-rc.1':raise ValueError('Unexpected candidate version')
    if citation['url']!='https://github.com/ArazSaieArasi3/Clariceptify':raise ValueError('Citation URL mismatch')
    if 'doi' in citation or 'date-released' in citation:raise ValueError('Unissued DOI/date must be omitted in this frozen candidate')
    if citation['license']!=['CC-BY-4.0','MIT']:raise ValueError('Scoped license identifiers differ')
    paths=['CITATION.cff','LICENSE','LICENSE-CC-BY-4.0','LICENSE-MIT','THIRD-PARTY-NOTICES.md',
           'docs/decisions/release-license.md','docs/decisions/artifact-creators.md','tools/vendor/cff-1.2.0.schema.json']
    for name in CREATORS:
        if name not in (root/'LICENSE').read_text() or name not in (root/'docs/decisions/artifact-creators.md').read_text():raise ValueError('Missing declared creator')
    return {'status':'PASS','creators':names,'version':citation['version'],'date_released':'omitted: candidate source, not asserted publication',
            'doi':'unassigned','cff_schema':'official 1.2.0, vendored with attribution',
            'license_scopes':{'research':'CC-BY-4.0','original_software':'MIT','third_party':'retains upstream rights'},
            'inputs_sha256':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths},
            'limits':'Checks metadata correspondence and schema, not rights in third-party works, detailed contributor roles or final package acceptance.'}

if __name__=='__main__':print(json.dumps(check(),indent=2))
