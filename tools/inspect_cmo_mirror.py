"""Inventory one pinned third-party CMO N3 candidate; no imports or inference."""
import argparse
import hashlib
import json
import platform
from pathlib import Path
import rdflib
from rdflib import Graph, Literal, URIRef, RDF, RDFS, OWL
from rdflib.compare import to_canonical_graph

NAMESPACE = 'http://purl.org/twc/ontologies/cmo.owl#'


def inspect(source, expected_sha):
    raw = source.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != expected_sha:
        raise ValueError('CMO mirror source substitution')
    graph = to_canonical_graph(Graph().parse(data=raw, format='n3'))
    annotations = {RDFS.comment, RDFS.label, RDFS.seeAlso, OWL.versionInfo}

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
            for p, o in sorted(graph.predicate_objects(node), key=lambda t: tuple(map(str, t)))
            if p not in annotations]}

    report = {}
    kinds = {'classes': OWL.Class, 'object_properties': OWL.ObjectProperty,
             'datatype_properties': OWL.DatatypeProperty,
             'annotation_properties': OWL.AnnotationProperty, 'named_individuals': OWL.NamedIndividual}
    for name, kind in kinds.items():
        rows = []
        for entity in sorted({s for s in graph.subjects(RDF.type, kind) if isinstance(s, URIRef)}, key=str):
            comments = sorted(str(x) for x in graph.objects(entity, RDFS.comment))
            other = sorted(str(x) for x in graph.objects(entity, RDFS.seeAlso) if isinstance(x, Literal))
            rows.append({'iri': str(entity), 'local': str(entity).startswith(NAMESPACE),
                         'labels': sorted(str(x) for x in graph.objects(entity, RDFS.label)),
                         'declarations_and_constraints': [
                             {'predicate': str(p), 'object': expression(o)}
                             for p, o in sorted(graph.predicate_objects(entity), key=lambda t: tuple(map(str, t)))
                             if p not in annotations],
                         'source_comment_count': len(comments),
                         'source_comment_sha256': hashlib.sha256(json.dumps(comments, separators=(',', ':')).encode()).hexdigest() if comments else None,
                         'seeAlso_literal_count': len(other),
                         'seeAlso_literal_sha256': hashlib.sha256(json.dumps(other, separators=(',', ':')).encode()).hexdigest() if other else None,
                         'annotation_triples_not_copied': sum(p in annotations for p, _ in graph.predicate_objects(entity))})
        report[name] = rows
    report.update(schema_version='1.0', checked_on='2026-10-27', source_sha256=digest,
                  source_syntax='N3', source_redistributed=False, explicit_triples=len(graph),
                  ontology_iris=sorted(str(x) for x in graph.subjects(RDF.type, OWL.Ontology)),
                  declared_import_iris=sorted(str(x) for x in graph.objects(None, OWL.imports)),
                  import_resolution='NOT_EXECUTED_HISTORICAL_IMPORTS_UNPINNED',
                  counts={name: len(report[name]) for name in kinds},
                  local_counts={name: sum(x['local'] for x in report[name]) for name in kinds},
                  anonymous_restrictions=len(set(graph.subjects(RDF.type, OWL.Restriction))),
                  generator={'path': 'tools/inspect_cmo_mirror.py',
                             'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                             'python': platform.python_version(), 'rdflib': rdflib.__version__},
                  provenance={'repository': 'dbpedia/ontology-tracker',
                              'commit': '32f457a42b910e39ef087b26f1664bd8d507518b',
                              'path': 'ontologies/purl.org/cmo/v2006/2006-06-30.n3',
                              'git_blob_sha': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest(),
                              'authority': 'THIRD_PARTY_MIRROR_NOT_AUTHOR_RELEASE',
                              'path_date_is_release_date': False, 'paper_2011_fidelity': 'NOT_ESTABLISHED',
                              'source_license': 'NOT_IDENTIFIED_IN_SELECTED_FILE'},
                  reasoner_execution='NOT_EXECUTED', inference_counts=None,
                  semantic_acceptance='NOT_ASSESSED', model_change='NONE',
                  scope='All explicit named declarations/constraints in one third-party candidate, not the complete original2011 ontology or imported/inferred populations.')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True, type=Path)
    parser.add_argument('--expected-sha256', required=True)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    data = inspect(args.source, args.expected_sha256)
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: data[k] for k in ['counts', 'local_counts', 'explicit_triples', 'anonymous_restrictions']}))
