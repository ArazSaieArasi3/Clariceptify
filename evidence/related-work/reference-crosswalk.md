# Retained reference collection

This index preserves all 24 rows of the owner-designated reference collection without overwriting later research. It maps 19 original candidates, the already imported LION source, and four supplementary theoretical/methodological leads. It does not imply 24 distinct implemented ontologies, complete reading, or article inclusion.

- Machine-readable index: [reference-crosswalk.yaml](reference-crosswalk.yaml).
- Four additional leads: [supplemental-reference-register.yaml](supplemental-reference-register.yaml).
- Current review authority: [deep-review register](deep-reviews/register.yaml) and its linked dossiers. Historical candidate/access statuses are not substitutes for this authority.
- Frozen imported bibliography: [source register](../source-register.yaml). LION is CLR-SRC0014; SKOS also crosslinks CLR-SRC0039. Do not duplicate these identities.

| Collection row | Source | Canonical ID |
|---|---|---|
| 1 | Epistemic Foundational Ontology (EFO) | CLR-RW-EFO |
| 2 | Constructive Descriptions and Situations (c.DnS) | CLR-RW-cDnS |
| 3 | Conceptualization.owl | CLR-RW-DULConceptualization |
| 4 | DOLCE+DnS Ultralite (DUL) | CLR-RW-DUL |
| 5 | Linguistic Meta-Model (LMM) | CLR-RW-LMM |
| 6 | An Ontology of Representation | CLR-RW-Representation |
| 7 | Conceptual Model Ontology (CMO) | CLR-RW-CMO |
| 8 | Ontology for Ontological Analysis (O4OA) | CLR-RW-O4OA |
| 9 | Computational Ontology of Mind (COM) | CLR-RW-COM |
| 10 | Information and Discourse Acts (I&DA) | CLR-RW-IDA |
| 11 | Descriptions and Situations (DnS) | CLR-RW-DnS |
| 12 | OntoKADS | CLR-RW-OntoKADS |
| 13 | Foundations for an Ontology of Belief, Desire and Intention | CLR-RW-BDI |
| 14 | DOLCE Mental States and Needs | CLR-RW-DOLCEMental |
| 15 | Information Artifact Ontology (IAO) | CLR-RW-IAO |
| 16 | OntoLex-Lemon | CLR-RW-OntoLex |
| 17 | SKOS | CLR-RW-SKOS |
| 18 | Emotions & Cognition Ontology | CLR-RW-EmotionsCognition |
| 19 | Cognitive Atlas | CLR-RW-CognitiveAtlas |
| 20 | A Plea for Epistemic Ontologies | CLR-RW-PleaEpistemic |
| 21 | Ontologies epistemiques vs referentielles | CLR-RW-EpistemicReferential |
| 22 | Foundations for a Realist Ontology of Mental Representation | CLR-RW-RealistMentalRepresentation |
| 23 | Linguistic and Ontological Concept Formation: The LION Method | CLR-SRC0014 |
| 24 | Concepts in Context: Ontological Coherence in Political Science Research | CLR-RW-ConceptsInContext |

## Use in later articles

The four supplementary entries are unreviewed source leads (`not_assessed`), not citation-ready claims. Verify bibliographic identity/access, read the intended source version, and record page/section evidence before deciding inclusion or making comparisons. The two-page Plea extended abstract must not stand in for the full article. The French epistemic/referential paper is not an executable ontology. Source registration neither rewrites a manuscript nor changes any ontology axiom.

Related families and versions stay distinct: DnS/cDnS/DUL/Conceptualization; cDnS 2007/2008; BDI 2020/later preprint; EmotionsOnto2014/Emotions-2015. Consult current dossiers for version-specific limits. No historical size estimates or old comparison judgments are promoted here.

## Validation

Run `python tools/check_reference_crosswalk.py`. This checks the 24-row reconciliation, canonical IDs and crosslinks, supplementary status boundary, public locator hygiene, and nonduplication with the frozen bibliography. It does not verify publications or scientific conclusions.
