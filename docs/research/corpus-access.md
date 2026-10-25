# Research source access, archive and next review packages

Date: 2026-10-25. Input: main 29cc41372e046da9791534019b23a899c105c3f5.

The [complete access inventory](../../evidence/related-work/corpus/access-inventory.yaml) covers all 19 original candidate labels, with additional versions and the distinct 2026 BDI work separate. Acquisition is not critical review. The owner-accessible archive contains 12 validated PDFs (185 pages), direct formal resources and five complete tracked-tree repository snapshots. All 62 ZIP members were read back; exact hashes and missing-access evidence are recorded. The [archive receipt](../../evidence/related-work/corpus/archive-record.json) publishes its identity without redistributing third-party bytes.

## Missing texts requested from the owner

These are all seven currently identified missing texts in this frozen inventory. A failed endpoint is not evidence that the work is unavailable everywhere. An unknown DOI is retained as unknown.

| Title | DOI | Authoritative record or explicit lookup |
| --- | --- | --- |
| Dolce+D&S Ultralite and its main Ontology Design Patterns | 10.3233/978-1-61499-676-7-81 | https://doi.org/10.3233/978-1-61499-676-7-81 |
| The Ontology for Conceptual Characterization of Ontologies | 10.1007/978-3-031-47262-6_6 | https://research.utwente.nl/en/publications/the-ontology-forconceptual-characterization-ofontologies/ |
| An Ontology of Representation | 10.1177/15705838251337943 | https://journals.sagepub.com/doi/10.1177/15705838251337943 |
| Managing Knowledge at the Information Level: an Ontological Approach | Not verified | https://scholar.google.com/scholar?q=Managing+Knowledge+at+the+Information+Level+Fortier+Kassel |
| Needs and Intentionality: An Ontological Analysis and an Application to Public Services | 10.3233/FAIA200666 | https://iris.unitn.it/handle/11572/336248 |
| Norms and plans as unification criteria for social collectives | 10.1007/s10458-008-9038-9 | https://link.springer.com/article/10.1007/s10458-008-9038-9 |
| Emotions Ontology for Collaborative Modelling and Learning of Emotional Responses | 10.1016/j.chb.2014.11.100 | https://doi.org/10.1016/j.chb.2014.11.100 |

O4OA institutional PDF returned HTTP 403, while its specification download returned an anti-bot HTML page. Neither is counted as acquired. EFO and Cognitive Atlas were recovered from alternative publisher endpoints; no upload from the owner is currently needed for those PDFs. CMO is acquired but its defective text layer requires later visual/OCR work. EmotionsOnto 2014 is acquired; the related 2015 article is separate.

## Completed LMM review package

