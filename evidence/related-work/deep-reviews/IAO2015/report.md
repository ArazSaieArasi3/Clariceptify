# Aboutness: Towards Foundations for the Information Artifact Ontology

Work: `IAO2015` | Issue: #78 | State: `REVIEW_COMPLETE`

Reviewed version: Smith and Ceusters, CEUR Workshop Proceedings 1515, 2015, pp.1-5. Input: `IAO-2015.pdf`, 5 PDF pages, SHA256 `11c3413eb339aadc8baed9c6991a986c9f489d0ff2ca2b16508bb2688ff77b37`.

The structured `review.yaml` is the evidence authority; this report is derived. This is an AI-assisted critical review, not independent expert acceptance. Clariceptify is unchanged; later use requires an owner decision.

## Identity and reading coverage

Barry Smith and Werner Ceusters. This five-page conceptual proposal critiques and extends the then-current IAO; it is not a release note for the current repository. Printed and PDF pages coincide. No DOI is established in the acquired primary paper. BFO/MFO commitments and proposed changes are kept distinct from current OWL implementation.

All five pages, all seven numbered sections, subsections5.1/5.2, numbered unit categories, the single table and the bibliography were inspected. All explicitly defined/elucidated ontology terms and their foundational categories are catalogued below, along with the semantic distinction families used in examples. Incidental object names are examples, not a new ontology class population.

| Paper unit | Coverage | Evidence |
|---|---|---|
| Title, abstract and sec.1 Introduction | REVIEWED | E01, E02 |
| Sec.2 Aboutness and portions of reality | REVIEWED | E03 |
| Sec.3 Information and mis-information | REVIEWED | E04 |
| Sec.4 Representation and reference; list1-5 | REVIEWED | E05, E06 |
| Sec.5.1 Primitives and elucidations | REVIEWED | E07 |
| Sec.5.2 Definitions | REVIEWED | E08 |
| Sec.6 Discussion | REVIEWED | E09 |
| Sec.7 Conclusion | REVIEWED | E10 |
| Table1 representational units | REVIEWED | E06 |
| Acknowledgements and bibliography; no figures or appendices | REVIEWED | E10 |

## Common review dimensions

### D1_identity_coverage

The selected work is the 2015 five-page Smith/Ceusters proposal, reviewed in full. It critiques an existing ICE definition and proposes broader aboutness/representation foundations; those proposals are not assumed to be accepted by current IAO releases. [AUTHOR_REPORTED; E01, E10]

### D2_problem_contribution

Existing IAO treatment of ICE, cognitive representation and aboutness is insufficient for information creation, reference failure, misinformation, fiction and time/context. The proposed contribution links content and material/mental concretizations, broadens targets to portions of reality and distinguishes successful reference from intended reference. [AUTHOR_REPORTED; E01, E03, E04, E05, E07, E08]

### D3_method

The method is foundational conceptual analysis: critique a definition, distinguish dependency/representation levels, analyze counterexamples and propose English logical definitions and elucidations. Nurse/pulse, false presidential claims, fiction and Vulcan are argumentative cases; there is no implemented study protocol or formal-model experiment in this text. [REVIEWER_INTERPRETATION; E01, E03, E04, E06, E07, E08]

### D4_requirements

The paper targets domain-neutral information modeling, especially scientific/biomedical records. A satisfactory account should handle shareable content across bearers, cognitive grounding, past or misidentified targets, false composites and corrected reference beliefs. These are reconstructed requirements from the paper arguments, not author-declared competency questions or a passing CQ suite. [REVIEWER_INTERPRETATION; E02, E03, E04, E06, E09]

### D5_concepts

ICE is generically dependent content, IQE its specifically dependent quality concretization and an information artifact its material bearer. Cognitive representation is a mental quality; Representation allows intended reference to fail. Referring/non-referring units and recognition status distinguish what exists, what is intended and what is believed. ICE is explicitly historical rather than an abstract proposition. [AUTHOR_REPORTED; E01, E02, E03, E05, E06]

### D6_relations_formalization

Definitions and primitive elucidations are inventoried without turning them into OWL axioms. Successful is_about entails target existence; intended-to-be-about does not. Conformity shares a GDC and alone does not encode truth, reliable observation or identity of targets. Time is explicit for concretization/dependence and context-dependent reference histories require more than a static class label. [REVIEWER_INTERPRETATION; E03, E04, E07, E08]

