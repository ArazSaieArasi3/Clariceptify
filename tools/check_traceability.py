"""Run public traceability gates afresh and reject incomplete/stale footprints."""
from pathlib import Path
import copy
import hashlib
import json
import yaml
import check_trace_contracts
import check_generated_links
import check_requirement_witnesses
import check_claim_register

ROOT = Path(__file__).resolve().parents[1]


def footprint_errors(graph):
    errors = []
    registry = yaml.safe_load((ROOT / 'traceability/artifacts.yaml').read_text())
    required = {'traceability/artifacts.yaml', 'traceability/link-types.yaml',
                'traceability/schema/trace-edge.schema.json', 'traceability/requirements-model.yaml'}
    required.update(row['location'] for row in registry['records']
                    if row['location_kind'] == 'file' and row['location'].endswith('.yaml'))
    if graph.get('schema_version') != '0.1.0' or graph.get('asset_id') != 'CLR-TRACE-LINKS':
        errors.append('invalid_graph_contract')
    footprint = graph.get('input_file_sha256', {})
    if not required.issubset(footprint):
        errors.append('incomplete_input_footprint')
    for name, expected in footprint.items():
        path = Path(name)
        if path.is_absolute() or '..' in path.parts or not (ROOT / path).resolve().is_relative_to(ROOT):
            errors.append('unsafe_input_locator')
            continue
        if not (ROOT / path).is_file() or hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
            errors.append('stale_input:' + name)
    return errors


def check():
    graph = yaml.safe_load((ROOT / 'traceability/links.yaml').read_text())
    errors = footprint_errors(graph)
    if errors:
        raise ValueError(errors)
    # Stored PASS is never the gate: execute the validators against current bytes.
    layers = {'artifact_contracts': check_trace_contracts.check(),
              'generated_links': check_generated_links.check(),
              'requirement_witnesses': check_requirement_witnesses.check(),
              'claim_register': check_claim_register.check()}
    negatives = []
    for name, mutate, expected in [
            ('removed model fingerprint', lambda g: g['input_file_sha256'].pop('model/concepts.yaml'), 'incomplete_input_footprint'),
            ('removed witness fingerprint', lambda g: g['input_file_sha256'].pop('traceability/requirements-model.yaml'), 'incomplete_input_footprint'),
            ('forged source fingerprint', lambda g: g['input_file_sha256'].update({'model/concepts.yaml': '0' * 64}), 'stale_input:model/concepts.yaml'),
            ('escaping input locator', lambda g: g['input_file_sha256'].update({'../outside.yaml': '0' * 64}), 'unsafe_input_locator'),
            ('wrong graph contract', lambda g: g.update(asset_id='CLR-OTHER'), 'invalid_graph_contract')]:
        changed = copy.deepcopy(graph)
        mutate(changed)
        if expected not in footprint_errors(changed):
            raise AssertionError('Traceability boundary not rejected: ' + name)
        negatives.append(name)
    code_paths = ['tools/' + name + '.py' for name in ['check_traceability', 'check_trace_contracts',
                  'check_generated_links', 'check_requirement_witnesses', 'check_claim_register']]
    return {'status': 'PASS', 'scope': 'Current artifact/link/witness/claim integrity; not semantic validation',
            'edges': layers['generated_links']['edges'], 'layers': layers,
            'negative_input_cases_rejected': negatives,
            'input_file_sha256': graph['input_file_sha256'],
            'validator_file_sha256': {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in code_paths},
            'limits': ['Layer results retain their own scope and denominators.',
                       'No link-count quality score, inherited PASS, requirement satisfaction, proof or independent approval.']}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
