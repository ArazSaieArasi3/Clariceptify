"""Render the full selected OntoLex root class register from the pinned census."""
from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
CENSUS = 'evaluation/related-work/ontolex237/census.json'
CATALOG = 'evidence/related-work/ontolex237-class-catalog.yaml'
REPORT = 'evidence/related-work/ontolex237-class-catalog.md'
PARAPHRASES = {
    'Affix': 'A lexical entry for a bound morpheme attached to a word stem to make a new word.',
    'ConceptSet': 'A collection of lexical concepts; the formal membership direction is separately recorded.',
    'Form': 'A grammatical realization of a lexical entry.',
    'LexicalConcept': 'A mental abstraction or thought unit conveying the meanings of lexical entries.',
    'LexicalEntry': 'A lexicon unit grouping related grammatical forms and associated base meanings.',
    'LexicalSense': 'The meaning of an entry when interpreted in relation to a particular ontology element.',
    'MultiWordExpression': 'A lexical entry comprising at least two words.',
    'Word': 'A lexical entry consisting of one token.',
}


def calculate(root=ROOT):
    census = json.loads((root / CENSUS).read_text())
    rows = []
    for c in census['classes']:
        local = c['population'] == 'LOCAL'
        name = c['iri'].rsplit('#', 1)[-1]
        rows.append(dict(iri=c['iri'], population=c['population'], label_en=c['label_en'],
                         source_definition_status=c['source_comment_status'],
                         source_definition_sha256=c['source_comment_sha256'], source_locator=c['source_locator'],
                         reviewer_paraphrase=PARAPHRASES[name] if local else None,
                         reviewer_basis='ATTRIBUTED_COMMENT_PARAPHRASE' if local else 'MISSING_IN_SELECTED_ROOT',
                         hierarchy_and_constraints_ref=CENSUS + '::classes[iri=' + c['iri'] + ']',
                         deprecated=c['deprecated']))
    return dict(schema_version='1.0', issue=237, source_sha256=census['source_sha256'],
                selected_root='http://www.w3.org/ns/lemon/ontolex',
                population_policy='All 16 declared named classes in one exact official core graph; eight local and eight external redeclarations. Anonymous expressions and external references are separate. No declared imports.',
                counts=dict(named_declarations=len(rows), local_classes=sum(r['population'] == 'LOCAL' for r in rows),
                            external_redeclarations=sum(r['population'] == 'EXTERNAL_REDECLARATION' for r in rows),
                            local_comment_candidates=sum(r['population'] == 'LOCAL' and r['source_definition_status'] == 'PRESENT_ENGLISH_COMMENT' for r in rows),
                            local_missing_comments=sum(r['population'] == 'LOCAL' and r['source_definition_status'] != 'PRESENT_ENGLISH_COMMENT' for r in rows),
                            external_missing_comments=sum(r['population'] == 'EXTERNAL_REDECLARATION' and r['source_definition_status'] != 'PRESENT_ENGLISH_COMMENT' for r in rows),
                            imported_classes=0, inferred_classes=None),
                rows=rows, other_modules='NOT_INCLUDED', no_reviewer_invented_external_definitions=True,
                model_change='NONE')


def render(d):
    lines = ['# OntoLex 2016 core: complete selected named-class register', '',
             'Issue #237. Exact W3C RDF/XML root SHA256 `' + d['source_sha256'] + '`. '
             'The acquired `.ttl` filename does not describe its syntax. This is the eight-local/eight-external-declaration population, not the entire five-module specification.', '',
             'A source comment is an annotation candidate, not a complete logical definition. Every local paraphrase below is attributed to its English source comment; no external redeclaration receives an invented definition. '
             'The [machine census](../../evaluation/related-work/ontolex237/census.json) has each class IRI, English label/comment hash and source locator, named/anonymous hierarchy, equivalent restrictions and deprecation state.', '',
             '| Declared class IRI | Population | English label | Source comment | Short attributed paraphrase / gap |',
             '|---|---|---|---|---|']
    for r in d['rows']:
        lines.append('| ' + ' | '.join([r['iri'], r['population'], r['label_en'] or 'MISSING',
                                    r['source_definition_status'], r['reviewer_paraphrase'] or 'MISSING IN SELECTED ROOT']) + ' |')
    lines += ['', 'Eight local classes have English comment candidates; all eight external redeclarations have no English comment in this selected root. The root declares **no `owl:imports`**: external declarations are not counted as imported classes or proof of imported source definitions. Two anonymous `owl:Class` nodes, six restriction nodes and the referenced but undeclared `rdfs:Resource` are kept outside the 16 named declarations. `rdf:langString` is a datatype and `owl:Thing` a built-in class, not additional local names.', '',
              'The report and [source version delta](../../evaluation/related-work/ontolex237/census.json) retain the published W3C `ConceptSet` restriction versus the pinned repository correction. No automatic alignment to Clariceptify, semantic acceptance or historical paper-byte parity follows.', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    d = calculate()
    (ROOT / CATALOG).write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=False))
    (ROOT / REPORT).write_text(render(d))
    print(d['counts'])
