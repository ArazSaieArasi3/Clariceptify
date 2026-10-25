# Native Wiki publication

The generated Markdown filename and the GitHub editor title have different
roles. Use the generated `wiki-title-map.json` when publishing. For example,
`Conceptual-Model.md` must have the native title `Conceptual Model`, producing
the controlled link slug `Conceptual-Model`. A literal hyphen in the native
title creates a different page whose canonical URL contains an encoded Unicode
hyphen. That page can have the correct body while the guide link is broken.

| Source file | Native title | Controlled Wiki slug |
| --- | --- | --- |
| Conceptual-Model.md | Conceptual Model | Conceptual-Model |
| Requirements-and-CQs.md | Requirements and CQs | Requirements-and-CQs |
| Research-Roadmap.md | Research Roadmap | Research-Roadmap |

Keep single-word titles and `_Sidebar`/`_Footer` unchanged. Rename an incorrectly
titled existing page through its native editor, preserving the controlled body;
do not create a second explanatory authority. After saving, follow the actual
Home/sidebar link, confirm the rendered destination, reopen its editor and
compare the complete body with the source. A successful save or body comparison
alone is not a navigation check.

The initial native publication exposed this naming defect for three pages.
The titles were corrected in place and all three controlled links then opened
their rendered pages. Their exact body readbacks still match the same frozen
source hashes. See [the actual receipt](../../evaluation/publication/wiki-readback.json).
