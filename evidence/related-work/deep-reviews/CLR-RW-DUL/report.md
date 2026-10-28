# Dolce+D&S Ultralite and its main ontology design patterns

Work: `CLR-RW-DUL` | Issue: #70 | State: `REVIEW_COMPLETE`

Reviewed version: Chapter5 in Ontology Engineering with Ontology Design Patterns: Foundations and Applications, printed81-103; supplied book PDF98-120. Input: `DUL-2016-book-owner.pdf`, 389 PDF pages, SHA256 `6605f2d66dbd6a0a7af21bfa7f0802050abd2c5122c0c5410bfb073479a29ca8`.

The structured `review.yaml` is the evidence authority; this report is derived. This is an AI-assisted critical review, not independent expert acceptance. Clariceptify is unchanged; later use requires an owner decision.

## Identity and reading coverage

The389-page owner book is the source container; only23 chapter pages were reviewed. PDF n maps to printed n-17. PDF121 is blank; PDF122 begins chapter6. Current DUL4.2 and standalone sample files are separate versioned evidence, not an established exact2016 implementation. No public redistribution of book or OWL bytes.

Complete selected chapter, not whole book: all23 pages,19 pattern subsections, all six figures/visible interfaces, nine notes and39 references. No numbered formulas/tables/appendices. Paper concepts, pattern commitments, UML interfaces and retained machine class populations remain distinct.

| Paper unit | Coverage | Evidence |
|---|---|---|
| Chapter identity/front matter | REVIEWED | E01 |
| 5.1 Introduction | REVIEWED | E02 |
| 5.2 Five input theories | REVIEWED | E05 |
| 5.2.1 DOLCE principles | REVIEWED | E03 |
| 5.2.1.1 Endurants/perdurants | REVIEWED | E03 |
| 5.2.1.2 Qualities | REVIEWED | E03 |
| 5.2.1.3 Abstracts | REVIEWED | E03 |
| 5.2.1.4 Main relations | REVIEWED | E03, E20 |
| 5.2.2 D&S | REVIEWED | E04 |
| 5.2.3 Plan | REVIEWED | E05 |
| 5.2.4 Information Object | REVIEWED | E05 |
| 5.2.5 Collection | REVIEWED | E05, E09 |
| 5.2.6 DUL integration | REVIEWED | E05 |
| 5.3 Pattern catalogue introduction | REVIEWED | E06 |
| 5.3.1 Events and participation | REVIEWED | E06 |
| 5.3.2 Quality of entities | REVIEWED | E07 |
| 5.3.3 Region | REVIEWED | E07 |
| 5.3.3.1 Time Interval | REVIEWED | E07 |
| 5.3.4 Entity Classification | REVIEWED | E08 |
| 5.3.4.1 Role Classification | REVIEWED | E08 |
| 5.3.4.2 Parameter Classification | REVIEWED | E08 |
| 5.3.4.3 Task Classification | REVIEWED | E08 |
| 5.3.5 Collection and Membership | REVIEWED | E09 |
| 5.3.6 Location | REVIEWED | E10 |
| 5.3.7 Part-whole | REVIEWED | E10 |
| 5.3.7.1 Component | REVIEWED | E10 |
| 5.3.8 Constitution | REVIEWED | E11 |
| 5.3.9 Sequence | REVIEWED | E11 |
| 5.3.10 Information Realisation | REVIEWED | E12 |
| 5.3.11 Description | REVIEWED | E13 |
| 5.3.11.1 Plan | REVIEWED | E13 |
| 5.3.12 Situation | REVIEWED | E14 |
| 5.3.13 Time-indexed participation | REVIEWED | E14 |
| 5.4 UML component notation | REVIEWED | E15 |
| 5.4.1 Composing ODPs | REVIEWED | E16 |
| 5.4.2 DUL composition | REVIEWED | E16 |
| 5.5 All reuse examples | REVIEWED | E17 |
| 5.6 Conclusion | REVIEWED | E18 |
| Figure5.1 complete literal matrix | REVIEWED | E20 |
| Figure5.2 all eight nodes/twelve links | REVIEWED | E05 |
| Figure5.3 both stereotypes/intent tag | REVIEWED | E15 |
| Figure5.4 sample components/interfaces | REVIEWED | E15 |
| Figure5.5 all sixteen components/displayed interfaces | REVIEWED | E21 |
| Figure5.6 combined module and three internal patterns | REVIEWED | E22 |
| All nine numbered notes | REVIEWED | E19 |
| All39 bibliography entries | REVIEWED | E01 |

## Common review dimensions

### D1_identity_coverage

Exact2016 two-author chapter, printed81-103/PDF98-120 only, all23 pages, six figures, nine notes and39 references. No numbered formulas, numbered tables or appendices occur in this chapter. [REVIEWER_INTERPRETATION; E01, E19]

### D2_problem_contribution

A handbook-style account of DUL foundations, focused design patterns and a UML documentation notation. Independent pattern intent differs from composed foundational commitments. [AUTHOR_REPORTED; E02, E05, E15, E16]

### D3_method

Explain five source theories; present modeling issue/solution/sample patterns; demonstrate hypothetical recomposition through component interfaces. This is conceptual/tutorial exposition, not a reproduced experiment. [REVIEWER_INTERPRETATION; E02, E05, E16, E18]

### D4_requirements

All nineteen issue/solution subsections provide explicit user modeling needs and examples; no formal numbered CQ suite or evaluated acceptance benchmark is supplied. [REVIEWER_INTERPRETATION; E06, E07, E08, E09, E10, E11, E12, E13, E14]

### D5_concepts

Catalog keeps foundations, reified concepts, nineteen pattern subsections, diagram classes/interfaces and relation names separate from released OWL populations. Figure5.2 is an eight-node schematic, not all78 retained classes. [REVIEWER_INTERPRETATION; E03, E04, E05, E21]

### D6_relations_formalization

Prose gives signatures, inverses, disjointness, existential/universal and transitivity/symmetry commitments. No printed numbered DL/FOL formulas occur; reviewer paraphrases are not source formulas or executed proofs. [REVIEWER_INTERPRETATION; E06, E07, E10, E11, E12, E13, E14, E16]

