"""Inspect the exact Cognitive Atlas 0.3 export without running its generator.

No implicit imports, unpickling, author-source repair or Clariceptify model edits.
The licensed definition extract is distinct from the original OWL distribution.
"""
from pathlib import Path
from collections import Counter
import argparse
import csv
import hashlib
import importlib.metadata
import io
import json
import platform
import re
import subprocess
import time
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = 'evaluation/related-work/cognitiveatlas/'
MANIFEST = 'evidence/related-work/corpus/cognitiveatlas-inputs.yaml'
SOURCE = 'ontology/cogat.v2.owl'
SOURCE_SHA = '701aa9e8351fcec3de0122df7ed49158cff83fe4e7353bd540122d8a34ce5fd8'
NS = 'http://www.cognitiveatlas.org/ontology/cogat.owl#'
COGPO = 'http://www.cogpo.org/ontologies/working/CogPOver2011.owl#'
LICENSE = 'https://creativecommons.org/licenses/by-sa/3.0/us/'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def stable(v):
    return sha(json.dumps(v, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode())


def inputs(folder):
    m = yaml.safe_load((ROOT / MANIFEST).read_text())
    result = {}
    for spec in m['artifacts']:
        raw = (Path(folder) / spec['filename']).read_bytes()
        if sha(raw) != spec['sha256']:
            raise ValueError('Input digest mismatch: ' + spec['id'])
        result[spec['id']] = raw
    if sha(result[SOURCE]) != SOURCE_SHA:
        raise ValueError('Selected root substituted')
    return result


def graph(raw):
    from rdflib import Graph
    return Graph().parse(data=raw, format='xml')


def expr(g, n, seen=frozenset()):
    from rdflib import URIRef, Literal
    if isinstance(n, URIRef):
        return {'iri': str(n)}
    if isinstance(n, Literal):
        return {'literal': str(n), 'language': n.language,
                'datatype': str(n.datatype) if n.datatype else None}
    if n in seen:
        return {'cycle': True}
    rows = [{'predicate': str(p), 'object': expr(g, o, seen | {n})}
            for p, o in g.predicate_objects(n)]
    return {'anonymous_expression': sorted(rows, key=lambda x: json.dumps(x, sort_keys=True))}


def receipt(mode):
    import rdflib
    return dict(schema_version='1.0', issue=241, mode=mode,
                source_sha256=SOURCE_SHA, source_manifest_sha256=sha((ROOT / MANIFEST).read_bytes()),
                generator_path='tools/inspect_cognitive_atlas.py',
                generator_sha256=sha(Path(__file__).read_bytes()),
                python=platform.python_version(), rdflib=rdflib.__version__,
                model_change='NONE', original_source_files_redistributed=False)


def inspect(folder):
    from rdflib import RDF, RDFS, OWL, URIRef, BNode, Namespace
    raw = inputs(folder); g = graph(raw[SOURCE])
    SK = Namespace('http://www.w3.org/2004/02/skos/core#')
    DC = Namespace('http://purl.org/dc/terms/')
    declared = {s for k in [OWL.Class, RDFS.Class] for s in g.subjects(RDF.type, k) if isinstance(s, URIRef)}
    local = {c for c in declared if str(c).startswith(NS)}
    references = {o for p in [RDFS.subClassOf, OWL.someValuesFrom, OWL.allValuesFrom,
                              OWL.onClass, RDFS.domain, RDFS.range]
                  for o in g.objects(None, p) if isinstance(o, URIRef)}
    properties = set(g.subjects(RDF.type, OWL.ObjectProperty))
    used = set(g.objects(None, OWL.onProperty))
    rows, definitions = [], []
    for c in sorted(declared, key=str):
        labels = sorted(map(str, g.objects(c, RDFS.label)))
        ids = sorted(map(str, g.objects(c, DC.identifier)))
        values = sorted(g.objects(c, SK.definition), key=lambda x: (x.language or '', str(x)))
        state = 'NONEMPTY_SOURCE_DEFINITION' if any(str(v).strip() for v in values) else 'EMPTY_ANNOTATION_ONLY' if values else 'NOT_REPORTED_IN_SELECTED_SOURCE'
        annotations = [dict(predicate=str(SK.definition), characters=len(str(v)), language=v.language,
                            text_sha256=sha(str(v).encode()), nonempty=bool(str(v).strip())) for v in values]
        logical = sorted([{'predicate': str(p), 'object': expr(g, o)}
                          for p, o in g.predicate_objects(c)
                          if p in [RDFS.subClassOf, OWL.equivalentClass, OWL.disjointWith]],
                         key=lambda x: json.dumps(x, sort_keys=True))
        provenance = []
        for p in [DC.Contributor, DC.Date, SK.altLabel, SK.hasTopConcept]:
            for o in sorted(g.objects(c, p), key=str):
                provenance.append(dict(predicate=str(p), nonempty=bool(str(o).strip()),
                                       characters=len(str(o)), text_sha256=sha(str(o).encode())))
        rows.append(dict(iri=str(c), label=labels[0] if len(labels) == 1 else None,
                         labels=labels, label_basis='SOURCE_LABEL' if len(labels) == 1 else 'MULTIPLE_SOURCE_LABELS_AMBIGUOUS' if labels else 'NOT_REPORTED',
                         identifiers=ids, source_identifier_kinds=sorted({x.split('_', 1)[0] for x in ids}),
                         module='cogat.v2.owl header0.3', source_sha256=SOURCE_SHA,
                         population='LOCAL_DECLARED_NAMED_CLASS' if c in local else 'EXTERNAL_DECLARED_NAMED_CLASS',
                         deprecated=any(str(o).lower() in ['true', '1'] for o in g.objects(c, OWL.deprecated)),
                         source_definition=dict(status=state, predicate=str(SK.definition), annotations=annotations,
                             registry_path='evidence/related-work/cognitiveatlas/source-definitions.jsonl',
                             registry_key=str(c), logical_sufficiency='NOT_ASSESSED'),
                         reviewer_definition=dict(text=None, basis='ATTRIBUTED_ORIGINAL_DEFINITION_RETAINED' if state == 'NONEMPTY_SOURCE_DEFINITION' else 'MISSING_SOURCE_DEFINITION',
                             note='No invented paraphrase or invented completion; exact author text is in the separately licensed definition register.'),
                         named_superclasses=sorted(str(o) for o in g.objects(c, RDFS.subClassOf) if isinstance(o, URIRef)),
                         equivalent_expressions=sorted((expr(g, o) for o in g.objects(c, OWL.equivalentClass)), key=lambda x: json.dumps(x, sort_keys=True)),
                         constraints=logical, constraint_ref=str(c), constraint_sha256=stable(logical),
                         annotation_provenance=provenance,
                         notes=['Multiple source identifiers must not be treated as one disambiguated meaning.'] if len(ids) > 1 else []))
        definitions.append(dict(iri=str(c), labels=labels, identifiers=ids, source_sha256=SOURCE_SHA,
                                predicate=str(SK.definition), definitions=[dict(text=str(v), language=v.language,
                                    datatype=str(v.datatype) if v.datatype else None, text_sha256=sha(str(v).encode())) for v in values],
                                source_attribution='Cognitive Atlas contributors; export CognitiveAtlas/cogat-ontology at a600c366e9e3d3647a85cbc2c6e53e78abcf1951',
                                license_url=LICENSE, changes='RDF-decoded literal extraction; original wording retained, no semantic rewriting.'))
    def prop(p):
        return dict(iri=str(p), declared=p in properties,
                    population='LOCAL' if str(p).startswith(NS) else 'EXTERNAL',
                    axioms=sorted([dict(predicate=str(q), object=expr(g, o)) for q, o in g.predicate_objects(p)
                                   if q in [RDF.type, RDFS.domain, RDFS.range, RDFS.subPropertyOf, OWL.inverseOf, OWL.equivalentProperty]],
                                  key=lambda x: json.dumps(x, sort_keys=True)))
    categories = Counter('+'.join(r['source_identifier_kinds']) or 'helper/no_identifier'
                         for r in rows if r['population'] == 'LOCAL_DECLARED_NAMED_CLASS')
    result = receipt('COMPLETE_DECLARATION_AND_DEFINITION_EXTRACTION_NOT_SEMANTIC_ACCEPTANCE')
    result.update(ontology_iris=sorted(map(str, g.subjects(RDF.type, OWL.Ontology))),
                  version_info=sorted(map(str, g.objects(None, OWL.versionInfo))),
                  imports=sorted(map(str, g.objects(None, OWL.imports))),
                  counts=dict(explicit_triples=len(g), local_named_classes=len(local), external_named_classes=len(declared-local),
                      named_classes=len(declared), local_declared_object_properties=sum(str(p).startswith(NS) for p in properties),
                      external_declared_object_properties=sum(not str(p).startswith(NS) for p in properties),
                      declared_object_properties=len(properties), used_restriction_properties=len(used),
                      undeclared_used_object_properties=len(used-properties),
                      datatype_properties=len(set(g.subjects(RDF.type, OWL.DatatypeProperty))),
                      subclass_statements=sum(1 for s,p,o in g if p == RDFS.subClassOf),
                      named_subclass_statements=sum(1 for s,p,o in g if p == RDFS.subClassOf and isinstance(o, URIRef)),
                      restriction_nodes=len(set(g.subjects(RDF.type, OWL.Restriction))),
                      definition_nonempty_local_classes=sum(r['source_definition']['status'] == 'NONEMPTY_SOURCE_DEFINITION' for r in rows if r['population'].startswith('LOCAL')),
                      definition_empty_only_local_classes=sum(r['source_definition']['status'] == 'EMPTY_ANNOTATION_ONLY' for r in rows if r['population'].startswith('LOCAL')),
                      definition_absent_local_classes=sum(r['source_definition']['status'] == 'NOT_REPORTED_IN_SELECTED_SOURCE' for r in rows if r['population'].startswith('LOCAL')),
                      local_classes_with_multiple_identifiers=sum(len(r['identifiers']) > 1 for r in rows if r['population'].startswith('LOCAL')),
                      local_identifier_values=sum(len(r['identifiers']) for r in rows if r['population'].startswith('LOCAL')),
                      deprecated_classes=sum(r['deprecated'] for r in rows),
                      disjoint_axioms=len(list(g.triples((None, OWL.disjointWith, None))))+len(set(g.subjects(RDF.type, OWL.AllDisjointClasses))),
                      equivalent_class_axioms=len(list(g.triples((None, OWL.equivalentClass, None)))),
                      explicit_sameAs=len(list(g.triples((None, OWL.sameAs, None)))),
                      inverse_property_axioms=len(list(g.triples((None, OWL.inverseOf, None))))),
                  classes=rows, source_definition_register=definitions,
                  category_counts_mutually_exclusive=dict(sorted(categories.items())),
                  referenced_undeclared_class_iris=sorted(map(str, references-declared)),
                  properties=[prop(p) for p in sorted(properties | used, key=str)],
                  used_restriction_property_counts=dict(sorted(Counter(map(str,g.objects(None,OWL.onProperty))).items())),
                  inferred_class_population=None, foundation='SKOS/OBO RO/CogPO and BFO1.1 namespace references;no owl:imports or verified foundational alignment',
                  license_boundary='Definitions are a separately attributed CC-BY-SA3.0 US extract based on the official project site license. Original OWL distribution and all upstream files are not republished or blanket-relicensed.')
    return result


def static_sources(folder):
    from rdflib import Namespace, URIRef
    raw = inputs(folder); out = receipt('STATIC_GENERATOR_AND_RAW_INPUT_INSPECTION')
    code = raw['create_owl.v2.py'].decode(); linked = raw['paper-linked-create_owl.py'].decode()
    checks = []
    for name in ['ontology/all_concepts.rdf', 'ontology/all_tasks.rdf']:
        try:
            g = graph(raw[name]); checks.append(dict(path=name, sha256=sha(raw[name]), result='PARSE_PASS', triples=len(g)))
        except Exception as e:
            checks.append(dict(path=name, sha256=sha(raw[name]), result='PARSE_FAIL', error=type(e).__name__+': '+str(e)[:600]))
    csvs = {}
    for name in ['ontology/table_assertion.csv', 'ontology/table_relation.csv', 'ontology/type_condition.csv', 'ontology/type_contrast.csv']:
        rows = list(csv.reader(io.StringIO(raw[name].decode()), delimiter=';'))
        csvs[name] = dict(rows=len(rows), field_counts=dict(sorted(Counter(len(r) for r in rows).items())),
                          unique_first_column_values=len({r[0] for r in rows}),
                          sha256=sha(raw[name]))
    rows = list(csv.reader(io.StringIO(raw['ontology/table_assertion.csv'].decode()), delimiter=';'))
    checksums = []
    for filename, src in [('create_owl.v2.py',code),('paper-linked-create_owl.py',linked)]:
        checksums.append(dict(path=filename, sha256=sha(src.encode()), python2_print_syntax=bool(re.search(r'(?m)^\s*print [^(]',src)),
                              pickle_load='pickle.load(' in src, version_string=re.findall(r"versionString=['\"]([^'\"]+)",src),
                              selected_mapping_branches=sorted(set(re.findall(r"r\[3\]\s*==\s*['\"](T\d+)['\"]",src))),
                              removes_first_assertion='relations.remove(relations[0])' in src))
    homepage = raw['current-homepage.html'].decode()
    out.update(raw_RDF_parses=checks, csv_profiles=csvs, generators=checksums,
               first_assertion=dict(id=rows[0][0], relation=rows[0][3], is_header=False),
               source_relation_counts=dict(sorted(Counter(r[3] for r in rows).items())),
               selected_assertion_polarities=dict(sorted(Counter(r[12] for r in rows if len(r)>12).items())),
               license_evidence=dict(url='https://www.cognitiveatlas.org/', retrieved_on='2026-10-29',
                   html_sha256=sha(raw['current-homepage.html']), license_url=LICENSE,
                   exact_link_present=LICENSE.replace('https:','http:') in homepage,
                   note='Official project footer;the selected export has no embedded license. This licenses the attributed definition extract, not a blanket MIT claim for the ontology or the unrelated discussion repository.'),
               generator_execution='NOT_EXECUTED', pickle_execution='NOT_EXECUTED',
               blockers=['Exact raw RDF parses are reported as observed; no input correction is made.',
                         'The Python2/string-splitting generator reads pickle and drops the first assertion as a purported header. No conversion or unpickling is performed; exact historical byte generation is unestablished.'],
               paper_2011_equivalence='NOT_ESTABLISHED')
    return out


def cases():
    from rdflib import Graph, Namespace, RDF, OWL, BNode
    C=Namespace(NS);P=Namespace(COGPO);T=Namespace('urn:clariceptify:cogat241:');RO=Namespace('http://www.obofoundry.org/ro/ro.owl#')
    rows=[]
    def typ(g,n,c):g.add((T[n],RDF.type,c))
    def edge(g,a,p,b):g.add((T[a],p,T[b]))
    def not_type(g,n,c):
        b=BNode('cogat241-'+n+'-complement');g.add((T[n],RDF.type,b));g.add((b,RDF.type,OWL.Class));g.add((b,OWL.complementOf,c))
    def empty(g,n,p):
        b=BNode('cogat241-'+n+'-empty');g.add((T[n],RDF.type,b));g.add((b,RDF.type,OWL.Restriction));g.add((b,OWL.onProperty,p));g.add((b,OWL.allValuesFrom,OWL.Nothing))
    def neg(g,a,p,b):
        n=BNode('cogat241-denial');g.add((n,RDF.type,OWL.NegativePropertyAssertion));g.add((n,OWL.sourceIndividual,T[a]));g.add((n,OWL.assertionProperty,p));g.add((n,OWL.targetIndividual,T[b]))
    def case(i,q,ok,text,fn):
        g=Graph();fn(g);rows.append((i,q,ok,text,g))
    case('baseline','Q08',True,'Exact root with no added individuals',lambda g:None)
    case('contrast-measurement','Q03',True,'Concept measured by an instance of an actual contrast class',lambda g:(typ(g,'m',C.CAO_00101),typ(g,'c',C.CAO_01210),edge(g,'m',C.measured_by,'c')))
    case('concrete-concept-task-only','Q03',False,'This concrete concept has an all-values restriction to named contrast classes;its task-only filler denial contradicts those restrictions',lambda g:(typ(g,'m',C.CAO_00101),typ(g,'t',P.COGPO_00049),edge(g,'m',C.measured_by,'t'),not_type(g,'t',P.COGPO_00109)))
    case('neutral-concept-task-only','Q03',True,'A neutral concept has no concrete-class contrast-only restriction;the property range alone allows a task-only filler',lambda g:(typ(g,'m',C.CAO_00001),typ(g,'t',P.COGPO_00049),edge(g,'m',C.measured_by,'t'),not_type(g,'t',P.COGPO_00109)))
    case('denied-measurement-domain','Q03',False,'Source measured_by forces its subject into undeclared MentalConcept',lambda g:(edge(g,'m',C.measured_by,'t'),not_type(g,'m',C.MentalConcept)))
    case('mentalconcept-helper-not-joined','Q03',True,'Domain MentalConcept is not declared equivalent to CAO_00001',lambda g:(edge(g,'m',C.measured_by,'t'),not_type(g,'m',C.CAO_00001)))
    case('denied-measures-range','Q03',False,'Source measures incorrectly points its range to the task class',lambda g:(edge(g,'c',C.measures,'m'),not_type(g,'m',P.COGPO_00049)))
    case('inverse-not-entailed','Q03',True,'measured_by does not entail a reverse measures edge',lambda g:(edge(g,'m',C.measured_by,'c'),neg(g,'c',C.measures,'m')))
    case('concept-and-task-cotype','Q02',True,'Selected source does not disjoin mental concepts and tasks',lambda g:(typ(g,'x',C.CAO_00001),typ(g,'x',P.COGPO_00049)))
    case('collided-identifier-class','Q07',True,'Class with a construct identifier and an unrelated contrast identifier remains logically inhabitable',lambda g:typ(g,'x',C.CAO_01573))
    case('collision-with-reviewer-disjointness','Q07',False,'Explicit reviewer-added separation exposes a construct/contrast collision;not an authored disjointness axiom',lambda g:(g.add((C.CAO_00001,OWL.disjointWith,P.COGPO_00109)),typ(g,'x',C.CAO_01573)))
    case('condition-unnamed-task','Q04',True,'A condition may have an unnamed required part-of Task',lambda g:typ(g,'x',C.CAO_00980))
    case('condition-no-task','Q04',False,'A selected condition cannot deny every part-of witness',lambda g:(typ(g,'x',C.CAO_00980),empty(g,'x',RO.part_of)))
    case('undeclared-local-reference','Q05',True,'A referenced undeclared CAO IRI is not a missing owl:imports proof or a defined class',lambda g:typ(g,'x',C.CAO_00344))
    return rows


def reason(folder, private):
    import jpype,owlready2
    from rdflib.compare import to_canonical_graph
    from xml.etree import ElementTree as ET
    raw=inputs(folder);private=Path(private).resolve();private.mkdir(parents=True,exist_ok=True)
    jar=Path(owlready2.__file__).parent/'hermit/HermiT.jar';jpype.startJVM(classpath=[str(jar)]);J=jpype.JClass
    M=J('org.semanticweb.owlapi.apibinding.OWLManager');File=J('java.io.File');H=J('org.semanticweb.HermiT.Reasoner')
    def load(b,name):
        p=private/(name+'.owl');p.write_bytes(b);m=M.createOWLOntologyManager();return m,m.loadOntologyFromOntologyDocument(File(str(p)))
    m,o=load(raw[SOURCE],'profile');profile=J('org.semanticweb.owlapi.profiles.OWL2DLProfile')().checkOntology(o)
    violations=list(profile.getViolations());counts=Counter(str(v.getClass().getSimpleName()) for v in violations)
    metrics=dict(axioms=int(o.getAxiomCount()),logical_axioms=int(o.getLogicalAxiomCount()),signature_classes=len(o.getClassesInSignature()),signature_object_properties=len(o.getObjectPropertiesInSignature()))
    rr=H(o);base_consistent=bool(rr.isConsistent());unsat=sorted(str(x.getIRI()) for x in rr.getUnsatisfiableClasses().getEntitiesMinusBottom());rr.dispose();m.removeOntology(o)
    rows=[]
    for ident,q,expected,description,fixture in cases():
        nt='\n'.join(sorted(to_canonical_graph(fixture).serialize(format='nt').splitlines()))+'\n' if len(fixture) else ''
        elements=ET.fromstring(fixture.serialize(format='xml'))
        added=b'\n'.join(ET.tostring(e,encoding='utf-8') for e in elements)
        combined=raw[SOURCE].replace(b'</rdf:RDF>',added+b'\n</rdf:RDF>') if added else raw[SOURCE]
        m,o=load(combined,ident);start=time.monotonic();observed=None;error=None
        try:rr=H(o);observed=bool(rr.isConsistent());rr.dispose()
        except Exception as exc:error=type(exc).__name__+': '+str(exc)[:1000]
        m.removeOntology(o);rows.append(dict(id=ident,question=q,description=description,fixture_nt=nt,fixture_sha256=sha(nt.encode()),loaded_document_sha256=sha(combined),expected_consistent=expected,observed_consistent=observed,error=error,result='PASS' if observed is expected else 'ERROR' if error else 'FAIL',seconds=round(time.monotonic()-start,4)))
        print(ident,rows[-1]['result'],observed,flush=True)
    out=receipt('OWLAPI_PROFILE_AND_BOUNDED_HERMIT_EXECUTION')
    out.update(owl2_dl_profile_pass=bool(profile.isInProfile()),profile_violation_count=len(violations),profile_violation_kinds=dict(sorted(counts.items())),
               profile_examples=sorted(str(v) for v in violations)[:5],owlapi_metrics=metrics,core_logical_consistent=base_consistent,unsatisfiable_named_classes=unsat,
               tests=rows,summary=dict(total=len(rows),passed=sum(x['result']=='PASS' for x in rows),failed=sum(x['result']=='FAIL' for x in rows),errors=sum(x['result']=='ERROR' for x in rows)),
               hermit_version='1.3.8.1099 bundled jar manifest',hermit_jar_sha256=sha(jar.read_bytes()),jpype=importlib.metadata.version('JPype1'),owlready2=importlib.metadata.version('owlready2'),
               java=subprocess.run(['java','-version'],capture_output=True,text=True).stderr.strip(),
               input_policy='Exact original RDF/XML bytes with each isolated fixture appended as namespace-qualified child elements;no source axiom deletion or upstream import. Original source not redistributed.',
               profile_reasoner_boundary='Profile rejection due undeclared entities is separate from consistency of logical axioms accepted by the recorded OWLAPI/HermiT loader. No imported foundation proof or intended-model adequacy.',
               author_generator_execution='NOT_EXECUTED',author_CQ_suite='NOT_REPORTED_IN_SELECTED_PAPER',inferred_class_population=None)
    jpype.shutdownJVM();return out


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['census','static','reason']);p.add_argument('--source-dir',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--private-dir',type=Path);p.add_argument('--catalog-dir',type=Path);a=p.parse_args()
    if a.mode=='reason' and not a.private_dir:p.error('--private-dir required')
    if a.mode=='census' and not a.catalog_dir:p.error('--catalog-dir required')
    d=inspect(a.source_dir) if a.mode=='census' else static_sources(a.source_dir) if a.mode=='static' else reason(a.source_dir,a.private_dir)
    if a.mode=='census':
        a.catalog_dir.mkdir(parents=True,exist_ok=True)
        indexes={}
        for key,name in [('classes','classes.jsonl'),('source_definition_register','source-definitions.jsonl')]:
            rows=d.pop(key);data=''.join(json.dumps(row,sort_keys=True,ensure_ascii=True,separators=(',',':'))+'\n' for row in rows).encode()
            (a.catalog_dir/name).write_bytes(data);indexes[name]=dict(rows=len(rows),sha256=sha(data),path='evidence/related-work/cognitiveatlas/'+name)
        d['catalog_indexes']=indexes
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps(d.get('summary',d.get('counts',{'complete':True}))))
