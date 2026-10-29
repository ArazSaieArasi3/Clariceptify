"""Check #235 source-bound coverage and actual recorded results, not rerun reasoning."""
from pathlib import Path
import argparse,hashlib,json,yaml
from render_dns235 import ROOT,render_catalog,render_review
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(root=ROOT):
 r=yaml.safe_load((root/'evidence/related-work/artifacts/DnS.yaml').read_text())
 d={k:(json.loads if v['path'].endswith('.json') else yaml.safe_load)((root/v['path']).read_text()) for k,v in r['evidence'].items()}
 return r,d
def validate(r,d):
 def need(x,m):
  if not x:raise ValueError(m)
 need(r['issue']==235 and r['identity']['historical_2003_fidelity']=='NOT_ESTABLISHED','Historical source promotion')
 need(r['boundary']==dict(model_change='NONE',requirements_change='NONE',fixtures_change='NONE',manuscript_change='NONE',release_change='NONE',semantic_acceptance='NOT_ASSESSED',independent_expert_review='NOT_PERFORMED',adoption='OWNER_DECISION_REQUIRED',source_redistribution=False),'Scope/acceptance promoted')
 c=d['census'];cat=d['catalog'];s=d['semantic']
 need(c['source_sha256']==r['identity']['sha256']==cat['source_sha256']=='7d69150ed0b67ef4b0cbe0b50b03e64634de02f6a30988f83c26e90c33aadb41','Source substitution')
 need(c['counts']==dict(closure_unique_declared_classes=95,datatype_properties=0,explicit_root_triples=1650,external_class_redeclarations=10,external_object_properties=15,local_classes=58,local_comment_candidates=58,local_object_properties=118),'Changed unit/population')
 need(len(cat['classes'])==len({x['iri'] for x in cat['classes']})==68,'Missing/duplicate class')
 by={x['iri']:x for x in c['classes']};need(set(by)=={x['iri'] for x in cat['classes']},'Incomplete root population')
 need(len(c['imports'])==3 and len(c['modules'])==4 and c['unresolved_imports']==[] and c['referenced_not_declared_in_closure']==[],'Imports or undeclared references concealed')
 for row in cat['classes']:
  x=by[row['iri']]
  need(row['axiom_sha256']==x['axiom_sha256'] and row['population']==x['population'] and row['source_labels']==x['label'],'Source constraint/label changed')
  need(row['reviewer_definition']['text'] and row['source_definition']['raw_text_public'] is False and row['source_definition']['adequacy']=='NOT_INFERRED_FROM_COMMENT','Definition omitted/promoted')
  if x['population']=='LOCAL':need(row['source_definition']['annotations']==x['definition_annotations'],'Local annotation locator drift')
 missing=[x for x in cat['classes'] if x['source_definition']['state']=='INSUFFICIENT_COMMENT_TYPOLOGY_PENDING'];need(len(missing)==1 and missing[0]['iri'].endswith('#non-agentive-figure'),'Insufficient definition hidden')
 need(s['owl2_dl_profile_pass'] is True and s['profile_violation_count']==0 and s['baseline_consistent'] is True and s['unsatisfiable_named_classes']==[] and s['baseline_error'] is None,'Recorded observation altered')
 need(len(s['tests'])==len({x['id'] for x in s['tests']})==15 and s['summary']==dict(total=15,passed=15,failed=0,errors=0),'Incomplete/unexecuted semantic outcomes')
 for t in s['tests']:
  need(t['result']=='PASS' and isinstance(t['observed_consistent'],bool) and t['expected_consistent'] is t['observed_consistent'] and t['error'] is None,'Expected/observed result drift')
  need(hashlib.sha256(t['fixture_nt'].encode()).hexdigest()==t['fixture_sha256'],'Fixture changed')
 need([q['id'] for q in r['questions']]==[f'Q{i:02}' for i in range(1,9)],'Question scope changed')
 need({x['id'] for x in r['findings']}=={f'DNS235-F{i:02}' for i in range(1,10)} and len(r['findings'])==9 and all(x['next_issues']==[251,126] and x['utilization_categories'] and set(x['evidence_keys'])<=set(r['evidence']) and set(x['question_ids'])<={q['id'] for q in r['questions']} for x in r['findings']),'Findings lost')
 need(r['execution']['FOL_formula14_solver']==r['execution']['SWAP_execution']=='NOT_EXECUTED','Unperformed execution claimed')
 need(all(x['status']!='ACCEPTED_EQUIVALENCE' for x in r['model_comparison_candidates']),'Candidate mapping promoted')
 return dict(status='PASS',issue=235,local_classes=58,external_redeclarations=10,local_comment_candidates=58,insufficient_definitions=1,recorded_semantic_cases=15,scope='Evidence integrity, not a reasoner rerun or semantic acceptance')
def check(root=ROOT,source_dir=None):
 r,d=load(root);out=validate(r,d)
 for ref in r['evidence'].values():
  if sha(root/ref['path'])!=ref['sha256']:raise ValueError('Stale source binding '+ref['path'])
 for name in ['census','semantic']:
  x=d[name]
  if sha(root/x['generator_path'])!=x['generator_sha256'] or sha(root/'tools/inspect_bdi2026.py')!=x['helper_sha256']:raise ValueError('Changed executed inspector')
 if (root/'evidence/related-work/dns235-class-catalog.md').read_text()!=render_catalog(d['catalog']) or (root/'evidence/related-work/artifacts/DnS.md').read_text()!=render_review(r):raise ValueError('Stale rendered review')
 ids={x['id'] for x in yaml.safe_load((root/'model/concepts.yaml').read_text())['records']}
 model=r['model_comparison_baseline']
 if sha(root/model['path'])!=model['sha256'] or model['revision']!='input-r1-rev1':raise ValueError('Changed target model baseline')
 if any(not set(x['model_ids'])<=ids for x in r['model_comparison_candidates']):raise ValueError('Unbound model comparison')
 if source_dir is not None:
  from inspect_dns235 import census
  if census(source_dir)['classes']!=d['census']['classes']:raise ValueError('Exact source reparse differs')
  out['exact_source_reparse']='PASS'
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source-dir',type=Path);a=p.parse_args();print(json.dumps(check(source_dir=a.source_dir),indent=2))
