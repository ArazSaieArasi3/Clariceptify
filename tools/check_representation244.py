#!/usr/bin/env python3
"""Check selected publisher-supplement evidence and finite local axiom examples."""

import hashlib
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    d = yaml.safe_load((root / 'evidence/related-work/artifacts/Representation.yaml').read_text())
    review_path = root / d['source']['dossier']
    review = yaml.safe_load(review_path.read_text(encoding='utf-8'))
    ledger_path = root / d['source']['formal_ledger']
    discovery = json.loads((root / d['source']['discovery']).read_text(encoding='utf-8'))
    old = json.loads((root / discovery['prior_receipt']).read_text(encoding='utf-8'))
    assert d['issue'] == discovery['issue'] == 244 and d['source']['work'] == review['work_id']
    assert review['source']['sha256'] == discovery['paper_sha256'] == d['source']['main_paper_sha256']
    assert hashlib.sha256(review_path.read_bytes()).hexdigest() == d['source']['dossier_sha256']
    assert hashlib.sha256(ledger_path.read_bytes()).hexdigest() == d['source']['formal_ledger_sha256']
    assert d['source']['supplement_pages'] == review['supplement_formula_population']['pdf_pages'] == 10
    assert d['population']['printed_labeled_supplement_expressions'] == len(review['commitments']) == 49
    assert d['population']['tabulated_predicate_signatures'] == len(review['relation_index']) == 41
    assert len(d['commitments']) == d['population']['selected_paper_commitments'] == 8
    assert len({c['id'] for c in d['commitments']}) == 8
    source = {c['id']: c for c in review['commitments']}
    evidence = {e['id'] for e in review['evidence']}
    for c in d['commitments']:
        assert source[c['paper_id']]['label'] == c['formula']
        assert c['locator'].split(':')[1].split()[0] in source[c['paper_id']]['evidence']
        assert c['locator'].split(':')[1].split()[0] in evidence
        assert c['observation'] and 'PDF p.' in c['locator']
    assert {x['id'] for x in discovery['checks']} == {'P01', 'V01', 'G01', 'G02', 'W01'}
    assert discovery['checks'][1]['supplement_pdf_page'] == 8
    assert discovery['raw_supplement_sha256'] is None
    assert old['global_absence_claim'] is False
    assert not discovery['author_executable_root_identified'] and not discovery['global_absence_claim']
    for key in ('supplement_raw_sha256', 'machine_root', 'machine_root_version', 'machine_root_sha256',
                'repository_commit', 'machine_syntax', 'machine_license', 'direct_imports', 'unresolved_imports'):
        assert d['source'][key] is None, key
    for key in ('local_machine_classes', 'imported_machine_classes', 'referenced_machine_classes',
                'deprecated_machine_classes', 'inferred_machine_classes', 'named_machine_properties',
                'machine_definition_candidates', 'machine_missing_definitions', 'complete_machine_glossary'):
        assert d['population'][key] is None, key
    assert d['foundation']['exact_host_edition'] is None and d['foundation']['actual_formal_import'] is None
    assert d['foundation']['established_alignment'] is False

    # Explicitly local finite records. They check Ax9/Ax15 functionality only;
    # neither host mereology nor full first-order theory is interpreted here.
    def functional_on_pair(rows):
        return all(m == n for f, c, m in rows for g, d, n in rows if (f, c) == (g, d))

    def unique_pattern(rows):
        return all(p == q for p, entity in rows for q, other in rows if entity == other)

    assert functional_on_pair([('F', 'C', 'M')])
    assert not functional_on_pair([('F', 'C', 'M1'), ('F', 'C', 'M2')])
    assert unique_pattern([('P', 'book')])
    assert not unique_pattern([('P1', 'book'), ('P2', 'book')])
    assert 'exists o,r,p,p2' in source['K-D11']['statement']
    assert 'FORMOF(f,r)' in source['K-D11']['statement']
    assert 'PATTERNFORFORM(p,f)' in source['K-D11']['statement']
    assert d['execution']['selected_d11_visual_review'] == 'PASS_PUBLISHER_LINKED_PDF_PAGE_8'
    assert all(d['execution'][key].startswith('NOT_EXECUTED') for key in
               ('executable_root_parse', 'reasoner', 'theorem_prover', 'author_proof_reproduction'))
    assert set(d['scenarios']['paper_scenario_ids']) <= {s['id'] for s in review['scenarios']}
    model = yaml.safe_load((root / 'model/concepts.yaml').read_text(encoding='utf-8'))
    assert set(d['decision']['candidate_model_ids']) <= {r['id'] for r in model['records']}
    assert d['decision']['owner_status'] == 'OWNER_DECISION_REQUIRED'
    assert d['decision']['accepted_equivalences'] == []
    audit = yaml.safe_load((root / 'evidence/related-work/deep-reviews/source-audit.yaml').read_text(encoding='utf-8'))
    row = next(r for r in audit['records'] if r['id'] == 'CLR-RW-Representation')
    assert 'REP2025-TECH-20261030' in row['repository']['evidence']
    assert row['technical_followup']['evidence'] == 'evidence/related-work/artifacts/Representation.yaml'
    assert row['class_coverage']['local_classes'] is None
    assert row['class_coverage']['reasoner_execution'] == 'NOT_EXECUTED'
    assert row['next_issues'] == [255, 126]
    assert all(d['limits'][key] == 'NONE' for key in ('model_change', 'requirements_change',
                                                    'fixtures_change', 'manuscript_change', 'release_change'))
    print(json.dumps({'status': 'PASS', 'selected_formulas': 8, 'finite_local_cases': 4,
                      'machine_classes': None, 'D11_visual': 'SCOPED_PASS'}, sort_keys=True))


if __name__ == '__main__':
    check()
