# Post R1 execution and release sequence

Decision date: 2026-10-25. Input baseline: 105049edd7c6caf7e3ab7eca1b43788065a7c739.
The owner prioritizes public documentation and initial manuscript alignment while
R2 strengthens the scientific evidence. This decision does not change frozen R1 bytes.

| Station | Deliverable | Gate |
| --- | --- | --- |
| v0.1.1 | Versioned conceptual documentation | Actual public Pages and Wiki readback, exact controlled source, current/frozen identities, links/figures and limitations. |
| v0.1.2 | Initial manuscript and artifact alignment | Bounded draft alignment only; final title/contribution/Related Work and final submission tasks remain open pending their actual R2 prerequisites. |
| v0.2.0-alpha.1 | Closest-work comparison preview | Existing #135 exact dependencies; missing full texts and counts stay explicit. |
| v0.2.0-alpha.2 | Priority domain and source adequacy preview | Existing #136 dependencies plus input-bound review findings, no aggregate score conceals a blocker. |
| v0.2.0-beta.1 | Evaluation and manuscript consolidation | All declared R2 evidence obligations accounted for; each missing assessment has a disposition and scope consequence. |
| v0.2.0-rc.1 | Exact R2 candidate | Exact source, scientific delta from R1, resolved release-scope blockers and actual candidate review. |
| v0.2.0 | Assessed conceptual baseline | Actual accepted scope and public readback; independent review is claimed only if performed. |

## Publication order

Wiki and conceptual Pages are first. The complete R1 registries, diagram and
recorded evidence already support a reader portal. The architecture follows OntoSPK:
one curated guide, generated Wiki, conceptual reference, search, versioned routes,
explicit evidence and downloads. OWL-only WIDOCO/WebVOWL surfaces remain deferred
until their actual input artifact exists.

The first manuscript can be corrected against R1 immediately. Its comparative gap,
final contribution and final submission acceptance remain dependent on the R2 reviews.
Preparatory draft work is not closure of #178-#186.

#175 now depends on #172/#173 for the conceptual portal. The former mandatory #174
dependency is moved to the later formal-reference extension, under explicit owner
instruction. #174/#176 retain their scope and remain open.

Use [the machine-readable sequence](release-sequence.yaml) and the
[VVEAA profile](../../evaluation/vveaa-profile.yaml) for exact gates.
