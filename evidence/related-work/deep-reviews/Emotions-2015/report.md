# Emotions ontology for collaborative modelling and learning of emotional responses

Work: `Emotions-2015` | Issue: #77 | State: `REVIEW_COMPLETE`

Reviewed version: Computers in Human Behavior51PartB610-617,2015; online6March2015, issueOctober2015. Input: `Emotions-2015-owner.pdf`, 8 PDF pages, SHA256 `d819de5d40446fd924ea3eba41f3e5edbfc21850120a4ce2716765523745c69c`.

The structured `review.yaml` is the evidence authority; this report is derived. This is an AI-assisted critical review, not independent expert acceptance. Clariceptify is unchanged; later use requires an owner decision.

## Identity and reading coverage

Exact8-page published owner PDF, separate from2014 predecessor and later cognition implementation. Public institutional PDF has different bytes and is not substituted. ArticleCCBY4.0 does not establish an OWL source license.

Complete paper ontology-bearing concepts,39taxonomy labels,all7figures/10notes/38references and formal/application/evaluation distinctions.28candidate local classes are a separate current-source inventory, with1comment/27missing and unknown imported/historical populations.

| Paper unit | Coverage | Evidence |
|---|---|---|
| Front matter/title/abstract | REVIEWED | E01 |
| Section1Introduction | REVIEWED | E02 |
| Section2Relatedwork | REVIEWED | E03 |
| Section2.1Emotionontologies | REVIEWED | E03 |
| Section3Contribution | REVIEWED | E04, E05 |
| Section4Evaluation | REVIEWED | E08, E09 |
| Section4.1BCI | REVIEWED | E10 |
| Section5Conclusions/futurework | REVIEWED | E12 |
| Acknowledgements | REVIEWED | E12 |
| References38entries | REVIEWED | E13 |
| All10numberednotes | REVIEWED | E14 |
| No numbered formulas/tables/appendices | REVIEWED | E14 |
| Figure1 | REVIEWED | E06 |
| Figure2 | REVIEWED | E07 |
| Figure3 | REVIEWED | E08 |
| Figure4 | REVIEWED | E08 |
| Figure5 | REVIEWED | E09 |
| Figure6 | REVIEWED | E11 |
| Figure7 | REVIEWED | E11 |

## Common review dimensions

### D1_identity_coverage

Exact8-page four-author2015journal610-617, DOI10.1016/j.chb.2014.11.100; all units/figures/notes/references inspected. Independent from2014 and later cognition source. [REVIEWER_INTERPRETATION; E01, E14, E17]

### D2_problem_contribution

Context-sensitive flexible representation and structured collaborative emotion input; ontology models rather than detects emotion. BCI recognition is ongoing/future. [REVIEWER_INTERPRETATION; E02, E08, E09, E10, E12]

### D3_method

Named García2006 classical methodology, conceptual model to OWLclasses/properties/restrictions, DOLCE/FrameNet reuse and EmoCS demonstration; the thesis is cited, not wholly executed/reviewed here. [REVIEWER_INTERPRETATION; E04, E05, E08]

### D4_requirements

Flexibility across people/cultures/theories,context,multimodal input and reuse motivate the model. No numbered CQ suite or original controlled validation protocol is supplied. [REVIEWER_INTERPRETATION; E02, E03, E08, E12]

### D5_concepts

All39 taxonomy labels,14background affect labels and source-bearing process/context/role/measurement distinctions cataloged. Paper terms and28candidate root classes remain separate. [REVIEWER_INTERPRETATION; E02, E05, E07, E10, E15]

### D6_relations_formalization

All figure relation labels/role bindings and prose restrictions indexed. No numbered axioms. Selected root only/exactly restrictions and referenced imported-name constraints are separate source evidence, not a silently completed paper theory. [REVIEWER_INTERPRETATION; E04, E06, E07, E08, E09, E15]

### D7_grounding

DOLCE family and FrameNet contextualization are explicit; exact edition unknown. Agent/role,expression/description/situation and observed/input/state levels require care; broad internal cognition is outside current paper scope. [REVIEWER_INTERPRETATION; E02, E05, E08, E09, E15]

### D8_artifact_correspondence

Selected author-linked Maycandidate28classes/6object/3data properties, one comment27missing, complete local constraints and raw annotation reconciliation. Three legacy imports unacquired; original-release equivalence and later-cognition parity not assumed. [REVIEWER_INTERPRETATION; E15, E16]

### D9_evaluation

EmoCS screenshots and SDKmanual annotation support author-reported feasibility; no quantified participant/recognition/causal result. Fourmetric families and future six targets are distinct; no2014PrEmo results imported. [REVIEWER_INTERPRETATION; E08, E09, E10, E11, E12, E14]

### D10_critical_synthesis

Contextual role-based input is a useful comparison candidate; formal range/witness,definition/import,measurement/conflict and version limits remain239/253/126. Next84limited summary, no model/manuscript/release adoption. [REVIEWER_INTERPRETATION; E05, E09, E10, E15, E16]

