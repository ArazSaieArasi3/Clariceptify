#!/usr/bin/env python3
"""Read-only current SVG/registry correspondence audit (not OntoUML validation).
Requires PyYAML and lxml. Outputs detailed JSON to stdout; exits 1 on mismatch.
Geometry checks assume the original SVG's untransformed node/edge coordinates,
M/C path grammar and rectangular polygons. Unsupported geometry fails explicitly.
"""
import copy
import argparse, collections, hashlib, json, math, re
from pathlib import Path
import yaml
from lxml import etree as ET
NS={'s':'http://www.w3.org/2000/svg'}
NUM=r'[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?'
def numbers(s): return [float(x) for x in re.findall(NUM,s)]
def points(s):
    a=numbers(s)
    if len(a)%2: raise ValueError('Odd coordinate count')
    return list(zip(a[::2],a[1::2]))
def texts(e): return [''.join(t.itertext()) for t in e.xpath('.//s:text',namespaces=NS)]
def edge_view(root,edge):
    merged=copy.deepcopy(edge)
    for label in root.xpath('//s:g[@class="edge-labels"]',namespaces=NS):
        if label.get('data-edge-ref')==edge.get('id'):
            for child in label:merged.append(copy.deepcopy(child))
    return merged

def norm(s): return (s or '').replace('«','').replace('»','').replace('—','').strip()
def boundary_distance(p,box):
    x,y=p; x0,y0,x1,y1=box
    dx=max(x0-x,0,x-x1);dy=max(y0-y,0,y-y1)
    return math.hypot(dx,dy) if dx or dy else min(x-x0,x1-x,y-y0,y1-y)
