"""Failure boundaries for review coverage/integrity, not CQ semantic execution."""
from copy import deepcopy
from check_cq_reviews import read,validate,CQReviewError
base=read('evaluation/cq-review/batch-1.yaml');validate(base,1)
def fails(name,mutate):
    x=deepcopy(base);mutate(x)
    try:validate(x,1)
    except CQReviewError:print('EXPECTED_REJECTION:',name)
    else:raise RuntimeError('mutation escaped: '+name)
fails('denominator changed',lambda x:x['records'].pop())
fails('frozen AC changed',lambda x:x['records'][0]['frozen_fr_contract'].update(acceptance='new requirement'))
fails('answer field omitted',lambda x:x['records'][0]['answer_field_review'].pop(next(iter(x['records'][0]['answer_field_review']))))
fails('expected answer absent',lambda x:x['records'][0]['positive_case'].update(expected=''))
fails('adverse observation absent',lambda x:x['records'][0]['adverse_case'].update(observed=''))
fails('origin upgraded',lambda x:x['records'][0].update(origin='E'))
fails('unknown evidence',lambda x:x['records'][0].update(model_evidence_ids=['CLR-C9999']))
fails('decision applied',lambda x:x['records'][0].update(decision_gate='accepted'))
fails('manual review called execution',lambda x:x['records'][0].update(executable_semantics='PASS'))
fails('human approval invented',lambda x:x['records'][0].update(human_expert_validation='approved'))
fails('stale input',lambda x:x['input_bindings'].update({'model/concepts.yaml':'0'*64}))
print('PASS: 11 adverse review-integrity cases; not negative ontology-instance tests')

fails("nested AC removed",lambda x:x["records"][0]["analysis"].pop("ac_assessment"))
fails("nested execution promoted",lambda x:x["records"][0]["analysis"]["preserved_input_states"].update(test_execution="PASS"))
fails("nested origin promoted",lambda x:x["records"][0]["analysis"].update(origin="E"))
fails("nested evidence drift",lambda x:x["records"][0]["analysis"].update(evidence_ids=[]))
fails("nested expected drift",lambda x:x["records"][0]["analysis"]["positive_scenario"].update(expected="changed"))
fails("nested capability removed",lambda x:x["records"][0]["analysis"].pop("full_capability_assessment"))
print("PASS: 6 nested-evidence retention and consistency mutations")
