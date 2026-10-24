# Selected conceptual-model registries

The candidate source is jointly defined by [domains](domains.yaml), [concepts](concepts.yaml), [associations](relations.yaml), [generalizations](generalizations.yaml) and [textual constraints](constraints.yaml). All records preserve source locators bound to the selected DOCX digest and remain candidate/not_executed where appropriate. Their initial counts are 21 domain rows (20 subjects + Foundations), 137 concepts, 174 associations, 122 generalizations and 24 constraints.

The [schemas](schema/) check record shape. Association multiplicities preserve the labels at the respective source/target ends of the input drawing, not derived OWL restrictions. Generalization is child to parent; unknown set completeness/disjointness stays unknown. Constraint referenced IDs are only lexical mention candidates requiring semantic review. Input IEEE reference display is preserved in concept notes; stable source bindings are a later task. The migration ledger retains historical IDs and unreviewed correspondence candidates.

Run `python tools/check_model_import.py` from repository root for offline structural checks. Controlled re-import requires the frozen source DOCX and `python -m pip install -r requirements-import.txt`, then `python tools/import_selected_model.py INPUT.docx`. The input is not redistributed here; obtain authorized bytes and verify the manifest digest first. A changed digest is rejected before writes. Do not manually patch generated registries and rerun this original-source importer: after an accepted semantic change, record a new model revision/change history and corresponding migration path.

No joint satisfiability, full OntoUML validity, requirement satisfaction or independent expert approval is established by this import.
