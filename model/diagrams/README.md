# Diagram source and approval evidence

The historical Conceptiom vector master has been recovered and hash-bound in [source-manifest.yaml](source-manifest.yaml). It is an editable SVG with 137 named concept groups and 296 named relationship groups, not a recovered native OntoUML project. The historical generator is unknown. Its one-page full PDF and 45-page A3 atlas are separately fingerprinted; common delivery does not prove exact regeneration or visual parity. Raw originals remain outside this public repository under the migration distribution policy.

[approval-state.yaml](approval-state.yaml) distinguishes authorization to draw the diagram from scientific acceptance. The source specification says review candidate; an unsupported approval adjective in SVG accessibility metadata must not elevate that state. The originals remain unchanged. A versioned corrected derivative, full/detail views and element-level/visual verification are the separate issues #43, #44 and #45.

Model registries remain the semantic authority. Do not correct or reinterpret the model only inside the diagram. Recovery and structural correspondence do not establish native OntoUML validity or expert approval.

Run `python tools/check_diagram_sources.py` to check the public source/approval contracts. With authorized recovered originals, add `--inputs /path/to/input-directory` to verify all four exact hashes and the XML/DOCX evidence. The stored [source audit](../../evaluation/diagrams/source-approval-check.json) records an actual private-input check; a later public-only invocation reports that input audit as not run. These checks also passed under Python optimization; altered source bytes were rejected in both modes.
