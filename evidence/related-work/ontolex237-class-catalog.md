# OntoLex 2016 core: complete selected named-class register

Issue #237. Exact W3C RDF/XML root SHA256 `b4265ab8bf1fc61dc413ed3eb6c70b951cb69c76c406a6f4bfef7684acf014ee`. The acquired `.ttl` filename does not describe its syntax. This is the eight-local/eight-external-declaration population, not the entire five-module specification.

A source comment is an annotation candidate, not a complete logical definition. Every local paraphrase below is attributed to its English source comment; no external redeclaration receives an invented definition. The [machine census](../../evaluation/related-work/ontolex237/census.json) has each class IRI, English label/comment hash and source locator, named/anonymous hierarchy, equivalent restrictions and deprecation state.

| Declared class IRI | Population | English label | Source comment | Short attributed paraphrase / gap |
|---|---|---|---|---|
| http://www.w3.org/ns/lemon/ontolex#Affix | LOCAL | affix | PRESENT_ENGLISH_COMMENT | A lexical entry for a bound morpheme attached to a word stem to make a new word. |
| http://www.w3.org/ns/lemon/ontolex#ConceptSet | LOCAL | concept set | PRESENT_ENGLISH_COMMENT | A collection of lexical concepts; the formal membership direction is separately recorded. |
| http://www.w3.org/ns/lemon/ontolex#Form | LOCAL | form | PRESENT_ENGLISH_COMMENT | A grammatical realization of a lexical entry. |
| http://www.w3.org/ns/lemon/ontolex#LexicalConcept | LOCAL | lexical concept | PRESENT_ENGLISH_COMMENT | A mental abstraction or thought unit conveying the meanings of lexical entries. |
| http://www.w3.org/ns/lemon/ontolex#LexicalEntry | LOCAL | lexical entry | PRESENT_ENGLISH_COMMENT | A lexicon unit grouping related grammatical forms and associated base meanings. |
| http://www.w3.org/ns/lemon/ontolex#LexicalSense | LOCAL | lexical sense | PRESENT_ENGLISH_COMMENT | The meaning of an entry when interpreted in relation to a particular ontology element. |
| http://www.w3.org/ns/lemon/ontolex#MultiWordExpression | LOCAL | multi-word expression | PRESENT_ENGLISH_COMMENT | A lexical entry comprising at least two words. |
| http://www.w3.org/ns/lemon/ontolex#Word | LOCAL | word | PRESENT_ENGLISH_COMMENT | A lexical entry consisting of one token. |
| http://purl.org/vocommons/voaf#Vocabulary | EXTERNAL_REDECLARATION | MISSING | MISSING_IN_SELECTED_ROOT | MISSING IN SELECTED ROOT |
| http://www.ontologydesignpatterns.org/cp/owl/semiotics.owl#Expression | EXTERNAL_REDECLARATION | expression | MISSING_IN_SELECTED_ROOT | MISSING IN SELECTED ROOT |
| http://www.ontologydesignpatterns.org/cp/owl/semiotics.owl#Meaning | EXTERNAL_REDECLARATION | meaning | MISSING_IN_SELECTED_ROOT | MISSING IN SELECTED ROOT |
| http://www.w3.org/2004/02/skos/core#Concept | EXTERNAL_REDECLARATION | concept | MISSING_IN_SELECTED_ROOT | MISSING IN SELECTED ROOT |
| http://www.w3.org/2004/02/skos/core#ConceptScheme | EXTERNAL_REDECLARATION | concept scheme | MISSING_IN_SELECTED_ROOT | MISSING IN SELECTED ROOT |
| http://www.w3.org/ns/lemon/synsem#OntoMap | EXTERNAL_REDECLARATION | MISSING | MISSING_IN_SELECTED_ROOT | MISSING IN SELECTED ROOT |
| http://xmlns.com/foaf/0.1/Organization | EXTERNAL_REDECLARATION | MISSING | MISSING_IN_SELECTED_ROOT | MISSING IN SELECTED ROOT |
| http://xmlns.com/foaf/0.1/Person | EXTERNAL_REDECLARATION | MISSING | MISSING_IN_SELECTED_ROOT | MISSING IN SELECTED ROOT |

Eight local classes have English comment candidates; all eight external redeclarations have no English comment in this selected root. The root declares **no `owl:imports`**: external declarations are not counted as imported classes or proof of imported source definitions. Two anonymous `owl:Class` nodes, six restriction nodes and the referenced but undeclared `rdfs:Resource` are kept outside the 16 named declarations. `rdf:langString` is a datatype and `owl:Thing` a built-in class, not additional local names.

The report and [source version delta](../../evaluation/related-work/ontolex237/census.json) retain the published W3C `ConceptSet` restriction versus the pinned repository correction. No automatic alignment to Clariceptify, semantic acceptance or historical paper-byte parity follows.
