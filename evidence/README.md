# Source support

The [source register](source-register.yaml), [bibliography](bibliography.md) and [concept support](concept-support.yaml) preserve Stage-1 data from the frozen specification: 53 references and 137 concept-support records, including 44 D, 83 B and 10 P qualifications. P remains pending. Each concept retains at least two source pointers; pointer count does not prove independence, full-text verification or correct typing.

The [import representation decision](../docs/decisions/source-support-import.md) identifies the exact input and limits. The separately identified JSON ledger bytes have not been compared. Source locators and screening statuses are inherited, not freshly verified. Raw third-party full texts are not included.

Run `python tools/check_source_support.py`. For controlled re-import, the model import must precede `python tools/import_source_support.py INPUT.docx`; see the decision for the order and revision guard. New close-work research and full-text review remain separate tasks.
