"""Check candidate witness transfer and contracts, never satisfaction."""
from pathlib import Path
import copy
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()


def problems(mapping):
    def read(path):
        return yaml.safe_load((ROOT / path).read_text())
    errors = []
    for path, expected in mapping['input_file_sha256'].items():
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
            errors.append('stale_witness_input')
    fr = {row['id']: row for row in read('requirements/functional.yaml')['records']}
    cq = {row['id']: row for row in read('requirements/competency-questions.yaml')['records']}
    quality = {row['id']: row for row in read('requirements/quality.yaml')['records']}
    future = read('requirements/future.yaml')
    lr = {row['id']: row for row in future['requirements']}
    lcq = {row['id']: row for row in future['exploratory_questions']}
    labels = {row['label_en']: row['id'] for row in read('model/concepts.yaml')['records']}
    rows = mapping['records']
    if len(rows) != len(fr) or {row['requirement_id'] for row in rows} != set(fr) or {row['cq_id'] for row in rows} != set(cq):
        errors.append('missing_or_duplicate_fr_cq_contract')
    later = mapping['future_candidates']
    if len(later) != len(lcq) or {row['cq_id'] for row in later} != set(lcq):
        errors.append('missing_or_duplicate_future_contract')
    for row in rows + later:
        is_later = row in later
        needs, questions = (lr, lcq) if is_later else (fr, cq)
        need, question = needs.get(row['requirement_id']), questions.get(row['cq_id'])
        if not need or not question or question['requirement_id'] != row['requirement_id']:
            errors.append('unknown_or_mismatched_need_cq')
            continue
        if row['requirement_contract_sha256'] != fingerprint(need) or row['cq_contract_sha256'] != fingerprint(question):
            errors.append('candidate_contract_drift')
        source_text = question['candidate_existing_witnesses'] if is_later else row['source_cells'][1]
        expected_labels = [value.strip() for value in source_text.split(';') if value.strip()]
        expected_ids = [labels[label] for label in expected_labels if label in labels]
        expected_unresolved = [label for label in expected_labels if label not in labels]
        if row['input_witness_labels'] != expected_labels or row['candidate_concept_ids'] != expected_ids or row['unresolved_witness_labels'] != expected_unresolved:
            errors.append('witness_resolution_drift')
        if any(row[field] != value for field, value in [('witness_assessment', 'not_assessed'),
                ('satisfaction_status', 'not_assessed'), ('test_execution', 'not_executed'), ('answer_status', 'not_computed')]):
            errors.append('unsupported_witness_result')
        if is_later and row['blocks_r1'] is not False:
            errors.append('future_scope_inflation')
        if not is_later and row['source_cells'][0] != row['requirement_id'] + '\n' + row['cq_id']:
            errors.append('source_pair_drift')
    dispositions = mapping['quality_dispositions']
    if len(dispositions) != len(quality) or {row['requirement_id'] for row in dispositions} != set(quality):
        errors.append('missing_or_duplicate_quality_disposition')
    for row in dispositions:
        need = quality.get(row['requirement_id'])
        if not need or row['requirement_contract_sha256'] != fingerprint(need):
            errors.append('quality_contract_drift')
        if row['satisfaction_status'] != 'not_assessed' or row['test_execution'] != 'not_executed':
            errors.append('unsupported_quality_result')
    if mapping['source_sha256'] != read('requirements/functional.yaml')['source_sha256']:
        errors.append('wrong_source_revision')
    return errors


def check():
    path = ROOT / 'traceability/requirements-model.yaml'
    mapping = yaml.safe_load(path.read_text())
    errors = problems(mapping)
    if errors:
        raise ValueError(errors)
    rejected = []
    for name, mutate in [
        ('unknown requirement', lambda m: m['records'][0].update(requirement_id='FR-99')),
        ('mismatched CQ', lambda m: m['records'][0].update(cq_id='CQ-30')),
        ('dangling witness', lambda m: m['records'][0]['candidate_concept_ids'].append('CLR-C9999')),
        ('narrowed witness set', lambda m: m['records'][0]['candidate_concept_ids'].pop()),
        ('fabricated satisfaction', lambda m: m['records'][0].update(satisfaction_status='satisfied')),
        ('fabricated answer', lambda m: m['records'][0].update(answer_status='computed')),
        ('fabricated QR PASS', lambda m: m['quality_dispositions'][0].update(satisfaction_status='PASS')),
        ('future R1 blocker inflation', lambda m: m['future_candidates'][0].update(blocks_r1=True))]:
        changed = copy.deepcopy(mapping)
        mutate(changed)
        if not problems(changed):
            raise AssertionError('Negative candidate accepted: ' + name)
        rejected.append(name)
    return {'status': 'PASS', 'scope': 'Frozen ORSD candidate witness/contract integrity only',
            'fr_cq_pairs': len(mapping['records']), 'quality_dispositions': len(mapping['quality_dispositions']),
            'future_pairs': len(mapping['future_candidates']),
            'unresolved_witness_labels': sum(len(row['unresolved_witness_labels']) for row in mapping['records'] + mapping['future_candidates']),
            'negative_cases_rejected': rejected, 'checked_mapping_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'satisfaction': 'not_assessed', 'cq_execution': 'not_executed', 'answers': 'not_computed'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
