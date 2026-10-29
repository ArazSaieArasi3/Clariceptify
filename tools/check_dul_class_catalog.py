"""Check the complete, source-pinned DUL glossary without treating it as semantic proof.

Default mode validates the public records. --source additionally re-parses the
private Turtle input and reconciles exact class/axiom/annotation populations.
No network access, imports, reasoning, or original annotation redistribution.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'evidence/related-work/dul-class-catalog.yaml'
NS = 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#'
SHA = 'e5f6429596d2c7014730bad85aaaa9c39530235f27f596cd0e7ce85e6bbcba66'


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()).hexdigest()


def inspect_source(path):
    import rdflib
    from rdflib import Graph, URIRef, Literal, BNode, RDF, RDFS, OWL, XSD
    from rdflib.compare import to_canonical_graph
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != SHA:
        raise ValueError('Selected source hash differs')
    g = to_canonical_graph(Graph().parse(data=raw, format='turtle'))
    declared = {s for kind in (OWL.Class, RDFS.Class) for s in g.subjects(RDF.type, kind) if isinstance(s, URIRef)}
    local = sorted((s for s in declared if str(s).startswith(NS)), key=str)
    excluded = {RDFS.label, RDFS.comment, RDFS.seeAlso, RDFS.isDefinedBy, OWL.versionInfo}

    def expr(n, seen=frozenset()):
        if isinstance(n, URIRef):
            return {'iri': str(n)}
        if isinstance(n, Literal):
            return {'literal': str(n), 'language': n.language, 'datatype': str(n.datatype) if n.datatype else None}
        if n in seen:
            return {'cycle': True}
        return {'anonymous_expression': [
            {'predicate': str(p), 'object': expr(o, seen | {n})}
            for p, o in sorted(g.predicate_objects(n), key=lambda v: tuple(map(str, v))) if p not in excluded]}

    # Only class-valued positions, excluding enumerated individuals and property lists.
    referenced = set()
    class_positions = {RDFS.subClassOf, OWL.equivalentClass, OWL.disjointWith,
                       OWL.complementOf, OWL.onClass, OWL.someValuesFrom, OWL.allValuesFrom}
    for s, p, o in g:
        if p in class_positions and isinstance(o, URIRef):
            referenced.add(o)
        if p in (RDFS.domain, RDFS.range) and isinstance(o, URIRef):
            if p == RDFS.domain or (s, RDF.type, OWL.ObjectProperty) in g:
                referenced.add(o)
        if p in (OWL.unionOf, OWL.intersectionOf, OWL.members):
            if p != OWL.members or (s, RDF.type, OWL.AllDisjointClasses) in g:
                referenced.update(n for n in g.items(o) if isinstance(n, URIRef))
    builtin = sorted(str(s) for s in referenced | declared if str(s).startswith((str(OWL), str(RDF), str(RDFS), str(XSD))))
    nonbuiltin_ref = {s for s in referenced if str(s) not in builtin}
    rows = []
    for i, c in enumerate(local, 1):
        labels = sorted((str(v) for v in g.objects(c, RDFS.label) if v.language == 'en'))
        comments = sorted(g.objects(c, RDFS.comment), key=lambda x: (x.language or '', str(x)))
        annotation_records = [{'predicate': str(RDFS.comment), 'language': v.language,
            'datatype': str(v.datatype) if v.datatype else None,
            'text_sha256': hashlib.sha256(str(v).encode()).hexdigest(),
            'characters': len(str(v))} for v in comments]
        constraints = [{'predicate': str(p), 'object': expr(o)}
                       for p, o in sorted(g.predicate_objects(c), key=lambda v: tuple(map(str, v)))
                       if p not in excluded]
        rows.append({'iri': str(c), 'label': labels[0] if labels else str(c)[len(NS):],
            'label_basis': 'SOURCE_ENGLISH_LABEL' if labels else 'IRI_LOCAL_NAME',
            'module': 'DUL4.2 standalone root', 'source_sha256': SHA,
            'population': 'LOCAL_DECLARED_NAMED_CLASS',
            'deprecated': any(str(v).lower() in ('true', '1') for v in g.objects(c, OWL.deprecated)),
            'annotation_records': annotation_records,
            'named_superclasses': sorted(str(x) for x in g.objects(c, RDFS.subClassOf) if isinstance(x, URIRef)),
            'equivalent_expressions': sorted((expr(x) for x in g.objects(c, OWL.equivalentClass)), key=lambda x: json.dumps(x, sort_keys=True)),
            'constraint_ref': f'DUL-C{i:03d}', 'constraints': constraints,
            'constraint_sha256': digest(constraints)})
    return {'rows': rows, 'populations': {
        'local_declared_named_class_iris': list(map(str, local)),
        'external_declared_named_class_iris': sorted(str(x) for x in declared if x not in local),
        'referenced_undeclared_class_iris': sorted(str(x) for x in nonbuiltin_ref - declared),
        'builtin_class_position_iris': builtin,
        'declared_import_iris': sorted(str(x) for x in g.objects(None, OWL.imports)),
        'deprecated_named_class_iris': sorted(str(c) for c in declared if any(str(v).lower() in ('true', '1') for v in g.objects(c, OWL.deprecated))),
        'anonymous_class_declarations': len({s for k in (OWL.Class,RDFS.Class) for s in g.subjects(RDF.type,k) if isinstance(s,BNode)}),
        'anonymous_restrictions': len({s for s in g.subjects(RDF.type,OWL.Restriction) if isinstance(s,BNode)}),
        'explicit_document_triples': len(g)}, 'rdflib': rdflib.__version__}


def validate(data, source=None):
    errors = []
    rows = data.get('classes', [])
    iris = [r.get('iri') for r in rows]
    expected = data.get('populations', {}).get('local_declared_named_class_iris', [])
    if len(iris) != 78 or len(set(iris)) != 78 or sorted(iris) != expected:
        errors.append('Class population must exactly reconcile all 78 distinct IRIs')
    if digest(expected) != data.get('class_iri_set_sha256') or digest(expected) != 'a350185af60f8e2c1e4f37a79701e3c81790280de97fde4a13d3de4b59212de8':
        errors.append('Class IRI-set digest mismatch')
    if data.get('source', {}).get('sha256') != SHA:
        errors.append('Source digest mismatch')
    for r in rows:
        if r.get('source_sha256') != SHA or not r.get('iri', '').startswith(NS):
            errors.append('Bad class source or namespace')
        if r.get('constraint_sha256') != digest(r.get('constraints')):
            errors.append('Constraint hash mismatch: ' + r.get('iri',''))
        d = r.get('source_definition', {})
        state = d.get('status')
        para = r.get('reviewer_definition')
        if (state == 'NOT_REPORTED_IN_SELECTED_SOURCE') != (not r.get('annotation_records')):
            errors.append('Missing-comment state contradicts annotations')
        if (state == 'INSUFFICIENT_LABEL_RESTATEMENT') != (r.get('iri') in (NS+'Norm', NS+'SocialRelation')):
            errors.append('Label-only classification differs from manual review')
        for a in r.get('annotation_records', []):
            if not re.fullmatch('[0-9a-f]{64}', a.get('text_sha256', '')) or a.get('characters', 0) <= 0:
                errors.append('Malformed annotation provenance')
        if state == 'DESCRIPTIVE_COMMENT_REVIEWED':
            if not isinstance(para, str) or not para.strip() or not r.get('annotation_records'):
                errors.append('Definition requires prose and annotation evidence')
        elif state in ('NOT_REPORTED_IN_SELECTED_SOURCE', 'INSUFFICIENT_LABEL_RESTATEMENT'):
            if para is not None:
                errors.append('Unsupported reconstructed definition')
        else:
            errors.append('Unknown definition state')
        if d.get('locator') != r.get('iri') or d.get('predicate') != 'http://www.w3.org/2000/01/rdf-schema#comment':
            errors.append('Bad definition locator')
    calculated = {'local_classes':len(rows),
        'classes_with_comment_candidates':sum(bool(r.get('annotation_records')) for r in rows),
        'accepted_descriptive_comment_classes':sum(r.get('source_definition',{}).get('status')=='DESCRIPTIVE_COMMENT_REVIEWED' for r in rows),
        'insufficient_label_restatement_classes':sum(r.get('source_definition',{}).get('status')=='INSUFFICIENT_LABEL_RESTATEMENT' for r in rows),
        'classes_without_comment':sum(not r.get('annotation_records') for r in rows),
        'reviewer_reconstructions':0,
        'classes_with_asserted_equivalence':sum(bool(r.get('equivalent_expressions')) for r in rows)}
    if calculated != data.get('counts'):
        errors.append('Reported counts differ from rows')
    if source is not None:
        fresh = inspect_source(source)
        if fresh['populations'] != data.get('populations'):
            errors.append('Source populations differ')
        for a,b in zip(fresh['rows'], rows):
            for k,v in a.items():
                if b.get(k) != v:
                    errors.append('Source field differs: ' + a['iri'] + ':' + k)
    return {'status':'FAIL' if errors else 'PASS','errors':errors,'counts':calculated,
            'source_reparsed':source is not None,
            'source_sha256':SHA,
            'class_iri_set_sha256':data.get('class_iri_set_sha256'),
            'semantic_acceptance':'NOT_ASSESSED',
            'scope':'Set, annotation provenance, explicit axiom and record integrity; not scientific validation or reasoning'}


if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path);p.add_argument('--output',type=Path)
    a=p.parse_args();r=validate(yaml.safe_load(PATH.read_text()),a.source)
    r['catalog_sha256']=hashlib.sha256(PATH.read_bytes()).hexdigest()
    r['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if a.output:a.output.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(json.dumps(r,indent=2));raise SystemExit(r['status']!='PASS')
