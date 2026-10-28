# EmotionsOnto: an Ontology for Developing Affective Applications

Work: `EmotionsOnto2014` | Issue: #262 | State: `REVIEW_COMPLETE`

Reviewed version: J.UCS 20(13), 2014, printed 1813-1828;16-page publisher PDF. Input: `EmotionsOnto-2014.pdf`, 16 PDF pages, SHA256 `351bddf40462ec68b7ff990837b2a7cf144b8f239dc86bf76d2d9d0ec618d610`.

The structured `review.yaml` is the evidence authority; this report is derived. This is an AI-assisted critical review, not independent expert acceptance. Clariceptify is unchanged; later use requires an owner decision.

## Identity and reading coverage

Exact 2014 predecessor. PDF page n maps to printed n+1812. The missing 2015 related paper, author documentation and retained later Emotions & Cognition OWL are separate identities. Publisher metadata verifies DOI; no historical formal-file equivalence, experiment rerun or blanket source license is inferred.

Complete paper-level conceptual/relation catalog including nine core ovals, every one of 39 Figure 2 categories, reused foundation/frame terms, all 14 cited affective states, eight application labels, 14 distinct PrEmo instrument labels and role/measurement/device distinctions. Five figures and complete Table 1 inspected. No numbered equations, appendix, complete released-class census or evaluated general emotion-recognition system is invented.

| Paper unit | Coverage | Evidence |
|---|---|---|
| Front matter/title/authors/dates/abstract | REVIEWED | E01 |
| 1 Introduction: full scope/taxonomy/theory/context/application discussion | REVIEWED | E02 |
| 2 Related Work | REVIEWED | E03 |
| 2.1 Emotion-modeling ontologies | REVIEWED | E03 |
| 3 Contribution: methodology and OWL modeling | REVIEWED | E04, E05 |
| 3 External/interface/internal concepts and definitions | REVIEWED | E04 |
| Figure 1 all nine ovals and seven properties | REVIEWED | E04, E05 |
| 3 Properties/restrictions and upper ontology rationale | REVIEWED | E05 |
| Figure 2 all 39 categories and literal hierarchy | REVIEWED | E06 |
| 3 FrameNet integration and John/room role example | REVIEWED | E07 |
| 4 TUI architecture/application/learning | REVIEWED | E08 |
| Figure 3 front/rear physical/UI illustration | REVIEWED | E08 |
| Figure 4 complete instance frames/properties | REVIEWED | E09 |
| 4 Modeling-versus-recognition and bootstrapping limit | REVIEWED | E09 |
| 4.1 Empirical study objective | REVIEWED | E10 |
| 4.1.1 Participants | REVIEWED | E10 |
| 4.1.2 Material and instruments | REVIEWED | E11 |
| 4.1.3 Procedure | REVIEWED | E11 |
| Figure 5 all 14 PrEmo categories | REVIEWED | E11 |
| 4.1.4 Results and complete Table 1 | REVIEWED | E12 |
| 5 Conclusions/future work, both pages | REVIEWED | E13 |
| Acknowledgements and all 36 reference entries | REVIEWED | E13, E14 |
| All three footnotes, original ontology/FrameNet/toolkit leads | REVIEWED | E05, E07, E08, E14 |

## Common review dimensions

### D1_identity_coverage

All 16 PDF pages/printed1813-1828, five figures, one table, three footnotes and 36 reference entries were read and visually checked. Four authors/year/DOI confirmed at publisher; no appendix or numbered equation occurs. The 2014 paper is not replaced by the missing 2015 work or later cognition-extension files. [REVIEWER_INTERPRETATION; E01, E14, M01, S01]

### D2_problem_contribution

Contribution is a context-aware, multimodal conceptual/OWL framework for emotion detection/expression applications and personalized associations. Restricted full-blown-emotion scope, external/internal representations and contextual descriptions overlap substantially with mental/context/agency conceptualization. The ontology structures knowledge rather than recognizing emotion or proving a universal cognitive theory. [REVIEWER_INTERPRETATION; E02, E04, E05, E08, E09, E13]

### D3_method

Authors cite a classical ontology-engineering methodology, translate model ovals to OWL classes, add restrictions, reuse DOLCE and FrameNet and demonstrate EPF. Detailed requirements/CQs, elicitation sample, full formal axiom set and ontology metric/profile/reasoner results are not reported. Cited methodology year differs from bibliography; no detailed protocol is invented. [REVIEWER_INTERPRETATION; E04, E05, E06, E07, E14]

### D4_requirements

Stated goals include flexible theory adoption, personalization, context and multimodal cues with external/internal/interface separation. Frame-role, self-report, learned association and sadness-media examples provide scenarios; no numbered CQ suite is supplied. Reviewer adverse cases below distinguish target emotion, perceived cue, description and evaluated product response. [REVIEWER_INTERPRETATION; E02, E03, E07, E08, E09, E10, E11]

### D5_concepts

All 39 taxonomy nodes, nine core concepts, fourteen background affective categories, eight EPF labels and fourteen PrEmo labels are inventoried without an eight-item cap. Their populations and intended meanings differ. Situation/Description are reused foundation concepts; typed frame roles and fillers remain distinct. Later extension classes and their definitions are not inferred from these paper labels. [REVIEWER_INTERPRETATION; E02, E04, E06, E07, E08, E09, E11, E12]

### D6_relations_formalization

Seven core property labels and application/frame roles are indexed. Diagram inheritance, contextual reference, inputs/outputs, triggering and association do not become complete DL axioms or executable recognition/learning rules. Source does not print the trigger restriction's exact quantifier. Literal context-arrow directions, sensor-output type differences and sadness example remain unresolved rather than repaired. [REVIEWER_INTERPRETATION; E04, E05, E06, E07, E09]

### D7_grounding

DOLCE reuse is explicit, with dul-prefixed event/process/action/social/physical categories and ofntb:Frame under Description. Exact foundation edition and original formal imports are unknown. Later extension headers directly import legacy DUL/IOLite/ofntb IRIs; no current-version equivalence, accepted alignment or complete imported glossary follows. [REVIEWER_INTERPRETATION; E05, E06, E07, S01, A01, A02]

### D8_artifact_correspondence

Publisher/author links and bounded GitHub repository searches recorded; original and two dated predecessor endpoints not acquired via checked service. Later retained files are identical and header-parsed only, with no full census, imported-definition/profile/reasoner/experiment run. Source files, author guide, missing 2015 paper and original 2014 model stay distinct. [REVIEWER_INTERPRETATION; M01, S01, A01, A02, E05]