## Conceptual catalog

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| C001 / dul:Event | The author describes an Event as anything occurring in the model. Figure2 category with literal parent arrows: no parent arrow shown. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C002 / dul:Process | The author characterizes Process as an event considered in its evolution. Figure2 category with literal parent arrows: dul:Event. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C003 / dul:Action | The author characterizes Action as an event with at least one participating agent. Figure2 category with literal parent arrows: dul:Event. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C004 / dul:SocialObject | Figure2 category with literal parent arrows: no parent arrow shown. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C005 / dul:Description | The author uses Description for a representation of a situation. Figure2 category with literal parent arrows: dul:SocialObject. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C006 / dul:Situation | Situations provide the represented contextual configurations; the prose says social/environmental contexts are modeled with Situation, while the drawing arrows have the literal directions recorded here. Figure2 category with literal parent arrows: dul:SocialObject, SocialContext, EnvironmentalContext. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C007 / dul:PhysicalObject | Figure2 category with literal parent arrows: no parent arrow shown. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C008 / dul:PhysicalArtifact | Figure2 category with literal parent arrows: dul:PhysicalObject. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C009 / dul:PhysicalAgent | Figure2 category with literal parent arrows: dul:PhysicalObject. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C010 / dul:PhysicalBody | Figure2 category with literal parent arrows: dul:PhysicalObject. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C011 / dul:BiologicalObject | Figure2 category with literal parent arrows: dul:PhysicalBody. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C012 / ofntb:Frame | A frame represents a typical situation with participant/property roles and specializes Description in the drawing. Figure2 category with literal parent arrows: dul:Description. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C013 / Perception | The conceptual loop takes Sensation as input, uses Memory and produces Description; it is not a completed internal human-cognition theory. Figure2 category with literal parent arrows: dul:Process. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C014 / EmergentEmotion | Selected scope is the short-lived full-blown whole-system response; the model connects it to a contextual Description and expression interface. Figure2 category with literal parent arrows: dul:Event. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C015 / Memory | The conceptual loop stores descriptions/emotional associations and is used by Perception; a storage/update algorithm is not supplied. Figure2 category with literal parent arrows: dul:Process. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C016 / Sensation | Sensor output that feeds Perception in the conceptual loop; not the stimulus or interpreted emotion itself. Figure2 category with literal parent arrows: dul:Process. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C017 / Stimulus | An event-like part of a situation sensed at the interface and also produced by expression systems in the conceptual loop. Figure2 category with literal parent arrows: dul:Event. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C018 / DiscreteStimulus | Figure2 category with literal parent arrows: Stimulus. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C019 / ContinuousStimulus | Figure2 category with literal parent arrows: Stimulus. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C020 / Behavioural | Figure2 category with literal parent arrows: dul:Action, EmotionExpressionSystem. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C021 / Gestural | Figure2 category with literal parent arrows: Behavioural. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C022 / Speech | Figure2 category with literal parent arrows: Behavioural. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C023 / Facial | Figure2 category with literal parent arrows: Behavioural. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C024 / Psychophysiological | Figure2 category with literal parent arrows: dul:Action, EmotionExpressionSystem. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C025 / EmotionExpressionSystem | An interface accepting emergent-emotion input and producing stimulus output, specialized into the displayed expression channels. Figure2 category with literal parent arrows: Interface. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C026 / Verbal | Prose treats verbal expression as social/descriptive representation; the drawing specializes both Description and EmotionExpressionSystem. Figure2 category with literal parent arrows: dul:Description, EmotionExpressionSystem. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C027 / SocialContext | Prose associates social context with Situation; the literal drawing/selected root makes DULSituation a subtype of SocialContext. Figure2 category with literal parent arrows: no parent arrow shown. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C028 / EnvironmentalContext | Prose associates environmental context with Situation; the literal drawing/selected root makes DULSituation a subtype of EnvironmentalContext. Figure2 category with literal parent arrows: no parent arrow shown. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C029 / PersonalContext | Prose associates personal context with interfaces that include sensing and expression; the drawing direction is retained rather than repaired. Figure2 category with literal parent arrows: no parent arrow shown. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C030 / Interface | Common interface category for Sensor and EmotionExpressionSystem; the literal drawing classifies Interface under PersonalContext. Figure2 category with literal parent arrows: PersonalContext. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C031 / Sensor | A physical interface accepting stimuli and providing sensations in the conceptual loop; source-only restrictions do not require an actual reading. Figure2 category with literal parent arrows: Interface, dul:PhysicalObject. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07, E02, E06 |
| C032 / ArtificialSensor | Figure2 category with literal parent arrows: Sensor, dul:PhysicalArtifact. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C033 / BiologicalSensor | Figure2 category with literal parent arrows: Sensor, dul:PhysicalAgent, dul:BiologicalObject. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C034 / Sense | Figure2 category with literal parent arrows: BiologicalSensor. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C035 / Hearing | Figure2 category with literal parent arrows: Sense. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C036 / Touch | Figure2 category with literal parent arrows: Sense. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C037 / Taste | Figure2 category with literal parent arrows: Sense. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C038 / Sight | Figure2 category with literal parent arrows: Sense. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C039 / Smell | Figure2 category with literal parent arrows: Sense. This is a paper taxonomy label, not proof of an original machine declaration, sufficient definition or accepted mapping. | REVIEWER_INTERPRETATION; E05, E07 |
| C040 / Affective-state scope | Fourteen broad labels are background scope; the implemented focus is full-blown emergent emotion, not a comprehensive mind ontology. | REVIEWER_INTERPRETATION; E02 |
| C041 / Emergent emotion(full-blown) | Short-lived whole-system response to a person or situation, including feelings, impulses and bodily change; this is the selected source scope, not every affective state. | REVIEWER_INTERPRETATION; E02 |
| C042 / Emotion theory agnosticism | Design intention to accommodate alternative theories without binding developers to one; compatibility of every theory is not experimentally established. | REVIEWER_INTERPRETATION; E02, E03, E04 |
| C043 / Categorical theory | Background theoretical family exemplified by Ekman; six-category EEG detection is future work rather than the present measured output. | REVIEWER_INTERPRETATION; E03, E10, E12 |
| C044 / Dimensional theory | Background Lang family mentioned; no complete implemented dimensional scheme, shared scale or calibrated coordinate mapping is printed. | REVIEWER_INTERPRETATION; E03 |
| C045 / Appraisal theory | Background Scherer family mentioned; no complete appraisal calculus or automatic event-appraisal-to-emotion procedure is supplied. | REVIEWER_INTERPRETATION; E03 |
| C046 / Subjective/verbal information | User descriptions of perceived feelings; self-report is an observation channel, not infallible access to an internal state. | REVIEWER_INTERPRETATION; E03, E08 |
| C047 / Behavioral cues | Facial/postural/paralinguistic expression channels; availability varies by context and does not uniquely determine the underlying emotion. | REVIEWER_INTERPRETATION; E03 |
| C048 / Physiological cues | Heart rate, skin response and EEG are possible correlates; representation is distinct from validated emotional recognition. | REVIEWER_INTERPRETATION; E03, E10, E12 |
| C049 / Emotional affordance | Perceived characteristics of a situation affecting emotion; a motivating application notion, not an operational causal-effect metric in the paper. | REVIEWER_INTERPRETATION; E02 |
| C050 / Socialized emotional response | Cultural/social expression may mask a person's affective state, limiting naïve interpretation of visible or self-reported cues. | REVIEWER_INTERPRETATION; E03 |
| C051 / Personalization | Individual/cultural variation motivates flexible context-aware modeling; no complete learned personalization mechanism or calibration evaluation is supplied. | REVIEWER_INTERPRETATION; E02, E03, E12 |
| C052 / Multimodal context | Relevant channels, environment, social setting and person matter; ontology support does not by itself implement sensor fusion or conflict resolution. | REVIEWER_INTERPRETATION; E03, E05 |
| C053 / FrameNet frame | Schematic situation with participant/property roles, modeled under Description in Figure2; distinct from lexical unit, concrete event and role filler. | REVIEWER_INTERPRETATION; E05, E07 |
| C054 / Lexical unit | Word sense such as enter.v selecting Arriving; label-to-frame selection does not prove a uniquely identified real-world event. | REVIEWER_INTERPRETATION; E05, E08 |
| C055 / Frame element | Participant/property role such as Theme or Goal; not automatically an entity, adopted goal or full n-ary relation implementation. | REVIEWER_INTERPRETATION; E05 |
| C056 / Arriving | Example frame selected by enter.v, with John as Theme and room as destination Goal; an illustration, not a tested competency suite. | REVIEWER_INTERPRETATION; E05 |
| C057 / Feeling | Example frame with experiencer and emotional_state roles; the user, frame instance, emotion label and actual internal state are separate levels. | REVIEWER_INTERPRETATION; E09 |
| C058 / Cause_to_make_noise | Example play.v frame connecting a sound maker, song patient and emotional-state cause; illustrative role binding, not a verified causal rule. | REVIEWER_INTERPRETATION; E09 |
| C059 / Description versus situation | A representation is distinguished from what it describes; the phrase that an uploaded image constitutes a situation needs care about image/content/referent levels. | REVIEWER_INTERPRETATION; E05, E08 |
| C060 / Emotion association | Collected relation between structured situation descriptions and emotions; correlation/labeling is not proof of detection or causal affect change. | REVIEWER_INTERPRETATION; E08, E09 |
| C061 / EmotionalState figure label | Figure5 spelling differs from EmergentEmotion taxonomy; no complete printed equivalence establishes that they are the same released class. | REVIEWER_INTERPRETATION; E07, E09 |
| C062 / Emotion Common Sense / EmoCS | Collaborative structured-input application inspired by OMCS, with emotional sliders, frame-driven forms and multimedia/RDF storage. | REVIEWER_INTERPRETATION; E08 |
| C063 / Open Mind Common Sense / OMCS | Background initiative with comparatively free-text common-sense input; not an imported ontology or validation dataset for this review. | REVIEWER_INTERPRETATION; E08 |
| C064 / Autocomplete and dynamic form | FrameNet candidates and selected frame elements structure user entry; a UI affordance, not independent semantic correctness or measured efficiency. | REVIEWER_INTERPRETATION; E08 |
| C065 / Structured assertion | Description plus role fillers and emotion annotations stored for later application use; no provenance/confidence/disagreement schema is fully printed. | REVIEWER_INTERPRETATION; E08, E09 |
| C066 / Multimedia input | Images/audio/URLs can be associated with descriptions and emotions; media object, interpreted content and situation referent are not automatically identical. | REVIEWER_INTERPRETATION; E08 |
| C067 / RDF store / reasoning / query answering | Application capability is author-reported; no store version, exact query workload, expected-observed proof log or reasoner run is reproduced here. | REVIEWER_INTERPRETATION; E08 |
| C068 / Emotional bootstrapping | Initial emotional knowledge is needed for usefulness/continued participation; no quantitatively evaluated cold-start solution is supplied. | REVIEWER_INTERPRETATION; E09 |
| C069 / Reactive happy-media response | Example selects songs/images associated with happiness after sadness input; not a randomized intervention or demonstrated causal improvement. | REVIEWER_INTERPRETATION; E09 |
| C070 / Brain-computer interface / BCI | Measurement/integration discipline used in the application exploration; not itself the ontology or a validated emotional categorizer. | REVIEWER_INTERPRETATION; E10 |
| C071 / EEG | Historical brain-signal input contrasted with fMRI temporal/spatial properties; source claims are not current device recommendations or clinical validation. | REVIEWER_INTERPRETATION; E10 |
| C072 / Emotiv neuroheadset | Historical14-sensor device with named suites and scalp locations; photographs and SDK profile are not participant-count or accuracy evidence. | REVIEWER_INTERPRETATION; E10, E11 |
| C073 / Expressiv / Affectiv / Cognitiv | Historical device suites for different processed outputs; exact capabilities are source-reported, not newly benchmarked here. | REVIEWER_INTERPRETATION; E10 |
| C074 / SDK-mediated manual annotation | Investigators transcribed processed display outputs because direct emotional output was not accessible outside the SDK; automatic six-emotion recognition is not the reported pipeline. | REVIEWER_INTERPRETATION; E10, E11 |
| C075 / Excitement ambiguity | Vendor-named output may increase for fear or surprise; no uniquely identified emotion follows from its label. | REVIEWER_INTERPRETATION; E10 |
| C076 / Six Ekman targets | Anger,disgust,fear,happiness,sadness,surprise are future classifier targets; no six-class accuracy, confusion matrix or trained-model result is published. | REVIEWER_INTERPRETATION; E10, E12 |
| C077 / Training examples and direct feedback | Situations/expected emotions/user feedback are described as being collected/used in ongoing ML work; data size, splits and final performance remain unspecified. | REVIEWER_INTERPRETATION; E12 |
| C078 / Skin conductance complement | A proposed additional stress-related signal to improve future robustness; no completed multimodal classifier experiment is reported. | REVIEWER_INTERPRETATION; E12 |
| C079 / Future affective states/user models | Broader affect, disabilities, social settings and adaptive user models are future extensions, not completed coverage of every background affective category. | REVIEWER_INTERPRETATION; E12 |
| C080 / OWL modeling method | Classes from ovals, properties from arrows, restrictions and upper-ontology reuse are explicit construction steps; the García2006 methodology is cited, not reproduced in full. | REVIEWER_INTERPRETATION; E04, E05 |
| C081 / Selected May2015 OWL candidate | Author-linked predecessor used for a complete28-local-class inventory; date path is not an immutable release or verified publication-byte identity. | REVIEWER_INTERPRETATION; E15, E16 |
| C082 / Later cognition extension | Different namespace and changed categories including Motivation; December/current paths share bytes and cannot be counted as two versions or the original2015 paper artifact. | REVIEWER_INTERPRETATION; E16 |
| C083 / Source comment availability | Selected28 classes include one comment candidate and27explicit missing comments; paper-level definitions and reviewer constraint analyses are separate from author OWL definitions. | REVIEWER_INTERPRETATION; E15 |
| C084 / Context root class(candidate) | Selected candidate additionally declares Context, absent from the27 unprefixed taxonomy labels;39paper nodes and28root declarations have different boundaries. | REVIEWER_INTERPRETATION; E07, E15 |
| C085 / Attitudes | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C086 / Established emotion | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C087 / Emergent Emotion(full-blown) | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C088 / Emergent Emotion(suppressed) | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C089 / Moods | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C090 / Partial emotion(topic shifting) | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C091 / Partial emotion(simmering) | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C092 / Stance towards person | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C093 / Stance towards object/situation | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C094 / Interpersonal bonds | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C095 / Altered state of arousal | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C096 / Altered state of control | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C097 / Altered state of seriousness | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |
| C098 / Emotionless | One of14 background affective labels quoted in the introduction scope discussion; only full-blown emergent emotion is the selected model focus. This is not a declared14-class machine taxonomy. | AUTHOR_REPORTED; E02 |

