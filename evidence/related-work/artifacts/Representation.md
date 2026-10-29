# Representation 2025: bounded supplement formalism and artifact inspection

Issue #244. [Structured evidence](Representation.yaml), [dated discovery receipt](../../../evaluation/related-work/representation244/discovery.json) and [checker](../../../tools/check_representation244.py). The selected work is Mizoguchi and Borgo's [2025 article](https://journals.sagepub.com/doi/10.1177/15705838251337943), DOI `10.1177/15705838251337943`, plus its separate [ten-page publisher supplement](https://journals.sagepub.com/doi/suppl/10.1177/15705838251337943/suppl_file/sj-pdf-1-apo-10.1177_15705838251337943.pdf). The 16-page owner-supplied main PDF is pinned at SHA-256 `16db8e02cde831898224f0cf00600c7c8e30369e591c0acc3823806c200e733a`; publisher-byte parity is unestablished. The distinct 2021 *Towards* work is not substituted.

## Source and machine boundary

| Question | Checked state |
| --- | --- |
| Formal text | The publisher-linked A-C supplement has 49 labeled expressions and 41 tabulated predicate signatures, all previously indexed in the [paper dossier](../deep-reviews/CLR-RW-Representation/review.yaml). Eight source-bound formulas are selected here. The raw supplement bytes are not retained or hashed in this run. |
| Visual verification | Publisher PDF p.8 was inspected as an image for D11: the existential list names `o,r,p,p′` while the body uses `f` in `FORMOF` and `PATTERNFORFORM`. This **selected** glyph/quantifier observation is confirmed; the glyph fidelity of all other 48 expressions is not certified. No intended repair is attributed to the authors. |
| Executable distribution | No author-controlled, version-pinned machine implementation was identified in the [bounded discovery](../../../evaluation/related-work/representation244/discovery.json). FOL notation in the PDF is not a published OWL class file or theorem-prover input. This is not a universal absence statement. |
| Classes and license | Machine local/imported/referenced/deprecated/inferred class counts, definitions, namespace, syntax, direct imports and root license remain **unknown**, not zero. The publisher marks the article restricted access and states separate supplemental reuse terms for non-open-access works; no raw PDF is republished. |
| Foundation | DOLCE and YAMATO are illustrative host ontologies. Their exact editions and formal imports are not specified, and `SEMIABSTRACT`, mereology, pattern and satisfaction assumptions require a chosen host. Neither family supplies an accepted UFO alignment by name. |

## Eight commitments and local checks

| Formula | Supplement page | Bounded result |
| --- | --- | --- |
| Ax9 | A, p.2 | One form/content pair determines one encoding method; a different method for the same pair violates this axiom. |
| D1 and D2 | A, pp.2–3 | A representation relation uses form/content sum and encoding; OREO projects from that relation. This is separate from a physical copy. |
| T1 and T2 | A, p.3 | Distinct arguments and unique decomposition are author-stated theorems. Host sum and earlier axioms are needed; no proof was reproduced. |
| Ax15 | A, p.5 | Physical-pattern assignment is unique per entity in this predicate; the granularity of pattern and `FEATUREOF` needs host specialization. |
| D10 | A, p.7 | Content realisation requires a physical object or event satisfying content. It does not by itself encode a conceptual decision or a separate `SPECIFICATION` condition. |
| D11 | B, p.8 | The visually observed free `f` in the printed existential definition requires author clarification or an explicitly marked repair before executable use. |

The checker reproduces two satisfying and two violating **finite local records** for Ax9 and Ax15. These checks do not interpret the host mereology, all quantifiers, the complete 49-expression theory, or any OWL class hierarchy. A positive comparison case separates form F, content C, method M, their representation R and its physical copy B. An adverse case gives the same F/C two distinct methods; a second one assigns two distinct patterns to one medium. No theorem prover, OWL profile, author proof reproduction or expert validation was run.

## Contribution to #255 and #126

The form/content/encoding and physical-realisation distinctions are substantial overlap with Clariceptify's representation concerns, so the eventual gap statement must preserve them as counterevidence. The selected text does not establish a tested, person-indexed record of conceptual choice, evidence, rationale and revision. The [candidate IDs and explicit limits](Representation.yaml) are questions for comparison #255 and final synthesis #126. No equivalence, direct import or change to the R1 model, requirements, fixtures, manuscript or release is accepted.
