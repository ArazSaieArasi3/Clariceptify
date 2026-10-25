"""Check controlled publication completeness and planned/actual VVEAA boundaries."""
from pathlib import Path
import hashlib,json,tempfile
import yaml
from build_documentation import build,GUIDES
from build_manuscript_figure import build as build_figure

ROOT=Path(__file__).resolve().parents[1]
def check(root=ROOT):
    profile=yaml.safe_load((root/'evaluation/vveaa-profile.yaml').read_text())
    if [r['id'] for r in profile['layers']]!=['Verification','Validation','Evaluation','Assessment','Assurance']:raise ValueError('Missing or conflated VVEAA function')
    for layer in profile['layers']:
        if not all(layer.get(k) for k in ['purpose','method','indicators','r2_tasks','claim_boundary']):raise ValueError('Incomplete evidence obligation')
        for indicator in layer['indicators']:
            if 'denominator' not in indicator or not indicator.get('population'):raise ValueError('Indicator population/denominator missing')
    report=yaml.safe_load((root/'evaluation/vveaa-report.yaml').read_text())
    if report['profile_sha256']!=hashlib.sha256((root/'evaluation/vveaa-profile.yaml').read_bytes()).hexdigest():raise ValueError('Stale profile report')
    if report['overall_quality_score'] is not None:raise ValueError('An aggregate score cannot replace evidence gates')
    for row in report['layers']:
        if row['r2_execution']!='NOT_ASSESSED':raise ValueError('Unperformed R2 review was promoted')
        for e in row['actual_evidence']:
            if hashlib.sha256((root/e['path']).read_bytes()).hexdigest()!=e['sha256']:raise ValueError('Evidence hash mismatch')
    protocol=yaml.safe_load((root/'evidence/related-work/review-protocol.yaml').read_text())
    if len(protocol['seed_access_register'])!=19 or any(r['class_count'] is not None for r in protocol['seed_access_register']):raise ValueError('Recovered labels were promoted to reviewed counts')
    with tempfile.TemporaryDirectory() as temp:
        figure=Path(temp)/'selected-r1.svg';selection=build_figure(root,figure)
        if figure.read_bytes()!=(root/'docs/research/figures/selected-r1.svg').read_bytes():raise ValueError('Manuscript figure differs from authoritative selected rows')
        if selection['unique_concepts']!=13 or selection['selected_associations']!=14:raise ValueError('Manuscript selection count changed without a revision')
    manuscript=yaml.safe_load((root/'docs/research/manuscript-contract.yaml').read_text())
    for path,sha in manuscript['asset_sha256'].items():
        if hashlib.sha256((root/path).read_bytes()).hexdigest()!=sha:raise ValueError('Stale manuscript asset binding: '+path)
    if len(manuscript['cq_bindings'])!=30 or any(q['test_execution']!='not_executed' for q in manuscript['cq_bindings']):raise ValueError('Draft alignment promoted global CQ execution')
    draft_review=json.loads((root/'evaluation/manuscript/r1-draft-review.json').read_text())
    if draft_review['page_count']!=8 or draft_review['docx_sha256']!=manuscript['output']['sha256']:raise ValueError('Manuscript review identity mismatch')
    with tempfile.TemporaryDirectory() as temp:result=build(root,temp,'checked-working-snapshot')
    if result['concepts']!=137 or result['domains']!=21 or result['principal_cqs']!=30 or result['guide_pages']!=len(GUIDES):raise ValueError('Incomplete conceptual documentation')
    return {'status':'PASS','scope':'Controlled guide/reference completeness, local HTML paths/anchors and explicit VVEAA protocol/report boundaries; not publication or scientific validation.','guide_pages':result['guide_pages'],'wiki_files':result['wiki_files'],'concepts':result['concepts'],'domains':result['domains'],'principal_cqs':result['principal_cqs'],'site_audit':result['audit'],'input_path_digest_sha256':result['source_path_digest_sha256']}

if __name__=='__main__':print(json.dumps(check(),indent=2))
