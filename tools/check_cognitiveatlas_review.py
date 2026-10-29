"""Verify recorded Cognitive Atlas coverage and result boundaries, not rerun reasoning."""
from pathlib import Path
from collections import Counter
import argparse,hashlib,json,yaml
from render_cognitiveatlas_review import render_catalog,render_review
from build_corpus_descriptives import calculate,render as render_descriptives
ROOT=Path(__file__).resolve().parents[1]
SHA='701aa9e8351fcec3de0122df7ed49158cff83fe4e7353bd540122d8a34ce5fd8'
NS='http://www.cognitiveatlas.org/ontology/cogat.owl#'
LICENSE='https://creativecommons.org/licenses/by-sa/3.0/us/'


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def load(root=ROOT):
    report=yaml.safe_load((root/'evidence/related-work/artifacts/CognitiveAtlas.yaml').read_text())
    catalog=yaml.safe_load((root/'evidence/related-work/cognitiveatlas-class-catalog.yaml').read_text())
    data={k:json.loads((root/v['path']).read_text()) for k,v in report['evidence'].items() if v['path'].endswith('.json')}
    rows=[json.loads(x) for x in (root/catalog['indexes']['classes.jsonl']['path']).read_text().splitlines()]
    definitions=[json.loads(x) for x in (root/catalog['indexes']['source-definitions.jsonl']['path']).read_text().splitlines()]
    return report,catalog,data,rows,definitions


def validate(r,c,data,rows,definitions):
    from inspect_cognitive_atlas import stable
    def require(ok,message):
        if not ok:raise ValueError(message)
    require(r['boundary']==dict(model_change='NONE',requirements_change='NONE',fixtures_change='NONE',manuscript_change='NONE',release_change='NONE',independent_expert_review='NOT_PERFORMED',semantic_acceptance='NOT_ASSESSED',adoption='OWNER_DECISION_REQUIRED',original_source_files_redistributed=False),'Scope or acceptance promoted')
    require(r['source_root']['sha256']==c['source_sha256']==data['census']['source_sha256']==SHA,'Root source substituted')
    require(len(r['questions'])==8 and {q['id'] for q in r['questions']}=={f'Q{i:02}' for i in range(1,9)},'Incomplete eight-question scope')
    findings={f['id'] for f in r['findings']}
    require(len(findings)==len(r['findings'])==9 and all(f['next_issues']==[254,126] for f in r['findings']),'Findings lost from comparison')
    for q in r['questions']:require(q['result'] and q['locators'] and set(q['evidence'])<=set(r['evidence']) and set(q['finding_ids'])<=findings,'Unbound question')
    require(len(rows)==len({x['iri'] for x in rows})==1698,'Incomplete/duplicate class population')
    require(len(definitions)==len({x['iri'] for x in definitions})==1698,'Incomplete/duplicate definition register')
    by_iri={x['iri']:x for x in definitions};require(set(by_iri)=={x['iri'] for x in rows},'Definition/class join loses or duplicates IRIs')
    local=[x for x in rows if x['iri'].startswith(NS)];states=Counter(x['source_definition']['status'] for x in local)
    require(len(local)==1696 and len(rows)-len(local)==2,'Local/external class grain changed')
    require(states=={'NONEMPTY_SOURCE_DEFINITION':1232,'EMPTY_ANNOTATION_ONLY':55,'NOT_REPORTED_IN_SELECTED_SOURCE':409},'Missing/empty definitions hidden')
    require(c['counts']==dict(local_classes=1696,external_class_declarations=2,source_definition_candidates=1232,empty_definition_annotations=55,absent_definition_annotations=409,missing_source_definitions=464,ambiguous_multi_identifier_classes=101,reviewer_reconstructions=0),'Wrong definition denominator')
    collisions=[x for x in local if len(x['identifiers'])>1]
    require(len(collisions)==101 and all(x['source_identifier_kinds']==['cnt','trm'] for x in collisions),'Identifier collision hidden or treated as disambiguated')
    for x in rows:
        require(x['source_sha256']==SHA and x['constraint_sha256']==stable(x['constraints']),'Class provenance/constraints changed')
        require(x['reviewer_definition']['text'] is None,'Invented mass paraphrase or definition')
        source=by_iri[x['iri']]
        require(source['license_url']==LICENSE and source['source_sha256']==SHA,'Definition attribution/license/source stripped')
        for a in source['definitions']:require(hashlib.sha256(a['text'].encode()).hexdigest()==a['text_sha256'],'Definition text changed')
        require([a['text_sha256'] for a in source['definitions']]==[a['text_sha256'] for a in x['source_definition']['annotations']],'Definition annotation locator disagreement')
        if x['source_definition']['status']=='NOT_REPORTED_IN_SELECTED_SOURCE':require(source['definitions']==[],'Absent source definition invented')
        if x['source_definition']['status']=='EMPTY_ANNOTATION_ONLY':require(all(not a['text'].strip() for a in source['definitions']),'Empty source definition filled')
    census=data['census'];counts=census['counts']
    require(census['imports']==[] and census['version_info']==['0.3'],'Unexpected imports/version')
    require(counts['local_declared_object_properties']==3 and counts['external_declared_object_properties']==1 and counts['used_restriction_properties']==7 and counts['undeclared_used_object_properties']==3,'Declared/used relation units conflated')
    require(len(census['referenced_undeclared_class_iris'])==11,'Undeclared reference population hidden')
    semantic=data['semantic'];tests=semantic['tests']
    require(semantic['owl2_dl_profile_pass'] is False and semantic['profile_violation_count']==7341,'Profile failure hidden')
    require(semantic['core_logical_consistent'] is True and semantic['unsatisfiable_named_classes']==[],'Logical observation changed')
    require(len(tests)==len({t['id'] for t in tests})==14 and semantic['summary']==dict(total=14,passed=14,failed=0,errors=0),'Incomplete semantic execution')
    for t in tests:
        require(isinstance(t['observed_consistent'],bool) and t['observed_consistent'] is t['expected_consistent'] and t['result']=='PASS' and t['error'] is None,'Unsuccessful/unexecuted scenario promoted')
        require(hashlib.sha256(t['fixture_nt'].encode()).hexdigest()==t['fixture_sha256'],'Fixture provenance changed')
    by_id={t['id']:t for t in tests}
    require(by_id['concrete-concept-task-only']['observed_consistent'] is False and by_id['neutral-concept-task-only']['observed_consistent'] is True,'Concrete/schema control distinction lost')
    st=data['static']
    require(all(x['result']=='PARSE_FAIL' for x in st['raw_RDF_parses']) and len(st['raw_RDF_parses'])==2,'Raw source repaired or parse failure hidden')
    require(st['generator_execution']==st['pickle_execution']=='NOT_EXECUTED','Generation/pickle execution invented')
    require(st['first_assertion']['is_header'] is False and st['license_evidence']['exact_link_present'] is True,'Source/rights evidence lost')
    require(r['execution_summary']['semantic']==semantic['summary'],'Summary drift')
    return dict(status='PASS',issue=241,declared_class_rows=1698,local_classes=1696,nonempty_local_definitions=1232,missing_or_empty_local_definitions=464,identifier_collisions=101,recorded_semantic_expectations=14,scope='Recorded evidence integrity;not a reasoner rerun,foundational equivalence or independent expert acceptance')


