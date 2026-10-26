"""Inventory every explicitly declared entity in one retained OWL document.

No imports, inference, profile test, semantic acceptance or source redistribution.
Requires requirements-research.txt. Annotations are counted, not copied wholesale.
"""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import rdflib
from rdflib import BNode, Graph, Literal, OWL, RDF, RDFS, URIRef
from rdflib.compare import to_canonical_graph


def inventory(source, expected_sha):
    raw = Path(source).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != expected_sha:
        raise ValueError('Retained artifact digest differs from the selected input')
    graph = to_canonical_graph(Graph().parse(data=raw, format='xml'))
    annotations = {RDFS.comment, RDFS.label, RDFS.seeAlso, OWL.versionInfo}
    kinds = {'classes': OWL.Class, 'object_properties': OWL.ObjectProperty,
             'datatype_properties': OWL.DatatypeProperty,
             'annotation_properties': OWL.AnnotationProperty,
             'named_individuals': OWL.NamedIndividual}

    def expression(node, seen=frozenset()):
        if isinstance(node, URIRef):
            return {'iri': str(node)}
        if isinstance(node, Literal):
            return {'literal': str(node), 'datatype': str(node.datatype) if node.datatype else None,
                    'language': node.language}
        if node in seen:
            return {'cycle': True}
        return {'anonymous_expression': [
            {'predicate': str(p), 'object': expression(o, seen | {node})}
            for p, o in sorted(graph.predicate_objects(node), key=lambda pair: tuple(map(str, pair)))
            if p not in annotations]}

    result = {}
    for name, kind in kinds.items():
        result[name] = []
        for entity in sorted({s for s in graph.subjects(RDF.type, kind) if isinstance(s, URIRef)}, key=str):
            result[name].append({'iri': str(entity),
                'declarations_and_constraints': [
                    {'predicate': str(p), 'object': expression(o)}
                    for p, o in sorted(graph.predicate_objects(entity), key=lambda pair: tuple(map(str, pair)))
                    if p not in annotations],
                'annotation_triples_not_copied': sum(p in annotations for p, _ in graph.predicate_objects(entity))})
    result.update(schema_version='1.0', source_sha256=digest,
        generator={'path': 'tools/inventory_review_artifact.py',
                   'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   'python': platform.python_version(), 'rdflib': rdflib.__version__},
        source_syntax='RDF/XML', explicit_triples=len(graph),
        declared_import_iris=sorted(map(str, graph.objects(None, OWL.imports))),
        ontology_iris=sorted(str(s) for s in graph.subjects(RDF.type, OWL.Ontology) if isinstance(s, URIRef)),
        counts={name: len(result[name]) for name in kinds},
        anonymous_restrictions=len(set(graph.subjects(RDF.type, OWL.Restriction))),
        scope='All explicitly declared named entities and their outgoing constraints in this one document; annotation text excluded. This is not all entities of an unacquired paper version or all inferred consequences.',
        reasoner_execution='NOT_EXECUTED', semantic_acceptance='NOT_ASSESSED',
        source_redistributed=False, import_resolution='NO_NETWORK_IMPORTS',
        inference_counts=None)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True, type=Path)
    parser.add_argument('--expected-sha256', required=True)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    report = inventory(args.source, args.expected_sha256)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'explicit_triples': report['explicit_triples'], 'counts': report['counts'],
                      'source_sha256': report['source_sha256'], 'reasoner_execution': report['reasoner_execution']}))
