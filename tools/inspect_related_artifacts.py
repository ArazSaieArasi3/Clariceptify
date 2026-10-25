"""Inspect hash-pinned third-party graphs without reasoning or implicit network imports.

Download the manifest URLs into an external source directory first. The .owl suffix
does not determine RDF syntax. Outputs contain inventories and selected logical
axioms, not redistributed source files or annotation corpora.
"""
from pathlib import Path
import argparse
import hashlib
import json

import rdflib
from rdflib import Graph, URIRef, BNode, Literal, RDF, RDFS, OWL
from rdflib.collection import Collection
from rdflib.compare import isomorphic
import yaml

ROOT = Path(__file__).resolve().parents[1]
LOGICAL = {RDF.type, RDFS.subClassOf, RDFS.subPropertyOf, RDFS.domain,
           RDFS.range, OWL.inverseOf, OWL.equivalentClass, OWL.disjointWith,
           OWL.onProperty, OWL.someValuesFrom, OWL.allValuesFrom,
           OWL.unionOf, OWL.intersectionOf, OWL.complementOf,
           OWL.minCardinality, OWL.maxCardinality, OWL.cardinality,
           OWL.propertyChainAxiom, OWL.hasValue, OWL.hasSelf}


def expression(graph, node, trail=()):
    if isinstance(node, URIRef):
        return str(node)
    if isinstance(node, Literal):
        return {'value': str(node), 'datatype': str(node.datatype) if node.datatype else None}
    if node in trail:
        raise ValueError('Cyclic anonymous expression')
    if (node, RDF.first, None) in graph:
        return [expression(graph, item, trail + (node,)) for item in Collection(graph, node)]
    rows = [{'predicate': str(p), 'object': expression(graph, o, trail + (node,))}
            for p, o in graph.predicate_objects(node) if p in LOGICAL]
    return sorted(rows, key=lambda row: json.dumps(row, sort_keys=True))


def inspect(source_dir, manifest_path=None):
    manifest = yaml.safe_load((manifest_path or ROOT / 'evidence/related-work/artifact-inputs.yaml').read_text())
    graphs = {}
    for spec in manifest['artifacts']:
        data = (source_dir / spec['filename']).read_bytes()
        if hashlib.sha256(data).hexdigest() != spec['sha256']:
            raise ValueError('Changed source bytes: ' + spec['id'])
        graph = Graph().parse(data=data, format=spec['format'], publicID=spec['url'])
        if set(map(str, graph.subjects(RDF.type, OWL.Ontology))) != {spec['ontology_iri']}:
            raise ValueError('Unexpected ontology identity: ' + spec['id'])
        graphs[spec['ontology_iri']] = graph
    results = {}
    for spec in manifest['artifacts']:
        graph = graphs[spec['ontology_iri']]
        ontology = URIRef(spec['ontology_iri'])
        declared = {s for s in graph.subjects(RDF.type, OWL.Class) if isinstance(s, URIRef)}
        local = {s for s in declared if str(s).startswith(spec['namespace'])}
        closure = Graph()
        pending, seen = [spec['ontology_iri']], set()
        while pending:
            iri = pending.pop()
            if iri in seen:
                continue
            seen.add(iri)
            if iri not in graphs:
                raise ValueError('Unpinned import: ' + iri)
            # Separate blank-node identities before unioning independent documents.
            current = graphs[iri]
            blanks = {}
            def renamed(term):
                if isinstance(term, BNode):
                    return blanks.setdefault(term, BNode())
                return term
            for triple in current:
                closure.add(tuple(renamed(term) for term in triple))
            pending.extend(map(str, current.objects(None, OWL.imports)))
        axioms = []
        for name in spec['selected_terms']:
            subject = URIRef(spec['namespace'] + name)
            if not list(graph.predicate_objects(subject)):
                raise ValueError('Missing inspected term: ' + name)
            rows = [{'predicate': str(p), 'object': expression(graph, o)}
                    for p, o in graph.predicate_objects(subject) if p in LOGICAL]
            axioms.append({'iri': str(subject), 'logical_assertions': sorted(rows, key=lambda r: json.dumps(r, sort_keys=True))})
        licenses = [{'predicate': str(p), 'value': str(o)} for p, o in graph.predicate_objects(ontology)
                    if any(part in str(p).lower() for part in ('license', 'rights'))]
        results[spec['id']] = {
            'schema_version': '1.0', 'artifact_id': spec['id'],
            'source_url': spec['url'], 'source_sha256': spec['sha256'],
            'syntax': spec['format'], 'ontology_iri': spec['ontology_iri'],
            'version_info': sorted({str(value).splitlines()[0] for value in graph.objects(ontology, OWL.versionInfo)
                                    if str(value) and str(value)[0].isdigit()}),
            'parser': {'name': 'RDFLib', 'version': rdflib.__version__},
            'counts': {'explicit_triples_local_document': len(graph),
                       'local_named_owl_classes': len(local),
                       'external_named_owl_classes_declared_in_document': len(declared - local),
                       'local_named_object_properties': len({s for s in graph.subjects(RDF.type, OWL.ObjectProperty) if isinstance(s, URIRef) and str(s).startswith(spec['namespace'])}),
                       'import_closure_named_owl_classes': len({s for s in closure.subjects(RDF.type, OWL.Class) if isinstance(s, URIRef)}),
                       'inferred_classes': None},
            'local_named_class_iris': sorted(map(str, local)),
            'imports': sorted(map(str, graph.objects(ontology, OWL.imports))),
            'resolved_closure': sorted(seen), 'license_annotations': sorted(licenses, key=lambda r: json.dumps(r, sort_keys=True)),
            'license_scope': 'Ontology-header license/rights annotations only; absent annotations do not grant redistribution.',
            'selected_axioms': axioms,
            'reasoner_execution': 'NOT_EXECUTED',
            'count_policy': 'Unique URI subjects explicitly typed owl:Class; local namespace filter; blank-node classes excluded. Import closure is asserted graph union, not inference.',
            'scope': 'Syntax, inventories and selected asserted axioms; no OWL profile, satisfiability, equivalence or paper-to-OWL fidelity proof.'}
    alias = manifest.get('alias_check')
    if not alias:
        return results
    data = (source_dir / alias['filename']).read_bytes()
    if hashlib.sha256(data).hexdigest() != alias['sha256']:
        raise ValueError('Changed alias bytes')
    graph = Graph().parse(data=data, format='xml', publicID=alias['url'])
    if not isomorphic(graph, graphs[alias['ontology_iri']]):
        raise ValueError('cDnS URL variants are not graph-isomorphic')
    results['cDnS']['alias_check'] = {**alias, 'rdf_isomorphic': True, 'byte_identical': False}
    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--manifest', type=Path)
    args = parser.parse_args()
    if args.source_dir.resolve().is_relative_to(ROOT):
        raise ValueError('Keep third-party source files outside the public repository')
    reports = inspect(args.source_dir, args.manifest)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for key, report in reports.items():
        (args.output_dir / (key + '.json')).write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status': 'PASS', 'reports': {k: r['counts'] for k, r in reports.items()}}, sort_keys=True))
