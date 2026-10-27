# Towards an Ontology for Conceptual Modeling

Work: `CMO` | Issue: #83 | State: `REVIEW_COMPLETE`

Reviewed version: ICBO2011, CEUR-WS833, pp.191-199;9-page proceedings PDF. Input: `CMO.pdf`, 9 PDF pages, SHA256 `344fde1855db6b10dbc56d66874543163f75620d8d8b82078bee15db72b1ce49`.

The structured `review.yaml` is the evidence authority; this report is derived. This is an AI-assisted critical review, not independent expert acceptance. Clariceptify is unchanged; later use requires an owner decision.

## Identity and reading coverage

Exact9-page proceedings work, conference 2011 and proceedings copyright/publication2012 kept separate. Printed page = PDF+190. Complete sections1-8 plus 2.1, six figures, five numbered content footnotes and 37 references. No table, appendix or numbered mathematical formula. The alternate differently paginated author-uploaded version was not substituted; in this selected work concepts are explicitly called Level 2 entities. PDF metadata names Sandra Smith as technical author, which is not substituted for the three visible scholarly authors. No DOI established in the checked primary proceedings metadata.

Defective embedded-font text extraction was not accepted as reading. All 9 pages OCR recovered, read in column order and visually inspected. All six figures, query text, chart labels, rule arrows, five footnotes and 37 references covered. diagrams.yaml separates class boxes, property labels, query/chart items and rule variables. Complete paper catalog and seven-local-class third-party candidate are distinct populations; original author release/imported glossary remains unknown.

| Paper unit | Coverage | Evidence |
|---|---|---|
| Title/authors/abstract and sec.1 Introduction | REVIEWED | E01 |
| Sec.2 Background, Levels1-3, two goals and footnote 1 | REVIEWED | E02 |
| Sec.2.1 Relevant Ontologies and Frameworks | REVIEWED | E03 |
| Sec.3 three use cases; footnotes 2-4 | REVIEWED | E04 |
| Sec.3 all five requirement headings | REVIEWED | E05 |
| Sec.4 all core/descriptive definitions, footnote 5 and metamodel argument | REVIEWED | E06, E07 |
| Figs.1-2 category hierarchy and all properties | REVIEWED | E07 |
| Sec.5 Implementation, including continuation above Fig. 1 | REVIEWED | E08 |
| Sec.6 Evaluation; Figs.3-4 query and nine-bar chart | REVIEWED | E09 |
| Sec.6 Figs.5-6 rule patterns and requirement claims | REVIEWED | E10 |
| Sec.7 Future Work, continuing after figure page | REVIEWED | E11 |
| Sec.8 Conclusion | REVIEWED | E12 |
| References1-37, including split reference 19; no tables or appendices | REVIEWED | E13 |

## Common review dimensions

### D1_identity_coverage

Pin the exact nine-page proceedings source and all content units. OCR was only a reading aid; every page and small diagram/query label was visually checked. Conference2011, proceedings 2012, PDF technical metadata and other layouts are not interchangeable identities. [REVIEWER_INTERPRETATION; E01, E13]

### D2_problem_contribution

CMO seeks conceptual interoperability through a reusable vocabulary layer over logical models without unintended baseline inference. Its contribution includes a metamodel and swBIG prototype. This directly overlaps conceptualization knowledge; universal correctness/noninterference is not proved. [REVIEWER_INTERPRETATION; E01, E02, E08, E12]

### D3_method

Requirements derive from prior caBIG-to-OWL modeling difficulties. BFO/IAO/SKOS reuse, OWL2 punning, conceptual annotations and an application proxy form the method. No systematic elicitation sample, full construction protocol or independent evaluation design is reported. [REVIEWER_INTERPRETATION; E03, E05, E06, E08]

### D4_requirements

All three author use cases and five requirements are retained below, with patient/search, clinical-date/vital-status and BRIDG examples. Examples are not a comprehensive CQ benchmark; application-dependent alignment fidelity requires an explicit policy. [REVIEWER_INTERPRETATION; E04, E05, E09, E10]

### D5_concepts

Catalog all ontology-bearing distinctions, eight prose/diagram CMO category names, reused foundation categories, logical/physical/lexical layers, permissible-value concepts and rule variables. Figure1 has seven local class labels, while FiatEntity is additional prose content. Neither number is the complete original distribution census. [REVIEWER_INTERPRETATION; E02, E06, E07, E08, E10]

### D6_relations_formalization

Record every visible property and all inverses/subproperties/signatures, the printed query, and both mapping patterns. Separate class hierarchy, concept hierarchy, punning and inference-rule policy. No numbered mathematical displays occur. Shared concept anchors alone do not prove class subsumption. [REVIEWER_INTERPRETATION; E06, E07, E09, E10, S01, S02]

### D7_grounding

BFO family and IAO reuse are explicit, not inferred from a citation. Paper edition unknown; bfo2 prefix is not an edition identifier. Candidate uses actual BFO1.1 namespace IRIs but imports only unversioned IAO/SKOS endpoints. GenericallyIndependentContinuant in Fig. 1 conflicts with dependent terminology in prose and is preserved, not repaired. [REVIEWER_INTERPRETATION; E03, E06, E07, A01]

### D8_artifact_correspondence

