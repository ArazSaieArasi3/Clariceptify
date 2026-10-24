"""Check imported records and graph integrity; no philosophical validity claim."""
from pathlib import Path
import copy,json,hashlib
import yaml
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
NAMES={'domain':'domains','concept':'concepts','relation':'relations','generalization':'generalizations','constraint':'constraints'}


def inspect(families):
    errors=[]
    for kind,items in families.items():
        schema=json.loads((ROOT/f'model/schema/{kind}.schema.json').read_text())
        for r in items:
            for e in Draft202012Validator(schema).iter_errors(r):errors.append(kind+':schema:'+r.get('id','?')+':'+e.message)
        ids=[r['id'] for r in items]
        if len(ids)!=len(set(ids)):errors.append(kind+':duplicate_id')
    concepts={r['id'] for r in families['concept']};domains={r['id'] for r in families['domain']}
    for r in families['concept']:
        if r['primary_domain_id'] not in domains:errors.append('missing_domain:'+r['id'])
    edges=[];parents={}
    for r in families['relation']:
        if r['source_id'] not in concepts or r['target_id'] not in concepts:errors.append('missing_endpoint:'+r['id'])
        edges.append((r['source_id'],r['target_id']))
    for r in families['generalization']:
        if r['child_id'] not in concepts or r['parent_id'] not in concepts:errors.append('missing_endpoint:'+r['id'])
        edges.append((r['child_id'],r['parent_id']));parents.setdefault(r['child_id'],[]).append(r['parent_id'])
    states={}
    def visit(n):
        if states.get(n)==1:return False
        if states.get(n)==2:return True
        states[n]=1
        if not all(visit(x) for x in parents.get(n,[])):return False
        states[n]=2;return True
    if not all(visit(n) for n in concepts):errors.append('generalization_cycle')
    for r in families['constraint']:
        if any(x not in concepts for x in r['referenced_ids']):errors.append('missing_constraint_mention:'+r['id'])
        if r['execution_status']!='not_executed':errors.append('unexpected_constraint_execution_claim:'+r['id'])
    return errors,edges


def check():
    payload={k:yaml.safe_load((ROOT/f'model/{name}.yaml').read_text()) for k,name in NAMES.items()}
    families={k:v['records'] for k,v in payload.items()}
    errors,edges=inspect(families)
    if errors:raise AssertionError(errors)
    expected={'domain':21,'concept':137,'relation':174,'generalization':122,'constraint':24}
    if {k:len(v) for k,v in families.items()}!=expected:raise AssertionError('selected snapshot parity changed; declare a new model revision')
    if len({v['source_sha256'] for v in payload.values()})!=1:raise AssertionError('mixed source revisions')
    if any(v['status']!='imported_candidate' for v in payload.values()):raise AssertionError('unexpected import/approval status')
    negative_checks=[]
    mutated=copy.deepcopy(families);mutated['relation'][0]['target_id']='CLR-C9999'
    if not any(e.startswith('missing_endpoint:') for e in inspect(mutated)[0]):raise AssertionError('missing endpoint not detected')
    negative_checks.append('syntactically valid but absent concept endpoint rejected')
    mutated=copy.deepcopy(families);mutated['generalization'][0]['parent_id']=mutated['generalization'][0]['child_id']
    if 'generalization_cycle' not in inspect(mutated)[0]:raise AssertionError('cycle not detected')
    negative_checks.append('self specialization cycle rejected')
    mutated=copy.deepcopy(families);mutated['concept'].append(copy.deepcopy(mutated['concept'][0]))
    if 'concept:duplicate_id' not in inspect(mutated)[0]:raise AssertionError('duplicate ID not detected')
    negative_checks.append('duplicate concept identifier rejected')
    graph={r['id']:set() for r in families['concept']}
    for a,b in edges:graph[a].add(b);graph[b].add(a)
    remaining=set(graph);parts=0
    while remaining:
        stack=[remaining.pop()];parts+=1
        while stack:
            for n in graph[stack.pop()] & remaining:remaining.remove(n);stack.append(n)
    files={f'model/{name}.yaml':hashlib.sha256((ROOT/f'model/{name}.yaml').read_bytes()).hexdigest() for name in NAMES.values()}
    return {'status':'PASS','scope':'selected import schemas and basic graph integrity only',
            'counts':expected,'subject_domains':sum(r['layer']=='subject' for r in families['domain']),
            'foundations_concepts':sum(next(d for d in families['domain'] if d['id']==c['primary_domain_id'])['layer']=='foundations' for c in families['concept']),
            'connected_components_undirected':parts,'generalization_acyclic':True,'missing_endpoints':0,
            'negative_checks':negative_checks,'checked_file_sha256':files,
            'limits':['constraint ID mentions are lexical candidates, not complete semantic bindings',
                      'source passage verification and semantic lineage adjudication pending',
                      'graph integrity does not establish adequacy, joint satisfiability or expert acceptance']}


if __name__=='__main__':print(json.dumps(check(),indent=2))
