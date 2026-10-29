# IOLite 1.8: complete selected-module glossary

Issue #271. Reviewed 2026-10-29 against main `224f31e55cdb7ceebee510cbf4b746c5b53ff6a0`. This is source-bound catalogue completion, not a new ontology release or final scientific synthesis.

## Exact evidence and results

The [canonical formal file](http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl) was retrieved again; its SHA256 is `15f8ac177bc2b481e13f326cdccd0c9551f0721506adbac10ea694778a35f23f`, identical to the retained #90 input. The ontology header identifies version1.8 and explicitly imports DUL. The root is RDF/XML with666 explicit triples,46 local named OWL classes and20 external class redeclarations. It has no named rdfs:Class declarations or deprecated named classes; three anonymous class declarations and40 anonymous restrictions are counted separately. No nonbuiltin undeclared class-position IRIs were found under the documented position policy.

- [Complete class reader](classes.md) and [machine-readable glossary](classes.yaml): all46 local IRIs, labels, annotation hashes, attributed paraphrases, hierarchy, equivalence counts and complete constraint pointers.
- [Complete declaration/constraint census](IOLite-census.json):66 named declarations, including all20 external redeclarations. The source has31 local and17 external object-property declarations; these are not extra classes.
- [Reparsed source and import evidence](source-reconciliation.json): four exact source hashes, class-valued position populations and resolved assertion-based closure inventories.
- [154-IRI glossary reconciliation](closure-coverage.json): every selected LMM closure class points to its authoritative shared glossary, or the explicit builtin disposition.

All43 local classes having comment candidates were reviewed and given short paraphrases. DigitalPhoto, Gesture and WebPage have no source comment; their definitions remain null. No definition was reconstructed from a name or superclass. Descriptive comment acceptance means usable source description, not a sufficient logical definition. DataStructure and KOS use inclusive examples; ContractText has a minimal relational description. Seven comments carry WordNet attribution in the source; no dictionary edition or additional rights are inferred. Sound's prose describes information realization while its explicitly named superclass here is DUL Process; prose is not promoted to a formal equivalence or entailment. All46 rows retain complete source-constraint pointers independently of these descriptions.

## Shared foundation and consumers

The retained chain is LMM_L2 1.2 → LMM_L1 1.8 → IOLite1.8 → DUL4.2. Each edge is an actual owl:imports statement resolved only to pinned bytes. No network imports, unknown modules or inferred-class counts are silently added. DUL's shared [78-class glossary](../../../dul-class-catalog.md) and [bounded technical review](../../../artifacts/DUL-technical-review.md) remain authoritative; their definitions are not duplicated here.

The20 IOLite external redeclarations comprise19 DUL classes plus builtin owl:Thing. An external redeclaration does not add a new local IOLite concept and may carry extra outgoing constraints; those statements remain in the IOLite census rather than being attributed to the DUL source. The unique closure is125 IRIs at IOLite,133 at LMM_L1 and154 at LMM_L2. LMM_L2's154 are153 local source classes (78 DUL +46 IOLite +8 L1 +21 L2) and owl:Thing, deduplicated by IRI.

The153 source classes now have complete accounting:135 descriptive-comment/paraphrase records,16 absent comments (9 DUL +3 IOLite +4 LMM), and2 label-only DUL comments. This does **not** mean all153 classes have adequate definitions. The builtin has no fabricated source-definition obligation.

Consumers use this shared review rather than duplicating it:

- [LMM local glossary](../../LMM2008/classes.md), [paper review](../../LMM2008/report.md), and [source audit](../../source-audit.md).
- [Coverage guide](../../coverage-guide.md) distinguishes completed class accounting from remaining semantic and historical work.
- Older #90 selected inspection remains historically scoped; its parsing result is not rewritten as an inference result. LMM correspondence #274, comparison #252 and synthesis #126 stay open.
- The Emotions2015 legacy URL/import candidate remains a distinct, not-yet-established version under #239; a matching short name does not transfer this glossary's coverage to different bytes.

## Limits and acceptance boundary

No whole IOLite/LMM reasoner, profile, satisfiability, equivalence or alignment experiment was executed in #271. DUL #88's29 cases apply only to their recorded DUL inputs and do not transfer through imports. The retained1.8/4.2 bytes are not established as the exact historical2008 LMM distribution. The grounding evidence is DUL/DOLCE reuse through actual imports, not UFO/BFO grounding inferred from citations.

No license/right annotation was found in the selected ontology header; public availability is not redistribution permission. Raw sources and the full third-party annotation corpus remain outside the repository. Published data contains short reviewer paraphrases, annotation hashes and formal observation records. Review is AI-assisted, not an independent expert endorsement.

Clariceptify model, requirements, fixtures, manuscript and releases remain unchanged. Scientific adoption requires the owner's later decision.

## Reproduction

Use the exact four files listed in `evidence/related-work/corpus/lmm-inputs.yaml` in a private input directory. `python tools/check_iolite_catalog.py` validates recorded public evidence without research dependencies. With research dependencies installed, `python tools/check_iolite_catalog.py --source-dir INPUT_DIRECTORY` additionally checks all four source digests before parsing, regenerates population/import evidence and compares the IOLite full census. `python tools/test_iolite_catalog.py` exercises adverse cases. No command downloads a source, follows an unpinned import or runs a reasoner.