### D7_grounding

DUL simplifies and integrates DOLCE, D&S, Plan, IO and Collection. Modal/temporal loss, social-object typing and local composition choices must be distinguished from exact imports and historical release identity. [REVIEWER_INTERPRETATION; E03, E05, E16, E19]

### D8_artifact_correspondence

Canonical root bytes match retained DUL4.2; two sample files were parsed for selected statements. An exact2016 distribution, all local manual definitions and complete sample imports remain #88; the official related DOLCE repo is not this DUL source. [REVIEWER_INTERPRETATION; E19, E23, E24, E25]

### D9_evaluation

Illustrative solutions and cited applications support exposition; no new participant, effectiveness, benchmark, reasoner, consistency-proof or comparative-superiority result is reported in this chapter. [NOT_REPORTED; E17, E18]

### D10_critical_synthesis

Prior overlap in conceptualization/context/classification is substantial, but theory/pattern/version/implementation distinctions and eight unresolved technical questions prevent immediate equivalence or adoption. [REVIEWER_INTERPRETATION; E02, E04, E08, E16, E20, E23]

## Conceptual catalog

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| C001 / Ontology Design Pattern | Reusable focused modeling solution, distinct from a particular implementation and full foundational ontology. | AUTHOR_REPORTED; E02 |
| C002 / DUL | Lightweight integration of five theories for Semantic Web modeling; not a guaranteed full-modal DOLCE translation. | AUTHOR_REPORTED; E05, E19 |
| C003 / DOLCE | Foundational source with an S5 original account and four disjoint categories in this chapter. | AUTHOR_REPORTED; E03 |
| C004 / D&S | Reified descriptions, concepts, entities and situations organize intensional/extensional distinctions. | AUTHOR_REPORTED; E04 |
| C005 / Plan ontology | Source of plans, executions, goals, tasks, roles and parameters. | AUTHOR_REPORTED; E05 |
| C006 / Information Object ontology | Social information entities and distinct realizations enable communication and replication across media. | AUTHOR_REPORTED; E05, E12 |
| C007 / Collection ontology | Collections/collectives are individual entities; membership is not instantiation. | AUTHOR_REPORTED; E05, E09 |
| C008 / Endurant / Object | Wholly present during existence; DUL Object is an intuitive term with simplified commitments. | AUTHOR_REPORTED; E03, E05 |
| C009 / Perdurant / Event | Temporally extended entity with temporal parts; DUL Event does not retain all original modal/temporal indexing. | AUTHOR_REPORTED; E03, E05, E19 |
| C010 / Quality | Particular bearer-dependent aspect, distinct from its value; a quality may itself have qualities. | AUTHOR_REPORTED; E03, E07 |
| C011 / Quale / quality value | Position/value in a quality space, not the bearer-specific quality itself. | AUTHOR_REPORTED; E03 |
| C012 / Abstract / Region / Quality Space | Original DOLCE abstracts are nonspatial/nontemporal; Region and Quality Space appear in the simplified patterns with locally stated relations. | AUTHOR_REPORTED; E03, E07 |
| C013 / Social Object / Physical Object | Paper distinguishes these disjoint Object specializations and locates descriptions/concepts/situations on the social side. | AUTHOR_REPORTED; E05, E19 |
| C014 / Description | First-order reified conceptualization; descriptions define concepts rather than merely labeling them. | AUTHOR_REPORTED; E04, E13 |
| C015 / Concept | First-order classificatory entity; classifies an entity while permitting facts about the concept. | AUTHOR_REPORTED; E04, E08 |
| C016 / Entity | Thing that may be classified or occur as a situational participant; no claim of a complete top taxonomy. | AUTHOR_REPORTED; E04 |
| C017 / Situation | Reified state of affairs/context can involve participants and satisfy descriptions. | AUTHOR_REPORTED; E04, E14, E16 |
| C018 / Role | Concept used to classify role players; instance-level role assertions differ from OWL subclassing. | AUTHOR_REPORTED; E05, E08 |
| C019 / Task / Action | Task classifies an action; a task concept is not its execution. | AUTHOR_REPORTED; E05, E08 |
| C020 / Parameter | Concept classifying regions; a datatype-shortcut alternative changes representation structure. | AUTHOR_REPORTED; E05, E08 |
| C021 / Plan / Plan Execution | Description of goals/tasks/roles/parameters differs from a situation of actual execution. | AUTHOR_REPORTED; E05, E13, E14 |
| C022 / Goal | Required plan component in the described Plan solution; not automatically a mental intention. | AUTHOR_REPORTED; E13 |
| C023 / Information Object / Information Realisation | Information entity and concrete realization are distinct/disjoint in the presented pattern with mutual existential commitments. | AUTHOR_REPORTED; E05, E12 |
| C024 / Collection / Collective | Container-like individual and social grouping; members need not be named or enumerated in the account. | AUTHOR_REPORTED; E05, E09 |
| C025 / Place | Approximate or relational location, distinguished from precise dimensional Region values. | AUTHOR_REPORTED; E10 |
| C026 / Time Interval | Region specialization with date values; begin/end/format meanings need further constraints. | AUTHOR_REPORTED; E07 |
| C027 / Time Indexed Participation / Time Indexed Situation | Prose names used in the external illustrative specialization; do not collapse parent/specialized types or rewrite current imported signatures. | AUTHOR_REPORTED; E14, E25 |
| C028 / Parthood / Component / Constituent | Transitive mereology, direct structural relation and layered constitution solve different problems. | AUTHOR_REPORTED; E03, E10, E11 |
| C029 / Ontology Module / ODP stereotype | UML component profile where ODP specializes OM and carries an intent tag; not an OWL subclass assertion. | AUTHOR_REPORTED; E15 |
| C030 / Interface / uses / realizes | Design-time promised interface and implementation-time vocabulary exposure are different states. | AUTHOR_REPORTED; E15 |
| C031 / Intent / design / implementation | Intent documents a modeling problem; monolithic implementation can still realize modular pattern design. | AUTHOR_REPORTED; E02, E15, E16 |
| C032 / Punning / reification | Separate OWL interpretations do not themselves encode D&S conceptual commitments. | AUTHOR_REPORTED; E04 |
| C033 / Local universal restriction / composition axiom | Combining ODPs adds type restrictions beyond independent pattern commitments. | AUTHOR_REPORTED; E16 |
| C034 / Events and participation ODP | Disjoint classes, inverse property typing and an existential obligation in each direction. | AUTHOR_REPORTED; E06 |
| C035 / Quality of entities ODP | Qualities are bearer-specific; quality and space disjoint; mutual quality/space existential association. | AUTHOR_REPORTED; E07 |
| C036 / Region ODP | Reify dimensional values/spaces and associate typed data values; optional composition with quality, sequence and parthood. | AUTHOR_REPORTED; E07 |
| C037 / Time Interval ODP | Specialize region; multiple date values may encode boundaries, holding dates or formats without an ordered interval calculus. | AUTHOR_REPORTED; E07 |
| C038 / Entity Classification ODP | Represent classifying concepts as first-order objects with their own facts. | AUTHOR_REPORTED; E08 |
| C039 / Role Classification ODP | Specialize conceptual classification for contextually played roles. | AUTHOR_REPORTED; E08 |
| C040 / Parameter Classification ODP | Classify a region using a parameter; alternative shortcuts region individuals with a datatype property. | AUTHOR_REPORTED; E08 |
| C041 / Task Classification ODP | Classify an action by a task; context of a whole plan is not required in this isolated pattern. | AUTHOR_REPORTED; E08 |
| C042 / Collection and Membership ODP | Represent a collection as an object, not a class of which each member is an instance; described pattern does not force a known/member witness. | AUTHOR_REPORTED; E09 |
| C043 / Location ODP | Approximate place associated to at least one entity; precise spatial values use Region separately. | AUTHOR_REPORTED; E10 |
| C044 / Part-whole ODP | Transitive parthood supports part-of-part inference. | AUTHOR_REPORTED; E10 |
| C045 / Component ODP | Direct component relation does not license transitive shortcuts; this alone is not an intransitivity axiom. | AUTHOR_REPORTED; E10 |
| C046 / Constitution ODP | Different layers can constitute each other without being mereological parts; local restrictions depend on the layer theory. | AUTHOR_REPORTED; E11 |
| C047 / Sequence ODP | Transitive sequencing and symmetric overlap; strictness, acyclicity and interval algebra are not supplied here. | AUTHOR_REPORTED; E11 |
| C048 / Information Realisation ODP | Disjoint information object and concrete realization classes; inverse realization with mutual existentials. | AUTHOR_REPORTED; E12 |
| C049 / Description ODP | Reified conceptualization defines concepts; this pattern explicitly separates the two classes. | AUTHOR_REPORTED; E13 |
| C050 / Plan ODP | Specialize Description, combine classification families and require a Goal as a direct component. | AUTHOR_REPORTED; E13 |
| C051 / Situation ODP | Reify observed states of affairs and relational context; combine with Description and classification for the D&S core. | AUTHOR_REPORTED; E14 |
| C052 / Time-indexed participation ODP | An illustrative Situation specialization; source prose uses both participation/situation type names. Interval objects and date literals are alternative models. | AUTHOR_REPORTED; E14 |
| C053 / atemporal / temporal parthood | Original typed/time-sensitive relations; Figure5.1 and prose disagree on the Abstract row. | AUTHOR_REPORTED; E03, E20 |
| C054 / constitution | Co-presence/co-location with different persistence and histories; not identity. | AUTHOR_REPORTED; E03 |
| C055 / participation | Original time-indexed endurant/perdurant relation, distinct from the binary isolated pattern. | AUTHOR_REPORTED; E03, E06 |
| C056 / inherence / quale | Bearer-to-quality and quality-to-value links must remain different. | AUTHOR_REPORTED; E03 |
| C057 / participates in / has participant | Inverse Object/Event relation with two existential prose commitments. | AUTHOR_REPORTED; E06 |
| C058 / has quality / is quality of | Entity/quality association; do not collapse quality into its literal value. | AUTHOR_REPORTED; E07 |
| C059 / has region / is region for | Quality/space signature in one pattern and general association in Region; global domains need reconciliation. | AUTHOR_REPORTED; E07 |
| C060 / has region data value | Region-to-literal datatype association. | AUTHOR_REPORTED; E07 |
| C061 / has interval date / has time interval | Dates associated with intervals versus entity-to-interval association. | AUTHOR_REPORTED; E07 |
| C062 / classifies / classified by | Concept-to-classified-entity relation; Figure5.5 prints is classified By. | AUTHOR_REPORTED; E08, E21 |
| C063 / is role of / has role | Role classification inverse pair. | AUTHOR_REPORTED; E08 |
| C064 / is parameter of / has parameter | Parameter-to-region classification in prose; diagram parameterization labels are separately recorded. | AUTHOR_REPORTED; E08 |
| C065 / is parameter for region data value | Datatype alternative that bypasses region individuals. | AUTHOR_REPORTED; E08 |
| C066 / is task of / has task / task addressed by / addresses task | Task/action classification and proposed more specific labels. | AUTHOR_REPORTED; E08 |
| C067 / has member / is member of | Membership relation distinct from rdf:type. | AUTHOR_REPORTED; E09 |
| C068 / is location of / has location | Place/located-entity relation; one associated entity existential is described. | AUTHOR_REPORTED; E10 |
| C069 / has part / is part of | Transitive parthood inverse pair. | AUTHOR_REPORTED; E10 |
| C070 / has component / is component of | Direct component relation with no transitive shortcut; no intransitivity inferred. | AUTHOR_REPORTED; E10 |
| C071 / has constituent / is constitutent of | Printed inverse typo retained as a prose label; Figure5.5 uses constituent spelling. | AUTHOR_REPORTED; E11, E21 |
| C072 / preceeds / follows / overlaps | Printed preceeds spelling; sequence transitivity and overlap symmetry only. | AUTHOR_REPORTED; E11 |
| C073 / is realised by / realises | Inverse information realization relation; disjoint classes with mutual existentials. | AUTHOR_REPORTED; E12 |
| C074 / defines / is defined by | Description-to-Concept relation and inverse; Plan reuses it. | AUTHOR_REPORTED; E13 |
| C075 / is setting for | Situation-to-involved-entity relation for contextual n-ary modeling. | AUTHOR_REPORTED; E14 |
| C076 / has participant / is participant in | Time-indexed specialization uses situation-based participation labels; differs from unqualified binary pattern context. | AUTHOR_REPORTED; E14 |
| C077 / at time (object property) | Relation to an interval; source prose gives Time Indexed Situation as domain. | AUTHOR_REPORTED; E14 |
| C078 / at time (datatype alternative) | Alternative date-literal model with Time Indexed Participation domain; not simultaneous OWL object/datatype use claimed. | AUTHOR_REPORTED; E14 |
| C079 / satisfies / is satisfied by | Composition-added inverse interface; text permits satisfaction and does not state a new global totality axiom. | AUTHOR_REPORTED; E16, E22 |
| C080 / parametrizes / is parametrized By | Literal Figure5.5 interface labels; not silently equated to prose or current IRIs. | AUTHOR_REPORTED; E21 |
| C081 / precedes/follows / directly precedes/follows | Diagram gives direct sequence interfaces beyond the simpler prose solution. | AUTHOR_REPORTED; E21 |
| C082 / is time interval Of / has time interval | Figure5.5 interval interface pair. | AUTHOR_REPORTED; E21 |
| C083 / is about / is reference of | Information Realisation diagram interfaces; not separately axiomatized by5.3.10 prose. | AUTHOR_REPORTED; E21 |
| C084 / rdfs:subClassOf / defines / classifies / isSettingFor / satisfies | Five distinct Figure5.2 edge types; classification is not subclassing. | AUTHOR_REPORTED; E05 |

