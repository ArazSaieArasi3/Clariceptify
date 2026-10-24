# Source-support import representation

The actual imported representation for R1-016 is the Stage-1 support table, concept reference cells and 53-entry bibliography in the frozen SRC-SPEC DOCX. Its SHA-256 is bound in the input manifest and every extracted record. The separate identified Stage-1 JSON input has not been materialized or byte-compared; this change does not claim JSON byte parity. Raw documents are not redistributed.

Source IDs CLR-SRC0001..CLR-SRC0053 are allocated once against the current source bibliography; they are stable identity keys after allocation, not mutable display numbers. Future display renumbering retains identity; a replaced bibliographic work receives a different key with lineage. The original IEEE citation text is retained verbatim so metadata are not silently lost through partial parsing.

Concept support preserves the input classification: 44 direct notion pointers (D), 83 adaptations/theoretical bases (B), and 10 pending exact-passage supports (P). Each concept has at least two pointers, which do not establish independence, full-text review, correctness of its complete scoped definition or OntoUML typing approval. The source location text is inherited evidence, not a statement of fresh verification. All pending items remain pending.

Reconstruction order is `import_selected_model.py`, `import_orsd.py`, then `import_source_support.py` using authorized, digest-matching inputs. The last step adds bibliographic bindings to the imported concepts without changing their definitions/stereotypes. It must follow the model extractor; rerunning the original model extractor alone would remove these later bindings. Do not run the original-input pipeline over accepted future semantic edits: new source/model revisions require a controlled change record.

This is a preparation and provenance decision. No publication-rights grant, full literature verification, independent acceptance or semantic equivalence is inferred.
