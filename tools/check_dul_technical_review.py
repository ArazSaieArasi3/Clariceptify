"""Check recorded DUL research evidence integrity, not rerun HermiT or validate meaning."""
from pathlib import Path
import hashlib,json,yaml
from check_dul_class_catalog import validate as validate_catalog
ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(root=ROOT):
 r=yaml.safe_load((root/'evidence/related-work/artifacts/DUL-technical-review.yaml').read_text())
 if r['source_root']['sha256']!='e5f6429596d2c7014730bad85aaaa9c39530235f27f596cd0e7ce85e6bbcba66':raise ValueError('Changed root source')
 if r['boundary']!={'model_change':'NONE','requirements_change':'NONE','manuscript_change':'NONE','release_change':'NONE','source_redistribution':False,'scientific_acceptance':'NOT_ASSESSED','independent_expert_review':'NOT_PERFORMED','adoption':'OWNER_DECISION_REQUIRED'}:raise ValueError('Unjustified acceptance or scope expansion')
 if {x['id'] for x in r['questions']}!={f'Q{i:02}' for i in range(1,9)} or len(r['questions'])!=8:raise ValueError('Incomplete eight-question scope')
 for ref in [r['chapter_evidence'],*r['evidence'].values()]:
  if digest(root/ref['path'])!=ref['sha256']:raise ValueError('Changed evidence binding')
 cat=yaml.safe_load((root/r['evidence']['class_catalog']['path']).read_text());cr=validate_catalog(cat)
 if cr['status']!='PASS':raise ValueError('Invalid complete class catalog: '+str(cr['errors']))
 receipt=json.loads((root/r['evidence']['class_checks']['path']).read_text())
 if receipt['status']!='PASS' or receipt['catalog_sha256']!=digest(root/r['evidence']['class_catalog']['path']) or receipt['checker_sha256']!=digest(root/'tools/check_dul_class_catalog.py'):raise ValueError('Stale glossary check receipt')
 semantic=json.loads((root/r['evidence']['semantic_tests']['path']).read_text())
 modules=json.loads((root/r['evidence']['module_closure']['path']).read_text())
 for record in [semantic,modules]:
  if digest(root/record['generator_path'])!=record['generator_sha256']:raise ValueError('Changed executed generator')
 tests=semantic['tests']
 if len(tests)!=29 or len({x['id'] for x in tests})!=29:raise ValueError('Incomplete semantic cases')
 for t in tests:
  if t['result']!='PASS' or not isinstance(t['observed_consistent'],bool) or t['observed_consistent'] is not t['expected_consistent'] or t['error'] is not None:raise ValueError('Unsuccessful semantic case')
  if hashlib.sha256(t['fixture_nt'].encode()).hexdigest()!=t['fixture_sha256']:raise ValueError('Changed semantic fixture')
 if semantic['summary']!={'total':29,'passed':29,'failed':0,'errors':0}:raise ValueError('Wrong semantic denominator')
 if semantic['source_sha256']!=r['source_root']['sha256'] or semantic['source_imports']!=[]:raise ValueError('Semantic source substitution')
 if len(modules['roots'])!=9 or len(modules['modules'])!=21 or modules['unresolved'] or any(x['unresolved_files'] for x in modules['closures']):raise ValueError('Unresolved or changed module closure')
 if modules['source_redistributed'] or modules['historical_2016_byte_parity']!='NOT_ESTABLISHED':raise ValueError('Unsupported source claim')
 if len({f['id'] for f in r['findings']})!=8 or any(f['next_issue'] not in [251,126] for f in r['findings']):raise ValueError('Untracked findings')
 findings={x['id'] for x in r['findings']}
 for q in r['questions']:
  if not q['result'] or not q['chapter_evidence'] or not set(q['evidence'])<=set(r['evidence']) or not set(q['finding_ids'])<=findings:raise ValueError('Unbound question')
 return {'status':'PASS','questions':8,'local_classes':78,'recorded_semantic_tests':29,'pattern_roots':9,'pattern_closure_files':21,'scope':'Evidence/claim integrity only. Recorded HermiT outcomes are not re-executed by this checker. No scientific acceptance.'}
if __name__=='__main__':print(json.dumps(check(),indent=2))
