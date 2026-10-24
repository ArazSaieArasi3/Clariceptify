"""Preserve frozen ORSD candidate witnesses; do not assess satisfaction."""
from pathlib import Path
import argparse
import hashlib
import json
import yaml
from docx import Document

ROOT = Path(__file__).resolve().parents[1]
QUALITY_PLANS = {
    'QR-01': ('Review scope fidelity and the purpose of each named domain; class counts alone are not adequacy.', [2, 92, 111]),
    'QR-02': ('Use extraction parity as partial evidence; reconcile the diagram separately before judging the complete contract.', [33, 43, 45]),
    'QR-03': ('Review identity, rigidity, modes, qualities and higher-order typing with sources and counterexamples.', [120, 121, 122]),
    'QR-04': ('Separate graph connectivity from meaningful paths and scoped domain adequacy.', [37, 92, 111]),
    'QR-05': ('Review all 24 textual constraints and cross-relation interactions; lexical mentions are only candidates.', [51, 119, 143]),
    'QR-06': ('Review definition provenance and exact passage support; inherited citations do not establish full-text or typing approval.', [112, 113]),
    'QR-07': ('Check requirement/CQ witness contracts, stable IDs, lineage and version-bound links without inferring satisfaction.', [34, 38]),
    'QR-08': ('Execute positive, missing-link and misleading-link cases under exact answer contracts; none is executed here.', [123, 124, 125, 147, 148]),
    'QR-09': ('Reconcile complete and detail diagrams, domain colors, semantics and readability against the exact model.', [41, 42, 43, 44, 45]),
    'QR-10': ('Keep claim, machine-check, CQ and human-review layers distinct; no minimum domain class quota.', [35, 51, 127, 128])}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()


def generate(path):
    path = Path(path)
    source_digest = hashlib.sha256(path.read_bytes()).hexdigest()
    def read(name):
        return yaml.safe_load((ROOT / name).read_text())
    fr = {row['id']: row for row in read('requirements/functional.yaml')['records']}
    cq = {row['id']: row for row in read('requirements/competency-questions.yaml')['records']}
    qr = read('requirements/quality.yaml')['records']
    future = read('requirements/future.yaml')
    if source_digest != read('requirements/functional.yaml')['source_sha256']:
        raise ValueError('ORSD digest mismatch; no witness output written')
    concepts = {row['label_en']: row for row in read('model/concepts.yaml')['records']}
    domains = {row['label_en']: row for row in read('model/domains.yaml')['records']}

    def witnesses(text):
        labels = [value.strip() for value in text.split(';') if value.strip()]
        return {'input_witness_labels': labels,
                'candidate_concept_ids': [concepts[label]['id'] for label in labels if label in concepts],
                'unresolved_witness_labels': [label for label in labels if label not in concepts]}

    records = []
    doc = Document(path)
    for number, row in enumerate(doc.tables[5].rows[1:], 1):
        cells = [cell.text for cell in row.cells]
        need_id, cq_id = cells[0].split('\n')
        if need_id not in fr or cq_id not in cq or cq[cq_id]['requirement_id'] != need_id:
            raise ValueError('Unknown or mismatched witness contract')
        values = witnesses(cells[1])
        declared_labels = [value.strip() for value in cells[2].split(';') if value.strip()]
        declared_ids = [domains[label]['id'] for label in declared_labels if label in domains]
        observed_ids = sorted({concepts[label]['primary_domain_id'] for label in values['input_witness_labels'] if label in concepts})
        records.append({'requirement_id': need_id, 'cq_id': cq_id, **values,
                        'input_domain_labels': declared_labels, 'declared_domain_ids': declared_ids,
                        'unresolved_domain_labels': [label for label in declared_labels if label not in domains],
                        'observed_primary_domain_ids': observed_ids,
                        'domain_list_comparison': 'same_set' if set(declared_ids) == set(observed_ids) else 'difference_requires_review',
                        'requirement_contract_sha256': fingerprint(fr[need_id]), 'cq_contract_sha256': fingerprint(cq[cq_id]),
                        'source_locator': f'SRC-ORSD@sha256:{source_digest}#table-6/data-row-{number}',
                        'source_cells': cells, 'witness_assessment': 'not_assessed',
                        'satisfaction_status': 'not_assessed', 'test_execution': 'not_executed', 'answer_status': 'not_computed'})
    if {row['requirement_id'] for row in records} != set(fr) or {row['cq_id'] for row in records} != set(cq):
        raise ValueError('Frozen witness table does not cover the declared FR/CQ records')
    quality = [{'requirement_id': row['id'], 'requirement_contract_sha256': fingerprint(row),
                'review_plan': QUALITY_PLANS[row['id']][0], 'planned_issue_numbers': QUALITY_PLANS[row['id']][1],
                'satisfaction_status': 'not_assessed', 'test_execution': 'not_executed',
                'disposition': 'Review plan only; linked artifacts or completed subchecks do not satisfy the whole quality contract.'}
               for row in qr]
    needs = {row['id']: row for row in future['requirements']}
    later = [{'requirement_id': row['requirement_id'], 'cq_id': row['id'],
              **witnesses(row['candidate_existing_witnesses']), 'input_witness_text': row['candidate_existing_witnesses'],
              'requirement_contract_sha256': fingerprint(needs[row['requirement_id']]), 'cq_contract_sha256': fingerprint(row),
              'source_locator': row['source_locator'], 'release_target': row['release_target'], 'blocks_r1': False,
              'witness_assessment': 'not_assessed', 'satisfaction_status': 'not_assessed',
              'test_execution': 'not_executed', 'answer_status': 'not_computed'} for row in future['exploratory_questions']]
    paths = ['requirements/functional.yaml', 'requirements/quality.yaml', 'requirements/competency-questions.yaml',
             'requirements/future.yaml', 'model/concepts.yaml', 'model/domains.yaml']
    return {'schema_version': '0.1.0', 'asset_id': 'CLR-TRACE-REQUIREMENT-WITNESSES',
            'source_id': 'SRC-ORSD', 'source_sha256': source_digest, 'source_witness_table': 6,
            'status': 'imported_candidates_not_assessed',
            'input_file_sha256': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in paths},
            'records': records, 'quality_dispositions': quality, 'future_candidates': later,
            'limits': ['Witnesses are exact-label resolutions of the frozen ORSD proposals; no new adequacy judgment.',
                       'No class-presence, edge-count or citation proxy establishes requirement satisfaction.',
                       'Domain-list differences and unresolved labels remain visible; they are not silently corrected.',
                       'Future candidates remain R2 proposals and do not automatically block R1.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('orsd_docx')
    parser.add_argument('--output', default=str(ROOT / 'traceability/requirements-model.yaml'))
    args = parser.parse_args()
    result = generate(args.orsd_docx)
    Path(args.output).write_text(yaml.safe_dump(result, sort_keys=False, allow_unicode=True))
    print(json.dumps({'status': 'PASS', 'fr_cq_pairs': len(result['records']), 'quality_dispositions': len(result['quality_dispositions']),
                      'future_pairs': len(result['future_candidates']),
                      'unresolved_labels': sum(len(row['unresolved_witness_labels']) for row in result['records'] + result['future_candidates']),
                      'domain_list_differences': sum(row['domain_list_comparison'] != 'same_set' for row in result['records'])}))
