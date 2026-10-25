# R1 candidate station

The target is v0.1.0-rc.1, a prerelease, not a stable release. Directory presence
is not publication. The prior preparation manifest remains historical until
replaced by the exact committed-source candidate inventory in the freeze step.

The final [manifest](manifest.yaml) registers each distributable source byte,
Git blob identity, license scope and artifact revision against one exact source
commit. Its own bytes are included separately as a package envelope, outside
the source-member digest set. SHA256SUMS excludes itself. Private raw inputs,
third-party full texts, external applications, font programs and caches are
excluded. Published alpha payloads are immutable.

Install requirements-dev.txt, obtain the source commit named in the final
manifest and the trusted manifest from the freeze commit, then run:

```sh
python tools/build_release.py --root /path/to/frozen-source --manifest /path/to/trusted/manifest.yaml --output /tmp/clariceptify-rc
python tools/readback_release.py /tmp/clariceptify-rc/clariceptify-v0.1.0-rc.1.zip --manifest /path/to/trusted/manifest.yaml
python tools/test_release_preparation.py
```

The builder rejects stale members and unregistered RC identities. Readback
checks exact membership/digests before fresh temporary extraction and runs all
declared public checks with an empty HOME, no Git/private source access and
installed declared Python dependencies. This is not a new OS or expert review.

The owner approved research CC-BY-4.0, code MIT and the three creators/order.
Root CITATION.cff describes this candidate source and omits an unissued
publication date and DOI. Actual publication time belongs to the GitHub Release
record. A byte-identical archive can be rebuilt without altering frozen metadata.

#62 records actual acceptance of the exact candidate after #61 publication;
#63/#64 remain stable publication and its public readback. The license/creator
instruction does not count as early acceptance of this future package.
