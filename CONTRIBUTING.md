# Contributing

Use English for every repository-facing contribution, including issues, comments, pull requests, commit messages, files, diagrams, release notes and published documentation. Do not include Persian text or Persian/Arabic-script digits. Preserve source provenance through English descriptions and external pointers.

Read [the repository instructions](AGENTS.md), [artifact authority](docs/decisions/artifact-authority.md) and [release policy](docs/decisions/release-policy.md). Keep changes small, bind evidence to exact inputs, and distinguish candidate support from verified findings.

Before submitting, run:

```sh
python tools/check_repository_language.py
python tools/check_bootstrap.py
python tools/check_model_import.py
python tools/check_requirements.py
python tools/check_source_support.py
```

The language command inspects tracked and non-ignored untracked local file paths and UTF-8 text. It does not inspect binary document contents or GitHub discussions. Review those surfaces explicitly before publishing. Install `requirements-dev.txt` for the other checks. Their PASS results establish only their declared integrity scopes.
