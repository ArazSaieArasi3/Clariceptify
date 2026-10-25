"""Check declared structural relations; connectivity is descriptive, not validity."""
from pathlib import Path
from collections import deque
import copy
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
NAMES = {'concept': 'concepts', 'domain': 'domains', 'relation': 'relations',
         'generalization': 'generalizations', 'constraint': 'constraints'}


def inspect(model):
    errors = []
    concepts = {row['id'] for row in model['concept']}
    domains = {row['id'] for row in model['domain']}
    adjacency = {identity: set() for identity in concepts}
    parents = {identity: set() for identity in concepts}
    for row in model['concept']:
        if row['primary_domain_id'] not in domains:
            errors.append({'code': 'missing_domain', 'id': row['id'], 'target': row['primary_domain_id']})
    pairs = set()
    for kind, left, right in [('relation', 'source_id', 'target_id'), ('generalization', 'child_id', 'parent_id')]:
        for row in model[kind]:
            a, b = row[left], row[right]
            if a not in concepts or b not in concepts:
                errors.append({'code': 'missing_endpoint', 'id': row['id'], 'source': a, 'target': b})
                continue
            adjacency[a].add(b)
            adjacency[b].add(a)
            if kind == 'generalization':
                if (a, b) in pairs:
                    errors.append({'code': 'duplicate_generalization_pair', 'id': row['id']})
                pairs.add((a, b))
                parents[a].add(b)
    degree = {identity: 0 for identity in concepts}
    for children in parents.values():
        for parent in children:
            degree[parent] += 1
    queue = deque(identity for identity, count in degree.items() if count == 0)
    visited = 0
    while queue:
        identity = queue.popleft()
        visited += 1
        for parent in parents[identity]:
            degree[parent] -= 1
            if degree[parent] == 0:
                queue.append(parent)
    if visited != len(concepts):
        errors.append({'code': 'generalization_cycle', 'affected_or_downstream_ids': sorted(identity for identity, count in degree.items() if count)})
    for row in model['constraint']:
        if any(identity not in concepts for identity in row['referenced_ids']):
            errors.append({'code': 'missing_constraint_mention', 'id': row['id']})
    remaining = set(concepts)
    components = 0
    while remaining:
        stack = [remaining.pop()]
        components += 1
        while stack:
            for neighbor in adjacency[stack.pop()] & remaining:
                remaining.remove(neighbor)
                stack.append(neighbor)
    return errors, components


def check():
    model = {kind: yaml.safe_load((ROOT / 'model' / (name + '.yaml')).read_text())['records'] for kind, name in NAMES.items()}
    errors, components = inspect(model)
    if errors:
        raise ValueError(errors[:20])
    rejected = []
    def two_cycle(changed):
        a, b = changed['concept'][0]['id'], changed['concept'][1]['id']
        changed['generalization'][0].update(child_id=a, parent_id=b)
        changed['generalization'][1].update(child_id=b, parent_id=a)
    for label, mutate, expected in [
            ('absent primary domain', lambda m: m['concept'][0].update(primary_domain_id='CLR-D9999'), 'missing_domain'),
            ('absent association endpoint', lambda m: m['relation'][0].update(target_id='CLR-C9999'), 'missing_endpoint'),
            ('absent inheritance endpoint', lambda m: m['generalization'][0].update(parent_id='CLR-C9999'), 'missing_endpoint'),
            ('self-specialization cycle', lambda m: m['generalization'][0].update(parent_id=m['generalization'][0]['child_id']), 'generalization_cycle'),
            ('two-node specialization cycle', two_cycle, 'generalization_cycle'),
            ('unknown constraint mention', lambda m: m['constraint'][0]['referenced_ids'].append('CLR-C9999'), 'missing_constraint_mention')]:
        changed = copy.deepcopy(model)
        mutate(changed)
        if expected not in {row['code'] for row in inspect(changed)[0]}:
            raise AssertionError('Expected structure rejection missing: ' + label)
        rejected.append(label)
    return {'status': 'PASS', 'scope': 'Declared domain/endpoints/hierarchy/lexical references only',
            'counts': {kind: len(rows) for kind, rows in model.items()},
            'connected_components_undirected': components, 'generalization_acyclic': True,
            'negative_cases_rejected': rejected,
            'input_file_sha256': {'model/' + name + '.yaml': hashlib.sha256((ROOT / 'model' / (name + '.yaml')).read_bytes()).hexdigest() for name in NAMES.values()},
            'limits': ['Connectivity is not meaningfulness, consistency, satisfiability or adequacy.',
                       'Constraint references remain lexical candidates; no execution or partition axiom is inferred.']}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
