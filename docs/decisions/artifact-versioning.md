# Artifact identity and version bindings

Decision date: 2026-10-24. Status: adopted for the R1 preparation scope. Evidence: issue [#9](https://github.com/ArazSaieArasi3/Clariceptify/issues/9).

Every governed family records a stable asset_id, kind, lifecycle and an immutable revision reference/content digest. Use a human semantic version where meaningful, not a fabricated independent release number for every image.

| Family | Example stable asset | Revision binding |
|---|---|---|
| Package | CLR-PACKAGE | package tag, source commit, manifest |
| Conceptual model | CLR-MODEL | model revision and registry digest set |
| Requirements | CLR-ORSD | ORSD 0.1 input plus controlled destination revision |
| Evaluation | CLR-EVAL-<protocol> | input fingerprints, tool/protocol version, run ID |
| Diagram | CLR-FIG-FULL | model ref, layout/generator ref, output digest |
| Documentation | CLR-DOC-SPEC | source ref and export profile |
| Manuscript | CLR-MANUSCRIPT | exact article revision, figure/model/evidence bindings |
| Formal ontology / RDB | separate assets when implemented | absent until implemented; then bind conceptual model and mappings |

An engineering package tag does not automatically increment model semantics, ORSD or manuscript versions. The alpha.1 package contains contracts and migration preparation; current_semantic_release remains null. An output correction may change a diagram/document revision with the semantic model unchanged. A definition/cardinality change affects model semantics and invalidates affected evidence/review bindings.

An evaluation remains applicable only when its declared relevant input fingerprints, protocol/tool and configuration match. An unrelated README edit need not invalidate model reasoning; a changed constraint cannot inherit an older PASS. A publication cites a frozen package/model/evaluation, not moving main. Historical distributions retain their bytes and status. A DOI identifies an archived research object, not its ontology namespace or validity.
