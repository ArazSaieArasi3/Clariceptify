# Local checks and controlled input import

Install requirements-dev.txt and run, from repository root:

```sh
python tools/check_repository_language.py
python tools/check_bootstrap.py
python tools/check_model_import.py
python tools/check_requirements.py
python tools/check_source_support.py
python tools/check_trace_contracts.py
python tools/check_generated_links.py
python tools/check_requirement_witnesses.py
python tools/check_claim_register.py
```

These checks need no private repository or raw document access. They check record/graph/contract integrity, not adequacy or independent acceptance. Reports live under evaluation/.

To reconstruct the selected input imports, obtain authorized digest-matching documents, install requirements-import.txt, and run import_selected_model.py, import_orsd.py, then import_source_support.py with their respective source DOCX paths. The final step restores qualified bibliographic bindings to concept records. This pipeline is for the frozen original input, not a way to overwrite later accepted semantic changes. See docs/decisions/source-support-import.md.

build_bootstrap_preview.py remains restricted to the previously approved alpha.1 snapshot and cannot silently publish a newer model under that tag.

The language guard checks current file paths and UTF-8 text for Arabic/Persian script. It does not inspect remote issue/PR/release content, history or binary artifacts; check those before posting. See CONTRIBUTING.md and AGENTS.md.

`build_artifact_register.py` rebuilds the declared storage snapshot plus its hash-bound publication receipt. Stable IDs are explicit mappings; update locators without reallocating IDs. `check_trace_contracts.py` checks the snapshot and initial edge schema, including negative integrity/claim cases; it does not claim a complete generated graph.

For the historical alpha.2 builder use commit b0edfdcb99e283eadce94ba11535d8179dbd1f04. The current baseline builder is restricted to the alpha.2.1 correction; it does not replace published assets.

For authorized input reconstruction, `import_requirement_witnesses.py ORSD.docx` imports the original table-6 witness proposals after the ORSD/model imports. Run `build_trace_links.py` afterwards. The optional private-input parity checker now compares all 14 outputs; the public integrity commands need no raw DOCX files.

`build_claim_register.py` records the bounded working claims and explicit draft-manuscript binding. `check_claim_register.py` checks input fingerprints and claim-state boundaries, not philosophical soundness, novelty or peer approval.

## Public integrity gates

`check_schemas.py` validates model and need/CQ record contracts plus stable ID uniqueness. `check_model_structure.py` checks primary domains, both endpoint families and specialization cycles; connectivity is descriptive. `check_traceability.py` freshly runs artifact, generated-link, witness and claim checks, rejecting missing input fingerprints and stale/unsafe bindings. These commands need no private inputs and do not establish semantic adequacy or satisfaction. Reports under evaluation/ record the scoped initial runs; CI must evaluate current bytes rather than inherit those PASS values.

## CI evidence

`python tools/run_integrity.py --output ../clariceptify-integrity` runs the seven public gate layers and writes reports outside the evaluated tree. It records actual Git commit/tree, every tracked input digest, all validator digests, tool versions, event/run identifiers and per-layer results. A dirty local tree is explicitly labelled and never presented as a clean commit. No stored PASS is inherited.

The single primary `ci.yml` workflow uses read-only repository permissions, declared public path triggers, cancellation of superseded development runs and a retained evidence artifact. It does not run formal reasoners, access private inputs, commit results or publish releases. The separately requested immutable release publishers keep their own non-cancelling publication gates.

## Same-source diagram PDFs

Install `requirements-diagrams.txt`, then run `python tools/build_diagram_pdfs.py`.
This generates the vector overview and exact A3 reading atlas from the current
hash-bound public SVG after its registry audit. See `model/diagrams/README.md`
and `evaluation/diagrams/pdf-atlas-build.json`. The #45 assessment reports preserved element parity but blocked readability (#217).

`check_diagram_visual_parity.py --output /tmp/visual-parity.json` performs the
input-bound SVG/PDF/atlas element audit and approximate later-stroke/text
intersection screen. `test_diagram_visual_parity.py` verifies rejection of stale
PDF bytes and displaced geometry/text even after an updated output checksum.
Read `evaluation/diagram-parity.yaml` for the actual human/agent/machine review
boundaries and the open rendering correction. A successful parity command does
not mean the R1 readability gate passed.

## Reference views, fixtures and review states

`build_reference_pages.py --part concepts --baseline COMMIT` generates concept/domain
pages and qualified source displays. Run `--part relations` afterwards for relation,
generalization and textual-constraint tables and eight typed CSV exports. Every
source field round-trips; model/evidence YAML remains the editable authority.
Manifests are `evaluation/reference-concepts.json` and `reference-relations.json`.

