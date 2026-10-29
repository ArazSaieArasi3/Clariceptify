"""Reproduce a source-bound SKOS schema census without remote imports or entailment claims."""
from pathlib import Path
import argparse, hashlib, json
from rdflib import Graph, RDF, RDFS, OWL, URIRef, Namespace

ROOT = Path(__file__).resolve().parents[1]
PIN = 'e79633b8d0564816cee8a99f5c9acf9a0e6fc7257c7209acd684ecad53a89dd6'
SKOS = Namespace('http://www.w3.org/2004/02/skos/core#')
PREDICATES = (RDFS.subClassOf, OWL.equivalentClass, OWL.disjointWith)


def inspect(source):
    data = source.read_bytes()
    if hashlib.sha256(data).hexdigest() != PIN:
        raise ValueError('Selected SKOS RDF bytes differ from pinned corpus')
    graph = Graph().parse(data=data, format='xml')
    declared = {s for s in graph.subjects(RDF.type, OWL.Class) if isinstance(s, URIRef)}
    local = sorted((s for s in declared if str(s).startswith(str(SKOS))), key=str)
    external = sorted(declared - set(local), key=str)
    rows = []
    for cls in local + external:
        defs = [str(v) for v in graph.objects(cls, SKOS.definition)]
        comments = [str(v) for v in graph.objects(cls, RDFS.comment)]
        rows.append(dict(iri=str(cls), population='LOCAL' if cls in local else 'EXTERNAL_REDECLARED',
                         label=[str(v) for v in graph.objects(cls, RDFS.label)],
                         definition_candidates=defs, comment_candidates=comments,
                         definition_locator=f'SKOS.rdf::{cls} skos:definition' if defs else None,
                         paraphrase={'Concept':'An identifiable unit of thought; the RDF class itself does not identify an agent or mental episode.',
                                     'ConceptScheme':'A grouping of concepts that may carry their semantic relations.',
                                     'Collection':'A meaningful grouping of concepts, distinct from a concept.',
                                     'OrderedCollection':'A collection for which order has meaning.'}.get(str(cls).split('#')[-1]),
                         axioms={str(p).split('#')[-1]: sorted(str(o) for o in graph.objects(cls, p)) for p in PREDICATES},
                         deprecated=any(str(v).lower() == 'true' for v in graph.objects(cls, OWL.deprecated))))
    expected = {'Collection', 'Concept', 'ConceptScheme', 'OrderedCollection'}
    if {str(c).split('#')[-1] for c in local} != expected or external:
        raise ValueError('Unexpected class declaration census')
    selected = [
        ('S01', SKOS.OrderedCollection, RDFS.subClassOf, SKOS.Collection, 'Hierarchy asserted in RDF.'),
        ('S02', SKOS.ConceptScheme, OWL.disjointWith, SKOS.Concept, 'Explicit class disjointness.'),
        ('S03', SKOS.Collection, OWL.disjointWith, SKOS.Concept, 'Explicit class disjointness.'),
        ('S04', SKOS.broader, RDFS.subPropertyOf, SKOS.broaderTransitive, 'Hierarchy link propagates to transitive property.'),
        ('S05', SKOS.broaderTransitive, RDF.type, OWL.TransitiveProperty, 'Transitivity declared; no cycle prohibition.'),
        ('S06', SKOS.related, RDF.type, OWL.SymmetricProperty, 'Symmetry declared.'),
        ('S07', SKOS.exactMatch, RDF.type, OWL.TransitiveProperty, 'Transitivity declared for exactMatch; avoid treating closeMatch likewise.'),
        ('S08', SKOS.memberList, RDFS.domain, SKOS.OrderedCollection, 'Member-list domain asserted.')]
    checks = [dict(id=i, locator=f'SKOS.rdf::<{s}> <{p}> <{o}>', asserted=(s,p,o) in graph, reading=reading)
              for i,s,p,o,reading in selected]
    if not all(c['asserted'] for c in checks):
        raise ValueError('Selected source triple missing')
    types = {str(t).split('#')[-1]: len({s for s in graph.subjects(RDF.type,t) if isinstance(s,URIRef) and str(s).startswith(str(SKOS))}) for t in (OWL.ObjectProperty,OWL.DatatypeProperty,OWL.AnnotationProperty,RDF.Property)}
    referenced = {x for p in PREDICATES + (RDFS.domain,RDFS.range) for s,o in graph.subject_objects(p) for x in (s,o) if isinstance(x,URIRef) and str(x).startswith(str(SKOS)) and x not in declared}
    return dict(issue=238, source_sha256=PIN, source_bytes=len(data), source_url='https://www.w3.org/2009/08/skos-reference/skos.rdf', syntax='RDF/XML', triples=len(graph), ontology_imports=sorted(str(o) for o in graph.objects(None,OWL.imports)), population=dict(local_named_classes=len(local), external_redeclared_classes=len(external), imported_classes=0, inferred_classes=None, referenced_non_class_iris=sorted(map(str,referenced)), property_declarations=types, anonymous_owl_class_nodes=sum(1 for s in set(graph.subjects(RDF.type,OWL.Class)) if not isinstance(s,URIRef))), classes=rows, selected_assertions=checks, execution='RDF parse and explicit triple checks only; OWL profile, reasoner and recommendation-only integrity rules NOT_EXECUTED')

if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('source',type=Path);parser.add_argument('--output',type=Path,default=ROOT/'evaluation/related-work/skos238/census.json');args=parser.parse_args()
    result=inspect(args.source);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:result[k] for k in ('source_sha256','triples','population','execution')},indent=2))
