# SKOS Reference: 2009 document critical review

Issue #76 | COMPLETE_WITH_EXPLICIT_LIMITS | Reviewed 2026-10-29

This is an AI-assisted review of the W3C Recommendation and its official errata, not a journal-paper review, schema validation or adoption decision.

[Pinned Reference](https://www.w3.org/TR/2009/REC-skos-reference-20090818/) | [Structured review](SKOS.yaml) | [Document inventory](../../../evaluation/related-work/skos/document-census.json) | [Reading ledger](../../../evaluation/related-work/skos/reading-ledger.json) | [Errata review](../../../evaluation/related-work/skos/errata-review.json)

SHA256: `3aa00cd16ee4d86d3a19b75501bb317d0b0c134e1f4029e9f3098c4dd3669e4c`. Exact bytes match the retained acquisition manifest. Editors: Alistair Miles, Sean Bechhofer.

SKOS represents knowledge-organization resources and relationships in RDF. The Reference separates concepts, schemes, collections, lexical labels, notations, notes and mappings. Its optional XL vocabulary identifies label resources. Open-world conditions and conservative constraints distinguish what can be inferred from what an application may require.

## Coverage and populations

Read 143 numbered/appendix headings, 62 semantic statements, 90 numbered examples and two text subproperty diagrams. No substantive image figures occur; two badges are excluded. Source examples were inspected, not run.

Document tables only. 38 vocabulary entries are not 38 ontology classes; local/imported/inferred schema populations remain null.

S1-S46 core; S47-S62 XL. Eight integrity conditions including S48/S58 per errata, not eight executed tests.

The separate Primer is not represented as fully reviewed. The official errata are retained separately; they do not overwrite the archived Reference bytes.

## Critical review dimensions

- **purpose:** Treat this as evidence for publishing a KOS, not as an engineering method for discovering all conceptualization knowledge. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L879).
- **process product agent content:** Concept schemes, labels and their links provide overlap on products and content. Do not infer an explicit conceptualizing episode or responsible agent from these resource types. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L895).
- **mental orientation:** The suggestive unit-of-thought account is counterevidence to claiming SKOS ignores conceptual content. It does not establish a person-indexed mental-state theory. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1437).
- **representation referent:** Separate a concept resource, lexical label, represented subject and OWL class in later comparison. Hierarchical KOS links are not automatically subclass axioms about the subject domain. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1045).
- **requirements:** Conservative constraints serve heterogeneous KOS reuse. A stronger Clariceptify requirement may justify a separate application profile, not a claim that the base standard is defective. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#rationale).
- **method:** Working-group standardization and linked implementation experience are source context. This task performs no new empirical replication or independent expert acceptance. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#status).
- **formal assumptions:** Interpret domain and range as inference conditions under open-world semantics. A missing explicit type is not by itself invalid data. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L881).
- **foundation:** RDF/RDFS/OWL Full are the stated representation basis; this is not evidence of UFO, BFO or DOLCE grounding. Actual schema imports and class populations remain uninspected here. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1045).
- **evaluation:** Do not turn source consistency examples into a formal conformance certification: the Reference declines to define one. Examples below are read, not executed. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L434).
- **limitations:** The document is stronger than the downloadable RDF subset in some constraints. A future parser or DL-reasoner pass cannot automatically certify the complete Recommendation. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#namespace-document-rdf).

## Findings and follow-up questions

