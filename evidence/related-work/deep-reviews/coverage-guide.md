# What a completed deep review does and does not cover

A primary-paper review and a technical artifact inspection are different deliverables. Closing one does not automatically close the other. Every source/version and execution state must remain visible.

## Three coverage layers

| Layer | Required coverage | Completion does not establish |
|---|---|---|
| Full paper | Every page, section, figure, table, appendix, footnote and relevant bibliography; every ontology-bearing category/distinction, relation, constraint, numbered formula, example and evaluation claim | Every class in a different or later released ontology, correctness of all arguments, or independent expert acceptance |
| Retained artifact | Exact bytes/version, all explicitly declared local named classes/properties and their constraints when a full census is recorded; actual imports and dependencies, license/version limits and paper correspondence | Missing external modules, an unacquired historical version, inferred classes or full semantic equivalence |
| Semantic execution | Explicitly named profile/reasoner/SHACL/query/FOL runs, fixtures, expected outcomes, tool versions, results and limitations | Tests that were not run, all logically possible consequences, human validation or global adequacy |

The complete paper catalog has no eight-concept limit. The existing eight-selected-commitment limit belongs to bounded semantic artifact checks. It is compatible with a full declaration census: inventory every declared entity, then use medium follow-ups for deeper semantic obligations. Inventory and source inspection must never be described as a completed exhaustive inference proof.

## Current completed-paper boundaries

| Paper dossier | Full-paper coverage | Retained artifact coverage | Remaining technical work |
|---|---|---|---|
| OntoKADS2005, #74 | Complete paper-level catalog and labeled formulas | No corresponding version-pinned executable distribution identified in the retained corpus | #236 discovery and inspection |
| IAO2015, #78 | Complete paper-level definitions, arguments, examples and table | Repository retained; release/development identity checked, current root distinguished from the 2015 proposal | #240 root selection, imports, full census and bounded semantic tests |
| EFO, #80 | Complete category map, all labeled formulas and arguments | Printed FOL outline available; separate machine-readable distribution not identified in the retained corpus | #242 artifact discovery and technical inspection |
| cDnS2007, #259 | All 40 pages, 141 numbered displays including examples, all paper categories/relations, one table and both figures | Entire retained cDnS1.1 parsed; all 12 named classes manually reviewed; all 47 object properties and their declared constraints inventoried; no declared imports | #267 profile and eight correspondence checks; #263 distinct 2008 paper |
| LMM2008, #260 | All seven pages, all six figures, complete diagram-slot ledger, 52 paper conceptual/distinction entries and all 16 references | Full retained L1/L2 censuses and all 29 local classes manually reviewed; existing 154-IRI asserted import closure retained; four missing definition comments explicit | #274 eight correspondence/semantic questions; #88/#271 imported DUL/IOLite definitions; original alignment root not acquired |
| DnS2003, #261 | All 18 pages, all 23 numbered displays, five figures, eight content footnotes and 18 references; complete paper category/role/filler and formal ledger | Official DLP3971 ZIP retained;11 modules parsed, all candidate class IRIs/comment availability indexed; ExtendedDnS397 has 58 local classes plus 10 external redeclarations | #235 exact 2003 correspondence, all 58 local manual definitions/constraints and eight bounded checks; #251 comparison |
| CMO, #83 | All nine pages after OCR and original-page inspection, six figures, five footnotes, 37 references, all three use cases/five requirements and complete paper concept/property/rule catalog | One pinned third-party candidate: all 12 named class declarations/20 object properties inventoried; all seven local classes manually reviewed (six comment candidates, one descriptive seeAlso literal) | #245 original-author identity, historical imports, missing terms and eight semantic questions; #255 comparison |

The cDnS core is not the complete plan/norm/collective theory in the paper. The absence of those classes in that one file is neither absence in the paper nor proof that no related module exists. Its header binds it to the 2008 article, whose full text has not been acquired.

## Shared analytical dimensions

1. Identity, versions, bibliographic discrepancies and complete reading coverage.
2. Problem, research questions, contributions and supported gap claims.
3. Research and ontology-engineering method, sources and construction process.
4. Scope, users, requirements, competency questions and positive/adverse scenarios.
5. Concepts, categories, definitions, hierarchy, reuse and classification level.
6. Relations, signatures, cardinality, constraints, formulas and local consequences.
7. Foundations, identity, dependence, agency, mental/content/expression/referent distinctions, time and context.
8. Repository/files/modules/imports, licenses, source/version correspondence and reproducibility.
9. Verification, Validation, Evaluation, Assessment and Assurance, with actual evidence populations.
10. Strengths, weaknesses, contrary evidence, validity limits, open questions and candidate later uses.

Every substantive observation has a stable evidence ID and an exact locator. Author-reported, reviewer-interpreted, executed, not-reported and unknown evidence remain distinct. All later uses await the owner's decision after synthesis; this research does not alter Clariceptify.

## Mandatory repository, definition and foundation supplement

The [source audit](source-audit.md) now records all 19 exact paper/version records and four separate documentation sources under [catalog-contract.yaml](catalog-contract.yaml). Each source must have a dated repository discovery outcome, actual file/version state, complete local/imported class populations, definitions or explicit gaps, and the exact kind of foundational relation. Unknown is not zero or nonexistence.

All 12 local cDnS1.1 classes, all 29 local LMM L1/L2 classes and the one local Conceptualization0.1 class have selected-module glossaries and complete declaration/constraint censuses. Thirty-eight of the 42 classes have source comment candidates with short attributed reviewer paraphrases; four LMM classes have no definition comment and remain explicit missing-definition findings. Comment candidates do not establish sufficient logical definitions. LMM's other 125 unique asserted-closure IRIs (124 DUL/IOLite classes and owl:Thing) are not a completed imported glossary; DUL #88 and IOLite #271 retain that work.

Foundation family, exact edition, paper claim, project-documentation claim, actual import, conceptual reuse/alignment and independent foundation are separate. O4OA's author documentation names UFO-A/B/C and gUFO; those module names do not mean UFO1. IAO's 2015 dossier establishes the BFO family, not BFO1 from the family name alone. cDnS2007 claims ground-ontology independence, while its retained core has no declared imports. This supplement does not automatically add new prerelease gates or close final synthesis #126.

Reproduce structural/definition-annotation checks with `python tools/check_source_audit.py --source-dir /path/to/private/corpus-vault`. Public CI validates retained census hashes, exact local class sets, source identities, derived readers, unknowns and completion boundaries without redistributing raw third-party annotations. Raw annotation reconciliation is recorded only when actually run with the private sources.

The four selected raw source files were actually reconciled against the 42 class rows, annotation hashes and asserted hierarchies; see the [executed private-source reconciliation record](../../../evaluation/related-work/class-catalogs/raw-source-reconciliation.json). Public CI deliberately does not claim to repeat that raw-source run.
