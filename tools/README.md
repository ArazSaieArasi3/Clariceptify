# Local checks and controlled input import

Install requirements-dev.txt and run, from repository root:

```sh
python tools/check_repository_language.py
python tools/check_bootstrap.py
python tools/check_model_import.py
python tools/check_requirements.py
python tools/check_source_support.py
python tools/check_trace_contracts.py
```

These checks need no private repository or raw document access. They check record/graph/contract integrity, not adequacy or independent acceptance. Reports live under evaluation/.

To reconstruct the selected input imports, obtain authorized digest-matching documents, install requirements-import.txt, and run import_selected_model.py, import_orsd.py, then import_source_support.py with their respective source DOCX paths. The final step restores qualified bibliographic bindings to concept records. This pipeline is for the frozen original input, not a way to overwrite later accepted semantic changes. See docs/decisions/source-support-import.md.

build_bootstrap_preview.py remains restricted to the previously approved alpha.1 snapshot and cannot silently publish a newer model under that tag.

The language guard checks current file paths and UTF-8 text for Arabic/Persian script. It does not inspect remote issue/PR/release content, history or binary artifacts; check those before posting. See CONTRIBUTING.md and AGENTS.md.

`build_artifact_register.py` rebuilds the declared storage snapshot plus its hash-bound publication receipt. Stable IDs are explicit mappings; update locators without reallocating IDs. `check_trace_contracts.py` checks the snapshot and initial edge schema, including negative integrity/claim cases; it does not claim a complete generated graph.

For the historical alpha.2 builder use commit b0edfdcb99e283eadce94ba11535d8179dbd1f04. The current baseline builder is restricted to the alpha.2.1 correction; it does not replace published assets.