Official paper PURL redirects to a Google Code SVN file returning 404. A pinned third-party DBpedia tracker candidate matches the CMO namespace and several paper terms; original 2011 byte/axiom identity is not established. All 12 declared named classes and 20 object properties are inventoried, all seven local class definitions/constraints manually reviewed below. Imports, original missing terms and selected semantic execution remain #245. [REVIEWER_INTERPRETATION; A01, E06, E07, E10]

### D9_evaluation

Authors show query/result and two mapping diagrams as evaluation. They provide no identified expert sample, controlled accuracy/precision/recall or reasoner/profile log. A current parser rejects the literal printed query; this syntax-only result does not refute an undocumented historical dialect or reproduce its dataset. Five VVEAA functions remain distinct. [REVIEWER_INTERPRETATION; E09, E10, E12, S01]

### D10_critical_synthesis

Positive prior coverage includes conceptual/logical/real separation, vocabulary-mediated interoperability and task-specific conversion/mapping. Limits include implicit policy, unsupported granularity, foundation/version discrepancies and missing reproducibility. All proposed uses remain owner-deferred. [REVIEWER_INTERPRETATION; E02, E05, E06, E10, E11, A01]

## Conceptual catalog

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| C01 / Level 1 reality | Objects/processes/qualities/states in reality; paper then describes realist logical classes/properties at this level. Distinguish universal, class and instance interpretation. | REVIEWER_INTERPRETATION; E02, E06 |
| C02 / Level 2 cognitive representation | Paper treats conceptual models and CMO concepts as Level 2; later asserting SKOS concepts under IAO information-content category raises a modeling-level grounding question, not an automatic identity of mental act and information artifact. | REVIEWER_INTERPRETATION; E02, E06, E07 |
| C03 / Level 3 representational artifact / term | Textual/graphical concretization and lexicographic labels; label string is not identical to the concept or represented thing. | REVIEWER_INTERPRETATION; E02 |
| C04 / Conceptual model | Set of Level 2 entities representing Level 1 or Level2 classes/properties; model members may also have separate logical-model roles. No complete ConceptualModel class declaration is shown. | REVIEWER_INTERPRETATION; E02, E06 |
| C05 / Logical model | Collection of classes/properties from Level 1 or 2; distinguish extensional class interpretation from concept-individual use of a shared name. | REVIEWER_INTERPRETATION; E02, E06 |
| C06 / Physical model | Implementation-layer representation mentioned in the introduction; not developed as a separate formal class family in this paper. | REVIEWER_INTERPRETATION; E01 |
| C07 / Common vocabulary | Reusable term/concept system kept distinct from an individual conceptual/logical model to avoid privileging one source. Common anchors provide candidates, not guaranteed equivalence. | REVIEWER_INTERPRETATION; E02, E05 |
| C08 / Conceptual interoperability | Interoperation intended to match human conceptual alignment, through search, conversion and mapping. Alignment fidelity is a task-dependent premise. | REVIEWER_INTERPRETATION; E02, E04, E10 |
| C09 / cmo:Type | Conceptual generalization associated with a collection of instances; it is an idea-of-type rather than automatically the represented class or one of its members. | REVIEWER_INTERPRETATION; E06 |
| C10 / cmo:Quality | Conceptualized inherent property or assigned attribute; source deliberately groups these. This is not automatically a BFO quality or OWL property. | REVIEWER_INTERPRETATION; E06 |
| C11 / cmo:Relation | Conceptual relation between independent entities; endpoints are expressed through Type role links. Not an executable RDF predicate solely from its class label. | REVIEWER_INTERPRETATION; E06, E07 |
| C12 / cmo:Universal | Realist-side category, prose grounded under independent continuant; punning/class-versus-individual commitments need exact semantics. | REVIEWER_INTERPRETATION; E06, E07 |
| C13 / cmo:UniversalClass | Fig. 1 Universal subtype; candidate comment describes natural groupings and its minQualifiedCardinality0 restriction imposes no positive representation witness. | REVIEWER_INTERPRETATION; E07, A01 |
| C14 / cmo:UniversalQuality | Fig. 1 Universal subtype; candidate has no rdfs:comment but has a descriptive rdfs:seeAlso literal. Do not label all source definition text absent or silently invent a comment. | REVIEWER_INTERPRETATION; E07, A01 |
| C15 / cmo:UniversalRelation | Fig. 1 Universal subtype for real-side relations; distinguish from conceptual cmo:Relation and punned OWL object property. | REVIEWER_INTERPRETATION; E07, A01 |
| C16 / cmo:FiatEntity | Explicit prose category under generically dependent continuent; absent fromFig.1 and the selected mirror. Absence in that file is not absence in the paper or all historical sources. | REVIEWER_INTERPRETATION; E06, E07, A01 |
| C17 / skos:Concept | Common conceptual/vocabulary entity, source asserted under IAO information content entity. New foundation typing can affect other SKOS-typed individuals when combined, so noninterference requires a scoped proof. | REVIEWER_INTERPRETATION; E06, E07, A01 |
| C18 / iao:information content entity; iao:is about | Information-content category and aboutness predicate reused for CMO concepts/represents. A representational content item is not automatically a cognitive episode or truth guarantee. | REVIEWER_INTERPRETATION; E03, E06, E07 |
| C19 / bfo2:Entity; snap:Continuant; snap:IndependentContinuant | Printed foundation nodes above Universal; bfo2 is a prefix name and does not prove BFO2. Candidate IRIs explicitly use ifomis.org/bfo/1.1. | REVIEWER_INTERPRETATION; E07, A01 |
| C20 / snap:GenericallyIndependentContinuant / generically dependent continuent | Preserve conflicting figure/prose strings. Figure1 sends the printed independent category under IndependentContinuant; do not publish this as a verified BFO hierarchy. | REVIEWER_INTERPRETATION; E06, E07 |
| C21 / OWL class / individual / property; punning | Same IRI can be used at different entity levels; source metamodel argument requires explicit bridge policy. Assigning skos:Concept to the individual facet does not automatically transfer class-extension facts. | REVIEWER_INTERPRETATION; E06, S02 |
| C22 / Self-representation / concept versus represented thing | Source permits concept/class self-representation but rejects universal self-representation. These are ontological claims; the mirror explicitly makes representsUniversal irreflexive only. | REVIEWER_INTERPRETATION; E02, E06, A01 |
| C23 / Concept composition / primary concept / qualifier | Tissue Specimen example uses Specimen primary anchor and Tissue qualifier. This decomposition lacks a generally specified compositional identity, qualifier order or inverse reconstruction. | REVIEWER_INTERPRETATION; E07 |
| C24 / Conceptual quality values / permissible concepts | valuesCanBe relates Quality to permissible conceptual values; CDE conversion uses an OWL enumeration range of concepts rather than raw strings. Graph linkage alone is not a closed value validator. | REVIEWER_INTERPRETATION; E07, E08 |
| C25 / Source/target roles / generic relation role | Conceptual Relation-to-Type links and inverses. No displayed cardinality makes every relation binary, uniquely sourced/targeted, total or directionally symmetric. | REVIEWER_INTERPRETATION; E07 |
| C26 / UML generalization / attribute / association | Input-model structures claimed preserved by swBIG conversion. Prior one-to-one attribute/property mapping failure motivates the separation; preservation is not formally verified here. | REVIEWER_INTERPRETATION; E03, E08 |
| C27 / CDE / semantic metadata | Common Data Elements supply conceptual annotations and permitted values. Their version, curation policy and mappings affect data correctness; no complete snapshot supplied. | REVIEWER_INTERPRETATION; E08 |
| C28 / swBIG / caBIG / caGrid | Prototype linked-data proxy, originating biomedical infrastructure and service calls. These are implementation architecture, not additional invented CMO ontology classes. | REVIEWER_INTERPRETATION; E03, E08 |
| C29 / NCIt / SKOS conversion / OWLtoSKOS | Vocabulary transformation supports concept-individual queries; loss of logical semantics or alignment provenance must be assessed, not inferred correct from successful conversion. | REVIEWER_INTERPRETATION; E08 |
| C30 / GEO / ArrayExpress / caArray; MAGE / MIAME | Author motivating resources/models with overlapping conceptual content; no actually reproduced multi-resource search/conversion experiment is reported. | REVIEWER_INTERPRETATION; E02 |
| C31 / HL7-RIM / PML / domain-specific model | Cross-cutting clinical/provenance model examples and interoperability targets; these are not established equivalents or necessarily imported ontologies. | REVIEWER_INTERPRETATION; E02, E04 |
| C32 / Search / query | Author use case hides logical-model details behind common concepts; education and adverse-event examples provide functional motivation, not exhaustive recall guarantees. | REVIEWER_INTERPRETATION; E04, E09 |
| C33 / Conversion / fidelity | Task-selected data translation, including Clinical Service on a Date to an Alive-status record on that Date. Requires event/date/subject evidence and explicit fidelity policy. | REVIEWER_INTERPRETATION; E04, E10 |
| C34 / Direct mapping / BRIDG / AIM Person | Vocabulary-mediated generation of model relationships; a shared NCIt Person anchor is not proof that two class extensions coincide or one contains the other. | REVIEWER_INTERPRETATION; E04, E10 |
| C35 / Person / Education Level / HINTS2005 | Query/example domain roles and dataset. Fig. 4 contains nine education categories; these labels are not newly declared CMO classes. | REVIEWER_INTERPRETATION; E09 |
| C36 / Clinical Service / Date / Vital Status / Alive | Conversion scenario predicates/concepts; temporal and evidential adequacy of inferred Alive requires task-specific guards, not merely concept similarity. | REVIEWER_INTERPRETATION; E04 |
| C37 / Tissue Specimen / Specimen / Tissue; Adverse Event / Drug class | Search/composition illustrations and type-of-drug abstraction. They do not establish corresponding actual CMO class declarations. | REVIEWER_INTERPRETATION; E04, E07 |
| C38 / Bird / flying / flightless / injured | Concept-level defeasible-sounding association without automatic class entailment; this does not implement a default logic, exceptions policy or validated biological rule. | REVIEWER_INTERPRETATION; E10 |
| C39 / Common Vocabulary requirement | Separate portable vocabulary must not favor one particular conceptual/logical representation. | REVIEWER_INTERPRETATION; E05 |
| C40 / Distinction from Logical Models requirement | Separate metamodel roles to prevent idea-of-thing versus thing-instance conflation. Expressing both in OWL does not alone invalidate the distinction if entity roles are explicit. | REVIEWER_INTERPRETATION; E05, E06 |
| C41 / Natural, Idiomatic Expression requirement | Annotation should preserve natural logical/data representation without requiring baseline modifications. This is a scoped noninterference goal, not a proved conservative extension. | REVIEWER_INTERPRETATION; E05, E10 |
| C42 / Types, Properties, and Relations requirement | Represent conceptual structure and its relations across the relevant modeling roles, not only class names. | REVIEWER_INTERPRETATION; E05, E07 |
| C43 / Additional Relationships requirement | Allow extra concept relationships as appropriate for interoperability. No automatic logical-class inference is intended solely from all such relationships. | REVIEWER_INTERPRETATION; E05, E10 |
| C44 / Granularity / reified relationship | Explicit future-work gap: one source has a direct relation while another introduces an intervening entity. The selected CMO does not yet map these generally. | REVIEWER_INTERPRETATION; E11 |
| C45 / Provenance / biomedical experiment / TMO | Stated future conceptual integration targets; not a completed current domain-model/provenance experiment. | REVIEWER_INTERPRETATION; E11 |
| C46 / ?x / ?class / ?otherClass / ?typeConcept / ?otherTypeConcept / ?commonConcept | Fig. 5 rule variables, distinct from released class names. Complete before/after graph is retained in diagrams.yaml. | REVIEWER_INTERPRETATION; E10 |
| C47 / ?domainClass / ?bridgClass / ?domainConcept / ?bridgConcept | Fig. 6 rule variables; output are arc is interpreted as generated subclass assertion by the caption, not an automatic theorem. | REVIEWER_INTERPRETATION; E10 |

