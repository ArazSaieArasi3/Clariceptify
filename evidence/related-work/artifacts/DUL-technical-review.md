# DUL4.2 technical review
#88. Research evidence only; no Clariceptify model or manuscript change.

## Inputs and results

Current root: DUL4.2, SHA256 `e5f6429596d2c7014730bad85aaaa9c39530235f27f596cd0e7ce85e6bbcba66`. The existing 2016 chapter review is used with its page/section locators; exact historical implementation identity remains unestablished.

- 78 local classes accounted for; 67 usable descriptive paraphrases, two label-only comments and nine missing comments.
- 29 isolated HermiT tests against the full retained root; see the executable receipt for actual outcomes.
- Nine chapter-pattern roots, 21 distinct files in their asserted closures, no unresolved imports.

## Eight bounded questions

### Q01: Complete root census and version boundary

All 78 local named classes, one owl:Thing redeclaration, anonymous expressions and asserted constraints are accounted for. There are 69 comment-candidate classes: 67 usable descriptive paraphrases, two label-only comments, and nine classes without comments. No definitions were invented. Root has no imports. Current TimeIndexedRelation and Parthood carry 2021 dates, so this exact graph is not established as the 2016 chapter implementation. HermiT baseline is consistent and reports no unsatisfiable classes; no inferred population or independent OWL2 profile certification is claimed.

Chapter evidence: E05, E23.

### Q02: Disjointness and source-version correspondence

Whole-root co-instance tests are consistent for Description/Concept, InformationObject/Description and InformationObject/Concept, providing bounded non-disjointness countermodels beyond mere missing-triple inspection. InformationObject plus InformationRealization is inconsistent. The separately pinned Description pattern explicitly asserts Concept/Description disjointness. The standalone InformationRealization sample contains mutual existence restrictions; root 4.2 requires a realization to realize an InformationObject but does not require every InformationObject to have a realization. Do not transfer one module/version result to another.

Chapter evidence: E12, E13, E23, E24.

### Q03: Temporal parthood and chapter discrepancy

The reviewed Figure 5.1/prose discrepancy is retained: diagram temporal row versus prose atemporal Abstract parthood. This review cannot determine the authors intended correction. Current root adds TimeIndexedRelation (Situation with a TimeInterval setting) and Parthood with part/whole witnesses. Its inverse-includesWhole/includesPart chain entails binary hasPart. A counterexample test confirms that two named Parthood records with shared part and whole cannot be forced different even when distinct time nodes are supplied: the declared key includes part and whole, not time. The matched control allows the records to coincide while keeping time witnesses explicitly different and is consistent. Temporal contextual identity and semantic preservation therefore remain qualified.

Chapter evidence: E03, E14, E20.

### Q04: Typed composition and Plan goal

SocialObject/PhysicalObject co-instantiation is inconsistent in the root. A Concept with a PhysicalObject part is inconsistent because its parts must be Concepts, which are SocialObjects. Plan with no components is inconsistent; Plan without a named Goal remains consistent because an existential Goal component can be unnamed. These tests do not endorse the chapter generalization that all pattern classes are social objects; physical information realizations retain their separate typing.

Chapter evidence: E13, E16, E19.

### Q05: Unknown, empty and existential witnesses

Unknown-members, explicitly empty-members and existential unnamed-member Collection fixtures are each consistent; combining empty membership and an existential membership is inconsistent. Root Object requires Event participation, Event requires an Object participant, and InformationRealization requires an InformationObject; denying each witness is inconsistent. Denying all realizations for an InformationObject is consistent in this root. No named witness is manufactured and closed-world absence is not substituted for emptiness.

Chapter evidence: E06, E09, E12.

### Q06: Relation profiles with adverse fixtures

Component chains permit both an asserted shortcut and an explicitly denied shortcut, so the root imposes neither transitivity nor intransitivity for hasComponent. Reverse component edges contradict asymmetry. Denying the shortcut of hasPart or precedes chains is inconsistent; precedence cycles remain consistent. Overlap symmetry is enforced, while overlap transitivity and direct-precedence transitivity are not entailed in the tested chains. These are exact-input logical observations, not a general claim that all applications tolerate those patterns.

Chapter evidence: E10, E11.

### Q07: TIP modules, names and date alternatives

Pinned TimeIndexedParticipation closure contains six documents with seven unique named declared classes including owl:Thing, no unresolved import. TIP directly imports Participation and TimeIndexedSituation; the latter imports Situation, TimeInterval and the annotation schema. TimeIndexedParticipation is a subclass of TimeIndexedSituation with at least one object, event and atTime value and minimum three forEntity values. atTime is an object property targeting TimeInterval. TimeInterval defines datatype start/end/date properties with at-most-one start/end, but no start-before-end comparison. The chapter datatype-shortcut alternative is not declared as a direct TIP atTime datatype property in these files. TIP remains an external illustration, not a native DUL root import.

Chapter evidence: E14, E25.

### Q08: Selected sources, interfaces and licenses

Nine chapter pattern roots and their complete asserted import closure are pinned:21 distinct parseable files. The DUL root and two previously inspected samples retain matching digests. Header license/right annotations are absent in inspected module headers; that observation grants no redistribution permission. isAbout/isReferenceOf and direct sequence interfaces exist in current DUL, but conceptual component diagrams are not exact release or import graphs. Shared IOLite definitions remain #271. Fresh bounded searches and the 2016 W3C namespace/governance record support continuity of the namespace, not exact historical bytes or a source license.

Chapter evidence: E19, E21, E23, E24, E25.

## Findings retained for comparison

- **DUL88-F01**: Nine lack comment annotations; Norm and SocialRelation merely repeat labels. Preserve absent/insufficient distinction in synthesis. Tracked in #251.
- **DUL88-F02**: A stable namespace and present4.2 source do not establish a 2016 byte-level release. Dates on current added terms demonstrate later content. Tracked in #251.
- **DUL88-F03**: Use module-specific constraints. Root and standalone patterns must not be treated as semantically interchangeable. Tracked in #251.
- **DUL88-F04**: Figure 5.1/prose conflict is preserved, not silently repaired or assigned author intent. Tracked in #251.
- **DUL88-F05**: Shared part and whole can identify records even with different time nodes. Preserve this concern in contextual identity comparison; no source/model change is made. Tracked in #251.
- **DUL88-F06**: Transitive precedes permits cycles; non-transitive component is not intransitive. Downstream requirements must state desired behavior separately. Tracked in #251.
- **DUL88-F07**: At-most-one endpoints and date ranges do not implement chronological interval comparison. TIP is not an imported DUL root module. Tracked in #251.
- **DUL88-F08**: No third-party raw source files are republished or relicensed; private bytes are used for reproducible inspection. Tracked in #126.

## Evidence

[Full class glossary](../dul-class-catalog.md), [technical record](DUL-technical-review.yaml), [reasoner cases](../../../evaluation/related-work/dul/semantic-cases.json), [module closure](../../../evaluation/related-work/dul/module-closure.json).

The original third-party files and logs remain private. Comments are not logical definitions. Successful consistency tests are not empirical validation, historical equivalence, independent review, source-license permission or model adoption. IOLite definitions remain #271; comparison #251 and synthesis #126 remain open.
