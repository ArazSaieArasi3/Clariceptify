"""Validate synthesis population, model bindings and candidate/unknown boundaries."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return yaml.safe_load((ROOT / path).read_text())


def check():
    d = read('docs/research/gap-comparison.yaml')
    assert d['issue'] == 126 and d['status'].startswith('BOUNDED_FINAL_RELATED_WORK_SYNTHESIS')
    m = d['baseline']
    assert hashlib.sha256((ROOT / m['model_path']).read_bytes()).hexdigest() == m['model_sha256']
    model = read(m['model_path'])['records']
    model_ids = {x['id'] for x in model}
    domains = read('model/domains.yaml')['records']
    domain_ids = {x['id'] for x in domains}
    assert len(model) == m['selected_concepts'] == 137
    assert len(domains) == m['subject_domains'] + m['foundations_domain'] == 21
    assert m['principal_cqs'] == 30
    batches = [read(p) for p in d['inputs']['comparison_paths']]
    assert len(batches) == 6 and {b['issue'] for b in batches} == set(range(251, 257))
    assert sum(len(b['matrix']) for b in batches) == d['inputs']['comparison_cells'] == 76
    works = [w for b in batches for w in b['scope']['works']]
    assert len(works) == len(set(works)) == d['inputs']['comparison_source_labels'] == 19
    cell_ids = {x['id'] for b in batches for x in b['matrix']}
    assert len(cell_ids) == 76
    audit = read(d['inputs']['source_audit'])
    assert len(audit['records']) == d['inputs']['source_audit_records'] == 23
    assert audit['population']['paper_or_version_records'] == 19
    assert audit['population']['separate_document_sources'] == d['inputs']['standalone_document_sources'] == 4
    assert d['inputs']['full_paper_dossiers'] == 18 and d['inputs']['limited_summary_dossiers'] == 1
    gaps = d['gap_table']
    assert [x['id'] for x in gaps] == [f'G{i:02}' for i in range(1, 6)]
    assert all(set(x['existing_model_ids']) <= model_ids and set(x['current_domains']) <= domain_ids for x in gaps)
    assert all(x['source_cells'] and set(x['source_cells']) <= cell_ids for x in gaps)
    assert all(x['contrary_evidence'] and x['test'] and x['decision'] == 'OWNER_DECISION_REQUIRED'
               and x['model_defect_state'].startswith('UNASSESSED') for x in gaps)
    assert len(d['candidate_use_register']) == 6
    assert all(x['status'] == 'OWNER_DECISION_REQUIRED' and x['prerequisites'] and x['cost_risk']
               for x in d['candidate_use_register'])
    assert d['domain_review']['proposed_new_domain'] is None
    queue = d['unmodeled_concept_register']
    assert queue['current_selected'] == 137
    pending = queue['support_pending_within_selected']
    actual_p = {x['concept_id'] for x in read('evidence/concept-support.yaml')['records'] if x['support_type'] == 'P'}
    assert len(actual_p) == pending['count'] == 10 and set(pending['ids']) == actual_p
    ledger = read(queue['historical_unselected']['path'])['unselected_origin_records']
    assert len(ledger) == queue['historical_unselected']['count'] == 260
    assert sum(x['source_family'] == 'inventory' for x in ledger) == queue['historical_unselected']['inventory_ids'] == 254
    assert sum(x['source_family'] == 'thesis-core' for x in ledger) == queue['historical_unselected']['thesis_core_ids'] == 6
    assert all(x['disposition'] == 'not_selected_for_this_slice_no_deletion' for x in ledger)
    assert queue['historical_unselected']['unique_new_concept_count'] is None
    assert d['limits']['no_universal_novelty_claim'] and d['limits']['no_accepted_equivalences']
    assert d['limits']['no_model_change'] and d['limits']['no_release_decision']
    assert d['limits']['unresolved_source_followups'] == [91, 246]
    for path in ('README.md', 'docs/research/corpus-access.md'):
        assert 'gap-comparison.md' in (ROOT / path).read_text()
    return {'status': 'PASS', 'batches': 6, 'source_labels': 19, 'cells': 76,
            'gaps': 5, 'audit_records': 23, 'historical_unselected_ids': 260,
            'in_model_pending_support': 10, 'accepted_equivalences': 0}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
