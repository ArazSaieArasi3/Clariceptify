"""Validate bounded BDI2020 paper-formalism claims and unavailable-source limits."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    d = yaml.safe_load((root / 'evidence/related-work/artifacts/BDI2020.yaml').read_text())
    paper = yaml.safe_load((root / d['paper']['full_review']).read_text())
    discovery = json.loads((root / d['formal_source']['discovery']).read_text())
    assert d['issue'] == discovery['issue'] == 247
    assert d['checked_on'] == discovery['checked_on']
    assert d['paper']['retained_sha256'] == paper['source']['sha256'] == discovery['paper_source_sha256']
    assert d['paper_expression']['expression_records'] == len(paper['commitments']) == 31
    selected = d['paper_expression']['selected_commitment_ids']
    assert len(selected) == len(set(selected)) == d['paper_expression']['selected_count'] == 8
    by_id = {x['id']: x for x in paper['commitments']}
    assert set(selected) <= set(by_id)
    assert all(by_id[k]['formula_page'] and by_id[k]['evidence'] and by_id[k]['transcription'] ==
               'VISUAL_EDITORIAL_TEXT_NOT_EXECUTABLE_ONTOLOGY' for k in selected)
    assert {r['id'] for r in d['checks']} == {f'Q{i:02}' for i in range(1, 9)}
    assert {k for r in d['checks'] for k in r['selected_commitment_ids']} == set(selected)
    assert all(r['locator'] and r['result'] for r in d['checks'])
    for k in ('author_repository', 'selected_root', 'version', 'sha256', 'syntax', 'license', 'declared_direct_imports'):
        assert d['formal_source'][k] is None
    for k in ('local_machine_classes', 'imported_machine_classes', 'referenced_machine_classes',
              'deprecated_machine_classes', 'inferred_machine_classes', 'source_definition_candidates',
              'missing_source_definitions', 'complete_selected_root_glossary'):
        assert d['population'][k] is None
    assert discovery['global_absence_claim'] is False and d['limits']['global_absence_claim'] is False
    assert d['formal_source']['later_FOSSR_BDI2026_is_original_source'] is False
    assert d['foundation']['family'] is None and d['foundation']['exact_edition'] is None
    assert d['decision']['accepted_equivalences'] == []
    assert d['execution']['reasoner'] == 'NOT_EXECUTED_NO_ROOT' and d['limits']['model_change'] == 'NONE'
    assert '[BDI2020 technical #247]' in (root / 'docs/research/corpus-access.md').read_text()
    return {'status': 'PASS', 'selected_paper_commitments': 8, 'machine_source': None,
            'machine_class_population': None, 'reasoner': 'NOT_EXECUTED',
            'comparison_export': [256, 126]}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
