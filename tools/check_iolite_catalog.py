"""Verify IOLite's complete source-bound glossary and unique-IRI import coverage.

Default checks are offline and dependency-light, not an OWL reasoner. --source-dir
reparses four exact private inputs using optional research dependencies.
"""
from pathlib import Path
import argparse,hashlib,json,yaml
from inspect_iolite_source import NS,SHA,digest,inspect
from check_source_audit import validate_catalog
ROOT=Path(__file__).resolve().parents[1]
BASE='evidence/related-work/deep-reviews/shared-foundations/IOLite'
DUL='http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#'
BUILTIN='http://www.w3.org/2002/07/owl#Thing'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(root=ROOT):
 b=root/BASE
 return yaml.safe_load((b/'classes.yaml').read_text()),json.loads((b/'source-reconciliation.json').read_text()),json.loads((b/'IOLite-census.json').read_text())
def validate(cat,source,census,root=ROOT):
 validate_catalog(cat,{'IOLite':census})
 if cat['issue']!=271 or cat['modules'][0]['source_sha256']!=SHA or source['source_sha256']!=SHA:raise ValueError('Source identity changed')
 if source['reasoner_execution']!='NOT_EXECUTED' or source['unresolved_imports'] or cat['logical_inference']!='NOT_EXECUTED':raise ValueError('Unsupported semantic/import claim')
 if sha(root/source['generator']['path'])!=source['generator']['sha256']:raise ValueError('Source inspector changed')
 if sha(root/census['generator']['path'])!=census['generator']['sha256']:raise ValueError('Census generator changed')
 if sha(root/cat['modules'][0]['census_path'])!=cat['modules'][0]['census_sha256']:raise ValueError('Census binding changed')
 rows=cat['classes'];irs=sorted(r['iri'] for r in rows)
 if len(irs)!=46 or len(set(irs))!=46 or digest(irs)!='15ab9f07a4f9f3f91f3445852be3436a1461e51c083d4c2a6bfa72e9010a5354':raise ValueError('Wrong local class set')
 if cat['counts']!={'local_classes':46,'source_definition_candidates':43,'missing_source_definitions':3,'reviewer_reconstructions':0,'inferred_classes':None}:raise ValueError('Definition counts changed')
 missing={NS+x for x in ['DigitalPhoto','Gesture','WebPage']}
 by={r['iri']:r for r in source['rows']}
 if set(by)!=set(irs):raise ValueError('Source census misses local classes')
 for r in rows:
  a=by[r['iri']]
  for k in ['label','label_basis','deprecated','annotation_records','named_superclasses','equivalent_expressions']:
   if r[k]!=a[k]:raise ValueError('Source field changed: '+k)
  d=r['source_definition']
  if d['annotation_sha256']!=a['annotation_sha256']:raise ValueError('Comment provenance changed')
  if (d['status']=='NOT_REPORTED_IN_SELECTED_SOURCE')!=(r['iri'] in missing):raise ValueError('Missing definition invented')
  if r['constraint_ref']!=BASE+'/IOLite-census.json classes[iri='+r['iri']+']':raise ValueError('Unbound class constraints')
 if cat['modules'][0]['other_class_populations']!=source['populations']:raise ValueError('Population ledger changed')
 p=source['populations']
 if p['local_named_classes']!=irs or len(p['external_redeclarations'])!=20 or p['anonymous_class_declarations']!=3 or p['anonymous_restrictions']!=40 or p['referenced_undeclared_nonbuiltin_classes'] or p['deprecated_named_classes'] or p['named_rdfs_class_declarations']:raise ValueError('Other class population changed')
 declared={r['iri'] for r in census['classes']}
 if declared!=set(irs)|set(p['external_redeclarations']) or census['explicit_triples']!=666:raise ValueError('Full census differs')
 mods={m['id']:m for m in source['modules']}
 if set(mods)!={'DUL','IOLite','LMM_L1','LMM_L2'}:raise ValueError('Wrong import boundary')
 specs=yaml.safe_load((root/'evidence/related-work/corpus/lmm-inputs.yaml').read_text())['artifacts']
 by_iri={s['ontology_iri']:s['id'] for s in specs};all_local=set()
 for s in specs:
  m=mods[s['id']]
  if m['source_sha256']!=s['sha256'] or m['namespace']!=s['namespace'] or m['inferred_class_count'] is not None:raise ValueError('Module identity/inference changed')
  todo=[s['id']]; seen=set(); union=set()
  while todo:
   n=todo.pop()
   if n in seen:continue
   seen.add(n); other=mods[n];union.update(other['local_class_iris']);union.update(other['external_redeclaration_iris'])
   for i in other['declared_import_iris']:
    if i not in by_iri:raise ValueError('Unresolved import')
    todo.append(by_iri[i])
  if sorted(seen)!=m['resolved_closure_modules'] or sorted(union)!=m['asserted_closure_class_iris']:raise ValueError('Closure union mismatch')
  if all_local & set(m['local_class_iris']):raise ValueError('Duplicate local ownership')
  all_local.update(m['local_class_iris'])
 if {k:len(v['local_class_iris']) for k,v in mods.items()}!={'DUL':78,'IOLite':46,'LMM_L1':8,'LMM_L2':21}:raise ValueError('Local module counts changed')
 if {k:len(v['asserted_closure_class_iris']) for k,v in mods.items()}!={'DUL':79,'IOLite':125,'LMM_L1':133,'LMM_L2':154}:raise ValueError('Wrong unique-IRI closure count')
 if set(mods['LMM_L2']['asserted_closure_class_iris'])!=all_local|{BUILTIN}:raise ValueError('Unaccounted closure class')
 if p['external_redeclarations']!=mods['IOLite']['external_redeclaration_iris'] or not set(p['external_redeclarations'])<=set(mods['DUL']['asserted_closure_class_iris']):raise ValueError('External class not covered by DUL')
 dul=yaml.safe_load((root/'evidence/related-work/dul-class-catalog.yaml').read_text());lmm=yaml.safe_load((root/'evidence/related-work/deep-reviews/LMM2008/classes.yaml').read_text())
 if set(mods['DUL']['local_class_iris'])!={r['iri'] for r in dul['classes']} or set(mods['LMM_L1']['local_class_iris']+mods['LMM_L2']['local_class_iris'])!={r['iri'] for r in lmm['classes']}:raise ValueError('Shared glossary set mismatch')
 coverage=[]
 for r in dul['classes']:coverage.append({'iri':r['iri'],'catalog':'evidence/related-work/dul-class-catalog.yaml','definition_state':r['source_definition']['status']})
 for c,path in [(cat,BASE+'/classes.yaml'),(lmm,'evidence/related-work/deep-reviews/LMM2008/classes.yaml')]:
  for r in c['classes']:coverage.append({'iri':r['iri'],'catalog':path,'definition_state':r['source_definition']['status']})
 coverage.append({'iri':BUILTIN,'catalog':None,'definition_state':'BUILTIN_NOT_SOURCE_GLOSSARY'})
 if len(coverage)!=154 or len({x['iri'] for x in coverage})!=154:raise ValueError('Duplicate/missing closure glossary entry')
 if cat['foundation']['relation']!='ACTUAL_IMPORT' or cat['foundation']['edition']!='IOLite1.8 imports retained DUL4.2' or cat['historical_paper_fidelity']!='NOT_ESTABLISHED':raise ValueError('Unsupported foundation/historical claim')
 if cat['imported_glossary']['unique_external_classes_pending']!=0 or cat['imported_glossary']['catalog_path']!='evidence/related-work/dul-class-catalog.yaml':raise ValueError('Unbound imported glossary')
 return {'status':'PASS','local_classes':46,'comment_candidates_reviewed':43,'missing_comments':3,'external_redeclarations':20,'lmm_asserted_closure_classes':154,'local_source_classes':153,'builtin_classes':1,'coverage':sorted(coverage,key=lambda x:x['iri']),'reasoner_execution':'NOT_EXECUTED','model_change':'NONE','scope':'All selected definitions accounted for, including explicit gaps; not all definitions available or scientifically adequate.'}
def check(root=ROOT,source_dir=None):
 cat,source,census=load(root);r=validate(cat,source,census,root)
 if source_dir is not None:
  fresh=inspect(source_dir)
  if fresh!=source:raise ValueError('Actual source inspection differs from recorded evidence')
  from inventory_review_artifact import inventory
  fresh_census=inventory(Path(source_dir)/'IOLite.owl',SHA)
  if fresh_census!=census:raise ValueError('Actual complete constraint census differs')
 recorded=json.loads((root/BASE/'closure-coverage.json').read_text())
 expected={**r,'source_reparsed':True}
 if recorded!=expected:raise ValueError('Recorded closure coverage differs from shared catalogues')
 r['source_reparsed']=source_dir is not None
 return r
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source-dir',type=Path);p.add_argument('--output',type=Path);a=p.parse_args();r=check(source_dir=a.source_dir)
 if a.output:a.output.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:v for k,v in r.items() if k!='coverage'},indent=2))
