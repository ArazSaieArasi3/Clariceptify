# Cognitive Atlas: bounded technical review

Issue #241. BOUNDED_TECHNICAL_REVIEW_COMPLETE_WITH_SOURCE_AND_ENCODING_FINDINGS.

The selected later OWL export is inspected independently of the completed 2011 paper review. Every selected class and definition availability state is accounted for. Source defects and historical limits remain findings, not repaired author artifacts.

| Check | Observed result |
|---|---|
| Complete class register | 1696 local and two external declarations; 101 mixed identifier collisions |
| Definition availability | 1232 nonempty, 55 empty and 409 absent among local classes |
| Object properties | Three local and one external declaration; seven used restriction properties |
| OWL2 DL profile | FAIL: 7341 undeclared-entity violations under the recorded OWLAPI validator |
| Loaded logical ontology | Consistent, no unsatisfiable named classes returned |
| Isolated HermiT expectations | 14/14 expected consistency/adverse outcomes reproduced |
| Author generator / pickle / historical reproduction | Not executed; both raw RDF input parses fail |

Consistency does not establish correct conceptual identity or definition adequacy. The complete [class guide](../cognitiveatlas-class-catalog.md) links the structured declarations and separately attributed original definitions. No artificial class definitions are invented.

## Q01: Root, complete class population and historical provenance

The selected 13-file official snapshot and exact cogat.v2.owl bytes/header 0.3 are pinned separately from the paper-linked generator. The 1698 declared named classes contain 1696 local IRIs and two external declarations. They are not the 2011 paper 904 terms or today's website vocabulary. No other source module is folded into this selected count. There are 1796 distinct identifier values distributed across 1695 identified local class IRIs and one helper; 101 IRIs carry two identifiers. Exact 2011 byte equivalence remains unestablished.

Locators: ontology header; dc:identifier, all class IRIs; paper E12/E18; R01-R04.

Evidence: [census](../../../evaluation/related-work/cognitiveatlas/technical-census.json), [static](../../../evaluation/related-work/cognitiveatlas/static-source-inspection.json), [catalog](../../../evidence/related-work/cognitiveatlas-class-catalog.yaml).

## Q02: Lexical record versus OWL class

The generator turns skos:Concept element names into owl:Class and assigns CAO identifiers. This is an engineering transformation, not an argument that lexical entries are universally instantiated domain types. Header CAO_00001 subclasses a declared SKOS Concept class; concrete generated classes add hierarchy/restrictions. Full raw RDF parsing fails in both selected input dumps; the generated export itself parses. A concept/task co-instance is logically allowed; no intended category separation or epistemic agreement is proved.

Locators: create_owl.v2.py:skos:Concept replacement; CAO_00001; paper E05/E12.

Evidence: [census](../../../evaluation/related-work/cognitiveatlas/technical-census.json), [static](../../../evaluation/related-work/cognitiveatlas/static-source-inspection.json), [semantic](../../../evaluation/related-work/cognitiveatlas/semantic-cases.json).

## Q03: Measurement direction and actual restrictions

measured_by has undeclared MentalConcept domain and CogPO Task range. Its helper domain is not joined to CAO_00001. measures also ranges over Task despite its mental-concept description, and no inverse is asserted. A concrete Abductive reasoning class has additional all-values restrictions to named contrasts: its task-only filler denial contradicts those restrictions. A neutral concept without that concrete-class restriction permits a task-only filler. The initial broad range-only expectation was therefore split into these two explicit controls. Denying the declared domain/range is inconsistent; denying the reverse edge is consistent.

Locators: measured_by/measures domain/range; CAO_00101 restriction; paper E10.

Evidence: [census](../../../evaluation/related-work/cognitiveatlas/technical-census.json), [semantic](../../../evaluation/related-work/cognitiveatlas/semantic-cases.json).

## Q04: Condition/contrast structure and signed semantics

