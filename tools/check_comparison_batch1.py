#!/usr/bin/env python3
"""Check the bounded comparison contract against pinned source and model records."""
import hashlib
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'evidence/related-work/comparisons/batch-1.yaml'
DIMENSIONS = {'agency_activity', 'content_expression_referent', 'episode_decision_rationale', 'formal_evaluation_limits'}
WORKS = {'DnS', 'cDnS', 'DUL', 'DULConceptualization'}


def check(root=ROOT):
    data = yaml.safe_load((root / PATH.relative_to(ROOT)).read_text())
    assert data['batch_id'] == 'R2-CMP-001' and data['issue'] == 251
    assert data['scope']['synthesis_target'] == 126
    assert data['scope']['owner_decision'] == 'OWNER_DECISION_REQUIRED'
    assert data['model']['accepted_equivalences'] == []
    baseline = root / data['model']['path']
    assert hashlib.sha256(baseline.read_bytes()).hexdigest() == data['model']['sha256']
    model_ids = {row['id'] for row in yaml.safe_load(baseline.read_text())['records']}
    paper_ids = {}
    for work, entry in data['source_columns'].items():
        assert work in WORKS
        doc = entry.get('paper') or entry.get('documentation')
        dossier = yaml.safe_load((root / doc['dossier' if 'dossier' in doc else 'review']).read_text())
        source = dossier['source'] if 'source' in dossier else dossier['access']
        assert doc['sha256'] == source['sha256']
        if 'evidence' in dossier:
            paper_ids[doc['id']] = {item['id'] for item in dossier['evidence']}
        if 'additional_paper' in entry:
            other = entry['additional_paper']
            review = yaml.safe_load((root / other['dossier']).read_text())
            assert review['source']['sha256'] == other['sha256']
            paper_ids[other['id']] = {item['id'] for item in review['evidence']}
        assert (root / entry['artifact']['review']).exists()
        artifact = yaml.safe_load((root / entry['artifact']['review']).read_text())
        recorded_sha = (artifact.get('identity') or artifact.get('source') or artifact.get('source_root') or {}).get('sha256', artifact.get('artifact_sha256'))
        assert recorded_sha == entry['artifact']['sha256']
        assert entry['repository']['discovery'] and entry['access_license']['license']
        assert entry['classes']['catalog'] and (root / entry['classes']['catalog']).exists()
        assert entry['foundation']['relation'] and entry['foundation']['alignment'] == 'NOT_ACCEPTED'
        assert entry['artifact']['sha256'] and entry['repository'].get('exact_2003_correspondence', entry['repository'].get('exact_2007_or_2008_correspondence', entry['repository'].get('exact_2016_correspondence', entry['repository'].get('original_import_edition')))) == 'NOT_ESTABLISHED'
        catalog = yaml.safe_load((root / entry['classes']['catalog']).read_text())
        expected_local = entry['classes'].get('local', entry['classes'].get('selected_map_unique'))
        assert catalog['counts']['local_classes'] == expected_local
    ids = set()
    assert len(data['matrix']) == 16
    for cell in data['matrix']:
        assert cell['id'] not in ids
        ids.add(cell['id'])
        assert cell['work'] in WORKS and cell['dimension'] in DIMENSIONS
        assert all(cell[k] for k in ('paper_locators', 'artifact_locators', 'native_support', 'required_specialization', 'unsupported_inference', 'counterevidence', 'unknowns', 'use_ids'))
        assert set(cell['model_ids']) <= model_ids
        for locator in cell['paper_locators']:
            if locator.startswith('RW-DUL-CONCEPTUALIZATION-0.1'):
                assert 'observations/' in locator
            else:
                source_id, rest = locator.split(':', 1)
                assert rest.split()[0] in paper_ids[source_id], locator
        assert all(item.split()[0].startswith(('evidence/', 'evaluation/')) and (root / item.split()[0]).exists() for item in cell['artifact_locators'])
    assert {(x['dimension'], x['work']) for x in data['matrix']} == {(d, w) for d in DIMENSIONS for w in WORKS}
    scenario = data['common_scenario']
    assert scenario['positive'] and scenario['adverse']
    assert scenario['assessment_basis'] == 'REVIEWER_THOUGHT_EXPERIMENT_NOT_NEW_EXECUTED_REASONER_FIXTURE'
    assert set(scenario['model_ids']) <= model_ids
    assert {k for k in scenario['cross_source_disposition']} == WORKS
    for item in data['candidate_mappings']:
        assert set(item['model_ids']) <= model_ids
        assert set(item['supporting_cells'] + item['contrary_cells']) <= ids
        assert item['status'] == 'OWNER_DECISION_REQUIRED' and item['equivalence'] == 'NOT_ESTABLISHED'
    assert data['limits']
    print('R2-CMP-001: 16 versioned cells, four sources, one positive/adverse scenario and model-ID bindings PASS')


if __name__ == '__main__':
    check()