## Relations and formal commitments

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| K001 / Restricted affective scope | The paper chooses full-blown emergent emotion instead of claiming coverage of the complete affective-state taxonomy. | REVIEWER_INTERPRETATION; E02 |
| K002 / Theory-flexibility objective | Categorical, dimensional and appraisal theories motivate agnosticism; the text supplies no universal compatibility proof or complete instantiated mapping for all three. | REVIEWER_INTERPRETATION; E02, E03, E04 |
| K003 / Class/property construction | Figure1 ovals become OWL classes and relation arrows become object properties; additional restrictions enrich the model. | REVIEWER_INTERPRETATION; E04, E06 |
| K004 / Trigger restriction in prose | The Description-to-EmergentEmotion example states a target type without printing a quantifier; do not silently make it an existential causal rule. | REVIEWER_INTERPRETATION; E04 |
| K005 / Upper-ontology grounding | DOLCE family and Description/Situation reuse are explicit; exact legacy edition and historical import identity require separate evidence. | REVIEWER_INTERPRETATION; E05 |
| K006 / Frame specialization | Figure2 shows ofntb:Frame as a Description subtype; formal correspondence with the selected ofntb import is not proved by the diagram alone. | REVIEWER_INTERPRETATION; E05, E07 |
| K007 / Literal context direction | Figure2 DULSituation has outgoing subclass arrows to SocialContext/EnvironmentalContext; Interface points to PersonalContext. Preserve the source rather than reverse the arrows. | REVIEWER_INTERPRETATION; E07 |
| K008 / Multiple inheritance | Sensor, biological/artificial sensor and expression channels have multiple parents; imported disjointness/compatibility must be assessed on an exact module version. | REVIEWER_INTERPRETATION; E07, E15 |
| K009 / Input-output loop | Sensing/perception/expression relations organize a conceptual loop; no explicit timing, automatic state estimation or causal fusion procedure is printed. | REVIEWER_INTERPRETATION; E06 |
| K010 / Frame role identity | Arriving Goal is a destination frame role; goal in the Torres sentence is a scored-object filler, not a BDI goal or adopted plan. | REVIEWER_INTERPRETATION; E05, E08 |
| K011 / User-entered emotional association | EmoCS stores structured frame/emotion input and multimedia references; this does not establish truth, unique interpretation, consensus or individual calibration. | REVIEWER_INTERPRETATION; E08 |
| K012 / Representation boundary | Figure4 sentence/description and Figure5 instance labels are illustrative; no complete URI-bound instance graph or alias equivalence is printed. | REVIEWER_INTERPRETATION; E08, E09 |
| K013 / Emotion recognition exclusion | The text explicitly says the ontology models associations and does not recognize emotional responses; do not promote storage/UI modeling into a detector. | REVIEWER_INTERPRETATION; E09 |
| K014 / SDK manual output | Reported BCI annotations are manual after inspecting the SDK display, using four metric families that do not match an established emotion classification. | REVIEWER_INTERPRETATION; E10, E11 |
| K015 / Future six-class model | Raw EEG collection/training and six-Ekman output are ongoing/future, without sample count, evaluation splits or recognition performance. | REVIEWER_INTERPRETATION; E10, E12 |
| K016 / Source-candidate universals | Selected Mayroot uses allValuesFrom for sensory/perception/expression/memory outputs, including global Description triggers; these do not alone require any linked filler. | REVIEWER_INTERPRETATION; E15 |
| K017 / Datatype cardinalities | DiscreteStimulus threshold and continuous range bounds each have exactly-one float cardinality; no numerical ordering, measurement validity or continuous/discrete disjointness is supplied. | REVIEWER_INTERPRETATION; E15 |
| K018 / Referenced external-name constraints | Selected root globally constrains imported DULDescription/Situation IRIs despite not declaring them as named owl:Class locally; their outgoing constraints are separately indexed. | REVIEWER_INTERPRETATION; E15 |
| K019 / Missing source definitions | All28 local classes are accounted for, but27 have no rdfs:comment. Reviewer hierarchy summaries do not become author natural-language definitions. | REVIEWER_INTERPRETATION; E15 |
| K020 / Version and import boundary | Three declared legacy imports are unacquired as this exact closure; current DUL/IOLite cannot silently replace them. Later cognition bytes and selected Mayroot are separate populations. | REVIEWER_INTERPRETATION; E15, E16 |
| K021 / Application validation limit | Screenshots/use examples support feasibility of represented interactions, not measured emotion improvement, ontology consistency, adoption or independent user validation. | REVIEWER_INTERPRETATION; E08, E09, E10, E11, E12 |
| K022 / No numbered formal theory | No numbered DL/FOL axioms or complete executable constraint listing is printed in the paper. Selected external source assertions are separately attributed, not presented as paper formulas. | REVIEWER_INTERPRETATION; E04, E14, E15 |