### D7_grounding

BFO dependence and material/quality/GDC distinctions ground the account; MFO adds mental qualities and cognitive representation. Intentional acts ground artifact aboutness. A target need not exist contemporaneously with its representation, and veridical representation need not identify its target universal correctly. These realist commitments differ from treating all content as private DOLCE mental objects or as atemporal propositions. [REVIEWER_INTERPRETATION; E01, E02, E03, E05, E09]

### D8_artifact_correspondence

The retained IAO repository contains current release/development roots and many historical releases. The reviewed 2015 proposal does not pin that repository commit or show adoption of every proposal. Repository README distinguishes iao.owl and iao-edit.owl; the retained release root identifies 2026-03-30. Detailed selection/import/count/axiom work remains #240, with no summation across release directories. [REVIEWER_INTERPRETATION; E01, E07, E10, R01, R02]

### D9_evaluation

Arguments are illustrated by philosophical/clinical examples; no recruited expert sample, quantitative experiment, full CQ suite or executed consistency proof is reported. Neuroscientific grounding is explicitly uncertain and several language/mental questions are future work. Reviewer critical analysis is separate from author evidence and independent scientific acceptance. [REVIEWER_INTERPRETATION; E04, E06, E09, E10]

### D10_critical_synthesis

Useful prior distinctions cover content versus carrier/quality, intentional versus successful reference, temporal provenance and representational error. Weak points for computational reuse are the lack of an operational account of intention/recognition, an executable configuration semantics and a complete identity rule across contexts. Their resolution is not supplied by generic aboutness or a current IAO class count. [REVIEWER_INTERPRETATION; E03, E04, E06, E07, E08, E09]

