"""Descriptive coverage from current dossiers and separately pinned module censuses.

Paper catalog entries, relation groups, local OWL classes and object properties
are different units. No corpus-wide semantic size/quality total is fabricated.
"""
from pathlib import Path
import hashlib
import json
import yaml

ROOT=Path(__file__).resolve().parents[1]
BASE='evidence/related-work/deep-reviews/'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def calculate(root=ROOT):
    reg=yaml.safe_load((root/(BASE+'register.yaml')).read_text()); papers=[]; bindings={}
    for entry in reg['acquired_papers']:
        path=BASE+entry['id']+'/review.yaml'; d=yaml.safe_load((root/path).read_text()); bindings[path]=sha(root/path)
        papers.append(dict(work_id=entry['id'], review_state=d['status'],
                           catalog_items=len(d['catalog']),
                           indexed_relation_groups=len(d['relation_index']) if isinstance(d.get('relation_index'), list) else None,
                           commitment_records=len(d['commitments']), reviewer_scenarios=len(d['scenarios']),
                           critical_findings=len(d['findings']), source=path,
                           units='Paper extraction records, not machine classes/properties or unique corpus concepts.'))
    modules=[]
    def legacy(label, path, namespace):
        d=json.loads((root/path).read_text()); bindings[path]=sha(root/path)
        cs=[x['iri'] for x in d['classes']]; ops=[x['iri'] for x in d['object_properties']]
        modules.append(dict(module=label, source_sha256=d['source_sha256'],
            local_classes=sum(x.startswith(namespace) for x in cs), external_class_redeclarations=sum(not x.startswith(namespace) for x in cs),
            local_declared_object_properties=sum(x.startswith(namespace) for x in ops),
            external_object_property_redeclarations=sum(not x.startswith(namespace) for x in ops),
            all_declared_object_properties=len(ops), source=path))
    legacy('cDnS core1.1', BASE+'cDnS2007/artifact-census.json','http://www.loa-cnr.it/ontologies/cDnS.owl#')
    legacy('LMM L1', BASE+'LMM2008/LMM_L1-census.json','http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#')
    legacy('LMM L2', BASE+'LMM2008/LMM_L2-census.json','http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#')
    legacy('Conceptualization0.1', BASE+'shared-foundations/Conceptualization/DULConceptualization-census.json','http://www.ontologydesignpatterns.org/ont/dul/Conceptualization.owl#')
    legacy('IOLite', BASE+'shared-foundations/IOLite/IOLite-census.json','http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl#')
    legacy('Emotions May2015', BASE+'Emotions-2015/candidate-census.json','http://rhizomik.net/ontologies/emotionsonto.owl#')
    path='evaluation/related-work/bdi2026/technical-census.json'; b=json.loads((root/path).read_text()); bindings[path]=sha(root/path)
    for name, ns in [('bdi/bdi.ttl','https://w3id.org/fossr/ontology/bdi/'),('d0','http://www.ontologydesignpatterns.org/ont/d0.owl#'),('DUL','http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#')]:
        d=b['modules'][name]; ops=d['object_properties']; modules.append(dict(module={'bdi/bdi.ttl':'BDI0.5','d0':'d0 selected source','DUL':'DUL4.2'}[name], source_sha256=d['source_sha256'], local_classes=len(d['local_class_iris']), external_class_redeclarations=len(d['external_class_iris']), local_declared_object_properties=sum(x.startswith(ns) for x in ops), external_object_property_redeclarations=sum(not x.startswith(ns) for x in ops), all_declared_object_properties=len(ops), source=path))
    path='evaluation/related-work/cognitiveatlas/technical-census.json'; d=json.loads((root/path).read_text()); bindings[path]=sha(root/path); c=d['counts']
    modules.append(dict(module='Cognitive Atlas export0.3', source_sha256=d['source_sha256'], local_classes=c['local_named_classes'], external_class_redeclarations=c['external_named_classes'], local_declared_object_properties=c['local_declared_object_properties'], external_object_property_redeclarations=c['external_declared_object_properties'], all_declared_object_properties=c['declared_object_properties'], source=path))
    path='evaluation/related-work/dns235/census.json';dns=json.loads((root/path).read_text());bindings[path]=sha(root/path);dc=dns['counts']
    modules.append(dict(module='ExtendedDnS397 (later candidate)',source_sha256=dns['source_sha256'],local_classes=dc['local_classes'],external_class_redeclarations=dc['external_class_redeclarations'],local_declared_object_properties=dc['local_object_properties'],external_object_property_redeclarations=dc['external_object_properties'],all_declared_object_properties=dc['local_object_properties']+dc['external_object_properties'],source=path))
    # Source-bound namespaces must come from the actual catalogue. Reject a misspelled
    # namespace instead of silently displaying zero local classes.
    if any(m['local_classes']==0 for m in modules):raise ValueError('Empty local namespace; check actual source/module definition')
    counts=dict(full_paper_reviews=len(papers), full_reviews_complete=sum(p['review_state']=='REVIEW_COMPLETE' for p in papers),
                limited_summary_reviews=len(reg.get('limited_evidence_papers',[])),
                separate_document_sources=len(reg.get('separate_document_tasks',[])),
                module_rows=len(modules), catalog_item_records=sum(p['catalog_items'] for p in papers),
                findings_records=sum(p['critical_findings'] for p in papers),
                papers_with_relation_index=sum(p['indexed_relation_groups'] is not None for p in papers))
    return dict(schema_version='1.0', requested_on='2026-10-29', status='DESCRIPTIVE_BASELINE_NOT_FINAL_SYNTHESIS',
        generator_path='tools/build_corpus_descriptives.py', generator_sha256=sha(root/'tools/build_corpus_descriptives.py'),
        register_sha256=sha(root/(BASE+'register.yaml')), counts=counts, papers=papers, modules=modules,
        source_bindings=bindings, claim_limits=[
            'The 18 retained full-paper reviews and one limited I&DA review are separate evidence populations.',
            'Catalog items include several extracted kinds; the count is not an OWL class count or unique conceptual inventory.',
            'Relation-index rows are paper-specific groups; missing relation indexes are null, not zero. No unified relation sum.',
            'Module rows use a selected exact root and local namespace. External redeclarations and property totals stay separate.',
            'Classes reused across imports, serializations, modules and versions are not summed into a unique corpus class total.',
            'Not every primary work has a completed formal artifact census. Null/unavailable sources do not establish ontology absence.',
            'Numbers describe retained sources, not correctness, comparative superiority, coverage of conceptualization or novelty.'],
        conclusion='The reading wave can be summarized now and descriptive statistics are available. Final technical/comparative synthesis #126 remains dependent on the source-specific technical tasks and six comparison batches.', model_change='NONE')