## Complete paper relation index

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| R001 / hasInput | Sensor takes Stimulus, Perception takes Sensation, expression system takes emotion; selected source class restrictions are universal, not domain/range declarations or causal existence. | REVIEWER_INTERPRETATION; E06, E15 |
| R002 / hasOutput / hasOuput | Sensor produces sensations, Perception outputs Description, expression systems output stimuli. Figure5 misspells hasOuput; do not assert a formal alias by typography alone. | REVIEWER_INTERPRETATION; E06, E09, E15 |
| R003 / hasPart | Situation-to-Stimulus in the drawing and selected DULSituation restriction; mereological part is not automatic semantic content, causal responsibility or setting membership. | REVIEWER_INTERPRETATION; E06, E15 |
| R004 / describes | Description-to-Situation and illustrative sentence descriptions; distinguish expression/content/referent levels and absence of complete identity rules. | REVIEWER_INTERPRETATION; E05, E06, E08, E09 |
| R005 / triggers | Description-to-emotion link; paper prose omits quantification, selected candidate is only restriction. Neither alone implements affect recognition or proves causal triggering. | REVIEWER_INTERPRETATION; E04, E06, E15 |
| R006 / uses | Perception-to-Memory; no existence or calibrated memory retrieval process is supplied by only restriction. | REVIEWER_INTERPRETATION; E06, E15 |
| R007 / stores | Memory associations/descriptions; selected source limits fillers to Description but does not supply persistence, confidence or learning-update policy. | REVIEWER_INTERPRETATION; E06, E15 |
| R008 / Frame/lexical-unit selection | enter.v selects Arriving; autocomplete selects candidate frames and frame elements. These are not automatically disambiguated real-world assertions. | REVIEWER_INTERPRETATION; E05, E08 |
| R009 / Theme / Goal | Arriving ThemeJohn/Goalroom; Goal is destination role. Torres Themegoal is an object-like filler, not a desired-plan goal. | REVIEWER_INTERPRETATION; E05, E08 |
| R010 / Recipient / Result / Time | Torres score example binds RecipientTorres,Resultwinning,Timeinlastminute. No global cardinality or temporal theory is established by the illustration. | REVIEWER_INTERPRETATION; E08 |
| R011 / experiencer / emotional_state | Feeling frame relates User023 and sadness label; participant, frame and emotion state are distinct modeling levels. | REVIEWER_INTERPRETATION; E09 |
| R012 / sound_maker / patient / cause | Play frame relates User023,happysong and sadness as cause role; no automatic causal intervention-success proof. | REVIEWER_INTERPRETATION; E09 |
| R013 / Subclass links | All39 taxonomy label/arrow records retained literally; selected Mayroot has28 local declarations and additional referenced DUL constraints. No inferred class equivalence. | REVIEWER_INTERPRETATION; E07, E15 |
| R014 / produces(candidate-only) | Declared object property has no selected domain/range or used restriction in the inspected root; do not add it to the printed Figure1 relation labels. | REVIEWER_INTERPRETATION; E15 |
| R015 / threshold / rangeLow / rangeHigh(candidate-only) | Float-valued datatype properties, exact-one restrictions on corresponding stimulus classes; no required bound ordering or measurement calibration. | REVIEWER_INTERPRETATION; E15 |

