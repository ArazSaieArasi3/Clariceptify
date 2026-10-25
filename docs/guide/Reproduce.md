# Reproduce the baseline

Use the [v0.1.0 release](https://github.com/ArazSaieArasi3/Clariceptify/releases/tag/v0.1.0)
and its trusted source manifest. The payload source commit and separate freeze/tag
commit are recorded in [stable instructions](../../releases/v0.1.0/README.md).

```sh
python -m pip install -r requirements-dev.txt
python tools/run_integrity.py --output /tmp/clariceptify-integrity
python tools/test_release_preparation.py
```

Run exact frozen-package commands against its declared source commit, not a later
main snapshot. A new documentation check on current main is not retroactive
execution by the older frozen release. Source bytes, validator versions, runtime,
method and applicability belong to each result.

The public checks do not require private raw documents. Clean readback verifies
membership/checksums before extraction and runs the declared checks with an empty
HOME and installed declared dependencies. It is not independent expert review.

The documentation build uses requirements-docs.txt and tools/build_documentation.py.
Wiki and HTML are generated from the same curated guide; the publication manifest
identifies current and frozen sources. Preparing output is not actual deployment.
