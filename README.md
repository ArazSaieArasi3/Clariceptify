# Clariceptify

An Ontology for Representing Conceptualization Knowledge

Clariceptify develops a conceptual model of purposeful conceptualization and its explicit products. This repository is currently at the **R1 stable baseline v0.1.0** station: scoped traceability and public integrity/CI are published; diagram element parity has been assessed and the scoped rendering defect in #217 corrected; owner-declared licensing/creators and validated citation are recorded; the exact candidate has passed readiness and public readback. Definitions and modeling commitments are preserved from the selected input. No stable semantic release or completed semantic acceptance is claimed.

The selected input comprises 137 concepts, 20 subject domains plus Foundations, 174 associations, 122 generalizations and 24 textual constraints. These are input counts, not a claim of semantic completeness. R1 will publish a documented conceptual-model/requirements baseline; R2 assesses scoped adequacy and sources; R3 formalizes a declared subset.

Latest stable release: [v0.1.0](https://github.com/ArazSaieArasi3/Clariceptify/releases/tag/v0.1.0).
The actual owner accepted the documented baseline scope and retained limitations.
All 233 protected scientific members match the accepted RC. The stable ZIP has
375 registered source members and 378 archive members; all ten issued assets,
nine checksum entries and eleven extracted checks were verified. See
[actual stable readback](evaluation/release/published-readback.yaml),
[the frozen manifest](releases/v0.1.0/manifest.yaml), and
[stable rebuild instructions](releases/v0.1.0/README.md).
The accepted model remains input-r1-rev1 and diagram diagram-r1.2; scientific
adequacy/source/CQ/expert qualifications remain explicit. All R1 work units are
completed within that declared scope; later research work is tracked separately.

Latest prerelease: [v0.1.0-rc.1](https://github.com/ArazSaieArasi3/Clariceptify/releases/tag/v0.1.0-rc.1).
The exact candidate has 361 registered source members and 364 archive members;
two builds are byte-identical. All seven issued assets were downloaded and checked,
and all eleven public checks passed on actual downloaded archive extraction.
See [publication evidence](evaluation/release/rc-publication.yaml) and the
[focused acceptance packet](docs/review/rc1-acceptance.md). The owner accepted the exact candidate with its recorded limitations on 2026-10-25
([decision](docs/decisions/r1-scope-acceptance.md)). Stable publication/readback
under #63/#64 are complete; see the actual stable readback record above.

Previous engineering checkpoint: [v0.1.0-alpha.3](https://github.com/ArazSaieArasi3/Clariceptify/releases/tag/v0.1.0-alpha.3). It freezes the scoped traceability/integrity station at f4a3e233fc283c065a2c48297657878a4625d780: 118 source files evaluated by actual main CI, with 1,815 project links, candidate witnesses, bounded claims and public checks. All five public assets and 122 archive members were read back. See the [release index](releases/release-index.yaml), [changelog](CHANGELOG.md) and [public readback](evaluation/traceability-preview-publication.json). Package version does not establish model semantic acceptance.

## Start here

- [R1 scope and claim boundary](docs/decisions/r1-scope.md)
- [Authority and composition](docs/decisions/artifact-authority.md)
- [Imported model registries](model/) and [import checks](evaluation/model-structure-report.json)
- [Requirements and CQ contracts](requirements/) and [qualified source support](evidence/)
- [Model schemas](model/schema/) and [artifact implementation status](docs/artifact-status.yaml)
- [Artifact identities, generated links and candidate witnesses](traceability/)
- [Bounded claims and manuscript binding](docs/research/claim-register.yaml)
- [Input manifest](traceability/migration/source-manifest.yaml), [integrity](traceability/migration/input-integrity.yaml) and [candidate entity ledger](traceability/migration/entity-ledger.yaml)
- [Identifiers](docs/decisions/stable-identifiers.md), [artifact versions](docs/decisions/artifact-versioning.md), [release policy](docs/decisions/release-policy.md)
- [Bootstrap verification](evaluation/bootstrap-report.json) and [local check](tools/README.md)
- [Contribution and English-only policy](CONTRIBUTING.md)
- [Related-work candidate register](evidence/related-work/)
- [Complete 24-row retained reference collection](evidence/related-work/reference-crosswalk.md), including four unreviewed supplementary source leads
- [OntoLex 2016 official-document critical review](evidence/related-work/reviews/OntoLex.md), separate from the paper corpus and pending formal-artifact task
- [Shared deep-paper review framework and current queue](evidence/related-work/deep-reviews/README.md)
- [Execution roadmap](https://github.com/ArazSaieArasi3/Clariceptify/issues/1)

## Structure and status

`requirements/` owns requirements/CQ contracts; `model/` owns the conceptual registries; `evidence/` owns source support; `traceability/` owns bindings and migration; `evaluation/` owns actual results; `docs/` owns explanations; `releases/` owns frozen package membership; `tools/` owns reproducible commands. Implementation status is explicit: candidate model registries are imported; requirements and source-support bindings are imported as review baselines; formal ontology files are absent.

Research identity remains R-001; Portfolio owns research governance and OGCM-RF supplies method contracts. Pinned local profiles record adoption without claiming assessed conformance. Public users can read these local decisions and run the bootstrap check without access to private upstream repositories. Historical inputs and releases retain their identities; this wave does not clean up or change the origin repository.

## Limits and reuse status

No full OWL/SHACL/FOL implementation, relational projection, all-CQ execution, joint satisfiability proof, independent expert acceptance, complete literature review or novelty priority is claimed. Diagram element parity and the scoped paint-order correction are assessed; source-passage reconciliation remains open. No DOI or registered ontology IRI is assigned here. Original research material is CC-BY-4.0 and original code is MIT under the [scoped LICENSE notice](LICENSE). The owner-declared creators, in order, are Araz Saie Arasi, Hassan Haghighi and Hossein azgomi. See [CITATION.cff](CITATION.cff) for the candidate citation and [third-party notices](THIRD-PARTY-NOTICES.md) for exclusions. Raw thesis, article and third-party full texts are not distributed in this bootstrap.

## Historical diagram-r1.1 assessment

The [visual assessment](evaluation/diagram-parity.yaml) binds the historical diagram-r1.1 complete
SVG, vector PDF and A3 atlas to the model. Element parity passed; readability did
not pass because later connector strokes obscure some labels. See the
[evidence plate](evaluation/diagrams/readability-findings.png) and
[blocking correction #217](https://github.com/ArazSaieArasi3/Clariceptify/issues/217).
This completed review is neither a rendering repair nor scientific acceptance.

Current diagram-r1.2: [scoped rendering reassessment](evaluation/diagrams/paint-order-reassessment.yaml)
records the #217 correction, zero current connector-over-text candidates, exact
geometry/label-value preservation and regenerated same-source PDFs. Historical
negative evidence remains intact. This is not human scientific acceptance.

## Reference and review path

- [Concept/domain/source reference](docs/reference/README.md)
- [Relations and generalizations](docs/reference/relations/README.md)
- [Textual constraints](docs/reference/constraints/README.md)
- [Lossless CSV export contract](docs/reference/exports/README.md)
- [Positive and negative example result](evaluation/conceptualization-fixtures.json)
- [Review state](evaluation/review-state.yaml) and [six-unit dossier](docs/review/r1-attention-queue.md)

The [license decision](docs/decisions/release-license.md) and
[creator/citation decision](docs/decisions/artifact-creators.md) record the actual
owner instruction of 2026-10-25. Detailed contribution roles remain unassessed.
They do not establish final package acceptance or independent expert review.

## First-release candidate

Follow the [reading guide](docs/reading-guide.md), inspect the
[known limitations](docs/known-limitations.md), and use the
[candidate build/readback instructions](releases/v0.1.0-rc.1/README.md).
The [exact manifest](releases/v0.1.0-rc.1/manifest.yaml), readiness and actual
publication evidence identify the issued RC. Rebuilding requires the frozen
source commit plus its trusted manifest; later main-branch documentation edits
do not replace the published package. Root CITATION.cff and the issued stable package name 0.1.0. The GitHub Release and its publication/readback record establish actual issuance.

## Documentation and next research increment

The [shared reader guide](docs/guide/Home.md), [publication-surface contract](docs/publication-surface-contract.yaml)
and [release sequence](docs/development/release-sequence.md) prioritize Wiki and
conceptual Pages now, over unchanged scientific core v0.1.0. Publication receipts
will distinguish preparation, actual deployment and frozen routes. WIDOCO/WebVOWL
remain dependent on an actual formal slice.

The [critical-review protocol](evidence/related-work/review-protocol.yaml),
[VVEAA profile](evaluation/vveaa-profile.yaml) and [initial evidence report](evaluation/vveaa-report.yaml)
make each function, population, method and missing evidence explicit. Initial
manuscript alignment precedes final comparative/contribution and submission gates.

The [initial manuscript alignment](docs/research/manuscript-contract.yaml) binds revision `0.1-r1-aligned.1` to the published R1 core and current evidence. The eight-page draft has a source-derived selected figure and explicit limits; final comparison, bibliography and R2 submission gates remain open.

The [first DnS-family comparison](docs/research/dns-family-comparison.md) records scoped primary-source reviews and pinned artifact inspections. See the [execution guide](evidence/related-work/execution-guide.md) for evidence and reproducible counts; full corpus synthesis and two DUL prerequisites remain open.

The [source-access and archive report](docs/research/corpus-access.md) records all 19 original candidates, seven requested texts, five pinned repository snapshots and the completed LMM paper/artifact review. The [23 medium-sized extension tasks](evidence/related-work/corpus/extension-tasks.json) preserve the original plan and keep source access separate from comparative evaluation.

Research checkpoint: [DUL4.2 technical review and 78-class glossary](evidence/related-work/artifacts/DUL-technical-review.md), with version-qualified semantic cases and retained source gaps. This evidence does not change the Clariceptify ontology or complete final synthesis.

Shared research foundation: [IOLite1.8 complete selected-class glossary and LMM import coverage](evidence/related-work/deep-reviews/shared-foundations/IOLite/README.md). This accounts for source-definition gaps without changing the Clariceptify model.

- [SKOS Reference critical document review](evidence/related-work/reviews/SKOS.md): source and errata evidence; formal artifact work remains separate.

- [O4OA supporting specification checkpoint](evidence/related-work/artifacts/O4OA.md): 138 document rows; #91 remains blocked on the formal artifact.