## Requirements, examples and adverse cases

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| S001 / John enters room | AUTHOR EXAMPLE: enter.v selects Arriving; ThemeJohn and Goalroom bind participants without making the destination an adopted goal. | REVIEWER_INTERPRETATION; E05 |
| S002 / Torres score | AUTHOR EXAMPLE: RecipientTorres,Resultwinning,Themegoal,Timeinlastminute organize a description; no participant identity or truth proof follows from a word label. | REVIEWER_INTERPRETATION; E08 |
| S003 / Manual slider response | AUTHOR EXAMPLE: a user chooses a frame and emotional slider input. This is a recorded self-report association, not objective decoded mental state. | REVIEWER_INTERPRETATION; E08 |
| S004 / Incomplete autocomplete | ADVERSE RECONSTRUCTION: an offered frame or role can be wrong or ambiguous; structured input alone does not resolve word sense or real-world truth. | REVIEWER_INTERPRETATION; E05, E08 |
| S005 / Sadness and happy song | AUTHOR EXAMPLE: a system can respond to sadness input with media associated with happiness; the paper supplies no causal improvement measurement. | REVIEWER_INTERPRETATION; E09 |
| S006 / Image and situation | ADVERSE RECONSTRUCTION: a photograph is an informational/physical item representing a situation; the paper's shorthand does not justify identifying every image with its referent. | REVIEWER_INTERPRETATION; E08 |
| S007 / Cultural masking | AUTHOR QUALIFICATION: social expression may mask internal affect; visible action, self-report and actual state may disagree. | REVIEWER_INTERPRETATION; E03 |
| S008 / Conflicting channels | ADVERSE RECONSTRUCTION: verbal happiness and physiological arousal require fusion/uncertainty policy not supplied by a generic multimodal graph. | REVIEWER_INTERPRETATION; E03, E10 |
| S009 / Fear versus surprise | AUTHOR QUALIFICATION: Excitement can increase for either state; metric label alone cannot identify one emotion. | REVIEWER_INTERPRETATION; E10 |
| S010 / SDK transcription | AUTHOR REPORTED PROCEDURE: researchers inspect Affectiv output and manually annotate descriptions; this is not an exported automatic six-category classifier. | REVIEWER_INTERPRETATION; E10, E11 |
| S011 / Five screenshot traces | ADVERSE RECONSTRUCTION: instantaneous and long-term excitement are two traces within one metric family; do not invent a fifth independent categorical emotion. | REVIEWER_INTERPRETATION; E10, E11 |
| S012 / Headset user photograph | ADVERSE RECONSTRUCTION: an illustrated person or SDK profile does not establish sample size, consent protocol, experiment population or model accuracy. | REVIEWER_INTERPRETATION; E11 |
| S013 / Unreported study sample | ADVERSE RECONSTRUCTION: do not import the14-person PrEmo2014 study into this2015 paper; participant count and recognition accuracy remain unspecified here. | REVIEWER_INTERPRETATION; E10, E12, E14 |
| S014 / Cold start | AUTHOR QUALIFICATION: the useful association base needs bootstrapping to retain users; no measured cold-start or reinforcement-learning performance is supplied. | REVIEWER_INTERPRETATION; E09 |
| S015 / Different users/same situation | ADVERSE RECONSTRUCTION: one shared description can accompany different emotional responses; ontology storage alone does not produce a per-person calibrated predictor. | REVIEWER_INTERPRETATION; E02, E03, E08 |
| S016 / No linked sensor input | ADVERSE SOURCE ANALYSIS: selected Sensor input only Stimulus allows no input links; no sensing event or stimulus existence follows from the universal restriction. | REVIEWER_INTERPRETATION; E15 |
| S017 / No triggered emotion | ADVERSE SOURCE ANALYSIS: global Description triggers only EmergentEmotion allows descriptions with no triggers; it is not a mandatory emotional reaction or causal law. | REVIEWER_INTERPRETATION; E15 |
| S018 / Invalid continuous bounds | ADVERSE SOURCE ANALYSIS: exactly-one float low/high does not impose low<=high or unit calibration; arbitrary reversed bounds are not excluded by those restrictions alone. | REVIEWER_INTERPRETATION; E15 |
| S019 / Both stimulus kinds | ADVERSE SOURCE ANALYSIS: no explicit disjointness in this root prevents an entity being continuous and discrete; full imported consequences remain untested. | REVIEWER_INTERPRETATION; E15 |
| S020 / All situations typed as contexts | ADVERSE SOURCE ANALYSIS: referenced DULSituation subclass statements apply globally to social/environmental contexts, rather than only a local emotional situation subtype. | REVIEWER_INTERPRETATION; E07, E15 |
| S021 / Uncommented class | ADVERSE RECONSTRUCTION:27root classes lack comments; descriptive hierarchy summaries can be useful without being labeled author definitions. | REVIEWER_INTERPRETATION; E15 |
| S022 / Later motivation extension | ADVERSE VERSION CASE: December/current cognition paths contain later categories under another namespace; do not substitute them for the publication artifact or count identical bytes twice. | REVIEWER_INTERPRETATION; E15, E16 |
| S023 / Future six-emotion recognition | AUTHOR FUTURE CASE: collecting EEG/training examples and adding skin conductance are proposed/ongoing; six-class success requires a future dataset/evaluation, not ontology import. | REVIEWER_INTERPRETATION; E10, E12 |
| S024 / No imported closure | ADVERSE SOURCE CASE: declared DUL/IOLite/ofntb imports are not a completed exact legacy closure or imported glossary; current editions cannot silently supply historical results. | REVIEWER_INTERPRETATION; E15, E16 |