## Relations and formal commitments

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| K01 / Modeling levels and identity | Paper separates reality, cognitive/conceptual layer and representational artifact, while allowing conceptual/logical facets to share identifiers. Explicit level and bridge semantics are required; no global disjointness or identity theorem is supplied. | REVIEWER_INTERPRETATION; E02, E06 |
| K02 / Core hierarchy | Type/Quality/Relation below SKOS Concept; Concept asserted under IAO information content entity. Universal and its three specializations form a separate displayed branch. FiatEntity is prose-only in this retained source. | REVIEWER_INTERPRETATION; E06, E07 |
| K03 / Representation / inverse / aboutness | represents goes from concept to represented entity, inverse representedBy; represents subproperty of IAO is about; representsUniversal specializes it. Role/filler typing does not establish correctness of what is represented. | REVIEWER_INTERPRETATION; E06, E07 |
| K04 / Self-representation limit | Source allows self-representation for concepts but rules it out for universals conceptually. Candidate representsUniversal irreflexivity does not establish global irreflexivity of represents, class/concept disjointness or every intended prohibition. | REVIEWER_INTERPRETATION; E06, A01 |
| K05 / Primary/qualifier composition | hasPrimaryConcept/hasQualifier specialize broadMatch in the conceptual layer. Shared anchor or qualifier omission cannot be assumed to preserve set inclusion or distinguish two composites. | REVIEWER_INTERPRETATION; E07, E10 |
| K06 / Quality relations | hasQuality Type->Quality, inverse qualityOf; valuesCanBe Quality->SKOS Concept. Signatures are not totality, unique-value or closed-enumeration conditions. | REVIEWER_INTERPRETATION; E07 |
| K07 / Relation roles | hasRole Relation->Type; hasRoleIn inverse. Source/target role properties specialize these and have corresponding inverse properties. No existential, exactly-two endpoint or functional constraint is printed in Fig. 2. | REVIEWER_INTERPRETATION; E07 |
| K08 / Proxy preservation | Authors claim UML generalizations, attributes, associations, typing and cardinality preserved through linked-data proxy generation; CDE permissible concepts become enumeration range. No proof/run log of complete preservation is supplied. | REVIEWER_INTERPRETATION; E08 |
| K09 / Fig. 3 query dependencies | Graph patterns use class/properties represented by concepts whose skos:broader points directly to NCIt Person/Education_Level. Direct broader is not an arbitrary transitive path; returned rows depend on dataset/entailment configuration, labels and vocabulary versions. | REVIEWER_INTERPRETATION; E09 |
| K10 / Fig. 3 syntax check | Current RDFLib7.6.0 parseQuery rejects the visually transcribed printed query at count (line4,col8). Printed aggregate alias lacks standard parentheses; GROUP BY and rdfs prefix are also absent. The historical engine/dialect is unknown; no corrected query, endpoint or HINTS result was run. | EXECUTED; E09, S01 |
| K11 / Fig. 4 evidence boundary | Nine bars visualize an author-reported education query. Exact count labels, missing-value population, sample provenance, weights and raw records are absent; no chart number is reconstructed as exact. | REVIEWER_INTERPRETATION; E09 |
| K12 / Fig. 5 instance rule | Before/after rule adds ?x rdf:type ?otherClass when two concepts point to the same primary anchor. Both arrows are hasPrimaryConcept despite broader/parent wording. This requires a policy/guard; shared anchors alone do not logically entail instance retyping. | REVIEWER_INTERPRETATION; E10 |
| K13 / Fig. 6 subclass rule | broaderTransitive/domain-concept and primary/BRIDG-concept paths meet at a common concept, then a subclass assertion is added. Concept hierarchy plus annotation links alone does not entail logical subsumption. | REVIEWER_INTERPRETATION; E10 |
| K14 / Noninterference and optional rules | Passive annotation and actively generated subclass/instance assertions have different effects. A general no-undesired-inference claim must specify signature, import closure and rule policy rather than assume all mappings conservative. | REVIEWER_INTERPRETATION; E01, E05, E10 |
| K15 / Candidate restriction boundaries | All four candidate qualified minimum cardinalities are0, which imposes no positive filler witness. No local FiatEntity or representedByType declaration exists; unversioned imported source contents were not resolved. | REVIEWER_INTERPRETATION; A01, E06, E10 |

