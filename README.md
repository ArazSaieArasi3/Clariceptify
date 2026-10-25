# Clariceptify

An Ontology for Representing Conceptualization Knowledge

Clariceptify develops a conceptual model of purposeful conceptualization and its explicit products. This repository is currently at the **R1 post-alpha.3 preparation** station: scoped traceability and public integrity/CI are published; diagram element parity has been assessed and the scoped rendering defect in #217 corrected; remaining R1 review/documentation/package gates follow. Definitions and modeling commitments are preserved from the selected input. No stable semantic release or completed semantic acceptance is claimed.

The selected input comprises 137 concepts, 20 subject domains plus Foundations, 174 associations, 122 generalizations and 24 textual constraints. These are input counts, not a claim of semantic completeness. R1 will publish a documented conceptual-model/requirements baseline; R2 assesses scoped adequacy and sources; R3 formalizes a declared subset.

Latest engineering prerelease: [v0.1.0-alpha.3](https://github.com/ArazSaieArasi3/Clariceptify/releases/tag/v0.1.0-alpha.3). It freezes the scoped traceability/integrity station at f4a3e233fc283c065a2c48297657878a4625d780: 118 source files evaluated by actual main CI, with 1,815 project links, candidate witnesses, bounded claims and public checks. All five public assets and 122 archive members were read back. See the [release index](releases/release-index.yaml), [changelog](CHANGELOG.md) and [public readback](evaluation/traceability-preview-publication.json). Package version does not establish model semantic acceptance.

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
- [Execution roadmap](https://github.com/ArazSaieArasi3/Clariceptify/issues/1)

## Structure and status

`requirements/` owns requirements/CQ contracts; `model/` owns the conceptual registries; `evidence/` owns source support; `traceability/` owns bindings and migration; `evaluation/` owns actual results; `docs/` owns explanations; `releases/` owns frozen package membership; `tools/` owns reproducible commands. Implementation status is explicit: candidate model registries are imported; requirements and source-support bindings are imported as review baselines; formal ontology files are absent.

Research identity remains R-001; Portfolio owns research governance and OGCM-RF supplies method contracts. Pinned local profiles record adoption without claiming assessed conformance. Public users can read these local decisions and run the bootstrap check without access to private upstream repositories. Historical inputs and releases retain their identities; this wave does not clean up or change the origin repository.

## Limits and reuse status

No full OWL/SHACL/FOL implementation, relational projection, all-CQ execution, joint satisfiability proof, independent expert acceptance, complete literature review or novelty priority is claimed. Diagram element parity and the scoped paint-order correction are assessed; source-passage reconciliation remains open. No DOI or registered ontology IRI is assigned here. The repository-level reuse license and final creator/citation metadata remain to be settled in the dedicated publication tasks; public visibility alone is not a reuse license. Raw thesis, article and third-party full texts are not distributed in this bootstrap.

## Historical diagram-r1.1 assessment

The [visual assessment](evaluation/diagram-parity.yaml) binds the current complete
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

The [license proposal](docs/decisions/release-license.md) and
[creator/citation proposal](docs/decisions/artifact-creators.md) await an actual
owner decision. No root license grant, stable release, DOI or human acceptance is
created by these generated documentation and review artifacts.
