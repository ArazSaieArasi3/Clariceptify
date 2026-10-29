"""Inspect two exact OntoLex core bytes offline; no remote imports or source repairs."""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import platform

ROOT = Path(__file__).resolve().parents[1]
NS = 'http://www.w3.org/ns/lemon/ontolex#'
OFFICIAL_SHA = 'b4265ab8bf1fc61dc413ed3eb6c70b951cb69c76c406a6f4bfef7684acf014ee'
REPO_SHA = '76e4c74fae4013944f60701df83828836c22a7f19c8cc8f72f994e321d12efd9'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def run(official_path, repo_path, census_path, execution_path):
    import jpype
    import owlready2
    from rdflib import BNode, Graph, OWL, RDF, RDFS, URIRef
    from rdflib.compare import graph_diff, to_isomorphic

    raw = official_path.read_bytes()
    other = repo_path.read_bytes()
    if sha(raw) != OFFICIAL_SHA or sha(other) != REPO_SHA:
        raise ValueError('Pinned source-byte mismatch')
    a, b = Graph().parse(data=raw, format='xml'), Graph().parse(data=other, format='xml')
    declared = {s for s in a.subjects(RDF.type, OWL.Class) if isinstance(s, URIRef)}
    local = sorted((s for s in declared if str(s).startswith(NS)), key=str)
    external = sorted(declared - set(local), key=str)
    anonymous = list({s for s in a.subjects(RDF.type, OWL.Class) if isinstance(s, BNode)})
    if len(local) != 8 or len(external) != 8 or len(anonymous) != 2:
        raise ValueError('Changed declared class population')

    def expr(node):
        if isinstance(node, URIRef):
            return str(node)
        if not isinstance(node, BNode):
            return str(node)
        if (node, RDF.type, OWL.Restriction) in a:
            fields = {}
            for pred in (OWL.onProperty, OWL.onClass, OWL.onDataRange, OWL.minQualifiedCardinality,
                         OWL.maxQualifiedCardinality, OWL.qualifiedCardinality, OWL.cardinality):
                vals = list(a.objects(node, pred))
                if vals:
                    fields[str(pred).rsplit('#', 1)[-1]] = expr(vals[0])
            return {'Restriction': fields}
        return {'anonymous': sorted((str(p), expr(o)) for p, o in a.predicate_objects(node))}

    def english(node, pred):
        return next((str(v) for v in a.objects(node, pred) if getattr(v, 'language', None) == 'en'), None)

    rows = []
    for c in local + external:
        comment = english(c, RDFS.comment)
        rows.append(dict(iri=str(c), population='LOCAL' if c in local else 'EXTERNAL_REDECLARATION',
                         label_en=english(c, RDFS.label), source_comment_status='PRESENT_ENGLISH_COMMENT' if comment else 'MISSING_IN_SELECTED_ROOT',
                         source_comment_sha256=sha(comment.encode()) if comment else None,
                         source_locator=f'{str(official_path.name)}::{c} rdfs:comment' if comment else f'{str(official_path.name)}::{c} no rdfs:comment',
                         subclass_of=sorted([expr(o) for o in a.objects(c, RDFS.subClassOf)], key=str),
                         equivalent_class=sorted([expr(o) for o in a.objects(c, OWL.equivalentClass)], key=str),
                         disjoint_with=sorted([expr(o) for o in a.objects(c, OWL.disjointWith)], key=str),
                         deprecated=any(str(v).lower() == 'true' for v in a.objects(c, OWL.deprecated))))

    referenced = {o for p in (RDFS.subClassOf, OWL.equivalentClass, OWL.onClass, RDFS.domain, RDFS.range)
                  for _, o in a.subject_objects(p) if isinstance(o, URIRef)}
    o = URIRef(NS[:-1]); concept_set = URIRef(NS + 'ConceptSet')
    old_expr, new_expr = next(a.objects(concept_set, OWL.equivalentClass)), next(b.objects(concept_set, OWL.equivalentClass))
    w3c_prop, repo_prop = next(a.objects(old_expr, OWL.onProperty)), next(b.objects(new_expr, OWL.onProperty))
    inverse = next(b.objects(repo_prop, OWL.inverseOf), None)
    if str(w3c_prop) != 'http://www.w3.org/2004/02/skos/core#inScheme' or inverse != w3c_prop:
        raise ValueError('ConceptSet direction evidence changed')
    # Make a canonical RDF delta after eliminating translated labels; a syntactic
    # difference is not assumed to be a logical difference without the above path.
    filtered = []
    for graph in (a, b):
        g = Graph()
        for s, p, v in graph:
            if p != RDFS.label:
                g.add((s, p, v))
        filtered.append(g)
    common, a_only, b_only = graph_diff(to_isomorphic(filtered[0]), to_isomorphic(filtered[1]))
    imports = sorted(str(v) for v in a.objects(None, OWL.imports))
    census = dict(schema_version='1.0', issue=237, checked_on='2026-10-29',
                  source_sha256=OFFICIAL_SHA, source_iri=str(o), version_info=[str(v) for v in a.objects(o, OWL.versionInfo)],
                  source_rights=[str(v) for v in a.objects(o, URIRef('http://purl.org/dc/elements/1.1/rights'))],
                  source_licenses=sorted(str(v) for p in (URIRef('http://creativecommons.org/ns#license'), URIRef('http://creativecommons.org/ns#licence')) for v in a.objects(o, p)),
                  parsed_as='RDF/XML despite acquired .ttl filename', triples=len(a),
                  counts=dict(named_classes=len(declared), local_classes=len(local), external_class_redeclarations=len(external),
                              anonymous_owl_class_nodes=len(anonymous), local_english_comment_candidates=sum(r['source_comment_status'] == 'PRESENT_ENGLISH_COMMENT' for r in rows if r['population'] == 'LOCAL'),
                              external_english_comments=sum(r['source_comment_status'] == 'PRESENT_ENGLISH_COMMENT' for r in rows if r['population'] != 'LOCAL'),
                              local_object_properties=sum(isinstance(s, URIRef) and str(s).startswith(NS) for s in set(a.subjects(RDF.type, OWL.ObjectProperty))),
                              local_datatype_properties=sum(isinstance(s, URIRef) and str(s).startswith(NS) for s in set(a.subjects(RDF.type, OWL.DatatypeProperty)))),
                  declared_import_iris=imports, imported_class_population=0 if not imports else None,
                  referenced_without_declaration=sorted(str(x) for x in referenced - declared),
                  classes=rows, repo_snapshot=dict(commit='ab0165605301413e64a66d53d23c3095fa879a26', tree='463af47eef62fe99641bc33d0cc416363c58ba69',
                                                  blob='10783b4c747bbc5f08fbae8f4169d6e02fc22565', sha256=REPO_SHA, triples=len(b)),
                  comparison=dict(w3c_only_nonlabel_triples=len(a_only), repo_only_nonlabel_triples=len(b_only),
                                  concept_set_2016_on_property=str(w3c_prop),
                                  concept_set_repo_on_property='owl:inverseOf ' + str(inverse),
                                  correspondence='LOGICAL_DIRECTION_DIFFERS; SAME_VERSION_INFO_DOES_NOT_CERTIFY_IDENTICAL_AXIOMS',
                                  other_nonlabel_difference='One duplicate spelling cc:licence only in selected W3C bytes; cc:license exists in both.'),
                  model_change='NONE')

    jar = Path(owlready2.__file__).parent / 'hermit/HermiT.jar'
    jpype.startJVM(classpath=[str(jar)])
    J = jpype.JClass
    File = J('java.io.File')
    m = J('org.semanticweb.owlapi.apibinding.OWLManager').createOWLOntologyManager()
    ont = m.loadOntologyFromOntologyDocument(File(str(official_path.resolve())))
    check = J('org.semanticweb.owlapi.profiles.OWL2DLProfile')().checkOntology(ont)
    violations = list(check.getViolations())
    types = {}
    for v in violations:
        k = str(v.getClass().getSimpleName())
        types[k] = types.get(k, 0) + 1
    reasoner = J('org.semanticweb.HermiT.Reasoner$ReasonerFactory')().createReasoner(ont)
    try:
        consistent = bool(reasoner.isConsistent())
        unsat = sorted(str(c.getIRI()) for c in reasoner.getUnsatisfiableClasses().getEntitiesMinusBottom())
    finally:
        reasoner.dispose()
    execution = dict(schema_version='1.0', issue=237, checked_on='2026-10-29',
                     generator='tools/inspect_ontolex237.py', generator_sha256=sha(Path(__file__).read_bytes()),
                     python=platform.python_version(), rdflib=importlib.metadata.version('rdflib'),
                     jpype=importlib.metadata.version('JPype1'), owlready2=importlib.metadata.version('owlready2'),
                     source_sha256=OFFICIAL_SHA, parsed_graph_triples=len(a), owlapi_axioms=int(ont.getAxiomCount()),
                     owl2_dl_profile_pass=bool(check.isInProfile()), profile_violation_count=len(violations),
                     profile_violation_types=dict(sorted(types.items())), hermit_baseline_consistent=consistent,
                     hermit_unsatisfiable_named_classes=unsat,
                     reasoning_limit='Profile fails; HermiT observations on original bytes are recorded, but not certified OWL 2 DL consequences or all-resource validation.',
                     isolated_semantic_cases='NOT_EXECUTED_PROFILE_FAIL',
                     source_repair='NONE', remote_imports_loaded=0,
                     command='python tools/inspect_ontolex237.py --official PRIVATE/OntoLex-core.ttl --repository PRIVATE/ontolex-repository-current.owl --census evaluation/related-work/ontolex237/census.json --execution evaluation/related-work/ontolex237/execution.json')
    census_path.parent.mkdir(parents=True, exist_ok=True)
    execution_path.parent.mkdir(parents=True, exist_ok=True)
    census_path.write_text(json.dumps(census, indent=2, sort_keys=True) + '\n')
    execution_path.write_text(json.dumps(execution, indent=2, sort_keys=True) + '\n')
    return census, execution


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--official', type=Path, required=True)
    p.add_argument('--repository', type=Path, required=True)
    p.add_argument('--census', type=Path, required=True)
    p.add_argument('--execution', type=Path, required=True)
    x = p.parse_args()
    c, e = run(x.official, x.repository, x.census, x.execution)
    print(json.dumps({'counts': c['counts'], 'profile': e['owl2_dl_profile_pass'], 'violations': e['profile_violation_count']}, sort_keys=True))
