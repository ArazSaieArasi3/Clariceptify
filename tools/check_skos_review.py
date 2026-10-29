"""Check complete SKOS document evidence without promoting unexecuted semantics."""
from pathlib import Path
import argparse,hashlib,json,re,yaml
from inspect_skos_document import SHA,URL,ERRATA_SHA,ERRATA_URL,inspect
from render_skos_review import render
ROOT=Path(__file__).resolve().parents[1]
BASE='evidence/related-work/reviews/SKOS.yaml'
COUNTS=dict(badges=2,numbered_examples=90,sections=143,semantic_statements=62,substantive_image_figures=0,text_diagrams=2)
BOUNDARY=dict(model_change='NONE',requirements_change='NONE',fixtures_change='NONE',manuscript_change='NONE',release_change='NONE',artifact_issue=238,comparison_issue=253,synthesis_issue=126,artifact_review_completed=False,reasoner_execution='NOT_EXECUTED',scientific_acceptance='NOT_ASSESSED',independent_expert_review='NOT_PERFORMED',adoption='OWNER_DECISION_REQUIRED',source_redistribution=False,full_paper_denominator_change=0)
ERRATA_IDS=['SKOS-DL-versionIRI','DCT-abbrev','HTML-namespace','S14','love77','skos-vs-skos-xl','xl-integrity-constraints','ISO-Correspondences','SPARQL-variable-typo','narrower-scopeNote','missing-tags']
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(root=ROOT):
 r=yaml.safe_load((root/BASE).read_text());return r,{k:json.loads((root/v['path']).read_text()) for k,v in r['evidence'].items()}
