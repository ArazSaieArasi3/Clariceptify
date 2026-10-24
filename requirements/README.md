# Retrospective requirements baseline

The controlled input ORSD 0.1 is now imported: [30 functional](functional.yaml), [10 quality/delivery](quality.yaml), [30 CQs](competency-questions.yaml) and [eight future requirements/eight exploratory CQs](future.yaml). Original LR/LCQ identifiers, E/R/I origins, MUST/SHOULD priorities, release targets, positive AC and adverse NAC are preserved. [Scope/scenarios](scope-and-scenarios.yaml) retain the source framing, examples and review roadmap.

This ORSD was reconstructed after the conceptual model. Requirements remain proposed review obligations, satisfaction/acceptance not_assessed, queries not_executed and answers not_computed. Future SHOULD candidates target R2 and are not R1 closure conditions. Candidate concept witnesses/model links are separate traceability work; the presence of this catalogue does not show that any need has passed.

Run `python tools/check_requirements.py` for record and contract integrity. To reconstruct from authorized frozen input bytes, install requirements-import.txt and run `python tools/import_orsd.py INPUT.docx`; a changed input digest is rejected. The [integrity report](../evaluation/requirements-integrity.json) and [import report](../evaluation/orsd-import-report.json) describe the actual checks and their limits.