`check_conceptualization_fixtures.py --output /tmp/fixtures.json` exercises the
positive episode and the one-clause empty-subject counterexample. This does not
change global CQ/constraint execution states. `check_review_state.py` checks evidence
hashes, review types and actual-decision boundaries; it also runs with Python -O.
See `docs/review/r1-attention-queue.md` for six bounded review units and publication
metadata decisions. Neither script can manufacture human or scientific approval.

## Exact release engineering

The RC and stable manifests describe their respective issued packages; use the frozen payload source
commit and its trusted freeze manifest as described in the
[candidate station](../releases/v0.1.0-rc.1/README.md). Later changes on main
correctly fail the old exact manifest if passed as the source root.

`build_release.py` emits a deterministic archive, package manifest and checksums;
`readback_release.py` validates exact membership/bytes before extracting and
running eleven public checks. It needs no Git/private raw inputs or network.
The fresh file tree uses declared installed Python dependencies, not a new OS.
`test_release_preparation.py` runs eight preparation/RC boundary cases.

Historical `preparation_only` manifests produce `clariceptify-r1-preparation.zip`;
strictly registered `rc_candidate` manifests produce `clariceptify-v0.1.0-rc.1.zip`.
Neither command publishes a release or grants final owner acceptance.
Re-register a changed source as a new candidate/version record; never overwrite
an issued payload or merely update hashes to conceal a failing content check.

## Candidate publication metadata and package

`python tools/check_publication_metadata.py` validates the official CFF 1.2.0
schema and owner-declared creators, version and scoped licenses. It is the
eleventh public integrity layer. The release builder accepts either explicit
preparation snapshots or a strictly registered `rc_candidate` bound to an exact
source commit. Readback checks all eleven layers on fresh extraction. See the
[candidate station](../releases/v0.1.0-rc.1/README.md). Existing historical
preparation evidence remains input-bound and does not grant RC readiness.

## Accepted stable promotion

`check_stable_promotion.py` compares every protected scientific member with the
exact accepted RC manifest, checks actual owner disposition, and is called by
the eleventh integrity layer for stable metadata. The stable manifest uses
`accepted_stable` and its own envelope path. Rebuild instructions are in
[the stable station](../releases/v0.1.0/README.md). Actual issuance/readback remains
a separate action; builders do not grant approval or publish.

Current stable publication/readback is recorded in evaluation/release/published-readback.yaml.
Use the stable station instructions for v0.1.0; historical RC commands retain their
RC filename and trusted manifest. Eleven boundary cases now cover all three stages.

## Controlled conceptual documentation

Install requirements-docs.txt as well as requirements-dev.txt.
`build_documentation.py --source-ref COMMIT --output /tmp/site` creates the
complete conceptual portal and fourteen Wiki projections from twelve guide
pages. `build_pages.py` combines current and exact-ref frozen routes. The
`check_documentation.py` layer validates reader completeness, paths/anchors and
VVEAA planned-versus-actual evidence boundaries. Two negative controls reject
a missing reader target and a stale profile/report binding. Current primary CI
has twelve layers; the issued v0.1.0 release retains its original eleven.

`build_manuscript_figure.py --output OUTPUT.svg` derives the selected 13-class/14-association portrait figure and its exact row bindings. `check_documentation.py` rejects stale figure, manuscript asset and evidence identities. The owner-managed article remains a draft; its raw bytes are not part of public CI. `readback_pages.py` compares actual public current/frozen reader bytes against each exact build manifest.

## DUL source-bound technical review

`check_dul_technical_review.py` and `check_dul_class_catalog.py` validate public evidence/claim bindings without private inputs or network access. They do not rerun reasoning. For exact-source reconciliation, run the glossary checker with `--source DUL.owl`.

The optional research runners `inspect_dul_semantics.py` and `inspect_dul_modules.py` consume private hash-pinned source files. Use rdflib 7.6.0, owlready2 0.51 and Java for the semantic runner; keep complete combined source graphs and logs outside the public repository with `--private-dir`. The former runs isolated full-root consistency/adverse cases; the latter inventories selected asserted module closures with blank nodes standardized apart. Neither downloads sources, modifies Clariceptify, redistributes third-party bytes or establishes scientific acceptance. Run under a bounded process timeout (the recorded 29-case run used 240 seconds).

Install the optional pinned runner dependencies with `python -m pip install -r requirements-dul-review.txt`; Java must also be available.
