"""Validate generated structural/source links against their actual records."""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json
import yaml
from jsonschema import Draft202012Validator
from build_trace_links import key, bind_ids

ROOT = Path(__file__).resolve().parents[1]


def context():
    def read(path):
        return yaml.safe_load((ROOT / path).read_text())
    assets = {row['asset_id']: row for row in read('traceability/artifacts.yaml')['records']}
    nodes = {}
    models = {}
    for kind, name in [('concept', 'concepts'), ('domain', 'domains'), ('association', 'relations'),
                       ('generalization', 'generalizations'), ('constraint', 'constraints')]:
        data = read('model/' + name + '.yaml')
        models[kind] = data['records']
        nodes.update({(kind, row['id']): data['asset_id'] for row in data['records']})
    refs = read('evidence/source-register.yaml')['records']
    nodes.update({('reference', row['id']): 'CLR-SOURCE-REGISTER' for row in refs})
    for name, asset_id, kind in [('functional', 'CLR-ORSD-FR', 'requirement'),
                                ('quality', 'CLR-ORSD-QR', 'requirement'),
                                ('competency-questions', 'CLR-ORSD-CQ', 'cq')]:
        nodes.update({(kind, row['id']): asset_id for row in read('requirements/' + name + '.yaml')['records']})
    future = read('requirements/future.yaml')
    nodes.update({('requirement', row['id']): 'CLR-ORSD-FUTURE' for row in future['requirements']})
    nodes.update({('cq', row['id']): 'CLR-ORSD-FUTURE' for row in future['exploratory_questions']})
    nodes.update({('artifact', asset_id): asset_id for asset_id in assets})
    raw = {row['source_id']: row for row in read('traceability/migration/input-integrity.yaml')['records']}
    nodes.update({('input', row['id']): row['id'] for row in read('traceability/migration/source-manifest.yaml')['sources']})
    bindings = {asset_id: {'ref': row['version']['source_ref'], 'sha256': row['version']['content_sha256']}
                for asset_id, row in assets.items()}
    bindings.update({source_id: {'ref': 'sha256:' + row['sha256'], 'sha256': row['sha256']}
                     for source_id, row in raw.items() if row['sha256']})
    expected = set()
    for row in models['concept']:
        expected.add(('belongs_to_domain', row['id'], row['primary_domain_id'], None))
        expected.update(('cites', row['id'], ref, None) for ref in row['source_reference_ids'])
    for row in models['association']:
        expected.add(('association_source', row['id'], row['source_id'], None))
        expected.add(('association_target', row['id'], row['target_id'], None))
    for row in models['generalization']:
        expected.add(('generalization_child', row['id'], row['child_id'], None))
        expected.add(('generalization_parent', row['id'], row['parent_id'], None))
    for row in models['constraint']:
        expected.update(('constraint_mention_candidate', row['id'], value, None) for value in row['referenced_ids'])
    expected.update(('candidate_support', source, row['concept_id'], row['support_type'])
                    for row in read('evidence/concept-support.yaml')['records'] for source in row['source_ids'])
    if (ROOT / 'traceability/requirements-model.yaml').exists():
        witnesses = read('traceability/requirements-model.yaml')
        for row in witnesses['records'] + witnesses['future_candidates']:
            for concept_id in row['candidate_concept_ids']:
                expected.add(('requirement_witness_candidate', row['requirement_id'], concept_id, None))
                expected.add(('cq_witness_candidate', row['cq_id'], concept_id, None))
    digest_to_input = {row['sha256']: source_id for source_id, row in raw.items() if row['sha256']}
    for asset_id, asset in assets.items():
        path = asset['location']
        if asset['location_kind'] == 'file' and path.endswith('.yaml'):
            data = read(path)
            origin = data.get('source_sha256') if isinstance(data, dict) else None
            if origin:
                expected.add(('derived_from_input', asset_id, digest_to_input[origin], None))
    schema = json.loads((ROOT / 'traceability/schema/trace-edge.schema.json').read_text())
    return nodes, bindings, expected, Draft202012Validator(schema)


