"""Adverse integrity cases; works under python -O as well."""
from copy import deepcopy
from check_pending_passports import read, validate, PassportError

base = read('evidence/passports/pending-batch-1.yaml')
validate(base, 1)

def fails(name, change):
    item = deepcopy(base); change(item)
    try:
        validate(item, 1)
    except PassportError:
        print('EXPECTED_REJECTION:', name)
    else:
        raise RuntimeError(f'mutation escaped: {name}')

fails('missing concept', lambda x: x['concepts'].pop())
fails('definition changed', lambda x: x['concepts'][0].update(frozen_definition='new'))
fails('typing approval invented', lambda x: x['concepts'][0].update(typing_approval='approved'))
fails('source promotion', lambda x: x['concepts'][0].update(preserve_imported_support='D'))
fails('lost original provenance', lambda x: x['concepts'][0]['original_support_record'].update(passage_verification='verified'))
fails('unapproved decision applied', lambda x: x['concepts'][0]['proposed_delta'].update(status='accepted'))
fails('unknown evidence', lambda x: x['concepts'][0]['clause_support'][0].update(evidence=['missing']))
fails('source locator absent', lambda x: x['sources'][0].update(locator=''))
fails('stale input', lambda x: x['input_bindings'].update({'model/concepts.yaml':'0'*64}))
fails('original source audit removed', lambda x: x['sources'].pop(0))
fails('misleading result', lambda x: x.update(status='SEMANTIC_PASS'))
print('PASS: 11 adverse passport-integrity cases; not source-semantic tests')
