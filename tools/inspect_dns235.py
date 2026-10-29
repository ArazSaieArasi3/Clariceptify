"""Inspect exact later DLP3971 inputs for #235; never repair or fetch imports."""
from pathlib import Path
import argparse,hashlib,json,platform,sys
ROOT=Path(__file__).resolve().parents[1]
NS='http://www.loa-cnr.it/ontologies/ExtendedDnS.owl#'
ARCHIVE='b88ce73648ffdbb200a371ac8c51e51739c3ad1760680e644e8cf5cde322bcc2'
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,d):Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def inputs(folder):
 from rdflib import Graph
 from zipfile import ZipFile
 intake=json.loads((ROOT/'evidence/related-work/corpus/dlp3971-intake.json').read_text())
 source=Path(folder)/'DLP3971.zip'
 if sha(source.read_bytes())!=ARCHIVE:raise ValueError('Archive substitution')
 out={}
 with ZipFile(source) as z:
  for x in intake['modules']:
   raw=z.read(x['filename'])
   if sha(raw)!=x['sha256']:raise ValueError('Module substitution')
   out[x['filename']]=(raw,x,Graph().parse(data=raw,format='xml'))
 return out
def receipt(kind):
 return dict(kind=kind,issue=235,checked_on='2026-10-29',archive_sha256=ARCHIVE,
  generator_path='tools/inspect_dns235.py',generator_sha256=sha(Path(__file__).read_bytes()),
  helper_sha256=sha((ROOT/'tools/inspect_bdi2026.py').read_bytes()),python=platform.python_version(),
  historical_2003_fidelity='NOT_ESTABLISHED',model_change='NONE')
def census(folder):
 from rdflib import RDF,RDFS,OWL,URIRef
 from inspect_bdi2026 import expression,stable
 data=inputs(folder);raw,pin,g=data['ExtendedDnS.owl'];classes=sorted({x for x in g.subjects(RDF.type,OWL.Class) if isinstance(x,URIRef)},key=str)
 rows=[]
 for c in classes:
  annotations=[dict(predicate=str(p),language=o.language,datatype=str(o.datatype) if o.datatype else None,text_sha256=sha(str(o).encode())) for p in [RDFS.comment] for o in sorted(g.objects(c,p),key=str)]
  axioms={str(p):sorted([expression(g,o) for o in g.objects(c,p)],key=lambda x:json.dumps(x,sort_keys=True)) for p in [RDFS.subClassOf,OWL.equivalentClass,OWL.disjointWith]}
  rows.append(dict(iri=str(c),label=[str(o) for o in sorted(g.objects(c,RDFS.label),key=str)],population='LOCAL' if str(c).startswith(NS) else 'EXTERNAL_REDECLARATION',source_sha256=pin['sha256'],source_locator=str(c),definition_annotations=annotations,definition_state='COMMENT_CANDIDATE' if annotations else 'NOT_REPORTED_IN_SELECTED_ROOT',deprecated=[str(o) for o in g.objects(c,OWL.deprecated)],axioms=axioms,axiom_sha256=stable(axioms)))
 props=sorted({x for x in g.subjects(RDF.type,OWL.ObjectProperty) if isinstance(x,URIRef)},key=str)
 properties=[dict(iri=str(p),axioms={str(k):sorted([expression(g,o) for o in g.objects(p,k)],key=lambda x:json.dumps(x,sort_keys=True)) for k in [RDFS.domain,RDFS.range,RDFS.subPropertyOf,OWL.inverseOf,RDF.type]}) for p in props]
 refs=set()
 for p in [RDFS.subClassOf,OWL.equivalentClass,OWL.disjointWith,OWL.someValuesFrom,OWL.allValuesFrom,RDFS.domain,RDFS.range]:
  refs|={x for x in g.objects(None,p) if isinstance(x,URIRef) and not str(x).startswith('http://www.w3.org/2001/XMLSchema#')}
 local=[x for x in rows if x['population']=='LOCAL']
 direct=sorted(str(x) for x in g.objects(None,OWL.imports));mapping={x[1]['ontology_iri']:n for n,x in data.items()};seen=set();pending=[pin['ontology_iri']]
 while pending:
  iri=pending.pop()
  if iri in seen:continue
  if iri not in mapping:raise ValueError('Unresolved supplied import '+iri)
  seen.add(iri);pending.extend(str(x) for x in data[mapping[iri]][2].objects(None,OWL.imports))
 modules=[dict(filename=mapping[i],ontology_iri=i,sha256=data[mapping[i]][1]['sha256'],version=data[mapping[i]][1]['version_info'],role='SELECTED_ROOT' if i==pin['ontology_iri'] else 'DIRECT_IMPORT' if i in direct else 'TRANSITIVE_DEPENDENCY') for i in sorted(seen)]
 declared=set().union(*[{x for x in data[mapping[i]][2].subjects(RDF.type,OWL.Class) if isinstance(x,URIRef)} for i in seen])
 out=receipt('RDF_CENSUS_AND_ALL_SELECTED_DECLARATIONS');out.update(source_sha256=pin['sha256'],namespace=NS,version=pin['version_info'],imports=direct,modules=modules,counts=dict(local_classes=len(local),external_class_redeclarations=len(rows)-len(local),local_comment_candidates=sum(bool(x['definition_annotations']) for x in local),local_object_properties=sum(str(p).startswith(NS) for p in props),external_object_properties=sum(not str(p).startswith(NS) for p in props),datatype_properties=len(set(g.subjects(RDF.type,OWL.DatatypeProperty))),explicit_root_triples=len(g),closure_unique_declared_classes=len(declared)),classes=rows,object_properties=properties,referenced_not_declared_in_root=sorted(str(x) for x in refs-set(classes)),referenced_not_declared_in_closure=sorted(str(x) for x in refs-declared),unresolved_imports=[],inferred_class_count=None,reasoner_execution='NOT_EXECUTED_BY_CENSUS',foundation='DOLCE-Lite supplied 397-family modules; not DUL or a proven 2003 byte-identical edition')
 return out
