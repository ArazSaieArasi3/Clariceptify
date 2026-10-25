# R1 candidate reading guide

Status: synchronized candidate reader path after the actual license/creator decision.
Input baseline: d5672a1625193dd62107e089f984178f0c51b6c8; model input-r1-rev1;
diagram diagram-r1.2; current published candidate v0.1.0-rc.1.

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
| Reuse or cite | [Scoped licenses](../LICENSE), [creators](decisions/artifact-creators.md), [CITATION.cff](../CITATION.cff) | Owner-declared creators/order and CC-BY-4.0 research / MIT code; candidate citation omits an unissued date/DOI |

All required evidence for the public engineering checks is in this repository.
Private raw source files are not needed to read these views or run those checks.
Historical Word/PDF inputs remain provenance, not parallel editing authorities.
See [known limitations](known-limitations.md) before drawing scientific conclusions.

## Candidate and publication

The [candidate station](../releases/v0.1.0-rc.1/README.md) explains exact source
registration, reproducible builds and clean readback. A folder or build does not
establish publication. Check the [release index](../releases/release-index.yaml)
and actual GitHub Releases for issued versions. The final package disposition
under #62 applies to an exact candidate, independently of the owner-approved
license and creator metadata. No stable version is claimed by this guide.

The [actual RC publication and readback](../evaluation/release/rc-publication.yaml)
and [acceptance packet](review/rc1-acceptance.md) now identify the concrete candidate.
