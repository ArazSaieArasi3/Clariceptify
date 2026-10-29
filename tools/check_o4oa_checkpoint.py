"""Guard an explicitly incomplete O4OA technical review and document-only evidence."""
from pathlib import Path
import argparse,collections,hashlib,json,re,yaml
from render_o4oa_checkpoint import render,ROOT,BASE
SHA='8bbcc649518217e34ca0f12b486fda58042d055da45792c7b6f706e5356bfdfb'
PAGES={8:11,9:7,10:15,11:9,12:16,13:9,14:10,15:11,16:15,17:9,18:13,19:10,20:3}
BOUNDARY=dict(model_change='NONE',requirements_change='NONE',fixtures_change='NONE',manuscript_change='NONE',release_change='NONE',reasoner_execution='NOT_EXECUTED',solver_execution='NOT_EXECUTED',api_execution='NOT_EXECUTED',machine_class_census='NOT_PERFORMED',source_redistribution=False,scientific_acceptance='NOT_ASSESSED',adoption='OWNER_DECISION_REQUIRED',full_paper_denominator_change=0,issue_must_remain_open=True)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(root=ROOT):
 r=yaml.safe_load((root/BASE).read_text());return r,{k:json.loads((root/v['path']).read_text()) for k,v in r['evidence'].items()}
def validate(r,d):
 def need(x,m):
  if not x:raise ValueError(m)
 need(r['issue']==91 and r['candidate_id']=='CLR-RW-O4OA' and r['status']=='PARTIAL_SPECIFICATION_REVIEW_BLOCKED_FORMAL_ARTIFACT' and r['issue_completion'] is False,'False technical closure')
 need(r['boundary']==BOUNDARY,'Scope or execution promotion')
 i=r['identity'];need(i['source_sha256']==SHA and i['pdf_pages']==44 and i['source_bytes']==4107800,'Source identity mismatch')
 need(i['document_version']=='1' and i['reference_ontology_version_at_front']=='2.6' and i['reference_ontology_version_in_conclusion']=='6.2' and i['version_conflict_resolved'] is False,'Source version discrepancy lost')
 need(all(i[x] is None for x in ['formal_root','formal_root_sha256','reference_repository_commit']),'Unacquired root promoted')
 pop=r['populations'];need(pop==dict(local_machine_classes=None,imported_machine_classes=None,inferred_machine_classes=None,document_table5_entries=138,document_cqs=24,document_figures=29,document_tables=16),'Document population promoted to machine census')
 a=d['discovery'];need(a['reference_root_acquired'] is False and a['reference_commit'] is None and a['global_absence_claim'] is False and a['license_permission']=='NOT_ESTABLISHED','Discovery overclaim')
 retrievals={x['id']:x for x in a['retrievals']};need(len(retrievals)==5 and retrievals['reference-tree']['status']==403 and retrievals['reference-project']['status']==200 and retrievals['light-tree']['status']==200,'Access result changed')
 need(retrievals['specification']['sha256']==SHA and a['light_tree_entries']==8 and a['light_tree_files']==5 and a['formal_root_in_selected_light_tree']=='NOT_IDENTIFIED','Discovery population mismatch')
 t=d['terms'];rows=t['rows'];need(t['source_sha256']==SHA and t['count']==138 and t['no_machine_population_claim'] is True and len(rows)==138,'Incomplete document inventory')
 need([x['id'] for x in rows]==[f'O4OA-SPEC-T5-{n:03}' for n in range(1,139)] and len({x['source_label'] for x in rows})==138,'Duplicate or missing document row')
 need(dict(collections.Counter(x['pdf_page'] for x in rows))==PAGES,'Page population mismatch')
 need(collections.Counter(x['definition_status'] for x in rows)=={'DESCRIPTIVE_SOURCE_CANDIDATE':125,'LABEL_ONLY':13},'Definition qualification lost')
 for x in rows:need(x['machine_class_iri'] is None and x['pdf_page']==x['printed_page'] and x['source_locator'].startswith('Table 5,') and x['statement_basis']=='REVIEWER_PARAPHRASE_OF_DOCUMENT_ROW' and bool(x['reviewer_paraphrase']),'Unbound or promoted document row')
 need([x['source_label'] for x in rows if x['source_stereotype'] is None]==['XML DTDs'],'Missing stereotype invented')
 l=d['reading'];need(l['source_sha256']==SHA and l['read_pages']==list(range(1,45)) and l['visually_inspected_pages']==list(range(1,45)),'Reading coverage incomplete')
 need([x['figure'] for x in l['figures']]==list(range(1,30)) and l['tables']==list(range(1,17)) and l['bibliography_entries']==79,'Visual/table coverage incomplete')
 need(l['execution']=='DOCUMENT_REVIEW_ONLY' and l['solver_execution']=='NOT_EXECUTED' and l['expert_acceptance']=='NOT_ASSESSED','Reading promoted to execution')
 need([q['id'] for q in r['questions']]==[f'Q{n:02}' for n in range(1,9)] and all(q['status'] not in ['PASS','COMPLETE'] for q in r['questions']),'Question obligation hidden')
 f={x['id'] for x in r['findings']};need(f=={f'O4OA91-F{n:02}' for n in range(1,18)} and len(r['findings'])==17,'Findings incomplete')
 for x in r['findings']:need(x['locator'].startswith('Specification ') and x['next_issues']==[91,252,126] and bool(x['judgment']),'Unbound finding')
 for q in r['questions']:need(set(q['finding_ids'])<=f,'Unknown finding')
 need(len(r['conceptual_adverse_cases'])==5 and all(x['execution']=='REVIEWER_CONCEPTUAL_ANALYSIS_NOT_SOLVER_RUN' for x in r['conceptual_adverse_cases']),'Conceptual case promoted')
 need(r['closure']['decision']=='KEEP_ISSUE_91_OPEN' and r['closure']['AC-ALL-CLASSES']=='BLOCKED_NO_RELEASED_ROOT' and r['closure']['AC-1']=='BLOCKED_NO_FORMAL_ARTIFACT','Missing artifact gate removed')
 text=json.dumps([r,d]);need(not any(x in text for x in ['chatgpt.com/c/','/workspace/','file_000000','access_token','api_key']),'Private data in public evidence')
 return dict(status='PASS',scope='Evidence integrity and blocked completion guards, not technical/scientific acceptance',issue_completion=False,document_rows=138,document_figures=29,document_tables=16,findings=17,reasoner_execution='NOT_EXECUTED')
