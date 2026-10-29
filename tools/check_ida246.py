"""Validate the I&DA bounded-discovery dossier without claiming formal-source coverage."""
from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    dossier = yaml.safe_load((root / 'evidence/related-work/artifacts/IDA.yaml').read_text())
    receipt = json.loads((root / dossier['source']['discovery']).read_text())
    summary = yaml.safe_load((root / dossier['work']['prior_summary_receipt']).read_text())
    assert dossier['issue'] == receipt['issue'] == 246
    assert dossier['checked_on'] == receipt['checked_on']
    assert len(dossier['checks']) == 8
    assert len({r['id'] for r in dossier['checks']}) == 8
    assert {r['id'] for r in dossier['checks']} == {f'T{i:02}' for i in range(1, 9)}
    assert receipt['global_absence_claim'] is False
    assert receipt['original_paper_sha256'] is None
    assert receipt['selected_source_sha256'] is None
    assert receipt['selected_source_file'] is None
    assert receipt['original_executable_class_inventory'] is None
    assert all(dossier['source'][k] is None for k in ('module', 'release_version', 'repository', 'file_sha256', 'syntax', 'license', 'direct_imports'))
    for key in ('local_named_classes', 'externally_redeclared_classes', 'imported_classes',
                'referenced_undeclared_classes', 'inferred_classes', 'local_properties'):
        assert dossier['population'][key] is None
    claims = {r['id'] for r in summary['claims']}
    for row in dossier['checks']:
        assert row['summary_claims'] and set(row['summary_claims']) <= claims
        assert row['paper_locator'].startswith('indexed original section')
        assert row['formal_iri'] is None and row['exact_formula_locator'] is None
        assert row['result']
    assert dossier['foundation']['edition'] is None and dossier['foundation']['actual_import'] is None
    assert dossier['decision']['accepted_equivalences'] == []
    assert dossier['limits']['reasoner'] == 'NOT_EXECUTED'
    assert dossier['limits']['model_change'] == 'NONE'
    assert dossier['acceptance']['ac2'].startswith('OPEN_')
    assert dossier['acceptance']['issue_closure'] == 'OPEN'
    index = (root / 'docs/research/corpus-access.md').read_text()
    assert 'evidence/related-work/artifacts/IDA.yaml' in index
    assert '[I&DA technical #246]' in index
    return {'status': 'PASS', 'selected_checks': 8,
            'formal_module': None, 'machine_class_population': None,
            'ac2': dossier['acceptance']['ac2'], 'issue_closure': 'OPEN'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
