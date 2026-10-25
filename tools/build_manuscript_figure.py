"""Derive a selected, portrait manuscript view from authoritative R1 rows.

This selection is explanatory, not a replacement for the complete model diagram.
All labels, stereotypes, association ends and multiplicities come from registries.
"""
from pathlib import Path
from html import escape
import argparse, hashlib, json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def build(root, output):
    root, output = Path(root), Path(output)
    concepts = {r['id']: r for r in yaml.safe_load((root/'model/concepts.yaml').read_text())['records']}
    relations = {r['id']: r for r in yaml.safe_load((root/'model/relations.yaml').read_text())['records']}
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="720" height="970" viewBox="0 0 720 970"><title>Selected Clariceptify R1 conceptualization view</title><desc>Thirteen distinct classes and fourteen selected plain associations in three explanatory panels. Repeated classes have the same registry identity. All other classes, generalizations, associations and textual constraints are omitted from this selected view.</desc><rect width="720" height="970" fill="white"/>']
    nodes, edges, bindings = [], [], []

    def text(x, y, value, size=12, anchor='middle', weight='normal', halo=False):
        attrs=f'x="{x}" y="{y}" text-anchor="{anchor}" font-family="DejaVu Sans, sans-serif" font-size="{size}" font-weight="{weight}"'
        if halo:
            parts.append(f'<text {attrs} fill="white" stroke="white" stroke-width="4" stroke-linejoin="round">{escape(str(value))}</text>')
        parts.append(f'<text {attrs} fill="#172b38">{escape(str(value))}</text>')

    def node(key, number, x, y):
        cid = f'CLR-C{number:04d}'
        c = concepts[cid]
        nodes.append(cid)
        parts.append(f'<g data-registry-id="{cid}"><rect x="{x}" y="{y}" width="180" height="48" fill="#f1f5f8" stroke="#243b4b"/>')
        text(x+90, y+13, c['ontouml_stereotype'], 10.5)
        text(x+90, y+30, c['label_en'], 13, weight='bold')
        text(x+90, y+42, cid, 9)
        parts.append('</g>')
        bindings.append({'instance': key, 'concept_id': cid, 'label': c['label_en'], 'stereotype': c['ontouml_stereotype']})
        return cid

    def edge(number, source, target, points, label, start_card, end_card):
        rid = f'CLR-R{number:04d}'
        r = relations[rid]
        if r['source_id'] != source or r['target_id'] != target:
            raise ValueError(f'Selected association does not match registry: {rid}')
        parts.append(f'<g data-registry-id="{rid}"><polyline points="'+ ' '.join(f'{x},{y}' for x,y in points)+'" fill="none" stroke="#243b4b" stroke-width="1.2"/>')
        text(*label, r['label_en'], 11.5, halo=True)
        if r['ontouml_stereotype']:
            text(label[0], label[1]-14, r['ontouml_stereotype'], 10.5, halo=True)
        text(*start_card, r['source_multiplicity'], 10.5, halo=True)
        text(*end_card, r['target_multiplicity'], 10.5, halo=True)
        parts.append('</g>')
        edges.append({k:r[k] for k in ['id','label_en','source_id','target_id','source_multiplicity','target_multiplicity','ontouml_stereotype','connector']})

    text(20, 25, 'Selected conceptualization view', 18, 'start', 'bold')
    text(20, 45, 'Scientific core v0.1.0 · model input-r1-rev1 · explanatory selection', 11.5, 'start')
    text(20, 73, 'A  Agency, orientation and explicit content', 13, 'start', 'bold')
    a=node('A.conceptualizer',27,20,95);p=node('A.perspective',93,270,95);i=node('A.intention',61,520,95)
    e=node('A.episode',26,270,215);g=node('A.goal',54,520,215)
    c=node('A.artifact',19,270,335);el=node('A.element',22,20,335)
    edge(54,a,e,[(110,143),(110,239),(270,239)],(184,225),(126,160),(251,255))
    edge(42,e,p,[(330,215),(330,143)],(361,184),(312,204),(312,158))
    edge(51,e,i,[(420,215),(420,172),(565,172),(565,143)],(493,164),(436,204),(580,158))
    edge(89,i,g,[(660,143),(660,215)],(644,186),(681,158),(680,204))
    edge(48,e,c,[(360,263),(360,335)],(389,305),(345,278),(341,326))
    edge(32,c,el,[(270,359),(200,359)],(233,323),(252,375),(217,375))

    text(20, 420, 'B  Representation and interpretation', 13, 'start', 'bold')
    c=node('B.artifact',19,20,465);r=node('B.representation',101,270,465);ip=node('B.process',63,520,465);it=node('B.interpretation',62,520,580)
    edge(140,r,c,[(270,489),(200,489)],(235,453),(252,507),(217,507))
    edge(93,ip,r,[(520,489),(450,489)],(485,453),(502,507),(467,507))
    edge(94,ip,it,[(610,513),(610,580)],(650,552),(592,528),(590,573))

    text(20, 675, 'C  Evaluation activity, criterion and atomic finding', 13, 'start', 'bold')
    q=node('C.evaluation',97,20,700);er=node('C.result',40,520,700)
    c=node('C.artifact',19,20,855);ec=node('C.criterion',39,520,855)
    edge(131,q,er,[(200,724),(520,724)],(360,712),(217,740),(501,740))
    edge(130,q,c,[(110,748),(110,855)],(161,805),(91,764),(88,847))
    edge(129,q,ec,[(200,748),(270,795),(565,795),(565,855)],(401,785),(224,757),(546,847))
    edge(65,er,ec,[(640,748),(640,855)],(665,820),(623,764),(624,846))
    edge(62,er,c,[(700,724),(710,724),(710,933),(200,933),(200,879)],(408,923),(685,766),(218,892))
    text(20, 963, 'Plain associations; no arrowheads. Multiplicities label their respective ends.', 11, 'start')
    parts.append('</svg>')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(parts)+'\n')
    record={'schema_version':'1.0','status':'DERIVED_SELECTED_VIEW','scientific_core':'v0.1.0',
            'model_revision':'input-r1-rev1','unique_concepts':len(set(nodes)),
            'selected_associations':len(edges),'rendered_class_instances':len(nodes),
            'inputs':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in ['model/concepts.yaml','model/relations.yaml']},
            'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
            'nodes':bindings,'associations':edges,
            'omissions':'All other classes, all generalizations, all other associations and all 24 textual constraints. Repeated classes retain one identity. The complete 137-class/296-relationship model remains the release authority.',
            'claim_boundary':'Exact selected registry projection; no semantic, native OntoUML or independent review acceptance.'}
    output.with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
    return record


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=build(a.root,a.output);print(json.dumps({k:v for k,v in result.items() if k not in ['nodes','associations']},indent=2))
