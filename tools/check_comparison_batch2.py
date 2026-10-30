"""Validate the bounded LMM/O4OA/OntoKADS comparison and source limits."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKS = ('LMM', 'O4OA', 'OntoKADS')
DIMS = ('agency_activity', 'content_expression_referent',
        'episode_decision_rationale', 'formal_evaluation_limits')


def read(path):
    return yaml.safe_load((ROOT / path).read_text())


def check():
    d = read('evidence/related-work/comparisons/batch-2.yaml')
    assert d['issue'] == 252 and d['scope']['works'] == list(WORKS)
    assert d['scope']['dimensions'] == list(DIMS)
    assert hashlib.sha256((ROOT / d['model']['path']).read_bytes()).hexdigest() == d['model']['sha256']
    model_ids = {x['id'] for x in read(d['model']['path'])['records']}
    assert d['model']['accepted_equivalences'] == []
    s = d['source_columns']
    assert set(s) == set(WORKS)
    lmm = read(s['LMM']['artifact']['review'])
    o4oa = read(s['O4OA']['artifact']['review'])
    ok = read(s['OntoKADS']['artifact']['review'])
    assert lmm['issue'] == 274 and s['LMM']['paper']['sha256'] == lmm['source']['paper']['sha256']
    assert s['LMM']['classes']['selected_local_total'] == lmm['source']['local_classes']['selected_pair_total'] == 29
    assert s['LMM']['classes']['asserted_closure_unique'] == lmm['source']['local_classes']['asserted_closure_unique'] == 154
    assert s['LMM']['execution']['isolated_cases_passed'] == lmm['execution']['isolated_positive_adverse_cases']['passed'] == 13
    assert o4oa['issue'] == 91 and o4oa['issue_completion'] is False
    assert s['O4OA']['artifact']['sha256'] == o4oa['identity']['source_sha256']
    assert s['O4OA']['classes']['specification_table5_rows'] == o4oa['populations']['document_table5_entries'] == 138
    assert s['O4OA']['execution']['document_cqs'] == o4oa['populations']['document_cqs'] == 24
    assert ok['issue'] == 236 and s['OntoKADS']['paper']['sha256'] == ok['source']['paper_sha256']
    assert s['OntoKADS']['classes']['paper_catalog'] == ok['population']['paper_catalog_records'] == 72
    assert s['OntoKADS']['classes']['selected_commitments'] == ok['population']['selected_paper_commitments'] == 8
    for w in ('O4OA', 'OntoKADS'):
        assert s[w]['foundation']['exact_edition'] is None and s[w]['foundation']['actual_import'] is None
        assert s[w]['classes']['local_machine'] is None and s[w]['classes']['imported_machine'] is None
        assert s[w]['classes']['inferred_machine'] is None and s[w]['classes']['complete_root_glossary'] is None
    assert s['O4OA']['artifact']['reference_root'] is None and s['OntoKADS']['artifact']['original_root'] is None
    assert all(s[w]['repository']['global_absence_claim'] is False for w in WORKS)
    cells = d['matrix']
    assert len(cells) == d['scope']['matrix_cells'] == 12
    assert len({x['id'] for x in cells}) == 12
    assert {(x['work'], x['dimension']) for x in cells} == {(w, dim) for w in WORKS for dim in DIMS}
    for x in cells:
        assert set(x['model_ids']) <= model_ids
        assert all(x[k] for k in ('paper_locators', 'artifact_locators', 'native_support',
                                  'required_specialization', 'unsupported_inference',
                                  'counterevidence', 'unknowns', 'model_ids'))
        assert x['work'] in ' '.join(x['paper_locators'])
    assert d['scenario']['common'] and d['scenario']['adverse']
    assert len(d['candidate_mappings']) == 4
    for x in d['candidate_mappings']:
        assert set(x['model_ids']) <= model_ids
        assert set(x['supporting_cells'] + x['contrary_cells']) <= {c['id'] for c in cells}
        assert x['status'] == 'OWNER_DECISION_REQUIRED' and x['equivalence'] == 'NOT_ESTABLISHED'
    assert {g for x in d['synthesis_export']['discovery_questions'] for g in x['related_gap_ids']} == {'G01', 'G02', 'G03', 'G04', 'G05'}
    assert d['synthesis_export']['target_issue'] == 126
    assert d['limits']['no_formal_equivalence'] and d['limits']['no_corpus_wide_novelty_claim']
    assert all(d['limits'][k] == 'NONE' for k in ('model_change', 'requirements_change',
             'fixtures_change', 'manuscript_change', 'release_change'))
    for p in ('README.md', 'docs/research/corpus-access.md', 'evidence/related-work/deep-reviews/README.md'):
        assert 'batch-2.md' in (ROOT / p).read_text()
    return {'status': 'PASS', 'sources': 3, 'cells': 12, 'candidate_mappings': 4,
            'O4OA_formal_root': None, 'OntoKADS_formal_root': None, 'accepted_equivalences': 0}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
