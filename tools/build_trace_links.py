"""Generate input-bound project links without changing model semantics."""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def key(edge):
    return (edge['link_type'], edge['source']['asset_id'], edge['source']['id'],
            edge['target']['asset_id'], edge['target']['id'])


def bind_ids(records, previous=None, retirement_reason=None):
    previous = previous or {'records': [], 'retired_edges': []}
    old = {key(row): row['id'] for row in previous['records']}
    retired = copy.deepcopy(previous.get('retired_edges', []))
    retired_keys = {tuple(row['key']) for row in retired}
    if len(old) != len(previous['records']) or len({key(row) for row in records}) != len(records):
        raise ValueError('Duplicate trace identity key')
    all_ids = [row['id'] for row in previous['records']] + [row['id'] for row in retired]
    if len(set(all_ids)) != len(all_ids) or any(not re.fullmatch(r'CLR-TE\d{6}', value) for value in all_ids):
        raise ValueError('Invalid or reused edge identifier')
    next_id = max([int(value[6:]) for value in all_ids] or [0]) + 1
    current_keys = {key(row) for row in records}
    removed = set(old) - current_keys
    if removed and not retirement_reason:
        raise ValueError('Removing existing links requires an explicit retirement reason')
    for identity in sorted(removed):
        retired.append({'id': old[identity], 'key': list(identity), 'reason': retirement_reason})
    for row in sorted(records, key=key):
        identity = key(row)
        if identity in retired_keys:
            raise ValueError('Reactivating a retired key requires a separate lineage decision')
        if identity in old:
            row['id'] = old[identity]
        else:
            if next_id > 999999:
                raise ValueError('Edge identifier capacity exceeded')
            row['id'] = f'CLR-TE{next_id:06d}'
            next_id += 1
    return sorted(records, key=lambda row: row['id']), sorted(retired, key=lambda row: row['id'])