def audit(repo, inputs, svg_override=None):
    def records(name):return yaml.safe_load((repo/'model'/f'{name}.yaml').read_text())['records']
    cs,rs,gs,ds=[records(n) for n in ['concepts','relations','generalizations','domains']]
    concepts={c['label_en']:c for c in cs};byid={c['id']:c for c in cs};domains={d['id']:d for d in ds}
    svg=svg_override or inputs/'Conceptiom_Release_1_OntoUML_Full.svg';root=ET.parse(str(svg));nodes=root.xpath('//s:g[@class="node"]',namespaces=NS);edges=[edge_view(root,e) for e in root.xpath('//s:g[@class="edge"]',namespaces=NS)]
    failures=[]; nr=[];er=[];boxes={};colors=collections.defaultdict(set)
    def check(result,name,ok):
        result.setdefault('checks',{})[name]=bool(ok)
        if not ok:failures.append({'svg_id':result.get('svg_id'),'check':name})
    for node in nodes:
        label=node.get('data-concept');c=concepts.get(label);r={'svg_id':node.get('id'),'label':label,'registry_id':c['id'] if c else None,'visible_text':texts(node)}
        check(r,'registered_label',c is not None)
        if c:
            check(r,'stable_id_binding',node.get('data-registry-id')==c['id'])
            check(r,'visible_label',label == ' '.join(t for t in r['visible_text'] if t != c['ontouml_stereotype']));check(r,'visible_stereotype',c['ontouml_stereotype'] in r['visible_text']);check(r,'stereotype_attribute',norm(node.get('data-stereotype'))==norm(c['ontouml_stereotype']));check(r,'domain_attribute',node.get('data-domain')==domains[c['primary_domain_id']]['label_en'])
        polygons=node.xpath('.//s:polygon',namespaces=NS)
        check(r,'single_box_polygon',len(polygons)==1)
        check(r,'no_local_transform',not node.xpath('.//*[@transform]') and not node.get('transform'))
        if len(polygons)==1:
            ps=points(polygons[0].get('points'));xs=[p[0] for p in ps];ys=[p[1] for p in ps];box=[min(xs),min(ys),max(xs),max(ys)];boxes[label]=box;r['box']=box;r['fill']=polygons[0].get('fill');colors[node.get('data-domain')].add(r['fill']);check(r,'rectangular_box',all(x in (box[0],box[2]) and y in (box[1],box[3]) for x,y in ps))
        nr.append(r)
    associations={(byid[r['source_id']]['label_en'],r['label_en'],byid[r['target_id']]['label_en']):r for r in rs}
    generals={(byid[r['child_id']]['label_en'],'specializes',byid[r['parent_id']]['label_en']):r for r in gs}
    seen=collections.Counter()
    for edge in edges:
        key=tuple(edge.get(k) for k in ['data-source','data-relation','data-target']);general=edge.get('data-stereotype')=='Generalization';reg=(generals if general else associations).get(key);seen[key]+=1
        r={'svg_id':edge.get('id'),'ordered_key':key,'kind':'generalization' if general else 'association','registry_id':reg['id'] if reg else None,'visible_text':texts(edge)}
        check(r,'ordered_registry_binding',reg is not None);check(r,'stable_id_binding',reg is not None and edge.get('data-registry-id')==reg['id']);check(r,'no_local_transform',not edge.xpath('.//*[@transform]') and not edge.get('transform'))
        paths=edge.xpath('.//s:path[not(@class="label-leader")]',namespaces=NS);polys=edge.xpath('.//s:polygon',namespaces=NS);check(r,'single_path',len(paths)==1)
        if len(paths)==1:
            d=paths[0].get('d');check(r,'supported_path_commands',not re.sub(NUM+'|[MC,\\s]','',d));ps=points(d);r['path_start']=ps[0];r['path_end']=ps[-1]
            if key[0] in boxes:
                r['source_boundary_distance']=boundary_distance(ps[0],boxes[key[0]]);check(r,'path_starts_at_source',r['source_boundary_distance']<0.02)
            if not general and key[2] in boxes:
                r['target_boundary_distance']=boundary_distance(ps[-1],boxes[key[2]]);check(r,'path_ends_at_target',r['target_boundary_distance']<0.02)
        if general:
            check(r,'one_hollow_triangle',len(polys)==1 and polys[0].get('fill') in ('none','white'));check(r,'no_association_labels',not r['visible_text'])
            if len(polys)==1 and key[2] in boxes:
                ps=points(polys[0].get('points'));r['triangle_points']=ps;r['triangle_parent_boundary_distance']=min(boundary_distance(p,boxes[key[2]]) for p in ps);check(r,'triangle_at_parent',r['triangle_parent_boundary_distance']<0.02)
        elif reg:
            check(r,'no_arrow_polygon',not polys);check(r,'association_label',reg['label_en'] == ' '.join(''.join(t.itertext()) for t in edge.xpath('.//s:text[@text-anchor="start"]',namespaces=NS) if ''.join(t.itertext()) != reg['ontouml_stereotype']));check(r,'stereotype_attribute',norm(edge.get('data-stereotype'))==norm(reg['ontouml_stereotype']));check(r,'visible_stereotype',not reg['ontouml_stereotype'] or reg['ontouml_stereotype'] in r['visible_text'])
            mult=edge.xpath('.//s:text[@text-anchor="middle"]',namespaces=NS);r['multiplicity_labels']=[{'text':''.join(t.itertext()),'x':t.get('x'),'y':t.get('y')} for t in mult];r['expected_multiplicities_target_then_source']=[reg['target_multiplicity'],reg['source_multiplicity']];check(r,'multiplicities_target_then_source',[m['text'] for m in r['multiplicity_labels']]==r['expected_multiplicities_target_then_source'])
        er.append(r)
    aggregate={}
    metadata=json.loads(root.find('s:metadata',NS).text)
    check(aggregate,'historical_source_binding',metadata.get('historical_source_sha256')==next(r['sha256'] for r in yaml.safe_load((repo/'model/diagrams/source-manifest.yaml').read_text())['inputs'] if r['source_id']=='SRC-SVG') and metadata.get('artifact_id')=='CLR-DIAGRAM-FULL')
    check(aggregate,'visible_candidate_state','R1 REVIEW CANDIDATE' in ' '.join(texts(root)) and 'Review candidate' in root.find('s:title',NS).text and 'approved specification' not in root.find('s:desc',NS).text)
    check(aggregate,'candidate_state',metadata.get('semantic_approval')=='not_established' and metadata.get('native_ontouml_validation')=='not_assessed')
    check(aggregate,'revision_binding',metadata.get('diagram_revision')==root.getroot().get('data-artifact-version') and metadata.get('diagram_revision') in ('diagram-r1.1','diagram-r1.2') and metadata.get('model_revision')==root.getroot().get('data-model-revision')=='input-r1-rev1')
    check(aggregate,'model_hash_bindings',all(hashlib.sha256((repo/path).read_bytes()).hexdigest()==digest for path,digest in metadata['model_sha256'].items()) and set(metadata['model_sha256'])=={'model/'+n+'.yaml' for n in ['concepts','domains','relations','generalizations','constraints']})
    check(aggregate,'node_set_exact',collections.Counter(n.get('data-concept') for n in nodes)==collections.Counter(list(concepts)))
    check(aggregate,'edge_set_exact',seen==collections.Counter(list(associations)+list(generals)))
    check(aggregate,'all_domain_colors_single',all(len(v)==1 for v in colors.values()))
    check(aggregate,'domain_colors_distinct',len(set(c for v in colors.values() for c in v))==len(ds)==len(colors))
    if metadata.get('diagram_revision')=='diagram-r1.2':
        graph=root.xpath('//s:g[@class="graph"]',namespaces=NS)[0]
        layers=graph.xpath('./s:g[@id="edge-label-layer"]',namespaces=NS)
        labels=root.xpath('//s:g[@class="edge-labels"]',namespaces=NS)
        originals=root.xpath('//s:g[@class="edge"]',namespaces=NS)
        expected={e.get('id'):e.get('data-registry-id') for e in originals if e.get('data-stereotype')!='Generalization'}
        check(aggregate,'label_layer_identity',len(layers)==1 and len(labels)==len(expected) and collections.Counter(l.get('data-edge-ref') for l in labels)==collections.Counter(expected.keys()) and all(l.get('data-registry-id')==expected.get(l.get('data-edge-ref')) and l.getparent() is layers[0] and not l.get('transform') for l in labels))
        check(aggregate,'label_layer_order',len(layers)==1 and all(graph.index(e)<graph.index(layers[0]) for e in originals) and all(graph.index(n)>graph.index(layers[0]) for n in root.xpath('//s:g[@class="node"]',namespaces=NS)))
    alltext=' '.join(texts(root));legend=[]
    for d in ds:
        r={'registry_id':d['id'],'label':d['label_en']};check(r,'legend_description_present',d['description'] in alltext);legend.append(r)
    files=[]
    for p in ([svg] if svg_override else sorted(inputs.iterdir())):
        if not p.is_file():continue
        b=p.read_bytes();r={'filename':p.name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
        if p.suffix=='.pdf':
            import fitz
            with fitz.open(p) as doc:r.update(pages=len(doc),page_sizes_points=[[page.rect.width,page.rect.height] for page in doc],metadata=doc.metadata)
        files.append(r)
    return {'status':'FAIL' if failures else 'PASS','scope':'Current SVG structural and endpoint-geometry correspondence, not scientific or native OntoUML validation; multiplicity association follows original target-then-source XML ordering, not rendered visual proximity; no exhaustive PDF/atlas parity or occlusion check.','files':files,'counts':{'nodes':len(nodes),'edges':len(edges),'associations':len(rs),'generalizations':len(gs)},'aggregate':aggregate,'nodes':nr,'edges':er,'domains':legend,'domain_colors':{k:sorted(v) for k,v in colors.items()},'approval_description':root.find('s:desc',NS).text,'failures':failures}
if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('--svg',type=Path)
    a=p.parse_args()
    svg=a.svg or a.repo/'model/diagrams/generated/full.svg'
    r=audit(a.repo, svg.parent, svg)
    print(json.dumps(r,indent=2))
    raise SystemExit(r['status']!='PASS')
