# cDnS1.1: core profile and eight correspondence checks

Issue #267 | BOUNDED_CORE_FOLLOWUP_COMPLETE_WITH_PROFILE_FAILURE | 2026-10-29

The unchanged selected core has 12 named classes, 47 object properties, 411 RDF triples, 14 anonymous restrictions and no declared imports. Its header refers to JAAMAS2008; exact 2007/2008 release fidelity remains unestablished. Existing complete selected-class catalogues are reused, not replaced.

| Actual operation | Recorded outcome |
|---|---|
| Exact input and retained census reconciliation | PASS |
| OWLAPI OWL2 DL profile | FAIL: one non-simple-property minimum-cardinality violation |
| HermiT construction on unchanged full core | Refused for hasProperPart cardinality |
| Logical consistency / unsatisfiable classes | NOT_ESTABLISHED / null |
| Asserted RDF queries | 8/8 expected ASK results; source-structure checks only |
| Whole-core positive/adverse consistency scenarios | Not executed after reasoner refusal |
| Source repair or approximate surrogate | Not performed |

[Structured review](cDnS-core-followup.yaml) | [Actual execution receipt](../../../evaluation/related-work/cdns267/execution.json) | [Existing complete core glossary](../deep-reviews/cDnS2007/classes.md) | [Separately mapped extension glossary](../deep-reviews/cDnS-journal-2008/classes.md)

## Profile finding and safe execution boundary

Bundle requires at least two hasProperPart fillers while hasProperPart is declared transitive. OWLAPI reports this as a non-simple property in ObjectMinCardinality; HermiT raises IllegalArgumentException for the same restriction. Tool refusal is not an inconsistency proof. The source was not stripped, cardinality was not weakened and transitivity was not removed.

Exact original core can be loaded and profiled, but HermiT refuses its non-simple-property cardinality. Whole-core consistency scenarios remain unexecuted. Eight asserted RDF queries ran; they are not semantic validity tests. No repaired surrogate or selective source-axiom deletion is authorized by this task.

## Eight selected comparisons

### Q01: Concept definition uniqueness

CORE_STRENGTHENS_DISPLAYED_EXISTENCE. Concept has some Description and exactly one isDefinedIn filler. Both papers display 18 supplies existence without stating uniqueness in that display. This is a local commitment comparison, not a proof that the entire paper permits multiple definitions. Different names do not entail different individuals.

Locators: Concept / isDefinedIn cardinality1; cDnS2007 K018 p12; journal K018 PDF15 / printed84.

Positive scenario: A Concept has one defining Description.

Adverse scenario: Two explicitly distinct defining Descriptions violate the selected cardinality; two names alone can denote the same Description.

Scenario execution: NOT_EXECUTED_FULL_CORE_REASONER_REFUSED. The corresponding asserted source query is recorded separately.

### Q02: Conceptualization range

ALIGNED_WITH_2008_RANGE_NOT_A_NEW_2008_DIFFERENCE. conceptualizes ranges over SchematicEntity and has SocialAgent domain. The journal already generalizes the range in display37, unlike the earlier Description-oriented shares(a,d,t) display38 vocabulary. Do not report the broader range as a novel core-versus-2008 discrepancy or equate the differently named relations automatically.

Locators: conceptualizes domain/range; 2007 K038 PDF15; journal K037 PDF17 / printed86.

Positive scenario: A social agent conceptually targets a Concept as a schematic entity.

Adverse scenario: Treating the core range as Description-only adds an unsupported restriction; cross-version identity also needs separate evidence.

Scenario execution: NOT_EXECUTED_FULL_CORE_REASONER_REFUSED. The corresponding asserted source query is recorded separately.

### Q03: Expression and aboutness

ALIGNED_2008_RANGE_DERIVATION_NOT_REPRODUCED. expresses ranges over SchematicEntity, matching journal46 rather than the earlier expresses(i,d,t) signature47. The binary property declaration and range do not reproduce journal49 aboutness derivation through a satisfying situation, description and referent. No property-chain axiom is present in this root.

Locators: expresses and its declared inverse/range; 2007 K047 PDF16; journal K046/K049 PDF19 / printed88.

Positive scenario: An information object expresses a schematic entity.

Adverse scenario: A broad expression range alone does not establish a specific referent or an asserted aboutness chain with the required shared witnesses.

Scenario execution: NOT_EXECUTED_FULL_CORE_REASONER_REFUSED. The corresponding asserted source query is recorded separately.

### Q04: Temporal projection

BINARY_CORE_DOES_NOT_PRESERVE_EXPLICIT_TIME_ARGUMENT. All 47 declared properties are object properties; this root declares no Time class or datatype property and imports nothing. Time-indexed paper signatures are represented by binary core vocabulary without an explicit temporal argument. This does not establish that no temporal extension exists elsewhere or prove a lossless projection.

Locators: Core object-property inventory; 2007 K038/K047; journal K037/K046 and K114 temporal order.

Positive scenario: Retain an atemporal social-agent/content link when that is the declared intended scope.

Adverse scenario: Two time-qualified claims cannot be distinguished by assigning only the same binary pair; no preservation of ordering or changing context is established.

Scenario execution: NOT_EXECUTED_FULL_CORE_REASONER_REFUSED. The corresponding asserted source query is recorded separately.

### Q05: Core and normative extension boundary

MODULAR_SCOPE_NOT_PAPER_ABSENCE. Plan, Norm and KnowledgeCommunity are not declared in this 12-class standalone core. They are present in the separately pinned collInt1.0 catalogue mapped through ground1.0 to core1.1. The 25/14/12 class map is separately inventoried and is not imported or reasoned over in this task. Original-host/edition compatibility remains unverified.