### D9_evaluation

Paper reports a task-oriented EPF experience study:14 students, 7 women/7 men, 30 minutes free use and one PrEmo choice. Six admiration/four satisfaction/four fascination selections sum to 14, with other 11 categories zero. This is not recognition accuracy, causal sadness reduction, ontology consistency, general theory validation or independent replication. [REVIEWER_INTERPRETATION; E08, E09, E10, E11, E12, E13]

### D10_critical_synthesis

Strengths include explicit representation/context/input-output distinctions, frame reuse and a concrete application/user-feedback report. Limits include restricted scope, theory-flexibility overreach, ambiguous taxonomy/type mappings, unspecified learning/reasoning, sparse study controls and original-source gaps. Findings feed #239/#253/#126; no automatic conceptual alignment or release/novelty conclusion. [REVIEWER_INTERPRETATION; E02, E04, E05, E06, E08, E09, E10, E11, E12, E13, S01]

## Conceptual catalog

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| C001 / dul:Event | Reused occurring-entity foundation category. Figure 2 outgoing taxonomy targets: none drawn. | REVIEWER_INTERPRETATION; E04, E06 |
| C002 / dul:Process | Reused event considered through its evolution. Figure 2 outgoing taxonomy targets: dul:Event. | REVIEWER_INTERPRETATION; E04, E06 |
| C003 / dul:Action | Reused event with an agent participant; a complete agent/role ontology is not supplied. Figure 2 outgoing taxonomy targets: dul:Event. | REVIEWER_INTERPRETATION; E04, E06 |
| C004 / dul:SocialObject | Foundation generalization for descriptions/situations and verbal expression through the source hierarchy. Figure 2 outgoing taxonomy targets: none drawn. | REVIEWER_INTERPRETATION; E04, E06 |
| C005 / dul:Description | Reused contextual representation of a situation guiding an agent's behavior/emotional response; retain representation versus external arrangement. Figure 2 outgoing taxonomy targets: dul:SocialObject. | REVIEWER_INTERPRETATION; E04, E06 |
| C006 / dul:Situation | Reused recognized/contextualized arrangement of external-world elements; Figure 2 context arrows require correspondence checking. Figure 2 outgoing taxonomy targets: dul:SocialObject, SocialContext, EnvironmentalContext. | REVIEWER_INTERPRETATION; E04, E06 |
| C007 / dul:PhysicalObject | Foundation anchor for sensors and more specific physical categories. Figure 2 outgoing taxonomy targets: none drawn. | REVIEWER_INTERPRETATION; E04, E06 |
| C008 / dul:PhysicalArtifact | Foundation category reused for artificial sensing devices. Figure 2 outgoing taxonomy targets: dul:PhysicalObject. | REVIEWER_INTERPRETATION; E04, E06 |
| C009 / dul:PhysicalAgent | Foundation category appearing in the biological-sensor branch. Figure 2 outgoing taxonomy targets: dul:PhysicalObject. | REVIEWER_INTERPRETATION; E04, E06 |
| C010 / dul:PhysicalBody | Foundation category generalizing the biological-object branch. Figure 2 outgoing taxonomy targets: dul:PhysicalObject. | REVIEWER_INTERPRETATION; E04, E06 |
| C011 / dul:BiologicalObject | Foundation category reused for biological sensors. Figure 2 outgoing taxonomy targets: dul:PhysicalBody. | REVIEWER_INTERPRETATION; E04, E06 |
| C012 / ofntb:Frame | Reused schematic description of a situation/event with participant/property roles; Figure 2 places it under dul:Description. Figure 2 outgoing taxonomy targets: dul:Description. | REVIEWER_INTERPRETATION; E04, E06 |
| C013 / Perception | Organizes sensations using prior experience to generate a description of perceived circumstances. Figure 2 outgoing taxonomy targets: dul:Process. | REVIEWER_INTERPRETATION; E04, E06 |
| C014 / EmergentEmotion | The selected full-blown agent reaction to a situation internally represented by a description; other affective states remain outside the chosen core. Figure 2 outgoing taxonomy targets: dul:Event. | REVIEWER_INTERPRETATION; E04, E06 |
| C015 / Memory | Stores previous experience as descriptions/sensations and links to other descriptions/emotions; no retrieval/update algorithm is specified. Figure 2 outgoing taxonomy targets: dul:Process. | REVIEWER_INTERPRETATION; E04, E06 |
| C016 / Sensation | Internal representation of a stimulus generated by sensing; distinct from the external stimulus and from the perceptual mechanism. Figure 2 outgoing taxonomy targets: dul:Process. | REVIEWER_INTERPRETATION; E04, E06 |
| C017 / Stimulus | External-world input captured by sensors, including output from another emotion-expression system. Figure 2 outgoing taxonomy targets: dul:Event. | REVIEWER_INTERPRETATION; E04, E06 |
| C018 / DiscreteStimulus | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Stimulus. | REVIEWER_INTERPRETATION; E06 |
| C019 / ContinuousStimulus | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Stimulus. | REVIEWER_INTERPRETATION; E06 |
| C020 / Behavioural | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: dul:Action, EmotionExpressionSystem. | REVIEWER_INTERPRETATION; E06 |
| C021 / Gestural | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Behavioural. | REVIEWER_INTERPRETATION; E06 |
| C022 / Speech | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Behavioural. | REVIEWER_INTERPRETATION; E06 |
| C023 / Facial | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Behavioural. | REVIEWER_INTERPRETATION; E06 |
| C024 / Psychophysiological | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: dul:Action, EmotionExpressionSystem. | REVIEWER_INTERPRETATION; E06 |
| C025 / EmotionExpressionSystem | Agent subsystem communicating an emotional state as external stimuli, distinct from an emotion-recognition algorithm. Figure 2 outgoing taxonomy targets: Interface. | REVIEWER_INTERPRETATION; E04, E06 |
| C026 / Verbal | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: dul:Description, EmotionExpressionSystem. | REVIEWER_INTERPRETATION; E06 |
| C027 / SocialContext | Social aspect of context. No independent formal definition is printed; preserve literal incoming Figure 2 Situation arrow. Figure 2 outgoing taxonomy targets: none drawn. | REVIEWER_INTERPRETATION; E04, E06 |
| C028 / EnvironmentalContext | Environmental aspect of context. Prose says modeled using Situation; do not silently reverse the Figure 2 arrow. Figure 2 outgoing taxonomy targets: none drawn. | REVIEWER_INTERPRETATION; E04, E06 |
| C029 / PersonalContext | Personal aspect based on interface/sensor/expression structure; source taxonomy has Interface under this node. Figure 2 outgoing taxonomy targets: none drawn. | REVIEWER_INTERPRETATION; E04, E06 |
| C030 / Interface | Boundary/concept family joining sensing and emotional expression; source has Interface pointing to PersonalContext. Figure 2 outgoing taxonomy targets: PersonalContext. | REVIEWER_INTERPRETATION; E04, E06 |
| C031 / Sensor | Artificial/biological sensing entity converting external stimulus to internal sensation; Figure 2 places it at the physical/interface boundary. Figure 2 outgoing taxonomy targets: Interface, dul:PhysicalObject. | REVIEWER_INTERPRETATION; E04, E06 |
| C032 / ArtificialSensor | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Sensor, dul:PhysicalArtifact. | REVIEWER_INTERPRETATION; E06 |
| C033 / BiologicalSensor | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Sensor, dul:PhysicalAgent, dul:BiologicalObject. | REVIEWER_INTERPRETATION; E06 |
| C034 / Sense | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: BiologicalSensor. | REVIEWER_INTERPRETATION; E06 |
| C035 / Hearing | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Sense. | REVIEWER_INTERPRETATION; E06 |
| C036 / Touch | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Sense. | REVIEWER_INTERPRETATION; E06 |
| C037 / Taste | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Sense. | REVIEWER_INTERPRETATION; E06 |
| C038 / Sight | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Sense. | REVIEWER_INTERPRETATION; E06 |
| C039 / Smell | Diagram-only named specialization; label-based interpretation is not an author definition annotation or sufficient logical characterization. Figure 2 outgoing taxonomy targets: Sense. | REVIEWER_INTERPRETATION; E06 |
| C040 / Attitudes | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C041 / Established emotion | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C042 / Emergent Emotion (full-blown) | Cited affective-state taxonomy label; selected paper focus. | REVIEWER_INTERPRETATION; E02 |
| C043 / Emergent Emotion (suppressed) | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C044 / Moods | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C045 / Partial emotion (topic shifting) | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C046 / Partial emotion (simmering) | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C047 / Stance towards person | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C048 / Stance towards object/situation | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C049 / Interpersonal bonds | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C050 / Altered state of arousal | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C051 / Altered state of control | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C052 / Altered state of seriousness | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C053 / Emotionless | Cited affective-state taxonomy label; not implemented as a complete affective-state taxonomy by this paper. | REVIEWER_INTERPRETATION; E02 |
| C054 / EPF category: joy | One of the eight emotion labels exactly listed for the categorical TUI example; not a universal exhaustive mental-state class or a PrEmo response category. | REVIEWER_INTERPRETATION; E02, E08 |
| C055 / EPF category: acceptance | One of the eight emotion labels exactly listed for the categorical TUI example; not a universal exhaustive mental-state class or a PrEmo response category. | REVIEWER_INTERPRETATION; E02, E08 |
| C056 / EPF category: fear | One of the eight emotion labels exactly listed for the categorical TUI example; not a universal exhaustive mental-state class or a PrEmo response category. | REVIEWER_INTERPRETATION; E02, E08 |
| C057 / EPF category: submission | One of the eight emotion labels exactly listed for the categorical TUI example; not a universal exhaustive mental-state class or a PrEmo response category. | REVIEWER_INTERPRETATION; E02, E08 |
| C058 / EPF category: sadness | One of the eight emotion labels exactly listed for the categorical TUI example; not a universal exhaustive mental-state class or a PrEmo response category. | REVIEWER_INTERPRETATION; E02, E08 |
| C059 / EPF category: disgust | One of the eight emotion labels exactly listed for the categorical TUI example; not a universal exhaustive mental-state class or a PrEmo response category. | REVIEWER_INTERPRETATION; E02, E08 |
| C060 / EPF category: anger | One of the eight emotion labels exactly listed for the categorical TUI example; not a universal exhaustive mental-state class or a PrEmo response category. | REVIEWER_INTERPRETATION; E02, E08 |
| C061 / EPF category: anticipation | One of the eight emotion labels exactly listed for the categorical TUI example; not a universal exhaustive mental-state class or a PrEmo response category. | REVIEWER_INTERPRETATION; E02, E08 |
| C062 / PrEmo: contempt | Product-experience questionnaire label; unpleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C063 / PrEmo: indignation | Product-experience questionnaire label; unpleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C064 / PrEmo: disgust | Product-experience questionnaire label; unpleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C065 / PrEmo: dissatisfaction | Product-experience questionnaire label; unpleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C066 / PrEmo: disappointment | Product-experience questionnaire label; unpleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C067 / PrEmo: unpleasant surprise | Product-experience questionnaire label; unpleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C068 / PrEmo: boredom | Product-experience questionnaire label; unpleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C069 / PrEmo: desire | Product-experience questionnaire label; pleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C070 / PrEmo: inspiration | Product-experience questionnaire label; pleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C071 / PrEmo: admiration | Product-experience questionnaire label; pleasant group, Table 1 count 6. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C072 / PrEmo: satisfaction | Product-experience questionnaire label; pleasant group, Table 1 count 4. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C073 / PrEmo: fascination | Product-experience questionnaire label; pleasant group, Table 1 count 4. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C074 / PrEmo: pleasant surprise | Product-experience questionnaire label; pleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C075 / PrEmo: amusement | Product-experience questionnaire label; pleasant group, Table 1 count 0. Counts are author-reported single choices, not detection-accuracy scores. | REVIEWER_INTERPRETATION; E11, E12 |
| C076 / External world / internal world / interface grouping | Three conceptual regions organizing the nine core concepts; not three additional OWL classes inferred from page layout. | REVIEWER_INTERPRETATION; E04 |
| C077 / Agent / person | Bearer/perceiver/communicator in the conceptual account and User 023 frame example; source provides no complete agency or personal-identity criteria. | REVIEWER_INTERPRETATION; E04, E09 |
| C078 / Context / personalization / multimodality | Context determines available cues and interpretable responses. Personalized associations are not proof of a universal emotion detector. | REVIEWER_INTERPRETATION; E02, E03 |
| C079 / Categorical / dimensional / appraisal theories | Alternative theory families the ontology aims to accommodate; categorical EPF is demonstrated while no separate dimensional/appraisal implementation is evaluated. | REVIEWER_INTERPRETATION; E02, E03 |
| C080 / Subjective / behavioral / psychophysiological channels | User report, observable expression and physiological response channels can disagree or be unavailable. Correlation is motivation, not a measured fusion algorithm. | REVIEWER_INTERPRETATION; E03 |
| C081 / Emotional memory / socialized emotion | Experience and cultural norms can influence or mask expressed affect; observed cue and actual affect cannot automatically be equated. | REVIEWER_INTERPRETATION; E03 |
| C082 / Frame / lexical unit / Frame Element | FrameNet schema, word sense and participant/property role are distinct entities. A role is not its concrete filler. | REVIEWER_INTERPRETATION; E07 |
| C083 / Arriving / enter.v / Theme / Goal | Example frame and lexical unit: Theme is John and Goal is the room in John enters the room. Goal here is a frame role rather than an adopted BDI goal. | REVIEWER_INTERPRETATION; E07 |
| C084 / Feeling / feel.v / experiencer / emotional_state | Figure 4 frame vocabulary with User 023 and sadness; represented emotional content is not a demonstrated recognition result. | REVIEWER_INTERPRETATION; E09 |
| C085 / Cause_to_make_noise / play.v / sound_maker / patient | Figure 4 action-description frame with User 023 and happy song; literal diagram still connects cause to sadness, not a measured successful happiness transition. | REVIEWER_INTERPRETATION; E09 |
| C086 / Emotional State / EmotionalState | Two Figure 4 spellings for sadness-related labels, distinct from the core EmergentEmotion name until exact artifact correspondence is established. | REVIEWER_INTERPRETATION; E09 |
| C087 / EPF / TUI / GUI / Phidgets | Prototype, physical interaction modality, graphical interface and implementation toolkit; not ontology classes solely because a device exists. | REVIEWER_INTERPRETATION; E08, E09 |
| C088 / Picture Area / Feeling Area / emotion-history controls | Figure 3 interface parts: emotional picture/buttons, heart indicator, history buttons, replay and delete; distinguish interface widgets from cognitive categories. | REVIEWER_INTERPRETATION; E08 |
| C089 / Camera / microphone / buttons / screen / speakers | Sensing/self-report and output channels mentioned. Final account emphasizes explicit buttons and screen; no measured automatic multimodal detector is reported. | REVIEWER_INTERPRETATION; E08, E13 |
| C090 / Situation-description-emotion association / bootstrapping | Random favorite pictures/songs gather user responses to contextual descriptions; useful behavior requires initial knowledge. Learning rules/thresholds are not formally specified. | REVIEWER_INTERPRETATION; E08, E09 |
| C091 / PrEmo / forced single choice | Non-verbal product-emotion instrument represented with animated expressions; adapted procedure chooses just one category after 30 minutes, not an intensity or repeated-measure outcome. | REVIEWER_INTERPRETATION; E11 |
| C092 / WordNet / WordNetAffect / emotional cue ontologies | Related lexical and multimodal emotion approaches motivate the contribution, without being silently imported into this model. | REVIEWER_INTERPRETATION; E03 |
| C093 / DOLCE / DUL / FrameNet / ofntb | DOLCE stated grounding, dul-prefixed diagram terms and FrameNet/ofntb reuse; exact foundation editions/imported definitions not established by the paper. | REVIEWER_INTERPRETATION; E05, E06, E07 |
| C094 / Affective-state / disability / social-network extension | Explicit future work beyond the selected full-blown emotion core, not completed current ontology functionality. | REVIEWER_INTERPRETATION; E13 |
| C095 / hasInput / relation | system/process -> input: Sensor->Stimulus, Perception->Sensation and expression-system->EmergentEmotion are Figure 1 examples. Direction is a property toward input, not input causing the subject. | REVIEWER_INTERPRETATION; E04, E05 |
| C096 / hasOutput / relation | system/process -> output: Sensor->Sensation, Perception->Description and expression-system->Stimulus. Figure 4 instead labels a sensor output EmotionalState, which needs typing reconciliation. | REVIEWER_INTERPRETATION; E04, E05, E09 |
| C097 / hasPart / relation | Situation -> Stimulus: Source relation connects contextual situation with stimulus. Properness, temporal parthood and full mereological axioms are not printed. | REVIEWER_INTERPRETATION; E04, E05 |
| C098 / describes / relation | Description -> Situation: Representation/reference relationship, not identity of content with the external arrangement. | REVIEWER_INTERPRETATION; E04, E05 |
| C099 / triggers / relation | Description -> EmergentEmotion: Paper says a restriction types targets, without printing all-only versus some, cardinality or a rule proving causal sufficiency. | REVIEWER_INTERPRETATION; E05 |
| C100 / stores / relation | Memory -> contextual description/emotion structure: Figure 1 grouping and source memory narrative; no reification or memory persistence/update algorithm supplied. | REVIEWER_INTERPRETATION; E04 |
| C101 / uses / relation | Perception -> Memory: Perception is guided by previous experience; not an executable inference or retrieval algorithm. | REVIEWER_INTERPRETATION; E04 |
| C102 / experiencer / emotional_state / relation | Feeling frame -> person / emotional state: Figure 4 role links User 023 and sadness. Roles do not by themselves establish external truth or detection confidence. | REVIEWER_INTERPRETATION; E09 |
| C103 / sound_maker / patient / cause / relation | Cause_to_make_noise frame -> person / song / state: Source action-frame roles and causal label; prose intended affective intervention is not proved by these edges. | REVIEWER_INTERPRETATION; E09 |
| C104 / Theme / Goal / relation | Arriving frame -> moving entity / destination: John/room role-filler example, not a universal relation on every cognitive agent. | REVIEWER_INTERPRETATION; E07 |
| C105 / taxonomy arrows / relation | specific node -> displayed target: Figure 2 source directions preserved, including unusual Situation-to-context arrows. No automatic disjointness, covering, equivalence or accepted import inferred. | REVIEWER_INTERPRETATION; E06 |

