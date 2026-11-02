"""Adverse report-integrity tests; not philosophical or native OntoUML proofs."""
from copy import deepcopy
from check_semantic_reviews import read, validate, SemanticReviewError, finite_checks
base=read('evaluation/semantic-reviews/mental-content.yaml')
validate(base,114)
def fails(name,mutate):
    x=deepcopy(base);mutate(x)
    try:validate(x,114)
    except SemanticReviewError:print('EXPECTED_REJECTION:',name)
    else:raise RuntimeError('mutation escaped: '+name)
fails('semantic promotion',lambda x:x.update(semantic_acceptance='accepted'))
fails('invented expert approval',lambda x:x.update(expert_review='approved'))
fails('stale input',lambda x:x['input_bindings'].update({'model/concepts.yaml':'0'*64}))
fails('lost source binding',lambda x:x.update(source_refs=[]))
fails('source record drift',lambda x:x['source_refs'][0].update(sha256='0'*64))
fails('model snapshot drift',lambda x:x['model_snapshot']['model/concepts.yaml'][0].update(definition='altered'))
fails('cited snapshot deleted',lambda x:x['model_snapshot'].update({'model/concepts.yaml':[r for r in x['model_snapshot']['model/concepts.yaml'] if r['id']!='CLR-C0017']}))
fails('snapshot family deleted',lambda x:x['model_snapshot'].pop('model/constraints.yaml'))
fails('findings silently accepted',lambda x:x['findings'][0].update(decision_gate='accepted'))
fails('unknown affected entity',lambda x:x['findings'][0].update(model_ids=['CLR-C9999']))
fails('unknown source',lambda x:x['findings'][0].update(source_ids=['unknown']))
fails('missing cases',lambda x:x.update(case_review={}))
if finite_checks(114)!=4:raise RuntimeError('fixture denominator changed')
print('PASS: 12 adverse integrity cases and 4 bounded mental-content predicates')
