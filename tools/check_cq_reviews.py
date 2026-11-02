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

MANUAL_STATUSES = {1: {'ac_assessment': ['conceptually_supported', 'conceptually_supported_for_artifact_scoped_input', 'conceptually_supported_for_recorded_abstraction', 'conceptually_supported_given_compatibility_record', 'conceptually_supported_textually', 'partial'], 'nac_assessment': ['conceptually_supported', 'conceptually_supported_not_formally_enforced', 'conceptually_supported_textually', 'conceptually_supported_with_query_scope', 'partial_terminological_mismatch'], 'conclusion': ['completed_with_limitations']}, 2: {'ac_assessment': ['bounded_manual_support', 'partial_support_metalevel_interpretation_unresolved'], 'nac_assessment': ['manual_support_not_automated'], 'conclusion': ['bounded_manual_support', 'partial_support_metalevel_interpretation_unresolved']}, 3: {'conclusion': ['BOUNDED_MANUAL_CONTRACT_SUPPORT_EXECUTION_UNASSESSED', 'CONCEPTUALLY_CONDITIONAL_COMPARISON_POLICY_REQUIRED', 'CONCEPTUALLY_SUPPORTED_FROZEN_SCOPE', 'CONCEPTUALLY_SUPPORTED_RECORDED_USE_AND_ARTICULATION_WITH_CAUSAL_SCOPE_LIMITATION', 'CONCEPTUALLY_SUPPORTED_SELECTED_CASE_WITH_SCOPE_LIMITATION', 'CONCEPTUALLY_SUPPORTED_SINGLE_ARTIFACT_CRITERION_CASE', 'CONCEPTUALLY_SUPPORTED_TEXTUAL_ATOMICITY_AND_ALIGNMENT', 'CONCEPTUALLY_SUPPORTED_WITH_CONTEXT_QUALIFICATION', 'PARTIAL_OPERATION_DISAMBIGUATION_WITH_OPTIONAL_SCOPE_QUESTION']}}