## Relations and formal commitments

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| K01 / Restricted affective scope | The full-blown emergent-emotion case is selected from a broader taxonomy; do not call the core a complete model of all affect or internal emotional processing. | REVIEWER_INTERPRETATION; E02 |
| K02 / Theory flexibility versus demonstration | Authors aim at categorical/dimensional/appraisal neutrality. Demonstrated categorical application does not verify all alternative theory mappings. | REVIEWER_INTERPRETATION; E02, E03, E08 |
| K03 / Nine model ovals as classes | Source states all Figure 1 ovals become OWL classes; diagram arrows/prose do not specify a complete profile, full axiom set or machine population. | REVIEWER_INTERPRETATION; E04 |
| K04 / Input/output/reference distinctions | External stimulus, internal sensation, process and contextual description have separate roles. hasInput/hasOutput orientation must not be inverted into an ontology-generated classifier. | REVIEWER_INTERPRETATION; E04, E05 |
| K05 / Description trigger restriction | Targets of Description triggers are EmergentEmotion in the example restriction. Exact DL quantification/existence/causal strength is not printed; no some/only formula is invented. | REVIEWER_INTERPRETATION; E05 |
| K06 / Foundation and frame reuse | DOLCE Description/Situation contextualize the model; ofntb:Frame is drawn under dul:Description. Exact upper-ontology edition/import closure remains an artifact question. | REVIEWER_INTERPRETATION; E05, E06, E07 |
| K07 / Literal context arrows | Figure 2 shows dul:Situation pointing to SocialContext/EnvironmentalContext and Interface pointing to PersonalContext. Retain drawing/prose ambiguity rather than silently asserting the reverse hierarchy. | REVIEWER_INTERPRETATION; E06 |
| K08 / Sensor and expression specializations | Taxonomy includes physical and interface multiple inheritance and process/event expression categories; joint satisfiability and type commitments require exact source definitions. | REVIEWER_INTERPRETATION; E06 |
| K09 / Frame role versus filler | Arriving Theme=John and Goal=room distinguish semantic role from its instance; Figure 4 similarly separates person, emotion-state and action/song fields. | REVIEWER_INTERPRETATION; E07, E09 |
| K10 / Recognition excluded from ontology role | Authors explicitly say ontology models emotion associations but does not recognize emotional responses; sensor recognition is an external capability. | REVIEWER_INTERPRETATION; E09 |
| K11 / Association bootstrapping | Random favorites and explicit user responses seed situation/emotion associations; no formal learning objective, confidence threshold or executable rule set supplied. | REVIEWER_INTERPRETATION; E08, E09 |
| K12 / Intervention is not observed causal success | Sadness detection followed by formerly happy-associated media is intended behavior; source drawing labels sadness and study does not measure a controlled sadness-to-happiness effect. | REVIEWER_INTERPRETATION; E08, E09, E10, E12 |
| K13 / PrEmo outcome boundary | Fourteen students use EPF freely 30 minutes then choose one experience category; result is count 6 admiration, 4 satisfaction, 4 fascination, not emotion-recognition accuracy. | REVIEWER_INTERPRETATION; E10, E11, E12 |
| K14 / Extension/version boundary | Later Emotions & Cognition files and missing 2015 paper remain separate. Identical two-path retained extension bytes are not an original 2014 release or independent validation. | REVIEWER_INTERPRETATION; S01, A01, A02 |

