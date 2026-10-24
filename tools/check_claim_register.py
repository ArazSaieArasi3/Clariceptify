"""Validate bounded claim bindings; not peer review or novelty assessment."""
from pathlib import Path
import copy
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def problems(register):
    errors = []
    for path, expected in register['input_file_sha256'].items():
        if not (ROOT / path).is_file() or hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
            errors.append('stale_claim_input:' + path)
    claims = register['claims']
    if len({row['id'] for row in claims}) != len(claims):
        errors.append('duplicate_claim_id')
    for row in claims:
        if not row['text'] or not row['boundary'] or not row['evidence_paths']:
            errors.append('unbounded_or_unsupported_claim')
        if any(path not in register['input_file_sha256'] for path in row['evidence_paths']):
            errors.append('unbound_claim_evidence')
        expected_status = 'supported_within_scope' if row['claim_class'] == 'recorded_observation' else 'proposed_for_review'
        if row['status'] != expected_status:
            errors.append('claim_status_inflation')
    by_id = {row['id']: row for row in claims}
    mapping = yaml.safe_load((ROOT / 'evaluation/requirement-witnesses.json').read_text())
    fact = by_id['CLR-CL003']['facts']
    if any(fact[key] != mapping[key] for key in ['fr_cq_pairs', 'quality_dispositions', 'future_pairs', 'satisfaction', 'cq_execution', 'answers']):
        errors.append('requirement_claim_drift')
    graph = json.loads((ROOT / 'evaluation/generated-links.json').read_text())
    if by_id['CLR-CL002']['facts']['edges'] != graph['edges']:
        errors.append('graph_claim_drift')
    article = register['manuscript_binding']
    if article['model_evidence_alignment'] != 'not_assessed' or article['current_public_manuscript'] != 'not_materialized' or article['doi'] is not None:
        errors.append('unsupported_manuscript_or_doi_claim')
    return errors


def check():
    path = ROOT / 'docs/research/claim-register.yaml'
    register = yaml.safe_load(path.read_text())
    errors = problems(register)
    if errors:
        raise ValueError(errors)
    negatives = []
    for name, mutate in [
        ('duplicate claim identifier', lambda r: r['claims'].append(copy.deepcopy(r['claims'][0]))),
        ('unbound evidence', lambda r: r['claims'][0]['evidence_paths'].append('evaluation/not-present.json')),
        ('missing claim boundary', lambda r: r['claims'][0].update(boundary='')),
        ('novelty/contribution inflation', lambda r: r['claims'][-1].update(status='supported_within_scope')),
        ('fabricated requirement satisfaction', lambda r: r['claims'][2]['facts'].update(satisfaction='satisfied')),
        ('stale evidence fingerprint', lambda r: r['input_file_sha256'].update({'model/concepts.yaml': '0' * 64})),
        ('fabricated manuscript alignment', lambda r: r['manuscript_binding'].update(model_evidence_alignment='approved')),
        ('unissued DOI', lambda r: r['manuscript_binding'].update(doi='unissued-placeholder'))]:
        changed = copy.deepcopy(register)
        mutate(changed)
        if not problems(changed):
            raise AssertionError('Negative claim accepted: ' + name)
        negatives.append(name)
    return {'status': 'PASS', 'scope': 'Claim-register identity, input and state boundaries; not scientific peer review',
            'claims': len(register['claims']), 'negative_cases_rejected': negatives,
            'register_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'input_snapshot_ref': register['input_snapshot_ref'],
            'manuscript_alignment': 'not_assessed', 'novelty_review': 'pending'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