## Relations and formal commitments

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| K-5.3.1 / Events and participation | Disjoint classes, inverse property typing and an existential obligation in each direction. | AUTHOR_REPORTED; E06 |
| K-5.3.2 / Quality of entities | Qualities are bearer-specific; quality and space disjoint; mutual quality/space existential association. | AUTHOR_REPORTED; E07 |
| K-5.3.3 / Region | Reify dimensional values/spaces and associate typed data values; optional composition with quality, sequence and parthood. | AUTHOR_REPORTED; E07 |
| K-5.3.3.1 / Time Interval | Specialize region; multiple date values may encode boundaries, holding dates or formats without an ordered interval calculus. | AUTHOR_REPORTED; E07 |
| K-5.3.4 / Entity Classification | Represent classifying concepts as first-order objects with their own facts. | AUTHOR_REPORTED; E08 |
| K-5.3.4.1 / Role Classification | Specialize conceptual classification for contextually played roles. | AUTHOR_REPORTED; E08 |
| K-5.3.4.2 / Parameter Classification | Classify a region using a parameter; alternative shortcuts region individuals with a datatype property. | AUTHOR_REPORTED; E08 |
| K-5.3.4.3 / Task Classification | Classify an action by a task; context of a whole plan is not required in this isolated pattern. | AUTHOR_REPORTED; E08 |
| K-5.3.5 / Collection and Membership | Represent a collection as an object, not a class of which each member is an instance; described pattern does not force a known/member witness. | AUTHOR_REPORTED; E09 |
| K-5.3.6 / Location | Approximate place associated to at least one entity; precise spatial values use Region separately. | AUTHOR_REPORTED; E10 |
| K-5.3.7 / Part-whole | Transitive parthood supports part-of-part inference. | AUTHOR_REPORTED; E10 |
| K-5.3.7.1 / Component | Direct component relation does not license transitive shortcuts; this alone is not an intransitivity axiom. | AUTHOR_REPORTED; E10 |
| K-5.3.8 / Constitution | Different layers can constitute each other without being mereological parts; local restrictions depend on the layer theory. | AUTHOR_REPORTED; E11 |
| K-5.3.9 / Sequence | Transitive sequencing and symmetric overlap; strictness, acyclicity and interval algebra are not supplied here. | AUTHOR_REPORTED; E11 |
| K-5.3.10 / Information Realisation | Disjoint information object and concrete realization classes; inverse realization with mutual existentials. | AUTHOR_REPORTED; E12 |
| K-5.3.11 / Description | Reified conceptualization defines concepts; this pattern explicitly separates the two classes. | AUTHOR_REPORTED; E13 |
| K-5.3.11.1 / Plan | Specialize Description, combine classification families and require a Goal as a direct component. | AUTHOR_REPORTED; E13 |
| K-5.3.12 / Situation | Reify observed states of affairs and relational context; combine with Description and classification for the D&S core. | AUTHOR_REPORTED; E14 |
| K-5.3.13 / Time-indexed participation | An illustrative Situation specialization; source prose uses both participation/situation type names. Interval objects and date literals are alternative models. | AUTHOR_REPORTED; E14 |
| K20 / Original four-way distinction | Endurant, Perdurant, Quality and Abstract are pairwise disjoint in the presented DOLCE account. | AUTHOR_REPORTED; E03 |
| K21 / Quality individuation | Qualities of distinct bearers are distinct even when their qualia coincide; quality and value are not interchangeable. | AUTHOR_REPORTED; E03 |
| K22 / Constitution versus identity | Co-localized/co-present constituent and constituted thing have different persistence/history criteria. | AUTHOR_REPORTED; E03 |
| K23 / Modal/temporal loss | The chapter footnote explicitly says temporal/possible-world indexing was left out of DOLCE-Lite; lighter DUL is not merely lexical substitution. | AUTHOR_REPORTED; E05, E19 |
| K24 / Core DUL disjointness | Object, Event, Region and Quality are disjoint in the recomposition narrative. | AUTHOR_REPORTED; E16 |
| K25 / Social-object composition | Descriptions, concepts and situations are assigned to social objects. Broad statements about every added pattern class require careful typing, especially physical realizations. | AUTHOR_REPORTED; E16, E19 |
| K26 / Concept parts restriction | Composing patterns adds Concept SubClassOf (has part only Concept) as a prose example, not a complete DL theory in this chapter. | AUTHOR_REPORTED; E16 |
| K27 / Satisfaction packaging | Satisfaction may be added to Situation, to Description, or to a combined module; one packaging is not the sole formal authority. | AUTHOR_REPORTED; E16, E22 |
| K28 / Pattern versus implementation | Pattern reuse may use local templates or imports; monolithic same-namespace files can still embody pattern composition. | AUTHOR_REPORTED; E02, E15, E16 |