## Complete paper relation index

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| R01 / hasInput | system/process -> input: Sensor->Stimulus, Perception->Sensation and expression-system->EmergentEmotion are Figure 1 examples. Direction is a property toward input, not input causing the subject. | REVIEWER_INTERPRETATION; E04, E05 |
| R02 / hasOutput | system/process -> output: Sensor->Sensation, Perception->Description and expression-system->Stimulus. Figure 4 instead labels a sensor output EmotionalState, which needs typing reconciliation. | REVIEWER_INTERPRETATION; E04, E05, E09 |
| R03 / hasPart | Situation -> Stimulus: Source relation connects contextual situation with stimulus. Properness, temporal parthood and full mereological axioms are not printed. | REVIEWER_INTERPRETATION; E04, E05 |
| R04 / describes | Description -> Situation: Representation/reference relationship, not identity of content with the external arrangement. | REVIEWER_INTERPRETATION; E04, E05 |
| R05 / triggers | Description -> EmergentEmotion: Paper says a restriction types targets, without printing all-only versus some, cardinality or a rule proving causal sufficiency. | REVIEWER_INTERPRETATION; E05 |
| R06 / stores | Memory -> contextual description/emotion structure: Figure 1 grouping and source memory narrative; no reification or memory persistence/update algorithm supplied. | REVIEWER_INTERPRETATION; E04 |
| R07 / uses | Perception -> Memory: Perception is guided by previous experience; not an executable inference or retrieval algorithm. | REVIEWER_INTERPRETATION; E04 |
| R08 / experiencer / emotional_state | Feeling frame -> person / emotional state: Figure 4 role links User 023 and sadness. Roles do not by themselves establish external truth or detection confidence. | REVIEWER_INTERPRETATION; E09 |
| R09 / sound_maker / patient / cause | Cause_to_make_noise frame -> person / song / state: Source action-frame roles and causal label; prose intended affective intervention is not proved by these edges. | REVIEWER_INTERPRETATION; E09 |
| R10 / Theme / Goal | Arriving frame -> moving entity / destination: John/room role-filler example, not a universal relation on every cognitive agent. | REVIEWER_INTERPRETATION; E07 |
| R11 / taxonomy arrows | specific node -> displayed target: Figure 2 source directions preserved, including unusual Situation-to-context arrows. No automatic disjointness, covering, equivalence or accepted import inferred. | REVIEWER_INTERPRETATION; E06 |

