"""Derive diagram-r1.2 from the exact public diagram-r1.1; change only paint order."""
from pathlib import Path
import argparse, hashlib, json, math
import fitz
from check_diagram_model import points
from lxml import etree as ET

ROOT=Path(__file__).resolve().parents[1]
NS={'s':'http://www.w3.org/2000/svg'}
PREVIOUS='a13f3d543eb076646bbacc437d2a8e8425a37300d87c7aa51589560d3472e0ba'

def build(source):
    data=source.read_bytes()
    if hashlib.sha256(data).hexdigest()!=PREVIOUS:raise ValueError('Expected exact diagram-r1.1 source')
    root=ET.fromstring(data);graph=root.xpath('//s:g[@class="graph"]',namespaces=NS)[0]
    layer=ET.Element('{'+NS['s']+'}g',id='edge-label-layer')
    layer.set('data-paint-layer','labels-after-connectors')
    for edge in graph.xpath('./s:g[@class="edge"]',namespaces=NS):
        moved=ET.Element('{'+NS['s']+'}g')
        moved.set('class','edge-labels');moved.set('data-edge-ref',edge.get('id'))
        moved.set('data-registry-id',edge.get('data-registry-id'))
        for child in list(edge):
            if child.tag in ('{'+NS['s']+'}text','{'+NS['s']+'}rect') or child.get('class')=='label-leader':
                edge.remove(child);moved.append(child)
        if len(moved):layer.append(moved)
    first_node=graph.xpath('./s:g[@class="node"]',namespaces=NS)[0]
    graph.insert(graph.index(first_node),layer)
    # Keep opaque label backgrounds away from parent triangles. Move only
    # affected label blocks; connector/node geometry and label values stay fixed.
    arrows=[];nodes=[];blocks=[]
    for poly in graph.xpath('.//s:polygon',namespaces=NS):
        ps=points(poly.get('points'))
        box=fitz.Rect(min(x for x,y in ps),min(y for x,y in ps),max(x for x,y in ps),max(y for x,y in ps))
        (nodes if poly.getparent().get('class')=='node' else arrows).append(box)
    for group in layer:
        children=list(group)
        for i,rect in enumerate(children):
            if rect.tag!='{'+NS['s']+'}rect':continue
            x,y,w,h=[float(rect.get(k)) for k in ('x','y','width','height')]
            text=[]
            for child in children[i+1:]:
                if child.tag=='{'+NS['s']+'}rect':break
                if child.tag=='{'+NS['s']+'}text':text.append(child)
            blocks.append((group,rect,text,fitz.Rect(x,y,x+w,y+h)))
    adjustments=[]
    for group,rect,text,old in blocks:
        if not any(old.intersects(a) for a in arrows):continue
        others=[b for g,r,t,b in blocks if r is not rect]
        selected=None
        offsets=sorted(((dx,dy) for dx in range(-60,61,2) for dy in range(-60,61,2) if dx or dy),key=lambda p:(math.hypot(*p),abs(p[0]),p))
        for dx,dy in offsets:
            candidate=old+(dx,dy,dx,dy)
            padded=candidate+(-1,-1,1,1)
            if any(padded.intersects(b) for b in arrows+nodes+others):continue
            selected=(dx,dy,candidate);break
        if selected is None:raise ValueError('No bounded clear label placement')
        dx,dy,new=selected
        rect.set('x',str(new.x0));rect.set('y',str(new.y0))
        for t in text:
            t.set('x',str(float(t.get('x'))+dx));t.set('y',str(float(t.get('y'))+dy))
        a,b=(old.x0+old.x1)/2,(old.y0+old.y1)/2
        c,d=a+dx,b+dy
        leader=ET.Element('{'+NS['s']+'}path',{'class':'label-leader','fill':'none','stroke':'#8a929d','stroke-width':'.45','d':f'M{a},{b} C{a},{b} {c},{d} {c},{d}'})
        group.insert(0,leader)
        adjustments.append({'registry_id':group.get('data-registry-id'),'text':[''.join(t.itertext()) for t in text],'old_background':list(old),'new_background':list(new),'offset_pt':[dx,dy]})
        old.x0,old.y0,old.x1,old.y1=list(new)
    root.set('data-artifact-version','diagram-r1.2')
    for t in root.xpath('./s:text',namespaces=NS):
        if t.text:t.text=t.text.replace('diagram-r1.1','diagram-r1.2')
    m=root.find('s:metadata',NS);metadata=json.loads(m.text)
    metadata.update(diagram_revision='diagram-r1.2',generator='tools/fix_diagram_paint_order.py',
                    predecessor={'commit':'8b24132a41b49f08dd81153bba09aa05f9571af9','sha256':PREVIOUS},
                    correction='CLR-VIS-001; connector geometry, IDs, label values and model hashes unchanged',label_adjustments=adjustments)
    m.text=json.dumps(metadata,sort_keys=True)
    target=ROOT/'model/diagrams/generated/full.svg'
    target.write_bytes(ET.tostring(root,encoding='utf-8',xml_declaration=True))
    print(json.dumps({'revision':'diagram-r1.2','sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'label_groups':len(layer)}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);a=p.parse_args();build(a.source)
