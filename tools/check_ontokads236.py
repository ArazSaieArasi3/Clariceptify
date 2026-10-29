"""Validate bounded negative OntoKADS artifact evidence, without claiming execution."""
from pathlib import Path
import hashlib
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]


def run(root=ROOT):
    d = yaml.safe_load((root / 'evidence/related-work/artifacts/OntoKADS.yaml').read_text())
    paper = yaml.safe_load((root / d['source']['dossier']).read_text())
    receipt = json.loads((root / d['source']['discovery_receipt']).read_text())
    assert d['issue'] == receipt['issue'] == 236 and paper['work_id'] == d['source']['work']
    assert paper['source']['sha256'] == receipt['retained_paper_sha256'] == d['source']['paper_sha256']
    assert hashlib.sha256((root / d['source']['dossier']).read_bytes()).hexdigest() == d['source']['dossier_sha256']
    assert d['population']['paper_catalog_records'] == len(paper['catalog']) == 72
    assert d['population']['paper_labeled_commitments'] == sum(bool(re.fullmatch(r'[ADT]\d+', c['label'])) for c in paper['commitments']) == 22
    assert len(paper['commitments']) == 31 and len(d['commitments']) == d['population']['selected_paper_commitments'] == 8
    ids = {x['id']: x for x in paper['commitments']}
    evidence = {e['id'] for e in paper['evidence']}
    assert len({x['id'] for x in d['commitments']}) == 8
    for c in d['commitments']:
        assert c['id'] in ids and c['formula'] == ids[c['id']]['label']
        assert c['locator'].split(':')[1].split()[0] in evidence
        assert c['locator'].split(':')[1].split()[0] in ids[c['id']]['evidence']
        assert c['observation']
    assert not receipt['author_controlled_machine_root_identified'] and not receipt['global_absence_claim']
    assert {c['id'] for c in receipt['checks']} == {'P01', 'W01', 'G01', 'G02', 'N01', 'C01'}
    assert receipt['checks'][2]['reported_total_count'] == 0
    assert receipt['checks'][3]['reported_total_count'] == 46
    assert not d['source']['universal_absence_claim']
    for field in ('formal_root', 'root_version', 'root_sha256', 'license_for_formal_root', 'formal_syntax', 'declared_imports', 'unresolved_imports'):
        assert d['source'][field] is None
    for field in ('local_machine_classes', 'imported_machine_classes', 'referenced_machine_classes', 'deprecated_machine_classes', 'inferred_machine_classes', 'named_machine_properties'):
        assert d['population'][field] is None
    assert d['foundation']['family'] == 'DOLCE' and d['foundation']['edition'] is None
    assert d['foundation']['actual_formal_import'] is None
    assert all(v.startswith('NOT_EXECUTED') for k, v in d['execution'].items() if k in ('parser', 'reasoner', 'formula_solver', 'validation'))
    model = yaml.safe_load((root / 'model/concepts.yaml').read_text())
    model_ids = {x['id'] for x in model['records']}
    assert set(d['decision']['candidate_model_ids']) <= model_ids
    assert d['decision']['model_use'] == 'OWNER_DECISION_REQUIRED' and d['decision']['accepted_equivalences'] == []
    assert d['boundary']['model_change'] == 'NONE' and d['boundary']['release_change'] == 'NONE'
    assert d['boundary']['later_issues'] == [252, 126]
    audit = yaml.safe_load((root / 'evidence/related-work/deep-reviews/source-audit.yaml').read_text())
    row = next(x for x in audit['records'] if x['id'] == 'OntoKADS2005')
    assert 'ONTOKADS236-S01' in row['repository']['evidence']
    assert row['technical_followup']['evidence'] == 'evidence/related-work/artifacts/OntoKADS.yaml'
    assert row['class_coverage']['local_classes'] is None and row['class_coverage']['reasoner_execution'] == 'NOT_EXECUTED'
    assert row['next_issues'] == [252, 126]
    assert 'OntoKADS followup #236' in (root / 'evidence/related-work/deep-reviews/README.md').read_text()
    print(json.dumps({'status': 'PASS', 'selected_paper_commitments': 8, 'formal_root': None, 'machine_classes': None}, sort_keys=True))


if __name__ == '__main__':
    run()
