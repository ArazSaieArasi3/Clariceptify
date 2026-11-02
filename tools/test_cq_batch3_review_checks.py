"""Batch-three review-evidence guards, not executed ontology instances."""
from copy import deepcopy
from check_cq_reviews import read, validate, CQReviewError
base=read('evaluation/cq-review/batch-3.yaml');validate(base,3)
def fails(name, mutate):
    x=deepcopy(base);mutate(x)
    try:validate(x,3)
    except CQReviewError:print('EXPECTED_REJECTION:',name)
    else:raise RuntimeError('mutation escaped: '+name)
fails('nested original AC changed',lambda x:x['records'][0]['analysis'].update(frozen_AC='changed'))
fails('nested contract hash changed',lambda x:x['records'][0]['analysis']['contract_integrity'].update(cq_contract_sha256='0'*64))
fails('nested locator changed',lambda x:x['records'][0]['analysis']['contract_integrity'].update(fr_source_locator='unknown'))
fails('nested origin promoted',lambda x:x['records'][0]['analysis'].update(origin='E'))
fails('nested evidence removed',lambda x:x['records'][0]['analysis'].update(relation_ids=[]))
fails('nested capability removed',lambda x:x['records'][0]['analysis']['manual_review'].pop('capability_assessment'))
fails('nested adverse changed',lambda x:x['records'][0]['analysis']['manual_review'].update(NAC_observed='changed'))
fails('nested decision promoted',lambda x:x['records'][0]['analysis']['finding'].update(state='ACCEPTED'))
fails('execution promoted',lambda x:x['records'][0].update(executable_semantics='passed'))
def coordinated_promotion(x):
    x['records'][0]['analysis']['manual_review']['overall']='formal_solver_PASS'
    x['records'][0]['manual_conclusion']='formal_solver_PASS'
fails('coordinated manual status promoted',coordinated_promotion)
print('PASS: 10 batch-three evidence mutations; no semantic-instance proof')