## Requirements, examples and adverse cases

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| S01 / John enters the room | Arriving/enter.v with Theme John and Goal room demonstrates role/filler context modeling, not an adopted BDI planning goal. | REVIEWER_INTERPRETATION; E07 |
| S02 / Sensor stimulus-to-sensation | A sensor captures external stimulus and outputs internal sensation; physical event and mental representation must stay distinct. | REVIEWER_INTERPRETATION; E04 |
| S03 / Perception with memory | Perception organizes sensation using previous descriptions/experiences; a plausible cognitive schema is not a reproduced neural processing model. | REVIEWER_INTERPRETATION; E04 |
| S04 / Expression and feedback loop | An agent expression system creates stimulus that another sensor may receive; generic connectivity does not guarantee correct emotion communication. | REVIEWER_INTERPRETATION; E04, E08 |
| S05 / Explicit emotion button | Sad-button input labels a user report; that is not independent ground truth for automatic recognition accuracy. | REVIEWER_INTERPRETATION; E08, E09 |
| S06 / Random media bootstrapping | Favorite pictures/songs seed associations before useful response behavior; no training-set size, convergence or confidence metric is supplied. | REVIEWER_INTERPRETATION; E08, E09 |
| S07 / Sadness then happy-associated media | Rule-like response is proposed from prior personalized associations; no controlled observed happiness change is measured. | REVIEWER_INTERPRETATION; E08, E09, E12 |
| S08 / Figure4 literal sadness chain | Both source EmotionalState labels are sadness and the sensor output is an emotional state. Do not rewrite it to happiness or Sensation to manufacture correspondence. | REVIEWER_INTERPRETATION; E09 |
| S09 / Multimodal cue disagreement | Spoken/facial/physiological cues and self-report may conflict or be masked culturally. Ontology membership alone cannot resolve uncertainty or fuse evidence. | REVIEWER_INTERPRETATION; E03 |
| S10 / Affective category outside focus | A mood or interpersonal bond is mentioned in the background taxonomy but is not thereby implemented by the full-blown-emotion core. | REVIEWER_INTERPRETATION; E02, E13 |
| S11 / Context hierarchy direction | Literal dul:Situation-to-SocialContext/EnvironmentalContext and Interface-to-PersonalContext arrows require source/version reconciliation; no automatic reversal is justified. | REVIEWER_INTERPRETATION; E06 |
| S12 / No trigger occurrence from an unspecified restriction | A prose typed-target restriction does not reveal universal/existential choice, temporal precedence or causal sufficiency. | REVIEWER_INTERPRETATION; E05 |
| S13 / Role versus participant identity | A Goal frame role with room filler does not identify the lexical role with a room individual, agent intention or generic mental goal. | REVIEWER_INTERPRETATION; E07 |
| S14 / Study positive experience | Fourteen selected responses all belong to positive PrEmo categories; the observed outcome is product experience within this sample/procedure. | REVIEWER_INTERPRETATION; E10, E11, E12 |
| S15 / Forced single choice with mixed experience | A participant with several simultaneous feelings still selects one; zero counts in eleven categories do not prove absence of every other affective response. | REVIEWER_INTERPRETATION; E11, E12 |
| S16 / Unseen population or long-term outcome | A small student sample after 30 minutes does not establish cultural/disability/age generalization or sustained therapeutic/emotional benefit. | REVIEWER_INTERPRETATION; E02, E10, E11, E13 |
| S17 / Unsupported alternative theory | Dimensional/appraisal compatibility is claimed as design flexibility, not empirically demonstrated merely by a categorical EPF application. | REVIEWER_INTERPRETATION; E02, E03, E08 |
| S18 / Later file versus original paper | Identical retained later cognition-extension files can be parsed independently, but cannot stand in for missing original 2014 bytes or the missing 2015 paper. | REVIEWER_INTERPRETATION; S01, A01, A02 |

