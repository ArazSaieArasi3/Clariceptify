"""Run bounded consistency/countermodel tests on exact retained DUL4.2.

Private inputs are never fetched or redistributed. Requires rdflib7.6.0,
owlready2 0.51 and Java. No Clariceptify model is loaded or changed.
"""
from pathlib import Path
import argparse,contextlib,hashlib,io,json,platform,subprocess,tempfile,time
import rdflib,owlready2
from rdflib import Graph,Namespace,RDF,RDFS,OWL,BNode,Literal,URIRef
from rdflib.compare import to_canonical_graph
D=Namespace('http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#')
T=Namespace('urn:clariceptify:dul-review:')
EXPECTED='e5f6429596d2c7014730bad85aaaa9c39530235f27f596cd0e7ce85e6bbcba66'
def digest(b):return hashlib.sha256(b).hexdigest()
def typed(g,n,*classes):
 for c in classes:g.add((T[n],RDF.type,D[c]))
def edge(g,a,p,b):g.add((T[a],D[p],T[b]))
def negative(g,a,p,b):
 n=BNode();g.add((n,RDF.type,OWL.NegativePropertyAssertion));g.add((n,OWL.sourceIndividual,T[a]));g.add((n,OWL.assertionProperty,D[p]));g.add((n,OWL.targetIndividual,T[b]))
def no_values(g,n,p,cls='Thing'):
 b=BNode();g.add((T[n],RDF.type,b));g.add((b,RDF.type,OWL.Restriction));g.add((b,OWL.onProperty,D[p]));g.add((b,OWL.allValuesFrom,OWL.Nothing))
def some(g,n,p,cls='Entity'):
 b=BNode();g.add((T[n],RDF.type,b));g.add((b,RDF.type,OWL.Restriction));g.add((b,OWL.onProperty,D[p]));g.add((b,OWL.someValuesFrom,D[cls]))
def cases():
 rows=[]
 def case(id,q,expected,description,fn):
  g=Graph();fn(g);rows.append((id,q,expected,description,g))
 case('baseline','Q01',True,'Full retained DUL4.2 without added individuals',lambda g:None)
 for a,b,ok in [('Description','Concept',True),('InformationObject','Description',True),('InformationObject','Concept',True),('InformationObject','InformationRealization',False),('SocialObject','PhysicalObject',False)]:
  case('coinstance-'+a+'-'+b,'Q02' if a!='SocialObject' else 'Q04',ok,'Named individual in both exact root classes',lambda g,a=a,b=b:typed(g,'x',a,b))
 case('parthood-projection','Q03',False,'Reified Parthood must project a binary hasPart edge via the exact source property chain',lambda g:(typed(g,'p','Parthood'),edge(g,'p','includesWhole','a'),edge(g,'p','includesPart','b'),negative(g,'a','hasPart','b')))
 case('parthood-key-distinct-contexts','Q03',False,'Two named Parthood records sharing part and whole but declared different violate the source key even with different time witnesses',lambda g:(typed(g,'p','Parthood'),typed(g,'q','Parthood'),edge(g,'p','includesWhole','a'),edge(g,'q','includesWhole','a'),edge(g,'p','includesPart','b'),edge(g,'q','includesPart','b'),edge(g,'p','includesTime','t1'),edge(g,'q','includesTime','t2'),g.add((T.t1,OWL.differentFrom,T.t2)),g.add((T.p,OWL.differentFrom,T.q))))
 case('parthood-key-merge-control','Q03',True,'Distinct time witnesses remain consistent when shared-part/whole records may identify; isolates key-forced equality from temporal inconsistency',lambda g:(typed(g,'p','Parthood'),typed(g,'q','Parthood'),edge(g,'p','includesWhole','a'),edge(g,'q','includesWhole','a'),edge(g,'p','includesPart','b'),edge(g,'q','includesPart','b'),edge(g,'p','includesTime','t1'),edge(g,'q','includesTime','t2'),g.add((T.t1,OWL.differentFrom,T.t2))))
 case('concept-physical-part','Q04',False,'Concept has a PhysicalObject part, conflicting with Concept-only parts',lambda g:(typed(g,'a','Concept'),typed(g,'b','PhysicalObject'),edge(g,'a','hasPart','b')))
 case('plan-no-components','Q04',False,'Plan asserted to have no component despite existential Goal component',lambda g:(typed(g,'a','Plan'),no_values(g,'a','hasComponent')))
 case('plan-unnamed-goal','Q04',True,'Plan with no named Goal: existential witnesses remain permitted',lambda g:typed(g,'a','Plan'))
 case('collection-unknown-members','Q05',True,'Collection without membership facts',lambda g:typed(g,'a','Collection'))
 case('collection-empty','Q05',True,'Collection explicitly has no members',lambda g:(typed(g,'a','Collection'),no_values(g,'a','hasMember')))
 case('collection-existential-member','Q05',True,'Collection with existential but unnamed member',lambda g:(typed(g,'a','Collection'),some(g,'a','hasMember')))
 case('collection-empty-and-existential','Q05',False,'Explicit empty membership contradicts an added existential membership requirement',lambda g:(typed(g,'a','Collection'),some(g,'a','hasMember'),no_values(g,'a','hasMember')))
 for c,p,ok in [('Object','isParticipantIn',False),('Event','hasParticipant',False),('InformationRealization','realizes',False),('InformationObject','isRealizedBy',True)]:
  case('no-witness-'+c,'Q05',ok,'Assert no values for '+p+' on '+c,lambda g,c=c,p=p:(typed(g,'a',c),no_values(g,'a',p)))
 for p,ok in [('hasComponent',True),('hasPart',False),('precedes',False),('overlaps',True),('directlyPrecedes',True)]:
  case('chain-without-shortcut-'+p,'Q06',ok,'Two edges plus explicit denial of shortcut; consistency means a countermodel exists, not universal absence',lambda g,p=p:(edge(g,'a',p,'b'),edge(g,'b',p,'c'),negative(g,'a',p,'c')))
 case('component-chain-with-shortcut','Q06',True,'Component triangle is allowed, so chain does not impose intransitivity',lambda g:(edge(g,'a','hasComponent','b'),edge(g,'b','hasComponent','c'),edge(g,'a','hasComponent','c')))
 case('component-reverse','Q06',False,'Opposite component edges violate asymmetry',lambda g:(edge(g,'a','hasComponent','b'),edge(g,'b','hasComponent','a')))
 case('precedence-cycle','Q06',True,'Precedence cycle is not excluded by transitivity alone',lambda g:(edge(g,'a','precedes','b'),edge(g,'b','precedes','a')))
 case('overlap-deny-inverse','Q06',False,'Deny inverse of asserted overlap, conflicting with symmetry',lambda g:(edge(g,'a','overlaps','b'),negative(g,'b','overlaps','a')))
 return rows

