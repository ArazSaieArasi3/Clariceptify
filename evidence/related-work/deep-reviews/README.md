# Shared deep paper review

This owner-authorized research wave reviews prior work. It makes no changes to the Clariceptify ontology, requirements, fixtures, manuscript or release state. Suggested future uses remain proposals until the owner supplies the next-version instructions.

- [Protocol](protocol.yaml): ten common dimensions, exact locators, evidence vocabulary, complete paper coverage and closure conditions.
- [Coverage guide](coverage-guide.md): full paper, all-declaration artifact census and semantic execution are separate; current per-paper boundaries are explicit.
- [Ordered register](register.yaml): twelve acquired PDFs (185 pages), seven waiting-for-owner texts and separately identified standards/module documentation. Exactly one current primary deep-review issue per paper.
- [Synthesis procedure](synthesis-protocol.yaml): partial acquired-source synthesis, six bounded comparison batches, then evidence-qualified final #126 synthesis and an owner decision.
- [Baseline protection](baseline-protection.json): protected scientific source fingerprint, including added/deleted members.

Each paper has `<work-id>/review.yaml` as structured evidence authority and a derived `<work-id>/report.md`. Evidence IDs are stable within the work; cite them as `work-id:E01` across papers. Catalog items, commitments, scenarios, findings, questions and synthesis inputs have separate stable IDs. Add source-bound annotations; do not silently rewrite an earlier scientific decision. A subsequent paper version gets an explicit version relation and renewed review.

A conceptual paper catalog is exhaustive for the ontology-bearing content of that paper. It does not purport to enumerate all classes in a separately released ontology. The eight-selected-commitment limit in technical artifact tasks does not limit paper extraction.

Completion of a critical review can expose unresolved claims, formula defects or unavailable formal files. It is not independent expert approval, a reproduced author experiment or semantic acceptance. Earlier limited reviews remain closed with their original scope; new deep followups do not retroactively enlarge them.

## Commands

```bash
python tools/render_deep_review.py evidence/related-work/deep-reviews/<work-id>/review.yaml
python tools/check_deep_reviews.py
python tools/test_deep_reviews.py
```

Raw third-party PDFs and repository snapshots remain in the retained source archive. Public dossiers contain original critical paraphrases, locators, digests and links. Unknown counts are null. Full-text gaps remain visible and are never replaced by a different paper, abstract or current OWL file.

## Supplementary source and class contract

The owner-authorized repository/class-definition/foundation requirement is specified in [catalog-contract.yaml](catalog-contract.yaml). The [23-source audit](source-audit.md) records actual repository versus standalone-file discovery, retained versions, foundation evidence, all-class glossary coverage and explicit gaps. This is supplementary technical coverage; earlier paper review closures do not imply all imported classes or semantic tests are complete.

Current complete local glossaries: [cDnS1.1](cDnS2007/classes.md), [LMM L1/L2](LMM2008/classes.md) and [Conceptualization0.1](shared-foundations/Conceptualization/classes.md). LMM has four missing source definition comments; imported DUL/IOLite definitions remain #88/#271. Research-only boundary: no Clariceptify model change.

The complete [LMM2008 paper dossier](LMM2008/report.md) now connects all six figures and 29 current local-class reviews to exact paper/artifact evidence. [diagrams.yaml](LMM2008/diagrams.yaml) retains the full visible slot inventory. Historical alignment recovery and eight selected semantic correspondence questions remain #274; imported definitions stay #88/#271.

The complete [DnS2003 paper dossier](DnS2003/report.md) preserves all 23 numbered displays and [five-figure inventory](DnS2003/diagrams.yaml). The official related DLP3971 distribution is retained; [structural intake](../corpus/dlp3971-intake.json) lists every supplied named class IRI and comment-availability state. Its58-local-class ExtendedDnS candidate is later source evidence, not the original 2003 class count or a completed manual glossary; #235 stays open.