## Conceptual catalog

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| C01 / Entity | FOUNDATIONAL/CONTENT: Superclass in the existing ICE definition; the POR proposal broadens the target beyond BFO entities. | AUTHOR_REPORTED; E01 |
| C02 / InformationContentEntity / ICE | FOUNDATIONAL/CONTENT: Generically dependent information content about some target; existing and proposed definitions must be distinguished. | AUTHOR_REPORTED; E01 |
| C03 / GenericallyDependentContinuant / GDC | FOUNDATIONAL/CONTENT: Content dependent on some appropriate bearer rather than one specific bearer. | AUTHOR_REPORTED; E01 |
| C04 / MaterialEntity | FOUNDATIONAL/CONTENT: Bearer category; information artifacts are material, ICEs are not. | AUTHOR_REPORTED; E01 |
| C05 / SpecificallyDependentEntity | FOUNDATIONAL/CONTENT: Dependency on a particular bearer; the quality that concretizes content is of this kind. | AUTHOR_REPORTED; E01 |
| C06 / Quality | FOUNDATIONAL/CONTENT: All concretizations are qualities in the adopted BFO framework. | AUTHOR_REPORTED; E01 |
| C07 / Universal | FOUNDATIONAL/CONTENT: Type quantified over in generic dependence and included among proposed aboutness targets. | AUTHOR_REPORTED; E01 |
| C08 / Continuant / Occurrent | FOUNDATIONAL/CONTENT: Persistent informational content versus cognitive/communicative processes; processes inherit aboutness by a stated hypothesis. | AUTHOR_REPORTED; E01 |
| C09 / InformationQualityEntity / IQE | DEFINED: Quality concretizing an ICE; called information carrier in the then-current IAO terminology. | AUTHOR_REPORTED; E02 |
| C10 / Artifact | DEFINED: Material entity created, modified or selected by an agent to realize a function or role. | AUTHOR_REPORTED; E02 |
| C11 / InformationArtifact | DEFINED: Artifact whose function is bearing an IQE; includes hard drives, signs and printed forms. | AUTHOR_REPORTED; E02 |
| C12 / Disposition | DEFINED: May be grounded in a mental quality but is not identical to that quality; lab-order example. | AUTHOR_REPORTED; E02 |
| C13 / Function / Role | DEFINED: Purposes invoked in artifact definitions; their full BFO theories are not restated. | AUTHOR_REPORTED; E02 |
| C14 / Agent / cognitive subject | DEFINED: Creates artifacts and associates cognitive representations with patterns; not operationalized as an independent complete agent ontology here. | AUTHOR_REPORTED; E02 |
| C15 / Thinking / Speaking / Hearing / Writing / Reading | DEFINED: Process families through which content is created, understood and communicated; not a complete hierarchy in this paper. | AUTHOR_REPORTED; E02 |
| C16 / PortionOfReality / POR | SEMANTIC: Proposed generalized target category, including universals, relations, ICEs and configurations. | AUTHOR_REPORTED; E03 |
| C17 / Configuration | SEMANTIC: Entities related in a time interval considered together; used to explain composite sentence targets. | AUTHOR_REPORTED; E03 |
| C18 / Relation | SEMANTIC: Included among POR targets, e.g. part-whole transitivity. | AUTHOR_REPORTED; E03 |
| C19 / Pattern | SEMANTIC: Ambiguous between shareable content and bearer-specific quality; the distinction motivates ICE/IQE separation. | AUTHOR_REPORTED; E03 |
| C20 / DirectCognitiveRepresentation | SEMANTIC: Relational mental quality grounded by a target-initiated causal observation process. | AUTHOR_REPORTED; E03 |
| C21 / Indexicality | SEMANTIC: Historical creation context contributes to what an ICE is about and how it is truth-evaluated. | AUTHOR_REPORTED; E03 |
| C22 / Information / Mis-information | ANALYTICAL_DISTINCTION: The authors distinguish successful composite aboutness from failure while allowing component aboutness; not a complete executable truth taxonomy. | AUTHOR_REPORTED; E04 |
| C23 / Fictional representation | ANALYTICAL_DISTINCTION: Composite can lack a real configuration while some components still refer. | AUTHOR_REPORTED; E04 |
| C24 / Ungrounded representation | ANALYTICAL_DISTINCTION: Intended reference can depend on belief in a nonexistent target; Vulcan illustrates it. | AUTHOR_REPORTED; E04 |
| C25 / Belief / Intention | ANALYTICAL_DISTINCTION: Attitudes invoked in reference recognition and failure; no standalone BDI formalization is provided. | AUTHOR_REPORTED; E04 |
| C26 / Representation | DEFINED: Quality that is about or is intended to be about some POR; broader than ICE in the authors account. | AUTHOR_REPORTED; E05 |
| C27 / MentalQuality | DEFINED: Quality specifically dependent on an anatomical structure in an organism cognitive system. | AUTHOR_REPORTED; E05 |
| C28 / CognitiveRepresentation | DEFINED: Representation that is a MentalQuality. | AUTHOR_REPORTED; E05 |
| C29 / AnatomicalStructure / Organism / CognitiveSystem | DEFINED: Bearer context in the MentalQuality definition; fine physical realization is left open. | AUTHOR_REPORTED; E05 |
| C30 / MentalProcess | DEFINED: Thinking/imagining/remembering may be intentional; inheritance from continuant representation is hypothesized. | AUTHOR_REPORTED; E05 |
| C31 / RepresentationalUnit / RU | DEFINED: Smallest constituent subrepresentation, e.g. name, icon, word or identifier. | AUTHOR_REPORTED; E05 |
| C32 / ReferringRepresentationalUnit / RRU | UNIT_CATEGORY: Intended reference succeeds; Table1 abbreviates its first example as RU. | AUTHOR_REPORTED; E06 |
| C33 / NonReferringRepresentationalUnit / NRU | UNIT_CATEGORY: Fails to be about anything. | AUTHOR_REPORTED; E06 |
| C34 / UnrecognizedNonReferringRepresentationalUnit / UNRU | UNIT_CATEGORY: Nonreferring while intended and believed to refer. | AUTHOR_REPORTED; E06 |
| C35 / RecognizedNonReferringRepresentationalUnit / RNRU | UNIT_CATEGORY: Previously intended/believed reference is no longer believed after knowledge changes. | AUTHOR_REPORTED; E06 |
| C36 / RepresentationalUnitComponent / RUC | UNIT_CATEGORY: Component not intended by the artifact authors to refer in isolation; not clearly the same granularity as an RU. | AUTHOR_REPORTED; E06 |
| C37 / LanguageOntology | PROPOSED_EXTENSION: Future framework for assertion, perception and language-mediated creation of conformant mental representations. | AUTHOR_REPORTED; E10 |
| C38 / DocumentAct | PROPOSED_EXTENSION: Prior ontology/template named as a base for future language work, not implemented in this report. | AUTHOR_REPORTED; E10 |

