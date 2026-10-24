# Clariceptify

An Ontology for Representing Conceptualization Knowledge

Clariceptify develops a conceptual model of purposeful conceptualization and its explicit products. This repository is currently at the **R1 traceability and claim-baseline preparation** station: the imported candidate baseline is published; structural/source/witness links, migration parity and bounded claim records are present. Definitions and modeling commitments are preserved from the selected input. No stable semantic release or completed semantic acceptance is claimed.

The selected input comprises 137 concepts, 20 subject domains plus Foundations, 174 associations, 122 generalizations and 24 textual constraints. These are input counts, not a claim of semantic completeness. R1 will publish a documented conceptual-model/requirements baseline; R2 assesses scoped adequacy and sources; R3 formalizes a declared subset.

Latest engineering prerelease: [v0.1.0-alpha.2.1](https://github.com/ArazSaieArasi3/Clariceptify/releases/tag/v0.1.0-alpha.2.1). It freezes the imported candidate model, retrospective requirements/CQ contracts and qualified source baseline at fe347d2e62262f1cd43558d2330438f433f64f1d. It corrects check-report ordering in alpha.2 without changing scientific input. Alpha.1 and alpha.2 remain unchanged. See the [changelog](CHANGELOG.md) and [public readback](evaluation/baseline-preview-publication-alpha2-1.json).

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

No full OWL/SHACL/FOL implementation, relational projection, all-CQ execution, joint satisfiability proof, independent expert acceptance, complete literature review or novelty priority is claimed. Diagrams and source passages still require reconciliation. No DOI or registered ontology IRI is assigned here. The repository-level reuse license and final creator/citation metadata remain to be settled in the dedicated publication tasks; public visibility alone is not a reuse license. Raw thesis, article and third-party full texts are not distributed in this bootstrap.