def generate(previous=None, retirement_reason=None):
    inputs = {}

    def read(path):
        inputs[path] = digest(ROOT / path)
        return yaml.safe_load((ROOT / path).read_text())

    register = read('traceability/artifacts.yaml')
    assets = {row['asset_id']: row for row in register['records']}
    types = read('traceability/link-types.yaml')['types']
    read('traceability/schema/trace-edge.schema.json')
    sources = read('traceability/migration/source-manifest.yaml')['sources']
    integrity = {row['source_id']: row for row in read('traceability/migration/input-integrity.yaml')['records']}
    input_ids = {row['id'] for row in sources}
    raw_refs = {row['source_id']: {'ref': 'sha256:' + row['sha256'], 'sha256': row['sha256']}
                for row in integrity.values() if row['sha256']}
    model = {name: read('model/' + name + '.yaml')['records'] for name in
             ['concepts', 'domains', 'relations', 'generalizations', 'constraints']}
    support = read('evidence/concept-support.yaml')['records']
    read('evidence/source-register.yaml')
    records = []

    def binding(asset_id):
        if asset_id in raw_refs:
            return raw_refs[asset_id]
        asset = assets[asset_id]
        if asset['location_kind'] != 'file':
            raise ValueError('A materialized file binding is required: ' + asset_id)
        location = asset['location']
        actual = digest(ROOT / location)
        if actual != asset['version']['content_sha256']:
            raise ValueError('Refresh stale artifact revision before generating links: ' + asset_id)
        inputs[location] = actual
        return {'ref': asset['version']['source_ref'], 'sha256': actual}

    def add(link_type, source_id, target_id, source_asset, target_asset, locator, qualification=None):
        rule = types[link_type]
        records.append({'link_type': link_type,
                        'source': {'id': source_id, 'kind': rule['source_kind'], 'asset_id': source_asset},
                        'target': {'id': target_id, 'kind': rule['target_kind'], 'asset_id': target_asset},
                        'status': rule['status'], 'rationale': rule['meaning'], 'qualification': qualification,
                        'version_binding': {'source': binding(source_asset), 'target': binding(target_asset)},
                        'evidence_locators': [locator]})

    for row in model['concepts']:
        add('belongs_to_domain', row['id'], row['primary_domain_id'], 'CLR-MODEL-CONCEPT', 'CLR-MODEL-DOMAIN',
            'model/concepts.yaml#' + row['id'] + '/primary_domain_id')
        for reference in row['source_reference_ids']:
            add('cites', row['id'], reference, 'CLR-MODEL-CONCEPT', 'CLR-SOURCE-REGISTER',
                'model/concepts.yaml#' + row['id'] + '/source_reference_ids')
    for row in model['relations']:
        for end in ['source', 'target']:
            add('association_' + end, row['id'], row[end + '_id'], 'CLR-MODEL-RELATION', 'CLR-MODEL-CONCEPT',
                'model/relations.yaml#' + row['id'] + '/' + end + '_id')
    for row in model['generalizations']:
        for end in ['child', 'parent']:
            add('generalization_' + end, row['id'], row[end + '_id'], 'CLR-MODEL-GENERALIZATION', 'CLR-MODEL-CONCEPT',
                'model/generalizations.yaml#' + row['id'] + '/' + end + '_id')
    for row in model['constraints']:
        for concept in row['referenced_ids']:
            add('constraint_mention_candidate', row['id'], concept, 'CLR-MODEL-CONSTRAINT', 'CLR-MODEL-CONCEPT',
                'model/constraints.yaml#' + row['id'] + '/referenced_ids')
    for row in support:
        for reference in row['source_ids']:
            add('candidate_support', reference, row['concept_id'], 'CLR-SOURCE-REGISTER', 'CLR-MODEL-CONCEPT',
                'evidence/concept-support.yaml#' + row['concept_id'], row['support_type'])
    digest_to_input = {row['sha256']: source_id for source_id, row in integrity.items() if row['sha256']}
    for asset in sorted(assets.values(), key=lambda row: row['asset_id']):
        path = asset['location']
        if asset['location_kind'] != 'file' or not path.endswith('.yaml'):
            continue
        data = read(path)
        origin = data.get('source_sha256') if isinstance(data, dict) else None
        if origin:
            input_id = digest_to_input.get(origin)
            if input_id not in input_ids:
                raise ValueError('Unknown declared source digest: ' + path)
            add('derived_from_input', asset['asset_id'], input_id, asset['asset_id'], input_id,
                path + '#source_sha256')
    records, retired = bind_ids(records, previous, retirement_reason)
    return {'schema_version': '0.1.0', 'asset_id': 'CLR-TRACE-LINKS',
            'scope': 'Generated project links for the current structural/source baseline; not a complete research graph.',
            'identity_policy': 'Stable allocated edge IDs; existing keys retain IDs; removals require recorded disposition; retired IDs are not reused.',
            'input_file_sha256': dict(sorted(inputs.items())), 'records': records, 'retired_edges': retired,
            'limits': ['No requirement/CQ witness links yet; those are separate work.',
                       'Constraint mentions remain lexical candidates, not adjudicated coverage.',
                       'D/B/P support is inherited; full-text and typing approval remain unassessed.',
                       'No proves/satisfies links, human acceptance, source ownership transfer or semantic completeness claim.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=str(ROOT / 'traceability/links.yaml'))
    parser.add_argument('--retire-reason')
    args = parser.parse_args()
    path = Path(args.output)
    previous = yaml.safe_load(path.read_text()) if path.exists() else None
    graph = generate(previous, args.retire_reason)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(graph, sort_keys=False, allow_unicode=True, width=110))
    from collections import Counter
    print(json.dumps({'status': 'PASS', 'edges': len(graph['records']),
                      'by_type': dict(Counter(row['link_type'] for row in graph['records']))}, indent=2))