## Relations and formal commitments

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| K01 / Existing ICE definition | Entity generically dependent on some MaterialEntity and standing in aboutness to some Entity; this is the definition criticized, not the final broadening. | AUTHOR_REPORTED; E01 |
| K02 / generic dependence | a and b exist, b instantiates some universal B, and necessarily if a exists then some B exists. Specific bearer b is not required across all realizations. | AUTHOR_REPORTED; E01 |
| K03 / specific dependence | The dependent cannot exist without its particular bearer; contrasted with migration/copying. | AUTHOR_REPORTED; E01 |
| K04 / IQE definition | IQE is a Quality concretizing some ICE. | AUTHOR_REPORTED; E02 |
| K05 / Artifact definition | MaterialEntity created, modified or selected by some agent to realize Function or Role. | AUTHOR_REPORTED; E02 |
| K06 / InformationArtifact definition | Artifact with the function of bearing an IQE. | AUTHOR_REPORTED; E02 |
| K07 / Proposed target broadening | Replace aboutness to some Entity by aboutness to some POR, allowing universals, relations, other ICEs and configurations. Not all are BFO entities as understood in this paper. | AUTHOR_REPORTED; E03 |
| K08 / Representation definition | Quality that is_about or is intended to be about a POR; successful aboutness and mere intention are disjuncts. | AUTHOR_REPORTED; E05 |
| K09 / MentalQuality definition | Quality specifically dependent on an AnatomicalStructure in an Organism cognitive system. | AUTHOR_REPORTED; E05 |
| K10 / CognitiveRepresentation definition | Representation and MentalQuality; no consciousness or image-like form is entailed by the definition. | AUTHOR_REPORTED; E05 |
| K11 / RU and five unit categories | RU denotes minimal subrepresentation; RRU succeeds, NRU fails, UNRU/RNRU distinguish recognition, RUC is not intended to refer independently. The list mixes granularity/status and requires an implementation decision. | AUTHOR_REPORTED; E05, E06 |
| K12 / is_about primitive | Domain representations; range POR; if x is_about y then y exists. Intended aboutness does not carry this existential success condition. | AUTHOR_REPORTED; E07 |
| K13 / concretizes at t primitive | x is Quality, y is GDC, and for some material bearer z at t: x specifically depends on z and y generically depends on z. Migration to another bearer creates a copy of x, not numerical identity of quality across bearers. | AUTHOR_REPORTED; E07 |
| K14 / direct cognitive representation primitive | x is CognitiveRepresentation in subject s, x is_about y and x arises in s through an appropriate causal process initiated by y. Appropriateness is not operationally defined. | AUTHOR_REPORTED; E07 |
| K15 / is_a_representation_of definition | x is Representation and x is_about y, where y is POR. Unlike the Representation class alone, this relation entails successful reference. | AUTHOR_REPORTED; E08 |
| K16 / is_conformant_to definition | x is IQE, y is CognitiveRepresentation and some GDC g is concretized by both. The relation connects qualities through shared content; it does not itself assert truth or the same bearer. | AUTHOR_REPORTED; E08 |
| K17 / Continuation-to-process aboutness hypothesis | Cognitive occurrent representations inherit intended aboutness from underlying continuant representation; explicitly a hypothesis. | AUTHOR_REPORTED; E05 |
| K18 / Temporal target non-contemporaneity | A POR need not exist when its representation exists; past disorders remain direct targets rather than memories being substituted as targets. | AUTHOR_REPORTED; E09 |
| K19 / Component/composite reference | Components may refer while an entire false or fictional sentence fails to target an obtaining configuration; preserve levels. | AUTHOR_REPORTED; E04 |
| K20 / Context and truth history | The original context-indexed ICE is not claimed to change truth simply because the world changes; a new use may involve a different historical/indexical content. Identity conditions are not fully axiomatized. | AUTHOR_REPORTED; E04 |
| K21 / Time-dependent reference recognition | Unit classification can change as a target belief is corrected; the same string is insufficient to identify the semantic status across uses/times. | AUTHOR_REPORTED; E04, E06 |

