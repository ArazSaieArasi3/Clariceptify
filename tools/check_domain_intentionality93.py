"""Check the Intentionality dossier and one selected SC0003 agent join."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return yaml.safe_load((ROOT / path).read_text())


def records(path):
    return {row['id']: row for row in load(path)['records']}


def aligned(fixture):
    """Evaluate only bearers of motivating intentions in this episode slice."""
    edges = fixture['edges']
    participants = {(e['source'], e['target']) for e in edges if e['relation_id'] == 'CLR-R0054'}
    bearers = {(e['source'], e['target']) for e in edges if e['relation_id'] == 'CLR-R0007'}
    motivations = {(e['source'], e['target']) for e in edges if e['relation_id'] == 'CLR-R0051'}
    assert participants and bearers and motivations
    return all(any((bearer, episode) in participants for bearer, state in bearers if state == intention)
               for episode, intention in motivations)


def check():
    report = load('evaluation/domain-adequacy/intentionality.yaml')
    assert report['issue'] == 93 and report['task_id'] == 'R2-DOM-02'
    assert report['domain_id'] == 'CLR-D0002' and report['model_revision'] == 'input-r1-rev1'
    for path, digest in report['input_bindings'].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    domains, concepts, relations, gens, constraints = map(records, (
        'model/domains.yaml', 'model/concepts.yaml', 'model/relations.yaml',
        'model/generalizations.yaml', 'model/constraints.yaml'))
    frs, cqs = map(records, ('requirements/functional.yaml',
                              'requirements/competency-questions.yaml'))
    support = {x['concept_id']: x for x in load('evidence/concept-support.yaml')['records']}
    assert (domains[report['domain_id']]['label_en'], domains[report['domain_id']]['purpose']) == (
        report['domain_name'], report['purpose'])
    members = {x['id'] for x in concepts.values() if x['primary_domain_id'] == report['domain_id']}
    assert len(members) == report['scope']['primary_domain_concepts'] == 4
    assert members == set(report['scope']['domain_member_ids'])
    assert {x['id'] for x in report['concept_review']} == members
    for x in report['concept_review']:
        actual = concepts[x['id']]
        assert (x['label'], x['stereotype']) == (actual['label_en'], actual['ontouml_stereotype'])
        assert x['source_support'] == support[x['id']]['support_type']
        assert support[x['id']]['passage_verification'] == 'not_reverified_in_import'
        assert support[x['id']]['typing_approval'] == 'not_assessed'
    assert len(report['domain_questions']) == 3
    assert {q['contracts'][0] for q in report['domain_questions']} == set(report['scope']['relevant_requirements'])
    assert {q['contracts'][1] for q in report['domain_questions']} == set(report['scope']['relevant_cqs'])
    for q in report['domain_questions']:
        fr, cq = q['contracts']
        assert fr in frs and cq in cqs and cqs[cq]['requirement_id'] == fr
        assert cqs[cq]['test_execution'] == 'not_executed' and cqs[cq]['answer_status'] == 'not_computed'
        assert set(q['model_ids']) <= concepts.keys()
        assert set(q['relation_ids']) <= relations.keys()
        assert set(q['constraint_ids']) <= constraints.keys()
        assert q['outcome'] and q['evidence']
    assert {'CLR-G0050', 'CLR-G0113', 'CLR-G0114'} <= gens.keys()
    for rel, source, target in [('CLR-R0007', 'CLR-C0004', 'CLR-C0061'),
                                ('CLR-R0051', 'CLR-C0026', 'CLR-C0061'),
                                ('CLR-R0089', 'CLR-C0061', 'CLR-C0054'),
                                ('CLR-R0170', 'CLR-C0128', 'CLR-C0129'),
                                ('CLR-R0061', 'CLR-C0039', 'CLR-C0054')]:
        assert (relations[rel]['source_id'], relations[rel]['target_id']) == (source, target)
    assert constraints['CLR-SC0003']['execution_status'] == 'not_executed'
    pos = load(report['scenarios']['positive']['locator'])
    neg = load(report['scenarios']['adverse']['locator'])
    assert pos['id'] == report['scenarios']['positive']['id']
    assert neg['id'] == report['scenarios']['adverse']['id']
    assert neg['expected'] == 'reject_agent_alignment'
    assert aligned(pos) and not aligned(neg)
    assert report['scenarios']['conceptual_countercase']['execution'] == 'NOT_EXECUTED'
    assert {x['id'] for x in report['findings']} == {f'DOM02-F{i:02d}' for i in range(1, 5)}
    cells = {x['id'] for i in range(1, 7)
             for x in load(f'evidence/related-work/comparisons/batch-{i}.yaml')['matrix']}
    assert set(report['source_comparison']['source_cells']) <= cells
    assert all(report['decision'][x] == 'NONE' for x in
               ('model_change', 'requirements_change', 'manuscript_change', 'release_change'))
    assert report['decision']['semantic_adequacy'] == 'NOT_ASSESSED'
    assert '[Intentionality domain assessment]' in (ROOT / 'README.md').read_text()
    return {'status': 'PASS', 'domain_members': 4, 'questions': 3, 'findings': 4,
            'selected_positive_negative_agent_join': 'PASS',
            'cq_execution': 'NOT_EXECUTED', 'semantic_adequacy': 'NOT_ASSESSED'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
