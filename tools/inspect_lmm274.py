"""Pinned LMM1.8/1.2 import closure and isolated OWLAPI/HermiT cases for #274."""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import platform
import subprocess

ROOT = Path(__file__).resolve().parents[1]
L1 = 'http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#'
L2 = 'http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#'
DUL = 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#'
T = 'urn:clariceptify:lmm274:'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def fixtures():
    from rdflib import BNode, Graph, Literal, Namespace, OWL, RDF, RDFS, URIRef
    N1, N2, ND, NT = map(Namespace, (L1, L2, DUL, T))
    cases = []

    def typ(g, name, cls):
        g.add((NT[name], RDF.type, cls))

    def edge(g, a, prop, b):
        g.add((NT[a], prop, NT[b]))

    def no_edge(g, a, prop):
        restriction = BNode()
        g.add((NT[a], RDF.type, restriction))
        g.add((restriction, RDF.type, OWL.Restriction))
        g.add((restriction, OWL.onProperty, prop))
        g.add((restriction, OWL.allValuesFrom, OWL.Nothing))

    def case(name, question, expected, make):
        g = Graph()
        make(g)
        used = {p for p in g.predicates() if str(p).startswith((L1, L2, DUL))}
        used |= {p for p in g.objects(None, OWL.onProperty) if isinstance(p, URIRef)}
        for p in used:
            g.add((p, RDF.type, OWL.ObjectProperty))
        cases.append((name, question, expected, g))

    case('baseline', 'Q01', True, lambda g: None)
    case('expression-denotes', 'Q02', True, lambda g: (typ(g, 'e', N1.Expression), edge(g, 'e', N1.denotes, 'r')))
    case('expression-neither-arm', 'Q02', False, lambda g: (typ(g, 'e', N1.Expression), no_edge(g, 'e', N1.denotes), no_edge(g, 'e', ND.expresses)))
    case('meaning-no-expression', 'Q02', False, lambda g: (typ(g, 'm', N1.Meaning), no_edge(g, 'm', ND.isExpressedBy)))
    case('concept-individual-not-class', 'Q03', True, lambda g: (typ(g, 'c', ND.Concept), typ(g, 'r', N2.IndividualReference), edge(g, 'r', N2.isInstanceOf, 'c')))
    case('context-without-named-interpretation', 'Q04', True, lambda g: typ(g, 'c', N1.Context))
    case('individual-no-concept', 'Q05', False, lambda g: (typ(g, 'r', N2.IndividualReference), no_edge(g, 'r', N2.isInstanceOf)))
    case('individual-no-membership', 'Q05', False, lambda g: (typ(g, 'r', N2.IndividualReference), no_edge(g, 'r', ND.isMemberOf)))
    case('multiple-no-named-member', 'Q05', True, lambda g: typ(g, 'r', N2.MultipleReference))
    case('extensional-no-member', 'Q05', False, lambda g: (typ(g, 'r', N2.ExtensionalReference), no_edge(g, 'r', ND.hasMember)))
    case('name-contextual-same-individual', 'Q06', False, lambda g: (typ(g, 'e', N2.Name), typ(g, 'e', N2.ContextualExpression)))
    case('concept-name-same-individual', 'Q06', False, lambda g: (typ(g, 'e', N2.ConceptExpression), typ(g, 'e', N2.Name)))
    case('same-lexeme-distinct-expressions', 'Q06', True, lambda g: (typ(g, 'n', N2.Name), typ(g, 'c', N2.ConceptExpression), g.add((NT.n, RDFS.label, Literal('bank'))), g.add((NT.c, RDFS.label, Literal('bank'))), g.add((NT.n, OWL.differentFrom, NT.c))))
    return cases


