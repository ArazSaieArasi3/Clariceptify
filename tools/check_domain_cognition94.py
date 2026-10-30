"""Check the Cognition domain review and selected observation subject union."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return yaml.safe_load((ROOT / path).read_text())


def records(path):
    return {row['id']: row for row in load(path)['records']}


def check_selected_observation(fixture, concepts, relations):
    nodes = {n['id']: n['concept_id'] for n in fixture['nodes']}
    edges = fixture['edges']
    assert nodes.get('observation') == 'CLR-C0084'
    assert any(e['relation_id'] == 'CLR-R0118' and e['target'] == 'observation'
               and nodes[e['source']] == 'CLR-C0085' for e in edges)
    subject_relations = {'CLR-R0115', 'CLR-R0116', 'CLR-R0117'}
    for e in edges:
        assert e['relation_id'] in relations
        assert e['source'] in nodes and e['target'] in nodes
        assert (relations[e['relation_id']]['source_id'],
                relations[e['relation_id']]['target_id']) == (
                    nodes[e['source']], nodes[e['target']])
        assert nodes[e['source']] in concepts and nodes[e['target']] in concepts
    return any(e['source'] == 'observation' and e['relation_id'] in subject_relations
               for e in edges)


def check():
    report = load('evaluation/domain-adequacy/cognition.yaml')
    assert report['issue'] == 94 and report['task_id'] == 'R2-DOM-03'
    assert report['domain_id'] == 'CLR-D0003' and report['model_revision'] == 'input-r1-rev1'
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
    assert len(members) == report['scope']['primary_domain_concepts'] == 13
    assert members == set(report['scope']['domain_member_ids'])
    assert {x['id'] for x in report['concept_review']} == members
    for entry in report['concept_review']:
        actual = concepts[entry['id']]
        assert (entry['label'], entry['stereotype']) == (
            actual['label_en'], actual['ontouml_stereotype'])
        assert entry['source_support'] == support[entry['id']]['support_type']
        assert support[entry['id']]['passage_verification'] == 'not_reverified_in_import'
        assert support[entry['id']]['typing_approval'] == 'not_assessed'
    assert len(report['domain_questions']) == 4
    assert {q['contracts'][0] for q in report['domain_questions']} == set(report['scope']['relevant_requirements'])
    assert {q['contracts'][1] for q in report['domain_questions']} == set(report['scope']['relevant_cqs'])
    for q in report['domain_questions']:
        fr, cq = q['contracts']
        assert fr in frs and cq in cqs and cqs[cq]['requirement_id'] == fr
        assert cqs[cq]['test_execution'] == 'not_executed' and cqs[cq]['answer_status'] == 'not_computed'
        assert set(q['model_ids']) <= concepts.keys()
        assert set(q['relation_ids']) <= relations.keys()
        assert set(q['constraint_ids']) <= constraints.keys()
    additional = report['additional_domain_question']
    assert additional['related_contract'] == ['FR-05', 'CQ-05']
    assert set(additional['relation_ids']) <= relations.keys()
    assert constraints['CLR-SC0012']['execution_status'] == 'not_executed'
    assert constraints['CLR-SC0001']['execution_status'] == 'not_executed'
    assert (gens['CLR-G0053']['child_id'], gens['CLR-G0053']['parent_id']) == (
        'CLR-C0058', 'CLR-C0127')
    assert concepts['CLR-C0058']['ontouml_stereotype'] == '«subkind»'
    assert concepts['CLR-C0127']['ontouml_stereotype'] == '«mode»'
    pos = load(report['scenarios']['positive']['locator'])
    neg = load(report['scenarios']['adverse']['locator'])
    assert pos['id'] == report['scenarios']['positive']['id'] and pos['expected'] == 'accept'
    assert neg['id'] == report['scenarios']['adverse']['id']
    assert neg['expected'] == 'reject_empty_observation_union'
    assert pos['constraint_id'] == neg['constraint_id'] == 'CLR-SC0001'
    assert check_selected_observation(pos, concepts, relations)
    assert not check_selected_observation(neg, concepts, relations)
    assert all(e['relation_id'] != 'CLR-R0115' for e in pos['edges'])
    assert report['scenarios']['conceptual_countercase']['execution'] == 'NOT_EXECUTED'
    assert {x['id'] for x in report['findings']} == {f'DOM03-F{i:02d}' for i in range(1, 6)}
    cells = {x['id'] for i in range(1, 7)
             for x in load(f'evidence/related-work/comparisons/batch-{i}.yaml')['matrix']}
    assert set(report['source_comparison']['source_cells']) <= cells
    assert all(report['decision'][x] == 'NONE' for x in
               ('model_change', 'requirements_change', 'manuscript_change', 'release_change'))
    assert report['decision']['semantic_adequacy'] == 'NOT_ASSESSED'
    assert '[Cognition domain assessment]' in (ROOT / 'README.md').read_text()
    return {'status': 'PASS', 'domain_members': 13, 'questions': 4,
            'supplemental_question': 1, 'findings': 5,
            'selected_positive_negative_observation_union': 'PASS',
            'cq_execution': 'NOT_EXECUTED', 'semantic_adequacy': 'NOT_ASSESSED'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
