# Exact R1 candidate acceptance packet

Status: **ACCEPTED BY ACTUAL OWNER**, 2026-10-25; issue #62. The direct
continuation instruction accepted this exact candidate with its recorded limitations.

Candidate: [v0.1.0-rc.1](https://github.com/ArazSaieArasi3/Clariceptify/releases/tag/v0.1.0-rc.1).
Source: `4780cba43a5aab8f9867073a1e89de824d421d28`.
Freeze/tag: `bcce59992606a22ddb82a49c243aeda6f7f54963`.
ZIP SHA256: `b27b14c9ec602734085762c4472938e55c2b33614ccd1fe0ea7240720efac7c7`.

| Review point | Concrete evidence / scope |
| --- | --- |
| Release claim | [R1 scope](../decisions/r1-scope.md): documented conceptual-model/requirements baseline, not completed semantic validation |
| Read the artifact | [Reading guide](../reading-guide.md), [model/reference](../reference/README.md), [diagram](../../model/diagrams/README.md) |
| Engineering evidence | [Actual publication/readback](../../evaluation/release/rc-publication.yaml): seven assets; 361 source / 364 archive members; eleven extracted checks; exact reviewed archive |
| Readiness | [Input-bound readiness](../../evaluation/release/rc-readiness.yaml): PASS_FOR_RC, no blockers for that declared claim; independent expert review NOT_ASSESSED |
| Limitations | [Known limitations](../known-limitations.md): pending source/typing/CQs, absent full formalization/native-tool validation/expert review/paper/DOI |
| Rights and creators | [Scoped LICENSE](../../LICENSE), [creators](../decisions/artifact-creators.md), [CITATION.cff](../../CITATION.cff): owner-approved metadata; detailed roles unassessed |
| Actual decision | [Scope disposition record](../../evaluation/release/scope-disposition.yaml): ACCEPTED; direct owner decision recorded on 2026-10-25 |

Decision requested: accept this exact candidate's declared scope and retained
limitations as the R1 baseline, or identify required changes. Acceptance concerns
package scope and stable promotion, not a declaration that all semantic/source/
CQ or expert-review work is complete. The earlier license/creator approval is
separate. No new license or creator confirmation is needed.

After actual acceptance, #63/#64 publish and read back stable v0.1.0. Requested
scientific/content changes require an explicit delta and a new candidate rather
than silently replacing issued assets.

Actual decision: [R1 scope acceptance](../decisions/r1-scope-acceptance.md).
The earlier decision-request wording above is retained as the question that was answered.
