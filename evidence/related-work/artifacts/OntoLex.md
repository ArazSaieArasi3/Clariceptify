# OntoLex core: pinned artifact and class/commitment review

Issue #237; baseline Clariceptify commit `e0cdfee856eb919caec4fafe5a57560ee287da67`. The [structured review](OntoLex.yaml), [complete selected class register](../ontolex237-class-catalog.md), [technical census](../../../evaluation/related-work/ontolex237/census.json), [profile receipt](../../../evaluation/related-work/ontolex237/execution.json) and [discovery record](../../../evaluation/related-work/ontolex237/discovery.json) separate source versions. This is one core module, not all five OntoLex modules or their imported definitions.

## Identity and boundary

The reviewed official W3C Community Group report is dated 10 May 2016 and is not a W3C Standard. Its retained HTML SHA256 is `ce0996a09f6ab97633c0aaad0b6eb02120615f2f4b8d5aa5c4b2558ce5f5c9b2`. The exact official core at `https://www.w3.org/ns/lemon/ontolex` has SHA256 `b4265ab8bf1fc61dc413ed3eb6c70b951cb69c76c406a6f4bfef7684acf014ee`, 54,456 bytes, an ontology-header version `1.1` and CC-Zero/CC0 metadata. The previously acquired `.ttl` filename is **RDF/XML**. Its header issue/modified dates are 2016-01-10; that does not make the report and root byte-identical.

The Community Group links the public repository now at `ontolex/ontolex`. Commit `ab0165605301413e64a66d53d23c3095fa879a26` pins `Ontologies/ontolex.owl` (blob `10783b4c747bbc5f08fbae8f4169d6e02fc22565`, SHA256 `76e4c74fae4013944f60701df83828836c22a7f19c8cc8f72f994e321d12efd9`). The 54,553-byte repository file differs from the official W3C root despite the same `1.1` header. Its observed last push is repository metadata, not a historical 2016 equivalence guarantee. No raw third-party file is redistributed here.

## Selected-root census

| Population | Count | Meaning |
|---|---:|---|
| Named `owl:Class` declarations | 16 | 8 OntoLex-local; 8 external namespace redeclarations |
| Anonymous `owl:Class` nodes | 2 | Separate from named classes; 6 restriction nodes also occur |
| Local object / datatype properties | 17 / 3 | Declared property types, not relation assertions |
| Local English comment candidates | 8 / 8 | Source comments and attributed short paraphrases in the complete register |
| External English comments | 0 / 8 | External redeclarations have no local source definition; do not invent one |
| Declared imports / imported classes | 0 / 0 | No `owl:imports`; eight external redeclarations are not imported closure |
| Inferred classes | unknown | Not a proven full logical class population |

The complete [16-row class register](../ontolex237-class-catalog.md) lists every named IRI, English label state, comment/definition availability, source locator, paraphrase or missing state and deprecation flag. The machine census retains asserted superclasses, anonymous restrictions and equivalence per class. It also identifies the referenced but undeclared `rdfs:Resource`, built-in `owl:Thing` and datatype `rdf:langString` without adding them to the named class count.

The selected root references semiotics `Expression`/`Meaning` and SKOS `Concept`/`ConceptScheme` as declared external classes and superclasses; it does not import those modules. The report describes broader lexical interface reuse. Neither source establishes a UFO/BFO edition, an imported semiotics/SKOS glossary or identity equivalence with a Clariceptify class.

## Eight bounded commitments and version difference

The [structured authority](OntoLex.yaml) gives exact IRIs and adverse readings for C01-C08: LexicalEntry's minimum one lexical form and maximum one canonical form; Form's written representation; LexicalConcept's dual superclass; LexicalSense's entry/reference cardinalities; ConceptSet's equivalence; and `evokes`/`denotes` property chains. These are eight selected technical questions; the class register still covers every declared class.

The 2016 W3C root encodes `ConceptSet ≡ (skos:inScheme min 1 LexicalConcept)`. `skos:inScheme` normally links a concept **to** a scheme, while the restriction as written starts at a set. The pinned repository root instead uses `owl:inverseOf skos:inScheme` inside this restriction. Removing translated labels leaves six W3C-only and six repository-only triples: the changed anonymous restriction plus an extra W3C `cc:licence` spelling account for the non-label delta. Thus a shared header version does not certify identical axioms. The published file is neither silently repaired nor replaced with the current repository file.

**Positive source scenario:** A lexical entry with a form and sense can use the `sense/reference` path to denote an ontology resource and the `sense/isLexicalizedSenseOf` path to evoke a distinct lexical concept. This lexical linkage does not alone record the human conceptualization activity, intention or decision.

**Adverse source scenario:** A concept linked by `skos:inScheme` to a scheme satisfies the expected direction in the specification example, whereas the W3C root's outward set restriction points the other way. This is an exact axiom-direction discrepancy, not a benchmark failure or a complete logical countermodel. The repository change is evidence of a different formula in pinned later bytes, not proof of author approval of our interpretation.

OWLAPI loaded 521 axioms from the selected root. **OWL 2 DL profile failed** with 37 violations (22 undeclared annotation properties, five uses each of reserved class IRI, undeclared class, and unknown datatype). HermiT's baseline call reported consistency and no unsatisfiable named classes on these unchanged bytes; because the input fails the profile, that result is recorded as an observation and not certified as an OWL 2 DL conclusion. No isolated entailment suite, validation study, lexical accuracy benchmark or external import execution is claimed.

## Research disposition

Treat OntoLex as a **candidate lexical interface** for expression, form, sense and referent analysis in #253/#126. Formal alignment remains deferred pending source-bound counterexamples and the owner's decision. Candidate Clariceptify concepts are `CLR-C0026`, `CLR-C0047`, `CLR-C0062` and `CLR-C0101`; none is declared equivalent or adopted. The root and report are useful prior art, while exact implementation differences and non-DL profile state remain explicit limitations. No Clariceptify scientific model, requirements, fixtures, manuscript or release changed.