## Complete paper relation index

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| R01 / cmo:representedBy | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R02 / cmo:represents | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R03 / cmo:representsUniversal | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R04 / iao:'is about' | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R05 / cmo:hasQualifier | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R06 / cmo:hasPrimaryConcept | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R07 / skos:broadMatch | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R08 / cmo:hasQuality | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R09 / cmo:qualityOf | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R10 / cmo:valuesCanBe | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R11 / cmo:hasRole | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R12 / cmo:hasRoleIn | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R13 / cmo:hasSourceRole | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R14 / cmo:hasSourceRoleIn | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R15 / cmo:hasTargetRole | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R16 / cmo:hasTargetRoleIn | Printed Fig. 2 property; complete direction, inverse and subproperty connections retained in diagrams.yaml. Do not infer fillers/cardinalities or a released IRI from a display label alone. | REVIEWER_INTERPRETATION; E07 |
| R17 / cmo:representedByType | Fig. 5-6 bridge label, distinct from representedBy used by Fig. 3; absent from selected mirror declaration set. | REVIEWER_INTERPRETATION; E09, E10, A01 |
| R18 / skos:broader / skos:broaderTransitive | Direct vocabulary hierarchy query versus transitive conceptual path in mapping rule; neither alone is rdfs:subClassOf. | REVIEWER_INTERPRETATION; E09, E10 |
| R19 / rdf:type (a / is a); subclass (are) | Query/instance membership and rule-generated subclass must remain distinct; CMap conventions are caption-grounded. | REVIEWER_INTERPRETATION; E07, E09, E10 |
| R20 / rdfs:label | Printed query retrieves values through labels; identifier equivalence, language and aggregation policy are not determined by a string label. | REVIEWER_INTERPRETATION; E09 |
| R21 / Conceptual represents / self-representation | Prose describes an intentional representation relation and self-representation exceptions, not a fully formalized semantic truth/identity contract. | REVIEWER_INTERPRETATION; E02, E06 |

