# R1 licensing decision

Status: **ADOPTED BY ACTUAL OWNER INSTRUCTION**, 2026-10-25; issue #52.
Input baseline: d5672a1625193dd62107e089f984178f0c51b6c8; model input-r1-rev1;
diagram diagram-r1.2. This changes distribution metadata, not model semantics.

The owner explicitly approved CC-BY-4.0 for research and MIT for code in the
continuation instruction on this date. This actual decision replaces the
proposal from PR #220. The instruction also supplied the three package creators
recorded in [artifact-creators.md](artifact-creators.md).

| Material | Adopted treatment |
| --- | --- |
| Original conceptual registries, requirements, documentation, diagrams, traceability and project assessments | CC-BY-4.0 |
| Original utility scripts, workflow code, schemas and dependency declarations | MIT, with paths scoped by the root LICENSE notice |
| Third-party publications, historical private raw inputs and font programs | Excluded from the grant and, for raw/full-text/font inputs, from distribution |
| Imported bibliographic metadata and attributed support | Preserve provenance and qualifications; no relicensing of underlying works |
| Vendored CFF schema | Upstream CC-BY-4.0, separately attributed in THIRD-PARTY-NOTICES.md |

The [root notice](../../LICENSE) and full [research](../../LICENSE-CC-BY-4.0)
and [software](../../LICENSE-MIT) texts implement the split. The grant covers
applicable rights in original project contributions; it does not assert
third-party consent or ownership of third-party works. The final manifest
will enumerate exact members, per-file license scope and exclusions.

Verification: license text provenance/hashes, creator order and CFF validation
are recorded in evaluation/release/publication-metadata.json. Actual final
package acceptance, expert review and DOI issuance remain separate.
