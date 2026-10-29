"""Inspect only hash-pinned IOLite/LMM sources, with no network or inference.

Requires research dependencies only when actual source parsing is requested.
Raw comments remain private; only annotation hashes and structural data returned.
"""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
NS='http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl#'
SHA='15f8ac177bc2b481e13f326cdccd0c9551f0721506adbac10ea694778a35f23f'
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
def inspect(source_dir):
 import yaml
 specs=yaml.safe_load((ROOT/'evidence/related-work/corpus/lmm-inputs.yaml').read_text())['artifacts']
 raws={}
 for s in specs:
  raw=(Path(source_dir)/s['filename']).read_bytes()
  if hashlib.sha256(raw).hexdigest()!=s['sha256']:raise ValueError('Selected source digest differs: '+s['id'])
  raws[s['id']]=raw
 import rdflib
 from rdflib import Graph,URIRef,BNode,Literal,RDF,RDFS,OWL,XSD
 graphs={s['id']:Graph().parse(data=raws[s['id']],format=s['format']) for s in specs}
 declared=lambda g:{str(x) for k in (OWL.Class,RDFS.Class) for x in g.subjects(RDF.type,k) if isinstance(x,URIRef)}
 g=graphs['IOLite']; local=sorted(x for x in declared(g) if x.startswith(NS)); rows=[]
 for iri in local:
  c=URIRef(iri); comments=sorted(g.objects(c,RDFS.comment),key=lambda x:(x.language or '',str(x))); en=sorted(str(x) for x in g.objects(c,RDFS.label) if x.language=='en')
  ann=[{'predicate':str(RDFS.comment),'language':x.language,'datatype':str(x.datatype) if x.datatype else None,'characters':len(str(x)),'text_sha256':hashlib.sha256(str(x).encode()).hexdigest()} for x in comments]
  rows.append({'iri':iri,'label':en[0] if en else iri[len(NS):],'label_basis':'SOURCE_ENGLISH_LABEL' if en else 'IRI_LOCAL_NAME','annotation_records':ann,'annotation_sha256':hashlib.sha256(json.dumps(sorted(str(x) for x in comments),ensure_ascii=False,separators=(',',':')).encode()).hexdigest() if comments else None,'named_superclasses':sorted(str(x) for x in g.objects(c,RDFS.subClassOf) if isinstance(x,URIRef)),'equivalent_expressions':len(set(g.objects(c,OWL.equivalentClass))),'deprecated':any(str(x).lower() in ['true','1'] for x in g.objects(c,OWL.deprecated))})
 referenced=set()
 for s,p,o in g:
  if p in (RDFS.subClassOf,OWL.equivalentClass,OWL.disjointWith,OWL.complementOf,OWL.onClass,OWL.someValuesFrom,OWL.allValuesFrom) and isinstance(o,URIRef):referenced.add(str(o))
  if p in (RDFS.domain,RDFS.range) and isinstance(o,URIRef) and (p==RDFS.domain or (s,RDF.type,OWL.ObjectProperty) in g):referenced.add(str(o))
  if p in (OWL.unionOf,OWL.intersectionOf,OWL.members) and (p!=OWL.members or (s,RDF.type,OWL.AllDisjointClasses) in g):referenced.update(str(x) for x in g.items(o) if isinstance(x,URIRef))
 builtin={x for x in referenced|declared(g) if x.startswith((str(OWL),str(RDF),str(RDFS),str(XSD)))}
 pops={'local_named_classes':local,'external_redeclarations':sorted(declared(g)-set(local)),'referenced_undeclared_nonbuiltin_classes':sorted(referenced-declared(g)-builtin),'builtin_class_position_iris':sorted(builtin),'named_rdfs_class_declarations':sorted(str(x) for x in g.subjects(RDF.type,RDFS.Class) if isinstance(x,URIRef)),'anonymous_class_declarations':len({x for k in [OWL.Class,RDFS.Class] for x in g.subjects(RDF.type,k) if isinstance(x,BNode)}),'anonymous_restrictions':len({x for x in g.subjects(RDF.type,OWL.Restriction) if isinstance(x,BNode)}),'deprecated_named_classes':sorted(str(x) for x in g.subjects(OWL.deprecated,None) if isinstance(x,URIRef) and any(str(v).lower() in ['true','1'] for v in g.objects(x,OWL.deprecated)))}
 ids={s['ontology_iri']:s['id'] for s in specs}; modules=[]
 for s in specs:
  graph=graphs[s['id']]; seen=set(); todo=[s['ontology_iri']]; union=set()
  while todo:
   iri=todo.pop()
   if iri in seen:continue
   if iri not in ids:raise ValueError('Unresolved import: '+iri)
   seen.add(iri); cg=graphs[ids[iri]];union|=declared(cg);todo.extend(str(x) for x in cg.objects(None,OWL.imports))
  own=sorted(x for x in declared(graph) if x.startswith(s['namespace']))
  modules.append({'id':s['id'],'source_sha256':s['sha256'],'namespace':s['namespace'],'local_class_iris':own,'external_redeclaration_iris':sorted(declared(graph)-set(own)),'declared_import_iris':sorted(str(x) for x in graph.objects(None,OWL.imports)),'resolved_closure_modules':sorted(ids[x] for x in seen),'asserted_closure_class_iris':sorted(union),'inferred_class_count':None})
 return {'schema_version':'1.0','source_sha256':SHA,'parser':{'name':'rdflib','version':rdflib.__version__},'populations':pops,'rows':rows,'modules':modules,'reasoner_execution':'NOT_EXECUTED','unresolved_imports':[],'scope':'Exact declared populations and assertion-based import closure by unique IRI; not reasoning, historical equivalence or scientific acceptance.','generator':{'path':'tools/inspect_iolite_source.py','sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--source-dir',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=inspect(a.source_dir);a.output.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','local_classes':len(r['rows']),'closure_classes':len(r['modules'][-1]['asserted_closure_class_iris'])}))
