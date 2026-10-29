"""Check the pinned native symbol inventory and isolated logical examples."""
from pathlib import Path
import argparse
import hashlib
import json
import yaml
from inspect_dolcemental248 import inspect, render_catalog, SOURCE_SHA256

ROOT = Path(__file__).resolve().parents[1]


def _truth(source, y, w, biconditional):
    target = bool(w)
    return any((bool(e in y) == target) if biconditional else ((e not in y) or target)
               for e in source)


def check(root=ROOT, source=None):
    a = yaml.safe_load((root / 'evidence/related-work/artifacts/DOLCEMental.yaml').read_text())
    for item in a['evidence'].values():
        assert hashlib.sha256((root / item['path']).read_bytes()).hexdigest() == item['sha256']
    c = json.loads((root / 'evaluation/related-work/dolce-mental/technical-census.json').read_text())
    s = json.loads((root / 'evaluation/related-work/dolce-mental/semantic-cases.json').read_text())
    assert a['issue'] == c['issue'] == s['issue'] == 248
    assert a['source']['sha256'] == c['source_sha256'] == s['source_sha256'] == SOURCE_SHA256
    assert c['formula_counts'] == {'axiom': 58, 'conjecture': 12}
    assert (c['active_predicates'], c['unary_predicates'], c['binary_predicates'],
            c['ternary_predicates']) == (34, 16, 4, 14)
    assert c['inlined_foundation_predicates'] == 14 and c['local_native_predicates'] == 20
    assert c['direct_include_statements'] == 0
    assert c['duplicate_formula_names'] == {
        'ax_bel_int_disj': [169, 171, 173, 175, 177], 'ax_present_at': [60, 61],
        'ax_top_level': [28, 40, 41], 'th_unicity_of_agent_ms': [315, 328]}
    rows = c['predicates']; assert len(rows) == len({x['symbol'] for x in rows}) == 34
    assert len([x for x in rows if x['symbol'].endswith('/1') and x['origin'] == 'LOCAL_NATIVE_SYMBOL']) == 5
    assert [x['symbol'] for x in rows if x['definition_state'].startswith('REFERENCED_ONLY')] == ['intState/1']
    assert all(x['source_iri'] is None and x['active_axiom_lines'] and x['reviewer_paraphrase']
               and x['comment_or_header_line'] and x['annotation_availability'] for x in rows)
    assert all(set(x['biconditional_formula_lines']) <= set(x['active_axiom_lines']) for x in rows)
    for row in s['cases'][:2]:
        domain = s['individual_domain']; y = set(row['satisfiers_of_Y']); w = set(row['satisfiers_of_W'])
        is_bi = row['id'] == 'S02'
        source_result = _truth(domain, y, w, is_bi)
        paper_result = (bool(y) == bool(w)) if is_bi else (not y or bool(w))
        assert source_result == row['source_fragment_result'] is True
        assert paper_result == row['paper_fragment_result'] is False
    row = s['cases'][2]
    assert row['id'] == 'S03' and not any(
        ('c11' in selected) and not selected for selected in
        (set(), {'c11'}, {'c12'}, {'c11', 'c12'}))
    assert row['antecedent_satisfiable_for_any_desire_set'] is False
    assert s['tptp_parser'] == s['darwin_hets'] == 'NOT_EXECUTED'
    assert a['population']['selected_unary_predicates'] == 16
    assert a['population']['inferred_predicates'] is None
    assert a['decision']['accepted_equivalences'] == [] and a['boundary']['model_change'] == 'NONE'
    markdown = (root / 'evidence/related-work/artifacts/DOLCEMental-symbol-catalog.md').read_text()
    assert markdown == render_catalog(c)
    assert '[DOLCE Mental technical #248]' in (root / 'docs/research/corpus-access.md').read_text()
    if source:
        assert hashlib.sha256(source.read_bytes()).hexdigest() == SOURCE_SHA256
        assert inspect(source) == c
    return {'status': 'PASS', 'native_predicates': 34, 'unary_class_analogues': 16,
            'axioms': 58, 'conjectures': 12, 'isolated_cases': 3,
            'raw_reconciliation': 'PASS' if source else 'OPTIONAL_PRIVATE_SOURCE_NOT_RUN',
            'proof_status': 'NOT_EXECUTED'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path)
    args = parser.parse_args()
    print(json.dumps(check(source=args.source), indent=2))