## Complete paper relation index

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| R01 / atemporal / temporal parthood | Original typed/time-sensitive relations; Figure5.1 and prose disagree on the Abstract row. | AUTHOR_REPORTED; E03, E20 |
| R02 / constitution | Co-presence/co-location with different persistence and histories; not identity. | AUTHOR_REPORTED; E03 |
| R03 / participation | Original time-indexed endurant/perdurant relation, distinct from the binary isolated pattern. | AUTHOR_REPORTED; E03, E06 |
| R04 / inherence / quale | Bearer-to-quality and quality-to-value links must remain different. | AUTHOR_REPORTED; E03 |
| R05 / participates in / has participant | Inverse Object/Event relation with two existential prose commitments. | AUTHOR_REPORTED; E06 |
| R06 / has quality / is quality of | Entity/quality association; do not collapse quality into its literal value. | AUTHOR_REPORTED; E07 |
| R07 / has region / is region for | Quality/space signature in one pattern and general association in Region; global domains need reconciliation. | AUTHOR_REPORTED; E07 |
| R08 / has region data value | Region-to-literal datatype association. | AUTHOR_REPORTED; E07 |
| R09 / has interval date / has time interval | Dates associated with intervals versus entity-to-interval association. | AUTHOR_REPORTED; E07 |
| R10 / classifies / classified by | Concept-to-classified-entity relation; Figure5.5 prints is classified By. | AUTHOR_REPORTED; E08, E21 |
| R11 / is role of / has role | Role classification inverse pair. | AUTHOR_REPORTED; E08 |
| R12 / is parameter of / has parameter | Parameter-to-region classification in prose; diagram parameterization labels are separately recorded. | AUTHOR_REPORTED; E08 |
| R13 / is parameter for region data value | Datatype alternative that bypasses region individuals. | AUTHOR_REPORTED; E08 |
| R14 / is task of / has task / task addressed by / addresses task | Task/action classification and proposed more specific labels. | AUTHOR_REPORTED; E08 |
| R15 / has member / is member of | Membership relation distinct from rdf:type. | AUTHOR_REPORTED; E09 |
| R16 / is location of / has location | Place/located-entity relation; one associated entity existential is described. | AUTHOR_REPORTED; E10 |
| R17 / has part / is part of | Transitive parthood inverse pair. | AUTHOR_REPORTED; E10 |
| R18 / has component / is component of | Direct component relation with no transitive shortcut; no intransitivity inferred. | AUTHOR_REPORTED; E10 |
| R19 / has constituent / is constitutent of | Printed inverse typo retained as a prose label; Figure5.5 uses constituent spelling. | AUTHOR_REPORTED; E11, E21 |
| R20 / preceeds / follows / overlaps | Printed preceeds spelling; sequence transitivity and overlap symmetry only. | AUTHOR_REPORTED; E11 |
| R21 / is realised by / realises | Inverse information realization relation; disjoint classes with mutual existentials. | AUTHOR_REPORTED; E12 |
| R22 / defines / is defined by | Description-to-Concept relation and inverse; Plan reuses it. | AUTHOR_REPORTED; E13 |
| R23 / is setting for | Situation-to-involved-entity relation for contextual n-ary modeling. | AUTHOR_REPORTED; E14 |
| R24 / has participant / is participant in | Time-indexed specialization uses situation-based participation labels; differs from unqualified binary pattern context. | AUTHOR_REPORTED; E14 |
| R25 / at time (object property) | Relation to an interval; source prose gives Time Indexed Situation as domain. | AUTHOR_REPORTED; E14 |
| R26 / at time (datatype alternative) | Alternative date-literal model with Time Indexed Participation domain; not simultaneous OWL object/datatype use claimed. | AUTHOR_REPORTED; E14 |
| R27 / satisfies / is satisfied by | Composition-added inverse interface; text permits satisfaction and does not state a new global totality axiom. | AUTHOR_REPORTED; E16, E22 |
| R28 / parametrizes / is parametrized By | Literal Figure5.5 interface labels; not silently equated to prose or current IRIs. | AUTHOR_REPORTED; E21 |
| R29 / precedes/follows / directly precedes/follows | Diagram gives direct sequence interfaces beyond the simpler prose solution. | AUTHOR_REPORTED; E21 |
| R30 / is time interval Of / has time interval | Figure5.5 interval interface pair. | AUTHOR_REPORTED; E21 |
| R31 / is about / is reference of | Information Realisation diagram interfaces; not separately axiomatized by5.3.10 prose. | AUTHOR_REPORTED; E21 |
| R32 / rdfs:subClassOf / defines / classifies / isSettingFor / satisfies | Five distinct Figure5.2 edge types; classification is not subclassing. | AUTHOR_REPORTED; E05 |

