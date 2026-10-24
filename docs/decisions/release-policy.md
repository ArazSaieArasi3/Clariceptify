# Frequent release stations and compatibility

Decision date: 2026-10-24. Status: adopted for the R1 preparation scope. Evidence: issue [#10](https://github.com/ArazSaieArasi3/Clariceptify/issues/10).

## Stations

| Version | Meaning | Required work IDs |
|---|---|---|
| v0.1.0-alpha.1 | contracts, schemas, input inventory and candidate migration ledger | R1-001..R1-007 and their split units |
| v0.1.0-alpha.2 | controlled model/requirement/source import | transfer units |
| v0.1.0-alpha.3 | typed traceability and baseline integrity checks | traceability/control units |
| v0.1.0-rc.1 | synchronized, readable, reconstructable candidate | diagram, documentation, fixture, review and packaging gates |
| v0.1.0 | declared conceptual-model baseline | resolved scoped blockers and actual release disposition |
| v0.2.0 | domain/CQ adequacy assessment and prioritized changes | source comparison and R2 review/fix evidence |
| v0.3.0 | formalized selected subset | declared OWL/SHACL/reasoning/CQ/FOL evidence |

Publish at coherent checkpoints, not for every routine commit. An alpha is explicitly a prerelease; preparation of release files is not an actual GitHub Release. Repeat RCs when needed; never call incomplete work stable. DOI deposit is an independent post-R1 milestone.

PATCH changes packaging/editorial/link details while semantic and scholarly-claim contracts stay fixed (v0.1.0 -> v0.1.1). New semantic scope or changed evidence-supported claims use a new 0.x MINOR (v0.1.x -> v0.2.0). Pre-1.0 incompatible changes must explicitly state the break, affected IDs, consumers and migration; consumers must not assume minor compatibility. After 1.0 incompatible semantics require MAJOR, compatible extension MINOR, and contract-preserving correction PATCH. A new folder or label alone does not decide version impact.

Never move a published tag or replace its scholarly payload. Release notes state what changed, evidence that applies, limitations and compatibility. A newly issued DOI may be added to current metadata without rewriting the frozen package; distinguish metadata change from model change.

## Integrity contract

Manifest binds exact source commit and input/model/evaluation/document versions. Output digests are computed after generation; SHA256SUMS excludes itself. Do not demand a commit digest stored inside the very commit it hashes. Public readback must verify actual membership and digests. Model validity, human approval and public/archival accessibility remain distinct gates.

Keep one automatic validation entrypoint when CI is introduced; expensive checks depend on semantic risk and relevant inputs. Historical/manual release gates remain reproducible. This policy creates no recurring agent or scheduler.