- **F01:** Do not treat scheme membership as a closed enumeration. A shared concept may appear in several schemes, and extra membership can remain compatible with the source. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1101). Follow-up: #238, #253, #126.
- **F02:** A top-concept usage convention is not a prohibition on broader links. Keep intended application policy separate from source inconsistency. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2446). Follow-up: #238, #253, #126.
- **F03:** Preferred-label integrity requires both language-tag partitions and the untagged case clarified by the official S14 erratum. It is not a generic cardinality-one restriction. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1567). Follow-up: #238, #253, #126.
- **F04:** An alternative label without a preferred label is permitted by the source. A required display label would be an additional application rule. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1606). Follow-up: #238, #253, #126.
- **F05:** Notation uniqueness is a convention rather than an asserted key. Do not report duplicate-code rejection as a property of the selected schema without an added rule. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2646). Follow-up: #238, #253, #126.
- **F06:** Editorial and history notes prevent a blanket claim of absent rationale or provenance capability. A free note is nevertheless not an explicit typed decision episode with accountable participants. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2860). Follow-up: #238, #253, #126.
- **F07:** Non-transitive here means the transitive conclusion is not licensed, not that a direct shortcut is forbidden. The historical broader relation and the current broaderTransitive relation need separate version-aware tests. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2413). Follow-up: #238, #253, #126.
- **F08:** Cycles and alternate paths are permitted in this base model. A no-cycle metric must identify its application-specific policy rather than conflate it with SKOS integrity. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2484). Follow-up: #238, #253, #126.
- **F09:** Associative/hierarchical disjointness reaches indirect ancestors. Checking only explicitly adjacent pairs would miss the source example involving an inferred path. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4261). Follow-up: #238, #253, #126.
- **F10:** Functional memberList can identify two list resources rather than reject two identifiers. Distinctness and malformed-list policies require explicit treatment; no unique-name assumption is licensed. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3551). Follow-up: #238, #253, #126.
- **F11:** exactMatch is not sameAs or class equivalence. Carrying labels and all other properties across a proposed alignment would overstate this relation and can generate a label conflict. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4858). Follow-up: #238, #253, #126.
- **F12:** Symmetry and transitivity can produce self-links for participants in exactMatch. That does not assert universal reflexivity for every resource. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#mapping-cycles-exactMatch). Follow-up: #238, #253, #126.
- **F13:** Do not propagate broader or related links through exactMatch by an unstated composition rule. Keep any desired inference as an explicit extension. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5675). Follow-up: #238, #253, #126.
- **F14:** Equal XL literal forms do not identify their label resources. A string-based deduplicator would erase distinctions that the model permits. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5739). Follow-up: #238, #253, #126.
- **F15:** XL-only consistency and combined SKOS+XL consistency differ. The literal projections can activate core label constraints; testing only the extension would miss this boundary. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L899). Follow-up: #238, #253, #126.
- **F16:** The OWL 1 DL variant is an informative pruning, not an interchangeable complete normative model. Record removed commitments before drawing semantic conclusions. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#rdf-schema-owl-dl). Follow-up: #238, #253, #126.
- **F17:** An unchanged namespace is not proof of unchanged semantics: the historical broader/narrower interpretation changed. Pin bytes and edition rather than infer identity from URI alone. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#namespace). Follow-up: #238, #253, #126.
- **F18:** The text names Appendix A for the label extension while the linked target and actual extension are Appendix B. Treat the caption as an editorial cross-reference discrepancy, not an ontology defect. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3260). Follow-up: #238, #253, #126.
- **F19:** The domain/range note refers to example 26 and names a third resource absent there. The inference principle remains supported elsewhere; preserve the mistaken example pointer without inventing data. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2251). Follow-up: #238, #253, #126.
- **F20:** The acronym discussion spells the property with the core prefix while the example uses the XL prefix. Preserve the distinction when planning artifact correspondence checks. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1195). Follow-up: #238, #253, #126.
- **F21:** The appendix summary gives hasTopConcept a generic label rather than a descriptive one. Do not promote that caption into a definition or repair the source silently. [Locator](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#hasTopConcept). Follow-up: #238, #253, #126.

## Official corrections and their scope

- [SKOS-DL-versionIRI](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#SKOS-DL-versionIRI): Version identity correction concerns the informative DL subset, not an adopted module. Scope: `REFERENCE_INFORMATIVE_SCHEMA`.
- [DCT-abbrev](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#DCT-abbrev): Record the missing namespace abbreviation before reconstructing examples. Scope: `REFERENCE`.
- [HTML-namespace](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#HTML-namespace): Preserve corrected HTML access routes without rewriting the frozen source. Scope: `REFERENCE`.
- [S14](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#S14): Include untagged preferred literals in the later integrity test boundary. Scope: `REFERENCE`.
- [love77](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#love77): Retain the corrected language example separately from literal identity constraints. Scope: `REFERENCE`.
- [skos-vs-skos-xl](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#skos-vs-skos-xl): The namespace description concerns XL rather than the core vocabulary. Scope: `REFERENCE`.
- [xl-integrity-constraints](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#xl-integrity-constraints): Treat S48 and S58 as integrity conditions despite their section placement. Scope: `REFERENCE`.
- [ISO-Correspondences](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#ISO-Correspondences): This does not establish review of the Primer or current ISO mappings. Scope: `PRIMER_NOT_REVIEWED`.
- [SPARQL-variable-typo](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#SPARQL-variable-typo): Query correction is noted as out of this Reference review scope. Scope: `PRIMER_NOT_REVIEWED`.
- [narrower-scopeNote](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#narrower-scopeNote): Retain source annotation correction for the separate artifact inspection. Scope: `RDF_ARTIFACT_DEFERRED_238`.
- [missing-tags](https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata#missing-tags): Retain annotation language-tag correction for the separate artifact inspection. Scope: `RDF_ARTIFACT_DEFERRED_238`.

## Reviewer-constructed adverse cases

- **A01:** A concept is placed in two schemes. Disposition: `DO_NOT_INFER_DISJOINT_OR_CLOSED_MEMBERSHIP`. This is conceptual analysis, not an executed reasoner test.
- **A02:** Two distinct preferred literals have no language tag. Disposition: `APPLY_ERRATA_QUALIFICATION_IN_238`. This is conceptual analysis, not an executed reasoner test.
- **A03:** A hierarchy includes both a two-edge path and its direct shortcut. Disposition: `NONTRANSITIVE_DOES_NOT_MEAN_INTRANSITIVE`. This is conceptual analysis, not an executed reasoner test.
- **A04:** Two concepts are broader than each other. Disposition: `CYCLE_POLICY_IS_APPLICATION_SPECIFIC`. This is conceptual analysis, not an executed reasoner test.
- **A05:** An ordered collection points at two list identifiers without distinctness. Disposition: `DO_NOT_ASSUME_INCONSISTENCY_FROM_IDENTIFIER_COUNT`. This is conceptual analysis, not an executed reasoner test.
- **A06:** Two mapped concepts have different preferred labels and scheme memberships. Disposition: `DO_NOT_SUBSTITUTE_SAMEAS_FOR_EXACTMATCH`. This is conceptual analysis, not an executed reasoner test.
- **A07:** Two distinct XL label resources share one literal form. Disposition: `DO_NOT_MERGE_FROM_LITERAL_EQUALITY`. This is conceptual analysis, not an executed reasoner test.
- **A08:** Two XL label resources project different preferred strings in one language. Disposition: `DISTINGUISH_XL_ONLY_FROM_COMBINED_MODEL`. This is conceptual analysis, not an executed reasoner test.
- **A09:** A researcher changes an editorial rationale while concept links stay constant. Disposition: `NOTES_ARE_COUNTEREVIDENCE_BUT_NOT_EXPLICIT_EPISODE_MODEL`. This is conceptual analysis, not an executed reasoner test.

## Reading ledger

All semantic statement and example identifiers are bound to source-row/table hashes in the machine-readable ledger. An inspection state records reading, not a semantic PASS. Two unanchored XL summary headings use their actual nearest section locator; no invented anchor is created.

| Heading | Source location | State |
|---|---|---|
| 1. Introduction | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L155) | READ_AND_CRITICALLY_REVIEWED |
| 1.1. Background and Motivation | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L879) | READ_AND_CRITICALLY_REVIEWED |
| 1.2. SKOS Overview | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L895) | READ_AND_CRITICALLY_REVIEWED |
| 1.3. SKOS, RDF and OWL | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1045) | READ_AND_CRITICALLY_REVIEWED |
| 1.4. Consistency and Integrity | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L831) | READ_AND_CRITICALLY_REVIEWED |
| 1.5. Inference, Dependency and the Open World Assumption | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L881) | READ_AND_CRITICALLY_REVIEWED |
| 1.6. Design Rationale | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#rationale) | READ_AND_CRITICALLY_REVIEWED |
| 1.7. How to Read this Document | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L649) | READ_AND_CRITICALLY_REVIEWED |
| 1.7.1. Formal Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1291) | READ_AND_CRITICALLY_REVIEWED |
| 1.7.2. URI Abbreviations | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1368) | READ_AND_CRITICALLY_REVIEWED |
| 1.7.3. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1501) | READ_AND_CRITICALLY_REVIEWED |
| 1.8. Conformance | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L434) | READ_AND_CRITICALLY_REVIEWED |
| 2. SKOS Namespace and Vocabulary | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1302) | READ_AND_CRITICALLY_REVIEWED |
| 3. The skos:Concept Class | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1289) | READ_AND_CRITICALLY_REVIEWED |
| 3.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1437) | READ_AND_CRITICALLY_REVIEWED |
| 3.2. Vocabulary | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2039) | READ_AND_CRITICALLY_REVIEWED |
| 3.3. Class & Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L842) | READ_AND_CRITICALLY_REVIEWED |
| 3.4. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2118) | READ_AND_CRITICALLY_REVIEWED |
| 3.5. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2145) | READ_AND_CRITICALLY_REVIEWED |
| 3.5.1. SKOS Concepts, OWL Classes and OWL Properties | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L896) | READ_AND_CRITICALLY_REVIEWED |
| 4. Concept Schemes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2430) | READ_AND_CRITICALLY_REVIEWED |
| 4.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1638) | READ_AND_CRITICALLY_REVIEWED |
| 4.2. Vocabulary | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2457) | READ_AND_CRITICALLY_REVIEWED |
| 4.3. Class & Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L8421) | READ_AND_CRITICALLY_REVIEWED |
| 4.4. Integrity Conditions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1228) | READ_AND_CRITICALLY_REVIEWED |
| 4.5. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L21181) | READ_AND_CRITICALLY_REVIEWED |
| 4.6. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2497) | READ_AND_CRITICALLY_REVIEWED |
| 4.6.1. Closed vs. Open Systems | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1101) | READ_AND_CRITICALLY_REVIEWED |
| 4.6.2. SKOS Concept Schemes and OWL Ontologies | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1170) | READ_AND_CRITICALLY_REVIEWED |
| 4.6.3. Top Concepts and Semantic Relations | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2446) | READ_AND_CRITICALLY_REVIEWED |
| 4.6.4. Scheme Containment and Semantic Relations | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2577) | READ_AND_CRITICALLY_REVIEWED |
| 4.6.5. Domain of skos:inScheme | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2805) | READ_AND_CRITICALLY_REVIEWED |
| 5. Lexical Labels | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2831) | READ_AND_CRITICALLY_REVIEWED |
| 5.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2007) | READ_AND_CRITICALLY_REVIEWED |
| 5.2. Vocabulary | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1304) | READ_AND_CRITICALLY_REVIEWED |
| 5.3. Class & Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1329) | READ_AND_CRITICALLY_REVIEWED |
| 5.4. Integrity Conditions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1567) | READ_AND_CRITICALLY_REVIEWED |
| 5.5. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1409) | READ_AND_CRITICALLY_REVIEWED |
| 5.6. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1539) | READ_AND_CRITICALLY_REVIEWED |
| 5.6.1. Domain of SKOS Lexical Labeling Properties | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1541) | READ_AND_CRITICALLY_REVIEWED |
| 5.6.2. Range of SKOS Lexical Labeling Properties | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1581) | READ_AND_CRITICALLY_REVIEWED |
| 5.6.3. Defining Label Relations | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3260) | READ_AND_CRITICALLY_REVIEWED |
| 5.6.4. Alternates Without Preferred | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1606) | READ_AND_CRITICALLY_REVIEWED |
| 5.6.5. Labeling and Language Tags | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1629) | READ_AND_CRITICALLY_REVIEWED |
| 6. Notations | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2064) | READ_AND_CRITICALLY_REVIEWED |
| 6.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2531) | READ_AND_CRITICALLY_REVIEWED |
| 6.2. Vocabulary | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2542) | READ_AND_CRITICALLY_REVIEWED |
| 6.3. Class & Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2557) | READ_AND_CRITICALLY_REVIEWED |
| 6.4. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2584) | READ_AND_CRITICALLY_REVIEWED |
| 6.5. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2611) | READ_AND_CRITICALLY_REVIEWED |
| 6.5.1. Notations, Typed Literals and Datatypes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2613) | READ_AND_CRITICALLY_REVIEWED |
| 6.5.2. Multiple Notations | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2637) | READ_AND_CRITICALLY_REVIEWED |
| 6.5.3. Unique Notations in Concept Schemes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2646) | READ_AND_CRITICALLY_REVIEWED |
| 6.5.4. Notations and Preferred Labels | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2655) | READ_AND_CRITICALLY_REVIEWED |
| 6.5.5. Domain of skos:notation | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#notations-note-domain) | READ_AND_CRITICALLY_REVIEWED |
| 7. Documentation Properties (Note Properties) | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2860) | READ_AND_CRITICALLY_REVIEWED |
| 7.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2543) | READ_AND_CRITICALLY_REVIEWED |
| 7.2. Vocabulary | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1693) | READ_AND_CRITICALLY_REVIEWED |
| 7.3. Class & Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1738) | READ_AND_CRITICALLY_REVIEWED |
| 7.4. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1812) | READ_AND_CRITICALLY_REVIEWED |
| 7.5. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1877) | READ_AND_CRITICALLY_REVIEWED |
| 7.5.1. Domain of the SKOS Documentation Properties | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1879) | READ_AND_CRITICALLY_REVIEWED |
| 7.5.2. Range of the SKOS Documentation Properties | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1917) | READ_AND_CRITICALLY_REVIEWED |
| 8. Semantic Relations | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1930) | READ_AND_CRITICALLY_REVIEWED |
| 8.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2810) | READ_AND_CRITICALLY_REVIEWED |
| 8.2. Vocabulary | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2010) | READ_AND_CRITICALLY_REVIEWED |
| 8.3. Class & Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2055) | READ_AND_CRITICALLY_REVIEWED |
| 8.4. Integrity Conditions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2422) | READ_AND_CRITICALLY_REVIEWED |
| 8.5. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2157) | READ_AND_CRITICALLY_REVIEWED |
| 8.6. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2249) | READ_AND_CRITICALLY_REVIEWED |
| 8.6.1. Sub-Property Relationships | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3732) | READ_AND_CRITICALLY_REVIEWED |
| 8.6.2. Domain and Range of SKOS Semantic Relation Properties | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2251) | READ_AND_CRITICALLY_REVIEWED |
| 8.6.3. Symmetry of skos:related | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2255) | READ_AND_CRITICALLY_REVIEWED |
| 8.6.4. skos:related and Transitivity | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2344) | READ_AND_CRITICALLY_REVIEWED |
| 8.6.5. skos:related and Reflexivity | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2376) | READ_AND_CRITICALLY_REVIEWED |
| 8.6.6. skos:broader and Transitivity | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2413) | READ_AND_CRITICALLY_REVIEWED |
| 8.6.7. skos:broader and Reflexivity | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2449) | READ_AND_CRITICALLY_REVIEWED |
| 8.6.8. Cycles in the Hierarchical Relation (skos:broaderTransitive and Reflexivity) | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2484) | READ_AND_CRITICALLY_REVIEWED |
| 8.6.9. Alternate Paths in the Hierarchical Relation | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2518) | READ_AND_CRITICALLY_REVIEWED |
| 8.6.10. Disjointness of skos:related and skos:broaderTransitive | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4261) | READ_AND_CRITICALLY_REVIEWED |
| 9. Concept Collections | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2942) | READ_AND_CRITICALLY_REVIEWED |
| 9.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3806) | READ_AND_CRITICALLY_REVIEWED |
| 9.2. Vocabulary | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3282) | READ_AND_CRITICALLY_REVIEWED |
| 9.3. Class & Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3312) | READ_AND_CRITICALLY_REVIEWED |
| 9.4. Integrity Conditions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3424) | READ_AND_CRITICALLY_REVIEWED |
| 9.5. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3460) | READ_AND_CRITICALLY_REVIEWED |
| 9.6. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3512) | READ_AND_CRITICALLY_REVIEWED |
| 9.6.1. Inferring Collections from Ordered Collections | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3514) | READ_AND_CRITICALLY_REVIEWED |
| 9.6.2. skos:memberList Integrity | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3551) | READ_AND_CRITICALLY_REVIEWED |
| 9.6.3. Nested Collections | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3588) | READ_AND_CRITICALLY_REVIEWED |
| 9.6.4. SKOS Concepts, Concept Collections and Semantic Relations | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L3625) | READ_AND_CRITICALLY_REVIEWED |
| 10. Mapping Properties | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1309) | READ_AND_CRITICALLY_REVIEWED |
| 10.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4307) | READ_AND_CRITICALLY_REVIEWED |
| 10.2. Vocabulary | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4138) | READ_AND_CRITICALLY_REVIEWED |
| 10.3. Class & Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4186) | READ_AND_CRITICALLY_REVIEWED |
| 10.4. Integrity Conditions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5429) | READ_AND_CRITICALLY_REVIEWED |
| 10.5. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4316) | READ_AND_CRITICALLY_REVIEWED |
| 10.6. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4412) | READ_AND_CRITICALLY_REVIEWED |
| 10.6.1. Mapping Properties, Semantic Relation Properties and Concept Schemes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4160) | READ_AND_CRITICALLY_REVIEWED |
| 10.6.2. Clashes Between Hierarchical and Associative Links | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4394) | READ_AND_CRITICALLY_REVIEWED |
| 10.6.3. Mapping Properties and Transitivity | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4414) | READ_AND_CRITICALLY_REVIEWED |
| 10.6.4. Mapping Properties and Reflexivity | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4499) | READ_AND_CRITICALLY_REVIEWED |
| 10.6.5. Cycles and Alternate Paths Involving skos:broadMatch | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4564) | READ_AND_CRITICALLY_REVIEWED |
| 10.6.6. Cycles Involving skos:exactMatch and skos:closeMatch | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#mapping-cycles-exactMatch) | READ_AND_CRITICALLY_REVIEWED |
| 10.6.7. Sub-Property Chains Involving skos:exactMatch | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5675) | READ_AND_CRITICALLY_REVIEWED |
| 10.6.8. skos:closeMatch, skos:exactMatch, owl:sameAs, owl:equivalentClass, owl:equivalentProperty | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4858) | READ_AND_CRITICALLY_REVIEWED |
| 11. References | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L744) | READ_AND_CRITICALLY_REVIEWED |
| 12. Acknowledgments | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#ack) | READ_AND_CRITICALLY_REVIEWED |
| Appendix A. SKOS Properties and Classes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L7127) | READ_AND_CRITICALLY_REVIEWED |
| A.1. Classes in the SKOS Data Model | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L7130) | READ_AND_CRITICALLY_REVIEWED |
| A.2. Properties in the SKOS Data Model | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L7307) | READ_AND_CRITICALLY_REVIEWED |
| Appendix B. SKOS eXtension for Labels (SKOS-XL) | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L4945) | READ_AND_CRITICALLY_REVIEWED |
| B.1. SKOS-XL Namespace and Vocabulary | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5212) | READ_AND_CRITICALLY_REVIEWED |
| B.2. The skosxl:Label Class | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5444) | READ_AND_CRITICALLY_REVIEWED |
| B.2.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L375) | READ_AND_CRITICALLY_REVIEWED |
| B.2.2. Class and Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5518) | READ_AND_CRITICALLY_REVIEWED |
| B.2.3. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5525) | READ_AND_CRITICALLY_REVIEWED |
| B.2.4. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5716) | READ_AND_CRITICALLY_REVIEWED |
| B.2.4.1. Identity and Entailment | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5739) | READ_AND_CRITICALLY_REVIEWED |
| B.2.4.2. Membership of Concept Schemes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L648) | READ_AND_CRITICALLY_REVIEWED |
| B.3. Preferred, Alternate and Hidden skosxl:Labels | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L5981) | READ_AND_CRITICALLY_REVIEWED |
| B.3.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L661) | READ_AND_CRITICALLY_REVIEWED |
| B.3.2. Class and Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L677) | READ_AND_CRITICALLY_REVIEWED |
| B.3.3. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L724) | READ_AND_CRITICALLY_REVIEWED |
| B.3.4. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L778) | READ_AND_CRITICALLY_REVIEWED |
| B.3.4.1. Dumbing-Down to SKOS Lexical Labels | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L780) | READ_AND_CRITICALLY_REVIEWED |
| B.3.4.2. SKOS+XL Labeling Integrity | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L899) | READ_AND_CRITICALLY_REVIEWED |
| B.4. Links Between skosxl:Labels | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L7196) | READ_AND_CRITICALLY_REVIEWED |
| B.4.1. Preamble | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1120) | READ_AND_CRITICALLY_REVIEWED |
| B.4.2. Class and Property Definitions | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1129) | READ_AND_CRITICALLY_REVIEWED |
| B.4.3. Examples | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1160) | READ_AND_CRITICALLY_REVIEWED |
| B.4.4. Notes | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1193) | READ_AND_CRITICALLY_REVIEWED |
| B.4.4.1. Refinements of this Pattern | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L1195) | READ_AND_CRITICALLY_REVIEWED |
| B.5. SKOS-XL Schema Overview | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#xl-overview) | READ_AND_CRITICALLY_REVIEWED |
| B.5.1 Classes in the SKOS-XL Data Model | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#xl-overview) | READ_AND_CRITICALLY_REVIEWED |
| B.5.2.Properties in the SKOS-XL Data Model | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#xl-overview) | READ_AND_CRITICALLY_REVIEWED |
| Appendix C. SKOS and SKOS-XL Namespace Documents | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L2994) | READ_AND_CRITICALLY_REVIEWED |
| C.1. SKOS Namespace Document - HTML Variant (normative) | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#namespace-document-html) | READ_AND_CRITICALLY_REVIEWED |
| C.2. SKOS Namespace Document - RDF/XML Variant (normative) | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#namespace-document-rdf) | READ_AND_CRITICALLY_REVIEWED |
| C.3. SKOS RDF Schema - OWL 1 DL Sub-set (informative) | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#rdf-schema-owl-dl) | READ_AND_CRITICALLY_REVIEWED |
| C.4. SKOS-XL Namespace Document - HTML Variant (normative) | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#xl-namespace-document-html) | READ_AND_CRITICALLY_REVIEWED |
| C.5. SKOS-XL Namespace Document - RDF/XML Variant (normative) | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#xl-namespace-document-rdf) | READ_AND_CRITICALLY_REVIEWED |
| Appendix D. SKOS Namespace: a historical note | [Source](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#namespace) | READ_AND_CRITICALLY_REVIEWED |

## VVEAA and claim ceiling

- **verification:** Exact-source census, complete reading ledger, bound evidence and negative validator tests; not RDF validation.
- **validation:** AI-assisted critical reading with separate review; no independent domain-expert acceptance.
- **evaluation:** No new benchmark, measured semantic accuracy or replicated implementation study.
- **assessment:** Candidate reuse for KOS/lexical interfaces; no semantic adoption or novelty conclusion.
- **assurance:** Exact versions, official corrections, conceptual adverse cases and open issue references constrain claims.

## Decision and closure

Completes only #76 document review. #238 schema inspection/all-class definitions, #253 comparison and #126 synthesis remain separate. No 19th full-paper review, model change, release or scientific acceptance follows.

Recommendation: retain as an alignment/reuse candidate; defer adoption and novelty judgments to #238/#253/#126. No model, requirements, fixtures, manuscript or release changes.

Raw HTML and source illustrations are not redistributed. Source rights remain separate from the repository license.

Checks: `python tools/check_skos_review.py`; optional exact private-input verification adds `--source path/to/SKOS-reference.html --errata path/to/SKOS-errata.html`. Structural PASS does not establish scientific correctness.
