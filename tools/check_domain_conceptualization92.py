"""Check the Conceptualization domain review against its exact source baseline."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / 'evaluation/domain-adequacy/conceptualization.yaml'


def load(path):
    return yaml.safe_load((ROOT / path).read_text())


def check():
    report = yaml.safe_load(REPORT.read_text())
    assert report['issue'] == 92 and report['domain_id'] == 'CLR-D0001'
    assert report['model_revision'] == 'input-r1-rev1'
    for path, digest in report['input_bindings'].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    domains = {x['id']: x for x in load('model/domains.yaml')['records']}
    concepts = {x['id']: x for x in load('model/concepts.yaml')['records']}
    relations = {x['id']: x for x in load('model/relations.yaml')['records']}
    gens = {x['id']: x for x in load('model/generalizations.yaml')['records']}
    constraints = {x['id']: x for x in load('model/constraints.yaml')['records']}
    frs = {x['id']: x for x in load('requirements/functional.yaml')['records']}
    cqs = {x['id']: x for x in load('requirements/competency-questions.yaml')['records']}
    support = {x['concept_id']: x for x in load('evidence/concept-support.yaml')['records']}
    assert domains['CLR-D0001']['label_en'] == report['domain_name']
    assert domains['CLR-D0001']['purpose'] == report['purpose']
    members = {x['id'] for x in concepts.values() if x['primary_domain_id'] == report['domain_id']}
    assert len(members) == report['scope']['primary_domain_concepts'] == 9
    assert members == set(report['scope']['domain_member_ids'])
    assert len(report['concept_review']) == 9
    for entry in report['concept_review']:
        actual = concepts[entry['id']]
        assert entry['id'] in members
        assert (entry['label'], entry['stereotype']) == (actual['label_en'], actual['ontouml_stereotype'])
        assert entry['source_support'] == support[entry['id']]['support_type']
        assert support[entry['id']]['passage_verification'] == 'not_reverified_in_import'
    assert len(report['domain_questions']) == 7
    assert {i for q in report['domain_questions'] for i in q['contracts'] if i.startswith('FR-')} == set(report['scope']['relevant_requirements'])
    assert {i for q in report['domain_questions'] for i in q['contracts'] if i.startswith('CQ-')} == set(report['scope']['relevant_cqs'])
    for q in report['domain_questions']:
        assert len(q['contracts']) == 2
        assert q['contracts'][0] in frs and q['contracts'][1] in cqs
        assert cqs[q['contracts'][1]]['requirement_id'] == q['contracts'][0]
        assert set(q['model_ids']) <= set(concepts)
        assert set(q['relation_ids']) <= set(relations)
        assert set(q.get('generalization_ids', [])) <= set(gens)
        assert set(q.get('constraint_ids', [])) <= set(constraints)
        assert q['outcome'] and q['evidence']
    pos = load(report['scenarios']['positive']['locator'])
    neg = load(report['scenarios']['adverse']['locator'])
    receipt = json.loads((ROOT / 'evaluation/conceptualization-fixtures.json').read_text())
    assert pos['id'] == 'CLR-FIX-POS-001' and neg['id'] == 'CLR-FIX-NEG-001'
    assert neg['constraint_id'] == 'CLR-SC0001'
    actual = {x['id']: x for x in receipt['fixture_results']}
    assert actual[pos['id']]['result'] == 'accepted_for_selected_check'
    assert actual[neg['id']]['result'] == 'rejected_as_expected'
    assert actual[neg['id']]['violation_codes'] == ['EMPTY_SUBJECT_UNION']
    assert report['scenarios']['conceptual_countercase']['execution'] == 'NOT_EXECUTED'
    assert len(report['findings']) == 5
    assert {x['id'] for x in report['findings']} == {f'DOM01-F{i:02d}' for i in range(1, 6)}
    batches = [load(f'evidence/related-work/comparisons/batch-{i}.yaml') for i in range(1, 7)]
    cells = {x['id'] for b in batches for x in b['matrix']}
    assert set(report['source_comparison']['source_cells']) <= cells
    assert all(report['decision'][x] == 'NONE' for x in
               ('model_change', 'requirements_change', 'fixtures_change', 'manuscript_change', 'release_change'))
    assert report['decision']['semantic_adequacy'] == 'NOT_ASSESSED'
    assert '[Conceptualization domain assessment]' in (ROOT / 'README.md').read_text()
    return {'status': 'PASS', 'domain_members': 9, 'questions': 7, 'findings': 5,
            'selected_positive_negative_fixture': 'PASS', 'cq_execution': 'NOT_EXECUTED',
            'semantic_adequacy': 'NOT_ASSESSED'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