def check(root=ROOT,source=None):
 r,d=load(root);out=validate(r,d)
 for v in r['evidence'].values():
  if digest(root/v['path'])!=v['sha256']:raise ValueError('Evidence hash mismatch')
 if source is not None:
  if digest(source)!=SHA:raise ValueError('Wrong PDF bytes')
  import fitz
  doc=fitz.open(source)
  for n in PAGES:
   raw=doc[n-1].get_text('text',clip=fitz.Rect(425,205 if n==8 else 145,478,245 if n==20 else (600 if n in [10,14,16] else 640)))
   printed=[' '.join(s.split()) for s in re.findall(r'<<\s*(.*?)\s*>>',raw,re.S)]
   recorded=[x['source_stereotype'] for x in d['terms']['rows'] if x['pdf_page']==n and x['source_stereotype'] is not None]
   if printed!=recorded:raise ValueError('Printed stereotype sequence mismatch')
 if (root/BASE).with_suffix('.md').read_text()!=render(r,d):raise ValueError('Stale rendered checkpoint')
 audit=yaml.safe_load((root/'evidence/related-work/deep-reviews/source-audit.yaml').read_text());row=next(x for x in audit['records'] if x['id']=='CLR-RW-O4OA')
 if row['class_coverage']['local_classes'] is not None or row['class_coverage']['catalog_path'] is not None or row['class_coverage']['reasoner_execution']!='NOT_EXECUTED' or 91 not in row['next_issues']:raise ValueError('Audit silently completed technical work')
 out['exact_pdf_verified']=source is not None;return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path);a=p.parse_args();print(json.dumps(check(source=a.source),indent=2))