def validate_analysis(row, cq, fr, batch):
    a=row['analysis']
    require(row['manual_conclusion'] in MANUAL_STATUSES[batch]['conclusion'],'manual conclusion promoted')
    for key in ['ac_assessment','nac_assessment'] if batch in {1,2} else []:
        require(a.get(key,{}).get('status') in MANUAL_STATUSES[batch][key],'nested manual assessment promoted')
    require(a.get('cq_id')==cq['id'],'nested CQ identity')
    if batch==1:
        require(a.get('requirement_id')==fr['id'] and a.get('origin')==fr['origin'],'nested FR/origin')
        expected_contract={k:cq[k] for k in ['question','required_answer_fields','input_contract','acceptance','adverse_case','source_locator']}
        require(a.get('contract')==expected_contract,'nested CQ contract')
        require(a.get('fr_capability')==fr['capability'] and a.get('fr_locator')==fr['source_locator'],'nested FR contract')
        states={k:fr[k] for k in ['satisfaction_status','acceptance_status','test_execution']}
        states.update(cq_answer_status=cq['answer_status'],cq_test_execution=cq['test_execution'])
        require(a.get('preserved_input_states')==states,'nested input state promotion')
        require(a.get('witness_status')=='not_assessed' and a.get('executable_validation')=='not_executed' and a.get('human_expert_validation')=='not_assessed','nested acceptance promotion')
        for key in ['ac_assessment','nac_assessment']:
            require(isinstance(a.get(key),dict) and a[key].get('status') and a[key].get('reason'),'nested AC/NAC assessment missing')
        require(a.get('full_capability_assessment'),'nested capability missing')
        require(a.get('evidence_ids')==row['model_evidence_ids'],'nested evidence drift')
        require(a.get('finding_id')==row['finding_id'] and a.get('finding')==row['finding'] and a.get('conceptual_review_status')==row['manual_conclusion'],'nested finding drift')
        require(a.get('proposed_stage4_decision',{}).get('status')=='unapproved','nested decision promotion')
        for outer,inner in [('positive_case','positive_scenario'),('adverse_case','adverse_scenario')]:
            value=a.get(inner,{})
            require(value.get('synthetic') is True,'synthetic case scope')
            require(row[outer]==dict(scenario=value.get('description'),expected=value.get('expected'),observed=value.get('observed_manual_interpretation')),'nested case drift')
        fields=dict(a.get('answer_field_assessment',{}))
        if cq['id']=='CQ-09' and 'specific/general endpoints' in fields:
            fields={'Relation description':fields['Relation description'],'specific/general or instance/type endpoints':'Specific/general branch: '+fields['specific/general endpoints']+' Instance/type branch: '+fields['instance/type endpoints']}
        require(fields==row['answer_field_review'],'nested answer-field drift')
    elif batch==2:
        require(a.get('fr_id')==fr['id'] and a.get('frozen_cq_contract')==cq and a.get('frozen_fr_contract')==fr,'nested contract drift')
        require(a.get('model_evidence_ids')==row['model_evidence_ids'] and a.get('answer_field_analysis')==row['answer_field_review'],'nested evidence drift')
        for outer,inner in [('positive_case','positive_case'),('adverse_case','adverse_case_assessment')]:
            require(a.get(inner)==row[outer],'nested case drift')
        for key,field,case in [('ac_assessment','acceptance','positive_case'),('nac_assessment','adverse_case','adverse_case_assessment')]:
            v=a.get(key,{})
            require(v.get('status') and v.get('contract_field')=='frozen_fr_contract.'+field and v.get('expected_observed_evidence')==case,'nested AC/NAC evidence missing')
        require(a.get('capability_assessment'),'nested capability missing')
        require(a.get('failure_analysis')==row['finding'] and a['ac_assessment']['status']==row['manual_conclusion'],'nested finding drift')
        require(a.get('finding',{}).get('status')=='proposal_only_unresolved','nested decision promotion')
    else:
        require(a.get('requirement_id')==fr['id'] and a.get('origin')==fr['origin'],'nested FR/origin')
        for ak,expected in [('question',cq['question']),('required_answer_fields',cq['required_answer_fields']),('capability',fr['capability']),('frozen_AC',fr['acceptance']),('frozen_NAC',fr['adverse_case'])]:
            require(a.get(ak)==expected,'nested contract drift')
        m=a.get('manual_review',{})
        require(row['positive_case']==dict(scenario=m.get('positive_case'),expected=m.get('expected_answer'),observed=m.get('AC_observed')),'nested positive drift')
        require(row['adverse_case']==dict(scenario=m.get('adverse_case'),expected=m.get('NAC_expected'),observed=m.get('NAC_observed')),'nested adverse drift')
        require(m.get('answer_field_assessment')==row['answer_field_review'] and m.get('capability_assessment'),'nested capability/fields missing')
        require(a.get('relation_ids',[])+a.get('constraint_ids',[])==row['model_evidence_ids'],'nested evidence drift')
        f=a.get('finding',{})
        require(f.get('finding')==row['finding'] and f.get('id')==row['finding_id'] and m.get('overall')==row['manual_conclusion'],'nested finding drift')
        require(f.get('state')=='OPEN_REVIEW_FINDING' and f.get('no_model_change') is True,'nested decision promotion')

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
        validate_analysis(row,cq,fr,batch)
    return len(expected)

def main():
    p=argparse.ArgumentParser();p.add_argument('--batch',type=int,choices=[1,2,3],required=True);batch=p.parse_args().batch
    count=validate(read(f'evaluation/cq-review/batch-{batch}.yaml'),batch)
    print(f'PASS: {count} frozen CQ review records, all answer fields/positive/adverse evidence present; no executable semantic PASS or expert acceptance claimed')
if __name__=='__main__':main()
