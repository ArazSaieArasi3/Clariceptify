# Related-work execution and reproduction

## Executed first family review

The current [review index](review-index.yaml) overlays the unchanged historical
candidate register and protocol seed states. See [the bounded comparison](../../docs/research/dns-family-comparison.md).
Three paper/embedded-documentation reviews and three separate artifact inspections
are recorded. The 2016 DUL chapter remains a partial access-gap review; technical
inspection of DUL 4.2 does not complete its paper prerequisite.

Install `requirements-research.txt` alongside the development requirements to
reproduce artifact counts. Download the exact official URLs named in
[artifact-inputs.yaml](artifact-inputs.yaml) to a directory outside the repository,
using the registered filenames, then run:

```bash
python tools/inspect_related_artifacts.py --source-dir /path/to/third-party-inputs --output-dir /tmp/clariceptify-inspections
python tools/check_related_reviews.py
python tools/test_related_reviews.py
```

The inspector checks exact source hashes, parses the specified syntax, resolves
only the pinned local imports, separates local and closure populations and emits
selected asserted logical axioms. A changed upstream resource fails the pinned
check. It does not run a reasoner or infer redistribution permission. Original
PDFs/OWL files and their full annotation corpora are not distributed here.
