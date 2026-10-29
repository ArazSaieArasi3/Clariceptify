# Cognitive Atlas: complete selected class and definition register

Issue #241. Selected `cogat.v2.owl` has formal header 0.3 and source SHA256 `701aa9e8351fcec3de0122df7ed49158cff83fe4e7353bd540122d8a34ce5fd8`.

| Population | Count |
|---|---:|
| Local declared named classes | 1696 |
| External class declarations | 2 |
| Local classes with nonempty source definition | 1232 |
| Empty definition annotations | 55 |
| No definition annotation | 409 |
| Local class IRIs with two source identifiers | 101 |

Every selected declaration appears in [classes.jsonl](cognitiveatlas/classes.jsonl), including all labels/identifiers, hierarchy, equivalence, constraints, annotation digests, provenance and explicit definition gaps. The [attributed definition register](cognitiveatlas/source-definitions.jsonl) preserves all available original wording, including empty fields and ambiguous records. It is a separately licensed CC-BY-SA 3.0 US content extract; it is not mass-generated paraphrase or a claim that all 1696 definitions were independently validated. Read its [attribution and license scope](cognitiveatlas/ATTRIBUTION.md).

The 101 mixed construct/contrast identifiers are retained as ambiguity, not assigned an arbitrary preferred identity. Missing text is never invented. These are 1696 local class IRIs, not the 2011 paper population of 904 terms or the live website population.

No declared imports occur. Referenced undeclared classes/properties and BFO/CogPO namespace hints are recorded separately in the [census](../../evaluation/related-work/cognitiveatlas/technical-census.json); they do not prove a foundational import or alignment.

The [technical review](artifacts/CognitiveAtlas.md) retains eight source-bound questions and actual profile/reasoner results. No Clariceptify scientific artifact or release changed.
