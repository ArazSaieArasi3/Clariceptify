"""Execute exact-core profile and asserted queries without weakening the source."""
from pathlib import Path
import argparse,hashlib,importlib.metadata,json,platform,subprocess
ROOT=Path(__file__).resolve().parents[1]
SHA='f0d7b6c795fe9e1a699eda2d80089371336869e981e938648edd5db88358658a'
NS='http://www.loa-cnr.it/ontologies/cDnS.owl#'
PREFIX='PREFIX c: <'+NS+'>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'
def sha(b):return hashlib.sha256(b).hexdigest()
def inspect(source):
 from rdflib import Graph,OWL,RDF,RDFS,URIRef
 from inventory_review_artifact import inventory
 import jpype,owlready2
 source=Path(source).resolve();raw=source.read_bytes()
 if sha(raw)!=SHA:raise ValueError('Selected core bytes changed')
 g=Graph().parse(data=raw,format='xml');imports=sorted(str(x) for x in g.objects(None,OWL.imports))
 if imports:raise ValueError('Unexpected import boundary; no implicit network load')
 old=json.loads((ROOT/'evidence/related-work/deep-reviews/cDnS2007/artifact-census.json').read_text());current=inventory(source,SHA)
 fields=['classes','object_properties','datatype_properties','counts','explicit_triples','declared_import_iris','anonymous_restrictions']
 if any(current[k]!=old[k] for k in fields):raise ValueError('Retained all-declaration census differs')
 queries=[
 ('Q01','Concept definition exactly one','ASK { c:Concept rdfs:subClassOf ?r . ?r owl:onProperty c:isDefinedIn ; owl:cardinality ?n . FILTER(?n=1) }'),
 ('Q02','General schematic conceptualization range','ASK { c:conceptualizes rdfs:domain c:SocialAgent ; rdfs:range c:SchematicEntity . }'),
 ('Q03','General schematic expression without property-chain derivation','ASK { c:expresses rdfs:domain c:InformationObject ; rdfs:range c:SchematicEntity . FILTER NOT EXISTS { ?s owl:propertyChainAxiom ?l } }'),
 ('Q04','No declared Time or datatype property in this root','ASK { FILTER NOT EXISTS { c:Time rdf:type owl:Class } FILTER NOT EXISTS { ?p rdf:type owl:DatatypeProperty } }'),
 ('Q05','Plan/norm/community not declared in standalone core','ASK { FILTER NOT EXISTS { c:Plan rdf:type owl:Class } FILTER NOT EXISTS { c:Norm rdf:type owl:Class } FILTER NOT EXISTS { c:KnowledgeCommunity rdf:type owl:Class } }'),
 ('Q06','Schematic coverage not asserted by an equivalence axiom','ASK { c:SchematicEntity rdfs:subClassOf c:Entity . FILTER NOT EXISTS { c:SchematicEntity owl:equivalentClass ?x } }'),
 ('Q07','Configuration has only named Collection superclass','ASK { c:Configuration rdfs:subClassOf c:Collection . FILTER NOT EXISTS { c:Configuration owl:equivalentClass ?x } FILTER NOT EXISTS { c:Configuration rdfs:subClassOf ?x . FILTER(?x != c:Collection) } }'),
 ('Q08','Minimum cardinality two on transitive proper-part','ASK { c:hasProperPart rdf:type owl:TransitiveProperty . c:Bundle rdfs:subClassOf ?r . ?r owl:onProperty c:hasProperPart ; owl:minCardinality ?n . FILTER(?n=2) }')]
 asks=[]
 for ident,label,body in queries:
  query=PREFIX+body;observed=bool(g.query(query).askAnswer)
  asks.append(dict(id=ident,label=label,query=query,query_sha256=sha(query.encode()),expected_ask=True,observed_ask=observed,result='PASS' if observed else 'FAIL',basis='EXECUTED_ASSERTED_RDF_QUERY_NOT_SEMANTIC_VALIDATION'))
 jar=Path(owlready2.__file__).parent/'hermit/HermiT.jar';jpype.startJVM(classpath=[str(jar)]);J=jpype.JClass
 manager=J('org.semanticweb.owlapi.apibinding.OWLManager').createOWLOntologyManager();ontology=manager.loadOntologyFromOntologyDocument(J('java.io.File')(str(source)))
 profile=J('org.semanticweb.owlapi.profiles.OWL2DLProfile')().checkOntology(ontology);violations=sorted(str(x) for x in profile.getViolations());in_profile=bool(profile.isInProfile())
 attempt=dict(state='NOT_ATTEMPTED',consistent=None,unsatisfiable_named_classes=None,error=None)
 try:
  reasoner=J('org.semanticweb.HermiT.Reasoner')(ontology);attempt.update(state='EXECUTED',consistent=bool(reasoner.isConsistent()));reasoner.dispose()
 except Exception as e:attempt.update(state='REFUSED_NON_SIMPLE_PROPERTY',error=str(e).replace(str(source),'[private source]'))
 metrics=dict(axioms=int(ontology.getAxiomCount()),logical_axioms=int(ontology.getLogicalAxiomCount()),signature_classes=len(ontology.getClassesInSignature()),signature_object_properties=len(ontology.getObjectPropertiesInSignature()))
 jpype.shutdownJVM()
 return dict(schema_version='1.0',issue=267,checked_on='2026-10-29',source_sha256=SHA,source_bytes=len(raw),source_format='Unchanged original RDF/XML',generator_path='tools/inspect_cdns267.py',generator_sha256=sha(Path(__file__).read_bytes()),inventory_helper_sha256=sha((ROOT/'tools/inventory_review_artifact.py').read_bytes()),source_census_reconciliation='PASS',source_population=current['counts'],explicit_triples=len(g),imports=imports,loaded_ontology_count=1,
  source_classes=[x['iri'] for x in current['classes']],source_object_properties=[x['iri'] for x in current['object_properties']],
  profile=dict(kind='OWL2_DL',in_profile=in_profile,violation_count=len(violations),violations=violations),reasoner_attempt=attempt,owlapi_metrics=metrics,asserted_queries=asks,query_summary=dict(total=len(asks),passed=sum(x['result']=='PASS' for x in asks),failed=sum(x['result']=='FAIL' for x in asks)),
  python=platform.python_version(),rdflib=importlib.metadata.version('rdflib'),jpype=importlib.metadata.version('JPype1'),owlready2=importlib.metadata.version('owlready2'),hermit='1.3.8.1099 bundled jar manifest',hermit_jar_sha256=sha(jar.read_bytes()),java=subprocess.run(['java','-version'],capture_output=True,text=True).stderr.strip(),
  policy=dict(source_repair=False,axioms_deleted=0,imports_deleted=0,transitivity_removed=False,cardinality_weakened=False,approximate_repaired_theory_tested=False,fixture_consistency_execution='NOT_EXECUTED_FULL_CORE_REFUSED',logical_consistency='NOT_ESTABLISHED',global_paper_proof='NOT_EXECUTED',scientific_acceptance='NOT_ASSESSED',model_change='NONE'),claim_limit='Asserted ASK results describe source structure. A DL profile failure and tool refusal do not prove inconsistency. No source stripping or repaired surrogate is used to manufacture positive semantic results.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();d=inspect(a.source);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps(dict(profile=d['profile'],reasoner=d['reasoner_attempt'],queries=d['query_summary']),indent=2))
