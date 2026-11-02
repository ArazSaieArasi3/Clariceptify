"""Batch-two evidence integrity mutations, not CQ execution."""
from copy import deepcopy
from check_cq_reviews import read, validate, CQReviewError
base=read('evaluation/cq-review/batch-2.yaml');validate(base,2)
def fails(name, mutate):
    x=deepcopy(base);mutate(x)
    try:validate(x,2)
    except CQReviewError:print('EXPECTED_REJECTION:',name)
    else:raise RuntimeError('mutation escaped: '+name)
fails('nested AC removed',lambda x:x['records'][0]['analysis'].pop('ac_assessment'))
fails('nested contract changed',lambda x:x['records'][0]['analysis']['frozen_cq_contract'].update(test_execution='PASS'))
fails('nested origin changed',lambda x:x['records'][0]['analysis']['frozen_fr_contract'].update(origin='E'))
fails('nested evidence removed',lambda x:x['records'][0]['analysis'].update(model_evidence_ids=[]))
fails('nested fields removed',lambda x:x['records'][0]['analysis'].update(answer_field_analysis={}))
fails('nested capability removed',lambda x:x['records'][0]['analysis'].pop('capability_assessment'))
fails('decision promoted',lambda x:x['records'][0]['analysis']['finding'].update(status='accepted'))
fails('outer execution promoted',lambda x:x['records'][0].update(executable_semantics='passed'))
print('PASS: 8 batch-two evidence mutations; not semantic instance tests')

fails("nested NAC promotion",lambda x:x["records"][0]["analysis"]["nac_assessment"].update(status="formal_solver_PASS"))
def coordinated_promotion(x):
    x["records"][0]["analysis"]["ac_assessment"]["status"]="formal_solver_PASS"
    x["records"][0]["manual_conclusion"]="formal_solver_PASS"
fails("coordinated manual-to-formal promotion",coordinated_promotion)
print("PASS: 2 manual-status promotion mutations")
