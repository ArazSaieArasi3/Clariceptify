"""Inventory selected DUL chapter pattern files, without fetching or reasoning.
Inputs remain private. Only structural metadata, annotation hashes and short
version numbers are emitted. Does not establish original 2016 byte identity.
"""
from pathlib import Path
import argparse,hashlib,json,re
from rdflib import Graph,URIRef,BNode,Literal,OWL,RDF,RDFS
from rdflib.compare import to_canonical_graph
ROOTS=['description.owl','informationrealization.owl','participation.owl','collectionentity.owl','partof.owl','componency.owl','sequence.owl','basicplan.owl','timeindexedparticipation.owl']
DUL='http://www.ontologydesignpatterns.org/ont/dul/DUL.owl'
def sha(b):return hashlib.sha256(b).hexdigest()
def run(folder):
 graphs={};rows=[];queue=list(ROOTS);unresolved=[]
 while queue:
  name=queue.pop(0)
  if name in graphs:continue
  path=folder/name
  if not path.is_file():unresolved.append(name);continue
  raw=path.read_bytes();g=to_canonical_graph(Graph().parse(data=raw,format='xml'));graphs[name]=g
  imports=sorted(map(str,g.objects(None,OWL.imports)))
  for u in imports:
   if not u.startswith('http://www.ontologydesignpatterns.org/'):raise ValueError('Unexpected import authority')
   queue.append(u.rsplit('/',1)[-1])
  iris=sorted(str(s) for s in g.subjects(RDF.type,OWL.Ontology) if isinstance(s,URIRef))
  classes=sorted(str(s) for kind in [OWL.Class,RDFS.Class] for s in g.subjects(RDF.type,kind) if isinstance(s,URIRef));classes=sorted(set(classes))
  ns=[u+'#' for u in iris]
  annotations=sorted(str(o) for o in g.objects(None,OWL.versionInfo))
  rows.append(dict(filename=name,source_url=iris[0] if len(iris)==1 else None,sha256=sha(raw),bytes=len(raw),ontology_iris=iris,version_annotation_sha256=sha(json.dumps(annotations,separators=(',',':')).encode()),short_version_labels=sorted({v for a in annotations for v in re.findall(r'(?m)^(\d+\.\d+)(?:\s|$)',a)}),explicit_triples=len(g),declared_imports=imports,local_class_iris=[c for c in classes if any(c.startswith(n) for n in ns)],external_class_redeclarations=[c for c in classes if not any(c.startswith(n) for n in ns)],object_properties=sorted(str(s) for s in g.subjects(RDF.type,OWL.ObjectProperty)),datatype_properties=sorted(str(s) for s in g.subjects(RDF.type,OWL.DatatypeProperty)),header_license_rights_annotations=[dict(predicate=str(p),value=str(o)) for s in map(URIRef,iris) for p,o in g.predicate_objects(s) if any(t in str(p).lower() for t in ['license','rights'])]))
 def closure(name):
  seen=set();todo=[name]
  while todo:
   n=todo.pop()
   if n in seen:continue
   seen.add(n)
   if n in graphs:todo.extend(u.rsplit('/',1)[-1] for u in map(str,graphs[n].objects(None,OWL.imports)))
  union=Graph()
  for n in sorted(seen):
   if n in graphs:
    def apart(node):
     return BNode(sha((n+'|'+str(node)).encode())) if isinstance(node,BNode) else node
    for s,p,o in graphs[n]:union.add((apart(s),p,apart(o)))
  cls=sorted({str(s) for k in [OWL.Class,RDFS.Class] for s in union.subjects(RDF.type,k) if isinstance(s,URIRef)})
  return dict(root=name,files=sorted(seen),unresolved_files=sorted(seen-set(graphs)),unique_declared_class_iris=cls,unique_declared_classes=len(cls),asserted_union_triples=len(union),scope='Asserted union only, no inferred classes or completed imported glossary')
 def expression(g,n,seen=frozenset()):
  if isinstance(n,URIRef):return {'iri':str(n)}
  if isinstance(n,Literal):return {'literal':str(n),'datatype':str(n.datatype) if n.datatype else None,'language':n.language}
  if n in seen:return {'cycle':True}
  return {'anonymous_expression':[{'predicate':str(p),'object':expression(g,o,seen|{n})} for p,o in sorted(g.predicate_objects(n),key=lambda x:tuple(map(str,x))) if p not in [RDFS.comment,RDFS.label]]}
 selected=[]
 for name in ['description.owl','informationrealization.owl','participation.owl','collectionentity.owl','componency.owl','basicplandescription.owl','timeindexedparticipation.owl','timeindexedsituation.owl','timeinterval.owl']:
  g=graphs[name]
  for s in sorted(set(g.subjects(RDF.type,OWL.Class)),key=str):
   if not isinstance(s,URIRef):continue
   for p,o in sorted(g.predicate_objects(s),key=lambda x:tuple(map(str,x))):
    if p in [RDFS.subClassOf,OWL.equivalentClass,OWL.disjointWith]:selected.append(dict(file=name,subject=str(s),predicate=str(p),object=expression(g,o)))
 return dict(schema_version='1.0',issue=88,checked_on='2026-10-29',generator_path='tools/inspect_dul_modules.py',generator_sha256=sha(Path(__file__).read_bytes()),roots=ROOTS,modules=sorted(rows,key=lambda x:x['filename']),closures=[closure(n) for n in ROOTS],unresolved=sorted(set(unresolved)),selected_explicit_axioms=selected,source_redistributed=False,inference='NOT_EXECUTED',historical_2016_byte_parity='NOT_ESTABLISHED',raw_annotations='NOT_REDISTRIBUTED',license_conclusion='Header absence is not a legal determination. No third-party source is relicensed or redistributed.',definition_scope='DUL root glossary is separate. This receipt inventories selected pattern declarations and import closure; it is not a completed glossary of every pattern class.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source-dir',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=run(a.source_dir);a.output.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'modules':len(r['modules']),'unresolved':r['unresolved'],'roots':len(ROOTS)}))
