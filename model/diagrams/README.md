# Diagram source and approval evidence

The historical Conceptiom vector master has been recovered and hash-bound in [source-manifest.yaml](source-manifest.yaml). It is an editable SVG with 137 named concept groups and 296 named relationship groups, not a recovered native OntoUML project. The historical generator is unknown. Its one-page full PDF and 45-page A3 atlas are separately fingerprinted; common delivery does not prove exact regeneration or visual parity. Raw originals remain outside this public repository under the migration distribution policy.

[approval-state.yaml](approval-state.yaml) distinguishes authorization to draw the diagram from scientific acceptance. The source specification says review candidate; an unsupported approval adjective in SVG accessibility metadata must not elevate that state. The originals remain unchanged. A versioned corrected derivative, full/detail views and element-level/visual verification are the separate issues #43, #44 and #45.

Model registries remain the semantic authority. Do not correct or reinterpret the model only inside the diagram. Recovery and structural correspondence do not establish native OntoUML validity or expert approval.

Run `python tools/check_diagram_sources.py` to check the public source/approval contracts. With authorized recovered originals, add `--inputs /path/to/input-directory` to verify all four exact hashes and the XML/DOCX evidence. The stored [source audit](../../evaluation/diagrams/source-approval-check.json) records an actual private-input check; a later public-only invocation reports that input audit as not run. These checks also passed under Python optimization; altered source bytes were rejected in both modes.

## Current complete view (diagram-r1.1)

[generated/full.svg](generated/full.svg) is a controlled derivative of the exact recovered SVG, not a newly recovered native model or historical generator. It preserves all node/edge geometry, labels, direction, multiplicity and domain colors; adds stable registry identifiers and model hash bindings; changes the diagram brand to Clariceptify; corrects unsupported approval metadata; and removes embedded third-party font programs. Sans-serif fallback fonts are not distributed here. The manuscript title is unchanged.

Reproduce with `python tools/derive_complete_diagram.py /authorized/path/Conceptiom_Release_1_OntoUML_Full.svg`. The historical input SHA-256 is enforced. The public SVG remains editable without that private input. Install `requirements-diagrams.txt`, then run `python tools/check_diagram_model.py`. The [complete-model report](../../evaluation/diagrams/complete-model-parity.json) binds each of 137 nodes and 296 edges to its registry ID, checks visible labels/stereotypes, ordered endpoints, multiplicity text, endpoint geometry, all 21 domain colors/legend descriptions and current model hashes. It is not scientific approval or native OntoUML validation. The overall map requires substantial zoom and is not a printable reading view; PDF detail views are now generated under #44; exhaustive visual parity remains issue #45.

## PDF overview and A3 reading atlas

[generated/full.pdf](generated/full.pdf) preserves the complete vector canvas.
[generated/atlas.pdf](generated/atlas.pdf) provides 69 exact A3 landscape pages:
a linked overview, 66 overlapping detail tiles at source scale and two reflowed
legend/note pages. Print at actual size; follow row/column and neighbor labels.

Run `python tools/build_diagram_pdfs.py` with `requirements-diagrams.txt` installed.
The adapter reads the public current SVG, first audits its registry bindings and
records exact source/model/tool/output fingerprints in
[pdf-atlas-build.json](../../evaluation/diagrams/pdf-atlas-build.json).
The [generation review](../../evaluation/diagrams/pdf-atlas-review.md) records actual
coverage, vector, reproducibility and sampled visual checks and their limitations.
Neither generated PDF is an independent semantic authority. Issue #45 remains open.