## Requirements, examples and adverse cases

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| S01 / Search via NCIt | Positive: education/person fields annotated through the shared vocabulary can be queried without model-specific property names. Adverse: a concept related only by a longer broader chain or exact term is not matched by a direct skos:broader pattern under simple graph matching. | REVIEWER_INTERPRETATION; E04, E09 |
| S02 / Concept versus instance | Positive: a Cat concept represents a class whose members are cats. Adverse: typing the concept itself as a cat confuses class extension with idea-of-class; punning alone does not supply the required bridge. | REVIEWER_INTERPRETATION; E06 |
| S03 / Shared primary anchor | Manual countercase: AdultPerson and MinorPerson concepts both point to Person; one adult individual need not be an instance of MinorPerson. This refutes an unconditional shared-anchor-to-retyping rule, not every task-specific mapping. No solver countermodel executed. | REVIEWER_INTERPRETATION; E07, E10 |
| S04 / Conceptual broader versus subclass | Positive: a task may explicitly approve a mapped subclass assertion. Adverse: broader term can organize topics rather than denote set inclusion; its existence plus primary-concept annotations does not prove the proposed subclass. | REVIEWER_INTERPRETATION; E10 |
| S05 / Clinical encounter to Alive | Positive: a valid patient encounter attested on a date can support a dated derived record under an approved rule. Adverse: a planned/cancelled encounter, unrelated subject, time-zone mismatch or historical record requires explicit guards and provenance. | REVIEWER_INTERPRETATION; E04 |
| S06 / No baseline change | Positive: selected passive metadata can be managed separately. Adverse: imported domain/range/class axioms or an added subclass rule can create new typing/contradiction in the combined theory. Noninterference is scope-dependent. | REVIEWER_INTERPRETATION; E01, E05, E10, A01 |
| S07 / Composite concept fidelity | Positive: Tissue qualifier plus Specimen primary concept expresses an intended decomposition. Adverse: two qualified types sharing a primary anchor need not be interchangeable, and qualifier omission can erase a clinically meaningful distinction. | REVIEWER_INTERPRETATION; E07 |
| S08 / Permissible values | Positive: permitted concepts populate a CDE enumeration range. Adverse: annotation valuesCanBe alone is not a closed-world data-validation check and source strings may map ambiguously. | REVIEWER_INTERPRETATION; E07, E08 |
| S09 / Query/plot reproduction | Positive: printed query and chart illustrate the desired search task. Adverse: current syntax parser rejects the printed form; unavailable source dataset/engine means chart counts and semantics are not rerun. | REVIEWER_INTERPRETATION; E09, S01 |
| S10 / Punning statement | Positive: an individual facet can be explicitly typed as a SKOS Concept. Adverse: class-extension constraints are not automatically inherited by that facet, nor does this mean the individual facet has no semantics whatsoever. | REVIEWER_INTERPRETATION; E06, S02 |
| S11 / Defeasible-looking bird association | Positive: a conceptual birds-can-fly relationship can remain outside automatic instance inference. Adverse: it is not therefore a default-logic implementation with sound exception handling for injured/flightless birds. | REVIEWER_INTERPRETATION; E10 |
| S12 / Granularity difference | Positive: same-granularity classes may be related under an approved model policy. Adverse: a direct edge versus an intervening event/entity requires a transformation not provided by this CMO paper. | REVIEWER_INTERPRETATION; E11 |
| S13 / Mirror identity and date | Positive: pin the exact matching-namespace candidate for bounded analysis. Adverse: its v2006 path or matching class names does not establish release 2006 or fidelity to the2011 paper. | REVIEWER_INTERPRETATION; A01 |
| S14 / Zero cardinality | Positive: minQualifiedCardinality0 does not reject an entity without a representation edge. Adverse: describing it as a mandatory conceptual representation witness invents a stronger axiom. | REVIEWER_INTERPRETATION; A01 |