## Requirements, examples and adverse cases

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| S-5.3.1 / Events and participation | Person participates in a meeting. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E06 |
| S-5.3.2 / Quality of entities | Two distinct colors can have equal values. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E07 |
| S-5.3.3 / Region | Color or distance space. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E07 |
| S-5.3.3.1 / Time Interval | Shared vacation week. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E07 |
| S-5.3.4 / Entity Classification | Document topics with statistics. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E08 |
| S-5.3.4.1 / Role Classification | Project manager role with minimum fee. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E08 |
| S-5.3.4.2 / Parameter Classification | Very high building height. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E08 |
| S-5.3.4.3 / Task Classification | Buying ticket addresses work-trip organization. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E08 |
| S-5.3.5 / Collection and Membership | Historical works collection with unknown contents. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E09 |
| S-5.3.6 / Location | Area under a table. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E10 |
| S-5.3.7 / Part-whole | Engine, piston and car. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E10 |
| S-5.3.7.1 / Component | Piston is not inferred a direct car component. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E10 |
| S-5.3.8 / Constitution | Persons constitute a social system. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E11 |
| S-5.3.9 / Sequence | Coffee-choice action precedes preparation. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E11 |
| S-5.3.10 / Information Realisation | Composition and a recording. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E12 |
| S-5.3.11 / Description | Marriage law defines partner concepts. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E13 |
| S-5.3.11.1 / Plan | Coffee plan with tasks and drink goal. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E13 |
| S-5.3.12 / Situation | Actions in one plan execution. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E14 |
| S-5.3.13 / Time-indexed participation | Suspect at party from9pm to11pm. Reviewer use: test the stated pattern distinction and retain its local commitment boundary. | REVIEWER_INTERPRETATION; E14 |
| S20 / Unnamed member witness | Adverse: an OWL existential can be satisfied by an unnamed member. Lack of a known member does not by itself justify omitting non-emptiness; separate empty, unknown and historical collections. | REVIEWER_INTERPRETATION; E09 |
| S21 / Direct part versus part | Adverse: piston/engine/car can support broad parthood without proving a direct car component relation; no anti-transitivity follows. | REVIEWER_INTERPRETATION; E10 |
| S22 / Same word, separate levels | Adverse: Person as a class and Person as legal concept/role require distinct interpretations; punning alone is not a semantic bridge. | REVIEWER_INTERPRETATION; E04 |
| S23 / Contextual participation | Adverse: unqualified person/event participation cannot answer a bounded-time question without an explicit reified context/interval or declared shortcut. | REVIEWER_INTERPRETATION; E06, E14 |
| S24 / Local classification versus module grounding | Adverse: adopting only Information Realisation does not automatically commit to the entire DUL Object/Event split. | REVIEWER_INTERPRETATION; E02, E12 |
| S25 / Raw source transport | Adverse: HTTP200 at the literal case-variant OWL link can be an HTML page; filename and status alone do not establish an ontology input. | REVIEWER_INTERPRETATION; E19, E23 |

