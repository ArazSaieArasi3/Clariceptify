"""Check review provenance/state boundaries, not correctness of scientific judgment."""
from pathlib import Path
import hashlib,json
import yaml
ROOT=Path(__file__).resolve().parents[1]

def require(condition,message):
    if not condition:raise ValueError(message)

def check(root=ROOT):
    record=yaml.safe_load((root/'evaluation/review-state.yaml').read_text())
    allowed={'PASS','FAIL','BLOCKED','NOT_ASSESSED','NOT_APPLICABLE'}
    types={'machine','agent_assisted','author','simulated','independent_expert'}
    for review in record['reviews']:
        require(review['type'] in types and review['result'] in allowed,'Unknown review type or result')
        require(review['reviewed_ref'] and review['scope'] and review['reviewer'],'Missing review provenance')
        if review['type'] in {'author','independent_expert'}:
            require(review['result']=='NOT_ASSESSED' or (review.get('actual_decision_record') and review.get('reviewed_package_ref')),'Human decision evidence is missing')
        if review['result'] in {'PASS','FAIL'}:require(review['evidence'],'Assessment evidence is missing')
        for evidence in review['evidence']:
            require(hashlib.sha256((root/evidence['path']).read_bytes()).hexdigest()==evidence['sha256'],'Evidence digest mismatch: '+evidence['path'])
    for finding in record['findings']:
        require(all(finding.get(k) for k in ('id','reviewed_ref','type','severity','owner','disposition','tracking_issue')),'Missing finding field')
        require(finding['disposition'] in {'OPEN','IN_PROGRESS','RESOLVED','DEFERRED','ACCEPTED_LIMITATION'},'Unknown finding disposition')
        if finding['disposition']=='RESOLVED':require(finding.get('resolution_evidence'),'Resolution evidence missing')
    return {'status':'PASS','scope':'Review-state structure and actual evidence hashes; no scientific approval inferred','reviews':len(record['reviews']),'findings':len(record['findings']),'review_state_sha256':hashlib.sha256((root/'evaluation/review-state.yaml').read_bytes()).hexdigest()}

if __name__=='__main__':print(json.dumps(check(),indent=2))
