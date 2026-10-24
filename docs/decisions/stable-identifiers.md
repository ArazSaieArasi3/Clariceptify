# Stable identifiers and qualified lineage

Decision date: 2026-10-24. Status: adopted for the R1 preparation scope. Evidence: issue [#8](https://github.com/ArazSaieArasi3/Clariceptify/issues/8).

Local record keys use CLR-C0001 (concept), CLR-D0001 (domain), CLR-R0001 (association), CLR-G0001 (generalization) and CLR-SC0001 (constraint). They contain no model version or mutable label. Domain primary membership and relationship endpoints use IDs. Do not reuse allocated/released keys for a different referent. FR-01, QR-01 and CQ-01 retain their existing requirement-family identifiers and are qualified by their artifact/version when referenced.

These local record keys are not registered ontology IRIs. This wave reserves catalogue keys in a migration ledger; it does not assert acceptance of new semantic identities. Existing valid historical entity IDs and IRIs are preserved in qualified lineage. No historical identifier is rewritten or retired solely because the repository or brand changes.

The source inventory namespace C001..C387 is distinct from the thesis-core CO-F001..CO-F003, CO-C001..CO-C008 and CO-R001..CO-R010. Use `(source repository, commit, registry family, source ID)` as a predecessor key. Do not infer identity by a shared label or number.

The initial source-row-to-key reservation is frozen with the input digest; future sorting is presentation only. New entities receive the next unused key. Pure renaming retains identity and records the old label as an alias after review. Conceptiom is the historical working brand; Clariceptify is the destination brand. Neither is a novelty or trademark-exclusivity assertion.

Examples: correcting the spelling of a label leaves CLR-C0001 unchanged; splitting its intended meaning creates distinct successor keys and a lineage record; merging two entities records both predecessors and a justified successor; a retired key remains a tombstone and is never reassigned. `Conceptualization Process` is an inherited alias candidate for Conceptualization, not a new class by default.

Legacy alignment status is one of candidate_same_label, candidate_alias, reviewed_preserved, reviewed_refined, replaced, rejected or unresolved. Only a semantic decision can promote a candidate to reviewed_preserved; machine label matching cannot. A preserved historical entity may be bound to a local record key without changing the historical entity IRI. Canonical ontology/entity/version/document IRIs remain unassigned until the corresponding decision and resolver exist.