## Critical findings

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| F01 / Foundational and pattern commitments differ | A focused ODP carries its own commitments, while integrating it into DUL can add disjointness and classification assumptions. | REVIEWER_INTERPRETATION; E02, E16 |
| F02 / Reuse is not synonymous with import | Locally implementing a pattern and importing an existing realization are distinct valid strategies in this account. | REVIEWER_INTERPRETATION; E02, E15 |
| F03 / Pattern-shaped design can be monolithic | File/namespace layout is not proof for or against ODP reuse; compare conceptual intent and explicit composing axioms. | REVIEWER_INTERPRETATION; E16 |
| F04 / DUL is more than a terminology change | Five theories are integrated and commitments simplified; full S5/modal/temporal faithfulness is not established by friendly labels. | REVIEWER_INTERPRETATION; E03, E05, E19 |
| F05 / First-order conceptualizations already modeled | Description, Concept and Situation are explicit first-order entities; a later novelty claim cannot rely only on reifying a conceptualization. | REVIEWER_INTERPRETATION; E04, E13, E14 |
| F06 / Punning is not intended interpretation | OWL2 punning supplies separate interpretations but no automatic class/concept/role equivalence. | REVIEWER_INTERPRETATION; E04 |
| F07 / Quality is not value | Distinct quality bearers may share qualia; collapsing all into one data value loses individuated dependence information. | REVIEWER_INTERPRETATION; E03, E07 |
| F08 / Figure5.1 prose mismatch | The diagram places Abstract self-parthood in its temporal row, while prose assigns abstracts atemporal parthood; do not silently fix either source. | REVIEWER_INTERPRETATION; E03, E20 |
| F09 / No named member versus no member | The collection rationale needs an OWA qualification: unobserved/unnamed witnesses differ from an actually empty collection. | REVIEWER_INTERPRETATION; E09 |
| F10 / Non-transitive is not intransitive | The Component example blocks a licensed inference, not necessarily every possible direct shortcut fact. | REVIEWER_INTERPRETATION; E10 |
| F11 / Constitution not a parthood alias | Different granularity/identity layers have distinct persistence commitments; layer changes should not be compiled as hasPart without analysis. | REVIEWER_INTERPRETATION; E03, E11 |
| F12 / Sequence restrictions are partial | Transitivity and symmetric overlap do not by themselves deliver strict order, acyclicity or full temporal interval reasoning. | REVIEWER_INTERPRETATION; E11 |
| F13 / Time interval date semantics are underdetermined | Multiple date values can have different roles/formats; the sketch does not identify a full ordered begin/end contract. | REVIEWER_INTERPRETATION; E07 |
| F14 / TIP is an external illustration | The nineteen subsection patterns include one explicitly not extracted from DUL; treating all nineteen as native DUL modules misreports provenance. | REVIEWER_INTERPRETATION; E14 |
| F15 / Object/datatype shortcuts have costs | Parameter and at-time alternatives bypass intermediate individuals; identity, provenance and join behavior need independent assessment. | REVIEWER_INTERPRETATION; E08, E14 |
| F16 / Time-indexed naming is not silently corrected | The TIP prose mentions Time Indexed Situation and Time Indexed Participation; current sample imports a parent module. This is a correspondence question, not a proven printed typo. | REVIEWER_INTERPRETATION; E14, E25 |
| F17 / Description disjointness is version-bound | The chapter and current standalone Description pattern state Concept/Description disjointness; retained integrated DUL4.2 reports its removal. Neither source substitutes for the other. | REVIEWER_INTERPRETATION; E13, E23, E24 |
| F18 / Absence of one triple is not non-entailment | Selected current-root disjointWith triples are absent; no reasoner or non-entailment proof was run. | REVIEWER_INTERPRETATION; E23 |
| F19 / Diagrams are not axiom/import graphs | UML component interfaces document intent and availability, not exact class/property declarations, import closure or a successfully executed refactor. | REVIEWER_INTERPRETATION; E15, E16, E21, E22 |
| F20 / Design-time interface can be aspirational | The chapter allows planned requirements before an implementing module is identified; distinguish design and implementation snapshots. | REVIEWER_INTERPRETATION; E15 |
| F21 / Extra composition constraints matter | Core-category disjointness and Concept-only parts are introduced when combining patterns; keyword reuse alone misses those constraints. | REVIEWER_INTERPRETATION; E16 |
| F22 / Broad social-object wording needs scope | Assigning every class in every added pattern to Social Object would need reconciliation with physical Information Realisation and Event/Region targets. Treat the prose generalization as a typed-scope question. | REVIEWER_INTERPRETATION; E16, E19 |
| F23 / Names vary inside the chapter | preceeds/precedes, parameter classification/parametrization, and constituent/constitutent spellings must not silently become exact IRI equivalences. | REVIEWER_INTERPRETATION; E08, E11, E21 |
| F24 / Diagram contains additional interfaces | is about/is reference of and directly precedes/follows appear in Figure5.5 beyond some isolated prose solutions; no complete source axiom set follows. | REVIEWER_INTERPRETATION; E21 |
| F25 / Case-sensitive source link can yield HTML | The literal note1 path serves HTML; the canonical retained root path serves matching DUL4.2 bytes. The note4 misspelled host was not followed. | REVIEWER_INTERPRETATION; E19, E23 |
| F26 / Reuse list is not new effectiveness evidence | Section5.5 cites applications without a common benchmark, participant sample or measured quality/superiority result in this chapter. | REVIEWER_INTERPRETATION; E17 |
| F27 / Related DOLCE repo is not exact DUL source | Official current DOLCE GitHub tree is found and pinned as related foundational evidence, but it does not establish the original2016 DUL distribution. | REVIEWER_INTERPRETATION; E05, E23 |
| F28 / No model adoption yet | The source supports candidate terminology and scenario distinctions, not an accepted change to Clariceptify or final gap conclusion. | REVIEWER_INTERPRETATION; E02, E04, E16 |

