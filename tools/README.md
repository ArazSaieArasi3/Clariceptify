# Local checks and controlled input import

Install requirements-dev.txt and run, from repository root:

```sh
python tools/check_bootstrap.py
python tools/check_model_import.py
python tools/check_requirements.py
python tools/check_source_support.py
```

These checks need no private repository or raw document access. They check record/graph/contract integrity, not adequacy or independent acceptance. Reports live under evaluation/.

To reconstruct the selected input imports, obtain authorized digest-matching documents, install requirements-import.txt, and run import_selected_model.py, import_orsd.py, then import_source_support.py with their respective source DOCX paths. The final step restores qualified bibliographic bindings to concept records. This pipeline is for the frozen original input, not a way to overwrite later accepted semantic changes. See docs/decisions/source-support-import.md.

build_bootstrap_preview.py remains restricted to the previously approved alpha.1 snapshot and cannot silently publish a newer model under that tag.
