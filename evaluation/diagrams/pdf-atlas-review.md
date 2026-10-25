# PDF and atlas generation review - R1-025.b

Input baseline: `cc2a75c09ad2065bebbd11749a5a291742a6a6c1`.
The exact current `diagram-r1.1` SVG and five model registry digests are
recorded with the renderer and output hashes in [pdf-atlas-build.json](pdf-atlas-build.json).

## Delivered views

- `model/diagrams/generated/full.pdf`: one vector page preserving the original
  9974 by 3919 point canvas. This is the zoomable overview, not a paper reading view.
- `model/diagrams/generated/atlas.pdf`: 69 exact A3 landscape pages: one linked
  overview, 66 row/column detail tiles at 1:1 source scale and two reading-note pages.
  Adjacent windows overlap by 240 points horizontally and 96 points vertically.
  Headers identify source windows; footers identify adjacent tiles. Print at actual size.
- The appendix repeats the original legend descriptions and reading notes with
  line wrapping because long source sentences can cross detail-window boundaries.
  It adds no new conceptual definitions or acceptance claims.

## Actual checks

- The current SVG/registry correspondence audit passed for all 137 concepts and
  296 ordered relationships before PDF rendering.
- Both PDFs reopened successfully. All 69 atlas pages have text and measure
  420 by 297 mm within 0.001 point numerical tolerance.
- Overlapping windows cover the entire source canvas, including the legend.
- Both PDFs contain zero raster image objects; text remains selectable and the
  geometry remains vector-based. Both outputs were rebuilt a second time and
  their SHA-256 digests were identical.
- Rendered the complete atlas contact sheet and inspected the overview, first
  tile, tiles R02 C07 and R04 C05, final tile and both appendix pages. Labels,
  colors, triangle geometry and navigation survived in these samples. Cropped
  detail-window boundaries are intentional and have overlapping neighboring views.

## Limits and next gate

This closes PDF/atlas generation only. It does not close issue #45's exhaustive
element visibility, visual correspondence, text proximity and occlusion review.
Dense crossings and any pre-existing source layout limitations remain visible;
the renderer does not reroute or reinterpret them. No native OntoUML validation,
semantic acceptance, human approval or exact historical PDF regeneration is claimed.

The source SVG, conceptual registries, approval states and published alpha payloads
are unchanged. The original historical PDFs stay private under the migration policy.

Reproduce with `python tools/build_diagram_pdfs.py` after installing
`requirements-diagrams.txt` (PyMuPDF 1.26.6).