## Unresolved questions

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Q01 / Exact root and all-class glossary | Complete definitions and constraints for all78 local classes in retained4.2, separate external redeclaration/imported/reference populations, and establish what historical2016 version can actually be pinned. | REVIEWER_INTERPRETATION; E05, E23 |
| Q02 / Disjointness/version correspondence | Check chapter Description/Concept and Information Realisation assertions against exact root and standalone-pattern versions; preserve4.1/4.2 evolution and distinguish missing triples from non-entailment. | REVIEWER_INTERPRETATION; E12, E13, E23, E24 |
| Q03 / Time and matrix typing | Resolve Figure5.1 versus prose Abstract parthood; map original n-ary/time-indexed relations to the simplified binary and Situation patterns without claiming semantic preservation. | REVIEWER_INTERPRETATION; E03, E14, E20 |
| Q04 / Composition and social-object scope | Test one selected social/physical typing case, Concept-only parthood and Plan-goal component restriction against the exact selected module. | REVIEWER_INTERPRETATION; E13, E16, E19 |
| Q05 / OWL existential and OWA | Build a bounded unnamed-member example and distinguish unknown, empty and required-witness collections; inspect bidirectional participation/realization existence. | REVIEWER_INTERPRETATION; E06, E09, E12 |
| Q06 / Selected relation profiles | Test non-transitive versus intransitive Component, parthood transitivity and sequence overlap restrictions with one positive/adverse fixture. | REVIEWER_INTERPRETATION; E10, E11 |
| Q07 / TIP sample imports and name mappings | Pin the actual required parent files, class/property names and interval/datatype alternative; do not read the illustrated TIP as a native integrated DUL module. | REVIEWER_INTERPRETATION; E14, E25 |
| Q08 / Source, interfaces and licenses | Reconcile literal/canonical URLs, all selected artifact versions/imports, source licenses and diagram-only interfaces. Complete no more than the existing eight deep semantic questions; follow-up imported IOLite definitions stay #271. | REVIEWER_INTERPRETATION; E19, E21, E23, E24, E25 |

## Inputs for later synthesis

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Y01 / Conceptualization prior overlap | Candidate comparison input: Description/Concept/Situation and role/task/parameter classification already provide significant conceptualization/context support. | REVIEWER_INTERPRETATION; E04, E08, E13, E14 |
| Y02 / Selective pattern reuse | Candidate design option: assess a focused pattern independently of whole-DUL grounding; record any additional integration commitments. | REVIEWER_INTERPRETATION; E02, E16 |
| Y03 / Source-grounded scenario bank | Candidate future tests: quality/value, collection/member, plan/execution, binary/time-indexed participation and information/realization. | REVIEWER_INTERPRETATION; E03, E08, E09, E12, E14 |
| Y04 / Method/documentation distinction | Candidate method comparison: intent, design interfaces and implementation interfaces should be traceable without assuming file-level modularity. | REVIEWER_INTERPRETATION; E15, E16 |
| Y05 / Limits carried forward | Carry all eight #88 questions, current-vs-historical differences and reuse-evidence limits into #251/#126 after the remaining paper queue. | REVIEWER_INTERPRETATION; E17, E20, E23, E24, E25 |

## Evaluation evidence

- **Verification:** The chapter sketches axioms and illustrations; the reviewer checked exact source/page identity and selected current RDF statements. No inference, satisfiability or proof run is claimed. [REVIEWER_INTERPRETATION; E01, E16, E23, E24, E25]
- **Validation:** Modeling issues and worked examples are conceptual plausibility evidence; no independent expert/participant study is reported here. [REVIEWER_INTERPRETATION; E06, E08, E09, E14]
- **Evaluation:** Section5.5 is a non-exhaustive application list, not a new common-metric assessment of pattern effectiveness. [REVIEWER_INTERPRETATION; E17]
- **Assessment:** Review separates useful reification/modularity distinctions from version differences, source inconsistencies and OWA/profile questions. No superiority judgment about Clariceptify follows. [REVIEWER_INTERPRETATION; E02, E09, E16, E20, E23]
- **Assurance:** Exact book digest, chapter scope, complete reading declarations and separate current-source receipts support provenance only; all-class/import/semantic acceptance stays open. [REVIEWER_INTERPRETATION; E01, E19, E23, E24, E25]

