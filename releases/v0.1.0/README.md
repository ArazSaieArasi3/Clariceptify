# Accepted R1 baseline: v0.1.0

The actual owner accepted exact v0.1.0-rc.1 with its declared limitations on
2026-10-25. See [the decision](../../docs/decisions/r1-scope-acceptance.md) and
[scope disposition](../../evaluation/release/scope-disposition.yaml).

Stable promotion preserves the accepted scientific member bytes. Version,
publication/status documentation and reproducibility engineering have an explicit
version delta; no semantic, source, CQ or independent-expert state is promoted.
The RC and earlier releases remain immutable.

Actual publication: [v0.1.0](https://github.com/ArazSaieArasi3/Clariceptify/releases/tag/v0.1.0), 2026-10-25.
[Public readback evidence](../../evaluation/release/published-readback.yaml) verifies
all ten assets, nine checksum entries and eleven extracted checks. The final
manifest binds exact source commit 4b587ec12060d1ecd1b6a5bdbf8804dd44356766;
freeze/tag commit is def69ba04b472834bd1d37e567f77288128e6b90.
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
