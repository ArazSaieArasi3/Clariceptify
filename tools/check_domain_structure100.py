"""Check the Structure domain report and a selected shared-description query path."""
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


def selected_shared_description(fixture, concepts, relations, gens):
    nodes = {n['id']: n['concept_id'] for n in fixture['nodes']}
    assert len(nodes) == len(fixture['nodes']) and set(nodes.values()) <= concepts.keys()
    assert nodes['structure'] == 'CLR-C0116'
    assert nodes['part'] == 'CLR-C0088' and nodes['whole'] == 'CLR-C0137'
    edges = fixture['edges']
    assert len(edges) == len({(e['relation_id'], e['source'], e['target']) for e in edges})
    allowed = {'CLR-R0156', 'CLR-R0157', 'CLR-R0122', 'CLR-R0123'}
    assert {e['relation_id'] for e in edges} == allowed
    for e in edges:
        source, target, rid = e['source'], e['target'], e['relation_id']
        assert source in nodes and target in nodes
        rel = relations[rid]
        assert rel['source_id'] in ancestors(nodes[source], gens)
        assert rel['target_id'] in ancestors(nodes[target], gens)
    pairs = lambda rid: {(e['source'], e['target']) for e in edges if e['relation_id'] == rid}
    organized, specified, parts, wholes = map(pairs,
        ('CLR-R0156', 'CLR-R0157', 'CLR-R0122', 'CLR-R0123'))
    assert organized == {('structure', 'part'), ('structure', 'whole')}
    assert all(src == 'structure' for src, _ in specified)
    assert all(nodes[src] == 'CLR-C0089' for src, _ in parts | wholes)
    assert {target for _, target in parts} == {'part'}
    assert {target for _, target in wholes} == {'whole'}
    return any((relation, 'part') in parts and (relation, 'whole') in wholes
               for _, relation in specified)


def check():
    report = load('evaluation/domain-adequacy/structure.yaml')
    assert (report['issue'], report['task_id'], report['domain_id']) == (100, 'R2-DOM-09', 'CLR-D0009')
    assert report['model_revision'] == 'input-r1-rev1'
    assert report['baseline_commit'] == 'f1bab3769fda065e6820c81034c2793b9068ba4d'
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
        assert x['source_support'] == support[x['id']]['support_type'] == 'B'
        assert support[x['id']]['passage_verification'] == 'not_reverified_in_import'
        assert support[x['id']]['typing_approval'] == 'not_assessed'
    assert report['scope']['relevant_requirements'] == ['FR-11']
    assert report['scope']['relevant_cqs'] == ['CQ-11']
    assert len(report['domain_questions']) == 2
    for q in report['domain_questions']:
        fr, cq = q['contracts']
        assert (fr, cq) == ('FR-11', 'CQ-11')
        assert fr in frs and cq in cqs and cqs[cq]['requirement_id'] == fr
        assert frs[fr]['test_execution'] == cqs[cq]['test_execution'] == 'not_executed'
        assert cqs[cq]['answer_status'] == 'not_computed'
        assert set(q['model_ids']) <= concepts.keys()
        assert set(q['relation_ids']) <= relations.keys()
        assert set(q['constraint_ids']) <= constraints.keys()
    for cid in ('CLR-SC0005', 'CLR-SC0007', 'CLR-SC0008', 'CLR-SC0009'):
        assert constraints[cid]['execution_status'] == 'not_executed'
    for child, parent in [('CLR-C0088', 'CLR-C0017'), ('CLR-C0137', 'CLR-C0017'),
                          ('CLR-C0089', 'CLR-C0099'), ('CLR-C0116', 'CLR-C0057'),
                          ('CLR-C0119', 'CLR-C0116')]:
        assert parent in ancestors(child, gens)
    pos = load(report['scenarios']['positive']['locator'])
    neg = load(report['scenarios']['adverse']['locator'])
    assert pos['id'] == report['scenarios']['positive']['id']
    assert neg['id'] == report['scenarios']['adverse']['id']
    assert pos['model_revision'] == neg['model_revision'] == report['model_revision']
    assert pos['expected'] == 'selected_shared_parthood_description'
    assert neg['expected'] == 'no_selected_shared_parthood_description'
    assert selected_shared_description(pos, concepts, relations, gens)
    assert not selected_shared_description(neg, concepts, relations, gens)
    assert report['scenarios']['conceptual_countercase']['execution'] == 'NOT_EXECUTED'
    assert {x['id'] for x in report['findings']} == {f'DOM09-F{i:02d}' for i in range(1, 6)}
    cells = {x['id'] for i in range(1, 7)
             for x in load(f'evidence/related-work/comparisons/batch-{i}.yaml')['matrix']}
    assert set(report['source_comparison']['source_cells']) <= cells
    assert all(report['decision'][x] == 'NONE' for x in
               ('model_change', 'requirements_change', 'manuscript_change', 'release_change'))
    assert report['decision']['semantic_adequacy'] == 'NOT_ASSESSED'
    assert '[Structure domain assessment]' in (ROOT / 'README.md').read_text()
    return {'status': 'PASS', 'domain_members': 6, 'questions': 2, 'findings': 5,
            'selected_positive_adverse_shared_description_join': 'PASS',
            'cq_execution': 'NOT_EXECUTED', 'semantic_adequacy': 'NOT_ASSESSED'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
