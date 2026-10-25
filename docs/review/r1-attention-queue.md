# Focused R1 review queue and evidence dossier

Model input-r1-rev1; diagram diagram-r1.2. Baseline: 2a48140d8fdb89ce80826a04dd2ab0acd7ddea89.
The [review-state register](../../evaluation/review-state.yaml) binds current evidence hashes.
Preparing this queue does not record an owner's or expert's actual decision.

| Review unit | Inspectable evidence | Decision question | Current disposition |
| --- | --- | --- | --- |
| Scope and claims | [R1 scope](../decisions/r1-scope.md), [bounded claims](../research/claim-register.yaml) | Accept a documented conceptual-model baseline with explicit scientific limits? | Final exact-package acceptance remains #62, after RC preparation. |
| Diagram rendering | [Correction](../../evaluation/diagrams/paint-order-reassessment.yaml), [image](../../evaluation/diagrams/paint-order-corrected.png) | Are the declared paint-order correction and reader views sufficient for R1 presentation? | Scoped correction is machine/agent assessed. Human semantic approval is unperformed. |
| Selected example and counterexample | [Positive](../examples/conceptualization-positive.md), [negative](../examples/conceptualization-negative.md), [results](../../evaluation/conceptualization-fixtures.json) | Is the one-clause demonstration described within its actual evidence limits? | Positive accepted and negative rejected for the selected subject-union clause only. |
| Imported source qualifications | [Reference index](../reference/README.md), [support registry](../../evidence/concept-support.yaml) | Are pending passage/typing qualifications visible and acceptable as R1 limitations? | No claim of completed full-text or semantic review. R2 assessment remains separate. |
| Distribution license | [Concrete proposal](../decisions/release-license.md) | Approve CC-BY-4.0 for original research artifacts and MIT for original utility code, with third-party exclusions? | BLOCKED pending actual decision; #52. |
| Package creators and citation | [Concrete proposal](../decisions/artifact-creators.md) | Confirm the proposed creators, order and actual roles for the package? | BLOCKED pending actual decision; #53, followed by #54 citation validation. |

Only the two publication-metadata decisions are actionable owner choices now.
The final package decision will refer to an exact RC and is not requested in advance.
This queue has six small units; it is not the entire backlog.

## Reproduce the engineering checks

- `python tools/check_review_state.py`
- `python tools/check_diagram_visual_parity.py --output /tmp/diagram.json`
- `python tools/check_conceptualization_fixtures.py --output /tmp/fixtures.json`
- `python tools/build_reference_pages.py --part concepts --baseline 2a48140d8fdb89ce80826a04dd2ab0acd7ddea89`
- `python tools/build_reference_pages.py --part relations --baseline 2a48140d8fdb89ce80826a04dd2ab0acd7ddea89`

The generated reference manifests bind every input/output digest; the fixture report
binds all selected model/requirement inputs and the actual validator. No private raw
input is needed for these public checks. The dossier is a review aid, not approval.
