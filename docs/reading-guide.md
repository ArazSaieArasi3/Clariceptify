# R1 reading guide - preparation edition

Status: technically prepared; issue #55 remains open until actual citation
metadata is available. This guide creates no license or scientific acceptance.
Base: eeaa4a23d419ed6c3d915155bad3eebaab1a994a; model input-r1-rev1;
diagram diagram-r1.2; latest published engineering checkpoint v0.1.0-alpha.3.

| Reader goal | Start here | Interpretation |
| --- | --- | --- |
| Understand purpose and claim ceiling | [R1 scope](decisions/r1-scope.md) | Documented conceptual-model baseline, with explicit limits |
| Inspect conceptual commitments | [Concepts and domains](reference/README.md), [model registers](../model/README.md) | Candidate definitions, stereotypes, primary membership and qualified sources |
| Inspect relationships | [Associations](reference/relations/README.md), [generalizations](reference/relations/generalizations.md), [constraints](reference/constraints/README.md) | Multiplicities at their class ends; generalization points to parent; textual constraints are not all executable |
| Inspect requirements | [Requirement contracts](../requirements/README.md) | Reconstructed ORSD, candidate witnesses and unexecuted global CQs |
| Read the diagram | [Diagram guide](../model/diagrams/README.md), [full PDF](../model/diagrams/generated/full.pdf), [A3 atlas](../model/diagrams/generated/atlas.pdf) | Zoomable overview and same-scale details; scoped paint-order correction at diagram-r1.2 |
| Inspect source support | [Source register](reference/sources.md), [qualified support](../evidence/concept-support.yaml) | D/B/P are inherited screening qualifications; passage and typing review are not promoted |
| Inspect evidence and review | [Review dossier](review/r1-attention-queue.md), [review state](../evaluation/review-state.yaml) | Machine/agent checks and unperformed owner/expert review remain distinct |
| Run an example | [Positive example](examples/conceptualization-positive.md), [negative example](examples/conceptualization-negative.md) | One selected subject-union clause, not full instance conformance |
| Inspect traceability | [Trace guide](../traceability/README.md), [artifact register](../traceability/artifacts.yaml) | Declared identities, structural/source links and candidate witnesses; no full research-asset coverage claim |
| Reuse or cite | [License proposal](decisions/release-license.md), [creator/citation proposal](decisions/artifact-creators.md) | Actual owner decisions and final root CITATION.cff are pending |

All required evidence for the public engineering checks is in this repository.
Private raw source files are not needed to read these views or run those checks.
Historical Word/PDF inputs remain provenance, not parallel editing authorities.
See [known limitations](known-limitations.md) before drawing scientific conclusions.

## Preparation and publication

The [preparation manifest](../releases/v0.1.0-rc.1/manifest.yaml) registers an exact
working snapshot for local packaging tests. Its folder names the target station;
it is not an issued RC tag or a published GitHub Release. License/creator/citation
decisions, final reading-path acceptance, RC readiness and package acceptance
must still be recorded against the actual final package.