def problems(graph, ctx, first=False):
    nodes, bindings, expected, validator = ctx
    errors = []
    for name, expected_digest in graph['input_file_sha256'].items():
        path = ROOT / name
        if path.is_absolute() and not path.is_relative_to(ROOT) or '..' in Path(name).parts:
            errors.append('unsafe_input_locator')
        elif not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected_digest:
            errors.append('stale_input:' + name)
    ids, keys, actual = set(), set(), set()
    for edge in graph['records']:
        schema_errors = list(validator.iter_errors(edge))
        if schema_errors:
            errors.append('edge_schema:' + str(edge.get('id')))
            if first:
                return errors
            continue
        if edge['id'] in ids or key(edge) in keys:
            errors.append('duplicate_edge_identity')
        ids.add(edge['id'])
        keys.add(key(edge))
        for slot in ['source', 'target']:
            endpoint = edge[slot]
            asset_id = nodes.get((endpoint['kind'], endpoint['id']))
            if asset_id is None or asset_id != endpoint['asset_id']:
                errors.append('dangling_or_wrong_owner_endpoint:' + edge['id'])
            if bindings.get(endpoint['asset_id']) != edge['version_binding'][slot]:
                errors.append('invalid_endpoint_version:' + edge['id'])
        actual.add((edge['link_type'], edge['source']['id'], edge['target']['id'], edge['qualification']))
        if errors and first:
            return errors
    retired_ids = [row['id'] for row in graph.get('retired_edges', [])]
    if len(set(retired_ids)) != len(retired_ids) or ids.intersection(retired_ids):
        errors.append('retired_identifier_reused')
    if actual != expected:
        errors.append('source_projection_mismatch')
    return errors


def check():
    graph = yaml.safe_load((ROOT / 'traceability/links.yaml').read_text())
    ctx = context()
    errors = problems(graph, ctx)
    if errors:
        raise ValueError(errors[:20])
    negatives = []
    for name, mutate in [
        ('dangling endpoint', lambda g: g['records'][0]['target'].update(id='CLR-C9999')),
        ('wrong endpoint owner', lambda g: g['records'][0]['target'].update(asset_id='CLR-SOURCE-REGISTER')),
        ('stale endpoint digest', lambda g: g['records'][0]['version_binding']['source'].update(sha256='0' * 64)),
        ('stale endpoint revision', lambda g: g['records'][0]['version_binding']['source'].update(ref='commit:' + '0' * 40)),
        ('unsupported proof type', lambda g: g['records'][0].update(link_type='proves')),
        ('duplicate edge', lambda g: g['records'].append(copy.deepcopy(g['records'][0]))),
        ('missing structural edge', lambda g: g['records'].pop(0)),
        ('inflated support qualification', lambda g: next(e for e in g['records'] if e['link_type'] == 'candidate_support').update(qualification='verified'))]:
        changed = copy.deepcopy(graph)
        mutate(changed)
        if not problems(changed, ctx, first=True):
            raise AssertionError('Negative case accepted: ' + name)
        negatives.append(name)
    reassigned, retired = bind_ids(copy.deepcopy(graph['records']), graph)
    if [(key(row), row['id']) for row in reassigned] != [(key(row), row['id']) for row in graph['records']]:
        raise AssertionError('Repeated generation changed identities')
    removed = copy.deepcopy(graph['records'][1:])
    try:
        bind_ids(removed, graph)
    except ValueError:
        negatives.append('undispositioned edge removal')
    else:
        raise AssertionError('Silent edge retirement accepted')
    return {'status': 'PASS', 'scope': 'Exact current structural/source projection and version integrity; not semantic adequacy',
            'edges': len(graph['records']), 'by_type': dict(sorted(Counter(e['link_type'] for e in graph['records']).items())),
            'negative_cases_rejected': negatives, 'stable_edge_ids': 'preserved on repeat',
            'checked_sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in
                              ['traceability/links.yaml', 'tools/build_trace_links.py', 'tools/check_generated_links.py']},
            'input_file_sha256': graph['input_file_sha256'],
            'limits': graph['limits']}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
