"""Audit current SVG/PDF/atlas element parity and flag possible paint-order occlusion.

The full vector path is checked, not just counts. The intersection screen samples
each cubic at 32 intervals; its candidates require visual judgment. It is not a
proof of readability, semantic validity, or human acceptance.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import subprocess
import sys
import fitz
from lxml import etree as ET
from check_diagram_model import NS, points

ROOT = Path(__file__).resolve().parents[1]
BASELINE = '018e6e0b860718718b0845c7902cc070e835d71e'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def shifted(p):
    return (p[0]+82.4, p[1]+3202.88)

def near(a,b):
    return max(abs(a[k]-b[k]) for k in (0,1)) < .02

def spans(page):
    return [s for b in page.get_text('dict')['blocks'] if 'lines' in b
            for line in b['lines'] for s in line['spans']]

def segment_intersects(a,b,r):
    lo,hi=0,1
    for k in (0,1):
        delta=b[k]-a[k]
        if abs(delta)<1e-9:
            if a[k]<r[k] or a[k]>r[k+2]: return False
        else:
            x,y=sorted(((r[k]-a[k])/delta,(r[k+2]-a[k])/delta))
            lo,hi=max(lo,x),min(hi,y)
            if lo>hi: return False
    return True

def run():
    inputs=['model/diagrams/generated/'+n for n in ('full.svg','full.pdf','atlas.pdf')]
    inputs+=['model/'+n+'.yaml' for n in ('concepts','domains','relations','generalizations','constraints')]
    inputs+=['evaluation/diagrams/pdf-atlas-build.json']
    audit=json.loads(subprocess.run([sys.executable,str(ROOT/'tools/check_diagram_model.py')],
                                   check=True,capture_output=True,text=True).stdout)
    svg=ET.parse(str(ROOT/inputs[0]))
    # This bounded adapter supports the frozen source's actual nested transforms.
    groups=svg.xpath('//s:g[@class="graph"]',namespaces=NS)
    if len(groups)!=1 or groups[0].get('transform')!='translate(0 0) scale(1 1) rotate(0) translate(32.4 3037.88)' or groups[0].getparent().get('transform')!='translate(50 165) scale(1)':
        raise ValueError('Unsupported source transform: implement it before reassessing')
    full=fitz.open(ROOT/inputs[1]);atlas=fitz.open(ROOT/inputs[2])
    page=full[0];drawings=page.get_drawings();text=spans(page)
    traced=[(''.join(chr(c[0]) for c in t['chars']),t) for t in page.get_texttrace()]
    build=json.loads((ROOT/inputs[-1]).read_text())
    for name,record in build['outputs'].items():
        if sha(ROOT/'model/diagrams/generated'/name)!=record['sha256']:
            raise ValueError('Output differs from build receipt: '+name)
    atlas_text={i:spans(atlas[i]) for i in range(len(atlas))}
    labels=[];elements=[];paths=[];failures=[];nodes=[]
    for group in svg.xpath('//s:g[@class="node" or @class="edge"]',namespaces=NS):
        rid=group.get('data-registry-id');kind=group.get('class')
        item={'registry_id':rid,'svg_id':group.get('id'),'kind':kind,'checks':{}}
        def check(name,condition):
            item['checks'][name]=bool(condition)
            if not condition:failures.append({'registry_id':rid,'check':name})
        if kind=='node':
            poly=group.xpath('.//s:polygon',namespaces=NS)[0]
            ps=[shifted(p) for p in points(poly.get('points'))]
            box=fitz.Rect(min(p[0] for p in ps),min(p[1] for p in ps),max(p[0] for p in ps),max(p[1] for p in ps))
            candidates=[d for d in drawings if all(abs(d['rect'][k]-box[k])<.02 for k in range(4)) and d.get('fill')]
            rgb=tuple(int(poly.get('fill')[k:k+2],16)/255 for k in (1,3,5))
            check('pdf_box_and_domain_fill',any(max(abs(d['fill'][k]-rgb[k]) for k in range(3))<.001 for d in candidates))
            tile_pages=[t['page'] for t in build['atlas']['tiles'] if fitz.Rect(t['source_clip_pt']).contains(box)]
            check('complete_node_in_detail_tile',bool(tile_pages));item.update(pdf_bbox_pt=list(box),atlas_complete_pages=tile_pages)
            nodes.append((rid,box))
        else:
            path=group.xpath('.//s:path[not(@class="label-leader")]',namespaces=NS)[0]
            ps=[shifted(p) for p in points(path.get('d'))]
            candidates=[d for d in drawings if d['items'] and d['items'][0][0] in ('c','l') and near(d['items'][0][1],ps[0]) and near(d['items'][-1][-1],ps[-1])]
            matched=None
            for d in candidates:
                if len(d['items'])!=(len(ps)-1)//3:continue
                ok=True
                for j,part in enumerate(d['items']):
                    a,b,c,z=ps[j*3:j*3+4]
                    if part[0]=='c':ok &= all(near(u,v) for u,v in zip(part[1:],(a,b,c,z)))
                    elif part[0]=='l':
                        # MuPDF simplifies straight, collinear cubic segments.
                        length=math.dist(a,z)
                        def on_segment(v):
                            return length>0 and abs((z[0]-a[0])*(v[1]-a[1])-(z[1]-a[1])*(v[0]-a[0]))/length<.02 and math.dist(a,v)+math.dist(v,z)-length<.02
                        ok &= near(part[1],a) and near(part[2],z) and on_segment(b) and on_segment(c)
                    else:ok=False
                if ok:matched=d;break
            check('pdf_complete_curve_controls',matched is not None)
            item['source_endpoint_pdf_pt']=list(ps[0]);item['target_endpoint_pdf_pt']=list(ps[-1])
            flat=[ps[0]]
            for j in range(1,len(ps),3):
                a,b,c,z=ps[j-1:j+3]
                for step in range(1,33):
                    t=step/32;u=1-t
                    flat.append(tuple(u**3*a[k]+3*u*u*t*b[k]+3*u*t*t*c[k]+t**3*z[k] for k in (0,1)))
            if matched:paths.append((rid,matched['seqno'],flat,matched['rect']))
            if group.get('data-stereotype')=='Generalization':
                pp=[shifted(p) for p in points(group.xpath('.//s:polygon',namespaces=NS)[0].get('points'))]
                triangles=[d for d in drawings if d['items'] and all(x[0]=='l' for x in d['items']) and (d.get('fill') is None or all(abs(v-1)<.001 for v in d['fill']))]
                check('pdf_hollow_parent_triangle',any(all(any(near(v,p) for x in d['items'] for v in x[1:]) for p in pp) for d in triangles))
            else:
                m=group.xpath('.//s:text[@text-anchor="middle"]',namespaces=NS)
                pos=[shifted((float(t.get('x')),float(t.get('y')))) for t in m]
                check('multiplicity_own_end_proximity',len(pos)==2 and math.dist(pos[0],ps[-1])<math.dist(pos[0],ps[0]) and math.dist(pos[1],ps[0])<math.dist(pos[1],ps[-1]))
        for node in group.xpath('.//s:text',namespaces=NS):
            content=''.join(node.itertext());x,y=shifted((float(node.get('x')),float(node.get('y'))))
            candidates=[s for s in text if s['text']==content and abs(s['origin'][1]-y)<.02]
            matched=min(candidates,key=lambda s:abs((s['bbox'][0]+s['bbox'][2])/2-x) if node.get('text-anchor')=='middle' else abs(s['origin'][0]-x)) if candidates else None
            if not matched:
                failures.append({'registry_id':rid,'check':'pdf_text_missing','text':content});continue
            anchor=(matched['bbox'][0]+matched['bbox'][2])/2 if node.get('text-anchor')=='middle' else matched['origin'][0]
            row={'registry_id':rid,'text':content,'svg_baseline_pdf_pt':[x,y],'pdf_bbox_pt':list(matched['bbox']),'position_error_pt':abs(anchor-x),'font_size_pt':matched['size'],'atlas_complete_pages':[]}
            if row['position_error_pt']>.02:failures.append({'registry_id':rid,'check':'pdf_text_position','text':content})
            for tile in build['atlas']['tiles']:
                if not fitz.Rect(tile['source_clip_pt']).contains(fitz.Rect(matched['bbox'])):continue
                target=(matched['origin'][0]-tile['source_clip_pt'][0]+tile['destination_pt'][0],y-tile['source_clip_pt'][1]+tile['destination_pt'][1])
                if any(s['text']==content and near(s['origin'],target) and abs(s['size']-matched['size'])<.02 and s['color']==matched['color'] for s in atlas_text[tile['page']-1]):
                    row['atlas_complete_pages'].append(tile['page'])
            if not row['atlas_complete_pages']:failures.append({'registry_id':rid,'check':'atlas_text_not_wholly_preserved','text':content})
            tt=[q for value,q in traced if value==content and abs(q['chars'][0][2][1]-y)<.02]
            if not tt:
                for value,q0 in traced:
                    offset=value.find(content)
                    while offset>=0:
                        chars=q0['chars'][offset:offset+len(content)]
                        if abs(chars[0][2][1]-y)<.02:
                            tt.append({**q0,'bbox':chars[0][3]})
                        offset=value.find(content,offset+1)
            if not tt and kind=='edge':raise ValueError('No paint-order trace for '+rid+': '+content)
            q=min(tt,key=lambda q:abs(q['bbox'][0]-matched['bbox'][0])) if tt else None
            row['paint_sequence']=q['seqno'] if q else None;row['ink_band_bbox_pt']=[matched['bbox'][0],y-.70*matched['size'],matched['bbox'][2],y+.02*matched['size']]
            labels.append(row)
        elements.append(item)
    candidates=[]
    text_node_candidates=[]
    text_text_candidates=[]
    for i,label in enumerate(labels):
        band=fitz.Rect(label['ink_band_bbox_pt'])
        for other in labels[i+1:]:
            if label['registry_id']==other['registry_id']:continue
            other_band=fitz.Rect(other['ink_band_bbox_pt']);intersection=band & other_band
            if not intersection.is_empty and intersection.get_area()/min(band.get_area(),other_band.get_area())>.1:
                text_text_candidates.append([label['registry_id'],other['registry_id']])
        if label['registry_id'].startswith('CLR-R'):
            for rid,box in nodes:
                intersection=band & box
                if not intersection.is_empty and intersection.get_area()/band.get_area()>.2:
                    text_node_candidates.append([label['registry_id'],rid])
    for label in labels:
        if not label['registry_id'].startswith('CLR-R'):continue
        band=fitz.Rect(label['ink_band_bbox_pt'])
        for rid,seq,flat,box in paths:
            if rid==label['registry_id'] or seq<label['paint_sequence'] or not band.intersects(box):continue
            if any(segment_intersects(a,b,band) for a,b in zip(flat,flat[1:])):
                candidates.append({'candidate_id':f'CLR-VIS-CAND-{len(candidates)+1:03d}','label_edge':label['registry_id'],'text':label['text'],'later_line_edge':rid,'full_pdf_page':1,'full_pdf_bbox_pt':list(band),'atlas_pages':label['atlas_complete_pages'],'status':'machine_candidate_requires_visual_judgment'})
    report={'baseline_commit':BASELINE,'task':'R1-025.c','status':'FAIL' if failures else 'PARITY_PASS_WITH_READABILITY_CANDIDATES','input_sha256':{p:sha(ROOT/p) for p in inputs},'validator_sha256':sha(Path(__file__)),'runtime':{'python':sys.version.split()[0],'pymupdf':fitz.VersionBind,'mupdf':fitz.VersionFitz},'counts':{'nodes':len(nodes),'edges':len(paths),'model_text_labels':len(labels),'occlusion_candidates':len(candidates),'text_text_candidates':len(text_text_candidates),'text_node_candidates':len(text_node_candidates)},'elements':elements,'labels':labels,'occlusion_candidates':candidates,'text_text_candidates':text_text_candidates,'text_node_candidates':text_node_candidates,'failures':failures,'limitations':['Curve intersections use 32 linear intervals per cubic and a baseline-relative text band; not an exhaustive glyph visibility proof.','Visual judgment and semantic acceptance are distinct from PDF element parity.','Legacy input identity and current model correspondence were freshly checked; historical PDF byte reproduction is not claimed.']}
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    result=run();args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','counts','failures')}))
    raise SystemExit(bool(result['failures']))
