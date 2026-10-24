"""Offline integrity checks, not requirement-satisfaction evaluation."""
from pathlib import Path
import json,copy,hashlib,re,yaml

ROOT=Path(__file__).resolve().parents[1]


def problems(data):
    errors=[];ids=[]
    needs=data['functional']+data['quality']+data['future']['requirements']
    for row in needs:
        ids.append(row['id'])
        for field in ['title','capability','acceptance','adverse_case','source_locator','release_target']:
            if not row.get(field):errors.append('missing:'+field+':'+row['id'])
        if row['origin'] not in ['E','R','I']:errors.append('origin:'+row['id'])
        if row['satisfaction_status']!='not_assessed' or row['acceptance_status']!='not_assessed' or row['test_execution']!='not_executed':errors.append('premature_result:'+row['id'])
        raw=row['source_cells']
        header=re.fullmatch(r'(\w+-\d{2})\s+(MUST|SHOULD)\n(.+)\nOrigin ([ERI]) \| (.+)',raw[0])
        if not header or [row[k] for k in ['id','priority','title','origin','release_target']]!=list(header.groups()):errors.append('source_header_drift:'+row['id'])
        if raw[1]!=row['capability'] or raw[2]!='AC: '+row['acceptance']+'\nNAC: '+row['adverse_case']:errors.append('source_drift:'+row['id'])
    needmap={x['id']:x for x in needs}
    for row in data['cqs']+data['future']['exploratory_questions']:
        ids.append(row['id'])
        if row['requirement_id'] not in needmap:errors.append('dangling_requirement:'+row['id']);continue
        need=needmap[row['requirement_id']]
        if any(row[k]!=need[k] for k in ['acceptance','adverse_case']):errors.append('contract_drift:'+row['id'])
        if not row['question'] or not row['required_answer_fields']:errors.append('incomplete_question:'+row['id'])
        if row['test_execution']!='not_executed' or row['answer_status']!='not_computed':errors.append('premature_answer:'+row['id'])
        raw=row['source_cells']
        expected_question=row['question'] if row['id'].startswith('CQ-') else row['question']+'\nAnswer: '+row['required_answer_fields']
        if raw[0]!=row['id']+'\n'+row['requirement_id'] or raw[1]!=expected_question:errors.append('question_source_drift:'+row['id'])
        if row['id'].startswith('CQ-') and raw[2]!=row['required_answer_fields']:errors.append('answer_fields_drift:'+row['id'])
    if len(ids)!=len(set(ids)):errors.append('duplicate_id')
    return errors


def check():
    payload={n:yaml.safe_load((ROOT/'requirements'/f).read_text()) for n,f in [('functional','functional.yaml'),('quality','quality.yaml'),('cqs','competency-questions.yaml'),('future','future.yaml')]}
    data={k:(v['records'] if k!='future' else v) for k,v in payload.items()}
    assert not problems(data),problems(data)
    assert [len(data['functional']),len(data['quality']),len(data['future']['requirements']),len(data['cqs']),len(data['future']['exploratory_questions'])]==[30,10,8,30,8]
    for key,prefix,items in [('functional','FR',data['functional']),('quality','QR',data['quality']),('future','LR',data['future']['requirements']),('cq','CQ',data['cqs']),('lcq','LCQ',data['future']['exploratory_questions'])]:
        assert [x['id'] for x in items]==[f'{prefix}-{i:02d}' for i in range(1,len(items)+1)]
    assert len({x['source_sha256'] for x in payload.values()})==1
    negative=[]
    for label,mutate,expected in [
      ('missing adverse expectation',lambda d:d['functional'][0].update(adverse_case=''),'missing:adverse_case:'),
      ('unresolved CQ requirement',lambda d:d['cqs'][0].update(requirement_id='FR-99'),'dangling_requirement:'),
      ('invented CQ result',lambda d:d['cqs'][0].update(answer_status='satisfied'),'premature_answer:'),
      ('narrowed acceptance contract',lambda d:d['cqs'][0].update(acceptance='Weaker contract'),'contract_drift:'),
      ('rewritten source capability',lambda d:d['functional'][0].update(capability='Different meaning'),'source_drift:')]:
        changed=copy.deepcopy(data);mutate(changed);assert any(e.startswith(expected) for e in problems(changed)),label;negative.append(label)
    return {'status':'PASS','scope':'ORSD record parity and contract integrity; not satisfaction','counts':{'requirements':48,'cq_contracts':38},'negative_cases_rejected':negative,
            'input_sha256':next(iter(payload.values()))['source_sha256'],
            'files':{f:hashlib.sha256((ROOT/'requirements'/f).read_bytes()).hexdigest() for f in ['functional.yaml','quality.yaml','competency-questions.yaml','future.yaml','scope-and-scenarios.yaml']},
            'satisfaction':'not_assessed','execution':'not_executed'}


if __name__=='__main__':print(json.dumps(check(),indent=2))
