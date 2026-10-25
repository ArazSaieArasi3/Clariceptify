"""Create the current complete SVG from the exact recovered historical vector source.

No semantic or connector geometry change is allowed. The original stays private.
This is a controlled derivative, not the recovered historical generator.
"""
from pathlib import Path
import argparse, hashlib, json
import xml.etree.ElementTree as ET
import yaml
ROOT=Path(__file__).resolve().parents[1]
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)

def build(source):
    original=source.read_bytes()
    manifest=yaml.safe_load((ROOT/'model/diagrams/source-manifest.yaml').read_text())
    expected=next(r['sha256'] for r in manifest['inputs'] if r['source_id']=='SRC-SVG')
    if hashlib.sha256(original).hexdigest()!=expected: raise ValueError('Historical source digest mismatch')
    root=ET.fromstring(original)
    records={n:yaml.safe_load((ROOT/'model'/f'{n}.yaml').read_text())['records'] for n in ['concepts','domains','relations','generalizations']}
    concepts={c['label_en']:c for c in records['concepts']}; byid={c['id']:c for c in records['concepts']}
    edges={(byid[r['source_id']]['label_en'],r['label_en'],byid[r['target_id']]['label_en']):r['id'] for r in records['relations']}
    edges.update({(byid[r['child_id']]['label_en'],'specializes',byid[r['parent_id']]['label_en']):r['id'] for r in records['generalizations']})
    # Omit embedded third-party font programs. The font family is a metric-compatible
    # sans-serif fallback, not an included font licence or binary redistribution.
    for style in root.findall('{'+NS+'}style'):root.remove(style)
    for element in root.iter():
        if element.get('font-family')=='Arial':element.set('font-family','Arial, Liberation Sans, Helvetica, sans-serif')
        if element.get('class')=='node':element.set('data-registry-id',concepts[element.get('data-concept')]['id'])
        if element.get('class')=='edge':element.set('data-registry-id',edges[tuple(element.get(k) for k in ['data-source','data-relation','data-target'])])
        if element.text and element.text.startswith('CONCEPTIOM |'):
            element.text='CLARICEPTIFY | AN ONTOLOGY OF CONCEPTUALIZATION'
    root.find('{'+NS+'}title').text='Clariceptify | Release 1 | Complete conceptual model | Review candidate'
    for element in root.findall('{'+NS+'}text'):
        if element.text and element.text.startswith('Release 1 |'):
            element.text='R1 REVIEW CANDIDATE | 137 concepts | 174 associations | 122 generalizations | 20 subject domains + Foundations | diagram-r1.1 | 25 October 2026'
        if element.text and element.text.startswith('Complete vector master.'):
            element.text='Complete vector view; zoom required. Domain colors are not stereotypes. Scientific acceptance not established; native OntoUML validation not assessed.'
    root.find('{'+NS+'}desc').text='All 137 concepts and 296 relationships from the review-candidate specification. Human scientific acceptance and native OntoUML validation are not established.'
    root.set('data-artifact-version','diagram-r1.1')
    root.set('data-model-revision','input-r1-rev1')
    metadata=ET.SubElement(root,'{'+NS+'}metadata')
    metadata.text=json.dumps({'artifact_id':'CLR-DIAGRAM-FULL','diagram_revision':'diagram-r1.1','model_revision':'input-r1-rev1','historical_source_sha256':expected,'generator':'tools/derive_complete_diagram.py','model_sha256':{f'model/{n}.yaml':hashlib.sha256((ROOT/'model'/f'{n}.yaml').read_bytes()).hexdigest() for n in ['concepts','domains','relations','generalizations','constraints']},'semantic_approval':'not_established','native_ontouml_validation':'not_assessed'},sort_keys=True)
    target=ROOT/'model/diagrams/generated/full.svg';target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(ET.tostring(root,encoding='utf-8',xml_declaration=True))
    print(json.dumps({'path':str(target.relative_to(ROOT)),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'source_sha256':expected}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);a=p.parse_args();build(a.source)
