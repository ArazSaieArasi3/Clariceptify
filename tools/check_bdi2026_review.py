"""Check BDI evidence bindings and claim limits; never rerun semantic tools by default."""
from pathlib import Path
import argparse
import hashlib
import json
import yaml
from render_bdi2026_review import render_catalog, render_review

ROOT = Path(__file__).resolve().parents[1]
BASE = 'evidence/related-work/'
EXPECTED = {
    'bdi/bdi.ttl': '250e02bf7987802f6051fbf01f9af53990863f5edc3a8ea52de09c382cbde984',
    'bdi-dul/bdi-dul.rdf': 'cd7d37d41d787b1766741285402861f13388219e52b60cb930d012de03cd9a98',
    'd0': 'cce97e892f117d7f7b2518eae4a24fb21a77b0de5d9cc1af6d1bffc747d69b29',
    'DUL': 'e5f6429596d2c7014730bad85aaaa9c39530235f27f596cd0e7ce85e6bbcba66',
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load(root=ROOT):
    r = yaml.safe_load((root / (BASE + 'artifacts/BDI2026.yaml')).read_text())
    c = yaml.safe_load((root / (BASE + 'bdi2026-class-catalog.yaml')).read_text())
    data = {k: json.loads((root / v['path']).read_text())
            for k, v in r['evidence'].items() if v['path'].endswith('.json')}
    return r, c, data


def validate(r, c, data):
    from inspect_bdi2026 import stable
    def need(condition, message):
        if not condition:
            raise ValueError(message)
    need(r['boundary'] == dict(model_change='NONE', requirements_change='NONE',
        fixtures_change='NONE', manuscript_change='NONE', release_change='NONE',
        scientific_acceptance='NOT_ASSESSED', independent_expert_review='NOT_PERFORMED',
        source_redistribution=False, adoption='OWNER_DECISION_REQUIRED'), 'Unsupported acceptance or scope change')
    need(len(r['questions']) == 8 and {q['id'] for q in r['questions']} == {f'Q{i:02}' for i in range(1, 9)}, 'Incomplete eight-question review')
    findings = {f['id'] for f in r['findings']}
    need(len(findings) == len(r['findings']) == 11, 'Incomplete findings')
    for q in r['questions']:
        need(q['result'] and q['locators'] and q['evidence'] and
             set(q['evidence']) <= set(r['evidence']) and set(q['finding_ids']) <= findings,
             'Unbound question')
    need(all(f['next_issues'] == [256, 126] for f in r['findings']), 'Findings lost from synthesis')
    modules = data['census']['modules']
    for key, digest in EXPECTED.items():
        need(modules[key]['source_sha256'] == digest, 'Source substitution: ' + key)
    need(modules['bdi/bdi.ttl']['imports'] == [] and modules['bdi-dul/bdi-dul.rdf']['imports'] == [
        'http://www.ontologydesignpatterns.org/ont/d0.owl', 'https://w3id.org/fossr/bdi/ontology/0.3/'],
        'Alignment/core version boundary changed')
    need(c['import_closure']['unresolved'] == ['https://w3id.org/fossr/bdi/ontology/0.3/'] and
         c['import_closure']['imported_definitions_complete'] is False, 'Unresolved import promoted')
    need(data['discovery']['unresolved_imports'] == c['import_closure']['unresolved'], 'Import discovery drift')
    need(data['census']['core_serialization_isomorphic'] is True, 'Serialization counts cannot be combined')
    rows = c['classes']
    need(len(rows) == len({x['iri'] for x in rows}) == 35, 'Duplicate or missing glossary row')
    for module in ['bdi/bdi.ttl', 'd0']:
        expected_rows = modules[module]['classes']
        actual = [x for x in rows if x['module'] == module]
        need({x['iri'] for x in actual} == set(modules[module]['declared_named_class_iris']), 'Incomplete module glossary')
        by_iri = {x['iri']: x for x in expected_rows}
        for x in actual:
            need(all(x[k] == v for k, v in by_iri[x['iri']].items()), 'Changed class/annotation/constraint source')
            need(x['constraint_sha256'] == stable([x['constraints'], x['related_axioms'], x['all_disjoint_groups']]), 'Changed class constraints')
            present = bool(x['annotation_records'])
            need(bool(x['reviewer_definition']['text']) == present, 'Missing source definition invented or present definition omitted')
            need(x['source_definition']['raw_text_public'] is False and
                 x['source_definition']['logical_sufficiency'] == 'NOT_INFERRED_FROM_COMMENT', 'Comment promoted or raw annotations exposed')
    need(c['counts'] == dict(core_local_classes=22, core_external_declarations=3, d0_local_classes=10,
        glossary_rows=35, source_comment_candidates=32, partial_comment_classes=1,
        missing_comment_classes=3, reviewer_reconstructions=0), 'Wrong glossary denominator')
    partial = [x for x in rows if x['source_definition']['status'] == 'PARTIAL_COMMENT_CANDIDATE']
    need(len(partial) == 1 and partial[0]['iri'].endswith('/Belief'), 'Truncated comment hidden')
    semantic = data['semantic']
    need(semantic['core_sha256'] == EXPECTED['bdi/bdi.ttl'], 'Semantic source substitution')
    need(semantic['core_profile_in_OWL2_DL'] is False and len(semantic['core_profile_violations']) == 1
         and 'rdf:type' in semantic['core_profile_violations'][0], 'Profile failure hidden')
    need(semantic['core_consistent'] is True and semantic['unsatisfiable_core_classes'] == [], 'Core consistency observation changed')
    need(semantic['exact_alignment_reasoning'] == 'BLOCKED_MISSING_BDI_0_3; no import stripping or0.5 substitution', 'Unexecuted alignment promoted')
    tests = semantic['tests']
    need(len(tests) == len({t['id'] for t in tests}) == 30, 'Incomplete semantic cases')
    need(semantic['summary'] == dict(total=30, passed=30, failed=0, errors=0), 'Semantic denominator changed')
    for t in tests:
        need(isinstance(t['observed_consistent'], bool) and t['observed_consistent'] is t['expected_consistent']
             and t['result'] == 'PASS' and t['error'] is None, 'Unsuccessful or unexecuted case promoted')
        if 'fixture_nt' in t:
            need(hashlib.sha256(t['fixture_nt'].encode()).hexdigest() == t['fixture_sha256'], 'Changed semantic fixture')
    by_id = {t['id']: t for t in tests}
    need(by_id['modification-edge']['observed_consistent'] is False and
         by_id['desire-same-type-part']['observed_consistent'] is True and
         by_id['desire-belief-part']['observed_consistent'] is False, 'Adverse/control finding hidden')
    for t in tests:
        if 'source_dataset' in t:
            need(t['observed_consistent'] is False, 'Author data silently repaired')
    cqs = data['cqs']
    need(cqs['core_sha256'] == EXPECTED['bdi/bdi.ttl'] and cqs['documented_tests'] == cqs['paper_cqs'] == 18, 'Incomplete CQ scope')
    executions = cqs['executions']
    need(len(executions) == len({(x['dataset'], x['cq']) for x in executions}) == 36, 'Duplicated or missing query execution')
    need(cqs['summary'] == dict(total=36, matches=17, mismatches=19), 'Negative query results hidden')
    for dataset in ['bdi/data-unit-testing.ttl', 'bdi-tests/bdi-tests.ttl']:
        subset = [x for x in executions if x['dataset'] == dataset]
        need({x['cq'] for x in subset} == {f'CQ{i}' for i in range(1, 19)}, 'Incomplete dataset CQ inventory')
        need(sum(x['expected_equal_observed'] for x in subset) == (17 if dataset.startswith('bdi/') else 0), 'Namespace/entailment mismatch concealed')
        for x in subset:
            need(x['expected_equal_observed'] == (x['expected_binding_sha256'] == x['observed_binding_sha256']), 'Query outcome contradicts bindings')
    need(cqs['owlunit_engine'].startswith('NOT_EXECUTED') and cqs['entailment'].startswith('NONE:'), 'Harness promoted to author engine/entailment')
    app = data['application']
    need(app['execution'] == 'NOT_EXECUTED' and app['paid_api_calls'] == 0 and
         app['runtime_ontology_in_selected_tree'] is False, 'Application reproduction invented')
    need(r['execution_summary']['semantic_cases'] == semantic['summary'] and
         r['execution_summary']['asserted_query_executions'] == cqs['summary'], 'Summary drifts from executions')
    return dict(status='PASS', issue=250, reviewed_questions=8, glossary_rows=35,
        core_local_classes=22, supporting_d0_classes=10, shared_DUL_classes=78,
        recorded_semantic_cases=30, recorded_asserted_queries=36,
        observed_query_matches=17, observed_query_mismatches=19,
        scope='Recorded evidence integrity only; not a HermiT rerun, scientific acceptance or full alignment validation')


def check(root=ROOT, source_dir=None):
    r, c, data = load(root)
    for ref in [r['paper_review'], r['source_manifest'], *r['evidence'].values()]:
        if sha(root / ref['path']) != ref['sha256']:
            raise ValueError('Stale evidence binding: ' + ref['path'])
    if sha(root / c['shared_DUL_glossary']['path']) != c['shared_DUL_glossary']['sha256']:
        raise ValueError('Shared DUL glossary changed')
    manifest = yaml.safe_load((root / r['source_manifest']['path']).read_text())
    pins = {x['id']: x['sha256'] for x in manifest['artifacts']}
    if any(pins[k] != v for k, v in EXPECTED.items()):
        raise ValueError('Changed input source manifest')
    for key in ['census', 'semantic', 'cqs']:
        rec = data[key]
        if sha(root / rec['generator_path']) != rec['generator_sha256'] or rec['source_manifest_sha256'] != r['source_manifest']['sha256']:
            raise ValueError('Changed executed generator or manifest')
    result = validate(r, c, data)
    if (root / (BASE + 'bdi2026-class-catalog.md')).read_text() != render_catalog(c):
        raise ValueError('Stale rendered glossary')
    if (root / (BASE + 'artifacts/BDI2026.md')).read_text() != render_review(r):
        raise ValueError('Stale rendered review')
    if source_dir is not None:
        from inspect_bdi2026 import inspect
        observed = inspect(source_dir)
        if observed['modules'] != data['census']['modules']:
            raise ValueError('Public class census differs from exact raw sources')
        result['exact_private_source_reparse'] = 'PASS'
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--source-dir', type=Path)
    a = p.parse_args()
    print(json.dumps(check(source_dir=a.source_dir), indent=2))
