# DnS: bounded review of the later ExtendedDnS397 module

Issue #235. BOUNDED_SELECTED_LATER_MODULE_REVIEW_COMPLETE_WITH_LIMITS.

Official standalone DLP3971 distribution, copyright 2005, selected ExtendedDnS.owl header 397/classified. Exact 2003 paper fidelity remains NOT_ESTABLISHED. No current cDnS or DUL replacement is used.

| Observed population/check | Result |
|---|---|
| Selected named classes | 58 local / ten external redeclarations |
| Local source comments | 58 present; one insufficient typology placeholder |
| Object-property declarations | 118 local / 15 external; zero datatype properties in selected root |
| Actual imports | DOLCE-Lite, SpatialRelations, TemporalRelations; all supplied files resolved offline |
| Four-document closure | 95 unique declared classes; not a global corpus count |
| Recorded OWL2 DL profile | PASS under pinned OWLAPI |
| Recorded HermiT baseline | Consistent; no unsatisfiable named classes returned |
| Isolated semantic expectations | 15/15 expected positive/adverse outcomes reproduced |

[Complete selected class guide](../dns235-class-catalog.md) | [Structured authority](DnS.yaml) | [Census](../../../evaluation/related-work/dns235/census.json) | [Actual execution receipt](../../../evaluation/related-work/dns235/semantics.json)

## Q01: Identity, population and joint consistency

Official LOA DLP3971 is a later 2005 distribution, not established as exact 2003 implementation. The selected root has 58 local / ten external declarations; the four-document import closure has 95 unique declared classes. All 58 local comment candidates and ten direct-import comment sources are accounted for; non-agentive-figure lacks a distinguishing definition. Baseline and each of information-object/description alone are consistent, but their joint instance is inconsistent. Individual coherence does not establish joint coherence.

Locators: Root header; DnS2003 K01-K04/E02-E04; semantic baseline and separation cases.

## Q02: Scope indices and descriptive entities

concept requires defined-by some description. description uses concepts or figures, requires physical-agent representation and information-object expression. These restrictions are not the indexed Pi/PiD/SDi/Si FOL vocabulary or a proof of its global scope. Denying all description witnesses for a concept, or all representing agents for a description, is inconsistent.

Locators: concept/description restrictions; DnS2003 displays 9/14.

## Q03: Selection and explicit inverse correspondence

The later root explicitly makes classifies inverse to classified-by, with role/course/parameter specializations played-by, sequences and valued-by. This is not a literal selects/selectedBy IRI correspondence or proof of paper display 13. An isolated classification plus denial of its reverse is inconsistent.

Locators: classifies/classified-by/played-by/sequences/valued-by; DnS2003 displays 7/13.

## Q04: Per-setting existential versus shared description

situation is defined by a social-object condition, some setting-for particular and some satisfies description. This supplies a witness per situation; it does not assert one named or globally shared description, a unique description or all finite ground facts. Denying all satisfaction witnesses is inconsistent; ordinary situation instantiation is consistent through unnamed witnesses.

Locators: situation equivalentClass; satisfies/satisfied-by; DnS2003 displays 4/13.

## Q05: Unparenthesized paper formula and later encoding

No silent repair or FOL reconstruction of display 14 is adopted. The complete selected OWL constraints are retained separately; named definition/classification relations do not establish equivalence to either proposed scope reading of that formula. Formula 14 remains a qualified historical correspondence limit, rather than an executed theorem or repaired source.

Locators: DnS2003 K14 and source locators; selected root catalogue constraints.

## Q06: Structural direction and time boundary

temporary-component and temporary-component-of are explicit inverses. Denying the reverse is inconsistent. A component chain with its shortcut denied remains consistent, so transitivity is not forced by this selected profile. TemporalRelations is an actual pinned direct import, but a binary role chain is not the paper temporal t_component signature or a verified ternary translation.

Locators: temporary-component / temporary-component-of; direct TemporalRelations import; DnS2003 Figure 3 / display 17.

## Q07: Parameter values versus actual fillers

parameter has a valued-by existential to region; denying every value is inconsistent. A role with no played-by fillers and a course with no sequences fillers are each consistent. Descriptive classification capability therefore does not require every possible role/course to be actually realized. Source cardinality and existential restrictions stay separate from comment intent.

Locators: parameter/role/course restrictions; DnS2003 displays 18-21 / Figure 1.

## Q08: Communication, meanings and query-role boundary