## Critical findings

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| F01 / Useful conceptual distinctions | External situation/stimulus, internal sensation/description and processing/interface structure provide substantial prior knowledge representation beyond emotion labels. | REVIEWER_INTERPRETATION; E04, E05 |
| F02 / Context and frame reuse | DOLCE descriptions/situations and FrameNet roles give reusable contextual structure. Exact class/instance/role mapping still requires original-source technical inspection. | REVIEWER_INTERPRETATION; E05, E06, E07 |
| F03 / Restricted scope versus broad claims | The core selects full-blown emergent emotion and emphasizes detection/expression systems. General affective/cognitive completeness is explicitly outside scope. | REVIEWER_INTERPRETATION; E02, E13 |
| F04 / Theory independence not jointly validated | Categorical use and multiple theory citations do not test all dimensional/appraisal commitments or their joint consistency. | REVIEWER_INTERPRETATION; E02, E03, E08 |
| F05 / Ontology is not emotion detector | Authors explicitly limit ontology to modeling/associating emotion and descriptions. Broader sensor language is not a reported classifier benchmark. | REVIEWER_INTERPRETATION; E08, E09, E13 |
| F06 / Original formalization quantifiers unknown | The paper gives typed relations and a trigger restriction example but no full numbered DL/FOL axioms, cardinalities, global characteristics or executable rule set. Do not silently turn prose into some/only. | REVIEWER_INTERPRETATION; E05 |
| F07 / Literal context hierarchy ambiguity | Figure 2 Situation-to-context arrows and Interface-to-PersonalContext need correspondence assessment; prose motivation is not permission to reverse source arrows. | REVIEWER_INTERPRETATION; E06 |
| F08 / Mixed event/object/interface typing | Sensation/Memory/Perception under Process, EmergentEmotion under Event and physical/interface sensor inheritance impose nontrivial commitments. No joint imported-model satisfiability result is reported. | REVIEWER_INTERPRETATION; E06 |
| F09 / Figure4 type and vocabulary gaps | EmotionalState versus EmergentEmotion, sensor output versus Sensation and frame-instance schemas differ from core terminology. No equivalence/type repair is supplied by the paper. | REVIEWER_INTERPRETATION; E04, E09 |
| F10 / Intended response is not causal success | Sadness-triggered happy-associated media and cause labels do not establish an effective emotion-changing intervention; source figure retains sadness and experiment measures experience. | REVIEWER_INTERPRETATION; E08, E09, E10, E12 |
| F11 / Learning and cold start underspecified | Bootstrapping is acknowledged; no operational algorithm, thresholds, uncertainty, contradictory-association policy or complete training/test data is given. | REVIEWER_INTERPRETATION; E08, E09 |
| F12 / Study population and outcome bound | 14 computer-science students, balanced reported sex counts, 30-minute free use and one emotion choice evaluate the EPF product. No ontology-expert agreement, recognition accuracy or formal consistency outcome is measured. | REVIEWER_INTERPRETATION; E10, E11, E12 |
| F13 / Counts versus scores | Table 1 gives 6 admiration/4 satisfaction/4 fascination and eleven zeros, totaling 14. The prose word scores should not be promoted into continuous ratings, effect sizes or accuracy. | REVIEWER_INTERPRETATION; E12 |
| F14 / Study controls and generalization | No reported control/comparator, random allocation, baseline emotion measurement, raw participant responses or statistical uncertainty accompanies this study. Selection and short duration limit broader claims. | REVIEWER_INTERPRETATION; E10, E11, E12 |
| F15 / Two emotion-label populations | Eight EPF labels, including literal submission, differ from fourteen PrEmo product-experience labels and the initial affective taxonomy. Do not merge them into one measured ontology population. | REVIEWER_INTERPRETATION; E02, E08, E11, E12 |
| F16 / Original versus later sources | Author guide distinguishes older EmotionsOnto from cognition extension. Identical later file hashes/direct imports do not prove historical fidelity or independent validation; original file availability remains bounded. | REVIEWER_INTERPRETATION; S01, A01, A02 |
| F17 / Editorial/bibliographic ambiguities | Introduction references sec.4.2 though evaluation is4/4.1, García 2006 differs from bibliography 2010, and toolkit URL is misspelled. Retain exact source names and unresolved references rather than inventing corrected authority. | REVIEWER_INTERPRETATION; E02, E08, E14 |
| F18 / Reuse decision remains deferred | Paper-level overlap and user-experience result support later comparison, not accepted Clariceptify mappings, a full source glossary, expert adequacy, manuscript novelty or a new release. | REVIEWER_INTERPRETATION; E01, E13, S01 |

