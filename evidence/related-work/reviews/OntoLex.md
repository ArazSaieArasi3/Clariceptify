# OntoLex-Lemon: 2016 official-document critical review

Issue #75 | COMPLETE_WITH_EXPLICIT_LIMITS | Reviewed 2026-10-29

This is an AI-assisted review of the official Community Group Report, not a W3C Standard, journal paper, formal-artifact validation, or independent scientific acceptance.

[Pinned source](https://www.w3.org/2016/05/ontolex/) | [Structured review](OntoLex.yaml) | [Document inventory](../../../evaluation/related-work/ontolex/document-census.json) | [Image inspection](../../../evaluation/related-work/ontolex/image-inspection.json)

SHA256: `ce0996a09f6ab97633c0aaad0b6eb02120615f2f4b8d5aa5c4b2558ce5f5c9b2`. Exact bytes match the retained acquisition manifest. Editors: Philipp Cimiano, John P. McCrae, Paul Buitelaar.

## Short source synopsis

The report specifies lexical grounding through five modules: core, syntax-semantics, decomposition, variation-translation and metadata. It separates forms, entries, senses, concepts and referenced entities. Usage and conditions qualify lexical interpretation; external vocabularies supply linguistic categories. LIME counts links among lexicons, concepts and reference datasets. Examples cover multilingual terms, wordnets and publication arrangements. This is a community specification rather than an empirical evaluation study.

## Critical review dimensions

- **purpose:** Evaluate this source as a lexical interface candidate, not as a replacement for the research model. [Source locator](https://www.w3.org/2016/05/ontolex/#purpose-of-the-model).
- **process product agent content:** A link-set called conceptualization is not automatically an occurrence of concept formation. Keep entry/concept links separate from activity, participating person, intention and decision records. [Source locator](https://www.w3.org/2016/05/ontolex/#conceptualization-set).
- **mental orientation:** The mental-concept interpretation is relevant counterevidence against claiming no prior conceptual-content distinction. It does not by itself supply person-indexed mental states or an empirical cognitive theory. [Source locator](https://www.w3.org/2016/05/ontolex/#lexical-concept).
- **representation referent:** Preserve entry, form, sense, evoked concept and reference as separate comparison columns. An equivalence mapping to our Representation or Concept would require a later argument and adverse cases. [Source locator](https://www.w3.org/2016/05/ontolex/#lexical-sense-reference).
- **requirements:** The use cases support lexical interface requirements; test whether our intended question concerns a lexical relation or a decision episode before proposing reuse. No imported ORSD or CQ satisfaction is established. [Source locator](https://www.w3.org/2016/05/ontolex/#introduction).
- **method:** Community consensus and stated model inspirations are evidence of specification development, not independent expert validation of Clariceptify. [Source locator](https://www.w3.org/2016/05/ontolex/#purpose-of-the-model).
- **formal assumptions:** Natural-language axioms and embedded Turtle are evidence to inspect, not a substitute for parsing the pinned published modules and resolving imports in #237. [Source locator](https://www.w3.org/2016/05/ontolex/#conventions-in-this-document).
- **foundation:** The cited inspirations and visible SKOS/semiotics relationships justify documenting reuse. They do not establish a UFO/BFO grounding, exact foundation edition, or current executable import closure. [Source locator](https://www.w3.org/2016/05/ontolex/#purpose-of-the-model).
- **evaluation:** Worked examples and population ratios are not measured accuracy, usability or adequacy results. This review executes no benchmark or reasoner on the external ontology. [Source locator](https://www.w3.org/2016/05/ontolex/#publication-scenarios).
- **limitations:** The review is bounded to this 2016 document. Later module evolution, full imported class definitions, and corpus-wide novelty remain separate work. [Source locator](https://www.w3.org/2016/05/ontolex/#relation-to-other-models).

## Findings and retained questions

- **F01:** Direction ambiguity: the displayed ConceptSet restriction follows skos:inScheme, whereas the adjacent example links the concept to its set. Preserve both readings; #237 must compare the actual axiom without silently repairing the source. [Source locator](https://www.w3.org/2016/05/ontolex/#concept-set-class). Follow-up: #237, #253, #126.
- **F02:** Argument-position ambiguity: the propertyRange definition duplicates the first-position wording of propertyDomain, despite the section distinguishing two argument positions. Do not turn this editorial ambiguity into an accepted mapping rule. [Source locator](https://www.w3.org/2016/05/ontolex/#propertyrange-object-property). Follow-up: #237, #253, #126.
- **F03:** The first SKOS example targets a resource typed as LexicalEntry via lexicalizedSense, while the earlier property definition targets LexicalSense. Treat this as a documentation correspondence question, not proof of inconsistency. [Source locator](https://www.w3.org/2016/05/ontolex/#skos-xl). Follow-up: #237, #253, #126.
- **F04:** The prose describes denotes/chain equivalence. The displayed chain alone does not demonstrate that every denotes assertion creates a named sense witness. Separate the two directions in later formal testing. [Source locator](https://www.w3.org/2016/05/ontolex/#lexical-sense-reference). Follow-up: #237, #253, #126.
- **F05:** The printed chain traversal must be checked against the declared entry/sense directions, and against its inclusion direction. Do not copy the displayed expression into a reasoning claim without the actual module. [Source locator](https://www.w3.org/2016/05/ontolex/#translatableas-object-property). Follow-up: #237, #253, #126.
- **F06:** Denominator risk: an average over all domain entities differs from an average over linked entities. Test both with unused entities and an empty denominator; record rounding rather than interpreting illustrative decimals as exact measurements. [Source locator](https://www.w3.org/2016/05/ontolex/#formal-definition-of-properties). Follow-up: #237, #253, #126.
- **F07:** The river example prose and example literals assign the two endings in opposite order. This is a within-document inconsistency; no external linguistic truth judgment is required to preserve it. [Source locator](https://www.w3.org/2016/05/ontolex/#usage). Follow-up: #237, #253, #126.
- **F08:** Scope collision: lexical pairing and purposeful conceptualizing must not be equated merely because both use conceptualization terminology. A person changing an interpretation without changing lexical links is an adverse case for that equation. [Source locator](https://www.w3.org/2016/05/ontolex/#conceptualization-set). Follow-up: #237, #253, #126.
- **F09:** The PROV-based translation example prevents claiming the ecosystem has no process or provenance capability. Conversely, borrowed provenance vocabulary does not establish a dedicated conceptual-decision/rationale model. [Source locator](https://www.w3.org/2016/05/ontolex/#confidence). Follow-up: #237, #253, #126.
- **F10:** Shared reference, sense-level translation and entry-level translatability must not be treated as one interchangeable relation. Context-sensitive replacement needs an explicit criterion; shared denotation alone is too weak for universal substitutability. [Source locator](https://www.w3.org/2016/05/ontolex/#translation). Follow-up: #237, #253, #126.
- **F11:** Functional canonical-form constraints do not establish a closed-world data-quality check. Two identifiers need not denote distinct forms; missing explicit assertions need not mean OWL contradiction. Keep validation and reasoning goals separate. [Source locator](https://www.w3.org/2016/05/ontolex/#canonical-form-object-property). Follow-up: #237, #253, #126.
- **F12:** Recommendation: retain as an alignment/reuse candidate for lexical interfaces and a source of counterexamples. Defer semantic adoption, extension, and corpus-wide gap conclusions to #237/#253/#126 rather than rejecting the source for its deliberately different purpose. [Source locator](https://www.w3.org/2016/05/ontolex/#purpose-of-the-model). Follow-up: #237, #253, #126.
- **F13:** The displayed linguisticCatalog superproperty names voaf:Vocabulary, used nearby as a class. Record this typing ambiguity without treating the source document as an executable ontology. [Source locator](https://www.w3.org/2016/05/ontolex/#linguistic-catalog-object-property). Follow-up: #237, #253, #126.
- **F14:** Several figure labels differ from the accompanying vocabulary or examples. The image ledger preserves nine flagged illustrations, including clipped text. Do not reuse an illustration as a verified formal pattern or silently repair its labels. [Source locator](https://www.w3.org/2016/05/ontolex/#core). Follow-up: #237, #253, #126.

## Illustration discrepancies

Every non-logo image was visually inspected. These are document-level observations; none establishes an OWL inconsistency. Enlarged inspection disproved an initial suspected language-arrow swap in F48.

- **F16:** Figure uses context edges, while its section specifies usage. Prose reverses the two river distinctions relative to the figure. Track as document/example discrepancy. [Image](https://www.w3.org/2016/05/ontolex/Examples/ontolex/example12.png).
- **F20:** Definition text is visibly clipped in rectangular literal cells; consult source text rather than reconstruct omitted strings. [Image](https://www.w3.org/2016/05/ontolex/Examples/ontolex/example17.png).
- **F30:** Figure labels SemanticFrame and semArg, unlike adjacent LexicalSense/condition discussion. Treat as possible legacy illustration vocabulary, not current ontology declaration evidence. [Image](https://www.w3.org/2016/05/ontolex/Examples/synsem/example9.png).
- **F39:** Bottom box is labeled Sense Relation while connected to Lexical Concept; Conceptual Relation term in text makes this a likely diagram labeling discrepancy. [Image](https://www.w3.org/2016/05/ontolex/Lemon_Variation_and_Translation.png).
- **F42:** SenseRelation source/target arrows point to surrogate_mother/mother referent nodes rather than the *_sense nodes; conflicts with immediately preceding relates-exactly-two-LexicalSense statement at the diagram/text level. [Image](https://www.w3.org/2016/05/ontolex/Examples/vartrans/example2.png).
- **F44:** The three sense-to-target edges use isLexicalizedSenseOf, while the adjacent shared-reference Turtle uses reference. Keep the figure/text relation mismatch explicit; it does not establish a logical inconsistency. [Image](https://www.w3.org/2016/05/ontolex/Examples/vartrans/example5.png).
- **F62:** Both spiaggia and famoso canonicalForm arrows meet shared lemma node with writtenRep=famoso; feminine famosa node also displays famoso. Record as example identifier/literal discrepancy requiring textual comparison. [Image](https://www.w3.org/2016/05/ontolex/Examples/description/example3.png).
- **F67:** Inverse edge labeled isLexicalizedBy differs from surrounding prose isEvokedBy; inline Turtle also uses lexicalizedSense with a LexicalEntry object. Preserve these as document/example discrepancies. [Image](https://www.w3.org/2016/05/ontolex/Examples/other/example-skos1.png).
- **F68:** One sense-to-concept edge labeled isContainedIn, unlike the parallel isLexicalizedSenseOf edge; possible legacy vocabulary in diagram, not established current property. [Image](https://www.w3.org/2016/05/ontolex/Examples/other/example-skos2.png).

## Reviewer-constructed adverse cases

- **A01:** One entry has inflectional variants and spelling variants. Compare whether the proposed mapping wrongly merges form identity with written string identity. Expected review disposition: `DISTINCTIONS_REQUIRED`. Execution: `CONCEPTUAL_REVIEW_ONLY`.
- **A02:** A lexical item denotes an ontology property while evoking an event concept. A mapping that merges both targets loses the distinction. Expected review disposition: `DO_NOT_EQUATE_REFERENT_AND_EVOKED_CONCEPT`. Execution: `CONCEPTUAL_REVIEW_ONLY`.
- **A03:** A researcher revises a rationale while leaving every entry-to-concept pair unchanged. Lexical-set statistics cannot detect that research decision. Expected review disposition: `NO_ACTIVITY_EQUIVALENCE_FROM_LINK_SET`. Execution: `REVIEWER_CONSTRUCTED_NOT_SOURCE_EXPERIMENT`.
- **A04:** Two entries share a referent but differ in register or temporal usage. Test substitution rather than assuming unlimited translation equivalence. Expected review disposition: `CONTEXT_REQUIRED`. Execution: `CONCEPTUAL_REVIEW_ONLY`.
- **A05:** Add an unlinked ontology entity: coverage and average-per-entity change although the link set does not. An empty domain requires an explicit undefined-value policy. Expected review disposition: `DENOMINATOR_AND_ZERO_POLICY_REQUIRED`. Execution: `REVIEWER_CONSTRUCTED_NOT_SOURCE_EXPERIMENT`.
- **A06:** Two asserted form IRIs lack a distinctness assertion. Do not label the source inconsistent from a functional-property statement alone. Expected review disposition: `DEFER_ACTUAL_REASONING_TO_237`. Execution: `CONCEPTUAL_REVIEW_ONLY`.

## Reading coverage

83 definition headings in this report, not 83 ontology classes; all 49 numbered sections inspected. OWL local/imported/inferred populations remain unassessed under #237.

| Section | Reading state |
|---|---|
| [1. Overview](https://www.w3.org/2016/05/ontolex/#x1-overview) | READ_AND_CRITICALLY_REVIEWED |
| [2. Introduction](https://www.w3.org/2016/05/ontolex/#introduction) | READ_AND_CRITICALLY_REVIEWED |
| [2.1 Purpose of the model](https://www.w3.org/2016/05/ontolex/#purpose-of-the-model) | READ_AND_CRITICALLY_REVIEWED |
| [2.2 Namespaces](https://www.w3.org/2016/05/ontolex/#namespaces) | READ_AND_CRITICALLY_REVIEWED |
| [2.3 Conventions in this document](https://www.w3.org/2016/05/ontolex/#conventions-in-this-document) | READ_AND_CRITICALLY_REVIEWED |
| [3. Core](https://www.w3.org/2016/05/ontolex/#core) | READ_AND_CRITICALLY_REVIEWED |
| [3.1 Lexical Entries](https://www.w3.org/2016/05/ontolex/#lexical-entries) | READ_AND_CRITICALLY_REVIEWED |
| [3.2 Forms](https://www.w3.org/2016/05/ontolex/#forms) | READ_AND_CRITICALLY_REVIEWED |
| [3.3 Semantics](https://www.w3.org/2016/05/ontolex/#semantics) | READ_AND_CRITICALLY_REVIEWED |
| [3.4 Lexical Sense & Reference](https://www.w3.org/2016/05/ontolex/#lexical-sense-reference) | READ_AND_CRITICALLY_REVIEWED |
| [3.5 Usage](https://www.w3.org/2016/05/ontolex/#usage) | READ_AND_CRITICALLY_REVIEWED |
| [3.6 Lexical Concept](https://www.w3.org/2016/05/ontolex/#lexical-concept) | READ_AND_CRITICALLY_REVIEWED |
| [4. Syntax and Semantics (synsem)](https://www.w3.org/2016/05/ontolex/#syntax-and-semantics-synsem) | READ_AND_CRITICALLY_REVIEWED |
| [4.1 Syntactic Frames](https://www.w3.org/2016/05/ontolex/#syntactic-frames) | READ_AND_CRITICALLY_REVIEWED |
| [4.2 Ontology Mappings](https://www.w3.org/2016/05/ontolex/#ontology-mappings) | READ_AND_CRITICALLY_REVIEWED |
| [4.3 Complex ontology mappings / submappings](https://www.w3.org/2016/05/ontolex/#complex-ontology-mappings-submappings) | READ_AND_CRITICALLY_REVIEWED |
| [4.4 Conditions](https://www.w3.org/2016/05/ontolex/#conditions) | READ_AND_CRITICALLY_REVIEWED |
| [5. Decomposition (decomp)](https://www.w3.org/2016/05/ontolex/#decomposition-decomp) | READ_AND_CRITICALLY_REVIEWED |
| [5.1 Subterms](https://www.w3.org/2016/05/ontolex/#subterms) | READ_AND_CRITICALLY_REVIEWED |
| [5.2 Components](https://www.w3.org/2016/05/ontolex/#components) | READ_AND_CRITICALLY_REVIEWED |
| [5.3 Phrase structure](https://www.w3.org/2016/05/ontolex/#phrase-structure) | READ_AND_CRITICALLY_REVIEWED |
| [6. Variation & Translation (vartrans)](https://www.w3.org/2016/05/ontolex/#variation-translation-vartrans) | READ_AND_CRITICALLY_REVIEWED |
| [6.1 Lexico-Semantic Relations](https://www.w3.org/2016/05/ontolex/#lexico-semantic-relations) | READ_AND_CRITICALLY_REVIEWED |
| [6.2 Translation](https://www.w3.org/2016/05/ontolex/#translation) | READ_AND_CRITICALLY_REVIEWED |
| [6.2.1 Translation as shared reference](https://www.w3.org/2016/05/ontolex/#translation-as-shared-reference) | READ_AND_CRITICALLY_REVIEWED |
| [6.2.2 Translation as a relation between lexical senses](https://www.w3.org/2016/05/ontolex/#translation-as-a-relation-between-lexical-senses) | READ_AND_CRITICALLY_REVIEWED |
| [6.2.3 Translatable As](https://www.w3.org/2016/05/ontolex/#translatable-as) | READ_AND_CRITICALLY_REVIEWED |
| [6.2.4 Translation Set](https://www.w3.org/2016/05/ontolex/#translation-set) | READ_AND_CRITICALLY_REVIEWED |
| [7. Metadata (lime)](https://www.w3.org/2016/05/ontolex/#metadata-lime) | READ_AND_CRITICALLY_REVIEWED |
| [7.1 Lexicon and Lexicon Metadata](https://www.w3.org/2016/05/ontolex/#lexicon-and-lexicon-metadata) | READ_AND_CRITICALLY_REVIEWED |
| [7.2 Lexicalization Set](https://www.w3.org/2016/05/ontolex/#lexicalization-set) | READ_AND_CRITICALLY_REVIEWED |
| [7.3 Partitions](https://www.w3.org/2016/05/ontolex/#partitions) | READ_AND_CRITICALLY_REVIEWED |
| [7.4 Lexical Linkset](https://www.w3.org/2016/05/ontolex/#lexical-linkset) | READ_AND_CRITICALLY_REVIEWED |
| [7.5 Conceptualization Set](https://www.w3.org/2016/05/ontolex/#conceptualization-set) | READ_AND_CRITICALLY_REVIEWED |
| [7.6 Formal definition of properties](https://www.w3.org/2016/05/ontolex/#formal-definition-of-properties) | READ_AND_CRITICALLY_REVIEWED |
| [7.7 Publication Scenarios](https://www.w3.org/2016/05/ontolex/#publication-scenarios) | READ_AND_CRITICALLY_REVIEWED |
| [8. Linguistic Description](https://www.w3.org/2016/05/ontolex/#linguistic-description) | READ_AND_CRITICALLY_REVIEWED |
| [8.1 Morphosyntactic Description](https://www.w3.org/2016/05/ontolex/#morphosyntactic-description) | READ_AND_CRITICALLY_REVIEWED |
| [8.2 Paradigmatic Description](https://www.w3.org/2016/05/ontolex/#pragmatic-paradigmatic-description) | READ_AND_CRITICALLY_REVIEWED |
| [8.3 Arguments](https://www.w3.org/2016/05/ontolex/#arguments) | READ_AND_CRITICALLY_REVIEWED |
| [8.4 Frames](https://www.w3.org/2016/05/ontolex/#frames) | READ_AND_CRITICALLY_REVIEWED |
| [8.5 Other properties](https://www.w3.org/2016/05/ontolex/#confidence) | READ_AND_CRITICALLY_REVIEWED |
| [9. Lexical Nets](https://www.w3.org/2016/05/ontolex/#lexical-nets) | READ_AND_CRITICALLY_REVIEWED |
| [9.1 Lexical nets in OntoLex-lemon](https://www.w3.org/2016/05/ontolex/#lexical-nets-in-lemon) | READ_AND_CRITICALLY_REVIEWED |
| [10. Relation to Other Models](https://www.w3.org/2016/05/ontolex/#relation-to-other-models) | READ_AND_CRITICALLY_REVIEWED |
| [10.1 SKOS(-XL)](https://www.w3.org/2016/05/ontolex/#skos-xl) | READ_AND_CRITICALLY_REVIEWED |
| [10.2 LMF](https://www.w3.org/2016/05/ontolex/#lmf) | READ_AND_CRITICALLY_REVIEWED |
| [10.3 OpenAnnotation](https://www.w3.org/2016/05/ontolex/#openannotation) | READ_AND_CRITICALLY_REVIEWED |
| [11. Acknowledgements](https://www.w3.org/2016/05/ontolex/#x11-acknowledgements) | READ_AND_CRITICALLY_REVIEWED |

## VVEAA and interpretation limits

- **verification:** Source identity, heading/figure coverage, evidence binding, scope and negative validator cases only.
- **validation:** AI-assisted source interpretation; no independent domain-expert acceptance.
- **evaluation:** No new benchmark, user study or ontology-quality score. Source examples inspected, not run as experimental evidence.
- **assessment:** Bounded alignment candidate with explicit document ambiguities.
- **assurance:** Pinned bytes, locators, adverse cases and open technical/comparison issue links preserve the claim ceiling.

## Decision and closure

Recommendation: alignment/reuse candidate; adoption deferred. No ontology import, model edit or manuscript change performed. Artifact counts, formal tests and full class definitions remain #237; comparison #253 and synthesis #126 remain separate.

Completes only #75 critical review of the pinned official document. All 18 full-paper reviews and the limited-summary review retain their existing denominators. #237 technical artifact and all-class catalogue, #253 comparison, #126 synthesis remain open. No model or release acceptance is inferred.

The report contains original reviewer commentary and source locators. Raw source HTML and images are not redistributed. The source rights notice is retained by link, not converted into a claim of relicensing permission.

Validation: `python tools/check_ontolex_review.py`; exact private-input reparse: add `--source path/to/OntoLex-specification.html`. Structural PASS does not establish scientific correctness.
