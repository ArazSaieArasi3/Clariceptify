#!/usr/bin/env python3
"""Check the pinned fourth comparison's 12 source and model bindings."""

import hashlib
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = {
    'agency_activity', 'content_expression_referent',
    'episode_decision_rationale', 'formal_evaluation_limits',
}
WORKS = {'IAO', 'CognitiveAtlas', 'EFO'}


def read_yaml(root, path):
    return yaml.safe_load((root / path).read_text(encoding='utf-8'))


def check(root=ROOT):
    d = read_yaml(root, 'evidence/related-work/comparisons/batch-4.yaml')
    assert (d['batch_id'], d['issue'], d['scope']['synthesis_target']) == ('R2-CMP-004', 254, 126)
    assert d['model']['accepted_equivalences'] == []
    assert d['scope']['owner_decision'] == 'OWNER_DECISION_REQUIRED'
    model = root / d['model']['path']
    assert hashlib.sha256(model.read_bytes()).hexdigest() == d['model']['sha256']
    ids = {x['id'] for x in yaml.safe_load(model.read_text(encoding='utf-8'))['records']}

    sources = d['source_columns']
    assert set(sources) == WORKS
    for name, source in sources.items():
        paper = source['paper']
        review = read_yaml(root, paper['review'])
        assert review['source']['sha256'] == paper['sha256'], name
        assert (root / source['repository']['discovery'].split('#')[0]).exists(), name
        assert source['access_license']['raw_redistributed'] is False
        assert source['foundation']['alignment'] == 'NOT_ACCEPTED'

        artifact = source['artifact']
        technical = read_yaml(root, artifact['review'])
        if name == 'IAO':
            assert technical['identity']['selected_sha256'] == artifact['sha256']
            catalog = json.loads((root / artifact['class_catalog']).read_text(encoding='utf-8'))
            population = catalog['population']
            assert population['local_iao_named_classes'] == source['classes']['local'] == 210
            assert population['external_redeclared_named_classes'] == source['classes']['external_redeclarations'] == 56
            assert population['local_definition_states'] == {'MISSING': 13, 'PRESENT': 197}
            assert population['local_deprecated'] == source['classes']['deprecated_local'] == 16
            assert population['imported_classes'] == source['classes']['imported'] == 0
            assert source['foundation']['exact_bfo_edition'] is None
        elif name == 'CognitiveAtlas':
            assert technical['source_root']['sha256'] == artifact['sha256']
            catalog = read_yaml(root, artifact['class_catalog'])
            counts = catalog['counts']
            assert counts['local_classes'] == source['classes']['local'] == 1696
            assert counts['external_class_declarations'] == source['classes']['external_redeclarations'] == 2
            assert (counts['source_definition_candidates'], counts['empty_definition_annotations'],
                    counts['absent_definition_annotations'], counts['missing_source_definitions']) == (1232, 55, 409, 464)
            assert counts['ambiguous_multi_identifier_classes'] == source['classes']['multi_identifier_class_iris'] == 101
            assert source['execution']['owl2_dl_profile'].startswith('FAIL_')
            assert source['repository']['paper_export_correspondence'] == 'NOT_ESTABLISHED'
        else:
            assert artifact['sha256'] is None
            assert technical['identity']['pdf_sha256'] == paper['sha256']
            catalog = json.loads((root / artifact['paper_catalog']).read_text(encoding='utf-8'))
            assert catalog['population']['figure_category_labels'] == source['classes']['paper_figure_labels'] == 33
            assert len(catalog['figure_categories']) == 33
            assert catalog['population']['executable_root'] is None
            for field in ('local_owl', 'imported_owl', 'referenced_owl', 'deprecated_owl', 'inferred_owl'):
                assert source['classes'][field] is None
            assert source['repository']['commit'] is None
            assert source['foundation']['formal_imports'] is None
        assert source['classes'].get('glossary_complete_for_selected_root', True) is True

    cells = d['matrix']
    assert len(cells) == d['scope']['matrix_cells'] == 12
    assert len({x['id'] for x in cells}) == len(cells)
    assert {(x['work'], x['dimension']) for x in cells} == {(w, dim) for w in WORKS for dim in DIMENSIONS}
    for cell in cells:
        assert set(cell['model_ids']) <= ids, cell['id']
        assert all(cell[k] for k in ('paper_locators', 'artifact_locators', 'native_support',
                                     'required_specialization', 'unsupported_inference',
                                     'counterevidence', 'unknowns')), cell['id']
    assert all(d['scenario'][key] for key in ('common', 'adverse'))
    assert d['scenario']['status'] == 'CONCEPTUAL_REVIEW_ONLY'

    assert len(d['candidate_mappings']) == 4
    for candidate in d['candidate_mappings']:
        assert set(candidate['model_ids']) <= ids
        assert set(candidate['supporting_cells'] + candidate['contrary_cells']) <= {x['id'] for x in cells}
        assert candidate['question']
        assert candidate['status'] == 'OWNER_DECISION_REQUIRED'
        assert candidate['equivalence'] == 'NOT_ESTABLISHED'
    assert d['synthesis_export']['target_issue'] == 126
    assert d['limits']['no_corpus_wide_novelty_claim'] is True
    assert d['limits']['no_formal_equivalence'] is True
    assert d['limits']['raw_external_sources_redistributed'] is False
    assert all(d['limits'][key] == 'NONE' for key in ('model_change', 'requirements_change',
                                                      'fixtures_change', 'manuscript_change', 'release_change'))
    print('R2-CMP-004: three pinned works, twelve cells, model IDs, scenario and limits PASS')


if __name__ == '__main__':
    check()
