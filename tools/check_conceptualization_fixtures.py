#!/usr/bin/env python3
"""Check a bounded synthetic episode and subject-union counterexample.

This is not an OWL/SHACL engine or a general instance-conformance validator.
"""
import argparse
import copy
import hashlib
import json
import re
from pathlib import Path
import sys

import yaml

SUBJECT_RELATIONS = {'CLR-R0043', 'CLR-R0044', 'CLR-R0045', 'CLR-R0046', 'CLR-R0047'}
INPUT_PATHS = {'model/concepts.yaml', 'model/relations.yaml', 'model/generalizations.yaml', 'model/constraints.yaml', 'requirements/functional.yaml', 'requirements/competency-questions.yaml'}
ROLE_TYPES = {'agent': 'CLR-C0004', 'mental_state': 'CLR-C0061', 'goal': 'CLR-C0054', 'activity': 'CLR-C0026', 'content': 'CLR-C0017', 'product': 'CLR-C0019'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_yaml(path):
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    require(isinstance(data, dict), f'Expected mapping: {path}')
    return data


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(root, positive_only=False):
    positive_path = root / 'evaluation/fixtures/conceptualization-positive.yaml'
    negative_path = root / 'evaluation/fixtures/conceptualization-negative.yaml'
    positive = read_yaml(positive_path)
    negative = None if positive_only else read_yaml(negative_path)
    fixtures = (positive,) if positive_only else (positive, negative)
    require(positive['id'] == 'CLR-FIX-POS-001', 'Unexpected positive fixture ID')
    if negative is not None:
        require(negative['id'] == 'CLR-FIX-NEG-001', 'Unexpected negative fixture ID')
    for fixture in fixtures:
        require(fixture['evidence_kind'] == 'synthetic_illustrative_fixture', 'Wrong evidence kind')
        bindings = fixture['input_bindings']
        require(len(bindings) == len(INPUT_PATHS) and {b['path'] for b in bindings} == INPUT_PATHS, 'Input binding set mismatch')
        for b in bindings:
            require(sha(root / b['path']) == b['sha256'], f"Input digest mismatch: {b['path']}")
        require(fixture['model_revision'] == 'input-r1-rev1', 'Unexpected model revision')
    concepts = {x['id']: x for x in read_yaml(root / 'model/concepts.yaml')['records']}
    relations = {x['id']: x for x in read_yaml(root / 'model/relations.yaml')['records']}
    constraints = {x['id']: x for x in read_yaml(root / 'model/constraints.yaml')['records']}
    reqs = {x['id']: x for x in read_yaml(root / 'requirements/functional.yaml')['records']}
    cqs = {x['id']: x for x in read_yaml(root / 'requirements/competency-questions.yaml')['records']}
    parents = {}
    for g in read_yaml(root / 'model/generalizations.yaml')['records']:
        parents.setdefault(g['child_id'], set()).add(g['parent_id'])

    def compatible(actual, expected):
        seen, queue = set(), [actual]
        while queue:
            cur = queue.pop()
            if cur == expected:
                return True
            if cur not in seen:
                seen.add(cur)
                queue.extend(parents.get(cur, ()))
        return False

    nodes = {n['id']: n for n in positive['nodes']}
    require(len(nodes) == len(positive['nodes']), 'Duplicate fixture node ID')
    for n in nodes.values():
        require(isinstance(n['id'], str) and re.fullmatch(r'[a-z][a-z0-9-]*', n['id']) is not None, 'Malformed fixture node ID')
        require(n['concept_id'] in concepts, 'Unknown concept ID')
        require(bool(n['description'].strip()), 'Empty node description')
    roles = positive['required_roles']
    require(set(roles) == set(ROLE_TYPES), 'Required role set mismatch')
    require(len(set(roles.values())) == len(roles), 'Fixture roles unexpectedly identified')
    for role, expected in ROLE_TYPES.items():
        require(roles[role] in nodes, f'Missing role node: {role}')
        require(compatible(nodes[roles[role]]['concept_id'], expected), f'Role type mismatch: {role}')
    edge_tuples = set()
    for e in positive['edges']:
        require(e['relation_id'] in relations, 'Unknown relation ID')
        require(e['source'] in nodes and e['target'] in nodes, 'Missing endpoint')
        r = relations[e['relation_id']]
        require(compatible(nodes[e['source']]['concept_id'], r['source_id']), 'Source endpoint type mismatch')
        require(compatible(nodes[e['target']]['concept_id'], r['target_id']), 'Target endpoint type mismatch')
        tup = (e['relation_id'], e['source'], e['target'])
        require(tup not in edge_tuples, 'Duplicate edge')
        edge_tuples.add(tup)
    # These are local scenario-witness checks, not promotion of global FR/CQ status.
    for tup in [('CLR-R0054', roles['agent'], roles['activity']), ('CLR-R0007', roles['agent'], roles['mental_state']), ('CLR-R0051', roles['activity'], roles['mental_state']), ('CLR-R0089', roles['mental_state'], roles['goal']), ('CLR-R0048', roles['activity'], roles['product']), ('CLR-R0032', roles['product'], roles['content'])]:
        require(tup in edge_tuples, f'Missing scenario witness: {tup}')
    perspectives = {target for rel, source, target in edge_tuples if rel == 'CLR-R0042' and source == roles['activity']}
    require(bool(perspectives), 'Missing adopted perspective')
    require(all(('CLR-R0008', roles['agent'], perspective) in edge_tuples for perspective in perspectives), 'Perspective bearer is not the scenario agent')
    require(len(positive['requirement_links']) == 4, 'Expected four unique requirement links')
    for binding in positive['requirement_links']:
        require(binding['id'] in reqs and binding['cq_id'] in cqs, 'Unknown FR/CQ link')
        require(cqs[binding['cq_id']]['requirement_id'] == binding['id'], 'FR/CQ pairing mismatch')
    require({b['id'] for b in positive['requirement_links']} == {'FR-01', 'FR-02', 'FR-03', 'FR-04'}, 'Fixture requirement coverage changed')
    require(positive['selected_check']['constraint_id'] == 'CLR-SC0001', 'Wrong selected constraint')
    if negative is not None:
        require(negative['constraint_id'] == 'CLR-SC0001', 'Wrong negative constraint')
    require('Every Conceptualization concerns at least one subject across Object, Event, Type, State and Time.' in constraints['CLR-SC0001']['text'], 'Conceptualization subject clause changed')
    require('Optional individual branches do not permit an empty combined subject.' in constraints['CLR-SC0001']['text'], 'Subject-union textual contract changed')
    focus = positive['selected_check']['focus']
    require(focus == roles['activity'], 'Focus is not designated episode')

    def violations(edges):
        subjects = {e['target'] for e in edges if e['source'] == focus and e['relation_id'] in SUBJECT_RELATIONS}
        return [] if subjects else ['EMPTY_SUBJECT_UNION']

    positive_actual = violations(positive['edges'])
    require(positive['selected_check']['expected'] == 'accept' and positive_actual == positive['selected_check']['expected_violation_codes'] == [], 'Positive fixture failed selected check')
    results = [{'id': positive['id'], 'result': 'accepted_for_selected_check', 'violation_codes': positive_actual}]
    fixture_paths = [positive_path]
    if not positive_only:
        require(negative['derived_from'] == positive['id'], 'Counterexample source mismatch')
        require(negative['positive_fixture'] == 'evaluation/fixtures/conceptualization-positive.yaml', 'Unexpected source path')
        mutation = negative['mutation']
        require(mutation['operation'] == 'remove_focus_subject_edges' and mutation['focus'] == focus, 'Unexpected mutation')
        require(len(mutation['relation_ids']) == 5 and set(mutation['relation_ids']) == SUBJECT_RELATIONS, 'Mutation relation set mismatch')
        mutated = [e for e in copy.deepcopy(positive['edges']) if not (e['source'] == focus and e['relation_id'] in SUBJECT_RELATIONS)]
        require(len(mutated) < len(positive['edges']), 'Counterexample made no change')
        negative_actual = violations(mutated)
        require(negative['expected'] == 'reject' and negative_actual == negative['expected_violation_codes'] == ['EMPTY_SUBJECT_UNION'], 'Counterexample was not rejected for expected reason')
        require(negative['requirement_links'] == ['FR-02', 'CQ-02'], 'Counterexample FR/CQ scope mismatch')
        results.append({'id': negative['id'], 'result': 'rejected_as_expected', 'violation_codes': negative_actual})
        fixture_paths.append(negative_path)
    return {'schema_version': '1.0', 'status': 'PASS', 'scope': 'positive_only' if positive_only else 'positive_and_negative', 'evidence_kind': 'synthetic_illustrative_fixture_check', 'fixture_results': results, 'input_bindings': positive['input_bindings'], 'fixture_digests': {str(p.relative_to(root)): sha(p) for p in fixture_paths}, 'tool_sha256': sha(Path(__file__)), 'counts': {'nodes': len(nodes), 'edges': len(positive['edges']), 'linked_requirements': 4, 'textual_constraint_clauses_checked': 1}, 'claim_ceiling': positive['claim_ceiling'], 'global_requirement_cq_status_changed': False, 'unassessed': positive['unassessed']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path)
    parser.add_argument('--positive-only', action='store_true', help='Check #48 without reading or requiring the #49 negative fixture')
    args = parser.parse_args()
    try:
        result = run(args.root.resolve(), positive_only=args.positive_only)
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as exc:
        print(json.dumps({'status': 'FAIL', 'reason': str(exc)}))
        return 1
    rendered = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding='utf-8')
    print(rendered)
    return 0


if __name__ == '__main__':
    sys.exit(main())
