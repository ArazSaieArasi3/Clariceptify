"""Render the bound complete SVG and a same-scale, overlapping A3 reading atlas.

Run from any directory. Requires requirements-diagrams.txt. The SVG and registries
remain unchanged; this adapter is not a semantic or native OntoUML validator.
"""
from pathlib import Path
import hashlib
import json
import math
import subprocess
import sys
import textwrap
import xml.etree.ElementTree as ET
import fitz

ROOT = Path(__file__).resolve().parents[1]
BASELINE = '8b24132a41b49f08dd81153bba09aa05f9571af9'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def build():
    source = ROOT / 'model/diagrams/generated/full.svg'
    audit = subprocess.run([sys.executable, str(ROOT/'tools/check_diagram_model.py')],
                           capture_output=True, text=True, check=True)
    parity = json.loads(audit.stdout)
    svg = ET.parse(source).getroot()
    bindings = json.loads(svg.find('{http://www.w3.org/2000/svg}metadata').text)
    revision=bindings['diagram_revision']
    out = source.parent
    with fitz.open(source) as vector:
        full = fitz.open(stream=vector.convert_to_pdf(), filetype='pdf')
    metadata = {'title':f'Clariceptify - complete conceptual model - {revision}',
                'subject':f'Review candidate; source SHA256 {digest(source)}; model input-r1-rev1',
                'creator':f'build_diagram_pdfs.py; PyMuPDF {fitz.VersionBind}',
                'producer':f'PyMuPDF {fitz.VersionBind}'}
    full.set_metadata(metadata)
    full.save(out/'full.pdf', garbage=4, deflate=True, no_new_id=True)
    width, height = full[0].rect.width, full[0].rect.height
    pw, ph = 420*72/25.4, 297*72/25.4
    margin, top, bottom = 28, 54, 36
    overlap_x, overlap_y = 240, 96
    tw, th = pw-2*margin, ph-top-bottom
    cols = math.ceil((width-overlap_x)/(tw-overlap_x))
    rows = math.ceil((height-overlap_y)/(th-overlap_y))
    atlas = fitz.open()
    guide = atlas.new_page(width=pw, height=ph)
    guide.insert_text((28,30), f'CLARICEPTIFY | {revision} | A3 reading atlas', fontsize=18)
    guide.insert_text((28,51), 'Review candidate | Print at 100% / Actual size | Detail pages preserve source scale (1 pt = 1 pt).', fontsize=11)
    guide.insert_text((28,69), 'Read left to right, then top to bottom. Adjacent tiles overlap by 240 pt horizontally and 96 pt vertically. Follow row/column labels across pages.', fontsize=11)
    guide.insert_text((28,87), 'The complete overview needs zoom. Semantic acceptance and exhaustive visual parity are not established.', fontsize=11)
    overview = fitz.Rect(28,112,pw-28,ph-100)
    guide.show_pdf_page(overview,full,0)
    scale = min(overview.width/width, overview.height/height)
    ox = overview.x0+(overview.width-width*scale)/2
    oy = overview.y0+(overview.height-height*scale)/2
    tiles = []
    for row in range(rows):
        for col in range(cols):
            x, y = col*(tw-overlap_x), row*(th-overlap_y)
            clip = fitz.Rect(x,y,min(x+tw,width),min(y+th,height))
            page_number = len(tiles)+2
            page = atlas.new_page(width=pw,height=ph)
            label = f'R{row+1:02d} C{col+1:02d}'
            page.insert_text((28,23), f'CLARICEPTIFY | {revision} | {label} | page {page_number}', fontsize=13)
            page.insert_text((28,40), f'Source window: x={x:.1f}..{clip.x1:.1f}, y={y:.1f}..{clip.y1:.1f} pt | 100% scale | 240 / 96 pt overlap', fontsize=9)
            dest = fitz.Rect(margin,top,margin+clip.width,top+clip.height)
            page.show_pdf_page(dest,full,0,clip=clip,keep_proportion=False)
            page.draw_rect(dest,color=(.7,.7,.7),width=.3)
            neighbors = []
            for name, rr, cc in [('Left',row,col-1),('Right',row,col+1),('Up',row-1,col),('Down',row+1,col)]:
                if 0<=rr<rows and 0<=cc<cols:
                    target = 1+rr*cols+cc
                    neighbors.append(f'{name}: R{rr+1:02d} C{cc+1:02d} (p{target+1})')
            page.insert_text((28,ph-17), ' | '.join(neighbors)+' | Review candidate', fontsize=9)
            box = fitz.Rect(ox+clip.x0*scale,oy+clip.y0*scale,ox+clip.x1*scale,oy+clip.y1*scale)
            # Reacquire the guide after adding pages (PyMuPDF invalidates page objects).
            guide = atlas[0]
            guide.draw_rect(box,color=(.2,.3,.6),width=.4)
            guide.insert_text((box.x0+2,box.y0+9),f'{label} p{page_number}',fontsize=6)
            guide.insert_link({'kind':fitz.LINK_GOTO,'from':box,'page':page_number-1})
            tiles.append({'page':page_number,'row':row+1,'column':col+1,'source_clip_pt':list(clip),'destination_pt':list(dest),'scale':1.0})
    # Long source legend sentences can cross tile boundaries. Repeat their exact
    # text in a wrapped reading appendix; do not redefine or abbreviate them.
    appendix_start = len(atlas)+1
    page = None
    cursor = ph
    for element in svg.iter('{http://www.w3.org/2000/svg}text'):
        size = float(element.get('font-size', '0'))
        if size not in (22, 20.68, 19):
            continue
        text = ''.join(element.itertext())
        lines = textwrap.wrap(text, width=150, break_long_words=False)
        needed = len(lines)*15+12
        if cursor+needed > ph-40:
            page=atlas.new_page(width=pw,height=ph)
            page.insert_text((28,30),f'CLARICEPTIFY | Source legend and reading notes | {revision}',fontsize=16)
            page.insert_text((28,49),'Exact source wording, reflowed for reading. Review candidate; no new scientific acceptance.',fontsize=10)
            cursor=80
        for line in lines:
            page.insert_text((36,cursor),line,fontsize=11 if size!=22 else 12)
            cursor+=15
        cursor+=12
    atlas.set_metadata({**metadata,'title':f'Clariceptify - A3 reading atlas - {revision}'})
    atlas.set_toc([[1,'Overview and tile navigation',1]]+[[1,f"Row {r+1}",2+r*cols] for r in range(rows)]+[[1,'Source legend and reading notes',appendix_start]])
    atlas.save(out/'atlas.pdf',garbage=4,deflate=True,no_new_id=True)
    outputs = {}
    for name in ['full.pdf','atlas.pdf']:
        path=out/name
        with fitz.open(path) as pdf:
            outputs[name]={'sha256':digest(path),'bytes':path.stat().st_size,'pages':len(pdf),'page_sizes_pt':sorted(set(tuple(p.rect) for p in pdf)),'image_objects':sum(len(p.get_images()) for p in pdf)}
    report={'task':'R1-FIX-VIS-001' if revision=='diagram-r1.2' else 'R1-025.b','baseline_commit':BASELINE,'status':'PASS',
            'scope':'Same-source vector PDF generation and complete overlapping tile coverage; exhaustive visual parity/readability is issue #45.',
            'source':{'path':str(source.relative_to(ROOT)),'sha256':digest(source),'diagram_revision':bindings['diagram_revision'],'model_sha256':bindings['model_sha256']},
            'generator':{'path':'tools/build_diagram_pdfs.py','sha256':digest(Path(__file__)),'pymupdf':fitz.VersionBind,'mupdf':fitz.VersionFitz,'python':sys.version.split()[0]},
            'checks':{'current_svg_model_audit':parity['status'],'vector_outputs_no_raster_images':all(o['image_objects']==0 for o in outputs.values()),'coverage_no_gaps':tw>overlap_x and th>overlap_y and tiles[-1]['source_clip_pt'][2:]==[width,height]},
            'atlas':{'format':'A3 landscape','rows':rows,'columns':cols,'detail_scale':1.0,'appendix_start_page':appendix_start,'overlap_pt':[overlap_x,overlap_y],'tiles':tiles},'outputs':outputs,
            'limitations':['Original historical PDF/atlas byte regeneration is not claimed.','No semantic or human approval; no native OntoUML validation.','Issue #45 retains exhaustive visual parity, label proximity and occlusion checks.']}
    if not all(v is True or v=='PASS' for v in report['checks'].values()):
        raise ValueError(report['checks'])
    (ROOT/'evaluation/diagrams/pdf-atlas-build.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'outputs':outputs,'rows':rows,'columns':cols}))

if __name__=='__main__':
    build()