def render(d):
    c=d['counts']; lines=['# Source-review descriptive baseline','',
        'The deep-reading wave can be summarized: '+str(c['full_reviews_complete'])+'/'+str(c['full_paper_reviews'])+' retained full-text dossiers are complete, plus '+str(c['limited_summary_reviews'])+' separately bounded I&DA summary review. Final comparison/synthesis #126 remains open.','',
        '## Coverage and units','',
        str(c['catalog_item_records'])+' catalog-item records and '+str(c['findings_records'])+' critical-finding records are indexed across the 18 full-text dossiers. They are extraction records, not unique concepts, machine classes or independently proved defects.','',
        '## Selected machine-readable roots','',
        '| Exact selected module | Local named classes | External class declarations | Local object properties | External object-property declarations |',
        '|---|---:|---:|---:|---:|']
    for m in d['modules']:
        lines.append('| '+m['module']+' | '+' | '.join(str(m[k]) for k in ['local_classes','external_class_redeclarations','local_declared_object_properties','external_object_property_redeclarations'])+' |')
    lines+=['','An object-property declaration is a relation type, not the number of relation statements, restrictions, assertions or paper relation groups. Cognitive Atlas additionally has 2,825 restriction nodes and 4,622 subclass statements in its selected graph; they are not additional object properties.','',
        '## Per-paper extraction','',
        '| Work | Catalog items | Relation-index groups | Commitment records | Critical findings |',
        '|---|---:|---:|---:|---:|']
    for p in d['papers']:
        lines.append('| '+p['work_id']+' | '+' | '.join('NOT_SEPARATELY_INDEXED' if p[k] is None else str(p[k]) for k in ['catalog_items','indexed_relation_groups','commitment_records','critical_findings'])+' |')
    lines+=['','## Interpretation and next work','', d['conclusion'],'']
    lines+=['- '+x for x in d['claim_limits']]
    lines+=['','The [machine-readable record](../../evaluation/related-work/corpus-descriptives.json) binds every source file/hash and the calculation script. No paper/artifact equivalence, accepted alignment or ontology change is implied.','']
    return '\n'.join(lines)


if __name__=='__main__':
    d=calculate();(ROOT/'evaluation/related-work/corpus-descriptives.json').write_text(json.dumps(d, indent=2, sort_keys=True)+'\n');(ROOT/'docs/research/source-review-descriptives.md').write_text(render(d)); print(json.dumps(d['counts'], sort_keys=True))
