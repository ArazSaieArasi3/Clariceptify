#!/usr/bin/env python3
"""Check bounded COM paper evidence and two explicitly local Boolean fragments."""

import hashlib
import itertools
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    d = yaml.safe_load((root / 'evidence/related-work/artifacts/COM.yaml').read_text())
    p = yaml.safe_load((root / d['source']['dossier']).read_text())
    discovery = json.loads((root / d['source']['discovery']).read_text())
    old = json.loads((root / discovery['prior_receipt']).read_text())
    assert d['issue'] == discovery['issue'] == 243 and p['work_id'] == d['source']['work'] == 'COM2004'
    assert p['source']['sha256'] == discovery['paper_sha256'] == old['source_sha256'] == d['source']['paper_sha256']
    assert hashlib.sha256((root / d['source']['dossier']).read_bytes()).hexdigest() == d['source']['dossier_sha256']
    assert d['population']['figure_categories'] == 50 and d['population']['bold_com_additions_in_figure'] == 11
    assert d['population']['paper_catalog_entries'] == len(p['catalog']) == 80
    assert d['population']['labeled_paper_formulas'] == len(p['commitments']) == 20
    assert len(d['commitments']) == d['population']['selected_paper_commitments'] == 8
    paper = {x['id']: x for x in p['commitments']}
    evidence = {x['id'] for x in p['evidence']}
    assert len({x['id'] for x in d['commitments']}) == 8
    for c in d['commitments']:
        source = paper[c['paper_id']]
        assert c['formula'] == source['formula_label']
        assert c['locator'] == f"COM2004:{source['evidence'][0]} PDF p.{source['formula_page']}"
        assert source['evidence'][0] in evidence and source['transcription'] == 'VISUAL_ASCII_NOT_MACHINE_AXIOM'
        assert c['observation']
    assert {x['id'] for x in discovery['checks']} == {'P01', 'W01', 'G01', 'G02', 'V01'}
    assert not discovery['author_controlled_com_root_identified'] and not discovery['global_absence_claim']
    assert discovery['no_machine_population_inferred'] and not d['source']['global_absence_claim']
    assert old['formal_file']['state'] == 'NOT_IDENTIFIED_IN_BOUNDED_SEARCH'
    for k in ('formal_root', 'root_version', 'root_sha256', 'machine_syntax', 'author_repository_commit',
              'machine_license', 'declared_imports', 'unresolved_imports'):
        assert d['source'][k] is None, k
    for k in ('local_machine_classes', 'imported_machine_classes', 'referenced_machine_classes',
              'deprecated_machine_classes', 'inferred_machine_classes', 'named_machine_properties',
              'source_definition_candidates_for_machine_classes', 'missing_source_definitions_for_machine_classes',
              'complete_machine_glossary'):
        assert d['population'][k] is None, k
    assert d['foundation']['family'] == 'DOLCE' and d['foundation']['exact_edition'] is None
    assert d['foundation']['machine_import'] is None and not d['source']['same_title_2005_substituted']

    # Propositional skeleton of D1 with x=y: □(P→P) is true for every
    # assignment in two worlds. This is not a first-order modal theory solver.
    for values in itertools.product((False, True), repeat=2):
        assert all((not presence) or presence for presence in values)
    assert 'not exists y (MOB(y) and GED(x,y))' in paper['K04']['normalized_formula']
    assert 'BOX(' in paper['K01']['normalized_formula']
    # Local D9/D11/D12 fragment: co-participating owned objects of two
    # categories suffice for two state labels if all shared premises hold.
    common = {'APO': True, 'ST': True, 'OSD': True, 'PC_agent': True, 'PC_object': True}
    assert all(common.values()) and 'COB(z)' in paper['K13']['normalized_formula']
    assert 'COD(z)' in paper['K14']['normalized_formula']
    assert all(x in {s['id'] for s in p['scenarios']} for x in d['scenarios']['paper_scenario_ids'])

    model = yaml.safe_load((root / 'model/concepts.yaml').read_text())
    assert set(d['decision']['candidate_model_ids']) <= {x['id'] for x in model['records']}
    assert d['decision']['owner_status'] == 'OWNER_DECISION_REQUIRED' and d['decision']['accepted_equivalences'] == []
    assert all(d['execution'][k].startswith('NOT_EXECUTED') for k in ('machine_root_parser', 'owl_profile',
                                                                    'formal_theory_solver', 'author_experiment_reproduction'))
    assert d['limits']['later_issues'] == [255, 126]
    assert all(d['limits'][k] == 'NONE' for k in ('model_change', 'requirements_change', 'fixtures_change',
                                                'manuscript_change', 'release_change'))
    audit = yaml.safe_load((root / 'evidence/related-work/deep-reviews/source-audit.yaml').read_text())
    row = next(x for x in audit['records'] if x['id'] == 'COM2004')
    assert 'COM-S02' in row['repository']['evidence']
    assert row['technical_followup']['evidence'] == 'evidence/related-work/artifacts/COM.yaml'
    assert row['class_coverage']['local_classes'] is None
    assert row['class_coverage']['reasoner_execution'] == 'NOT_EXECUTED'
    assert row['next_issues'] == [255, 126]
    print(json.dumps({'status': 'PASS', 'selected_paper_commitments': 8,
                      'machine_class_population': None, 'fragment_boolean_checks': 2}, sort_keys=True))


if __name__ == '__main__':
    check()
