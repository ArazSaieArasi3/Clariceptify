"""Check Relations domain evidence and a selected CQ-10 endpoint/property join."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return yaml.safe_load((ROOT / path).read_text())


def records(path):
    return {row['id']: row for row in load(path)['records']}


def ancestors(cid, gens):
    parents = {x['child_id']: x['parent_id'] for x in gens.values()}
    seen = {cid}
    while cid in parents:
        cid = parents[cid]
        assert cid not in seen
        seen.add(cid)
    return seen


def selected_relation_query(fixture, concepts, relations, gens):
    nodes = {n['id']: n['concept_id'] for n in fixture['nodes']}
    assert len(nodes) == len(fixture['nodes']) and set(nodes.values()) <= concepts.keys()
    assert (nodes['process'], nodes['relation'], nodes['source_concept'],
            nodes['target_property']) == ('CLR-C0100', 'CLR-C0099', 'CLR-C0017', 'CLR-C0096')
    allowed = {'CLR-R0134', 'CLR-R0132', 'CLR-R0133', 'CLR-R0128'}
    edges = fixture['edges']
    assert len(edges) == len({(e['relation_id'], e['source'], e['target']) for e in edges})
    for e in edges:
        rid, source, target = e['relation_id'], e['source'], e['target']
        assert rid in allowed and source in nodes and target in nodes
        rel = relations[rid]
        assert rel['source_id'] in ancestors(nodes[source], gens)
        assert rel['target_id'] in ancestors(nodes[target], gens)
    pairs = {(e['relation_id'], e['source'], e['target']) for e in edges}
    required = {('CLR-R0134', 'process', 'relation'),
                ('CLR-R0132', 'relation', 'source_concept'),
                ('CLR-R0133', 'relation', 'target_property'),
                ('CLR-R0128', 'target_property', 'source_concept')}
    assert pairs <= required
    assert required - {('CLR-R0133', 'relation', 'target_property')} <= pairs
    return required <= pairs


def check():
    report = load('evaluation/domain-adequacy/relations.yaml')
    assert (report['issue'], report['task_id'], report['domain_id']) == (97, 'R2-DOM-06', 'CLR-D0006')
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
    assert len(members) == report['scope']['primary_domain_concepts'] == 5
    assert members == set(report['scope']['domain_member_ids'])
    assert {x['id'] for x in report['concept_review']} == members
    for x in report['concept_review']:
        actual = concepts[x['id']]
        assert (x['label'], x['stereotype']) == (actual['label_en'], actual['ontouml_stereotype'])
        assert x['source_support'] == support[x['id']]['support_type']
        assert support[x['id']]['passage_verification'] == 'not_reverified_in_import'
        assert support[x['id']]['typing_approval'] == 'not_assessed'
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
    for cid in ('CLR-SC0005', 'CLR-SC0008', 'CLR-SC0016'):
        assert constraints[cid]['execution_status'] == 'not_executed'
    for child, parent in [('CLR-C0020', 'CLR-C0099'), ('CLR-C0031', 'CLR-C0099'),
                          ('CLR-C0099', 'CLR-C0022'), ('CLR-C0096', 'CLR-C0022')]:
        assert parent in ancestors(child, gens)
    pos = load(report['scenarios']['positive']['locator'])
    neg = load(report['scenarios']['adverse']['locator'])
    assert pos['id'] == report['scenarios']['positive']['id']
    assert neg['id'] == report['scenarios']['adverse']['id']
    assert pos['expected'] == 'complete_selected_query_join'
    assert neg['expected'] == 'no_selected_query_answer'
    assert selected_relation_query(pos, concepts, relations, gens)
    assert not selected_relation_query(neg, concepts, relations, gens)
    assert report['scenarios']['conceptual_countercase']['execution'] == 'NOT_EXECUTED'
    assert {x['id'] for x in report['findings']} == {f'DOM06-F{i:02d}' for i in range(1, 6)}
    cells = {x['id'] for i in range(1, 7)
             for x in load(f'evidence/related-work/comparisons/batch-{i}.yaml')['matrix']}
    assert set(report['source_comparison']['source_cells']) <= cells
    assert all(report['decision'][x] == 'NONE' for x in
               ('model_change', 'requirements_change', 'manuscript_change', 'release_change'))
    assert report['decision']['semantic_adequacy'] == 'NOT_ASSESSED'
    assert '[Relations domain assessment]' in (ROOT / 'README.md').read_text()
    return {'status': 'PASS', 'domain_members': 5, 'questions': 4, 'findings': 5,
            'selected_positive_adverse_endpoint_query': 'PASS',
            'cq_execution': 'NOT_EXECUTED', 'semantic_adequacy': 'NOT_ASSESSED'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
