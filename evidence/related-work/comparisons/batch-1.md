# Comparison batch 1: DnS, cDnS, DUL, DULConceptualization

Issue #251, `R2-CMP-001`. Research comparison at Clariceptify v0.1.0 / `input-r1-rev1`, baseline commit `661cb4d40238a77f8f321fd99e232676716561b5`. The [machine-readable matrix](batch-1.yaml) is the authority for all 16 cells, exact source digests and locators, limits, model IDs, counterevidence and #126 export. This report summarizes the decision questions; it does not accept mappings.

## Versioned evidence boundaries

| Work | Paper or documentation | Exact selected formal file | Class and definition coverage | Foundation and repository boundary |
| --- | --- | --- | --- | --- |
| DnS | [2003 paper](../deep-reviews/DnS2003/review.yaml), 18 pages and 23 displays | [Later ExtendedDnS397](../artifacts/DnS.yaml), SHA256 `7d69150ed0b67ef4b0cbe0b50b03e64634de02f6a30988f83c26e90c33aadb41` | 58 local, ten external root redeclarations, 95 distinct declared classes in the resolved closure; 58 comments, one insufficient; imported definitions not independently complete | Selected later module imports three 397-family DOLCE-Lite/spatial/temporal files. Official standalone 2005-copyright ZIP, no corresponding development repository identified in the bounded search. Exact 2003 parity unknown; distribution README reports LGPL-2.1-or-later. |
| cDnS | [Distinct 2007](../deep-reviews/cDnS2007/review.yaml) and [2008 journal](../deep-reviews/cDnS-journal-2008/review.yaml) papers | [cDnS1.1 core](../artifacts/cDnS-core-followup.yaml), SHA256 `f0d7b6c795fe9e1a699eda2d80089371336869e981e938648edd5db88358658a` | Core12 local, no import, 12 comment candidates; separately selected collInt25/ground14/core12 map has 51 deduplicated classes and 51 comment candidates. Historical compatibility and extension semantics unverified | Constructive, foundation-neutral paper claim; core has no DOLCE import. Standalone files, no author repository identified in bounded searches; no header permission established. |
| DUL | [2016 chapter 5](../deep-reviews/CLR-RW-DUL/review.yaml), printed81-103, not the whole book | [Current DUL4.2 root](../artifacts/DUL-technical-review.yaml), SHA256 `e5f6429596d2c7014730bad85aaaa9c39530235f27f596cd0e7ce85e6bbcba66` | 78 local, one separate external `owl:Thing`, no imports, 67 descriptive comments, two label-only, nine absent. [Full local catalog](../dul-class-catalog.yaml). | Integrated DOLCE + DnS Ultralite, no root imports. Related DOLCE repository is not the exact 2016 DUL source; historical byte parity and source redistribution permission unestablished. |
| DULConceptualization | [Embedded 0.1 documentation](../reviews/DULConceptualization.yaml), no separate paper established | [Preliminary 0.1 file](../artifacts/DULConceptualization.yaml), SHA256 `75f17194b4096abecf57ebbe1e0f54af665e43f3b75952630744e423fa6365c3` | One local class/comment and eight local object properties; resolved DUL4.2 closure has 80 named declarations including `owl:Thing`. Imported historical edition unknown. | Actual mutable DUL import; standalone file with no repository identified in bounded search and no header redistribution permission. |

The matrix preserves referenced-only/deprecated/imported fields as counts or explicit unknowns, with per-root declaration policies and catalog links. Counts have different units and are not evidence of scientific quality or historical correspondence.

## Four-dimensional result

| Dimension | Supported overlap | Specialization question and contrary evidence |
| --- | --- | --- |
| Agency/activity | DnS communication roles; cDnS agent/schematic conceptualization; DUL agent/action/task; 0.1 conceptualization attitudes | An agent, a role and a dated conceptualization process require a case-specific identity policy. Nested existential restrictions in 0.1 do not force the cognitive system and conceptualizing agent to coincide. [Cells 01-04](batch-1.yaml). |
| Content/expression/referent | DnS semiotic roles and fillers; cDnS information expression; DUL information object/realization; 0.1 internal representation | Specify which expression carries which content and what is referred to. cDnS2008 already generalizes schematic ranges; core aboutness derivation was not reproduced. DUL4.2 does not require a realization for every InformationObject and differs from a standalone Description pattern. [Cells 05-08](batch-1.yaml). |
| Episode/decision/rationale | Situated descriptions, plan/goal/norm and attitude resources can describe context | None of these selected observations alone establishes Clariceptify's recorded conceptual decision with author, time, cited evidence and rationale. A missing named Goal is compatible with an unnamed existential witness. Norm application, compliance and execution are distinct. [Cells 09-12](batch-1.yaml). |
| Formal/evaluation limits | Later DnS397: 15 bounded HermiT expectations; current DUL4.2: 29 bounded cases; cDnS core: eight asserted ASK queries; 0.1: structural review | cDnS1.1 fails the OWL2 DL profile on transitive `hasProperPart` cardinality and HermiT refuses it; its consistency is unknown. Neither test counts nor reuse citations prove original-paper parity, human validation or superiority. [Cells 13-16](batch-1.yaml). |

## Common positive/adverse case

Ada interprets a sensor report as an expression of a Transit concept about event E. During episode T she selects a definition and records decision D with evidence V and a stated rationale. A proposed correspondence must name each distinct agent, process, content, expression, referent, time and evidence link.

In the adverse variant, Ben realizes a copy of the report while Ada conceptualizes a different description at another time; the report cites no evidence for D. Shared labels, unnamed existential witnesses and missing named triples do not merge those entities or establish a rationale. This is a reviewer thought experiment, **not a newly executed reasoner test**. The matrix states native support, required specialization and unsupported inference for each of the four sources.

## Research-use queue for #126

| Candidate | Actual Clariceptify IDs | Next evidence or decision |
| --- | --- | --- |
| CMP1-C01 agent/process identity | `CLR-C0004`, `CLR-C0026` | Specify same-agent and episode identity conditions before reuse. |
| CMP1-C02 content/expression/referent | `CLR-C0017`, `CLR-C0047`, `CLR-C0057`, `CLR-C0062`, `CLR-C0101` | Compare aboutness and realization against contrary version-specific tests. |
| CMP1-C03 recorded decision | `CLR-C0021`, `CLR-C0026`, `CLR-C0042`, `CLR-C0044`, `CLR-C0054`, `CLR-C0123` | Design future positive/adverse decision provenance and time checks. |
| CMP1-C04 formal adoption boundary | `CLR-C0017`, `CLR-C0026`, `CLR-C0123` | Resolve source profile/version limits before semantic mapping. |

All four candidate uses have `OWNER_DECISION_REQUIRED` and `NOT_ESTABLISHED` equivalence. The model, requirements, fixtures, manuscript and release are unchanged. Synthesis #126 must integrate the remaining five comparison batches and their actual blockers before any corpus-level gap conclusion. No third-party raw files are republished.
