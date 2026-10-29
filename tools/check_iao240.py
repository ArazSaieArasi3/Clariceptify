"""Check IAO selected-root census, source identity and review boundaries."""
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PIN = 'c27ff2964a2ad8165bc365698b628aae95108411384aa4450e6e1b1e82bf0f41'


def check(root=ROOT):
    d = yaml.safe_load((root / 'evidence/related-work/artifacts/IAO.yaml').read_text())
    r = json.loads((root / d['population']['census']).read_text())
    assert d['issue'] == r['issue'] == 240
    assert d['identity']['selected_sha256'] == r['source']['sha256'] == PIN
    assert d['identity']['retained_commit'] == r['source']['commit']
    assert d['identity']['version_iri'] == r['source']['version_iri']
    assert r['imports'] == d['imports']['direct_declared_in_selected_root'] == []
    rows = r['classes']
    assert len(rows) == len({x['iri'] for x in rows}) == 266
    local = [x for x in rows if x['population'] == 'LOCAL_IAO_IRI']
    external = [x for x in rows if x['population'] == 'EXTERNAL_REDECLARED_IN_ROOT']
    assert len(local) == d['population']['local_iao_named_classes'] == 210
    assert len(external) == d['population']['external_redeclared_named_classes'] == 56
    assert all(x['iri'].startswith('http://purl.obolibrary.org/obo/IAO_') for x in local)
    assert all(x['label'] and x['definition_state'] in {'PRESENT', 'MISSING', 'COMMENT_ONLY'} for x in rows if x in local)
    assert sum(x['definition_state'] == 'PRESENT' for x in local) == d['population']['local_definitions_present'] == 197
    assert sum(x['definition_state'] == 'MISSING' for x in local) == d['population']['local_definitions_missing'] == 13
    assert sum(x['deprecated'] for x in local) == d['population']['local_deprecated_classes'] == 16
    assert sum(x['definition_state'] == 'PRESENT' for x in external) == d['population']['external_definitions_present'] == 32
    assert all(x['definition_locator'] and x['source_definition'] if x['definition_state'] == 'PRESENT'
               else not x['source_definition'] for x in rows)
    assert not any('unparsed_anonymous_expression' in str(x) for x in rows)
    assert len(r['selected_commitments']) == d['selected_commitments']['count'] == 8
    assert {x['id'] for x in r['selected_commitments']} == set(d['selected_commitments']['selected_glosses'])
    assert all(x['asserted'] for x in r['selected_commitments'])
    assert d['foundation']['exact_bfo_edition_for_embedded_axioms'] == 'UNKNOWN_FROM_SELECTED_ROOT'
    assert d['decision']['accepted_equivalences'] == []
    assert all(d['boundary'][k] == 'NONE' for k in d['boundary'])
    assert d['execution']['owl2_dl_profile'] == d['execution']['reasoner_consistency'] == 'NOT_EXECUTED'
    assert (root / 'docs/research/corpus-access.md').read_text().find('(../../evidence/related-work/artifacts/IAO.md)') >= 0
    return {'status': 'PASS', 'named_classes': 266, 'selected_assertions': 8}


if __name__ == '__main__':
    print(check())