## Critical findings

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| F001 / Exact independent source | This four-author8-page2015 journal paper differs from the16-page2014 predecessor, its PrEmo evaluation and the later December cognition extension. | REVIEWER_INTERPRETATION; E01, E14, E16, E17 |
| F002 / Contextual modeling strength | The model explicitly joins situation descriptions, sensing channels, memory and emotion expression, helping avoid a flat list of emotion labels. | REVIEWER_INTERPRETATION; E02, E05, E06 |
| F003 / Structured collaborative input | FrameNet-guided forms and roles provide a concrete interaction path for structured emotion associations rather than unrestricted text alone. | REVIEWER_INTERPRETATION; E08 |
| F004 / Emotion versus detection | The paper explicitly separates modeling associations from recognizing emotion; storing an emotion label is not an emotion-classification result. | REVIEWER_INTERPRETATION; E09 |
| F005 / Theory agnostic is an objective | Categorical/dimensional/appraisal flexibility is a design goal, without complete instantiated mappings or comparative evaluation of every theoretical model. | REVIEWER_INTERPRETATION; E02, E03, E04 |
| F006 / Restricted affective coverage | Full-blown emergent emotion is selected; broader moods, stances, bonds and other affective categories are background or future work. | REVIEWER_INTERPRETATION; E02, E12 |
| F007 / Foundation evidence | DOLCE family,Description/Situation and FrameNet reuse are explicit. No exact foundational software edition follows from the family name or unversioned import paths. | REVIEWER_INTERPRETATION; E05, E15, E16 |
| F008 / Literal context direction | Figure2 DULSituation-to-SocialContext/EnvironmentalContext and Interface-to-PersonalContext arrows must not be silently inverted; selected Maysource repeats these directions. | REVIEWER_INTERPRETATION; E07, E15 |
| F009 / Paper versus local class population | Figure2 has39 labels including12prefixed categories; selected candidate has28local declarations, including Context. Neither count is the original full imported/inferred ontology population. | REVIEWER_INTERPRETATION; E07, E15 |
| F010 / Multiple inheritance scope | BiologicalSensor has a PhysicalAgent parent in Figure2 but not in the selected root. Imported inference might add consequences, but none has been run or presumed. | REVIEWER_INTERPRETATION; E07, E15 |
| F011 / Frame role distinctions | Arriving Goal is a destination role, score Themegoal a filler and Feeling experiencer a participant; these are not interchangeable with BDI goals, agents or classes. | REVIEWER_INTERPRETATION; E05, E08, E09 |
| F012 / Figure spelling/type gaps | Figure1 Stimuli and Figure5 EmotionalState/hasOuput differ from other names. Plausible aliases or typography repairs are not printed formal equivalences. | REVIEWER_INTERPRETATION; E06, E09, E15 |
| F013 / Expression/content/referent | Description, sentence/media, frame and represented situation must be distinguished; the image-as-situation shorthand is not a sufficient identity theory. | REVIEWER_INTERPRETATION; E05, E08 |
| F014 / OWL quantifier distinction | Paper trigger prose is unquantified; candidate uses allValuesFrom, so only restrictions do not generate inputs, outputs, memories or emotions. | REVIEWER_INTERPRETATION; E04, E15 |
| F015 / Global imported-name side effects | The selected root constrains imported DULDescription and DULSituation names without local owl:Class declarations. A local-only class census alone would omit these outgoing assertions. | REVIEWER_INTERPRETATION; E15 |
| F016 / Missing source definitions | All28candidate local classes/constraints are accounted for: one source comment candidate,27missing. Reviewer paper/hierarchy explanations do not fill the author-comment field. | REVIEWER_INTERPRETATION; E15 |
| F017 / Prototype evidence limit | Screenshots and worked examples support representation/interaction feasibility; no reported controlled user study, confusion matrix, benchmark or operational ontology-consistency log is supplied. | REVIEWER_INTERPRETATION; E08, E09, E10, E11, E12, E14 |
| F018 / Manual BCI procedure | SDK outputs were manually transcribed into annotations. The automatic six-Ekman pipeline remains ongoing/future rather than a demonstrated result. | REVIEWER_INTERPRETATION; E10, E11, E12 |
| F019 / Four metric families | Excitement,Frustration,Meditation,Engagement/Boredom are proprietary metric names with acknowledged ambiguity. Five plotted traces include two excitement timescales, not five discrete emotions. | REVIEWER_INTERPRETATION; E10, E11 |
| F020 / No borrowed participant count | Neither one person in a photograph nor the predecessor's14PrEmo students establishes this2015 study sample; participants,training size,calibration and accuracy are unreported here. | REVIEWER_INTERPRETATION; E10, E11, E12, E14 |
| F021 / Learning/data limits | Collaborative entry and ongoing raw EEG training are not a reproducible complete learning algorithm, public dataset, split protocol or evaluation result. | REVIEWER_INTERPRETATION; E08, E10, E12 |
| F022 / Intervention claims limited | The sadness-to-happy-media example does not demonstrate beneficial emotion change or MOOC dropout reduction; association and causal intervention are separate. | REVIEWER_INTERPRETATION; E02, E09, E12 |
| F023 / Cold-start/conflict/provenance gaps | Bootstrapping is acknowledged; the paper does not provide complete per-user/disagreement/confidence/provenance/time-update handling or validated multimodal fusion. | REVIEWER_INTERPRETATION; E03, E08, E09, E12 |
| F024 / Datatype constraints are limited | Exact-one float thresholds/bounds do not encode numerical ordering, units, calibration, stimulus disjointness or a causal threshold detector. | REVIEWER_INTERPRETATION; E15 |
| F025 / Selected version availability | Direct byte retrieval recovered previously unacquired2013/May candidates despite unsupported search-service content type. Date paths and asserted graph isomorphism are not immutable historical release identity. | REVIEWER_INTERPRETATION; E15, E16 |
| F026 / License and reproducibility | ArticleCCBY4.0 does not establish a linked OWL license. Exact legacy imports, original publication bytes and profile/reasoner results remain unestablished; source review does not imply adoption. | REVIEWER_INTERPRETATION; E01, E15, E16 |
| F027 / Candidate relevance | Descriptions/situations, role-based contextualization and separation of observed inputs from interpreted state can inform later comparison and terminology; no accepted mapping, novelty judgment or model change is made. | REVIEWER_INTERPRETATION; E05, E06, E08, E09 |

## Unresolved questions

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Q001 / Exact root and class source | In239, keep selectedMay2015 and later cognition extension separate from exact2014/2015 publication artifacts. All28local candidate declarations/definition gaps are accounted for, without original-byte fidelity. | REVIEWER_INTERPRETATION; E01, E15, E16 |
| Q002 / Legacy foundations/imports | In239, pin the exact three legacy DUL/IOLite/ofntb imports, resolve class definitions within a stated scope and record unavailable versions; never silently replace them with current editions. | REVIEWER_INTERPRETATION; E05, E15, E16 |
| Q003 / Taxonomy and inheritance | In239, test selected context directions and BiologicalSensor multiple inheritance on the exact closure, retaining all39drawing labels and source differences. | REVIEWER_INTERPRETATION; E07, E15 |
| Q004 / Inputs/outputs/triggers | In239, test representative only-versus-existence cases and global DULDescription/Situation restrictions; datatype cardinality is not bound ordering, causal triggering or recognition. | REVIEWER_INTERPRETATION; E04, E06, E15 |
| Q005 / Frame and participant levels | In239, trace lexical units,frames,roles and fillers for Arriving,Feeling and play; destination Goal and score-object goal are not adopted planning goals. | REVIEWER_INTERPRETATION; E05, E08, E09 |
| Q006 / Memory and personalization | In239, identify which memory,agency,conflict,bootstrapping and per-user commitments are formalized versus application logic, with positive and adverse cases. | REVIEWER_INTERPRETATION; E03, E06, E08, E09, E15 |
| Q007 / Execution and evaluation | In239, retain SDKmanual annotations/fourmetrics and future six-Ekman model separately; run only reproducible declared tests with tools/inputs/expected-observed results. No2014study transfer. | REVIEWER_INTERPRETATION; E10, E11, E12, E14 |
| Q008 / Version/license/comparison export | In239, preserve byte-distinct predecessor receipts and duplicate later paths, clarify licenses and export selected evidence to253/126 without full equivalence, semantic acceptance or model adoption. | REVIEWER_INTERPRETATION; E01, E15, E16 |

