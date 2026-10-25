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

## Preparation-only release engineering

`python tools/build_release.py --output /tmp/clariceptify-preparation` checks the
exact manifest and creates a deterministic local package, package manifest and
checksums. It refuses RC/stable promotion and performs no publication.
`python tools/readback_release.py /tmp/clariceptify-preparation/clariceptify-r1-preparation.zip`
checks exact archive membership and bytes before extraction, then runs ten public
checks in a fresh temporary file tree with an empty HOME and the current declared
Python dependencies. It needs no Git/private raw inputs or network.

`python tools/test_release_preparation.py` exercises changed source/member bytes,
unregistered archive paths and unauthorized preparation-to-RC promotion. A technical
PASS leaves publication BLOCKED until actual license/creator/citation and final
package/readiness/acceptance decisions are recorded. Re-register the manifest after
any input changes; do not update hashes merely to hide a failing content check.

## Candidate publication metadata and package

`python tools/check_publication_metadata.py` validates the official CFF 1.2.0
schema and owner-declared creators, version and scoped licenses. It is the
eleventh public integrity layer. The release builder accepts either explicit
preparation snapshots or a strictly registered `rc_candidate` bound to an exact
source commit. Readback checks all eleven layers on fresh extraction. See the
[candidate station](../releases/v0.1.0-rc.1/README.md). Existing historical
preparation evidence remains input-bound and does not grant RC readiness.