def fixtures():
 from rdflib import Graph,Namespace,RDF,OWL,BNode
 N=Namespace(NS);T=Namespace('urn:clariceptify:dns235:');cases=[]
 def typ(g,n,c):g.add((T[n],RDF.type,N[c]))
 def edge(g,a,p,b):g.add((T[a],N[p],T[b]))
 def empty(g,n,p):
  b=BNode();g.add((T[n],RDF.type,b));g.add((b,RDF.type,OWL.Restriction));g.add((b,OWL.onProperty,N[p]));g.add((b,OWL.allValuesFrom,OWL.Nothing))
 def neg(g,a,p,b):
  x=BNode();g.add((x,RDF.type,OWL.NegativePropertyAssertion));g.add((x,OWL.sourceIndividual,T[a]));g.add((x,OWL.assertionProperty,N[p]));g.add((x,OWL.targetIndividual,T[b]))
 def case(i,q,e,fn):
  g=Graph();fn(g)
  # A separately loaded fixture must declare its existing source properties;
  # otherwise this older RDF loader may classify positive edges as annotations.
  used={p for p in g.predicates() if str(p).startswith(NS)}
  used|={p for pred in [OWL.onProperty,OWL.assertionProperty] for p in g.objects(None,pred)}
  for p in used:g.add((p,RDF.type,OWL.ObjectProperty))
  cases.append((i,q,e,g))
 case('baseline','Q01',True,lambda g:None)
 case('information-object-alone','Q01',True,lambda g:typ(g,'x','information-object'))
 case('description-alone','Q01',True,lambda g:typ(g,'x','description'))
 case('situation-witnesses','Q04',True,lambda g:typ(g,'s','situation'))
 case('situation-no-description','Q04',False,lambda g:(typ(g,'s','situation'),empty(g,'s','satisfies')))
 case('concept-no-description','Q02',False,lambda g:(typ(g,'c','concept'),empty(g,'c','defined-by')))
 case('classification-inverse','Q03',False,lambda g:(edge(g,'c','classifies','x'),neg(g,'x','classified-by','c')))
 case('parameter-no-value','Q07',False,lambda g:(typ(g,'p','parameter'),empty(g,'p','valued-by')))
 case('role-no-player','Q07',True,lambda g:(typ(g,'r','role'),empty(g,'r','played-by')))
 case('course-no-sequenced-event','Q07',True,lambda g:(typ(g,'r','course'),empty(g,'r','sequences')))
 case('description-no-agent','Q02',False,lambda g:(typ(g,'d','description'),empty(g,'d','internally-represented-in')))
 case('satisfaction-inverse','Q04',False,lambda g:(edge(g,'s','satisfies','d'),neg(g,'d','satisfied-by','s')))
 case('component-inverse','Q06',False,lambda g:(edge(g,'a','temporary-component','b'),neg(g,'b','temporary-component-of','a')))
 case('component-chain-no-shortcut','Q06',True,lambda g:(edge(g,'a','temporary-component','b'),edge(g,'b','temporary-component','c'),neg(g,'a','temporary-component','c')))
 case('message-description-separation','Q08',False,lambda g:(typ(g,'x','information-object'),typ(g,'x','description')))
 return cases
