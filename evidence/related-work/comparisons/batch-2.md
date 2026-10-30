# Batch 2: LMM, O4OA and OntoKADS

Issue #252. [Structured twelve-cell comparison](batch-2.yaml) uses the unchanged v0.1.0 model. The owner directed us to proceed with the available source evidence and retain inaccessible formal material as unknown. The full LMM current four-module closure, O4OA ER 2023 paper plus separately identified 44-page specification, and OntoKADS May 2005 paper are different kinds of evidence. O4OA #91 remains open for its reference root, import and execution criteria.

| Source | What can be used | Boundary |
|---|---|---|
| [LMM](../artifacts/LMM-correspondence.yaml) | Pinned L2 1.2 → L1 1.8 → IOLite 1.8 → DUL 4.2, 29 local LMM classes, 154 asserted closure classes, 13 isolated expectations passing | 2008 historical alignment root unacquired; four class comments absent and three terminology discrepancies retained. Current OWL results do not certify historical parity. |
| [O4OA](../artifacts/O4OA.yaml) | ER 2023 paper and a separate 44-page specification, 138 Table 5 document entries and 24 document CQs | Formal reference ontology and API/solver unavailable; 2.6 versus 6.2 version conflict and Core/Domain orientation discrepancy unresolved. Document entries are not OWL classes. |
| [OntoKADS](../artifacts/OntoKADS.yaml) | May 2005 paper, 72 catalog entries, 22 labeled expressions, eight selected commitments | No author executable root; all machine class/import populations, exact DOLCE edition and solver results unknown. Printed D4 has an unbound variable; A13 alone permits a vacuous prefix. |

**Common case:** Ada chooses K1 over K2 for a sensor observation E at time T, expresses it as X in model M, and records evidence V and rationale J. A later competing interpretation remains visible. **Adverse case:** two distinct expressions share the spelling “bank”; an A13 cutoff predates all action presence; O4OA's written version and Core/Domain claims conflict. These are distinct source-level checks, not a joint consistency run.

| Dimension | LMM | O4OA | OntoKADS | Target model test |
|---|---|---|---|---|
| Agency/activity | Meaning and context without a required deciding actor. | Analysis roles and mental versus artifact levels, with unresolved identity wording. | Reasoning/action, agent interaction and time-indexed Task already covered. | `CLR-C0004`, `CLR-C0026`, `CLR-C0027`: identify the choosing agent and episode. |
| Content/expression/referent | Strong meaning/expression/reference distinction; equal spelling does not merge individuals. | Terms, schemas and ontology levels; written direction/version tensions. | Proposition subject as Concept, Data and KnowledgeRole at paper level. | `CLR-C0017`, `CLR-C0047`, `CLR-C0057`, `CLR-C0101`: separate K/X/E and false reference. |
| Episode/decision/rationale | Context and alignment exist without a dated approver/rationale record in the tested closure. | Ontology versions and document CQs do not by themselves record a choice or executed result. | Task/role classification does not entail evidence and rationale; A13 is insufficient for nonempty presence. | `CLR-C0021`, `CLR-C0042`, `CLR-C0065`, `CLR-C0123`: two alternatives, two times, V/J. |
| Formal/evaluation limits | Current pinned OWL profile, consistency and 13 cases pass; 2008 alignment unacquired. | Specification is inspectable, formal machine root and solver/API results unavailable. | Paper commitments can be checked, formal root/parser/reasoner not executed. | No equivalence/import is accepted from a cross-source comparison. |

Each of the 12 [matrix cells](batch-2.yaml) includes exact source locators, native overlap, required specialization, unsupported inference, counterevidence, unknowns and model IDs. Four mapping questions remain `OWNER_DECISION_REQUIRED`; none is an equivalence axiom.

## Export to final synthesis (#126)

| Question | Provisional gap | Countercase |
|---|---|---|
| CMP2-Q01 | G01, G05 | Ada chooses K1 for a task with V/J and a dated agent role. |
| CMP2-Q02 | G02 | Two expressions with one spelling do not share identity or a guaranteed referent. |
| CMP2-Q03 | G03 | Competing contextual interpretations need not be equivalent. |
| CMP2-Q04 | G04, G05 | A later mapping revision does not license A13 nonempty participation. |

The bounded hypothesis is a tested record of a dated revisable conceptual choice with evidence, rationale, actors and guarded reference. LMM, O4OA and OntoKADS each cover meaningful parts. The matrix does not establish universal absence, source equivalence or adequacy of Clariceptify. Integrate with the other five batches in #126 before any semantic decision in #129.
