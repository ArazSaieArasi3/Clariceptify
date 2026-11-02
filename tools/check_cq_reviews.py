"""Integrity/coverage of manual CQ reviews, not execution of the ontology."""
import argparse
import hashlib
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
class CQReviewError(ValueError):pass

def require(ok,message):
    if not ok:raise CQReviewError(message)

def read(path):return yaml.safe_load((ROOT/path).read_text())

def validate(report,batch):
    issue=122+batch
    require(report['issue']==issue and report['task_id']==f'R2-CQ-{batch}','review identity')
    require(report['status']=='MANUAL_FULL_CONTRACT_REVIEW_COMPLETE_WITH_OPEN_FINDINGS','review not satisfaction')
    require(report['model_tree']=='3e2d5b627af1b92cdb70c6bd7198868fa784e977','model tree')
    require(len(report['baseline_commit'])==40,'baseline ref')
    required={'requirements/functional.yaml','requirements/competency-questions.yaml','requirements/scope-and-scenarios.yaml','traceability/requirements-model.yaml','model/concepts.yaml','model/relations.yaml','model/generalizations.yaml','model/constraints.yaml'}
    require(required<=report['input_bindings'].keys(),'missing input family')
    for path,digest in report['input_bindings'].items():require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'stale input '+path)
    fdata=read('requirements/functional.yaml');frs={r['id']:r for r in fdata['records']};cqs={r['id']:r for r in read('requirements/competency-questions.yaml')['records']}
    require(report['origins']==fdata['origins'] and report['requirement_status']==fdata['status'],'retrospective origin boundary')
    expected=[f'CQ-{i:02d}' for i in range((batch-1)*10+1,batch*10+1)]
    require([r['cq_id'] for r in report['records']]==expected,'ten frozen CQ denominator')
    ids=set()
    for p in ['model/concepts.yaml','model/relations.yaml','model/generalizations.yaml','model/constraints.yaml']:
        ids.update(r['id'] for r in read(p)['records'])
    for i,row in enumerate(report['records'],1):
        cq=cqs[row['cq_id']];fr=frs[cq['requirement_id']]
        require(row['fr_id']==fr['id'],'FR/CQ correspondence')
        require(row['frozen_cq_contract']==cq and row['frozen_fr_contract']==fr,'frozen contract changed')
        require(row['origin']==fr['origin'],'origin promoted')
        fields={v.strip() for v in cq['required_answer_fields'].split(';')}
        require(set(row['answer_field_review'])==fields,'required answer-field coverage')
        require(all(isinstance(v,str) and v.strip() for v in row['answer_field_review'].values()),'empty field assessment')
        for case in ['positive_case','adverse_case']:
            require(all(row[case].get(f) for f in ['scenario','expected','observed']),'missing expected/observed case')
        require(row['model_evidence_ids'] and set(row['model_evidence_ids'])<=ids,'unknown or missing evidence IDs')
        require(row['finding_id']==f'CQ{issue}-F{i:02d}','finding identity')
        require(row['finding'] and row['manual_conclusion'] and row['analysis'],'manual reasoning missing')
        require(row['decision_gate']=='unapproved_joint_user_decision_129' and row['model_changes']=='none','unapproved change')
        require(row['executable_semantics']=='not_executed' and row['human_expert_validation']=='not_assessed','manual review promoted')
    return len(expected)

def main():
    p=argparse.ArgumentParser();p.add_argument('--batch',type=int,choices=[1,2,3],required=True);batch=p.parse_args().batch
    count=validate(read(f'evaluation/cq-review/batch-{batch}.yaml'),batch)
    print(f'PASS: {count} frozen CQ review records, all answer fields/positive/adverse evidence present; no executable semantic PASS or expert acceptance claimed')
if __name__=='__main__':main()
