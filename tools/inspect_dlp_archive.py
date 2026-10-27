"""Read one pinned DLP3971 archive without imports, inference or source modification."""
from pathlib import Path
import argparse
import hashlib
import json
import platform
from zipfile import ZipFile
import rdflib
from rdflib import Graph, OWL, RDF, RDFS, URIRef


def inspect(source, expected_sha256):
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if digest != expected_sha256:
        raise ValueError('DLP archive source substitution')
    modules, union = [], Graph()
    with ZipFile(source) as archive:
        members = archive.infolist()
        if sum(i.file_size for i in members) > 20_000_000:
            raise ValueError('Archive exceeds bounded research intake')
        selected = sorted(i.filename for i in members if '/' not in i.filename and i.filename.endswith('.owl'))
        for name in selected:
            raw = archive.read(name)
            graph = Graph().parse(data=raw, format='xml')
            union += graph
            ontology_iris = sorted(str(x) for x in graph.subjects(RDF.type, OWL.Ontology) if isinstance(x, URIRef))
            if len(ontology_iris) != 1:
                raise ValueError('Ambiguous module ontology identity')
            namespace = ontology_iris[0] + '#'
            classes = sorted({str(x) for x in graph.subjects(RDF.type, OWL.Class) if isinstance(x, URIRef)})
            local = [x for x in classes if x.startswith(namespace)]
            modules.append({'filename': name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
                            'ontology_iri': ontology_iris[0], 'namespace': namespace,
                            'version_info': sorted(str(x).strip() for x in graph.objects(None, OWL.versionInfo)),
                            'declared_import_iris': sorted(str(x) for x in graph.objects(None, OWL.imports)),
                            'explicit_triples_document': len(graph),
                            'declared_named_owl_classes_all_namespaces': len(classes),
                            'local_named_owl_classes': len(local),
                            'external_named_class_redeclarations': len(classes) - len(local),
                            'declared_named_class_iris': classes,
                            'local_definition_candidates': [
                                {'iri': iri,
                                 'labels': sorted(str(x) for x in graph.objects(URIRef(iri), RDFS.label)),
                                 'comment_count': len(list(graph.objects(URIRef(iri), RDFS.comment))),
                                 'comment_sha256': hashlib.sha256(json.dumps(sorted(str(x) for x in graph.objects(URIRef(iri), RDFS.comment)), ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
                                 if list(graph.objects(URIRef(iri), RDFS.comment)) else None,
                                 'definition_review': 'PENDING', 'public_raw_comment_text': False}
                                for iri in local]})
        readme = archive.read('README.txt')
    mapping = {m['ontology_iri']: m for m in modules}
    root_iri = 'http://www.loa-cnr.it/ontologies/DLP_397.owl'
    visited, pending, unresolved = set(), [root_iri], set()
    while pending:
        iri = pending.pop()
        if iri in visited:
            continue
        if iri not in mapping:
            unresolved.add(iri)
            continue
        visited.add(iri)
        pending.extend(mapping[iri]['declared_import_iris'])
    kinds = {'named_owl_classes': OWL.Class, 'object_properties': OWL.ObjectProperty,
             'datatype_properties': OWL.DatatypeProperty, 'annotation_properties': OWL.AnnotationProperty}
    counts = {k: len({s for s in union.subjects(RDF.type, kind) if isinstance(s, URIRef)}) for k, kind in kinds.items()}
    return {'schema_version': '1.0', 'checked_on': '2026-10-27',
            'archive': {'filename': source.name, 'source_url': 'https://www.loa.istc.cnr.it/old/ontologies/DLP3971.zip',
                        'linked_from': 'https://www.loa.istc.cnr.it/dolce/overview.html',
                        'sha256': digest, 'bytes': source.stat().st_size,
                        'retained_filename': 'Clariceptify_DLP3971_Source_2026-10-27.zip',
                        'raw_source_publicly_copied': False},
            'generator': {'path': 'tools/inspect_dlp_archive.py',
                          'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                          'python': platform.python_version(), 'rdflib': rdflib.__version__},
            'module_population': len(modules), 'modules': modules,
            'readme': {'sha256': hashlib.sha256(readme).hexdigest(), 'copyright_year': 2005,
                       'license_statement': 'GNU LGPL version2.1 or later',
                       'author_reported_population': {'classes': 205, 'object_properties': 311,
                                                      'datatype_properties': 4, 'annotation_properties': 2,
                                                      'individuals': 39},
                       'reported_expressivity': 'SHION(D), within OWL-DL',
                       'basis': 'AUTHOR_REPORTED_NOT_REPRODUCED_AS_PROFILE_OR_REASONER_RESULT'},
            'asserted_archive_union': {'counts': counts, 'explicit_triples': len(union),
                                       'root_iri': root_iri, 'resolved_modules': sorted(visited),
                                       'unresolved_declared_imports': sorted(unresolved),
                                       'policy': 'Unique named declarations in the union of supplied modules. No inference; no sum of external redeclarations; no inferred individual count.'},
            'scope': 'Archive acquisition, RDF parsing, declared class/definition-comment availability and supplied import resolution only. All manual class definitions and semantic correspondence remain #235.',
            'historical_2003_fidelity': 'NOT_ESTABLISHED', 'paper_class_count': None,
            'reasoner_execution': 'NOT_EXECUTED', 'inferred_counts': None,
            'semantic_acceptance': 'NOT_ASSESSED', 'model_change': 'NONE'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True, type=Path)
    parser.add_argument('--expected-sha256', required=True)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    result = inspect(args.source, args.expected_sha256)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'modules': result['module_population'],
                      'asserted_union': result['asserted_archive_union'],
                      'historical_2003_fidelity': result['historical_2003_fidelity']}))
