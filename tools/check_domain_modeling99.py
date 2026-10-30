"""Check Modeling domain evidence and one selected activity/model/view query join."""
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


def selected_model_view_join(fixture, concepts, relations, gens):
    nodes = {n['id']: n['concept_id'] for n in fixture['nodes']}
    assert len(nodes) == len(fixture['nodes']) and set(nodes.values()) <= concepts.keys()
    assert nodes['activity'] == 'CLR-C0077' and nodes['view'] == 'CLR-C0076'
    edges = fixture['edges']
    assert len(edges) == len({(e['relation_id'], e['source'], e['target']) for e in edges})
    allowed = {'CLR-R0110', 'CLR-R0109', 'CLR-R0108', 'CLR-R0140'}
    assert {e['relation_id'] for e in edges} == allowed
    for e in edges:
        rid, source, target = e['relation_id'], e['source'], e['target']
        assert source in nodes and target in nodes
        rel = relations[rid]
        assert rel['source_id'] in ancestors(nodes[source], gens)
        assert rel['target_id'] in ancestors(nodes[target], gens)
    pairs = lambda rid: {(e['source'], e['target']) for e in edges if e['relation_id'] == rid}
    produced, viewed, viewpoints, encoded = map(pairs,
        ('CLR-R0110', 'CLR-R0109', 'CLR-R0108', 'CLR-R0140'))
    assert len(produced) == len(viewed) == len(viewpoints) == len(encoded) == 1
    assert all(src == 'activity' for src, _ in produced)
    assert all(src == 'view' for src, _ in viewed | viewpoints)
    return any((model, 'artifact') in encoded and ('view', model) in viewed
               for _, model in produced)


def check():
    report = load('evaluation/domain-adequacy/modeling.yaml')
    assert (report['issue'], report['task_id'], report['domain_id']) == (99, 'R2-DOM-08', 'CLR-D0008')
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
    assert len(members) == report['scope']['primary_domain_concepts'] == 17
    assert members == set(report['scope']['domain_member_ids'])
    assert {x['id'] for x in report['concept_review']} == members
    for x in report['concept_review']:
        actual = concepts[x['id']]
        assert (x['label'], x['stereotype']) == (actual['label_en'], actual['ontouml_stereotype'])
        assert x['source_support'] == support[x['id']]['support_type']
        assert support[x['id']]['passage_verification'] == 'not_reverified_in_import'
        assert support[x['id']]['typing_approval'] == 'not_assessed'
    pending = {cid for cid in members if support[cid]['support_type'] == 'P'}
    assert len(pending) == 9 and pending == set(report['scope']['in_model_support_p'])
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
    for cid in ('CLR-SC0023', 'CLR-SC0024', 'CLR-SC0010', 'CLR-SC0009'):
        assert constraints[cid]['execution_status'] == 'not_executed'
    for child, parent in [('CLR-C0023', 'CLR-C0073'), ('CLR-C0073', 'CLR-C0101'),
                          ('CLR-C0074', 'CLR-C0125'), ('CLR-C0024', 'CLR-C0077')]:
        assert parent in ancestors(child, gens)
    pos = load(report['scenarios']['positive']['locator'])
    neg = load(report['scenarios']['adverse']['locator'])
    assert pos['id'] == report['scenarios']['positive']['id']
    assert neg['id'] == report['scenarios']['adverse']['id']
    assert pos['expected'] == 'selected_model_view_join'
    assert neg['expected'] == 'no_selected_model_view_join'
    assert selected_model_view_join(pos, concepts, relations, gens)
    assert not selected_model_view_join(neg, concepts, relations, gens)
    assert report['scenarios']['conceptual_countercase']['execution'] == 'NOT_EXECUTED'
    assert {x['id'] for x in report['findings']} == {f'DOM08-F{i:02d}' for i in range(1, 6)}
    cells = {x['id'] for i in range(1, 7)
             for x in load(f'evidence/related-work/comparisons/batch-{i}.yaml')['matrix']}
    assert set(report['source_comparison']['source_cells']) <= cells
    assert all(report['decision'][x] == 'NONE' for x in
               ('model_change', 'requirements_change', 'manuscript_change', 'release_change'))
    assert report['decision']['semantic_adequacy'] == 'NOT_ASSESSED'
    assert '[Modeling domain assessment]' in (ROOT / 'README.md').read_text()
    return {'status': 'PASS', 'domain_members': 17, 'questions': 4, 'findings': 5,
            'in_model_p_support': 9, 'selected_positive_adverse_model_view_join': 'PASS',
            'cq_execution': 'NOT_EXECUTED', 'semantic_adequacy': 'NOT_ASSESSED'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
