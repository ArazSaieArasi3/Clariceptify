"""Check exact OntoLex core census, full glossary and non-DL evidence limits."""
from pathlib import Path
import argparse
import hashlib
import json
import yaml
from build_ontolex237_catalog import calculate, render, CATALOG, REPORT, CENSUS

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = 'evidence/related-work/artifacts/OntoLex.yaml'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(root=ROOT, source_dir=None):
    d = yaml.safe_load((root / ARTIFACT).read_text())
    census = json.loads((root / CENSUS).read_text())
    receipt = json.loads((root / d['execution']['receipt']).read_text())
    disc = json.loads((root / d['source']['discovery']).read_text())
    catalog = yaml.safe_load((root / CATALOG).read_text())
    review = yaml.safe_load((root / d['source']['document']['review']).read_text())
    assert d['issue'] == census['issue'] == receipt['issue'] == disc['issue'] == catalog['issue'] == 237
    assert review['identity']['source_sha256'] == d['source']['document']['sha256']
    assert sha(root / d['source']['document']['review']) == d['source']['document']['review_sha256']
    assert d['source']['selected_core']['sha256'] == census['source_sha256'] == receipt['source_sha256'] == catalog['source_sha256']
    assert sha(root / receipt['generator']) == receipt['generator_sha256']
    assert d['source']['author_repository']['sha256'] == census['repo_snapshot']['sha256']
    assert d['source']['author_repository']['commit'] == census['repo_snapshot']['commit']
    assert d['source']['author_repository']['blob'] == census['repo_snapshot']['blob']
    assert d['source']['author_repository']['tree'] == census['repo_snapshot']['tree']
    assert len(disc['checks']) == 4 and {x['id'] for x in disc['checks']} == {'W01','W02','G01','G02'}
    assert disc['checks'][1]['sha256'] == census['source_sha256'] and disc['checks'][3]['sha256'] == census['repo_snapshot']['sha256']
    assert disc['checks'][2]['tree'] == census['repo_snapshot']['tree'] and disc['checks'][2]['tree_truncated'] is False
    assert d['source']['selected_core']['syntax'] == 'RDF/XML' and d['source']['selected_core']['header_version'] == census['version_info'][0] == '1.1'
    assert d['source']['selected_core']['declared_imports'] == census['declared_import_iris'] == disc['declared_imports'] == []
    assert d['source']['selected_core']['license_iri'] in census['source_licenses']
    c = census['counts']; p = d['population']; cc = catalog['counts']
    assert c['named_classes'] == cc['named_declarations'] == p['total_declared_named_classes'] == 16
    assert c['local_classes'] == cc['local_classes'] == p['local_declared_named_classes'] == 8
    assert c['external_class_redeclarations'] == cc['external_redeclarations'] == p['external_redeclared_named_classes'] == 8
    assert cc['local_comment_candidates'] == p['local_comment_candidates'] == 8
    assert cc['local_missing_comments'] == p['local_missing_comments'] == 0
    assert cc['external_missing_comments'] == p['external_missing_comments'] == 8
    assert c['local_object_properties'] == p['local_object_properties'] == 17
    assert c['local_datatype_properties'] == p['local_datatype_properties'] == 3
    assert p['anonymous_owl_class_nodes'] == c['anonymous_owl_class_nodes'] == 2
    assert cc['imported_classes'] == p['imported_classes'] == 0 and cc['inferred_classes'] is p['inferred_classes'] is None
    assert len(census['classes']) == len(catalog['rows']) == 16
    assert {r['iri'] for r in census['classes']} == {r['iri'] for r in catalog['rows']}
    assert catalog == calculate(root) and (root / REPORT).read_text() == render(catalog)
    for r in catalog['rows']:
        if r['population'] == 'LOCAL':
            assert r['reviewer_paraphrase'] and r['source_definition_sha256']
        else:
            assert r['reviewer_paraphrase'] is None and r['source_definition_sha256'] is None
        assert r['hierarchy_and_constraints_ref'].startswith(CENSUS + '::classes[iri=')
    assert len(d['selected_commitments']) == 8 and {x['id'] for x in d['selected_commitments']} == {f'C{i:02d}' for i in range(1,9)}
    assert all(x['locator'] and x['reading'] and x['adverse'] for x in d['selected_commitments'])
    delta = census['comparison']
    assert delta['w3c_only_nonlabel_triples'] == delta['repo_only_nonlabel_triples'] == 6
    assert delta['concept_set_2016_on_property'] == 'http://www.w3.org/2004/02/skos/core#inScheme'
    assert delta['concept_set_repo_on_property'] == 'owl:inverseOf ' + delta['concept_set_2016_on_property']
    assert d['execution']['owl2_dl_profile'] == 'FAIL' and receipt['owl2_dl_profile_pass'] is False
    assert d['execution']['profile_violations'] == receipt['profile_violation_count'] == 37
    assert receipt['hermit_baseline_consistent'] and not receipt['hermit_unsatisfiable_named_classes']
    assert d['execution']['entailment_certification'] == 'NOT_ESTABLISHED_PROFILE_FAIL'
    assert receipt['isolated_semantic_cases'] == d['execution']['isolated_semantic_cases'] == 'NOT_EXECUTED_PROFILE_FAIL'
    assert d['decision']['status'] == 'OWNER_DECISION_REQUIRED' and d['decision']['accepted_equivalences'] == []
    model_ids = {r['id'] for r in yaml.safe_load((root / 'model/concepts.yaml').read_text())['records']}
    assert set(d['decision']['candidate_model_ids']) <= model_ids and d['decision']['next_issues'] == [253,126]
    assert all(v == 'NONE' for k,v in d['boundary'].items() if k.endswith('_change'))
    assert d['source']['source_redistribution'] is False and d['boundary']['source_redistribution'] is False
    audit = yaml.safe_load((root / 'evidence/related-work/deep-reviews/source-audit.yaml').read_text())
    row = next(r for r in audit['records'] if r['id'] == 'OntoLex')
    assert 'ONTOLEX237-S01' in row['repository']['evidence'] and row['class_coverage']['catalog_path'] == CATALOG
    assert row['class_coverage']['reasoner_execution'] == 'NOT_EXECUTED' and row['next_issues'] == [253,126]
    if source_dir:
        from rdflib import Graph, OWL, RDF, URIRef
        a = source_dir / 'OntoLex-core.ttl'; b = source_dir / 'ontolex-repository-current.owl'
        assert sha(a) == census['source_sha256'] and sha(b) == census['repo_snapshot']['sha256']
        g = Graph().parse(a, format='xml')
        assert len(g) == census['triples']
        assert {str(s) for s in g.subjects(RDF.type, OWL.Class) if isinstance(s, URIRef)} == {r['iri'] for r in catalog['rows']}
    return {'status':'PASS','named_classes':16,'local_classes':8,'external_redeclarations':8,'profile':'FAIL','source_reparsed':bool(source_dir)}


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--source-dir', type=Path)
    args = p.parse_args()
    print(json.dumps(check(source_dir=args.source_dir), sort_keys=True))