## Requirements, examples and adverse cases

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| S01 / Positive observed measurement | A nurse observes a pulse, forms a direct cognitive representation and enters a value in a record. The record quality and mental quality can concretize shareable content grounded in that pulse. Causal provenance is doing more work than a bare string label. | REVIEWER_INTERPRETATION; E03, E07, E08 |
| S02 / False composite | The paper presidential counterexample retains reference of some components while denying a corresponding configuration for the whole. An implementation that assigns the whole sentence an obtaining target merely because two names refer would overstate its truth. | REVIEWER_INTERPRETATION; E04 |
| S03 / Failed reference and correction | Vulcan as believed in 1860 and a later acknowledged error illustrate UNRU versus RNRU. A static same-label lookup cannot encode belief-history and corrected reference status by itself. | REVIEWER_INTERPRETATION; E04, E06 |
| S04 / Adverse shared-content shortcut | Two qualities sharing a GDC satisfy the printed conformity definition, but that definition alone does not establish truthful content or reliable observation. Add a separate reference/grounding argument before making those claims. | REVIEWER_INTERPRETATION; E07, E08 |
| S05 / Past and unknown targets | A past disorder can be represented now, and a child/cat can perceive an object without knowing its universal. Do not require contemporaneous existence or correct type knowledge for every successful representation. | REVIEWER_INTERPRETATION; E09 |

## Critical findings

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| F01 / Carrier/content/quality separation | An ICE is not the material artifact and not a bearer-specific IQE. Equating these would erase sharing and dependence distinctions central to the paper. | REVIEWER_INTERPRETATION; E01, E02, E07 |
| F02 / Aboutness is a success condition | Successful aboutness and intended reference are distinct. A model limited to a single unrestricted is_about edge risks asserting real targets for mistaken or fictional representations. | REVIEWER_INTERPRETATION; E04, E05, E07 |
| F03 / Historical identity matters | The discussion treats ICE as a created historical entity with indexical origin. A string-only identity key cannot be assumed sufficient; the paper does not supply a complete replacement identity algorithm. | REVIEWER_INTERPRETATION; E03, E04 |
| F04 / Granularity and abbreviation caveat | The list defines RU and RRU separately but Table1 first row says RU; RUC is a component not intended to refer alone. Preserve the source labels and resolve classification granularity before executable reuse. | REVIEWER_INTERPRETATION; E05, E06 |
| F05 / Foundational range issue | POR includes targets not classified as BFO entities in the authors treatment. Encoding the proposed range as an undifferentiated BFO entity class would require a separate foundational mapping argument. | REVIEWER_INTERPRETATION; E03, E07 |
| F06 / Conceptual account not full computational method | Appropriate causation, intention, recognition and shared content are invoked without an operational determination procedure or validated extraction pipeline. A current OWL release cannot supply those claims retrospectively. | REVIEWER_INTERPRETATION; E06, E07, E08, E09, E10 |

## Unresolved questions

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Q01 / Proposal adoption | Which exact 2015 proposals are present, changed or absent in the selected current release? Keep same-word labels distinct from semantic implementation. #240 owns technical evidence. | UNKNOWN; E01, E07, E08 |
| Q02 / Identity/context | How should one identify historical content across creation, copying, re-use and belief correction? The text motivates the problem without a full algorithm. | UNKNOWN; E03, E04, E06 |
| Q03 / Operational grounding | What observable conditions establish appropriate causation or recognized reference failure, particularly for automatic sensors? The paper gives arguments/examples, not a validated operational test. | UNKNOWN; E04, E07, E09 |

## Inputs for later synthesis

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| U01 / Comparison cells | Keep ICE, IQE, material artifact, cognitive representation, cognitive act and POR separate in #254. Their relations should be compared under their actual foundational assumptions. | REVIEWER_INTERPRETATION; E01, E02, E03, E05 |
| U02 / Future adverse-case bank | Retain false composites, Vulcan corrections, past targets and shared-content-without-truth as research candidate cases. No Clariceptify constraints/CQs are changed. | REVIEWER_INTERPRETATION; E04, E06, E08, E09 |
| U03 / No automatic adoption | Possible use is to clarify reference-success and provenance distinctions after the owner reviews the cross-paper synthesis. No semantic equivalence, model repair or superiority follows from this single review. | REVIEWER_INTERPRETATION; E03, E05, E07, E08 |

## Evaluation evidence

