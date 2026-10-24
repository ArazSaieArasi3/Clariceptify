"""Lossless, hash-bound extraction of the retrospective ORSD input."""
from pathlib import Path
import argparse,hashlib,json,re,yaml
from docx import Document

ROOT=Path(__file__).resolve().parents[1]


def generate(path):
    digest=hashlib.sha256(Path(path).read_bytes()).hexdigest()
    integrity=yaml.safe_load((ROOT/'traceability/migration/input-integrity.yaml').read_text())
    expected=next(x['sha256'] for x in integrity['records'] if x['source_id']=='SRC-ORSD')
    if digest!=expected:raise ValueError('ORSD input digest differs from frozen source; no output written')
    doc=Document(path)
    def rows(n):return [[c.text for c in r.cells] for r in doc.tables[n].rows[1:]]
    def loc(n,i):return f'SRC-ORSD@sha256:{digest}#table-{n+1}/data-row-{i}'
    def needs(n,prefix):
        result=[]
        for i,row in enumerate(rows(n),1):
            m=re.fullmatch(r'('+prefix+r'-\d{2})\s+(MUST|SHOULD)\n(.+)\nOrigin ([ERI]) \| (.+)',row[0])
            if not m:raise ValueError('Unrecognized requirement heading '+row[0])
            ac,nac=row[2].split('\nNAC: ',1)
            if not ac.startswith('AC: '):raise ValueError('Missing acceptance marker')
            result.append({'id':m[1],'priority':m[2],'title':m[3],'origin':m[4],'release_target':m[5],
                           'capability':row[1],'acceptance':ac[4:],'adverse_case':nac,
                           'source_locator':loc(n,i),'source_cells':row,'satisfaction_status':'not_assessed',
                           'acceptance_status':'not_assessed','test_execution':'not_executed'})
        return result
    fr,qr,lr=needs(2,'FR'),needs(3,'QR'),needs(6,'LR')
    cqs=[]
    for i,row in enumerate(rows(4),1):
        cid,fid=row[0].split('\n')
        req=next(x for x in fr if x['id']==fid)
        cqs.append({'id':cid,'requirement_id':fid,'question':row[1],'required_answer_fields':row[2],
                    'input_contract':'A designated episode, artifact or record identified by the query subject; related records only through declared links.',
                    'acceptance':req['acceptance'],'adverse_case':req['adverse_case'],
                    'test_execution':'not_executed','answer_status':'not_computed',
                    'source_locator':loc(4,i),'source_cells':row})
    lcqs=[]
    for i,row in enumerate(rows(7),1):
        cid,rid=row[0].split('\n');question,fields=row[1].split('\nAnswer: ',1)
        req=next(x for x in lr if x['id']==rid)
        lcqs.append({'id':cid,'requirement_id':rid,'question':question,'required_answer_fields':fields,
                     'candidate_existing_witnesses':row[2],'acceptance':req['acceptance'],'adverse_case':req['adverse_case'],
                     'release_target':'R2 candidate','test_execution':'not_executed','answer_status':'not_computed',
                     'source_locator':loc(7,i),'source_cells':row})
    assert (len(fr),len(qr),len(lr),len(cqs),len(lcqs))==(30,10,8,30,8)
    base={'schema_version':'1.0','source_sha256':digest,'input_revision':'ORSD 0.1; 2026-10-24',
          'status':'retrospectively_reconstructed_review_draft','origins':{'E':'explicit owner instruction','R':'reconstructed from model; not prior stakeholder agreement','I':'inferred or proposed from purpose'}}
    outputs={'functional.yaml':dict(base,records=fr),'quality.yaml':dict(base,records=qr),
             'competency-questions.yaml':dict(base,records=cqs),
             'future.yaml':dict(base,requirements=lr,exploratory_questions=lcqs),
             'scope-and-scenarios.yaml':dict(base,profile=rows(0),scenarios=[{'id':row[0].split(' ',1)[0],'source_cells':row,'source_locator':loc(1,i)} for i,row in enumerate(rows(1),1)],
                     review_roadmap=rows(9),scope_decisions=rows(10))}
    for name,payload in outputs.items():(ROOT/'requirements'/name).write_text(yaml.safe_dump(payload,allow_unicode=True,sort_keys=False))
    report={'status':'PASS','source_sha256':digest,'counts':{'functional':30,'quality':10,'future':8,'cq':30,'exploratory_cq':8},
            'source_cells':'verbatim requirement and question cells retained','semantic_or_stakeholder_acceptance':'not_assessed',
            'cq_execution':'not_executed','limits':['candidate witness/model links are separate work','expected answer fields are not computed results','retrospective reconstruction not independent prospective elicitation']}
    (ROOT/'evaluation/orsd-import-report.json').write_text(json.dumps(report,indent=2)+'\n')
    return report


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('source_docx');a=ap.parse_args();print(json.dumps(generate(a.source_docx),indent=2))
