"""Inspect exact EmotionsCognition 2015/12 bytes and pinned direct legacy imports offline."""
from pathlib import Path
import argparse, hashlib, json
from rdflib import Graph, RDF, RDFS, OWL, URIRef, BNode

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    'EmotionsCognition-2015.owl': '0e19f81a2933032def83bd579e0f6bfc125b0be944fa8cfd27639a6319f041c2',
    'EmotionsCognition-current.owl': '0e19f81a2933032def83bd579e0f6bfc125b0be944fa8cfd27639a6319f041c2',
    'DUL.owl': 'b27e0111f1201d8815d6a68fdf1c3d8eaa9f34327bece17c75a3410fbe626485',
    'IOLite.owl': '98b9ddcbfdef997f89668c3738f9343ff8ce15079acca023bd6f870e0173e075',
    'ofntb.owl': 'd223c298e8c1997e02f9a538289f766bbdb744c1094454a44f46e7d55a50d289',
}
NS = 'http://rhizomik.net/ontologies/emotions&cognitionontology.owl#'
IMPORTS = {'http://www.loa-cnr.it/ontologies/DUL.owl': 'DUL.owl',
           'http://www.loa-cnr.it/ontologies/IOLite.owl': 'IOLite.owl',
           'http://www.loa-cnr.it/codeps/owl/ofntb.owl': 'ofntb.owl'}