def run(source_dir, private_dir):
    import jpype
    import owlready2
    from rdflib import Graph
    from rdflib.compare import to_canonical_graph
    import yaml

    source_dir, private_dir = Path(source_dir), Path(private_dir)
    private_dir.mkdir(parents=True, exist_ok=True)
    manifest = yaml.safe_load((ROOT / 'evidence/related-work/corpus/lmm-inputs.yaml').read_text())
    raw = {}
    for item in manifest['artifacts']:
        b = (source_dir / item['filename']).read_bytes()
        if digest(b) != item['sha256']:
            raise ValueError('Source hash mismatch: ' + item['id'])
        Graph().parse(data=b, format=item['format'])
        (private_dir / item['filename']).write_bytes(b)
        raw[item['ontology_iri']] = item
    jar = Path(owlready2.__file__).parent / 'hermit/HermiT.jar'
    jpype.startJVM(classpath=[str(jar)])
    J = jpype.JClass
    IRI, File = J('org.semanticweb.owlapi.model.IRI'), J('java.io.File')
    Manager, Mapper, Reasoner = J('org.semanticweb.owlapi.apibinding.OWLManager'), J('org.semanticweb.owlapi.util.SimpleIRIMapper'), J('org.semanticweb.HermiT.Reasoner')

    def load():
        manager = Manager.createOWLOntologyManager()
        for iri, item in raw.items():
            manager.addIRIMapper(Mapper(IRI.create(iri), IRI.create(File(str((private_dir / item['filename']).resolve())))))
        ontology = manager.loadOntologyFromOntologyDocument(File(str((private_dir / 'LMM_L2.owl').resolve())))
        return manager, ontology

    out = dict(issue=274, date='2026-10-29', kind='EXACT_PINNED_IMPORT_PROFILE_AND_ISOLATED_HERMIT',
               command='python tools/inspect_lmm274.py --source-dir PRIVATE --private-dir PRIVATE --output evaluation/related-work/lmm274/execution.json',
               source_sha256={x['id']: x['sha256'] for x in raw.values()},
               generator='tools/inspect_lmm274.py', generator_sha256=digest(Path(__file__).read_bytes()),
               python=platform.python_version(), rdflib=importlib.metadata.version('rdflib'),
               jpype=importlib.metadata.version('JPype1'), owlready2=importlib.metadata.version('owlready2'),
               hermit_jar_sha256=digest(jar.read_bytes()), hermit='bundled 1.3.8.1099',
               java_version=subprocess.run(['java', '-version'], capture_output=True, text=True).stderr.strip(),
               import_policy='Exact four retained files mapped by ontology IRI; no source alteration, network import, alignment-root substitution or ontology repair.',
               tests=[])
    manager, ontology = load()
    out['loaded_imports'] = sorted(str(x.getOntologyID().getOntologyIRI()) for x in ontology.getImportsClosure())
    profile = J('org.semanticweb.owlapi.profiles.OWL2DLProfile')().checkOntology(ontology)
    out['owl2_dl_profile_pass'] = bool(profile.isInProfile())
    out['profile_violations'] = sorted(str(v) for v in profile.getViolations())
    try:
        reasoner = Reasoner(ontology)
        out['baseline_consistent'] = bool(reasoner.isConsistent())
        out['unsatisfiable_named_classes'] = sorted(str(c.getIRI()) for c in reasoner.getUnsatisfiableClasses().getEntitiesMinusBottom()) if out['baseline_consistent'] else None
        reasoner.dispose()
        out['baseline_error'] = None
    except Exception as exc:
        out.update(baseline_consistent=None, unsatisfiable_named_classes=None, baseline_error=str(exc)[:1500])
    for name, question, expected, graph in fixtures():
        nt = ('\n'.join(sorted(to_canonical_graph(graph).serialize(format='nt').splitlines())) + '\n') if graph else ''
        observed, error = None, None
        try:
            m, o = load()
            if nt:
                f = private_dir / (name + '.nt')
                f.write_text(nt)
                fixture = m.loadOntologyFromOntologyDocument(File(str(f.resolve())))
                m.addAxioms(o, fixture.getAxioms())
            rr = Reasoner(o)
            observed = bool(rr.isConsistent())
            rr.dispose()
        except Exception as exc:
            error = str(exc)[:1500]
        row = dict(id=name, question=question, expected_consistent=expected, observed_consistent=observed,
                   error=error, fixture_nt=nt, fixture_sha256=digest(nt.encode()),
                   result='ERROR' if error else 'PASS' if observed is expected else 'FAIL')
        out['tests'].append(row)
        print(name, row['result'], observed, flush=True)
    out['summary'] = {name: sum(t['result'] == status for t in out['tests']) for name, status in [('passed', 'PASS'), ('failed', 'FAIL'), ('errors', 'ERROR')]}
    out['summary']['total'] = len(out['tests'])
    out['limitations'] = 'Isolated whole-closure OWL cases; not original 2008 parity, all-resource alignment, disambiguation evaluation or accepted Clariceptify equivalence. No published source bytes.'
    jpype.shutdownJVM()
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', required=True)
    parser.add_argument('--private-dir', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    result = run(args.source_dir, args.private_dir)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
