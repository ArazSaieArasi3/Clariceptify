"""Check artifact/revision contracts; full generated-edge coverage is later work."""
from pathlib import Path
import copy
import hashlib
import json
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def load_contracts():
    schemas = {}
    for key, filename in [('artifacts', 'artifact-register.schema.json'), ('edge', 'trace-edge.schema.json')]:
        schemas[key] = json.loads((ROOT / 'traceability/schema' / filename).read_text())
        Draft202012Validator.check_schema(schemas[key])
    return schemas


def problems(register, schema, check_bytes=True):
    errors = ['schema:' + error.message for error in Draft202012Validator(schema).iter_errors(register)]
    if errors:
        return errors
    rows = register['records']
    by_id = {row['asset_id']: row for row in rows}
    if len(by_id) != len(rows):
        errors.append('duplicate_asset_id')
    for row in rows:
        if row['location_kind'] == 'file':
            path = Path(row['location'])
            if path.is_absolute() or '..' in path.parts:
                errors.append('unsafe_locator:' + row['asset_id'])
            elif not (ROOT / path).is_file():
                errors.append('missing_file:' + row['asset_id'])
            elif check_bytes and hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != row['version']['content_sha256']:
                errors.append('stale_file_binding:' + row['asset_id'])
            if row['version']['source_ref'] != register['snapshot_ref']:
                errors.append('inconsistent_snapshot_ref:' + row['asset_id'])
        if row['location_kind'] == 'collection':
            parts = [by_id.get(asset_id) for asset_id in row['component_ids']]
            if any(part is None or part['location_kind'] != 'file' for part in parts):
                errors.append('dangling_or_nonfile_component:' + row['asset_id'])
                continue
            fingerprints = {part['location']: part['version']['content_sha256'] for part in parts}
            actual = hashlib.sha256(json.dumps(fingerprints, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
            if actual != row['version']['content_sha256']:
                errors.append('collection_fingerprint_drift:' + row['asset_id'])
    for item in register['auxiliary_inputs']:
        path = ROOT / item['path']
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            errors.append('auxiliary_input_drift')
    return errors


def check():
    schemas = load_contracts()
    register = yaml.safe_load((ROOT / 'traceability/artifacts.yaml').read_text())
    errors = problems(register, schemas['artifacts'])
    if errors:
        raise ValueError(errors)
    negative_cases = []
    mutations = [
        ('duplicate asset identifier', lambda r: r['records'].append(copy.deepcopy(r['records'][0]))),
        ('missing owner', lambda r: r['records'][0].pop('owner')),
        ('stale file digest', lambda r: next(x for x in r['records'] if x['location_kind'] == 'file')['version'].update(content_sha256='0' * 64)),
        ('dangling collection member', lambda r: next(x for x in r['records'] if x['location_kind'] == 'collection')['component_ids'].append('CLR-NOT-REGISTERED')),
        ('fabricated absent-ontology digest', lambda r: next(x for x in r['records'] if x['asset_id'] == 'CLR-ONTOLOGY-FORMAL')['version'].update(content_sha256='1' * 64))]
    for name, mutate in mutations:
        changed = copy.deepcopy(register)
        mutate(changed)
        if not problems(changed, schemas['artifacts']):
            raise AssertionError('Negative case accepted: ' + name)
        negative_cases.append(name)
    rows = {row['asset_id']: row for row in register['records']}
    source = rows['CLR-MODEL-CONCEPT']['version']
    target = rows['CLR-MODEL-DOMAIN']['version']
    edge = {'id': 'CLR-TE000001', 'link_type': 'belongs_to_domain',
            'source': {'id': 'CLR-C0001', 'kind': 'concept', 'asset_id': 'CLR-MODEL-CONCEPT'},
            'target': {'id': 'CLR-D0004', 'kind': 'domain', 'asset_id': 'CLR-MODEL-DOMAIN'},
            'status': 'recorded', 'rationale': 'Schema fixture copied from the primary-domain field; not a generated coverage claim.',
            'qualification': None, 'version_binding': {'source': {'ref': source['source_ref'], 'sha256': source['content_sha256']},
                                                      'target': {'ref': target['source_ref'], 'sha256': target['content_sha256']}},
            'evidence_locators': ['model/concepts.yaml#CLR-C0001/primary_domain_id']}
    validator = Draft202012Validator(schemas['edge'])
    validator.validate(edge)
    for name, mutate in [
            ('endpoint kind mismatch', lambda e: e['target'].update(kind='concept')),
            ('missing version binding', lambda e: e['version_binding'].pop('target')),
            ('invented PASS', lambda e: e.update(status='PASS')),
            ('unsupported proves link', lambda e: e.update(link_type='proves')),
            ('unsupported satisfies link', lambda e: e.update(link_type='satisfies')),
            ('unqualified inherited support', lambda e: e.update(link_type='candidate_support', source={'id': 'CLR-SRC0018', 'kind': 'reference', 'asset_id': 'CLR-SOURCE-REGISTER'}, target={'id': 'CLR-C0001', 'kind': 'concept', 'asset_id': 'CLR-MODEL-CONCEPT'}, status='inherited_qualification'))]:
        changed = copy.deepcopy(edge)
        mutate(changed)
        if not list(validator.iter_errors(changed)):
            raise AssertionError('Negative edge accepted: ' + name)
        negative_cases.append(name)
    types = yaml.safe_load((ROOT / 'traceability/link-types.yaml').read_text())['types']
    if set(types) != set(schemas['edge']['properties']['link_type']['enum']):
        raise AssertionError('Type register/schema mismatch')
    return {'status': 'PASS', 'scope': 'Artifact snapshot integrity and initial edge-contract behavior only',
            'snapshot_ref': register['snapshot_ref'], 'artifact_records': len(rows),
            'link_types': len(types), 'positive_edge_fixtures': 1, 'negative_cases_rejected': negative_cases,
            'input_sha256': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in
                             ['traceability/artifacts.yaml', 'traceability/link-types.yaml',
                              'traceability/schema/artifact-register.schema.json', 'traceability/schema/trace-edge.schema.json']},
            'limits': ['This checker covers artifact/edge contracts; generated graph integrity is checked separately', 'Fixture is not a coverage or satisfaction result',
                       'No semantic approval, proof, CQ execution or independent review']}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