- **Verification:** Definitions/elucidations and examples support conceptual inspection; there is no machine-checked consistency, entailment or completed CQ execution in this paper. [NOT_REPORTED; E07, E08, E10]
- **Validation:** Clinical/historical cases motivate intended adequacy; no independent domain-expert study, participants or acceptance population is reported. [NOT_REPORTED; E03, E04, E09]
- **Evaluation:** No controlled comparison, effect-size estimate or task benchmark is reported. Philosophical counterexamples provide argument, not empirical effectiveness measurements. [NOT_REPORTED; E04, E06, E10]
- **Assessment:** The reviewer finds useful separation of content, qualities, material carriers and reference success; computational identity/context/recognition remain unresolved within this text. [REVIEWER_INTERPRETATION; E02, E04, E06, E08]
- **Assurance:** The paper provides reasoned conceptual support and explicit open questions, not a certification or implemented assurance package. Physical grounding and future language work remain open. [NOT_REPORTED; E09, E10]

## Artifact and repository boundary

Technical follow-up: #240. State: `PINNED_REPOSITORY_AVAILABLE_TECHNICAL_REVIEW_PENDING`.

Retained repository information-artifact-ontology/IAO at 3006aedacbf813ffd1d2ac15cda10766ca9ed388 includes iao.owl, iao-edit.owl and historical releases. README identifies release versus development and imports; root iao.owl declares versionIRI http://purl.obolibrary.org/obo/iao/2026-03-30/iao.owl and CC-BY4.0 metadata. These current bytes are not a 2015 proposal implementation by assumption. #240 must select a root and inspect semantic correspondence, not sum all release classes.

## Evidence index

| ID | Exact source locator | Source-grounded summary |
|---|---|---|
| E01 | p.1, title/abstract and sec.1 Introduction | IAO scope, existing ICE definition, BFO generic/specific dependence and proposed embedding in MFO. |
| E02 | pp.1-2, sec.1 definitions and examples | IQE as quality concretizing ICE; dispositions versus mental qualities; material artifacts and information artifacts; processes creating/understanding/communicating ICEs. |
| E03 | p.2, sec.2 Aboutness and portions of reality | Aboutness extends reference to cognitive directedness; nurse/pulse grounding; created historical/indexical ICEs; targets generalized to portions of reality including universals, relations, other ICEs and configurations. |
| E04 | pp.2-3, sec.3 Information and mis-information | Component versus composite aboutness, false and fictional expressions, time-indexical truth, primacy of intentionality, sensor counterfactual and Vulcan reference failure. |
| E05 | pp.3-4, sec.4 Representation and reference | Representation as quality with successful or intended aboutness; mental quality and cognitive representation; hypothesized inheritance from continuant representation to cognitive processes. |
| E06 | p.4, sec.4 numbered list 1-5 and Table1 | RRU/NRU/UNRU/RNRU/RUC distinctions and time-dependent classifications. Table first row says RU while prose uses RRU; RUC is a non-independently-referring component. |
| E07 | p.4, sec.5.1 Primitives and elucidations | is_about with veridicality, concretizes at t, and direct cognitive representation via target-initiated causal process; primitives are elucidated, not a complete executable axiom set. |
| E08 | pp.4-5, sec.5.2 Definitions | is_a_representation_of adds successful aboutness; is_conformant_to relates IQE and cognitive representation through a shared generically dependent continuant. |
| E09 | p.5, sec.6 Discussion | Targets may be past, unknown by type or believed before evidence; physical basis of mental quality remains uncertain; unconscious representations deferred. |
| E10 | p.5, sec.7 Conclusion; acknowledgements and references | Proposed integration with MFO and future Language Ontology/document acts; no completed empirical or executable validation study is presented. |
| R01 | README.md, Files and development import list | Release iao.owl and development iao-edit.owl are distinguished; dependencies are enumerated. |
| R02 | iao.owl, ontology header/versionIRI/versionInfo/license | Pinned root declares 2026-03-30 release identity and CC-BY4.0 metadata, not 2015 proposal identity. |

## Closure boundary

This completes a source-bound critical paper dossier, not independent scientific acceptance, a reasoner run, author-experiment reproduction, formal-artifact completion or a Clariceptify model change. Named findings and technical tasks remain unresolved where stated. Disposition: DEFER_TO_OWNER_AFTER_SYNTHESIS; supported overlap is recorded, but no reuse/alignment/extension/rejection is applied to Clariceptify.
