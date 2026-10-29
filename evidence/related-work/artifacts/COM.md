# COM 2004: bounded formalism and artifact inspection

Issue #243. [Structured evidence](COM.yaml), [dated discovery receipt](../../../evaluation/related-work/com243/discovery.json) and [reproducible checker](../../../tools/check_com243.py). The primary work is Ferrario and Oltramari's *Towards a Computational Ontology of Mind*, FOIS 2004, an 11-page [institutional author PDF](https://www.loa.istc.cnr.it/old/Papers/focomf2.pdf), SHA-256 `16bce2d1a344a7cd1717f0f28b5b7fd94ee1f151ebea632f5b9f3593c187b245`. The [complete paper dossier](../deep-reviews/COM2004/review.yaml) keeps the separate same-title 2005 Aerospace work out of these counts and claims.

## Artifact and class boundary

| Dimension | Exact checked state |
| --- | --- |
| Formal source | No author-controlled COM 2004 executable root, repository commit, machine syntax, IRI namespace, declared import closure or file license identified within the [bounded searches](../../../evaluation/related-work/com243/discovery.json). This does not assert that no such distribution exists. |
| Paper population | 50 Figure 1 categories, including 11 typographically marked COM additions; 80 ontology-bearing paper catalog entries and 20 D/A-labeled printed formulas. Eight formulas are inspected here. These are **paper counts**, not OWL/FOL machine declarations. |
| Machine population | Local, imported, referenced, deprecated and inferred classes; machine properties; definition availability and a complete selected-root glossary are all **unknown**, not zero. No purported class IRI or generated definition is supplied. |
| Foundation | DOLCE family is explicit in the paper, including its reference to 2002 D17. The exact edition, 2004 machine import and correspondence remain unknown. The [current official DOLCE page](https://www.loa.istc.cnr.it/index.php/dolce/) links a newer OWL repository; this does not supply a COM release. |
| Execution | Eight exact paper locators and two local Boolean fragment checks are reproduced. No COM root parse, OWL profile, whole-theory solver or author experiment was run. |

The institutional publication entry and paper were checked again alongside four public web queries and bounded connected GitHub repository/code searches on 2026-10-29. Only paper/metadata, citations and an unrelated modern DOLCE release were identified. The earlier [discovery receipt](../../../evaluation/related-work/com/deep-review-discovery.json) distinguishes Drammar's citation of the 2005 work from original COM bytes. Search limits and date are retained; there is no inferred universal absence or source license.

## Eight source-bound commitments

| Paper formula | Exact locator | Bounded finding |
| --- | --- | --- |
| D1 | `COM2004:E07`, PDF p.6 | Necessary existence implication gives self-dependence when `y=x`, absent a printed inequality guard. |
| D4 | `E08`, PDF p.6 | The percept exclusion quantifies over any mental object, including itself under literal D1. |
| D6 | `E10`, PDF p.7 | Computed belief's direct historical percept predecessor inherits the percept concern. |
| D9 | `E10`, PDF p.7 | Aboutness is an agent–state–object–time relation using ownership and simultaneous participation. |
| D11/D12 | `E11`, PDF pp.7–8 | Belief/desire state classes arise from respective object witnesses; co-participation alone does not enforce exclusive state labels. |
| D14 | `E11`, PDF p.8 | Printed `PER` differs from `PES` in D10 and Figure 1; no silent correction is made. |
| A5 | `E14`, PDF p.9 | Agent presence requires an owned present computed belief; it is only a necessary condition. |

One locally coherent **D9 fragment** has agent `a`, state `s` and private object `z` co-participating at `t`, with `z` owner-dependent on `a`. It illustrates the intended aboutness tuple without claiming to satisfy the entire printed theory. In the adverse fragment, D1's `□(P→P)` makes `GED(x,x)` true for any presence pattern, and D4 bars a percept for a mental object `x`. Independently, if two differently typed, owned objects co-participate in `s`, D9 with D11/D12 can classify `s` as both belief and desire. These are local conditional arguments, not a solver verdict on the whole theory or a statement that object types overlap.

## Use in comparison and synthesis

The agent, private mental object, state and time roles are promising **comparison questions** for #255, anchored to existing Clariceptify IDs in the structured review. A native, tested record of a dated conceptual decision with evidence, rationale and revision is not established by these eight formulas, while COM's agent-indexed aboutness is positive contrary evidence against any blanket claim of absent agency. #126 must retain both facts. Formal import, equivalence and model changes require a separately identified source and owner decision. No R1 scientific artifact, manuscript or release was changed.