## Artifact and repository boundary

Technical follow-up: #88. State: `PAPER_COMPLETE_CURRENT_ROOT_AND_TWO_SAMPLES_BOUNDED_INSPECTION_FULL_TECHNICAL_WORK_OPEN`.

2016 chapter has no pinned DUL version number. Retained integrated root4.2, live standalone Description1.1 and TIP sample annotations are separate sources. Root4.2 reports relaxed disjointness; standalone Description retains its disjoint pair. No exact historical parity, complete imported glossary, reasoner or all-pattern equivalence is established. #88 retains eight bounded questions and all78 local manual definitions; IOLite #271 remains separate.

## Evidence index

| ID | Exact source locator | Source-grounded summary |
|---|---|---|
| E01 | Chapter5, printed81 and100-103; institutional DOI metadata | Presutti/Gangemi 2016 chapter, printed81-103 in the supplied389-page book;39 references, distinct chapter-scoped input. |
| E02 | 5.1, printed81-82 | Extracted ODPs have their own limited commitments; pattern use differs from importing a particular implementation; UML documentation proposed. |
| E03 | 5.2/5.2.1.1-5.2.1.4, printed82-85 | Original DOLCE S5 account, four top categories, quality/quale distinctions, typed/time-indexed relations and Figure5.1. |
| E04 | 5.2.2 and Figure5.1, printed84-85 | D&S reifies intensional/extensional relations and classes; OWL2 punning alone does not specify its intended modeling use. |
| E05 | 5.2.3-5.2.6 and Figure5.2, printed85-87 | Five source theories: DOLCE, D&S, Plan, Information Object and Collection; DUL is a lighter integrating OWL design rather than a semantics-preserving renaming. |
| E06 | 5.3/5.3.1, printed87 | Object/Event disjointness, inverse participation and mutual existential commitments stated in prose. |
| E07 | 5.3.2/5.3.3/5.3.3.1, printed88 | Quality/quality-space relations, region data values and time-interval specialization; no sample URL printed for the Quality pattern. |
| E08 | 5.3.4 and5.3.4.1-5.3.4.3, printed89-90 | Concept, Role, Parameter and Task as first-order classification entities; parameter datatype alternative and task-label variants. |
| E09 | 5.3.5, printed90 | Collection membership differs from instantiation; unknown historical members motivate omitting a required-member axiom in the described pattern. |
| E10 | 5.3.6/5.3.7/5.3.7.1, printed91 | Place, transitive part-whole, and direct component relation; inability to infer a shortcut is not a declaration of intransitivity. |
| E11 | 5.3.8/5.3.9, printed91-92 | Constitution is layered and distinct from parthood; sequence transitivity and symmetric overlap are described; spellings differ across prose and diagram. |
| E12 | 5.3.10, printed92 | Information Object/Realisation disjointness, inverse realization and mutual existentials; separate realizations can embody one information object. |
| E13 | 5.3.11/5.3.11.1, printed92-93 | Description/Concept disjointness and defines inverse; Plan uses concept classifications, direct components and at least one Goal. |
| E14 | 5.3.12/5.3.13, printed93-94 | Situation setting for n-ary context; Time-indexed participation is explicitly NOT extracted from DUL and includes a datatype shortcut alternative. |
| E15 | 5.4, Figures5.3/5.4, printed94-96 | OM/ODP component stereotypes, inherited module status and intent tag; design-time interfaces can be planned and differ from implemented vocabulary. |
| E16 | 5.4.1/5.4.2, Figures5.5/5.6, printed95-99 | Composition can introduce additional commitments; DUL monolithic file can still reflect pattern design; sixteen displayed components and alternative D&S module packaging. |
| E17 | 5.5, printed97/99 | Non-exhaustive cited reuse across learning, hydro, multimedia, legal, medical, engineering and other domains; not a new controlled evaluation. |
| E18 | 5.6, printed99-100 | Chapter concludes with independent pattern solutions and hypothetical recomposition of DUL, not an executable refactoring result. |
| E19 | Numbered notes1-9, printed81/86/89/97/99 | Literal source URLs, misspelled note4 host, temporal/possible-world omission note6, author OWL-Time compatibility claim and social-object distinction note8. |
| E20 | Figure5.1 and5.2.1.4, printed84-85 | Matrix places Abstract(Region) under Temporal parthood while preceding prose assigns abstracts atemporal parthood; both literal readings retained, no silent repair. |
| E21 | Figure5.5, printed98, landscape diagram | All sixteen component labels and their displayed interfaces catalogued; includes is about/is reference of, direct sequence and parameterization interfaces beyond some prose descriptions. |
| E22 | Figure5.6, printed99 | Three inner patterns and enclosing Description-and-Situation module expose an alternative interface packaging; this is a component diagram, not an OWL import proof. |
| E23 | Pinned DUL4.2 root; version header and selected explicit disjoint triples | Current root header reports relaxed disjointness; direct triple absence is not non-entailment. No2016 version parity established. |
| E24 | Sample description.owl; selected asserted Concept disjointWith Description triple | Current standalone Description sample retains the disjoint pair, unlike the retained integrated root; original2016 byte identity unverified. |
| E25 | Sample timeindexedparticipation.owl; header/imports and selected domains | Live sample imports participation and timeindexedsituation; prose names must not be silently treated as exact current IRIs. |

## Closure boundary

Exact selected chapter critical review complete. Paper closure does not close #88 all-class/definition/version/import/profile/semantic work, #271 imported definitions, #251 comparison or #126 synthesis. All eight technical questions carry forward; no Clariceptify ontology, requirement, fixture, manuscript or release change, adopted mapping, independent expert acceptance or reproduced author evaluation.