def run(source,output,private_dir):
 raw=source.read_bytes()
 if digest(raw)!=EXPECTED:raise ValueError('DUL source digest mismatch')
 base=Graph().parse(data=raw,format='turtle')
 if list(base.objects(None,OWL.imports)):raise ValueError('Unexpected root imports')
 private_dir.mkdir(parents=True,exist_ok=True)
 results=[]
 for ident,q,expected,description,fixture in cases():
  cg=to_canonical_graph(fixture);nt=''.join(sorted(cg.serialize(format='nt').splitlines(True)))
  g=base+fixture;p=private_dir/(ident+'.rdf');g.serialize(p,format='xml')
  world=owlready2.World();world.get_ontology(p.as_uri()).load()
  stdout,stderr=io.StringIO(),io.StringIO();start=time.monotonic();observed=None;error=None;unsat=None
  with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):
   try:
    owlready2.sync_reasoner(world,debug=2)
    observed=True
    unsat=sorted(str(c.iri) for c in world.inconsistent_classes())
   except owlready2.OwlReadyInconsistentOntologyError:observed=False
   except Exception as e:error=type(e).__name__+': '+str(e)
  logs=stdout.getvalue()+stderr.getvalue();(private_dir/(ident+'.log')).write_text(logs)
  row=dict(id=ident,question=q,description=description,fixture_nt=nt,fixture_sha256=digest(nt.encode()),combined_rdf_sha256=digest(p.read_bytes()),expected_consistent=expected,observed_consistent=observed,result='PASS' if observed is expected else 'ERROR' if error else 'FAIL',error=error,unsatisfiable_classes_if_consistent=unsat,log_sha256=digest(logs.encode()),seconds=round(time.monotonic()-start,3))
  results.append(row);print(ident,row['result'],observed,flush=True)
  world.close()
 import importlib.metadata
 jar=Path(owlready2.__file__).parent/'hermit/HermiT.jar'
 report=dict(schema_version='1.0',issue=88,source_sha256=EXPECTED,source_triples=len(base),source_imports=[],input_policy='Exact whole DUL4.2 RDF graph plus each isolated review fixture; Turtle serialized to RDF/XML without deleting source axioms. Fixtures are research tests, not Clariceptify model fixtures.',generator_sha256=digest(Path(__file__).read_bytes()),generator_path='tools/inspect_dul_semantics.py',python=platform.python_version(),rdflib=rdflib.__version__,owlready2=importlib.metadata.version('owlready2'),hermit_jar_sha256=digest(jar.read_bytes()),java_version=subprocess.run(['java','-version'],capture_output=True,text=True).stderr.strip(),reasoner='Bundled HermiT via owlready2.sync_reasoner',reasoner_options='-c -O -D -I',tests=results,summary=dict(total=len(results),passed=sum(r['result']=='PASS' for r in results),failed=sum(r['result']=='FAIL' for r in results),errors=sum(r['result']=='ERROR' for r in results)),limits=['Checks selected countermodels and contradictions; not full paper/artifact equivalence or empirical validation.','Consistency does not establish intended-model adequacy. No independent OWL2 profile validator run.','Inferred class populations are not claimed from these tests; no Clariceptify artifacts or imported IOLite definitions are evaluated.','Log and complete combined source graphs retained privately; original third-party ontology is not republished.'])
 output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 return report
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--private-dir',type=Path,required=True);a=p.parse_args();r=run(a.source,a.output,a.private_dir.resolve());raise SystemExit(r['summary']['failed']+r['summary']['errors']!=0)