def reason(folder,private):
 import jpype,owlready2,importlib.metadata,subprocess
 from rdflib import Graph
 from rdflib.compare import to_canonical_graph
 data=inputs(folder);private=Path(private).resolve();private.mkdir(parents=True,exist_ok=True)
 for n,(raw,pin,g) in data.items():(private/n).write_bytes(raw)
 jar=Path(owlready2.__file__).parent/'hermit/HermiT.jar';jpype.startJVM(classpath=[str(jar)])
 J=jpype.JClass;IRI=J('org.semanticweb.owlapi.model.IRI');File=J('java.io.File');Manager=J('org.semanticweb.owlapi.apibinding.OWLManager');Mapper=J('org.semanticweb.owlapi.util.SimpleIRIMapper');Reasoner=J('org.semanticweb.HermiT.Reasoner')
 def load():
  m=Manager.createOWLOntologyManager()
  for n,(_,pin,_) in data.items():m.addIRIMapper(Mapper(IRI.create(pin['ontology_iri']),IRI.create(File(str(private/n)))))
  return m,m.loadOntologyFromOntologyDocument(File(str(private/'ExtendedDnS.owl')))
 out=receipt('OFFLINE_EXACT_IMPORT_CLOSURE_PROFILE_AND_HERMIT');out.update(source_sha256=data['ExtendedDnS.owl'][1]['sha256'],source_module_hashes={n:p['sha256'] for n,(_,p,_) in data.items()},rdflib=importlib.metadata.version('rdflib'),jpype=importlib.metadata.version('JPype1'),owlready2=importlib.metadata.version('owlready2'),hermit_jar_sha256=sha(jar.read_bytes()),hermit='1.3.8.1099 bundled manifest',java_version=subprocess.run(['java','-version'],capture_output=True,text=True).stderr.strip(),import_policy='Unchanged source RDF/XML, exact offline ontology-IRI maps; no import deletion, URL rewrite or source axiom repair. Only selected root imports are loaded.',tests=[])
 m,o=load();profile=J('org.semanticweb.owlapi.profiles.OWL2DLProfile')().checkOntology(o);violations=[str(x) for x in profile.getViolations()]
 out.update(owl2_dl_profile_pass=bool(profile.isInProfile()),profile_violation_count=len(violations),profile_violations=sorted(violations),loaded_imports=sorted(str(x.getOntologyID().getOntologyIRI()) for x in o.getImportsClosure()))
 try:
  r=Reasoner(o);out['baseline_consistent']=bool(r.isConsistent());out['unsatisfiable_named_classes']=sorted(str(c.getIRI()) for c in r.getUnsatisfiableClasses().getEntitiesMinusBottom()) if out['baseline_consistent'] else None;r.dispose();out['baseline_error']=None
 except Exception as e:out.update(baseline_consistent=None,unsatisfiable_named_classes=None,baseline_error=str(e)[:2000])
 for ident,q,expected,g in fixtures():
  nt='\n'.join(sorted(to_canonical_graph(g).serialize(format='nt').splitlines()))+'\n' if len(g) else ''
  observed=None;error=None
  try:
   mm,oo=load()
   if nt:
    f=private/(ident+'.ttl');f.write_text(nt);fo=mm.loadOntologyFromOntologyDocument(File(str(f)));mm.addAxioms(oo,fo.getAxioms())
   rr=Reasoner(oo);observed=bool(rr.isConsistent());rr.dispose()
  except Exception as e:error=str(e)[:2000]
  row=dict(id=ident,question=q,expected_consistent=expected,observed_consistent=observed,error=error,fixture_nt=nt,fixture_sha256=sha(nt.encode()),result='ERROR' if error else 'PASS' if observed is expected else 'FAIL');out['tests'].append(row);print(ident,row['result'],observed,flush=True)
 out['summary']={k:sum(t['result']==v for t in out['tests']) for k,v in [('passed','PASS'),('failed','FAIL'),('errors','ERROR')]};out['summary']['total']=len(out['tests']);out['claim_limit']='Loaded logical axioms and isolated fixtures only; profile failure, unsatisfiable classes and tool errors remain explicit. Not 2003 FOL validation, source adequacy or accepted alignment.'
 jpype.shutdownJVM();return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('mode',choices=['census','reason']);p.add_argument('--source-dir',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--private-dir',type=Path);a=p.parse_args();d=census(a.source_dir) if a.mode=='census' else reason(a.source_dir,a.private_dir);dump(a.output,d)