## Critical findings

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| F01 / Direct prior conceptualization coverage | CMO directly models conceptual knowledge and its relation to logical models/common vocabularies; later novelty claims must compare concrete scenarios, not claim no prior conceptualization model. | REVIEWER_INTERPRETATION; E01, E02, E06 |
| F02 / Complete work/version boundary | Selected CEUR text uses Level 2 concepts, nine pages and 37 references. Other layouts/version wording are not substituted. Technical PDF creator metadata is not scholarly authorship. | REVIEWER_INTERPRETATION; E01, E06, E13 |
| F03 / Concept versus artifact grounding tension | Level 2 cognitive framing and asserted SKOS-to-IAO information-content inheritance require an explicit content/cognition distinction; the paper does not prove these are one category. | REVIEWER_INTERPRETATION; E02, E06, E07 |
| F04 / Foundation hierarchy discrepancy | Fig. 1 prints GenericallyIndependentContinuant under IndependentContinuant, unlike dependent terminology in prose. Preserve the observed conflict; no corrected foundation hierarchy or consistency proof is inferred. | REVIEWER_INTERPRETATION; E06, E07 |
| F05 / Prefix not edition | Paper family BFO is explicit; bfo2 display prefix alone does not specify version. Mirror actually names BFO1.1 namespace IRIs, without pinning a BFO import or original paper edition. | REVIEWER_INTERPRETATION; E03, E07, A01 |
| F06 / Shared concept anchor is insufficient | Fig. 5-6 additions are explicit rule-policy actions. A common conceptual anchor does not, without stronger premises, guarantee instance membership/subsumption. | REVIEWER_INTERPRETATION; E10 |
| F07 / Fig. 5 caption versus arcs | Parent/broader wording conflicts with two primary-concept arrows in the graph. Do not silently replace an arrow with broader or accept the rule as universally sound. | REVIEWER_INTERPRETATION; E10 |
| F08 / Representation bridge availability | Fig. 3 uses representedBy; Fig. 5-6 use representedByType absent from Fig. 2 and mirror. This is a source/version correspondence question, not proof that no historical implementation had it. | REVIEWER_INTERPRETATION; E07, E09, E10, A01 |
| F09 / Printed-query reproducibility limit | Executed parser rejection is specific to current RDFLib7.6.0 and the literal printed form. Missing GROUP BY/rdfs prefix and aggregate syntax matter for modern reproduction; historical dialect and results remain unknown. | REVIEWER_INTERPRETATION; E09, S01 |
| F10 / Evaluation shows illustration, not accuracy | One query plot and two rule diagrams demonstrate intended use; no controlled alignment precision/recall, expert validation, multi-resource fidelity/error study or reasoner log is identified. | REVIEWER_INTERPRETATION; E09, E10, E12 |
| F11 / Minimal semantics shifts obligation to policy | Task-tailored weak/strict alignment is flexible, but mapping soundness, conflict handling, qualification and preservation conditions must be supplied elsewhere. | REVIEWER_INTERPRETATION; E05, E10 |
| F12 / Noninterference claim requires scope | Adding passive concept metadata and adding active class/instance conclusions have different consequences. No blanket conservative-extension theorem is supplied for all imports and optional rules. | REVIEWER_INTERPRETATION; E01, E05, E10, A01 |
| F13 / Explicit unsupported granularity | Direct-relation versus intervening-class mapping is an author-stated future limitation; preserve it as a comparison constraint rather than inventing implemented support. | REVIEWER_INTERPRETATION; E11 |
| F14 / All candidate classes inspected, original unknown | Third-party candidate supplies seven local named classes and 14 local object properties, all inventoried with constraints; seven local classes manually reviewed. FiatEntity is missing there, as is representedByType. Original distribution and imported definitions remain unresolved #245. | REVIEWER_INTERPRETATION; E06, E10, A01 |
| F15 / Comment absence is not all-definition absence | UniversalQuality lacks rdfs:comment but has a descriptive seeAlso literal; do not count a missing comment as a complete missing-source-definition claim. | REVIEWER_INTERPRETATION; A01 |
| F16 / Candidate zero lower bounds | Four minimum-qualified cardinality 0 restrictions do not require representation witnesses; any stronger interpretation must be separately justified. | REVIEWER_INTERPRETATION; A01 |