The source has 323 condition records, 510 contrast records and 509 contrast identifiers occurring in class declarations; one supplied contrast is not mapped to a declared class. N-back condition CAO_00980 has a required part_of task witness; denying all such witnesses is inconsistent. Label strings containing minus do not encode signed coefficients or arithmetic; the graph has no datatype properties for a contrast expression. The article 0-back-minus-2-back illustration was not located in the selected exported labels or source contrast names; it is not silently replaced with a different contrast. Task nesting and contrast associations are retained as restrictions, not validated signed measurement functions.

Locators: CAO_00980/CAO_01210; type_condition/type_contrast CSV; has_contrast/is_related_to; paper E06/E08.

Evidence: [census](../../../evaluation/related-work/cognitiveatlas/technical-census.json), [static](../../../evaluation/related-work/cognitiveatlas/static-source-inspection.json), [semantic](../../../evaluation/related-work/cognitiveatlas/semantic-cases.json).

## Q05: Basic mappings and foundation boundary

The selected generator branches on T1, T2, T15, T16; the source relation table additionally contains synonym T10, preceded-by T5 and literature T17 descriptors. The actual 941 assertion rows include 173 T1, 107 T2, 22 T15, 585 T16, 53 synonym and one temporal relation. Imported RO axioms/inverse part relations are absent; seven restriction-property IRIs are used but only four are declared. Eleven class-position IRIs are undeclared, eight local including MentalConcept and three CogPO. A referenced BFO Process class and namespaces do not prove foundational grounding or imported edition closure.

Locators: source relation CSV and generator T-branches; owl:imports empty; RO part_of/has_part; CogPO2011 references; paper E09/R02.

Evidence: [census](../../../evaluation/related-work/cognitiveatlas/technical-census.json), [static](../../../evaluation/related-work/cognitiveatlas/static-source-inspection.json).

## Q06: Every definition, citations and provenance

All 1696 local class definitions are accounted: 1232 nonempty, 55 empty annotations and 409 absent. The glossary supplies source IRIs, annotation digests and the exact attributed wording in a separate CC-BY-SA 3.0-US definition extract using the observed official project license. This intentionally avoids mass-generated paraphrases and invented completions; source wording is not accepted logical adequacy. Contributor/date annotations are hashed and retained as provenance. No CiTO/SWAN support/refutation structure is implemented in this selected export. Two negative source assertion rows are not inspected by polarity in the generator's mapping branches.

Locators: skos:definition; dc:Contributor/Date; source-definitions.jsonl; assertion polarity column; paper E11/E13.

Evidence: [census](../../../evaluation/related-work/cognitiveatlas/technical-census.json), [static](../../../evaluation/related-work/cognitiveatlas/static-source-inspection.json), [catalog](../../../evidence/related-work/cognitiveatlas-class-catalog.yaml).

## Q07: Disagreement, synonyms and identifier collisions

The source includes 53 synonym assertion rows; the selected generator does not map T10 to equivalence, sameAs or a sense/fork model. All 101 multi-identifier class IRIs mix one trm construct identifier and one cnt contrast identifier. Example CAO_01573 combines sense of body ownership with a Wechsler vocabulary contrast. The raw logical source admits such an instance; adding an explicitly reviewer-defined separation of mental concept and contrast exposes a contradiction. This control is not an author disjointness axiom. Stale undeclared local class references remain explicit, not silently repaired or treated as expert consensus.

Locators: CAO_01573 and 101 exact collision records; T10; paper E13/E14.

Evidence: [census](../../../evaluation/related-work/cognitiveatlas/technical-census.json), [static](../../../evaluation/related-work/cognitiveatlas/static-source-inspection.json), [semantic](../../../evaluation/related-work/cognitiveatlas/semantic-cases.json).

## Q08: Executed checks and generation limits

