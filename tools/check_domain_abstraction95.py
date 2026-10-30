"""Check the Abstraction dossier and a selected SC0005 endpoint join."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return yaml.safe_load((ROOT / path).read_text())


def records(path):
    return {row['id']: row for row in load(path)['records']}


def ancestors(concept_id, generalizations):
    parents = {row['child_id']: row['parent_id'] for row in generalizations.values()}
    seen = {concept_id}
    while concept_id in parents:
        concept_id = parents[concept_id]
        assert concept_id not in seen, 'Cyclic type path in selected fixture'
        seen.add(concept_id)
    return seen


def selected_endpoint_alignment(fixture, concepts, relations, generalizations):
    nodes = {n['id']: n['concept_id'] for n in fixture['nodes']}
    assert nodes.get('description') == 'CLR-C0053'
    assert all(cid in concepts for cid in nodes.values())
    groups = {rid: [] for rid in ('CLR-R0079', 'CLR-R0080', 'CLR-R0132', 'CLR-R0133')}
    for edge in fixture['edges']:
        rid, source, target = edge['relation_id'], edge['source'], edge['target']
        assert rid in groups and source == 'description' and target in nodes
        relation = relations[rid]
        assert relation['source_id'] in ancestors(nodes[source], generalizations)
        assert relation['target_id'] in ancestors(nodes[target], generalizations)
        groups[rid].append(target)
    assert all(len(targets) == 1 for targets in groups.values())
    assert groups['CLR-R0079'][0] != groups['CLR-R0080'][0], 'Fixture must have distinct descriptions'
    return (groups['CLR-R0080'] == groups['CLR-R0132'] and
            groups['CLR-R0079'] == groups['CLR-R0133'])


def check():
    report = load('evaluation/domain-adequacy/abstraction.yaml')
    assert (report['issue'], report['task_id'], report['domain_id']) == (95, 'R2-DOM-04', 'CLR-D0004')
    assert report['model_revision'] == 'input-r1-rev1'
    for path, digest in report['input_bindings'].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    domains, concepts, relations, gens, constraints = map(records, (
        'model/domains.yaml', 'model/concepts.yaml', 'model/relations.yaml',
        'model/generalizations.yaml', 'model/constraints.yaml'))
    frs, cqs = map(records, ('requirements/functional.yaml',
                              'requirements/competency-questions.yaml'))
    support = {x['concept_id']: x for x in load('evidence/concept-support.yaml')['records']}
    domain = domains[report['domain_id']]
    assert (domain['label_en'], domain['purpose']) == (report['domain_name'], report['purpose'])
    members = {x['id'] for x in concepts.values() if x['primary_domain_id'] == report['domain_id']}
    assert len(members) == report['scope']['primary_domain_concepts'] == 6
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
    for cid in ('CLR-SC0005', 'CLR-SC0006', 'CLR-SC0007'):
        assert constraints[cid]['execution_status'] == 'not_executed'
    for child, parent in [('CLR-C0017', 'CLR-C0022'), ('CLR-C0053', 'CLR-C0099'),
                          ('CLR-C0099', 'CLR-C0022'), ('CLR-C0060', 'CLR-C0099')]:
        assert parent in ancestors(child, gens)
    pos = load(report['scenarios']['positive']['locator'])
    neg = load(report['scenarios']['adverse']['locator'])
    assert pos['id'] == report['scenarios']['positive']['id']
    assert neg['id'] == report['scenarios']['adverse']['id']
    assert pos['constraint_id'] == neg['constraint_id'] == 'CLR-SC0005'
    assert pos['expected'] == 'accept_selected_generalization_endpoints'
    assert neg['expected'] == 'reject_selected_generalization_endpoints'
    assert selected_endpoint_alignment(pos, concepts, relations, gens)
    assert not selected_endpoint_alignment(neg, concepts, relations, gens)
    assert report['scenarios']['conceptual_countercase']['execution'] == 'NOT_EXECUTED'
    assert {x['id'] for x in report['findings']} == {f'DOM04-F{i:02d}' for i in range(1, 6)}
    cells = {x['id'] for i in range(1, 7)
             for x in load(f'evidence/related-work/comparisons/batch-{i}.yaml')['matrix']}
    assert set(report['source_comparison']['source_cells']) <= cells
    assert all(report['decision'][x] == 'NONE' for x in
               ('model_change', 'requirements_change', 'manuscript_change', 'release_change'))
    assert report['decision']['semantic_adequacy'] == 'NOT_ASSESSED'
    assert '[Abstraction domain assessment]' in (ROOT / 'README.md').read_text()
    return {'status': 'PASS', 'domain_members': 6, 'questions': 3, 'findings': 5,
            'selected_generalization_endpoint_positive_adverse': 'PASS',
            'cq_execution': 'NOT_EXECUTED', 'semantic_adequacy': 'NOT_ASSESSED'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