## Unresolved questions

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Q01 / Original module and foundations | #245: Recover author-controlled cmo.owl/history and historical direct imports; compare exact missing terms and resolve the foundation typo/level/edition discrepancies without treating mirror path date as release date. | REVIEWER_INTERPRETATION; E03, E06, E07, A01 |
| Q02 / Eight bounded semantic questions | #245: At most eight checks: source/term/import identity; class/individual punning and self-representation; BFO/IAO hierarchy/category relation; zero-cardinality witness semantics; noninterference/import signatures; Fig. 3 query/dataset reproduction; Fig. 5 retyping safety; Fig. 6 subclass policy and granularity limits. | REVIEWER_INTERPRETATION; E05, E06, E07, E09, E10, E11, A01 |
| Q03 / Alignment evidence | What task-specific sample, expert/reference labels and positive/negative outcomes would distinguish common vocabulary linkage from correct conversion or subsumption? This is a later research candidate, not a completed study. | REVIEWER_INTERPRETATION; E04, E09, E10 |
| Q04 / Compositional meaning | What semantics distinguish primary concept plus qualifiers, preserve ordering/context and prevent the AdultPerson/MinorPerson common-anchor countercase? | REVIEWER_INTERPRETATION; E07, E10 |
| Q05 / Reproducible results | Can an exact HINTS2005 extract, swBIG revision, NCIt conversion, query dialect and chart data be recovered? Current parser rejection is not a historical runtime finding. | REVIEWER_INTERPRETATION; E08, E09 |

## Inputs for later synthesis

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Y01 / Bound future gap claims | Retain CMO as positive direct prior art for conceptual modeling, representation levels and vocabulary-mediated interoperability; compare with DnS/LMM on specific requirements and inference policy. | REVIEWER_INTERPRETATION; E01, E02, E06, E10 |
| Y02 / Scenario and evidence bank | Carry concept/instance identity, common-anchor false mapping, noninterference, CDE value constraints and granularity countercases into later bounded comparison. Adoption remains DEFER_TO_OWNER_AFTER_SYNTHESIS. | REVIEWER_INTERPRETATION; E04, E05, E06, E08, E10, E11 |
| Y03 / Three source populations | Separate full 2011 paper, pinned third-party seven-local-class candidate and unresolved original/import closure. Unknown original counts are null, not7 or 12. Candidate namespace1.1 is not an established paper edition. | REVIEWER_INTERPRETATION; A01, E03, E06 |
| Y04 / Comparison and final synthesis | Use existing bounded COM/Representation/CMO comparison #255 and final #126 procedure only when their own inputs are ready; this review closes #83, not #245 or final scientific acceptance. No Clariceptify change. | REVIEWER_INTERPRETATION; E11, E12, A01 |

## Evaluation evidence

- **Verification:** Paper gives hierarchy/properties/query and transformation sketches, but no reasoner/profile or complete mapping-preservation proof. Candidate RDF parsing and current printed-query parser rejection were actually executed; neither is ontology consistency or historical HINTS execution. [REVIEWER_INTERPRETATION; E07, E08, E09, A01, S01]
- **Validation:** Use cases and five requirements derive from author modeling experience. No independently recruited expert sample, validated CQ study or human agreement analysis is identified in the complete selected paper. [REVIEWER_INTERPRETATION; E03, E04, E05]
- **Evaluation:** Author query plot and two mapping diagrams illustrate use. No reproducible benchmark, alignment accuracy, conversion fidelity metric, controlled baseline or raw chart population is supplied. Future targets remain future. [REVIEWER_INTERPRETATION; E09, E10, E11]
- **Assessment:** Source-linked AI-assisted critique separates modeling levels, rule-policy assumptions, source/figure/candidate discrepancies and conditional countercases. It is not independent expert acceptance or exhaustive consequence analysis. [REVIEWER_INTERPRETATION; E06, E07, E09, E10, A01]
- **Assurance:** Pinned paper/mirror hashes, all-page OCR/visual recovery record, complete figures/properties, all seven local candidate-class reviews and bounded dated discovery support traceability. CI/source retention do not establish semantic or scientific adequacy. [REVIEWER_INTERPRETATION; E01, E13, A01]

## Artifact and repository boundary

Technical follow-up: #245. State: `THIRD_PARTY_CANDIDATE_RETAINED_ALL_LOCAL_CLASSES_REVIEWED_ORIGINAL_IMPORTS_SEMANTICS_PENDING`.

Original paper-linked PURL redirects to old Google Code SVN and returns404. Retained mirror at dbpedia/ontology-tracker commit 32f457a42b910e39ef087b26f1664bd8d507518b has exact CMO namespace but is not an author release; its path v2006/2006-06-30 is not established as a release date. Candidate147 explicit triples:12 named class declarations (7 local,5 external),20 object properties (14 local,6 external),4 anonymous restrictions. No explicit datatype/annotation-property/NamedIndividual declarations; this does not mean no annotations or no individuals of any kind. All local classes manually reviewed below, six with comment candidates and one with a descriptive seeAlso literal. Imports of IAO/SKOS unversioned and unresolved historically; no reasoner/profile execution, inferred counts or complete original 2011 census. #245 retains eight selected questions and exact correspondence. Raw source retained separately, not publicly copied.

### Every local class in the selected third-party CMO candidate

