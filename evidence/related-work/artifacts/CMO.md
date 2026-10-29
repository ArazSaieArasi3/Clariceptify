# CMO: bounded technical artifact review

Issue #245. Checked 2026-10-30 against Clariceptify baseline `3738d5333fbd348da051cb9aca5322fd4a546b27`. The selected [CEUR paper](https://ceur-ws.org/Vol-833/paper25.pdf) and [pinned third-party mirror](https://github.com/dbpedia/ontology-tracker/blob/32f457a42b910e39ef087b26f1664bd8d507518b/ontologies/purl.org/cmo/v2006/2006-06-30.n3) have separate identities.

The original paper-linked PURL returned 404 in the recorded probe. The mirror N3 file has 147 explicit triples, 7 local classes and 5 external redeclarations. Original 2011 author release/version correspondence is unverified. Its path date does not establish a release date; no source-file license was identified.

[Complete selected class glossary](CMO-class-catalog.md) and [structured catalog](CMO-class-catalog.yaml). The original and imported class populations remain unknown.

| Check | Source locator | Bounded result |
|---|---|---|
| T01: Source identity and FiatEntity/representedByType | CMO:E06,E07,E10,A01; mirror lines 1-14,124-193 | Mirror namespace matches, but original PURL returns 404; FiatEntity and representedByType have no local declarations in this candidate. Mirror path date, original-release identity and source license remain unknown. |
| T02: Punning, self-representation and irreflexivity | CMO:E06,A01; mirror lines 85-98,124-193 | representsUniversal is explicitly owl:IrreflexiveProperty; no general represents irreflexivity or complete class-individual bridge is asserted. The paper's self-representation allowance is a separate claim. |
| T03: BFO/IAO hierarchy and edition | CMO:E03,E06,E07,A01; mirror lines 1-14,139-150,188-193 | Universal subclasses BFO1.1 IndependentContinuant in the mirror; SKOS Concept subclasses IAO_0000030 locally. The paper's GenericallyIndependentContinuant figure/prose discrepancy remains, and original paper edition is unproven. |
| T04: Positive representation witnesses | CMO:E06,A01; mirror lines 139-185 | All four values are zero on representedBy; none entails an existential representation witness. No whole-closure satisfiability claim follows. |
| T05: Noninterference and SKOS chain | CMO:E01,E05,E10,A01; mirror lines 105-119 | The candidate adds exactMatch followed by broader as a chain for broaderTransitive. Its IAO/SKOS imports are not pinned. No conservative-extension proof or noninterference run exists for the combined theory. |
| T06: Query dialect and evaluation reproduction | CMO:E09,A01; evaluation/related-work/cmo/printed-query-parse.json | Current syntax rejection is bounded to the literal printed query; historical dialect, HINTS2005 data, NCIt mapping and bar values were not reproduced. |
| T07: Shared primary anchor and instance retyping | CMO:E07,E10,S03; paper Fig.5 | AdultPerson and MinorPerson may share Person while an adult instance need not be a minor. Fig.5 requires approved identity, qualifier and mapping-policy guards; no author rule engine was run. |
| T08: Conceptual hierarchy and generated subclass | CMO:E10,E11,S04,S12; paper Fig.6 | A topic hierarchy does not by itself establish class extension inclusion. Conflict handling and different-granularity mapping remain unsupported in this source. |

## Scenario and disposition

**Positive:** A typed conceptual vocabulary can annotate two source-model fields through a common Person concept, keeping each logical field distinct; the candidate's SKOS Concept, Type and primary/qualifier predicates supply a source-bound vocabulary pattern, subject to approved anchors.

**Adverse:** AdultPerson and MinorPerson concepts both have Person as primary anchor; a single adult instance does not thereby acquire MinorPerson membership. A qualifier omitted from a Tissue Specimen mapping may erase a clinical distinction. These are conceptual counterexamples, not reasoner-proved full-theory countermodels.

For #255/#126, retain direct conceptual-modeling and vocabulary overlap as counterevidence to absolute novelty. Test a dated conceptual decision with agent, episode, perspective, evidence and rationale against CMO native coverage, rather than inferring their absence from the mirror alone.

The selected mirror is a candidate for comparison, with no accepted equivalence or owner adoption. Historical import closure, full-theory reasoner execution, original query/plot reproduction and independent expert review remain open. No model, requirement, fixture, manuscript or release change was made.
