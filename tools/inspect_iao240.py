"""Inspect the pinned 2026-03-30 IAO release root without fetching imports."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS, OWL, URIRef
from rdflib.collection import Collection

PIN = 'c27ff2964a2ad8165bc365698b628aae95108411384aa4450e6e1b1e82bf0f41'
OBO = Namespace('http://purl.obolibrary.org/obo/')
DEFINITION = OBO.IAO_0000115
ROOT = Path(__file__).resolve().parents[1]


def inspect(path):
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != PIN:
        raise ValueError(f'Unexpected IAO release bytes: {digest}')
    graph = Graph().parse(data=data, format='xml')

    def expression(node, depth=0):
        if isinstance(node, Literal):
            return str(node)
        if isinstance(node, URIRef):
            return str(node)
        if depth > 8:
            raise ValueError('Nested anonymous expression exceeds inspection bound')
        out = {}
        for pred in (OWL.intersectionOf, OWL.unionOf, OWL.oneOf, OWL.complementOf,
                     OWL.onProperty, OWL.someValuesFrom, OWL.allValuesFrom,
                     OWL.hasValue, OWL.minCardinality, OWL.maxCardinality,
                     OWL.cardinality, OWL.onClass, OWL.minQualifiedCardinality,
                     OWL.maxQualifiedCardinality, OWL.qualifiedCardinality):
            values = list(graph.objects(node, pred))
            if not values:
                continue
            key = str(pred).split('#')[-1]
            if pred in (OWL.intersectionOf, OWL.unionOf, OWL.oneOf):
                out[key] = [expression(item, depth + 1) for item in Collection(graph, values[0])]
            else:
                out[key] = [expression(v, depth + 1) for v in values]
        return out if out else {'unparsed_anonymous_expression': True}

    declared = {s for s in graph.subjects(RDF.type, OWL.Class) if isinstance(s, URIRef)}
    local = {s for s in declared if str(s).startswith(str(OBO) + 'IAO_')}
    external = declared - local
    rows = []
    for cls in sorted(declared, key=str):
        defs = [str(v) for v in graph.objects(cls, DEFINITION)]
        comments = [str(v) for v in graph.objects(cls, RDFS.comment)]
        label = [str(v) for v in graph.objects(cls, RDFS.label)]
        rows.append({
            'iri': str(cls), 'population': 'LOCAL_IAO_IRI' if cls in local else 'EXTERNAL_REDECLARED_IN_ROOT',
            'label': label, 'definition_state': 'PRESENT' if defs else ('COMMENT_ONLY' if comments else 'MISSING'),
            'source_definition': defs, 'source_comment': comments,
            'definition_locator': f'iao.owl::<{cls}> <{DEFINITION}>' if defs else None,
            'comment_locator': f'iao.owl::<{cls}> <{RDFS.comment}>' if comments else None,
            'gloss_boundary': 'Original source definition is retained verbatim with attribution; do not infer a new definition from the label.' if defs else 'No source definition in this root; any comment is not silently promoted to a definition.',
            'hierarchy': sorted((expression(o) for o in graph.objects(cls, RDFS.subClassOf)), key=str),
            'equivalence': sorted((expression(o) for o in graph.objects(cls, OWL.equivalentClass)), key=str),
            'disjoint_with': sorted((expression(o) for o in graph.objects(cls, OWL.disjointWith)), key=str),
            'deprecated': any(str(o).lower() == 'true' for o in graph.objects(cls, OWL.deprecated)),
        })

    # Asserted commitments only. No inferred entailments, profile or consistency claims.
    def check(identifier, subject, predicate, obj, reading):
        actual = (subject, predicate, obj) in graph
        if not actual:
            raise ValueError(f'Selected assertion missing: {identifier}')
        rendered_object = expression(obj) if isinstance(obj, BNode) else str(obj)
        return dict(id=identifier, subject=str(subject), predicate=str(predicate), object=rendered_object,
                    locator=f'iao.owl::<{subject}> <{predicate}> {rendered_object}', asserted=actual, reading=reading)

    ice, data_entity, document, bearer = (OBO.IAO_0000030, OBO.IAO_0000027,
                                          OBO.IAO_0000310, OBO.IAO_0000178)
    about = OBO.IAO_0000136
    restriction = next((o for o in graph.objects(ice, RDFS.subClassOf)
                        if isinstance(o, BNode) and (o, OWL.onProperty, about) in graph), None)
    if restriction is None or (restriction, OWL.someValuesFrom, OBO.BFO_0000001) not in graph:
        raise ValueError('ICE aboutness restriction missing')
    selected = [
        check('I01', ice, RDFS.subClassOf, OBO.BFO_0000031, 'ICE is placed under BFO generically dependent continuant.'),
        check('I02', ice, RDFS.subClassOf, restriction, 'ICE requires some is-about BFO entity in the source restriction; blank-node expression recorded in class row.'),
        check('I03', about, RDFS.domain, ice, 'The aboutness property has an ICE domain; it does not assert a separate cognitive intention.'),
        check('I04', data_entity, RDFS.subClassOf, ice, 'Data entity is placed below ICE.'),
        check('I05', document, RDFS.subClassOf, ice, 'Document is placed below ICE.'),
        check('I06', bearer, RDFS.subClassOf, OBO.BFO_0000040, 'Material information bearer is placed under BFO material entity.'),
        check('I07', OBO.RO_0000058, OWL.inverseOf, OBO.RO_0000059, 'Concretization relation and its inverse are asserted using RO IRIs.'),
        check('I08', OBO.IAO_0000223, OWL.deprecated, Literal(True), 'The represents property is obsolete in this release.'),
    ]
    hierarchy_targets = {o for cls in declared for pred in (RDFS.subClassOf, OWL.equivalentClass, OWL.disjointWith)
                         for o in graph.objects(cls, pred) if isinstance(o, URIRef) and o not in declared}
    ontology = next(graph.subjects(RDF.type, OWL.Ontology))
    counts = Counter(row['definition_state'] for row in rows if row['population'] == 'LOCAL_IAO_IRI')
    return {
        'issue': 240, 'source_attribution': 'Information Artifact Ontology contributors; source annotations retained under the release root CC-BY-4.0 license; https://github.com/information-artifact-ontology/IAO',
        'source': {'repository': 'information-artifact-ontology/IAO',
                              'commit': '3006aedacbf813ffd1d2ac15cda10766ca9ed388',
                              'path': 'iao.owl', 'sha256': digest, 'bytes': len(data),
                              'ontology_iri': str(ontology),
                              'version_iri': str(next(graph.objects(ontology, OWL.versionIRI))),
                              'syntax': 'RDF/XML', 'license': str(next(graph.objects(ontology, URIRef('http://purl.org/dc/terms/license'))))},
        'triples': len(graph), 'imports': sorted(str(o) for o in graph.objects(ontology, OWL.imports)),
        'population': {'named_classes': len(declared), 'local_iao_named_classes': len(local),
                       'external_redeclared_named_classes': len(external),
                       'anonymous_owl_class_nodes': len(set(graph.subjects(RDF.type, OWL.Class)) - declared),
                       'local_definition_states': dict(sorted(counts.items())),
                       'local_deprecated': sum(r['deprecated'] for r in rows if r['population'] == 'LOCAL_IAO_IRI'),
                       'external_prefixes': dict(sorted(Counter(str(x).rsplit('/', 1)[-1].split('_')[0] for x in external).items())),
                       'referenced_only_named_hierarchy_targets': sorted(map(str, hierarchy_targets)),
                       'imported_classes': 0, 'inferred_classes': None},
        'classes': rows, 'selected_commitments': selected,
        'execution': 'Exact SHA and RDF parse, full asserted-class census and eight explicit triple checks; no OWL profile, inference or consistency test executed.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    parser.add_argument('--output', type=Path, default=ROOT / 'evaluation/related-work/iao240/census.json')
    args = parser.parse_args()
    receipt = inspect(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'source': receipt['source'], 'triples': receipt['triples'],
                      'population': receipt['population'], 'selected': len(receipt['selected_commitments'])}, indent=2))