| ID / class | Manual constraint/correspondence review | Evidence |
|---|---|---|
| AC01 / cmo:Quality | Source-attributed reviewer paraphrase and constraint review: Conceptual description of an inherent property or assigned attribute; source intentionally groups those cases. Subclass SKOS Concept only in selected local class axioms; no equivalence or value-filler existential. | REVIEWER_INTERPRETATION; A01 |
| AC02 / cmo:Relation | Source-attributed reviewer paraphrase and constraint review: Conceptual relation between independent entities; SKOS Concept subtype. Endpoint properties are recorded in the property census, not encoded as a mandatory exact-two local class restriction. | REVIEWER_INTERPRETATION; A01 |
| AC03 / cmo:Type | Source-attributed reviewer paraphrase and constraint review: Conceptual generalization representing instances; SKOS Concept subtype, not the represented logical class itself. No local equivalence/closure requirement. | REVIEWER_INTERPRETATION; A01 |
| AC04 / cmo:Universal | Source-attributed reviewer paraphrase and constraint review: Real-side entity category, under BFO1.1 IndependentContinuant plus representedBy min0 SKOS Concept. The zero minimum imposes no positive representation witness; philosophical category correspondence remains open. | REVIEWER_INTERPRETATION; A01 |
| AC05 / cmo:UniversalClass | Source-attributed reviewer paraphrase and constraint review: Realist-side natural grouping, under Universal plus representedBy min0 Type. The label and comment do not establish its extension or require an actual Type witness. | REVIEWER_INTERPRETATION; A01 |
| AC06 / cmo:UniversalQuality | Source-attributed reviewer paraphrase and constraint review: Real-side quality category according to a descriptive seeAlso literal; rdfs:comment absent. Under Universal plus representedBy min0 Quality. Preserve annotation kind; do not invent a comment or sufficient definition. | REVIEWER_INTERPRETATION; A01 |
| AC07 / cmo:UniversalRelation | Source-attributed reviewer paraphrase and constraint review: Real-side relationship category, under Universal plus representedBy min0 Relation. The zero minimum is not a mandatory conceptual-link constraint. | REVIEWER_INTERPRETATION; A01 |

## Evidence index

| ID | Exact source locator | Source-grounded summary |
|---|---|---|
| E01 | p.191/PDF 1, title/authors/abstract and sec.1 Introduction | Three authors, conceptual interoperability goal, separate conceptual/logical/physical modeling and noninterference aim. |
| E02 | pp.191-192/PDF 1-2, sec.2 Background including Levels1-3 and two goals | Reality/cognitive/representation distinction and conceptual/logical model definitions; two interoperability goals and data-resource examples. |
| E03 | p.192/PDF 2, sec.2.1 Relevant Ontologies and Frameworks | BFO/IAO reuse, SKOS vocabulary layer, caBIG/OWL prior limitations and failed one-to-one attribute/property mapping. |
| E04 | pp.192-193/PDF 2-3, sec.3 three use cases and footnotes 1-4 | Search/query, conversion and mapping; patient-history, clinical-service/vital-status and AIM/BRIDG Person examples. |
| E05 | p.193/PDF 3, sec.3 five requirement headings | Common vocabulary; conceptual/logical distinction; natural expression; type/property/relation support; additional relationships. |
| E06 | pp.193-194/PDF 3-4, sec.4 core definitions and footnote 5 | Type/Quality/Relation, SKOS/IAO superclasses, Universal/FiatEntity, punning and concept-versus-instance discussion. |
| E07 | pp.194-195/PDF 4-5, sec.4 representation/composition/structural relations and Figs.1-2 | Complete category hierarchy and relation diagram, inverses/subproperties/signatures; source spelling/direction and prose/figure discrepancies retained. |
| E08 | pp.194-195/PDF 4-5, sec.5 Implementation | swBIG REST proxy, caGrid calls, NCIt-to-SKOS conversion, UML preservation claims, CDE enumeration of concepts and instance generation. |
| E09 | pp.196-197/PDF 6-7, sec.6 query narrative and Figs.3-4 | Education-distribution query and nine displayed bars; no exact numeric bar labels or reproducible dataset/engine package. |
| E10 | pp.196-197/PDF 6-7, sec.6 conversion/mapping narrative and Figs.5-6 | Instance retyping and subclass-generation patterns, task-tailored weak/strict alignment and nonautomatic bird/flying example. |
| E11 | pp.196,198/PDF 6,8, sec.7 Future Work split by figure page | BRIDG/provenance/TMO plans and explicitly unsupported mapping between different granularity/reification levels. |
| E12 | p.198/PDF 8, sec.8 Conclusion | Generalized OWL-model applicability and current-use statements are author claims, not reproduced coverage/accuracy results. |
| E13 | pp.198-199/PDF 8-9, bibliography1-37 | All 37 bibliography records inspected; reference 19 continues onPDF9. Cited sources are not all acquired or independently validated. |
| A01 | Pinned dbpedia/ontology-tracker candidate file, all 147 explicit triples; selected file not an author release | Seven local named classes/14 local object properties; five external class and six external object-property declarations. All named declarations/constraints indexed; historical fidelity and imports unpinned. |
| S01 | SPARQL1.1 Query, sections11.2,11.4 and 16.1.2; accessed2026-10-27 | Current aggregate projection/grouping and expression rules used only as a comparison standard; historical endpoint dialect unknown. |
| S02 | OWL2 New Features and Rationale, section2.4.1 F12 Punning; accessed2026-10-27 | Class/individual facets of an IRI are treated separately under OWL2 Direct Semantics; SKOS assertions do not automatically transfer class-extension semantics. |

## Closure boundary

Complete critical review of the exact 9-page2011 proceedings paper, including OCR/visual recovery, six figures, five footnotes and 37 references. All seven local classes of one pinned third-party mirror manually reviewed with full declaration/constraint census; not a complete original-author distribution/imported glossary, reasoner/profile run, reproduced HINTS plot, validated rule policy or independent scientific acceptance. #245 remains open for historical source/import identity and at most eight bounded semantic questions; final #126 remains open. No Clariceptify ontology, definition, requirement, fixture, manuscript or release changed.
