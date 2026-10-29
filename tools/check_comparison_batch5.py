#!/usr/bin/env python3
"""Check the fifth comparison's exact sources, twelve cells and synthesis bounds."""

import hashlib
import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = {'agency_activity', 'content_expression_referent',
              'episode_decision_rationale', 'formal_evaluation_limits'}
WORKS = {'COM', 'Representation', 'CMO'}


def read_yaml(root, path):
    return yaml.safe_load((root / path).read_text(encoding='utf-8'))


def digest(root, path):
    return hashlib.sha256((root / path).read_bytes()).hexdigest()


def check(root=ROOT):
    d = read_yaml(root, 'evidence/related-work/comparisons/batch-5.yaml')
    assert (d['batch_id'], d['issue'], d['scope']['synthesis_target']) == ('R2-CMP-005', 255, 126)
    assert d['execution_baseline_commit'] == '0ab502fdece8677ebddfc8f33bcc89b721306e5e'
    assert d['scope']['owner_decision'] == 'OWNER_DECISION_REQUIRED'
    assert d['model']['accepted_equivalences'] == []
    assert digest(root, d['model']['path']) == d['model']['sha256']
    model_ids = {x['id'] for x in read_yaml(root, d['model']['path'])['records']}
    sources = d['source_columns']
    assert set(sources) == WORKS
    evidence_ids = {}
    for name, source in sources.items():
        paper, artifact = source['paper'], source['artifact']
        dossier = read_yaml(root, paper['review'])
        technical = read_yaml(root, artifact['review'])
        assert paper['sha256'] == dossier['source']['sha256']
        assert digest(root, artifact['review']) == artifact['source_sha256']
        assert (root / source['repository']['discovery']).exists()
        assert source['repository']['global_absence_claim'] is False
        assert source['access_license']['raw_redistributed'] is False
        assert source['foundation']['alignment'] == 'NOT_ACCEPTED'
        assert technical['decision']['owner_status'] == 'OWNER_DECISION_REQUIRED'
        evidence_ids[name] = {x['id'] for x in dossier['evidence']}
        if name == 'COM':
            assert artifact['sha256'] is None and technical['source']['formal_root'] is None
            assert source['classes']['paper_figure_labels'] == technical['population']['figure_categories'] == 50
            assert source['classes']['paper_catalog_entries'] == technical['population']['paper_catalog_entries'] == 80
            assert source['execution']['printed_labeled_formulas'] == technical['population']['labeled_paper_formulas'] == 20
            assert source['foundation']['exact_edition'] is None and source['foundation']['formal_import'] is None
        elif name == 'Representation':
            assert artifact['sha256'] is None and artifact['raw_supplement_sha256'] is None
            assert technical['source']['machine_root'] is None
            assert source['classes']['printed_supplement_expressions'] == technical['population']['printed_labeled_supplement_expressions'] == 49
            assert source['classes']['tabulated_predicate_signatures'] == technical['population']['tabulated_predicate_signatures'] == 41
            assert source['foundation']['formal_import'] is None and source['foundation']['exact_edition'] is None
        else:
            census = read_yaml(root, artifact['class_catalog'])
            assert artifact['sha256'] == technical['source']['mirror_sha256'] == census['source_sha256']
            assert source['repository']['commit'] == technical['source']['mirror_commit']
            assert source['repository']['paper_mirror_correspondence'] == 'NOT_ESTABLISHED'
            assert source['repository']['path_date_is_release_date'] is False
            assert source['classes']['local_mirror'] == census['counts']['local_classes'] == 7
            assert source['classes']['external_redeclarations'] == census['counts']['external_redeclarations'] == 5
            assert source['classes']['referenced_named'] == census['counts']['referenced_named_classes'] == 8
            assert (source['classes']['referenced_local'], source['classes']['referenced_external']) == (4, 4)
            assert source['classes']['local_comment_candidates'] == census['counts']['local_source_comment_candidates'] == 6
            assert source['classes']['local_descriptive_seeAlso_without_comment'] == census['counts']['local_descriptive_seeAlso_without_comment'] == 1
            assert source['classes']['deprecated_local'] == census['counts']['local_explicit_deprecated'] == 0
            assert source['foundation']['mirror_formal_imports'] == census['direct_imports']
            assert source['foundation']['paper_edition'] is None
            assert source['foundation']['bfo_formal_import'] is False
            assert source['classes']['selected_mirror_glossary_complete'] is True
            assert source['classes']['imported_glossary_complete'] is False
        for key in ('local_machine', 'imported_machine', 'referenced_machine', 'deprecated_machine',
                    'inferred_machine', 'machine_definition_candidates', 'machine_missing_definitions',
                    'selected_machine_glossary_complete') if name != 'CMO' else (
                    'imported_closure', 'inferred', 'original_author_machine_classes'):
            assert source['classes'][key] is None, (name, key)

    cells = d['matrix']
    assert len(cells) == d['scope']['matrix_cells'] == 12
    assert len({x['id'] for x in cells}) == 12
    assert {(x['work'], x['dimension']) for x in cells} == {(w, dim) for w in WORKS for dim in DIMENSIONS}
    for cell in cells:
        assert set(cell['model_ids']) <= model_ids, cell['id']
        assert all(cell[k] for k in ('paper_locators', 'artifact_locators', 'native_support',
                                     'required_specialization', 'unsupported_inference',
                                     'counterevidence', 'unknowns', 'model_ids')), cell['id']
        combined = ' '.join(cell['paper_locators'])
        prefixes = {'COM': 'COM2004:', 'Representation': 'CLR-RW-Representation:', 'CMO': 'CMO:'}
        assert prefixes[cell['work']] in combined, cell['id']
        named = re.findall(r'(?:COM2004|CLR-RW-Representation|CMO):(E\d{2})', combined)
        assert named and set(named) <= evidence_ids[cell['work']], cell['id']
    assert all(d['scenario'][key] for key in ('common', 'adverse'))
    assert d['scenario']['status'] == 'CONCEPTUAL_REVIEW_ONLY'
    assert len(d['candidate_mappings']) == 4
    for x in d['candidate_mappings']:
        assert x['model_ids'] and set(x['model_ids']) <= model_ids
        assert set(x['supporting_cells'] + x['contrary_cells']) <= {c['id'] for c in cells}
        assert x['status'] == 'OWNER_DECISION_REQUIRED' and x['equivalence'] == 'NOT_ESTABLISHED'
    assert {x['id'] for x in d['synthesis_export']['discovery_questions']} == {
        'CMP5-Q01', 'CMP5-Q02', 'CMP5-Q03', 'CMP5-Q04'}
    assert {g for x in d['synthesis_export']['discovery_questions']
            for g in x['related_gap_ids']} == {'G01', 'G02', 'G03', 'G04', 'G05'}
    assert d['synthesis_export']['target_issue'] == 126
    assert d['limits']['no_corpus_wide_novelty_claim'] is True
    assert d['limits']['no_formal_equivalence'] is True
    assert d['limits']['raw_external_sources_redistributed'] is False
    assert all(d['limits'][x] == 'NONE' for x in ('model_change', 'requirements_change',
                                                'fixtures_change', 'manuscript_change', 'release_change'))
    for p in ('docs/research/corpus-access.md', 'evidence/related-work/deep-reviews/README.md'):
        assert 'batch-5.md' in (root / p).read_text(encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'sources': 3, 'cells': 12,
                      'candidate_mappings': 4, 'accepted_equivalences': 0}, sort_keys=True))


if __name__ == '__main__':
    check()
