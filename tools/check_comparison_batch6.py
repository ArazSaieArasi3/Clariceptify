"""Check batch six evidence bindings and explicit limits, not semantic equivalence."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKS = ('IDA', 'BDI2020', 'DOLCEMental')
DIMS = ('agency_activity', 'content_expression_referent',
        'episode_decision_rationale', 'formal_evaluation_limits')


def read(path):
    return yaml.safe_load((ROOT / path).read_text())


def check():
    d = read('evidence/related-work/comparisons/batch-6.yaml')
    assert d['issue'] == 256 and d['scope']['works'] == list(WORKS)
    assert d['scope']['dimensions'] == list(DIMS)
    model_path = ROOT / d['model']['path']
    assert hashlib.sha256(model_path.read_bytes()).hexdigest() == d['model']['sha256']
    ids = {x['id'] for x in read(d['model']['path'])['records']}
    assert d['model']['accepted_equivalences'] == []
    sources = d['source_columns']
    assert set(sources) == set(WORKS)
    ida = read(sources['IDA']['artifact']['review'])
    bdi = read(sources['BDI2020']['artifact']['review'])
    dm = read(sources['DOLCEMental']['artifact']['review'])
    assert ida['issue'] == 246 and ida['acceptance']['issue_closure'] == 'OPEN'
    assert sources['IDA']['paper']['sha256'] is None
    assert bdi['issue'] == 247 and sources['BDI2020']['paper']['sha256'] == bdi['paper']['retained_sha256']
    assert sources['BDI2020']['paper']['paper_expression_records'] == bdi['paper_expression']['expression_records'] == 31
    assert dm['issue'] == 248 and sources['DOLCEMental']['artifact']['sha256'] == dm['source']['sha256']
    assert sources['DOLCEMental']['classes']['native_predicates'] == dm['population']['unique_native_predicates'] == 34
    assert sources['DOLCEMental']['classes']['unary_predicates'] == dm['population']['unary_predicates'] == 16
    assert sources['DOLCEMental']['execution']['active_axioms'] == dm['population']['active_fof_axioms'] == 58
    assert sources['DOLCEMental']['execution']['active_conjectures'] == dm['population']['active_fof_conjectures'] == 12
    for work in ('IDA', 'BDI2020'):
        assert sources[work]['artifact']['original_root'] is None
        assert all(sources[work]['classes'][k] is None for k in
                   ('local_machine', 'imported_machine', 'referenced_machine',
                    'deprecated_machine', 'inferred_machine', 'complete_root_glossary'))
        assert sources[work]['foundation']['exact_edition'] is None
    assert sources['DOLCEMental']['classes']['owl_class_declarations'] == 'NOT_APPLICABLE_NATIVE_FOL'
    assert all(sources[w]['repository'].get('global_absence_claim') is False for w in ('IDA', 'BDI2020'))
    cells = d['matrix']
    assert len(cells) == d['scope']['matrix_cells'] == 12
    assert len({c['id'] for c in cells}) == 12
    assert {(c['work'], c['dimension']) for c in cells} == {(w, k) for w in WORKS for k in DIMS}
    for c in cells:
        assert all(c[k] for k in ('paper_locators', 'artifact_locators', 'native_support',
                                  'required_specialization', 'unsupported_inference',
                                  'counterevidence', 'unknowns', 'model_ids'))
        assert set(c['model_ids']) <= ids
        assert c['work'] in ' '.join(c['paper_locators'])
    assert d['scenario']['common'] and d['scenario']['adverse']
    assert len(d['candidate_mappings']) == 4
    for x in d['candidate_mappings']:
        assert set(x['model_ids']) <= ids
        assert set(x['supporting_cells'] + x['contrary_cells']) <= {c['id'] for c in cells}
        assert x['status'] == 'OWNER_DECISION_REQUIRED' and x['equivalence'] == 'NOT_ESTABLISHED'
    assert {g for x in d['synthesis_export']['discovery_questions'] for g in x['related_gap_ids']} == {'G01', 'G02', 'G03', 'G04', 'G05'}
    assert d['synthesis_export']['target_issue'] == 126
    assert d['limits']['no_corpus_wide_novelty_claim'] and d['limits']['no_formal_equivalence']
    assert all(d['limits'][k] == 'NONE' for k in ('model_change', 'requirements_change',
             'fixtures_change', 'manuscript_change', 'release_change'))
    for path in ('README.md', 'docs/research/corpus-access.md', 'evidence/related-work/deep-reviews/README.md'):
        assert 'batch-6.md' in (ROOT / path).read_text()
    return {'status': 'PASS', 'sources': 3, 'cells': 12, 'candidate_mappings': 4,
            'accepted_equivalences': 0, 'IDA_root': None, 'BDI2020_root': None}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
