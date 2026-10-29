"""Check exact-core evidence bindings; never turn refusal into a semantic pass."""
import argparse,hashlib,json,yaml
from pathlib import Path
from render_cdns267 import ROOT,PATH,render
SHA='f0d7b6c795fe9e1a699eda2d80089371336869e981e938648edd5db88358658a'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(root=ROOT):
 r=yaml.safe_load((root/PATH).read_text());return r,json.loads((root/r['evidence']['execution']['path']).read_text())
def validate(r,e):
 def need(x,m):
  if not x:raise ValueError(m)
 need(r['issue']==e['issue']==267 and r['source']['sha256']==e['source_sha256']==SHA,'Input substitution')
 need(r['status']=='BOUNDED_CORE_FOLLOWUP_COMPLETE_WITH_PROFILE_FAILURE','Completion promoted')
 need(e['source_population']==dict(annotation_properties=0,classes=12,datatype_properties=0,named_individuals=0,object_properties=47) and e['explicit_triples']==411 and len(e['source_classes'])==12 and len(set(e['source_classes']))==12,'Population changed')
 need(e['imports']==r['source']['declared_imports']==[] and e['loaded_ontology_count']==1,'Import scope expanded')
 p=e['profile'];need(p['in_profile'] is False and p['violation_count']==len(p['violations'])==1 and 'ObjectMinCardinality(2' in p['violations'][0] and 'hasProperPart' in p['violations'][0],'Profile failure concealed')
 a=e['reasoner_attempt'];need(a['state']=='REFUSED_NON_SIMPLE_PROPERTY' and a['consistent'] is None and a['unsatisfiable_named_classes'] is None and 'Non-simple property' in a['error'],'Refusal changed to consistency judgment')
 need(e['policy']==dict(source_repair=False,axioms_deleted=0,imports_deleted=0,transitivity_removed=False,cardinality_weakened=False,approximate_repaired_theory_tested=False,fixture_consistency_execution='NOT_EXECUTED_FULL_CORE_REFUSED',logical_consistency='NOT_ESTABLISHED',global_paper_proof='NOT_EXECUTED',scientific_acceptance='NOT_ASSESSED',model_change='NONE'),'Source weakening or execution promotion')
 ids=[f'Q{i:02}' for i in range(1,9)];need([q['id'] for q in r['questions']]==ids and [q['id'] for q in e['asserted_queries']]==ids,'Missing/duplicate comparison or query')
 need(e['query_summary']==dict(total=8,passed=8,failed=0),'Query population wrong')
 for q in e['asserted_queries']:
  need(q['expected_ask'] is q['observed_ask'] is True and q['result']=='PASS' and q['basis']=='EXECUTED_ASSERTED_RDF_QUERY_NOT_SEMANTIC_VALIDATION' and hashlib.sha256(q['query'].encode()).hexdigest()==q['query_sha256'],'Query/result/basis changed')
 for q in r['questions']:
  need(q['artifact_locators'] and q['positive_scenario'] and q['adverse_scenario'] and q['scenario_execution']=='NOT_EXECUTED_FULL_CORE_REASONER_REFUSED' and set(q['evidence_keys'])<=set(r['evidence']),'Scenario promoted or unbound comparison')
 need(r['questions'][1]['disposition']=='ALIGNED_WITH_2008_RANGE_NOT_A_NEW_2008_DIFFERENCE','Invented journal/core range difference')
 need({f['id'] for f in r['findings']}=={f'CDNS267-F{i:02}' for i in range(1,9)} and len(r['findings'])==8 and all(f['next_issues']==[251,126] for f in r['findings']),'Findings lost')
 need(r['execution_summary']==dict(profile='FAIL_ONE_NON_SIMPLE_PROPERTY_CARDINALITY',reasoner='REFUSED_NON_SIMPLE_PROPERTY',consistent=None,unsatisfiable_named_classes=None,asserted_queries=dict(total=8,passed=8,failed=0),executed_consistency_scenarios=0,source_repair='NOT_PERFORMED'),'Summary promotion')
 need(r['boundary']==dict(model_change='NONE',requirements_change='NONE',fixtures_change='NONE',manuscript_change='NONE',release_change='NONE',source_change='NONE',source_redistribution=False,independent_expert_review='NOT_PERFORMED',scientific_acceptance='NOT_ASSESSED',adoption='OWNER_DECISION_REQUIRED'),'Boundary changed')
 need(r['selected_scope']['mapped_extension_reasoning']=='NOT_EXECUTED_OUTSIDE_SELECTED_CORE' and r['source']['historical_2007_fidelity']==r['source']['historical_2008_fidelity']=='NOT_ESTABLISHED','Extension/history promoted')
 return dict(status='PASS',issue=267,profile='FAIL_RECORDED',reasoner='REFUSED_RECORDED',logical_consistency=None,recorded_asserted_queries=8,correspondence_rows=8,executed_consistency_scenarios=0,scope='Evidence integrity only; no reasoner rerun or scientific acceptance')
def check(root=ROOT,source=None):
 r,e=load(root);out=validate(r,e)
 for x in [*r['evidence'].values(),r['model_baseline']]:
  if digest(root/x['path'])!=x['sha256']:raise ValueError('Stale evidence binding')
 if digest(root/e['generator_path'])!=e['generator_sha256'] or digest(root/'tools/inventory_review_artifact.py')!=e['inventory_helper_sha256']:raise ValueError('Changed executed generator')
 if (root/PATH).with_suffix('.md').read_text()!=render(r):raise ValueError('Stale readable review')
 ids={x['id'] for x in yaml.safe_load((root/'model/concepts.yaml').read_text())['records']}
 if any(not set(x['model_ids'])<=ids or x['status']!='OWNER_DECISION_REQUIRED' for x in r['candidate_uses']):raise ValueError('Unbound or accepted model mapping')
 if source is not None:
  from inventory_review_artifact import inventory
  current=inventory(source,SHA);old=json.loads((root/r['evidence']['core_census']['path']).read_text())
  if any(current[k]!=old[k] for k in ['classes','object_properties','counts','declared_import_iris','anonymous_restrictions']):raise ValueError('Exact source differs')
  out['exact_source_reparse']='PASS'
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path);a=p.parse_args();print(json.dumps(check(source=a.source),indent=2))