Information-object is distinct from description in the selected source; each can exist separately but their joint typing is inconsistent. communication-event and expression/aboutness/interpretation relations are present; the selected root is not a complete SWAP message/query-role ontology. Code, message-dependent initiator/resolver/forwarder behavior and successful shared interpretation are not established by this module.

Locators: information-object/description/communication-event; DnS2003 Figures 2-5 / E08-E12.

## Findings and planned use

| Finding | Evidence-qualified conclusion | Utilization categories |
|---|---|---|
| DNS235-F01: Later-distribution identity | 2005/397 source provenance does not establish 2003 byte or axiom fidelity. | U01, U08, U09 |
| DNS235-F02: Definition coverage differs from adequacy | All 58 local comments are present, but non-agentive-figure defers typology and several comments are explicitly tentative. | U03, U09 |
| DNS235-F03: Scope and unit boundaries | 58 local, ten external redeclarations, 95 import-closure declarations and archive-wide 208 are different populations. | U09 |
| DNS235-F04: Witness scope | Unnamed per-situation description witnesses are required; uniqueness or one globally shared description is not established. | U04, U10 |
| DNS235-F05: Inverse correspondence is version-qualified | Explicit classifies/classified-by inverses do not prove equivalence to the earlier paper selects vocabulary. | U04, U08 |
| DNS235-F06: Realization asymmetry | Parameter requires a value, while role and course can remain unfilled; avoid conflating descriptive possibility with current instantiation. | U03, U04, U10 |
| DNS235-F07: Structural temporal limits | An inverse component relation does not force transitivity or implement the earlier temporal signature. | U04, U06, U10 |
| DNS235-F08: Communication scope remains partial | Social description, information object and contextual setting support comparison, not SWAP execution or shared semantic agreement. | U02, U03, U07 |
| DNS235-F09: Conformance is bounded | OWL2 DL profile and 15 isolated reasoner outcomes passed; neither establishes foundational adequacy, historical FOL fidelity or adopted model mappings. | U05, U10 |

## Candidate comparisons, not accepted mappings

Use the [maintained utilization plan](../../../docs/research/review-utilization-plan.md). Comparison #251 and synthesis #126 retain their own prerequisites.

- http://www.loa-cnr.it/ontologies/ExtendedDnS.owl#concept -> CLR-C0017: Compare social classifier identity with the current Concept definition. State: RELATED_CANDIDATE_NOT_EQUIVALENCE.
- http://www.loa-cnr.it/ontologies/ExtendedDnS.owl#description -> CLR-C0026, CLR-C0101: Keep conceptualization process separate from its social description and information representation. State: DISTINCT_LEVELS_TO_ASSESS.
- http://www.loa-cnr.it/ontologies/ExtendedDnS.owl#agent -> CLR-C0004: Review generic agency and its physical/social grounding before any mapping. State: RELATED_CANDIDATE_NOT_EQUIVALENCE.
- http://www.loa-cnr.it/ontologies/ExtendedDnS.owl#goal -> CLR-C0054, CLR-C0061: Compare plan-part desirability with current Goal/Intention identity and dependence. State: RELATED_CANDIDATE_NOT_EQUIVALENCE.

Reuse decision: DEFER_EQUIVALENCE;USE_QUALIFIED_DESCRIPTIVE_PATTERN_CANDIDATES.

Represent one situation under a particular description while retaining separate classification and information expression.

One entity typed as both source information-object and description is inconsistent; copying shared-label mappings can collapse required distinctions.

## Reproduce and interpret

Obtain the exact official DLP3971.zip outside the repository. Install requirements-bdi-review.txt. The existing corpus/dlp3971-intake.json pins the archive and modules. No source rewriting or network import resolution occurs.

```bash
python tools/inspect_dns235.py census --source-dir /external/dns --output /external/census.json
python tools/inspect_dns235.py reason --source-dir /external/dns --private-dir /external/reasoning --output /external/semantics.json
python tools/check_dns235.py --source-dir /external/dns
```

Initial separately parsed fixtures omitted property declarations and three inverse controls were misparsed. Final fixtures declare only properties already declared by the exact source; source files and axioms remain unchanged. All 15 final outcomes are retained.

OWL2 profile/reasoner outcomes concern loaded logical axioms under the recorded tools. They do not prove the earlier FOL formulas, a complete theory of conceptualization, source-definition adequacy or accepted alignment. Formula 14 and SWAP are not solver/execution claims. README LGPL-2.1-or-later applies to its source distribution; original ontology files/comments are not republished here. No Clariceptify model, requirements, fixtures, manuscript or release changed.
