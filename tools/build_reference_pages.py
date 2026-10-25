"""Generate read-only Markdown reference views and lossless UTF-8 CSV exports.

No source definitions, qualification states or semantic commitments are edited.
CSV is a software interchange serialization, with lists/dicts/bools/null as JSON.
"""
from pathlib import Path
import argparse,csv,hashlib,html,io,json,os,re
import yaml
ROOT=Path(__file__).resolve().parents[1]

def sha(data):return hashlib.sha256(data).hexdigest()
def read(path):return yaml.safe_load((ROOT/path).read_text())['records']
def cell(value):return html.escape(str(value if value is not None else 'not specified')).replace('|','\\|').replace('\n','<br>')
def table(head,rows):return '| '+' | '.join(head)+' |\n| '+' | '.join(['---']*len(head))+' |\n'+''.join('| '+' | '.join(cell(v) for v in row)+' |\n' for row in rows)
def build(part,baseline):
    inputs=['model/'+n+'.yaml' for n in ('concepts','domains','relations','generalizations','constraints')]
    inputs+=['evidence/source-register.yaml','evidence/concept-support.yaml']
    records={n:read('model/'+n+'.yaml') for n in ('concepts','domains','relations','generalizations','constraints')}
    concepts={c['id']:c for c in records['concepts']};domains={d['id']:d for d in records['domains']}
    supports={c['concept_id']:c for c in read('evidence/concept-support.yaml')};sources={s['id']:s for s in read('evidence/source-register.yaml')}
    outputs={}
    def emit(path,text):outputs['docs/reference/'+path]=text.encode('utf-8')
    def header(title):return '# '+title+'\n\nGenerated view. Edit the authoritative registries, then regenerate. Model: `input-r1-rev1`; lifecycle: candidate.\n\n'
    if part=='concepts':
        emit('sources.md',header('Imported source register')+'These IEEE entries and metadata are reproduced from the imported register. Metadata and passages have not been reverified by this documentation step.\n\n'+''.join('## '+s['id']+'\n\n'+s['citation_ieee_input']+'\n\nMetadata: `'+s['metadata_verification']+'`; full-text review: `'+s['full_text_review']+'`.\n\n' for s in sources.values()))
        for c in concepts.values():
            support=supports[c['id']];domain=domains[c['primary_domain_id']]
            text=header(c['label_en']+' - '+c['id'])+'[Concept index](README.md) | [Domain: '+domain['label_en']+'](../domains/'+domain['id']+'.md)\n\n'
            text+='## Definition\n\n'+c['definition']+'\n\n'
            text+=table(['Field','Imported value'],[(k,c[k]) for k in ('ontouml_stereotype','ufo_type','lifecycle','introduced_version','is_abstract','source_locator','notes')])
            text+='\n## Source support\n\n'+table(['Field','Qualification'],[(k,support[k]) for k in ('support_type','support_scope_and_limit','input_source_locations','passage_verification','typing_approval','source_locator')])+'\n'
            text+='D: direct notion support in the input screening; B: adapted/theoretical basis; P: passage support pending. These qualifications are not independent typing approval.\n\n'
            for sid in c['source_reference_ids']:
                source=sources[sid];text+='- ['+sid+'](../sources.md#'+sid.lower()+'): '+source['citation_ieee_input']+'\n'
            text+='\n[Authoritative concept registry](../../../model/concepts.yaml). Source passages and philosophical adequacy are not reassessed by page generation.\n'
            emit('concepts/'+c['id']+'.md',text)
        emit('concepts/README.md',header('Concept index')+'\n'.join('- ['+c['label_en']+' - '+c['id']+']('+c['id']+'.md)' for c in concepts.values())+'\n')
        for d in domains.values():
            members=[c for c in concepts.values() if c['primary_domain_id']==d['id']]
            text=header(d['label_en']+' - '+d['id'])+'[Domain index](README.md)\n\n## Description\n\n'+d['description']+'\n\n## Purpose\n\n'+d['purpose']+'\n\n'
            text+=table(['Field','Imported value'],[(k,d[k]) for k in ('layer','lifecycle','introduced_version','source_locator')])+'\n## Primary members\n\n'
            text+='\n'.join('- ['+c['label_en']+' - '+c['id']+'](../concepts/'+c['id']+'.md)' for c in members)+'\n\n[Authoritative domain registry](../../../model/domains.yaml). Membership is not a domain-adequacy assessment.\n'
            emit('domains/'+d['id']+'.md',text)
        emit('domains/README.md',header('Domain index')+'\n'.join('- ['+d['label_en']+' - '+d['id']+']('+d['id']+'.md)' for d in domains.values())+'\n')
        emit('README.md',header('Clariceptify reference')+'- [Concepts](concepts/README.md)\n- [Domains](domains/README.md)\n- [Sources](sources.md)\n\nHistorical Word/PDF input specifications are frozen source evidence, not current editing authorities. Generated PDFs are diagram views. Definitions, membership and support states are owned by model/ and evidence/. This is repository documentation; Pages/WIDOCO/WebVOWL publication is separate.\n')
    else:
        # Readable labels accompany stable IDs; complete source fields survive in CSV.
        head=['Relation ID','Concept 1','Stereotype 1','Cardinality 1','Relation','Relation stereotype','Connector','Cardinality 2','Stereotype 2','Concept 2']
        rows=[]
        for r in records['relations']:
            a,b=concepts[r['source_id']],concepts[r['target_id']]
            rows.append([r['id'],'['+a['id']+' '+a['label_en']+'](../concepts/'+a['id']+'.md)',a['ontouml_stereotype'],r['source_multiplicity'],r['label_en'],r['ontouml_stereotype'],r['connector'],r['target_multiplicity'],b['ontouml_stereotype'],'['+b['id']+' '+b['label_en']+'](../concepts/'+b['id']+'.md)'])
        emit('relations/README.md',header('Association table')+'Multiplicity values belong to their respective class ends; no OWL restriction is inferred.\n\n'+table(head,rows)+'\n[Generalizations](generalizations.md) | [CSV exports](../exports/README.md) | [Registry](../../../model/relations.yaml)\n')
        emit('relations/generalizations.md',header('Generalization table')+table(['ID','Child','Parent','Completeness','Disjointness'],[[g['id'],'['+g['child_id']+' '+concepts[g['child_id']]['label_en']+'](../concepts/'+g['child_id']+'.md)','['+g['parent_id']+' '+concepts[g['parent_id']]['label_en']+'](../concepts/'+g['parent_id']+'.md)',g['set_completeness'],g['set_disjointness']] for g in records['generalizations']])+'\nHollow triangle points to the parent. Unknown set flags do not assert a partition. [Registry](../../../model/generalizations.yaml).\n')
        emit('constraints/README.md',header('Textual constraints')+'Mentioned concept IDs are lexical candidates, not reviewed formal scope. These textual constraints remain unexecuted except for separately declared bounded fixture checks.\n\n'+table(['ID','Text','Referenced IDs','Enforcement','Execution'],[[c['id'],c['text'],', '.join('['+cid+'](../concepts/'+cid+'.md)' for cid in c['referenced_ids']),c['enforcement'],c['execution_status']] for c in records['constraints']])+'\n[Registry](../../../model/constraints.yaml).\n')
        export_sets={**records,'sources':list(sources.values()),'concept-support':list(supports.values()),'membership':[{'concept_id':c['id'],'domain_id':c['primary_domain_id']} for c in concepts.values()]}
        for name,data in export_sets.items():
            fields=list(dict.fromkeys(k for record in data for k in record))
            stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=fields,lineterminator='\n');writer.writeheader()
            writer.writerows({k:(v if isinstance(v,str) else json.dumps(v,ensure_ascii=False,sort_keys=True)) for k,v in record.items()} for record in data)
            raw=stream.getvalue();roundtrip=list(csv.DictReader(io.StringIO(raw)))
            if len(roundtrip)!=len(data) or [list(r) for r in roundtrip]!=[fields]*len(data):raise ValueError('CSV shape mismatch: '+name)
            for actual,expected in zip(roundtrip,data):
                for k,v in expected.items():
                    decoded=actual[k] if isinstance(v,str) else json.loads(actual[k])
                    if decoded!=v:raise ValueError('CSV data loss: '+name+'/'+k)
            emit('exports/'+name+'.csv',raw)
        emit('exports/README.md',header('CSV export contract')+'UTF-8, RFC-style quoting, LF record separator. Every source field is retained. Strings stay strings; lists, dictionaries, booleans and null are JSON-serialized in cells. Decode by the authoritative record schema; CSV is not a second editing authority.\n\n'+''.join('- ['+n+']('+n+'.csv)\n' for n in export_sets))
    if part=='concepts' and (ROOT/'docs/reference/relations/README.md').exists():
        outputs['docs/reference/README.md']+=b'\n- [Associations and generalizations](relations/README.md)\n- [Textual constraints](constraints/README.md)\n- [CSV exports](exports/README.md)\n'
    # Verify encoding and all generated local Markdown destinations, including fragments.
    for path,data in outputs.items():
        data.decode('utf-8')
        for target in re.findall(r'\]\(([^)]+)\)',data.decode()) if path.endswith('.md') else []:
            if '://' in target or target.startswith('#'):continue
            dest,_,fragment=target.partition('#');resolved=os.path.normpath(str(Path(path).parent/dest))
            if resolved not in outputs and not (ROOT/resolved).exists():raise ValueError('Broken link: '+path+' -> '+target)
            if fragment:
                body=outputs.get(resolved,(ROOT/resolved).read_bytes() if (ROOT/resolved).exists() else b'').decode()
                if fragment not in [line[3:].strip().lower() for line in body.splitlines() if line.startswith('## ')]:raise ValueError('Missing fragment: '+target)
    for path,data in outputs.items():
        dest=ROOT/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    report={'task':'R1-026.a' if part=='concepts' else 'R1-026.b','baseline_commit':baseline,'status':'PASS','part':part,'input_sha256':{p:sha((ROOT/p).read_bytes()) for p in inputs},'generator_sha256':sha(Path(__file__).read_bytes()),'record_counts':{k:len(v) for k,v in records.items()},'checks':['UTF-8 decoding','all generated local links and source fragments resolve','all source definitions/membership preserved by direct projection']+(['all CSV source fields independently round-trip by source type'] if part=='relations' else []),'output_sha256':{p:sha(b) for p,b in outputs.items()},'limits':['No source metadata, passage, semantic typing or adequacy is newly verified.','Historical Word/PDF files remain source evidence.','No external documentation deployment is claimed.']}
    (ROOT/'evaluation'/('reference-'+part+'.json')).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'part':part,'outputs':len(outputs),'status':'PASS'}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--part',choices=['concepts','relations'],required=True);p.add_argument('--baseline',required=True);a=p.parse_args();build(a.part,a.baseline)