## Unresolved questions

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Q01 / Original source and all-class population | Recover or delimit exact 2014 EmotionsOnto version versus2010/2013/2015 predecessors and later cognition extension. Inventory EVERY selected local/external/referenced/deprecated class and definition/missing state; no eight-class sampling or summed duplicate versions. | REVIEWER_INTERPRETATION; E05, S01, A01, A02 |
| Q02 / Foundations and imports | Pin legacy DUL/IOLite/ofntb imports and unresolved definitions separately from original-paper grounding, FrameNet role/category semantics and edition claims. Preserve no-import-versus-unacquired distinction. | REVIEWER_INTERPRETATION; E06, E07, A01, A02 |
| Q03 / Taxonomy correspondence | Reconcile all 39 Figure 2 nodes/arrows, multiple inheritance and context directions against exact bytes without repairing author sources; test representative positive and adverse type cases. | REVIEWER_INTERPRETATION; E04, E06 |
| Q04 / Inputs, outputs and triggering | Inspect every selected property domain/range/restriction and source quantifier; distinguish stimulus/sensation/emotion-state, Description triggers and causal/existence assumptions. | REVIEWER_INTERPRETATION; E04, E05, E09 |
| Q05 / Frame roles and representation levels | Trace Frame/Description, Arriving and Feeling/Cause_to_make_noise examples with role/filler identity, lexical units and ontology instance/class levels; keep Goal frame role distinct from adopted planning goals. | REVIEWER_INTERPRETATION; E07, E09 |
| Q06 / Contextual learning/agency boundary | Determine which memory, agency, personalization and rule/association commitments are actually formalized or only application logic, including conflicting observations and cold start. | REVIEWER_INTERPRETATION; E03, E04, E08, E09 |
| Q07 / Execution and evaluation evidence | Inventory supplied datasets/tests/code and run only declared reproducible profile/reasoner/query checks with tool/input/expected-observed evidence; missing 2015 full paper affects its own historical/comparison claims, not all independent file parsing. Do not call PrEmo responses recognition or causal efficacy. | REVIEWER_INTERPRETATION; E09, E10, E11, E12, A01, A02 |
| Q08 / Version/license and comparison export | Keep identical later retained paths one byte population, record source-specific license limits and historical correspondence gaps, and export bounded findings to #253/#126 without semantic acceptance or model changes. | REVIEWER_INTERPRETATION; E01, E13, S01, A01, A02 |

## Inputs for later synthesis

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Y01 / Prior contextual/mental architecture | Compare Description/Situation, process/representation, memory and frame-role grounding as substantial prior conceptualization structure; avoid novelty claims based only on different emotion terminology. | REVIEWER_INTERPRETATION; E04, E05, E06, E07 |
| Y02 / Evidence-function separation | Use EPF example and PrEmo study to distinguish application feasibility/product response from ontology verification/validation, recognition accuracy and causal effectiveness. | REVIEWER_INTERPRETATION; E08, E09, E10, E11, E12 |
| Y03 / Candidate adverse bank | Preserve conflicting cues, unknown restriction quantifiers, reversed context arrows, frame-role/filler mixing, stale associations and categorical-versus-instrument labels as future candidate tests, not adopted fixtures. | REVIEWER_INTERPRETATION; E03, E05, E06, E07, E09, E11 |
| Y04 / Technical and synthesis routing | All 12 acquired-paper dossiers can now be complete; #239 technical, #253 comparison and #126 synthesis remain open. Seven missing texts are still access gaps; independent acquired artifact work continues with #250/#241 and foundations. | REVIEWER_INTERPRETATION; E01, E13, S01 |
| Y05 / Owner boundary | All reuse/extension is DEFER_TO_OWNER_AFTER_SYNTHESIS. No ontology, requirement, fixture, manuscript, release or accepted mapping change is authorized by this review. | REVIEWER_INTERPRETATION; E13 |

## Evaluation evidence

- **Verification:** OWL modeling and restrictions are described, but original full formal-file/profile/reasoner/unit-test results are not reported in this paper. This review hashes input/rendered pages and parses later retained header metadata only. No ontology solver or EPF/recognition code was executed. [REVIEWER_INTERPRETATION; E04, E05, E06, A01, A02]
- **Validation:** Frame examples and concrete device use support intended representational feasibility; no independent ontology-expert sampling/agreement or full competency-query validation suite is reported. EPF product-experience responses do not certify conceptual correctness. [REVIEWER_INTERPRETATION; E07, E08, E09, E10, E11]
- **Evaluation:** Author-reported14-person/30-minute/single-choice PrEmo study gives6/4/4 positive selections and eleven zeros. It measures experience of this product under this procedure, without a comparator or recognition/causal benchmark. No independent replication or numeric ontology metric table is provided. [REVIEWER_INTERPRETATION; E10, E11, E12]
- **Assessment:** Strengths are contextual/multimodal conceptual structure and explicit recognition limitation. Reviewer findings delimit theory-neutrality claims, ambiguous taxonomy/types, unspecified learning, study confounds and historical-source gaps; no cross-corpus adequacy rank is assigned. [REVIEWER_INTERPRETATION; E02, E03, E06, E08, E09, E12, E13, S01]
- **Assurance:** Publisher DOI/title/dates, retained hashes and author-version leads support provenance. Original file/license/import identity, complete class glossaries, imported definitions and reproducible semantic tests remain #239. Structural integrity checks protect Clariceptify bytes but do not confer independent expert or clinical acceptance. [REVIEWER_INTERPRETATION; E01, E05, E13, M01, S01, A01, A02]

