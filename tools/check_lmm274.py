"""Check the exact LMM followup evidence contract without retrieving third-party files."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def run(root=ROOT):
    d = yaml.safe_load((root / 'evidence/related-work/artifacts/LMM-correspondence.yaml').read_text())
    receipt = json.loads((root / d['execution']['receipt']).read_text())
    discovery = json.loads((root / d['source']['discovery']['current']).read_text())
    manifest = yaml.safe_load((root / d['source']['manifest']).read_text())
    paper = yaml.safe_load((root / d['source']['paper']['dossier']).read_text())
    catalog = yaml.safe_load((root / d['source']['local_classes']['catalog']).read_text())
    assert d['issue'] == receipt['issue'] == 274
    assert paper['source']['sha256'] == d['source']['paper']['sha256']
    assert {x['id']: x['sha256'] for x in manifest['artifacts']} == receipt['source_sha256']
    assert {x['id']: x['sha256'] for x in manifest['artifacts']} == {k: v['sha256'] for k, v in d['source']['modules'].items()}
    assert receipt['generator_sha256'] == hashlib.sha256((root / receipt['generator']).read_bytes()).hexdigest()
    assert len(receipt['loaded_imports']) == 4
    assert receipt['owl2_dl_profile_pass'] is True and receipt['profile_violations'] == []
    assert receipt['baseline_consistent'] is True and receipt['unsatisfiable_named_classes'] == []
    assert receipt['summary'] == {'total': 13, 'passed': 13, 'failed': 0, 'errors': 0}
    tests = {x['id']: x for x in receipt['tests']}
    assert len(tests) == 13
    for row in tests.values():
        assert row['result'] == 'PASS' and row['observed_consistent'] is row['expected_consistent']
        assert row['fixture_sha256'] == hashlib.sha256(row['fixture_nt'].encode()).hexdigest()
    assert not discovery['historical_root_acquired'] and len(discovery['results']) == 3
    assert sum(x.get('status') == 200 and x.get('content_type', '').startswith('text/html') for x in discovery['results']) == 1
    assert catalog['counts']['local_classes'] == 29 and catalog['counts']['missing_source_definitions'] == 4
    assert d['source']['historical_paper_axiom_fidelity'] == 'NOT_ESTABLISHED'
    assert d['source']['discovery']['historical_LMM_Alignments_root'] == 'NOT_ACQUIRED'
    paper_ids = {x['id'] for x in paper['evidence']}
    assert len(d['questions']) == 8 and len(d['findings']) == 8
    assert {x['id'] for x in d['questions']} == {'Q%02d' % x for x in range(1, 9)}
    findings = {x['id'] for x in d['findings']}
    assert len(findings) == 8
    for question in d['questions']:
        assert question['finding'] in findings and question['result'] and question['adverse']
        assert set(question['test_ids']) <= tests.keys()
        for locator in question['paper']:
            assert locator.split(':', 1)[0] == 'LMM2008'
            assert locator.split(':', 1)[1].split()[0] in paper_ids
    assert {t for q in d['questions'] for t in q['test_ids']} == tests.keys()
    assert d['questions'][-1]['state'] == 'NOT_EXECUTED_EXACT_ROOT_UNAVAILABLE'
    model = yaml.safe_load((root / 'model/concepts.yaml').read_text())
    model_ids = {x['id'] for x in model['records']}
    assert all(set(c['model_ids']) <= model_ids and c['status'] == 'OWNER_DECISION_REQUIRED' for c in d['candidate_uses'])
    assert d['boundary']['accepted_equivalences'] == [] and d['boundary']['model_change'] == 'NONE'
    print(json.dumps({'status': 'PASS', 'questions': 8, 'isolated_cases': 13, 'historical_alignment': 'NOT_ACQUIRED'}, sort_keys=True))


if __name__ == '__main__':
    run()