RDFLib parsing/census, CSV profiling, definition extraction, OWLAPI profile and 14 isolated HermiT expectations actually ran. The exact root fails the profile with 7341 undeclared-entity violations; the loaded logical ontology is consistent and has no unsatisfiable named classes under the recorded tool. This is not a conformance or adequacy certificate. Both raw RDF dumps fail strict parsing. The Python 2 generator reads a pickle and discards the first assertion although the supplied table has no header; it was inspected rather than executed or ported. No pickle loading, current-data generation, author CQ suite or historical reproduction is claimed.

Locators: raw RDF error locators; OWLAPI/HermiT recorded receipts; create_owl.v2.py:relations.remove(relations[0]); pickle.load; paper E12/R02.

Evidence: [census](../../../evaluation/related-work/cognitiveatlas/technical-census.json), [static](../../../evaluation/related-work/cognitiveatlas/static-source-inspection.json), [semantic](../../../evaluation/related-work/cognitiveatlas/semantic-cases.json).

## Findings for comparison #254 and synthesis #126

| ID | Finding |
|---|---|
| CA241-F01: Class encoding is not paper population or current website | 1696 local IRIs encode a later generated vocabulary, not the 904 terms reported in 2011 or current live counts; strict raw inputs fail parsing. |
| CA241-F02: Identifier collision conflates meanings | 101 class IRIs share a construct identifier and a contrast identifier; logical consistency does not establish successful sense management. |
| CA241-F03: Strict profile and raw-source parsing fail | 7341 checked profile violations concern undeclared entities; both retained raw RDF input files also fail parsing. |
| CA241-F04: Measurement schema and concrete restrictions differ | Task-valued range, unjoined MentalConcept helper, no inverse and a wrong measures range require source-specific interpretation; concrete all-values restrictions add further constraints. |
| CA241-F05: Signed contrast semantics are not formalized | Task/condition/contrast nesting and minus labels are not coefficients, indicator lineage or an executable contrast function; one supplied contrast is unmapped. |
| CA241-F06: Mappings omit some source relation kinds | T10/T5/T17 descriptors, undeclared properties and class references are not imported RO/foundation semantics. |
| CA241-F07: Definition coverage is incomplete and ambiguity is retained | 1232 local classes have nonempty definition text; 55 are empty and 409 absent. Presence is not sufficiency; collisions retain multiple labels/identifiers. |
| CA241-F08: Disagreement and citation polarity are lost | No complete sense/fork/support/refutation export is present; 53 synonym assertions and two negative source rows must not be promoted to accepted identity or consensus. |
| CA241-F09: Exact generation is not reproduced | Python 2/pickle/string-splitting and dropping a real first assertion prevent an unqualified generation or historical byte-parity claim; original code/data stay unchanged. |

## Reproduce and interpret

Keep exact original files outside the repository using the [source manifest](../corpus/cognitiveatlas-inputs.yaml). Install `requirements-cognitiveatlas-review.txt`. The original Python 2 generator is not ported or executed, and no pickle is loaded.

```bash
python tools/inspect_cognitive_atlas.py census --source-dir /external/cogat --output /external/census.json --catalog-dir /external/catalog
python tools/inspect_cognitive_atlas.py static --source-dir /external/cogat --output /external/static.json
python tools/inspect_cognitive_atlas.py reason --source-dir /external/cogat --output /external/semantics.json --private-dir /external/reasoner-inputs
python tools/check_cognitiveatlas_review.py --source-dir /external/cogat
```

The [descriptive corpus baseline](../../../docs/research/source-review-descriptives.md) summarizes the completed deep-reading wave and selected formal roots with separate units. It does not close the remaining technical inspections, six comparison batches or final synthesis.

Source definition text is an attributed CC-BY-SA 3.0 US extract. Project code, source code notices, the separate MIT discussion repository, the exact OWL source and current website remain distinct license/version scopes. The original ontology/source files are not redistributed. No independent expert acceptance, historical 2011 equivalence, automatic alignment, Clariceptify model/requirements/fixtures/manuscript change or new release is claimed.