[Paper review #72](../../evidence/related-work/reviews/LMM.yaml) binds the seven-page 2008 ACL text. [Artifact inspection #90](../../evidence/related-work/artifacts/LMM.yaml) pins LMM_L1 1.8 and LMM_L2 1.2, with the complete declared import chain through IOLite 1.8 and DUL 4.2. L1 has 8 local named owl:Class IRIs (133 in the asserted closure), while L2 has 21 (154 in the closure). Imported class redeclarations are separate; no reasoning is claimed. The paper supports substantial prior expression/meaning/reference overlap. The current files are not proven axiom-identical to their 2008 predecessors.

## Bounded extension tasks

The owner explicitly requested full reference-artifact access and medium-sized comparative work. The 194-unit original tracked plan is preserved; these 23 additional units are separately registered. Each artifact task addresses one module and at most eight commitments; comparison tasks address three or four candidates and four dimensions, with a shared scenario and adverse example. The original #126 synthesis remains distinct.

| Task | Issue | Deliverable |
| --- | --- | --- |
| R2-CORPUS-001 | [#234](https://github.com/ArazSaieArasi3/Clariceptify/issues/234) | evidence/related-work/corpus/access-inventory.yaml |
| R2-ART-DnS | [#235](https://github.com/ArazSaieArasi3/Clariceptify/issues/235) | evidence/related-work/artifacts/DnS.yaml |
| R2-ART-OntoKADS | [#236](https://github.com/ArazSaieArasi3/Clariceptify/issues/236) | evidence/related-work/artifacts/OntoKADS.yaml |
| R2-ART-OntoLex | [#237](https://github.com/ArazSaieArasi3/Clariceptify/issues/237) | evidence/related-work/artifacts/OntoLex.yaml |
| R2-ART-SKOS | [#238](https://github.com/ArazSaieArasi3/Clariceptify/issues/238) | evidence/related-work/artifacts/SKOS.yaml |
| R2-ART-EmotionsCognition | [#239](https://github.com/ArazSaieArasi3/Clariceptify/issues/239) | evidence/related-work/artifacts/EmotionsCognition.yaml |
| R2-ART-IAO | [#240](https://github.com/ArazSaieArasi3/Clariceptify/issues/240) | evidence/related-work/artifacts/IAO.yaml |
| R2-ART-CognitiveAtlas | [#241](https://github.com/ArazSaieArasi3/Clariceptify/issues/241) | evidence/related-work/artifacts/CognitiveAtlas.yaml |
| R2-ART-EFO | [#242](https://github.com/ArazSaieArasi3/Clariceptify/issues/242) | evidence/related-work/artifacts/EFO.yaml |
| R2-ART-COM | [#243](https://github.com/ArazSaieArasi3/Clariceptify/issues/243) | evidence/related-work/artifacts/COM.yaml |
| R2-ART-Representation | [#244](https://github.com/ArazSaieArasi3/Clariceptify/issues/244) | evidence/related-work/artifacts/Representation.yaml |
| R2-ART-CMO | [#245](https://github.com/ArazSaieArasi3/Clariceptify/issues/245) | evidence/related-work/artifacts/CMO.yaml |
| R2-ART-IDA | [#246](https://github.com/ArazSaieArasi3/Clariceptify/issues/246) | evidence/related-work/artifacts/IDA.yaml |
| R2-ART-BDI2020 | [#247](https://github.com/ArazSaieArasi3/Clariceptify/issues/247) | evidence/related-work/artifacts/BDI2020.yaml |
| R2-ART-DOLCEMental | [#248](https://github.com/ArazSaieArasi3/Clariceptify/issues/248) | evidence/related-work/artifacts/DOLCEMental.yaml |
| R2-LIT-BDI2026 | [#249](https://github.com/ArazSaieArasi3/Clariceptify/issues/249) | evidence/related-work/reviews/BDI2026.yaml |
| R2-ART-BDI2026 | [#250](https://github.com/ArazSaieArasi3/Clariceptify/issues/250) | evidence/related-work/artifacts/BDI2026.yaml |
| R2-CMP-001 | [#251](https://github.com/ArazSaieArasi3/Clariceptify/issues/251) | evidence/related-work/comparisons/batch-1.yaml |
| R2-CMP-002 | [#252](https://github.com/ArazSaieArasi3/Clariceptify/issues/252) | evidence/related-work/comparisons/batch-2.yaml |
| R2-CMP-003 | [#253](https://github.com/ArazSaieArasi3/Clariceptify/issues/253) | evidence/related-work/comparisons/batch-3.yaml |
| R2-CMP-004 | [#254](https://github.com/ArazSaieArasi3/Clariceptify/issues/254) | evidence/related-work/comparisons/batch-4.yaml |
| R2-CMP-005 | [#255](https://github.com/ArazSaieArasi3/Clariceptify/issues/255) | evidence/related-work/comparisons/batch-5.yaml |
| R2-CMP-006 | [#256](https://github.com/ArazSaieArasi3/Clariceptify/issues/256) | evidence/related-work/comparisons/batch-6.yaml |

Next independent work can proceed on the acquired OntoKADS, IAO, EFO, BDI and Cognitive Atlas texts and the recorded artifacts while the owner supplies the seven missing texts. Artifact acquisition/inspection tasks, paper reviews and scenario comparisons remain distinct; access gaps do not promote scientific acceptance.

## Reproduce the LMM inspection

```bash
python -m pip install -r requirements-dev.txt -r requirements-research.txt
python tools/inspect_related_artifacts.py --manifest evidence/related-work/corpus/lmm-inputs.yaml --source-dir /path/to/owner-reference-archive --output-dir /tmp/lmm-inspection
python tools/check_corpus_access.py
python tools/test_corpus_access.py
```
