# Accepted R1 baseline: v0.1.0

The actual owner accepted exact v0.1.0-rc.1 with its declared limitations on
2026-10-25. See [the decision](../../docs/decisions/r1-scope-acceptance.md) and
[scope disposition](../../evaluation/release/scope-disposition.yaml).

Stable promotion preserves the accepted scientific member bytes. Version,
publication/status documentation and reproducibility engineering have an explicit
version delta; no semantic, source, CQ or independent-expert state is promoted.
The RC and earlier releases remain immutable.

A directory is not publication. The final manifest will bind one exact committed
source snapshot; publication/readback evidence establishes actual issuance.
Its own bytes are supplied by the freeze commit as an envelope, outside its own
source-member hash set. The Git tag points to that freeze/publication commit.
The registered payload source commit is separate and explicit.

To rebuild, obtain the exact source commit and trusted manifest named by the
freeze record, install requirements-dev.txt, and run:

```sh
python tools/build_release.py --root /path/to/exact-source --manifest /path/to/trusted/manifest.yaml --output /tmp/clariceptify-stable
python tools/readback_release.py /tmp/clariceptify-stable/clariceptify-v0.1.0.zip --manifest /path/to/trusted/manifest.yaml
python tools/check_stable_promotion.py
```

Eleven checks run on fresh extraction with declared installed dependencies.
Optional CFF date-released is omitted; the actual GitHub Release record supplies
the publication date. No DOI is assigned. Refer to the declared limitations
before drawing scientific conclusions; stable denotes the accepted baseline.