## Inputs for later synthesis

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Y001 / Context and representation | Compare Description/Situation, information/media, role/filler and observed/interpreted state levels using exact source versions and contrary evidence. | REVIEWER_INTERPRETATION; E05, E06, E08, E09 |
| Y002 / Agency and goals | Frame participants and destination roles are not a theory of agency or adopted intentions; use ArrivingGoal and scoreThemegoal as adverse mapping cases. | REVIEWER_INTERPRETATION; E05, E08 |
| Y003 / Affective evidence level | Separate self-report,behavioral/physiological correlates, proprietary metrics, represented emotion and validated recognition/performance. | REVIEWER_INTERPRETATION; E03, E08, E10, E11 |
| Y004 / Formal source scope | Bind only/exactly restrictions and imported-name side effects to the selected Maycandidate; original-paper count and inferred taxonomy remain unknown. | REVIEWER_INTERPRETATION; E04, E07, E15 |
| Y005 / Future test candidates | Retain empty sensor input,untriggered description,conflicting channels,invalid bounds and per-user differences for later bounded technical work. | REVIEWER_INTERPRETATION; E03, E09, E10, E15 |
| Y006 / Ordered next use | Paper77 can close after merged checks.239technical and253comparison stay open; next is owner-authorized limited-summary84, then evidence-qualified synthesis/comparison work under actual prerequisites. | REVIEWER_INTERPRETATION; E12, E15, E16 |

## Evaluation evidence

- **Verification:** Paper describes OWL restrictions and RDF reasoning but gives no independently reproduced reasoner/profile or consistency log. Reviewer executes candidate parsing/census, all28 local definition-or-missing/constraint reviews and raw annotation/hierarchy reconciliation only. [REVIEWER_INTERPRETATION; E04, E08, E15]
- **Validation:** EmoCS worked input examples/screenshots and BCI annotation procedure motivate application fit; no specified participant population or controlled ontology-adequacy/recognition study is reported. [REVIEWER_INTERPRETATION; E08, E09, E10, E11, E14]
- **Evaluation:** Participant count,training-set size,recognition accuracy,calibration,comparative performance and causal emotion/dropout improvement are not reported in the selected paper. Six-emotion recognition and added skin sensors are ongoing/future. [NOT_REPORTED; E10, E12, E14]
- **Assessment:** Empty only-restriction fillers,invalid bounds,role/goal distinction,masked/conflicting cues,metric ambiguity and media/situation levels are reviewer adverse cases, not executed whole-theory models or user experiments. [REVIEWER_INTERPRETATION; E03, E05, E08, E09, E10, E15]
- **Assurance:** Selected owner PDF,public metadata,author candidate digests,full7figure ledger and28class source-gap inventory are pinned. Exact publication artifact,legacy closure/license,independent expert acceptance and semantic validation remain unestablished. [REVIEWER_INTERPRETATION; E01, E14, E15, E16, E17]

## Artifact and repository boundary

Technical follow-up: #239. State: `SELECTED_MAY_CANDIDATE_LOCAL_GLOSSARY_COMPLETE_IMPORT_VERSION_SEMANTICS_OPEN`.

Author-linkedMay2015 predecessor has28 local classes, one source comment27missing, all local constraints reviewed. It is not certified exact publication bytes. Literal context directions and global referenced DULDescription/Situation assertions are retained. Three legacy imports remain unacquired; later cognition namespace/root is distinct. December/current URLs have identical bytes and count as one later population. Source graph/byte comparison is not a reasoner or historical-equivalence result.

### All28 classes in the selected author-linked May2015 candidate

| ID / class | Manual constraint/correspondence review | Evidence |
|---|---|---|
| A001 / ArtificialSensor | Sensor and DULPhysicalArtifact; source provides no natural-language definition or existence of a reading. | REVIEWER_INTERPRETATION; E15 |
| A002 / Behavioural | EmotionExpressionSystem and DULAction; spelling is British in this candidate, unlike later Behavioral. | REVIEWER_INTERPRETATION; E15 |
| A003 / BiologicalSensor | Sensor and DULBiologicalObject; does not assert the DULPhysicalAgent superclass drawn in Figure2. | REVIEWER_INTERPRETATION; E15 |
| A004 / Context | Declared without superclass, equivalent definition or comment; do not invent an author definition. | REVIEWER_INTERPRETATION; E15 |
| A005 / ContinuousStimulus | Stimulus with exactly one rangeLow and rangeHigh float value each; no high-greater-than-low constraint or disjointness from DiscreteStimulus. | REVIEWER_INTERPRETATION; E15 |
| A006 / DiscreteStimulus | Stimulus with exactly one float threshold; no converse threshold-based definition or disjointness from ContinuousStimulus. | REVIEWER_INTERPRETATION; E15 |
| A007 / EmergentEmotion | DULEvent subtype; no specific categorical emotion taxonomy, recognition algorithm or empirical criterion in the class declaration. | REVIEWER_INTERPRETATION; E15 |
| A008 / EmotionExpressionSystem | Interface with hasInput only EmergentEmotion and hasOutput only Stimulus; universals require neither input nor output existence. | REVIEWER_INTERPRETATION; E15 |
| A009 / EnvironmentalContext | Context subclass; only source comment candidate characterizes an objective reference frame, without a sufficient logical definition. | REVIEWER_INTERPRETATION; E15 |
| A010 / Facial | Behavioural subtype only; no face detector, dataset or expression-to-emotion mapping is provided. | REVIEWER_INTERPRETATION; E15 |
| A011 / Gestural | Behavioural subtype only; no gesture recognition constraints or measurement protocol. | REVIEWER_INTERPRETATION; E15 |
| A012 / Hearing | Sense with hasInput only ContinuousStimulus; no existential input requirement. | REVIEWER_INTERPRETATION; E15 |
| A013 / Interface | PersonalContext superclass, matching the literal arrow direction; do not silently reverse it to PersonalContext-is-Interface. | REVIEWER_INTERPRETATION; E15 |
| A014 / Memory | DULProcess with stores only DULDescription; no stored-description existence, persistence or learning-update algorithm. | REVIEWER_INTERPRETATION; E15 |
| A015 / Perception | DULProcess with uses only Memory, input only Sensation and output only DULDescription; universal restrictions do not generate events or outputs. | REVIEWER_INTERPRETATION; E15 |
| A016 / PersonalContext | Context subtype only; paper interface inheritance is not a sufficient user-state model. | REVIEWER_INTERPRETATION; E15 |
| A017 / Psychophysiological | EmotionExpressionSystem and DULAction; not itself a measured physiological response or classifier. | REVIEWER_INTERPRETATION; E15 |
| A018 / Sensation | DULProcess subtype only; it is distinct from sensor, stimulus and interpreted emotional state. | REVIEWER_INTERPRETATION; E15 |
| A019 / Sense | BiologicalSensor subtype only; specific sensory subclasses add restricted filler types. | REVIEWER_INTERPRETATION; E15 |
| A020 / Sensor | Interface and DULPhysicalObject, input only Stimulus and output only Sensation; no sensor event/reading existence follows. | REVIEWER_INTERPRETATION; E15 |
| A021 / Sight | Sense with hasInput only ContinuousStimulus; no inference from a missing input triple to absence of sight. | REVIEWER_INTERPRETATION; E15 |
| A022 / Smell | Sense with hasInput only DiscreteStimulus; not a threshold-trigger causal rule. | REVIEWER_INTERPRETATION; E15 |
| A023 / SocialContext | Context subclass only; separate referenced DULSituation statements make every situation also SocialContext under these selected assertions. | REVIEWER_INTERPRETATION; E15 |
| A024 / Speech | Behavioural subtype only; no acoustic recognition model or language/individual calibration specified. | REVIEWER_INTERPRETATION; E15 |
| A025 / Stimulus | DULEvent subtype; Figure1 plural Stimuli is a diagram label, not a separately declared machine class. | REVIEWER_INTERPRETATION; E15 |
| A026 / Taste | Sense with hasInput only DiscreteStimulus; no reading or emotion witness generated. | REVIEWER_INTERPRETATION; E15 |
| A027 / Touch | Sense with hasInput only ContinuousStimulus; no obligatory physical interaction or measurement from this universal alone. | REVIEWER_INTERPRETATION; E15 |
| A028 / Verbal | EmotionExpressionSystem and DULDescription; do not collapse a verbal expression, the agent and a description referent into one level. | REVIEWER_INTERPRETATION; E15 |

