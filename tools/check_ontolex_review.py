"""Check document identity, complete reading ledger and research claim boundaries."""
from pathlib import Path
import argparse,hashlib,json,re,yaml
from inspect_ontolex_document import SHA,URL,inspect
from render_ontolex_review import render
ROOT=Path(__file__).resolve().parents[1]
BASE='evidence/related-work/reviews/OntoLex.yaml'
BOUNDARY=dict(model_change='NONE',requirements_change='NONE',fixtures_change='NONE',manuscript_change='NONE',release_change='NONE',artifact_issue=237,comparison_issue=253,synthesis_issue=126,artifact_review_completed=False,reasoner_execution='NOT_EXECUTED',scientific_acceptance='NOT_ASSESSED',independent_expert_review='NOT_PERFORMED',adoption='OWNER_DECISION_REQUIRED',source_redistribution=False,full_paper_denominator_change=0)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(root=ROOT):
 r=yaml.safe_load((root/BASE).read_text());return r,{k:json.loads((root/v['path']).read_text()) for k,v in r['evidence'].items()}
def validate(r,data):
 def need(v,m):
  if not v:raise ValueError(m)
 need(r['issue']==75 and r['candidate_id']=='CLR-RW-OntoLex' and r['review_kind']=='OFFICIAL_COMMUNITY_DOCUMENT_CRITICAL_REVIEW' and r['status']=='COMPLETE_WITH_EXPLICIT_LIMITS','Wrong task or status')
 i=r['identity'];need(i['source_sha256']==SHA and i['source_bytes']==286046 and i['source_url']==URL and i['date']=='2016-05-10' and i['same_bytes_as_acquired'] is True,'Source substitution')
 need(i['doi'] is None and i['w3c_standard'] is False and i['document_type']=='Final Community Group Report','Document promoted')
 need(r['boundary']==BOUNDARY,'Scope or semantic execution promoted')
 c=data['document'];im=data['images'];need(c['source_sha256']==SHA and c['reasoner_execution']=='NOT_EXECUTED','Census source changed')
 need(len(c['headings'])==136 and len(c['numbered_sections'])==49 and len(c['term_heading_inventory'])==83 and len(c['images'])==69,'Incomplete census')
 sections=r['coverage']['numbered_sections'];need(len(sections)==49 and len({s['anchor'] for s in sections})==49,'Missing or duplicate sections')
 need([{k:s[k] for k in ['anchor','title']} for s in sections]==[{k:s[k] for k in ['anchor','title']} for s in c['numbered_sections']],'Reading ledger differs from document')
 need(all(s['state']=='READ_AND_CRITICALLY_REVIEWED' for s in sections),'Unread section')
 need(r['coverage']['document_term_heading_counts']=={'class':23,'object_property':44,'datatype_property':16},'Wrong heading populations')
 need(all(r['coverage'][x] is None for x in ['local_owl_classes','imported_owl_classes','inferred_owl_classes']),'Document inventory promoted to ontology census')
 need(im['source_html_sha256']==SHA and im['total_images']==im['inspected_images']==69 and im['failed_images']==0 and len(im['images'])==69,'Incomplete image inspection')
 need([x['id'] for x in im['images']]==[f'F{x:02}' for x in range(1,70)],'Image identifier mismatch')
 need([x['url'] for x in im['images']]==[x['url'] for x in c['images']],'Image source substitution')
 need([x['section_id'] for x in im['images']]==[x['nearest_heading'] for x in c['images']],'Image locator mismatch')
 for x in im['images']:
  need(x['visual_inspection']=='INSPECTED_ACTUAL_PIXELS' and x['semantic_validation']=='NOT_EXECUTED' and x['public_redistribution']=='NOT_REQUESTED_OR_PERFORMED' and re.fullmatch('[0-9a-f]{64}',x['sha256']) and x['width']>0 and x['height']>0,'Invalid image evidence')
  need('path' not in x,'Private path leaked')
 need({f['id'] for f in r['findings']}=={f'F{x:02}' for x in range(1,15)} and len(r['findings'])==14,'Missing or duplicate findings')
 need(len(r['dimensions'])==10 and len(r['adverse_cases'])==6,'Incomplete critical review')
 anchors=set(c['anchors'])
 for x in list(r['dimensions'].values())+r['findings']:
  need(x['locator'].startswith(URL+'#') and x['locator'].split('#')[-1] in anchors and bool(x['judgment']) and x['next_issues']==[237,253,126],'Unbound finding')
 for x in r['adverse_cases']:need(x['anchor'] in anchors and x['execution'] in {'CONCEPTUAL_REVIEW_ONLY','REVIEWER_CONSTRUCTED_NOT_SOURCE_EXPERIMENT'},'Unsupported experimental claim')
 need(r['decision']['disposition']=='ALIGNMENT_CANDIDATE_DEFER_ADOPTION' and r['decision']['novelty_priority']=='NOT_ASSESSED' and r['decision']['defer']==[237,253,126],'Unperformed synthesis/adoption promoted')
 need(r['rights']['raw_html_or_images_redistributed'] is False and r['rights']['legal_permission_assessment']=='NOT_PERFORMED','Rights invented')
 text=json.dumps([r,data]);need(not any(v in text for v in ['chatgpt.com/c/','/workspace/','file_000000','api_key','access_token']), 'Private data in public evidence')
 return {'status':'PASS','numbered_sections':49,'document_term_headings':83,'document_class_headings':23,'inspected_nonlogo_images':69,'critical_findings':14,'adverse_review_cases':6,'artifact_review_completed':False,'reasoner_execution':'NOT_EXECUTED','full_paper_denominator_change':0,'scope':'Document evidence and claim boundaries; not ontology semantic acceptance.'}
def check(root=ROOT,source=None):
 r,d=load(root);out=validate(r,d)
 for k,v in r['evidence'].items():
  if digest(root/v['path'])!=v['sha256']:raise ValueError('Evidence hash changed')
 if source is not None and inspect(source)!=d['document']:raise ValueError('Actual source inspection differs')
 if (root/BASE).with_suffix('.md').read_text()!=render(r,d['images']):raise ValueError('Stale rendered review')
 reg=yaml.safe_load((root/'evidence/related-work/deep-reviews/register.yaml').read_text())
 doc=next(x for x in reg['separate_document_tasks'] if x['id']=='OntoLex')
 if doc['state']!='OFFICIAL_DOCUMENT_REVIEW_COMPLETE' or doc['artifact_issue']!=237:raise ValueError('Document register drift')
 if len(reg['acquired_papers'])!=18 or len(reg['limited_evidence_papers'])!=1:raise ValueError('Paper denominator changed')
 out['source_reparsed']=source is not None;return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path);a=p.parse_args();print(json.dumps(check(source=a.source),indent=2))