Locators: Core imports=[] and declarations; journal K068/K114/K128; selected journal classes.yaml collInt:Plan/Norm/KnowledgeCommunity.

Positive scenario: Use the core for its declared contextual-classification scope and consult the separate extension when relevant.

Adverse scenario: Absence from the core is not absence from either paper or project; the selected mapped extension is not a certified historical complete theory.

Scenario execution: NOT_EXECUTED_FULL_CORE_REASONER_REFUSED. The corresponding asserted source query is recorded separately.

### Q06: Schematic union coverage

EXPLICIT_COVER_AXIOM_NOT_MATCHED. The six principal schematic categories are subclasses of SchematicEntity with disjointness, but SchematicEntity has no equivalentClass union in the complete source census. Entity instead has a SchematicEntity/NonSchematicEntity union. Those are distinct statements. Subclass/disjointness assertions alone do not supply the paper display5 cover; global entailment remains unexecuted.

Locators: SchematicEntity and Entity axioms; 2007 K005 PDF10; journal K005 PDF12 / printed81; journal K077 PDF24 / printed93.

Positive scenario: Classify an individual under a named schematic category when evidence supports it.

Adverse scenario: Do not read Entity union or pairwise disjointness as the six-way SchematicEntity covering axiom.

Scenario execution: NOT_EXECUTED_FULL_CORE_REASONER_REFUSED. The corresponding asserted source query is recorded separately.

### Q07: Configuration conditions

ONLY_SUBCLASS_AXIOM_LOCALLY_INHERITS_COLLECTION. Configuration has only Collection as its explicit superclass and no equivalentClass definition. It inherits Collection coverage/unification restrictions, but the root does not assert the Configuration-specific member/part conditions described by paper64. The paper temporal-binder issue remains literal source evidence, not a repaired formula.

Locators: Configuration subclass Collection; Collection restrictions; 2007 K064 PDF18; journal K064 PDF21 / printed90.

Positive scenario: A Configuration remains subject to the inherited Collection restrictions.

Adverse scenario: Do not infer the detailed part/member pattern from its name or silently normalize the shadowed temporal binder.

Scenario execution: NOT_EXECUTED_FULL_CORE_REASONER_REFUSED. The corresponding asserted source query is recorded separately.

### Q08: Bundle and transitive-property cardinality

EXECUTED_PROFILE_FAILURE_REASONER_REFUSAL. Bundle has an unqualified minimum cardinality2 on transitive hasProperPart, plus some Description proper part. OWLAPI reports one non-simple-property cardinality violation; HermiT refuses construction for that restriction. No whole-core consistency value or unsatisfiable-class list is obtained. Paper65 does not explicitly distinguish its two variables in the formula despite the prose minimum; neither that formula nor all its context is certified by this execution.

Locators: Bundle / hasProperPart / minCardinality2; 2007 K065 PDF18; journal K065 PDF22 / printed91; execution.json profile/refusal.

Positive scenario: Record the source as it is and retain the profile failure as an inspection result.

Adverse scenario: Do not remove transitivity, weaken cardinality or delete the Bundle axiom to manufacture a passing consistency result.

Scenario execution: NOT_EXECUTED_FULL_CORE_REASONER_REFUSED. The corresponding asserted source query is recorded separately.

## Findings and later use

| Finding | Source question | Utilization categories |
|---|---|---|
| CDNS267-F01: Concept definition uniqueness | Q01 | U03, U04, U10 |
| CDNS267-F02: Conceptualization range | Q02 | U03, U04, U08 |
| CDNS267-F03: Expression and aboutness | Q03 | U03, U04, U09 |
| CDNS267-F04: Temporal projection | Q04 | U04, U06, U10 |
| CDNS267-F05: Core and normative extension boundary | Q05 | U01, U02, U08 |
| CDNS267-F06: Schematic union coverage | Q06 | U03, U04, U10 |
| CDNS267-F07: Configuration conditions | Q07 | U03, U04, U07 |
| CDNS267-F08: Bundle and transitive-property cardinality | Q08 | U04, U07, U10 |

Apply the [maintained U01-U13 plan](../../../docs/research/review-utilization-plan.md). These comparisons feed #251 and #126; no model adequacy or accepted equivalence is inferred.

- Q01 -> CLR-C0017: Assess definition identity and multiplicity requirements before borrowing exactly-one constraints. Status: OWNER_DECISION_REQUIRED.
- Q02 -> CLR-C0004, CLR-C0026, CLR-C0101: Compare agent, conceptualization process and schematic content without assuming equivalence. Status: OWNER_DECISION_REQUIRED.
- Q03 -> CLR-C0057, CLR-C0101, CLR-C0017: Preserve the difference between expression, represented content and evidence for a referent. Status: OWNER_DECISION_REQUIRED.
- Q04 -> CLR-C0123, CLR-C0026: Test whether temporal/context identity survives the intended formal projection. Status: OWNER_DECISION_REQUIRED.

## Reproduce and interpret

Obtain cDnS.owl with the recorded SHA256 outside the repository. Install requirements-bdi-review.txt for the pinned RDFLib/JPype/HermiT dependencies.

```bash
python tools/inspect_cdns267.py --source /external/cDnS.owl --output /external/execution.json
python tools/check_cdns267.py --source /external/cDnS.owl
```

The selected root imports nothing. The separately mapped collInt/ground/core catalogue is contextual evidence, not a loaded or reasoned extension in this followup. Original-host compatibility and the full 141/147-display theories remain outside this execution. No full source text, raw ontology, source repair, independent expert approval, Clariceptify model/requirements/fixtures/manuscript change or release is introduced.