## Evidence index

| ID | Exact source locator | Source-grounded summary |
|---|---|---|
| E01 | PDF1 / printed610, title, authors, journal block, DOI, online date and license | Four authors: Rosa Gil, Jordi Virgili-Goma, Roberto Garcia, Cindy Mason; CHB51:610-617,2015, online6March2015; article CC BY4.0, not a license grant for every linked OWL file. |
| E02 | PDF1-2 / printed610-611, section1 and note1 | Flexible/contextual emotion representation, emotional affordance and cultural/individual variation;14 broad affective labels, focus on full-blown emergent emotion and detection/expression interfaces rather than human internal processing. |
| E03 | PDF2-3 / printed611-612, section2 opening and2.1 | Categorical/dimensional/appraisal theories, subjective/behavioral/physiological channels, socialized expression masking, context and modality; related lexical and multimodal ontologies are background rather than imported classes. |
| E04 | PDF3 / printed612, section3 opening and note2 | Named Garcia2006 classical methodology; conceptual-model ovals become OWL classes, edges properties and range-like restrictions; prose triggers example has no explicit DL quantifier. |
| E05 | PDF3-4 / printed612-613, section3 foundation/model details and note3 | DOLCE Description/Situation, generic Event/Process/Action, physical/social categories and contextual types; FrameNet Frame specializes Description. Arriving ThemeJohn/Goalroom illustrates frame roles, not adopted planning goals. |
| E06 | PDF4 / printed613, Figure1 | Nine ovals plus Interface boundary; core sensing/perception/memory/description/emotion/expression loop, seven property labels. Stimuli plural is a drawing label; temporal/fusion/learning constraints are not printed. |
| E07 | PDF5 / printed614, Figure2 | All39 taxonomy labels and literal arrowheads inspected:27unprefixed,11DUL,1ofntb. DULSituation points to SocialContext/EnvironmentalContext; Interface points to PersonalContext. No silent hierarchy repair. |
| E08 | PDF4-5 / printed613-614, section4 opening, Figures3-4 and notes4-5 | EmoCS guided FrameNet autocomplete, structured manual emotional sliders, multimedia situation descriptions and RDF storage; Torres example binds Recipient/Result/Theme/Time. Browser/site statements are historical. |
| E09 | PDF5-6 / printed614-615, section4 continuation and Figure5 | Ontology models associations and explicitly does not recognize emotion. Happy media in response to sadness is illustrative; bootstrapping is acknowledged. Figure5 uses EmotionalState and literal hasOuput spelling, not an accepted formal alias. |
| E10 | PDF6 / printed615, section4.1 and notes6-10 | Historical EEG/BCI device and suites; annotations manually produced from SDK screen. Four metric families do not match an established categorization; fear/surprise ambiguity. Six-Ekman recognition is work in progress. |
| E11 | PDF7 / printed616, Figures6-7 | Headset photographs and SDK2.0.0.20 screenshot. Five traces include instantaneous/long-term excitement, not five independent categorical emotions or a participant/sample-size report. |
| E12 | PDF6-8 / printed615-617, section5 and acknowledgements | Scope/standards/application claims; extending affective states, automatic EEG annotations, training data/model processing, skin-conductance complement and broader social/user models remain future or ongoing, without reported accuracy or causal efficacy. |
| E13 | PDF8 / printed617, references38 entries | All38 bibliography entries inspected; methodological thesis and background references do not constitute a completed method, formal import edition or independently replicated emotion benchmark. |
| E14 | Complete page/visual census, all seven figures and ten notes | All8 pages and renders inspected, with individual Figures2/5/6/7 zooms. Seven figures, ten footnotes,38references; no numbered table, appendix or numbered formula. No2014 PrEmo participant/results table is present. |
| E15 | Author-linked2015/05 candidate, complete candidate-census.json and selected-external-constraints.yaml | Selected root has28 local classes,6 object properties,3 datatype properties,152 asserted triples, three declared unresolved imports; one class comment and27missing. Every local constraint inspected. DULDescription/Situation outgoing restrictions are separate from named declarations. |
| E16 | Author guide links2010/2013/May2015 predecessors and December2015/current cognition extension; checked2026-10-28 | Author guide distinguishes predecessor and later cognition extension. Later two URLs have identical bytes0e19f81a...; selected May candidate is not automatically the exact2015 article release. |
| E17 | Publisher and author-publication metadata, checked2026-10-28 | Four authors, journal51PartB610-617, issueOctober2015 and DOI confirmed. Owner eight-page journal PDF stays reading authority; public institutional PDF has different bytes. |

## Closure boundary

Paper77 completes only after merged relevant checks. All8pages and source units reviewed; SDKmanual/future recognition and unreported quantitative results remain explicit. SelectedMay28class comments-or-gaps/constraints are accounted for, not a complete legacy import glossary or verified publication artifact.239technical,253comparison and126synthesis stay OPEN. Next84is the separately authorized limited-summary review without a PDF gate. No ontology,requirements,fixtures,manuscript,release or adoption change.