def validate(r,data):
 def need(v,m):
  if not v:raise ValueError(m)
 need(r['issue']==76 and r['candidate_id']=='CLR-RW-SKOS' and r['review_kind']=='W3C_RECOMMENDATION_DOCUMENT_CRITICAL_REVIEW' and r['status']=='COMPLETE_WITH_EXPLICIT_LIMITS','Wrong task or promoted status')
 i=r['identity'];need(i['source_sha256']==SHA and i['source_bytes']==227150 and i['source_url']==URL and i['date']=='2009-08-18' and i['same_bytes_as_acquired'] is True,'Source substitution')
 need(i['doi'] is None and i['w3c_standard'] is True and i['document_type']=='W3C Recommendation' and i['primer_review']=='NOT_PERFORMED','Source identity promoted or substituted')
 need(r['boundary']==BOUNDARY,'Scope or semantic execution promoted')
 c=data['document'];ledger=data['reading'];e=data['errata']
 need(c['source_sha256']==SHA and c['source_bytes']==227150 and c['reasoner_execution']=='NOT_EXECUTED' and c['counts']==COUNTS,'Census source or population changed')
 need(len(c['headings'])==149 and len(c['sections'])==143 and len(c['anchors'])==419,'Incomplete census')
 sections=r['coverage']['sections'];need(len(sections)==143 and len({s['key'] for s in sections})==143,'Missing or duplicate sections')
 need([{k:v for k,v in s.items() if k!='state'} for s in sections]==c['sections'],'Reading ledger differs from source')
 need(all(s['state']=='READ_AND_CRITICALLY_REVIEWED' for s in sections),'Unread section')
 need(r['coverage']['counts']==COUNTS and r['coverage']['document_vocabulary_counts']==dict(core_classes=4,core_properties=28,xl_classes=1,xl_properties=5),'Wrong document populations')
 need(all(r['coverage'][x] is None for x in ['local_owl_classes','imported_owl_classes','inferred_owl_classes']),'Document table promoted to ontology census')
 need(ledger['source_sha256']==SHA and ledger['review_method']=='AI_ASSISTED_FULL_DOCUMENT_READING_NOT_REASONER_EXECUTION','Wrong reading provenance')
 need([x['id'] for x in ledger['statements']]==[f'S{x}' for x in range(1,63)],'Missing or duplicate statements')
 need([x['id'] for x in ledger['examples']]==[f'example-{x}' for x in range(1,91)],'Missing or duplicate examples')
 for group in ['statements','examples','text_diagrams']:
  need(len(ledger[group])==len(c[group]),'Reading population mismatch')
  for x,y in zip(ledger[group],c[group]):
   need(all(x[k]==v for k,v in y.items()) and x['reading_state']=='READ_AND_CRITICALLY_REVIEWED','Reading binding differs')
   for k,v in x.items():
    if k.endswith('sha256'):need(re.fullmatch('[0-9a-f]{64}',v),'Invalid source row digest')
 need({x['id'] for x in ledger['statements'] if x['classification']=='INTEGRITY_CONDITION'}=={'S9','S13','S14','S27','S37','S46','S48','S58'},'Integrity classification or errata lost')
 need(all(x['execution']=='DOCUMENT_REVIEW_ONLY' for x in ledger['statements']) and all(x['result_origin']=='SOURCE_STATED_NOT_INDEPENDENTLY_EXECUTED' for x in ledger['examples']),'Source example promoted to own test')
 need(len(c['images'])==2 and all(x['role']=='BADGE_NOT_CONTENT_FIGURE' for x in c['images']) and len(c['text_diagrams'])==2,'Visual scope changed')
 need(e['sha256']==ERRATA_SHA and e['url']==ERRATA_URL and e['primary_source_unchanged'] is True and e['primer_full_review']=='NOT_PERFORMED' and e['artifact_changes']=='NOT_PERFORMED','Errata scope/source drift')
 need([x['id'] for x in e['entries']]==ERRATA_IDS and all(x['locator']==ERRATA_URL+'#'+x['id'] and x['reviewer_disposition'] for x in e['entries']),'Missing or substituted erratum')
 need({f['id'] for f in r['findings']}=={f'F{x:02}' for x in range(1,22)} and len(r['findings'])==21,'Missing or duplicate findings')
 need(len(r['dimensions'])==10 and len(r['adverse_cases'])==9,'Incomplete critical review')
 anchors=set(c['anchors'])
 for x in list(r['dimensions'].values())+r['findings']:
  need(x['locator'].startswith(URL+'#') and x['locator'].split('#')[-1] in anchors and bool(x['judgment']) and x['next_issues']==[238,253,126],'Unbound finding')
 for x in r['adverse_cases']:need(x['anchor'] in anchors and x['execution']=='REVIEWER_CONCEPTUAL_ANALYSIS_NOT_REASONER_TEST','Unsupported experimental claim')
 need(r['decision']['disposition']=='ALIGNMENT_CANDIDATE_DEFER_ADOPTION' and r['decision']['novelty_priority']=='NOT_ASSESSED' and r['decision']['defer']==[238,253,126],'Unperformed synthesis/adoption promoted')
 need(r['rights']['raw_html_or_images_redistributed'] is False and r['rights']['legal_permission_assessment']=='NOT_PERFORMED','Rights invented')
 text=json.dumps([r,data]);need(not any(v in text for v in ['chatgpt.com/c/','/workspace/','file_000000','api_key','access_token']),'Private data in public evidence')
 return dict(status='PASS',**COUNTS,critical_findings=21,conceptual_adverse_cases=9,official_errata_entries=11,artifact_review_completed=False,reasoner_execution='NOT_EXECUTED',full_paper_denominator_change=0,scope='Document evidence and claim boundaries only; not schema validation or scientific acceptance.')
def check(root=ROOT,source=None,errata=None):
 r,d=load(root);out=validate(r,d)
 for k,v in r['evidence'].items():
  if digest(root/v['path'])!=v['sha256']:raise ValueError('Evidence hash changed')
 if source is not None and inspect(source)!=d['document']:raise ValueError('Actual source inspection differs')
 if errata is not None and digest(errata)!=ERRATA_SHA:raise ValueError('Wrong errata bytes')
 if (root/BASE).with_suffix('.md').read_text()!=render(r,d):raise ValueError('Stale rendered review')
 reg=yaml.safe_load((root/'evidence/related-work/deep-reviews/register.yaml').read_text());doc=next(x for x in reg['separate_document_tasks'] if x['id']=='SKOS')
 if doc['state']!='OFFICIAL_DOCUMENT_REVIEW_COMPLETE' or doc['artifact_issue']!=238:raise ValueError('Document register drift')
 if len(reg['acquired_papers'])!=18 or len(reg['limited_evidence_papers'])!=1:raise ValueError('Paper denominator changed')
 out['source_reparsed']=source is not None;out['errata_bytes_verified']=errata is not None;return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path);p.add_argument('--errata',type=Path);a=p.parse_args();print(json.dumps(check(source=a.source,errata=a.errata),indent=2))
