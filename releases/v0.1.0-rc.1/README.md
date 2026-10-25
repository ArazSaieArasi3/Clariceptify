# Target RC station - engineering preparation only

No RC tag or GitHub Release is created by this directory. The target station is
v0.1.0-rc.1; the current local bundle is labelled `r1-preparation` and is not an RC.

[manifest.yaml](manifest.yaml) registers each actual source byte and distinguishes
the base commit from prepared working-snapshot additions/edits. It does not claim
that the entire payload is the base commit. The manifest is outside its own member
digest set, then included as a package envelope file; checksum files exclude themselves.
All private raw source files, external full texts, runtime caches and generated
package/report directories are excluded. Published alpha payloads are unchanged.

From the repository root:

```sh
python tools/build_release.py --output /tmp/clariceptify-preparation
python tools/readback_release.py /tmp/clariceptify-preparation/clariceptify-r1-preparation.zip
python tools/test_release_preparation.py
```

The builder/readback tool uses Python with requirements-dev.txt installed. Its
clean extraction is a fresh file tree with an empty HOME and the declared current
Python dependencies, not a newly provisioned OS or independent validation.

The license/creator proposals (#52/#53) remain proposals; root citation (#54),
final reading/limitations acceptance (#55/#56), final manifest/build/readback
(#57-#59), readiness (#60), RC publication (#61) and later acceptance/stable
publication (#62-#64) retain their own completion conditions. A preliminary
technical PASS cannot close those pending gates or grant rights.