## Artifact and repository boundary

Technical follow-up: #239. State: `ORIGINAL_FILE_UNACQUIRED_LATER_EXTENSION_HEADERS_PARSED_TECHNICAL_WORK_OPEN`.

Exact paper ontology endpoint and older author-linked2013/02/2015/05 candidates could not be acquired in checked search-service opens. Two finite GitHub repository queries found no candidate; no global absence claim. Retained later EmotionsCognition-2015.owl/current.owl have identical SHA 256, no versionInfo and direct legacy DUL/IOLite/ofntb imports. Those bytes are not automatically the 2014 proposal or the missing 2015 full paper. #239 retains original correspondence, every selected class/definition/import and eight deeper questions. Existing #77 paper dependency remains; independent acquired-file inspection is allowed within the shared contract.

## Evidence index

| ID | Exact source locator | Source-grounded summary |
|---|---|---|
| E01 | Printed1813/PDF1 title, four authors, dates, abstract, keywords and copyright | J.UCS 20(13), 1813-1828; submitted 15 January 2014, accepted 6 September 2014, appeared 28 November 2014. Article scope is a generic emotion/detection/expression/context model, not the later cognition extension. |
| E02 | Complete sec.1 Introduction, taxonomy/scope, theories and application motivation | Fourteen affective-state categories cited; focus restricted to full-blown Emergent Emotion and detection/expression rather than internal human processing. Context, personalization, theory flexibility, DOLCE/FrameNet and EPF introduced. |
| E03 | Complete sec.2 and 2.1 Related Work | Categorical/dimensional/appraisal theories; subjective, behavioral and psychophysiological channels; culture/socialization/context and multimodality; WordNetAffect, speech and contextual ontology examples. These are related work, not executed comparisons. |
| E04 | Sec.3 Contribution: methodology, core definitions and Figure 1 | Classical engineering methodology cited, OWL classes for diagram ovals; external world, interface and internal world with nine core concepts. Figure 1 has seven distinct property labels and a feedback model. |
| E05 | Sec.3 property/restriction paragraph, DOLCE grounding and footnote 1 | hasInput/hasOutput/hasPart/describes/triggers/stores/uses; Description triggers targets EmergentEmotion, without a printed DL quantifier. Author ontology URL provided, original bytes not thereby established. |
| E06 | Complete Figure 2 and surrounding foundational/context discussion | Thirty-nine named taxonomy nodes:27 non-prefixed, 11 dul-prefixed and ofntb:Frame. Event/process/action/object categories, expression/sensor specializations and contexts. Literal Situation-to-context and Interface-to-PersonalContext arrows are retained, not repaired. |
| E07 | FrameNet discussion and John-enters-room example; footnote 2 | Frame is modeled under Description; enter.v/Arriving has Theme=John and Goal=room. Lexical unit, frame, role and filler remain different representation levels. |
| E08 | Sec.4 EPF architecture, interfaces and learning behavior; Figure 3; footnote 3 | Phidgets prototype, Picture/Feeling areas, buttons, heart/history/replay/delete controls, camera/microphone possibilities and picture/music outputs. Eight printed Plutchik labels include submission. Random favorites seed user associations; sadness-to-happy-content response described. |
| E09 | Complete Figure 4, caption and explicit modeling-versus-recognition limitation | Sad button input and Emotion/Feeling/Cause_to_make_noise frame example; diagram has EmotionalState sadness labels. Paper explicitly says ontology does not recognize emotions; initial knowledge needed for useful behavior. |
| E10 | Sec.4.1 study purpose and 4.1.1 Participants | Experience of EPF stimuli evaluated in 14 computer-science students at University of Cauca, Colombia: seven women/seven men. No classifier test set or ontology-expert sample claimed. |
| E11 | Complete 4.1.2 Materials/instruments, 4.1.3 Procedure and Figure 5 | PrEmo uses 14 product-experience emotions: seven pleasant/seven unpleasant. Free use for 30 minutes followed by one emotion selection per participant; not repeated intensity scores or a multi-label recognition benchmark. |
| E12 | Complete 4.1.4 Results and Table 1 | All 14 counts inspected: admiration 6, satisfaction 4, fascination 4, all 11 remaining categories 0. Total 14 agrees with participants; positive selections describe reported experience, not verified emotion detection or causal efficacy. |
| E13 | Complete sec.5 Conclusions/future work and Acknowledgements | Broader theory/technology utility claimed; conclusion describes explicit emotion buttons and screen outputs. Extension beyond EmergentEmotion, disability-aware models and social networks remain future work. |
| E14 | All 36 bibliography entries and three paper footnotes | All entries read. Method citation García 2006 differs from bibliography García 2010; intro Neyem 2007 versus Collazos 2007 and Douglas-Cowie 2005 versus other keys remain editorial uncertainties. Phidgets footnote URL is printed phidgtes.com; no silent correction or execution inferred. |
| M01 | Publisher exact title/authors/DOI metadata accessed 2026-10-28 | Official four-author 2014 work and DOI confirmed; exact retained PDF remains primary reading input. |
| S01 | Author guide: current/2015/12 cognition extension versus older EmotionsOnto links; accessed 2026-10-28 | Explicit author distinction supports predecessor/extension boundary; original 2014 equivalent file not established. |
| A01 | EmotionsCognition-2015.owl retained header, RDFLib metadata-only parse | Later extension ontology IRI, no versionInfo and legacy DUL/IOLite/ofntb imports; the two paths have identical retained SHA 256. Not the 2014 original or an independently validated release. |
| A02 | EmotionsCognition-current.owl retained header, RDFLib metadata-only parse | Later extension ontology IRI, no versionInfo and legacy DUL/IOLite/ofntb imports; the two paths have identical retained SHA 256. Not the 2014 original or an independently validated release. |

## Closure boundary

Complete exact-paper #262 only after relevant checks and merged PR. All-class/definition/import/profile/semantic work remains OPEN #239; missing 2015 paper #77 remains distinct. Comparison #253 and final synthesis #126 remain open. All 12 acquired-paper readings may then be complete, while seven missing primary texts and independent artifact/comparison work remain unfinished. No Clariceptify ontology, requirements, fixtures, manuscript, release or adoption decision changes.
