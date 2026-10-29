"""Inspect pinned BDI research inputs, never silently fetch or repair them.

Third-party files stay outside the repository. Outputs separate RDF census,
asserted SPARQL execution, OWL profile and isolated HermiT cases. This program
does not modify Clariceptify's model or execute paid/application APIs.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import platform
import re
import subprocess
import time
import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'evidence/related-work/corpus/bdi2026-inputs.yaml'
CORE = 'bdi/bdi.ttl'
ALIGN = 'bdi-dul/bdi-dul.rdf'
NS = 'https://w3id.org/fossr/ontology/bdi/'
D0 = 'http://www.ontologydesignpatterns.org/ont/d0.owl#'
DUL = 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def stable(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def sources(folder):
    manifest = yaml.safe_load((ROOT / MANIFEST).read_text())
    inputs = {}
    for spec in manifest['artifacts']:
        path = Path(folder) / spec['filename']
        raw = path.read_bytes()
        if sha(raw) != spec['sha256']:
            raise ValueError('Source digest mismatch: ' + spec['id'])
        inputs[spec['id']] = (raw, spec)
    return inputs


def graph(raw, fmt='turtle'):
    from rdflib import Graph
    from rdflib.compare import to_canonical_graph
    return to_canonical_graph(Graph().parse(data=raw, format=fmt))


def expression(g, n, seen=frozenset()):
    from rdflib import URIRef, Literal, RDFS
    if isinstance(n, URIRef):
        return {'iri': str(n)}
    if isinstance(n, Literal):
        return {'literal': str(n), 'language': n.language,
                'datatype': str(n.datatype) if n.datatype else None}
    if n in seen:
        return {'cycle': True}
    return {'anonymous_expression': [
        {'predicate': str(p), 'object': expression(g, o, seen | {n})}
        for p, o in sorted(g.predicate_objects(n), key=lambda x: tuple(map(str, x)))
        if p not in [RDFS.comment, RDFS.label]]}


def census(g, spec, namespace):
    from rdflib import URIRef, BNode, RDF, RDFS, OWL, XSD
    declared = {s for k in [OWL.Class, RDFS.Class]
                for s in g.subjects(RDF.type, k) if isinstance(s, URIRef)}
    references = set()
    for s, p, o in g:
        if p in [RDFS.subClassOf, OWL.equivalentClass, OWL.disjointWith,
                 OWL.complementOf, OWL.onClass, OWL.someValuesFrom, OWL.allValuesFrom,
                 RDFS.domain] and isinstance(o, URIRef):
            references.add(o)
        if p == RDFS.range and (s, RDF.type, OWL.ObjectProperty) in g and isinstance(o, URIRef):
            references.add(o)
        if p in [RDFS.subClassOf, OWL.equivalentClass, OWL.disjointWith] and isinstance(s, URIRef):
            references.add(s)
        if p in [OWL.unionOf, OWL.intersectionOf, OWL.members]:
            if p != OWL.members or (s, RDF.type, OWL.AllDisjointClasses) in g:
                references.update(x for x in g.items(o) if isinstance(x, URIRef))
    builtin = {x for x in references | declared
               if str(x).startswith(tuple(map(str, [RDF, RDFS, OWL, XSD])))}
    rows = []
    for index, c in enumerate(sorted(declared, key=str), 1):
        annotations = []
        for p in [RDFS.comment, URIRef('http://www.w3.org/2004/02/skos/core#definition')]:
            for o in sorted(g.objects(c, p), key=str):
                annotations.append({'predicate': str(p), 'text_sha256': sha(str(o).encode()),
                                    'characters': len(str(o)), 'language': o.language})
        labels = sorted(str(x) for x in g.objects(c, RDFS.label)
                        if x.language in ['en', None])
        constraints = [{'predicate': str(p), 'object': expression(g, o)}
                       for p, o in sorted(g.predicate_objects(c), key=lambda x: tuple(map(str, x)))
                       if p in [RDFS.subClassOf, OWL.equivalentClass, OWL.disjointWith]]
        # Preserve incoming disjoint/equivalence and n-ary disjoint memberships too.
        related = [{'subject': str(s), 'predicate': str(p)}
                   for p in [OWL.disjointWith, OWL.equivalentClass]
                   for s in sorted(g.subjects(p, c), key=str) if isinstance(s, URIRef)]
        groups = [sorted(map(str, g.items(g.value(n, OWL.members))))
                  for n in g.subjects(RDF.type, OWL.AllDisjointClasses)
                  if c in set(g.items(g.value(n, OWL.members)))]
        rows.append(dict(iri=str(c), label=labels[0] if labels else re.split(r'[/#]', str(c))[-1],
                         label_basis='SOURCE_LABEL' if labels else 'IRI_LOCAL_NAME',
                         module=spec['id'], source_sha256=spec['sha256'],
                         population='LOCAL_DECLARED_NAMED_CLASS' if str(c).startswith(namespace)
                         else 'EXTERNAL_DECLARATION',
                         deprecated=any(str(v).lower() in ['true', '1'] for v in g.objects(c, OWL.deprecated)),
                         annotation_records=annotations,
                         named_superclasses=sorted(str(x) for x in g.objects(c, RDFS.subClassOf) if isinstance(x, URIRef)),
                         equivalent_expressions=[expression(g, x) for x in sorted(g.objects(c, OWL.equivalentClass), key=str)],
                         constraint_ref=f"{spec['id']}:C{index:03d}", constraints=constraints,
                         related_axioms=related, all_disjoint_groups=groups,
                         constraint_sha256=stable([constraints, related, groups])))
    return dict(source_sha256=spec['sha256'], explicit_triples=len(g),
                ontology_iris=sorted(map(str, g.subjects(RDF.type, OWL.Ontology))),
                imports=sorted(map(str, g.objects(None, OWL.imports))),
                version_iris=sorted(map(str, g.objects(None, OWL.versionIRI))),
                declared_named_class_iris=sorted(map(str, declared)),
                local_class_iris=sorted(str(x) for x in declared if str(x).startswith(namespace)),
                external_class_iris=sorted(str(x) for x in declared if not str(x).startswith(namespace)),
                referenced_undeclared_nonbuiltin_class_iris=sorted(map(str, references - declared - builtin)),
                builtin_class_references=sorted(map(str, builtin)),
                anonymous_class_expressions=len({x for k in [OWL.Class, OWL.Restriction]
                    for x in g.subjects(RDF.type, k) if isinstance(x, BNode)}),
                deprecated_class_iris=[r['iri'] for r in rows if r['deprecated']],
                object_properties=sorted(map(str, g.subjects(RDF.type, OWL.ObjectProperty))),
                datatype_properties=sorted(map(str, g.subjects(RDF.type, OWL.DatatypeProperty))),
                property_axioms=[{'iri': str(p), 'axioms': [
                    {'predicate': str(q), 'object': expression(g, o)}
                    for q, o in sorted(g.predicate_objects(p), key=lambda x: tuple(map(str, x)))
                    if q in [RDF.type, RDFS.domain, RDFS.range, RDFS.subPropertyOf,
                             OWL.inverseOf, OWL.equivalentProperty, OWL.propertyChainAxiom]]}
                    for p in sorted(set(g.subjects(RDF.type, OWL.ObjectProperty)) |
                                    set(g.subjects(RDF.type, OWL.DatatypeProperty)), key=str)],
                classes=rows)


def receipt(mode):
    import rdflib
    return dict(schema_version='1.0', issue=250, mode=mode,
                generator_path='tools/inspect_bdi2026.py',
                generator_sha256=sha(Path(__file__).read_bytes()),
                python=platform.python_version(), rdflib=rdflib.__version__,
                source_manifest_sha256=sha((ROOT / MANIFEST).read_bytes()),
                model_change='NONE', source_redistributed=False)


def inspect(folder):
    from rdflib import RDF, RDFS, OWL, URIRef
    from rdflib.compare import isomorphic
    inputs = sources(folder)
    chosen = [(CORE, 'turtle', NS), (ALIGN, 'xml', NS), ('d0', 'xml', D0), ('DUL', 'turtle', DUL)]
    records = {}
    for ident, fmt, ns in chosen:
        raw, spec = inputs[ident]
        records[ident] = census(graph(raw, fmt), spec, ns)
    # Same graph in alternate serialization; do not add its classes a second time.
    iso = isomorphic(graph(inputs[CORE][0]), graph(inputs['bdi/bdi.rdf'][0], 'xml'))
    older = graph(inputs['bdi.ttl'][0])
    out = receipt('STRUCTURAL_CENSUS_NOT_REASONING')
    out.update(modules=records, core_serialization_isomorphic=iso,
               older_root=dict(ontology_iris=sorted(map(str, older.subjects(RDF.type, OWL.Ontology))),
                               version_iris=sorted(map(str, older.objects(None, OWL.versionIRI))),
                               source_sha256=inputs['bdi.ttl'][1]['sha256'],
                               substitution_for_0_3='NOT_JUSTIFIED'),
               alignment_import_closure='BLOCKED_EXACT_BDI_0_3_HTTP404',
               acquired_foundation_closure=['d0', 'DUL'],
               foundation_unique_declared_classes=len(set(records['d0']['declared_named_class_iris']) |
                                                     set(records['DUL']['declared_named_class_iris'])),
               inferred_classes=None)
    return out


def bindings(data):
    def term(t):
        # RDFLib normalizes valid xsd:dateTime lexical forms. Compare typed values,
        # not serialization spelling; record this convention explicitly.
        from rdflib import Literal, URIRef
        if t['type'] == 'uri':
            return str(URIRef(t['value']))
        return Literal(t['value'], lang=t.get('xml:lang'), datatype=t.get('datatype')).n3()
    return sorted(json.dumps({k: term(v) for k, v in row.items()}, sort_keys=True)
                  for row in data['results']['bindings'])


def run_cqs(folder):
    from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef
    inputs = sources(folder)
    core = graph(inputs[CORE][0])
    unit = Namespace('https://w3id.org/OWLunit/ontology/')
    tests = sorted(core.subjects(RDF.type, unit.CompetencyQuestionVerification),
                   key=lambda x: int(str(x).rsplit('-', 1)[-1]))
    paper = yaml.safe_load((ROOT / 'evidence/related-work/deep-reviews/BDI2026Preprint/review.yaml').read_text())
    paper_cqs = {x['label']: x for x in paper['catalog'] if x.get('kind') == 'COMPETENCY_QUESTION'}
    rows = []
    for dataset in ['bdi/data-unit-testing.ttl', 'bdi-tests/bdi-tests.ttl']:
        data = graph(inputs[dataset][0])
        union = core + data
        for t in tests:
            number = int(str(t).rsplit('-', 1)[-1])
            query = str(core.value(t, unit.hasSPARQLUnitTest))
            expected_raw = str(core.value(t, unit.hasExpectedResult))
            expected = json.loads(expected_raw)
            start = time.monotonic()
            observed = json.loads(union.query(query).serialize(format='json'))
            exp, obs = bindings(expected), bindings(observed)
            raw_query_iris = set(re.findall(r'PREFIX\s+\w+:\s*<([^>]+)>', query))
            rows.append(dict(test_iri=str(t), cq='CQ' + str(number),
                             paper_evidence=paper_cqs['CQ' + str(number)]['id'],
                             question_sha256=sha(str(core.value(t, unit.hasCompetencyQuestion)).encode()),
                             dataset=dataset, dataset_sha256=inputs[dataset][1]['sha256'],
                             declared_input_iri=str(core.value(t, unit.hasInputData)),
                             declared_ontology_iri=str(core.value(t, unit.testsOntology)),
                             query_sha256=sha(query.encode()), expected_literal_sha256=sha(expected_raw.encode()),
                             result_sha256=stable(observed), expected_rows=len(exp), observed_rows=len(obs),
                             expected_binding_sha256=stable(exp), observed_binding_sha256=stable(obs),
                             missing_expected_rows=len([x for x in exp if x not in obs]),
                             extra_observed_rows=len([x for x in obs if x not in exp]),
                             expected_equal_observed=exp == obs,
                             result='MATCH' if exp == obs else 'MISMATCH',
                             seconds=round(time.monotonic() - start, 4),
                             declared_prefix_iris=sorted(raw_query_iris)))
    out = receipt('ASSERTED_GRAPH_SPARQL_EXECUTION')
    out.update(core_sha256=inputs[CORE][1]['sha256'], documented_tests=len(tests),
               paper_cqs=len(paper_cqs), executions=rows,
               summary=dict(total=len(rows), matches=sum(r['result'] == 'MATCH' for r in rows),
                            mismatches=sum(r['result'] == 'MISMATCH' for r in rows)),
               comparison_policy='Exact variable-name/binding multiset comparison after RDFLib typed-literal normalization; row order ignored. No query, data, namespace, expected-result or source repair.',
               entailment='NONE: asserted union of exact core and one exact dataset per run',
               owlunit_engine='NOT_EXECUTED; annotations interpreted by this declared RDFLib harness',
               logical_validation='NOT_CLAIMED: successful query evaluation is distinct from consistency and CQ adequacy')
    return out


def fixtures():
    from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal, BNode, XSD
    B = Namespace(NS)
    T = Namespace('urn:clariceptify:bdi250:')
    rows = []
    def typ(g, n, *cs):
        for c in cs:
            g.add((T[n], RDF.type, B[c]))
    def edge(g, a, p, b):
        g.add((T[a], B[p], T[b]))
    def empty(g, n, p):
        r = BNode(); g.add((T[n], RDF.type, r)); g.add((r, RDF.type, OWL.Restriction))
        g.add((r, OWL.onProperty, B[p])); g.add((r, OWL.allValuesFrom, OWL.Nothing))
    def neg(g, a, p, b):
        n = BNode(); g.add((n, RDF.type, OWL.NegativePropertyAssertion))
        g.add((n, OWL.sourceIndividual, T[a])); g.add((n, OWL.assertionProperty, B[p])); g.add((n, OWL.targetIndividual, T[b]))
    def case(ident, q, expected, description, fn):
        g = Graph(); fn(g); rows.append((ident, q, expected, description, g))
    case('baseline', 'Q02', True, 'Exact core0.5, including embedded test annotations', lambda g: None)
    case('belief-instance', 'Q03', True, 'Belief may exist with anonymous required witnesses', lambda g: typ(g, 'b', 'Belief'))
    case('belief-no-desire', 'Q03', False, 'Belief cannot deny all motivating-desire witnesses', lambda g: (typ(g, 'b', 'Belief'), empty(g, 'b', 'motivates')))
    case('belief-no-support', 'Q03', True, 'Unlike printed axiom35, core does not require a support edge', lambda g: (typ(g, 'b', 'Belief'), empty(g, 'b', 'supports')))
    case('belief-two-distinct-owners', 'Q03', False, 'Core qualified ownership cardinality is exactly one Agent', lambda g: (typ(g, 'b', 'Belief'), typ(g, 'a', 'Agent'), typ(g, 'z', 'Agent'), edge(g, 'b', 'isBeliefOf', 'a'), edge(g, 'b', 'isBeliefOf', 'z'), g.add((T.a, OWL.differentFrom, T.z))))
    case('motivation-distinct-owners', 'Q03', True, 'Motivation does not force Belief and Desire to share their owner', lambda g: (typ(g, 'b', 'Belief'), typ(g, 'd', 'Desire'), edge(g, 'b', 'motivates', 'd'), edge(g, 'b', 'isBeliefOf', 'a'), edge(g, 'd', 'isDesireOf', 'z'), g.add((T.a, OWL.differentFrom, T.z))))
    case('desire-same-type-part', 'Q04', True, 'Same-type desire part is allowed', lambda g: (typ(g, 'a', 'Desire'), typ(g, 'b', 'Desire'), edge(g, 'a', 'hasPart', 'b')))
    case('desire-belief-part', 'Q04', False, 'Desire-only parts conflict with explicit Belief and disjointness', lambda g: (typ(g, 'a', 'Desire'), typ(g, 'b', 'Belief'), edge(g, 'a', 'hasPart', 'b')))
    case('desire-intention-part', 'Q04', False, 'Desire-only parts conflict with explicit Intention and disjointness', lambda g: (typ(g, 'a', 'Desire'), typ(g, 'b', 'Intention'), edge(g, 'a', 'hasPart', 'b')))
    case('mentalentity-no-atTime', 'Q05', True, 'Printed axiom77 existential is absent from core MentalEntity', lambda g: (typ(g, 'm', 'MentalEntity'), empty(g, 'm', 'atTime')))
    case('mentalentity-no-validity', 'Q05', False, 'Core retains existential hasValidity', lambda g: (typ(g, 'm', 'MentalEntity'), empty(g, 'm', 'hasValidity')))
    case('generation-time-not-propagated', 'Q05', True, 'Generating process time is not automatically copied to generated Belief', lambda g: (typ(g, 'p', 'BeliefProcess'), typ(g, 'b', 'Belief'), edge(g, 'p', 'generates', 'b'), edge(g, 'p', 'atTime', 't'), neg(g, 'b', 'atTime', 't')))
    case('instant-without-value', 'Q05', True, 'Max-one date value does not require a value', lambda g: (typ(g, 't', 'TimeInstant'), empty(g, 't', 'time')))
    case('interval-no-start', 'Q05', False, 'Exactly-one start creates an existential obligation', lambda g: (typ(g, 'i', 'TimeInterval'), empty(g, 'i', 'hasStartTime')))
    case('interval-open-end', 'Q05', True, 'An absent end is allowed', lambda g: (typ(g, 'i', 'TimeInterval'), empty(g, 'i', 'hasEndTime')))
    case('interval-two-distinct-starts', 'Q05', False, 'Two distinct starts violate qualified cardinality', lambda g: (typ(g, 'i', 'TimeInterval'), edge(g, 'i', 'hasStartTime', 'a'), edge(g, 'i', 'hasStartTime', 'b'), g.add((T.a, OWL.differentFrom, T.b))))
    case('interval-two-names-can-merge', 'Q05', True, 'No unique-name assumption; starts may identify', lambda g: (typ(g, 'i', 'TimeInterval'), edge(g, 'i', 'hasStartTime', 'a'), edge(g, 'i', 'hasStartTime', 'b')))
    case('interval-reversed-values', 'Q05', True, 'Date ranges/cardinality do not impose start-before-end', lambda g: (typ(g, 'i', 'TimeInterval'), edge(g, 'i', 'hasStartTime', 'a'), edge(g, 'i', 'hasEndTime', 'b'), g.add((T.a, B.time, Literal('2026-10-29T12:00:00', datatype=XSD.dateTime))), g.add((T.b, B.time, Literal('2026-10-28T12:00:00', datatype=XSD.dateTime)))))
    case('plan-without-parts', 'Q06', False, 'Reflexive hasPart alone forces a Plan self-part', lambda g: (typ(g, 'p', 'Plan'), empty(g, 'p', 'hasPart')))
    case('plan-no-distinct-part', 'Q06', True, 'hasPart may be satisfied by the Plan itself, with no distinct part', lambda g: (typ(g, 'p', 'Plan'), g.add((T.p, RDF.type, (r := BNode()))), g.add((r, RDF.type, OWL.Restriction)), g.add((r, OWL.onProperty, B.hasPart)), g.add((r, OWL.allValuesFrom, (o := BNode()))), g.add((o, RDF.type, OWL.Class)), g.add((o, OWL.oneOf, (lst := BNode()))), g.add((lst, RDF.first, T.p)), g.add((lst, RDF.rest, RDF.nil))))
    case('plan-no-components', 'Q06', True, 'Paper axiom53 some Task component is not a core existential', lambda g: (typ(g, 'p', 'Plan'), empty(g, 'p', 'hasComponent')))
    case('plan-no-execution', 'Q06', True, 'Plan does not require execution/success', lambda g: (typ(g, 'p', 'Plan'), empty(g, 'p', 'isSatisfiedBy')))
    case('precedence-cycle', 'Q06', True, 'Transitive order allows cycles', lambda g: (typ(g, 'a', 'Task'), typ(g, 'b', 'Task'), edge(g, 'a', 'precedes', 'b'), edge(g, 'b', 'precedes', 'a')))
    case('precedence-no-shortcut', 'Q06', False, 'Transitive precedence forces the shortcut', lambda g: (edge(g, 'a', 'precedes', 'b'), edge(g, 'b', 'precedes', 'c'), neg(g, 'a', 'precedes', 'c')))
    case('task-branching', 'Q06', True, 'Two distinct next tasks are allowed', lambda g: (typ(g, 'a', 'Task'), edge(g, 'a', 'precedes', 'b'), edge(g, 'a', 'precedes', 'c'), g.add((T.b, OWL.differentFrom, T.c))))
    case('modification-edge', 'Q08', False, 'Two explicit modifies domains force its subject into disjoint MentalState and MentalProcess', lambda g: edge(g, 'p', 'modifies', 'm'))
    case('intention-no-plan', 'Q06', True, 'Core does not require intention specifies some Plan', lambda g: (typ(g, 'i', 'Intention'), empty(g, 'i', 'specifies')))
    case('fulfils-alias-not-equivalent', 'Q08', True, 'Author fixture spelling fulfils is not declared equivalent to core fulfills', lambda g: (typ(g, 'i', 'Intention'), typ(g, 'd', 'Desire'), edge(g, 'i', 'fulfils', 'd'), neg(g, 'i', 'fulfills', 'd')))
    return rows


def reason(folder, private):
    from rdflib import Graph, Namespace, RDF, OWL, URIRef
    from rdflib.compare import to_canonical_graph
    import jpype
    import owlready2
    inputs = sources(folder)
    base = graph(inputs[CORE][0])
    private = Path(private).resolve(); private.mkdir(parents=True, exist_ok=True)
    jar = Path(owlready2.__file__).parent / 'hermit/HermiT.jar'
    if not jpype.isJVMStarted():
        jpype.startJVM(classpath=[str(jar)])
    J = jpype.JClass
    manager_class = J('org.semanticweb.owlapi.apibinding.OWLManager')
    profile_class = J('org.semanticweb.owlapi.profiles.OWL2DLProfile')
    file_class = J('java.io.File')
    reasoner_class = J('org.semanticweb.HermiT.Reasoner')
    def load(raw, ident):
        # Retain the exact primary Turtle byte order, then append isolated fixture
        # triples. This also avoids serializer-order ambiguity in an already
        # profile-invalid source's reserved rdf:type annotation declaration.
        p = private / (ident + '.ttl'); p.write_bytes(raw)
        m = manager_class.createOWLOntologyManager()
        return m, m.loadOntologyFromOntologyDocument(file_class(str(p)))
    manager, ontology = load(inputs[CORE][0], 'core-profile')
    profile = profile_class().checkOntology(ontology)
    violations = sorted(str(x) for x in profile.getViolations())
    axiom_metrics = dict(axioms=int(ontology.getAxiomCount()), logical_axioms=int(ontology.getLogicalAxiomCount()),
                        signature_classes=len(ontology.getClassesInSignature()),
                        signature_object_properties=len(ontology.getObjectPropertiesInSignature()),
                        signature_data_properties=len(ontology.getDataPropertiesInSignature()),
                        signature_individuals=len(ontology.getIndividualsInSignature()))
    r = reasoner_class(ontology)
    baseline_consistent = bool(r.isConsistent())
    unsat = sorted(str(c.getIRI()) for c in r.getUnsatisfiableClasses().getEntitiesMinusBottom()) if baseline_consistent else None
    r.dispose(); manager.removeOntology(ontology)
    tests = []
    for ident, q, expected, description, fixture in fixtures():
        # Whole exact core is retained. No alignment/core0.3 substitution.
        nt = '\n'.join(sorted(to_canonical_graph(fixture).serialize(format='nt').splitlines())) + '\n'
        if not len(fixture):
            nt = ''
        combined = inputs[CORE][0] if not nt else inputs[CORE][0] + b'\n' + nt.encode()
        m, o = load(combined, ident)
        start = time.monotonic(); observed = None; error = None
        try:
            rr = reasoner_class(o)
            observed = bool(rr.isConsistent()); rr.dispose()
        except Exception as exc:
            error = type(exc).__name__ + ': ' + str(exc)[:1600]
        tests.append(dict(id=ident, question=q, description=description, fixture_nt=nt,
                          fixture_sha256=sha(nt.encode()), loaded_turtle_sha256=sha(combined),
                          expected_consistent=expected,
                          observed_consistent=observed, error=error,
                          result='PASS' if observed is expected else 'ERROR' if error else 'FAIL',
                          seconds=round(time.monotonic() - start, 4)))
        m.removeOntology(o)
        print(ident, tests[-1]['result'], observed, flush=True)
    for name in ['bdi/data-unit-testing.ttl', 'bdi-tests/bdi-tests.ttl']:
        ident = name.replace('/', '-').replace('.', '-')
        combined = inputs[CORE][0] + b'\n' + inputs[name][0]
        m, o = load(combined, ident); rr = reasoner_class(o)
        value = bool(rr.isConsistent()); rr.dispose(); m.removeOntology(o)
        tests.append(dict(id=ident, question='Q04', description='Whole exact author dataset plus core0.5; no data repair',
                          source_dataset=name, source_dataset_sha256=inputs[name][1]['sha256'],
                          loaded_turtle_sha256=sha(combined),
                          expected_consistent=False, observed_consistent=value, error=None,
                          result='PASS' if value is False else 'FAIL'))
    out = receipt('OWLAPI_PROFILE_AND_HERMIT_EXECUTION')
    out.update(core_sha256=inputs[CORE][1]['sha256'], core_profile_in_OWL2_DL=bool(profile.isInProfile()),
               core_profile_violations=violations, core_consistent=baseline_consistent,
               unsatisfiable_core_classes=unsat, owlapi_metrics=axiom_metrics,
               jpype=importlib.metadata.version('JPype1'), owlready2=importlib.metadata.version('owlready2'),
               hermit_version='1.3.8.1099 (bundled jar manifest)', hermit_jar_sha256=sha(jar.read_bytes()),
               input_serialization='Exact primary core Turtle bytes; add only each isolated canonical NTriples fixture or unchanged author Turtle dataset. No core reserialization, axiom deletion, prefix repair or implicit imports.',
               java_version=subprocess.run(['java', '-version'], capture_output=True, text=True).stderr.strip(),
               tests=tests, summary=dict(total=len(tests), passed=sum(t['result'] == 'PASS' for t in tests),
                                        failed=sum(t['result'] == 'FAIL' for t in tests), errors=sum(t['result'] == 'ERROR' for t in tests)),
               profile_reasoner_boundary='Exact raw core is outside OWL2 DL because rdf:type is declared an annotation property. OWLAPI accepts it; HermiT outcomes concern its loaded logical axioms, not a DL-conformance certificate.',
               exact_alignment_reasoning='BLOCKED_MISSING_BDI_0_3; no import stripping or0.5 substitution',
               application_reproduction='NOT_EXECUTED; no API/LLM/SEMAS calls',
               inferred_population='No all-inferred-class population claimed; unsatisfiable named classes only')
    jpype.shutdownJVM()
    return out


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('mode', choices=['census', 'cqs', 'reason'])
    p.add_argument('--source-dir', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--private-dir', type=Path)
    a = p.parse_args()
    if a.mode == 'reason' and a.private_dir is None:
        p.error('--private-dir is required for reason')
    data = inspect(a.source_dir) if a.mode == 'census' else run_cqs(a.source_dir) if a.mode == 'cqs' else reason(a.source_dir, a.private_dir)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    print(json.dumps(data.get('summary', {'modules': list(data.get('modules', {}))})))