def check(root=ROOT,source_dir=None):
    r,c,data,rows,definitions=load(root)
    for ref in [r['source_manifest'],r['paper_review'],*r['evidence'].values()]:
        if digest(root/ref['path'])!=ref['sha256']:raise ValueError('Stale evidence binding:'+ref['path'])
    for name,index in c['indexes'].items():
        if digest(root/index['path'])!=index['sha256'] or index['rows']!=1698:raise ValueError('Changed complete class/definition index')
    from build_documentation import inventory
    public=inventory(root)
    if any(index['path'] not in public for index in c['indexes'].values()):raise ValueError('Complete class/definition register omitted from public reader')
    if c['indexes']!=data['census']['catalog_indexes']:raise ValueError('Catalogue/census index disagreement')
    for name in ['census','static','semantic']:
        rec=data[name]
        if rec['generator_sha256']!=digest(root/rec['generator_path']) or rec['source_manifest_sha256']!=r['source_manifest']['sha256']:raise ValueError('Changed executed generator/inputs')
    result=validate(r,c,data,rows,definitions)
    if (root/'evidence/related-work/cognitiveatlas-class-catalog.md').read_text()!=render_catalog(c):raise ValueError('Stale glossary reader')
    if (root/'evidence/related-work/artifacts/CognitiveAtlas.md').read_text()!=render_review(r):raise ValueError('Stale technical reader')
    current=calculate(root)
    if data['descriptives']!=current or (root/'docs/research/source-review-descriptives.md').read_text()!=render_descriptives(current):raise ValueError('Stale or unqualified corpus statistics')
    if source_dir is not None:
        from inspect_cognitive_atlas import inspect
        observed=inspect(source_dir)
        if observed['classes']!=rows or observed['source_definition_register']!=definitions:raise ValueError('Exact source/glossary reconciliation failed')
        result['exact_private_source_reparse']='PASS'
    return result


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source-dir',type=Path);a=p.parse_args();print(json.dumps(check(source_dir=a.source_dir),indent=2))
