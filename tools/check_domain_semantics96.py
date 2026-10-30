"""Check the Semantics dossier and a bounded interpretation-content query join."""
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
    parent = {x['child_id']: x['parent_id'] for x in gens.values()}
    seen = {cid}
    while cid in parent:
        cid = parent[cid]
        assert cid not in seen
        seen.add(cid)
    return seen


def selected_content_join(fixture, concepts, relations, gens):
    nodes = {n['id']: n['concept_id'] for n in fixture['nodes']}
    assert len(nodes) == len(fixture['nodes']) and set(nodes.values()) <= concepts.keys()
    selected = {'CLR-R0009', 'CLR-R0093', 'CLR-R0094', 'CLR-R0090', 'CLR-R0144'}
    edges = fixture['edges']
    assert {e['relation_id'] for e in edges} == selected and len(edges) == 5
    for e in edges:
        rel = relations[e['relation_id']]
        assert rel['source_id'] in ancestors(nodes[e['source']], gens)
        assert rel['target_id'] in ancestors(nodes[e['target']], gens)
    def pairs(rid):
        return {(e['source'], e['target']) for e in edges if e['relation_id'] == rid}
    bearer, interprets, originates, assigns, content_of = map(pairs,
        ('CLR-R0009', 'CLR-R0093', 'CLR-R0094', 'CLR-R0090', 'CLR-R0144'))
    return any((state, content) in assigns and (content, rep) in content_of and
               any(s == state for _, s in bearer)
               for process, rep in interprets for p, state in originates if p == process
               for s, content in assigns if s == state)


def check():
    report = load('evaluation/domain-adequacy/semantics.yaml')
    assert (report['issue'], report['task_id'], report['domain_id']) == (96, 'R2-DOM-05', 'CLR-D0005')
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
    assert len(members) == report['scope']['primary_domain_concepts'] == 7
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
    for cid in ('CLR-SC0011', 'CLR-SC0012', 'CLR-SC0016', 'CLR-SC0017'):
        assert constraints[cid]['execution_status'] == 'not_executed'
    assert 'CLR-C0127' in ancestors('CLR-C0062', gens)
    assert concepts['CLR-C0062']['ontouml_stereotype'] == '«subkind»'
    assert concepts['CLR-C0127']['ontouml_stereotype'] == '«mode»'
    pos = load(report['scenarios']['positive']['locator'])
    neg = load(report['scenarios']['adverse']['locator'])
    assert pos['id'] == report['scenarios']['positive']['id']
    assert neg['id'] == report['scenarios']['adverse']['id']
    assert pos['expected'] == 'accept_same_representation_join'
    assert neg['expected'] == 'reject_representation_mismatch'
    assert selected_content_join(pos, concepts, relations, gens)
    assert not selected_content_join(neg, concepts, relations, gens)
    assert report['scenarios']['conceptual_countercase']['execution'] == 'NOT_EXECUTED'
    assert {x['id'] for x in report['findings']} == {f'DOM05-F{i:02d}' for i in range(1, 6)}
    cells = {x['id'] for i in range(1, 7)
             for x in load(f'evidence/related-work/comparisons/batch-{i}.yaml')['matrix']}
    assert set(report['source_comparison']['source_cells']) <= cells
    assert all(report['decision'][x] == 'NONE' for x in
               ('model_change', 'requirements_change', 'manuscript_change', 'release_change'))
    assert report['decision']['semantic_adequacy'] == 'NOT_ASSESSED'
    assert '[Semantics domain assessment]' in (ROOT / 'README.md').read_text()
    return {'status': 'PASS', 'domain_members': 7, 'questions': 4, 'findings': 5,
            'selected_positive_adverse_content_join': 'PASS',
            'cq_execution': 'NOT_EXECUTED', 'semantic_adequacy': 'NOT_ASSESSED'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