def inspect(folder):
    import jpype, owlready2
    graphs = {}
    for name, digest in FILES.items():
        b = (folder/name).read_bytes()
        if hashlib.sha256(b).hexdigest() != digest:
            raise ValueError(f'Pinned source mismatch: {name}')
        graphs[name] = Graph().parse(data=b, format='xml')
    g=graphs['EmotionsCognition-2015.owl']
    if (folder/'EmotionsCognition-2015.owl').read_bytes() != (folder/'EmotionsCognition-current.owl').read_bytes():
        raise ValueError('Current and dated bytes differ')
    predecessor=folder/'EmotionsOnto-2015May.owl'
    if hashlib.sha256(predecessor.read_bytes()).hexdigest()!='fa719ad28a2eb6acb1d335542a70a36edf6be9f8477ac4354d79cf9815d700d7':raise ValueError('Predecessor bytes differ')
    previous_graph=Graph().parse(predecessor,format='xml')
    actual_imports = sorted(str(v) for v in g.objects(None, OWL.imports))
    if actual_imports != sorted(IMPORTS):
        raise ValueError('Direct import set changed')
    declared = {s for s in g.subjects(RDF.type, OWL.Class) if isinstance(s, URIRef)}
    local = sorted((s for s in declared if str(s).startswith(NS)), key=str)
    external = sorted(declared - set(local), key=str)
    if len(local) != 33 or external:
        raise ValueError('Unexpected declared class population')
    def expression(o):
        if isinstance(o,URIRef): return {'iri':str(o)}
        if isinstance(o,BNode):
            return {'restriction':{str(p):[str(v) for v in g.objects(o,p)] for p in (OWL.onProperty,OWL.allValuesFrom,OWL.someValuesFrom,OWL.cardinality,OWL.minCardinality,OWL.maxCardinality) if list(g.objects(o,p))}}
        return {'literal':str(o)}
    rows=[]
    for c in local:
        comments=[str(v) for v in g.objects(c,RDFS.comment)]
        rows.append(dict(iri=str(c), population='LOCAL_DECLARED', label=[str(v) for v in g.objects(c,RDFS.label)], source_comments=comments,
                         definition_status='COMMENT_CANDIDATE' if comments else 'NO_SOURCE_COMMENT_OR_DEFINITION_IN_SELECTED_ROOT',
                         source_locator=f'EmotionsCognition-2015.owl::<{c}> rdfs:comment' if comments else None,
                         short_paraphrase='An objective reference frame, according to the source comment.' if str(c).endswith('#EnvironmentalContext') else None,
                         subclass_of=[expression(o) for o in g.objects(c,RDFS.subClassOf)],
                         equivalent_class=[expression(o) for o in g.objects(c,OWL.equivalentClass)],
                         deprecated=any(str(v).lower()=='true' for v in g.objects(c,OWL.deprecated))))
    named_refs={o for c in local for o in g.objects(c,RDFS.subClassOf) if isinstance(o,URIRef) and not str(o).startswith(NS)}
    imports=[]
    for iri,name in sorted(IMPORTS.items()):
        h=graphs[name]; cs={c for c in h.subjects(RDF.type,OWL.Class) if isinstance(c,URIRef)}
        imports.append(dict(iri=iri, acquired_filename=name, sha256=FILES[name], bytes=(folder/name).stat().st_size, triples=len(h), local_declared_classes=len(cs), source_comment_candidates=sum(bool(list(h.objects(c,RDFS.comment))) for c in cs), ontology_version_info=[str(v) for v in h.objects(URIRef(iri),OWL.versionInfo) if len(str(v))<160], declared_imports=sorted(str(v) for v in h.objects(None,OWL.imports))))
    old_names={str(c).split('#')[-1] for c in previous_graph.subjects(RDF.type,OWL.Class) if isinstance(c,URIRef)}
    new_names={str(c).split('#')[-1] for c in local}
    references=[]
    for c in sorted(named_refs,key=str):
        matches=[(name,h) for name,h in graphs.items() if name in ('DUL.owl','IOLite.owl','ofntb.owl') and (c,RDF.type,OWL.Class) in h]
        references.append(dict(iri=str(c), declared_in=[name for name,_ in matches], definition_comments=[{'module':name,'comment':str(v),'locator':f'{name}::<{c}> rdfs:comment'} for name,h in matches for v in h.objects(c,RDFS.comment)], missing_in_selected_imports=not bool(matches)))
    selected=[('C01','Perception','hasInput','allValuesFrom','Sensation'),('C02','Perception','hasOutput','allValuesFrom','http://www.loa-cnr.it/ontologies/DUL.owl#Description'),('C03','Perception','uses','allValuesFrom','Memory'),('C04','Memory','stores','allValuesFrom','http://www.loa-cnr.it/ontologies/DUL.owl#Description'),('C05','Motivation','threshold','minCardinality','1'),('C06','EmotionExpressionSystem','hasInput','allValuesFrom','Emotion'),('C07','EmotionExpressionSystem','hasOutput','allValuesFrom','Stimulus'),('C08','Sensor','hasInput','allValuesFrom','Stimulus')]
    checks=[]
    for i,cls,prop,pred,val in selected:
        c=URIRef(NS+cls);property_iri=URIRef(NS+prop);p=getattr(OWL,pred);target=URIRef(val if val.startswith('http') else NS+val) if pred=='allValuesFrom' else None
        matches=[o for o in g.objects(c,RDFS.subClassOf) if isinstance(o,BNode) and (o,OWL.onProperty,property_iri) in g and ((o,p,target) in g if target else any(str(v)==val for v in g.objects(o,p)))]
        if len(matches)!=1: raise ValueError('Commitment mismatch '+i)
        checks.append(dict(id=i,class_iri=str(c),property_iri=str(property_iri),predicate_iri=str(p),target=str(target) if target else val,locator=f'EmotionsCognition-2015.owl::<{c}> rdfs:subClassOf [owl:onProperty <{property_iri}>; <{p}> {target if target else val}]',observed='ASSERTED_ONCE',semantic_limit='allValuesFrom is vacuous without a property filler' if pred=='allValuesFrom' else 'minCardinality is open-world and does not require a named literal in assertions'))
    jar=Path(owlready2.__file__).parent/'hermit/HermiT.jar'
    if not jpype.isJVMStarted():jpype.startJVM(classpath=[str(jar)])
    J=jpype.JClass;File=J('java.io.File');IRI=J('org.semanticweb.owlapi.model.IRI');Mapper=J('org.semanticweb.owlapi.util.SimpleIRIMapper');manager=J('org.semanticweb.owlapi.apibinding.OWLManager').createOWLOntologyManager()
    for iri,name in IMPORTS.items(): manager.addIRIMapper(Mapper(IRI.create(iri),IRI.create(File(str((folder/name).resolve())))))
    ontology=manager.loadOntologyFromOntologyDocument(File(str((folder/'EmotionsCognition-2015.owl').resolve())))
    closure=list(ontology.getImportsClosure());profile=J('org.semanticweb.owlapi.profiles.OWL2DLProfile')().checkOntology(ontology);violations=list(profile.getViolations());types={}
    for v in violations:
        name=str(v.getClass().getSimpleName());types[name]=types.get(name,0)+1
    return dict(issue=239,source_hashes=FILES,predecessor=dict(url='https://rhizomik.net/ontologies/2015/05/emotionsonto.owl',sha256='fa719ad28a2eb6acb1d335542a70a36edf6be9f8477ac4354d79cf9815d700d7',declared_local_classes=len(old_names),shared_local_names=len(old_names&new_names),later_only_names=sorted(new_names-old_names),earlier_only_names=sorted(old_names-new_names),original_2014_bytes_equivalence='NOT_ESTABLISHED'),source_root=NS[:-1],triples=len(g),classes=rows,selected_commitments=checks,external_named_superclasses=references,imports=imports,population=dict(local_named_classes=len(local),external_redeclarations=len(external),direct_import_module_declared_class_occurrences=sum(m['local_declared_classes'] for m in imports),inferred_classes=None,local_comment_candidates=sum(bool(r['source_comments']) for r in rows),referenced_external_named_superclasses=len(references),local_object_properties=sum(str(c).startswith(NS) for c in set(g.subjects(RDF.type,OWL.ObjectProperty)) if isinstance(c,URIRef)),local_datatype_properties=sum(str(c).startswith(NS) for c in set(g.subjects(RDF.type,OWL.DatatypeProperty)) if isinstance(c,URIRef))),execution=dict(import_closure_ontologies=len(closure),owl2_dl_profile='PASS' if profile.isInProfile() else 'FAIL',profile_violations=len(violations),violation_types=types,reasoner='NOT_EXECUTED_PROFILE_FAIL' if violations else 'NOT_EXECUTED',validation='NOT_EXECUTED',source_byte_equality='DATED_AND_CURRENT_IDENTICAL',owlapi_jar_sha256=hashlib.sha256(jar.read_bytes()).hexdigest()))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('source_dir',type=Path);parser.add_argument('--output',type=Path,default=ROOT/'evaluation/related-work/emotions239/census.json');args=parser.parse_args();r=inspect(args.source_dir);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n');print(json.dumps({k:r[k] for k in ('population','execution')},indent=2))
