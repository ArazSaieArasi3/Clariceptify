# An Ontological approach to the construction of problem-solving models

Work: `OntoKADS2005` | Issue: #74 | State: `REVIEW_COMPLETE`

Reviewed version: LaRIA research report LRR 2005-03, May 2005; arXiv cs/0505081. Input: `OntoKADS.pdf`, 10 PDF pages, SHA256 `040ad09c7efc2b988fdb0720c9ed580bce1778fa6494cdb484d827359d95026b`.

The structured `review.yaml` is the evidence authority; this report is derived. This is an AI-assisted critical review, not independent expert acceptance. Clariceptify is unchanged; later use requires an owner decision.

## Identity and reading coverage

Sabine Bruaux, Gilles Kassel and Gilles Morel. The ten-page input includes a cover and nine body/reference pages, cited here by PDF page. It extends the 2004 workshop work cited as reference 3; it is not silently identified with that earlier work. No DOI or released executable ontology version is established by these bytes.

The complete ten-page report, all five figures, sixteen footnotes, labeled formulas A1-A13/D1-D6/T1-T3 and bibliography were inspected. The catalog inventories the ontology-bearing categories, primitives and example families in this paper; aliases are grouped explicitly. It is not a class count of an unavailable formal distribution. Figure hierarchy edges and formula/prose differences are preserved below.

| Paper unit | Coverage | Evidence |
|---|---|---|
| Cover, title/authors and abstract | REVIEWED | E01 |
| Introduction | REVIEWED | E01 |
| Overview of OntoKADS | REVIEWED | E02 |
| How OntoKADS extends DOLCE: DOLCE and knowledge | REVIEWED | E03 |
| Two main sub-ontologies | REVIEWED | E04, E05 |
| Kernel: theoretical/practical knowledge | REVIEWED | E06 |
| Kernel: I&DA mental objects | REVIEWED | E07 |
| Kernel: participating entities | REVIEWED | E08 |
| Kernel: participation modes | REVIEWED | E09 |
| Kernel: KnowledgeRole | REVIEWED | E10 |
| Discussion | REVIEWED | E11 |
| Related ontological work | REVIEWED | E12 |
| Conclusion | REVIEWED | E13 |
| References 1-23 | REVIEWED | E14 |
| Figure 1: modeling workflow | REVIEWED | E02 |
| Figure 2: DOLCE hierarchy | REVIEWED | E03 |
| Figure 3: object/meta-level classification | REVIEWED | E05 |
| Figure 4: I&DA hierarchy | REVIEWED | E07 |
| Figure 5: role labeling | REVIEWED | E10 |
| Footnotes 1-16; no tables or appendices in the input | REVIEWED | E01, E02, E03, E04, E05, E06, E07, E09, E10 |

## Common review dimensions

### D1_identity_coverage

The acquired item is the May2005 LaRIA report, including its cover. PDF numbering avoids inventing publisher pagination. The complete text, figures and formulas are covered; the earlier workshop reference is kept distinct. [AUTHOR_REPORTED; E01, E14]

### D2_problem_contribution

The problem is semantic treatment of the interface between domain knowledge and reasoning in CommonKADS. The contribution combines a DOLCE problem-solving ontology with meta-properties for modeling primitives, giving knowledge roles an explicit content/participation interpretation. The claimed improvement is conceptual and methodological; comparative effectiveness is not established. [AUTHOR_REPORTED; E01, E02, E10, E11]

### D3_method

The authors analyze CommonKADS examples, specialize DOLCE, borrow I&DA mental-object distinctions and role meta-properties, then derive modeling questions and an ontology-to-expertise-model workflow. This is a constructive conceptual analysis using car diagnosis and code calibration. Participant recruitment, a reproducible annotation protocol and quantitative comparison are not reported in this selected text. [REVIEWER_INTERPRETATION; E02, E04, E07, E10, E11, E13]

### D4_requirements

Intended user: knowledge engineer constructing expertise models. The paper explicitly asks what participates in reasoning/communication, how participation works and how meta-properties characterize it. It requires application-independent methods and richer semantic commitments before primitive assignment. These are author questions/requirements, not an executed CQ suite. Collaboration/coordination is explicitly outside the current treatment. [AUTHOR_REPORTED; E01, E04, E06, E11]

### D5_concepts

The central separation is between perdurant reasoning/communication, endurant contents, content subjects and real-world referents. Expression is code-dependent; Content is code-independent. Document is a physical carrier; propositions and concepts are mental objects. A second classification level assigns modeling primitives to concepts at building times. Formal/material knowledge roles distinguish whether identity comes from the role or an underlying type. [AUTHOR_REPORTED; E03, E05, E07, E08, E10]

### D6_relations_formalization

All 22 labeled items are catalogued individually, with participation/classification/subsumption relations. A1-A3/D1 characterize action types, A4-A8 meta-level labels and restrictions, A9/D2 subject structure and A10-A13/D3-D6/T1-T3 input roles. D4 has an unbound variable; A13 alone permits a vacuous early cutoff. The source is not silently repaired and no prover result is claimed. [REVIEWER_INTERPRETATION; E04, E05, E07, E09]

### D7_grounding

DOLCE supplies particulars, endurants/perdurants and time-indexed participation. Role anti-rigidity and external dependence are inherited conceptual criteria; formal/material roles concern identity. Classifying a concept by a meta-property is different from a domain object instantiating that concept. Model-building times and action-participation times have different intended uses. The paper permits human/system reasoners and intentionally distinguishes reasoning from communication. [AUTHOR_REPORTED; E03, E04, E05, E09, E10]

### D8_artifact_correspondence

The text describes OntoSpec semi-informal specifications and an environment extending TERMINAE as being developed. No version-pinned executable OntoKADS module is present in the retained corpus. Its exact availability and machine-checkable correspondence are open in #236; no source absence, license, class count, consistency or generation success is inferred. [REVIEWER_INTERPRETATION; E02, E13]

### D9_evaluation

Car diagnosis and calibration illustrate the proposed semantics, and calibration is described as an ongoing evaluation application. Discussion says comparisons with CommonKADS are current work. There is no reported test population, effect estimate or completed independent expert study here. The reviewer inspects source coherence but does not reproduce an author experiment or execute ontology reasoning. [REVIEWER_INTERPRETATION; E04, E11, E13]

### D10_critical_synthesis

Strong prior coverage exists for mental reasoning activity, content/expression separation, temporally classified modeling primitives and context-dependent knowledge roles. This narrows any later novelty claim. Limits include conceptual/prototype status, deliberately narrow coordination scope, untested identity/role commitments and formula defects. Comparisons must keep foundational and classification-level differences explicit. All later uses remain proposals for the owner. [REVIEWER_INTERPRETATION; E05, E07, E09, E10, E11, E12, E13]

## Conceptual catalog

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| C01 / Particular / PT | REUSED_FOUNDATION: Top-level DOLCE population. | AUTHOR_REPORTED; E03 |
| C02 / Endurant / ED | REUSED_FOUNDATION: Wholly present entity; includes participating contents. | AUTHOR_REPORTED; E03 |
| C03 / Perdurant / PD | REUSED_FOUNDATION: Temporal occurrence; contrasted with an endurant. | AUTHOR_REPORTED; E03 |
| C04 / PhysicalObject / POB | REUSED_FOUNDATION: Object with direct physical location. | AUTHOR_REPORTED; E03 |
| C05 / NonPhysicalObject / NPOB | REUSED_FOUNDATION: Object without direct physical location. | AUTHOR_REPORTED; E03 |
| C06 / MentalObject / MOB | REUSED_FOUNDATION: Private nonphysical object associated with an agentive. | AUTHOR_REPORTED; E03 |
| C07 / AgentivePhysicalObject / APO | REUSED_FOUNDATION: Physical agentive category in Fig.2 and D1. | AUTHOR_REPORTED; E03 |
| C08 / AgentiveSocialObject / ASO | REUSED_FOUNDATION: Social agentive category; agentive is the union APO/ASO in footnote5. | AUTHOR_REPORTED; E03 |
| C09 / Event / EV | REUSED_FOUNDATION: Non-cumulative perdurant branch. | AUTHOR_REPORTED; E03 |
| C10 / Stative / STV | REUSED_FOUNDATION: Cumulative perdurant branch. | AUTHOR_REPORTED; E03 |
| C11 / State | REUSED_FOUNDATION: Stative branch displayed in Fig.2. | AUTHOR_REPORTED; E03 |
| C12 / Process | REUSED_FOUNDATION: Stative branch displayed in Fig.2; concepts of processes may be reasoning subjects. | AUTHOR_REPORTED; E03 |
| C13 / Achievement | REUSED_FOUNDATION: Event branch displayed in Fig.2. | AUTHOR_REPORTED; E03 |
| C14 / Accomplishment / ACC | REUSED_FOUNDATION: Non-atomic event branch. | AUTHOR_REPORTED; E03 |
| C15 / Action / AC | REUSED_FOUNDATION: Intentional accomplishment. | AUTHOR_REPORTED; E03 |
| C16 / Quality | REUSED_FOUNDATION: Top-level DOLCE branch shown but not developed. | AUTHOR_REPORTED; E03 |
| C17 / Abstract | REUSED_FOUNDATION: Top-level DOLCE branch shown but not developed. | AUTHOR_REPORTED; E03 |
| C18 / Agentive | REUSED_FOUNDATION: Bearer of knowledge/ability, potentially intentional and rational; not identical to the Agent participation role. | AUTHOR_REPORTED; E03 |
| C19 / Reasoning | DOMAIN: Action intended to transform the reasoner mental world; examples diagnosis, calibration and hypothesizing. | AUTHOR_REPORTED; E04 |
| C20 / Reasoner | DOMAIN: Agent participating in a reasoning; human or knowledge-based system, not supplied as an independently axiomatized class here. | AUTHOR_REPORTED; E04 |
| C21 / Interaction | DOMAIN: Action with a distinct additional agentive participant as in D1. | AUTHOR_REPORTED; E04 |
| C22 / Communication | DOMAIN: Interaction directed toward information exchange and disjoint from Reasoning in A3. | AUTHOR_REPORTED; E04 |
| C23 / Diagnosis | DOMAIN: Reasoning example and object of Task classification in A4. | AUTHOR_REPORTED; E04 |
| C24 / Calibrating | DOMAIN: Reasoning used to define CalibrationData. | AUTHOR_REPORTED; E04 |
| C25 / Goal / objective | DOMAIN: Desired-state mental representation; a role-like participant, not proof the desired real state exists. | AUTHOR_REPORTED; E04 |
| C26 / Task | MODELING_META_PROPERTY: Classifies Reasoning-subsumed concepts at model-building times. | AUTHOR_REPORTED; E05 |
| C27 / Inference | MODELING_META_PROPERTY: Alternative model-level classification of reasoning concepts; may change to Task when a decomposition method is supplied. | AUTHOR_REPORTED; E05 |
| C28 / DomainConcept | MODELING_META_PROPERTY: Modeling primitive exemplified by EmptyFuelTank. | AUTHOR_REPORTED; E05 |
| C29 / TransferFunction | MODELING_META_PROPERTY: Classifies concepts subsumed by Communication. | AUTHOR_REPORTED; E05 |
| C30 / Input / Output | MODELING_META_PROPERTY: Modeling primitives later specified as classifying Data/Result respectively; not the contents themselves. | AUTHOR_REPORTED; E05 |
| C31 / Document | BORROWED_IDA: Material medium bearing a semiotic inscription; can include a sound-carrying medium. | AUTHOR_REPORTED; E07 |
| C32 / Expression | BORROWED_IDA: Perceived signifier in a communication code; mental object branch in Fig.4. | AUTHOR_REPORTED; E07 |
| C33 / Content | BORROWED_IDA: Code-independent signified, subdivided into Concept and Proposition. | AUTHOR_REPORTED; E07 |
| C34 / Concept | BORROWED_IDA: Means of reference/classification, including concepts of states/processes, not the real-world instance. | AUTHOR_REPORTED; E07 |
| C35 / Proposition | BORROWED_IDA: Truth-bearing content with Concepts as subjects; can model a knowledge or mathematical model. | AUTHOR_REPORTED; E07 |
| C36 / Subject | BORROWED_IDA: Concept used by some Proposition; defined in D2. | AUTHOR_REPORTED; E07 |
| C37 / LinguisticObject | BORROWED_IDA: Expression branch in Fig.4. | AUTHOR_REPORTED; E07 |
| C38 / IconicObject | BORROWED_IDA: Expression branch in Fig.4. | AUTHOR_REPORTED; E07 |
| C39 / Term | BORROWED_IDA: Linguistic expression category in Fig.4. | AUTHOR_REPORTED; E07 |
| C40 / Text | BORROWED_IDA: Structured linguistic expression category in Fig.4. | AUTHOR_REPORTED; E07 |
| C41 / Discourse | BORROWED_IDA: Statement/communicative signifier paired with Message. | AUTHOR_REPORTED; E07 |
| C42 / Message | BORROWED_IDA: Proposition resulting from a discursive act. | AUTHOR_REPORTED; E07 |
| C43 / Assertion | BORROWED_IDA: Proposition treated as true for an agent. | AUTHOR_REPORTED; E07 |
| C44 / Hypothesis | BORROWED_IDA: Proposition arising from hypothetical reasoning. | AUTHOR_REPORTED; E07 |
| C45 / Information | BORROWED_IDA: Message example resulting from informing. | AUTHOR_REPORTED; E07 |
| C46 / Complaint | BORROWED_IDA: Message example resulting from complaining. | AUTHOR_REPORTED; E07 |
| C47 / Patient | PARTICIPATION_ROLE: Endurant affected in a perdurant through isAffectedBy. | AUTHOR_REPORTED; E09 |
| C48 / Data | PARTICIPATION_ROLE: Content participating as action input; formally a Patient by A11/T2. | AUTHOR_REPORTED; E09 |
| C49 / Result | PARTICIPATION_ROLE: Content participation at the action end is described; no symmetric fully labeled result definition is supplied. | AUTHOR_REPORTED; E09 |
| C50 / CalibrationData | PARTICIPATION_ROLE: Data of some Calibrating occurrence. | AUTHOR_REPORTED; E09 |
| C51 / ModelToCalibrate | PARTICIPATION_ROLE: Conjunction of Model and CalibrationData. | AUTHOR_REPORTED; E09 |
| C52 / Model / CarModel | PARTICIPATION_ROLE: Proposition with its own identity criterion; CarModel is an illustrative type. | AUTHOR_REPORTED; E09 |
| C53 / SolvingMethod | PARTICIPATION_ROLE: Essential mental participant in reasoning; fuller modeling remains expansion work. | AUTHOR_REPORTED; E09 |
| C54 / Role | ROLE_META_PROPERTY: Anti-rigid concept externally dependent on another entity. | AUTHOR_REPORTED; E10 |
| C55 / FormalRole | ROLE_META_PROPERTY: Role carrying no identity criterion; Agent/Patient illustrate it. | AUTHOR_REPORTED; E10 |
| C56 / MaterialRole | ROLE_META_PROPERTY: Role carrying identity inherited through a type; Student/Employee illustrate it. | AUTHOR_REPORTED; E10 |
| C57 / KnowledgeRole | ROLE_META_PROPERTY: Role played by Content and dependent on an action, reasoning or communication. | AUTHOR_REPORTED; E10 |
| C58 / FormalKnowledgeRole | ROLE_META_PROPERTY: KnowledgeRole without an identity criterion; Data/Result and specializations illustrate it. | AUTHOR_REPORTED; E10 |
| C59 / MaterialKnowledgeRole | ROLE_META_PROPERTY: KnowledgeRole carrying identity; ModelToCalibrate/DiagnosisHypothesis illustrate it. | AUTHOR_REPORTED; E10 |
| C60 / Agent | ROLE_META_PROPERTY: Formal participation role distinguished from the agentive bearer category. | AUTHOR_REPORTED; E10 |
| C61 / Determinant / Substrate | ROLE_META_PROPERTY: Participation-role branches displayed in Fig.5; not independently defined in the prose. | AUTHOR_REPORTED; E10 |
| C62 / DiagnosisResult | ROLE_META_PROPERTY: Formal knowledge-role example displayed in Fig.5. | AUTHOR_REPORTED; E10 |
| C63 / DiagnosisHypothesis | ROLE_META_PROPERTY: Material knowledge role combining Hypothesis and DiagnosisResult in Fig.5. | AUTHOR_REPORTED; E10 |
| C64 / Type | ROLE_META_PROPERTY: Identity-supplying category in the role analysis; Model/Hypothesis are Fig.5 examples. | AUTHOR_REPORTED; E10 |
| C65 / EmptyFuelTank | EXAMPLE_FAMILY: May denote a state concept or an agent assertion with that concept as subject; not interchangeable with the actual tank. | AUTHOR_REPORTED; E08 |
| C66 / EmptyFuelTankHypothesis | EXAMPLE_FAMILY: Proposition resulting from hypothetical reasoning. | AUTHOR_REPORTED; E08 |
| C67 / LowBatteryLevelComplaint | EXAMPLE_FAMILY: Message resulting from a complaining act. | AUTHOR_REPORTED; E08 |
| C68 / Perception/pathology qualifiers | EXAMPLE_FAMILY: Visible/invisible/observed/observable/pathological qualify domain concepts; not declared as a complete formal hierarchy here. | AUTHOR_REPORTED; E08 |
| C69 / Sign | COMPARISON_CATEGORY: FormalKnowledgeRole played by a concept; contrasted with DnS region-parameter concepts. | AUTHOR_REPORTED; E12 |
| C70 / Percept / ComputedObject | COMPARISON_CATEGORY: COM comparison categories, not asserted OntoKADS classes. | AUTHOR_REPORTED; E12 |
| C71 / s-description / c-description / InformationObject | COMPARISON_CATEGORY: DnS comparison categories with proposed Proposition/Concept/Expression correspondences and explicit qualifications. | AUTHOR_REPORTED; E12 |
| C72 / Intention | COMPARISON_CATEGORY: COM comparison object and possible part of reasoning; merger is proposed, not established. | AUTHOR_REPORTED; E12 |

## Relations and formal commitments

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| K01 / A1 | Reasoning(x) implies AC(x). | AUTHOR_REPORTED; E04 |
| K02 / D1 | Interaction(x) iff AC(x) and there exist y,z,t: isAgentOf(y,x), z differs from y, (APO(z) or ASO(z)) and PC(z,x,t). This requires another agentive participant; explanatory influence is not separately axiomatized. | AUTHOR_REPORTED; E04 |
| K03 / A2 | Communication(x) implies Interaction(x). | AUTHOR_REPORTED; E04 |
| K04 / A3 | Reasoning(x) implies not Communication(x); explicit disjointness direction. | AUTHOR_REPORTED; E04 |
| K05 / A4 | Example classification: classify(Task,Diagnosis,t1). | AUTHOR_REPORTED; E05 |
| K06 / A5 | Example classification: classify(FormalKnowledgeRole,CalibrationData,t2). | AUTHOR_REPORTED; E05 |
| K07 / A6 | Example classification: classify(DomainConcept,EmptyFuelTank,t3). | AUTHOR_REPORTED; E05 |
| K08 / A7 | classify(Task,x,t) implies subsumes(Reasoning,x). | AUTHOR_REPORTED; E05 |
| K09 / A8 | classify(TransferFunction,x,t) implies subsumes(Communication,x). | AUTHOR_REPORTED; E05 |
| K10 / A9 | hasForSubject(x,y) implies Proposition(x) and Concept(y). | AUTHOR_REPORTED; E07 |
| K11 / D2 | Subject(x) iff Concept(x) and there exists y: Proposition(y) and hasForSubject(y,x). | AUTHOR_REPORTED; E07 |
| K12 / A10 | isAffectedBy(x,y) implies there exists t: PC(x,y,t). | AUTHOR_REPORTED; E09 |
| K13 / D3 | Patient(x) iff there exists y: isAffectedBy(x,y). | AUTHOR_REPORTED; E09 |
| K14 / T1 | Patient(x) implies ED(x); labeled theorem, not independently proved here. | AUTHOR_REPORTED; E09 |
| K15 / A11 | isDataOf(x,y) implies isAffectedBy(x,y). | AUTHOR_REPORTED; E09 |
| K16 / A12 | isDataOf(x,y) implies Content(x) and Action(y). Source writes Action rather than the earlier AC abbreviation. | AUTHOR_REPORTED; E09 |
| K17 / A13 | isDataOf(x,y) implies there exists t, for all t-prime: (PRE(y,t-prime) and t-prime <= t) implies PC(x,y,t-prime). Preserve the existential cutoff; no PRE(y,t) or nonempty-prefix premise is printed. | AUTHOR_REPORTED; E09 |
| K18 / D4 | As printed: Data(x) =def isDataOf(x,y). The y is unbound. An existential repair is a candidate reading, not the literal source formula. | AUTHOR_REPORTED; E09 |
| K19 / T2 | Data(x) implies Patient(x); source-labeled theorem, affected by how D4 is read. | AUTHOR_REPORTED; E09 |
| K20 / T3 | Data(x) implies Content(x); source-labeled theorem, not a rerun proof. | AUTHOR_REPORTED; E09 |
| K21 / D5 | CalibrationData(x) iff there exists y: isDataOf(x,y) and Calibrating(y). | AUTHOR_REPORTED; E09 |
| K22 / D6 | ModelToCalibrate(x) iff Model(x) and CalibrationData(x). | AUTHOR_REPORTED; E09 |
| K23 / PC / temporal participation | PC(x,y,t): an endurant participates in a perdurant at time t. Footnote15 cites DOLCE Ad33 and Ad35, including time typing and existence of participation for endurants. | AUTHOR_REPORTED; E03, E09 |
| K24 / CF / classify | The time-indexed classification relation is extended to concepts classified by meta-properties. Meta-level labels are not object-level subclass axioms. | AUTHOR_REPORTED; E05 |
| K25 / subsumes / subsume | Footnote11 defines necessary instance inclusion; spelling differs between prose footnote and displayed predicates. | AUTHOR_REPORTED; E05 |
| K26 / isAgentOf | Agent participation predicate used in D1; complete role axiom system is not printed. | AUTHOR_REPORTED; E04 |
| K27 / PRE and temporal order | Presence of a perdurant at a time and <= used in A13; no full temporal theory is supplied in this report. | AUTHOR_REPORTED; E09 |
| K28 / hasForSubject | Proposition-to-Concept relation with explicit signature in A9; Subject is the inverse-existential class in D2. | AUTHOR_REPORTED; E07 |
| K29 / Content/Expression/Document links | Many expressions can convey the same content and many material inscriptions can realize an expression. Semantic links are explained but not given named formula axioms in this report. | AUTHOR_REPORTED; E07 |
| K30 / Role and identity constraints | KnowledgeRole specializes role/dependence to Content/action; FormalKnowledgeRole lacks identity and MaterialKnowledgeRole carries identity via a type. Fig.5 organizes examples; no executable modal characterization is supplied. | AUTHOR_REPORTED; E10 |
| K31 / Reasoning/Communication goals | Prose distinguishes transforming a mental world from information exchange; A1-A3 alone do not encode goal content or all mental-participant restrictions. | AUTHOR_REPORTED; E04, E06 |

## Requirements, examples and adverse cases

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| S01 / Author questions | What entities participate in reasoning/communication; how they participate; and which meta-properties characterize these roles. These are the three explicit kernel questions. | AUTHOR_REPORTED; E06 |
| S02 / Positive car diagnosis | Treat the empty-fuel-tank hypothesis as a Proposition whose Subject is the state Concept; let it play a diagnosis-result role. The actual fuel tank is not the direct mental-content participant. | REVIEWER_INTERPRETATION; E04, E07, E08, E10 |
| S03 / Positive calibration | A mathematical Model plays CalibrationData for a Calibrating occurrence, yielding ModelToCalibrate through D6. Model-building primitive labeling is a different relation from participation in that occurrence. | REVIEWER_INTERPRETATION; E05, E09, E10 |
| S04 / Adverse temporal input | Choose a cutoff earlier than every time at which y is present. Then the antecedent inside A13 is false throughout, so the displayed implication alone need not require x to participate at the action start. This is a logical reading, not a solver execution; added premises could block it. | REVIEWER_INTERPRETATION; E09 |
| S05 / Scope adverse case | A collaborative joint design meeting needs coordination of multiple reasoners and decisions. The current paper explicitly omits collaborative problem solving and coordination; no global claim about later OntoKADS is made. | REVIEWER_INTERPRETATION; E04, E11 |

## Critical findings

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| F01 / Prior overlap | Reasoning as purposeful mental transformation with content participants is explicit prior art. It prevents an unsupported universal claim that prior ontologies only model static concepts. | REVIEWER_INTERPRETATION; E04, E06, E08 |
| F02 / Classification-level discipline | A concept changing its Task/Inference label is a model-building event; it is not evidence that a domain entity changed its essential type. Treat both temporal axes explicitly in later comparisons. | REVIEWER_INTERPRETATION; E05 |
| F03 / D4 variable scope | The printed definition has an unbound y. Executable reuse requires an explicit, reviewed quantification decision; silently inserting exists-y would conceal a source discrepancy. | REVIEWER_INTERPRETATION; E09 |
| F04 / A13 weaker than prose | The displayed existential cutoff does not by itself force a nonempty prefix of participation. The positive prose intent and the weaker printed formula must be retained separately. | REVIEWER_INTERPRETATION; E09 |
| F05 / Method claim remains untested | The proposed ontology-first modeling workflow is clear, but paper evidence does not establish that it improves correctness, reuse, effort or agreement over CommonKADS. | REVIEWER_INTERPRETATION; E02, E11, E13 |
| F06 / Proposed mappings are not equivalences | The COM merger and DnS/I&DA correspondences are tentative and qualified by differences over regions, signs, mental objects and content. They cannot be imported as exact semantic equivalences. | REVIEWER_INTERPRETATION; E12 |

## Unresolved questions

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Q01 / Executable artifact | Can an author-controlled formal version corresponding to this report be recovered, and how are D4, temporal inputs/results and meta-properties represented? Track in #236. | UNKNOWN; E09, E13 |
| Q02 / Identity and context | Which identity conditions distinguish content across agents and communication codes, and how do later versions treat shared content versus private mental objects? The report states the distinction without a complete identity decision procedure. | UNKNOWN; E03, E07, E10 |
| Q03 / Method evaluation | Are the announced model comparisons, role-identification reliability or task-method expansions completed in later primary publications? Citation expansion must be separately versioned. | UNKNOWN; E11, E12, E13 |

## Inputs for later synthesis

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| U01 / Terminology and scope | Candidate synthesis distinction: reasoning occurrence, conceptual content, expression/physical carrier and real-world subject need separate comparison cells. No Clariceptify change is made. | REVIEWER_INTERPRETATION; E03, E07, E08 |
| U02 / Future test candidate | Retain the D4/A13 discrepancies and the non-collaborative boundary as candidate checks for future method/constraint design, subject to owner direction. | REVIEWER_INTERPRETATION; E04, E09 |
| U03 / Batch integration | Feed evidence into #252 with LMM/O4OA. Until O4OA is reviewed, any synthesis of this batch is partial and cannot close its final comparison. | REVIEWER_INTERPRETATION; E05, E07, E12 |

## Evaluation evidence

- **Verification:** Displayed definitions and diagrams permit source-level checking; D4 and A13 expose formalization questions. No executed consistency/proof suite or generated-model correctness test is reported or rerun. [REVIEWER_INTERPRETATION; E05, E09, E13]
- **Validation:** Diagnosis and calibration motivate intended modeling distinctions. The report does not present independent expert acceptance, study sampling or user success evidence. [NOT_REPORTED; E04, E11]
- **Evaluation:** Comparison with CommonKADS expertise models is described as ongoing; no completed comparative sample, metrics or quantified effect appears here. [NOT_REPORTED; E11, E13]
- **Assessment:** Reviewer judges the role/content distinctions relevant prior overlap, with explicit assumptions and limitations. This contextual judgment is not author approval or a release decision. [REVIEWER_INTERPRETATION; E07, E10, E12]
- **Assurance:** Versioned source and exact locators support a bounded review account. The report supplies no independent assurance case, certification or end-to-end reproducibility package. [NOT_REPORTED; E01, E13]

## Artifact and repository boundary

Technical follow-up: #236. State: `FORMAL_DISTRIBUTION_NOT_IDENTIFIED_IN_RETAINED_CORPUS`.

The report names OntoSpec and a developing TERMINAE extension, but gives no immutable executable-module ref that can be matched to these 2005 formulas. #236 retains discovery, license and technical inspection. No repository absence or satisfiability is inferred.

## Evidence index

| ID | Exact source locator | Source-grounded summary |
|---|---|---|
| E01 | PDF pp. 1-2, cover, abstract and Introduction | Report identity; ontology-centered CommonKADS expertise modeling and the disputed semantic status of knowledge roles. |
| E02 | PDF p. 3, Overview of OntoKADS; Fig. 1; footnotes 2-3 | Two sub-ontologies; application-ontology labeling and extraction into domain/inference/task models; task-method specification and software under development. |
| E03 | PDF pp. 3-4, How OntoKADS extends DOLCE / DOLCE and the notion of knowledge; Fig. 2; footnotes 4-6 | DOLCE particulars, endurant/perdurant distinction, temporal participation, mental objects, agentives and intentional action. |
| E04 | PDF p. 4, The two main sub-ontologies, A1-A3 and D1; footnotes 7-9 | Car diagnosis/calibration illustrations; reasoning and communication differentiated by goals; interaction participation; collaboration/coordination excluded. |
| E05 | PDF p. 5, second sub-ontology, A4-A8; Fig. 3; footnotes 10-11 | Meta-properties classify concepts at model-building times; Task/Inference reclassification; Task and TransferFunction sort restrictions. |
| E06 | PDF pp. 5-6, The OntoKADS kernel / Theoretical and practical knowledge and its objects; footnote 12 | Core analysis questions; theoretical/practical knowledge; reasoning participants as mental contents; physical execution contingencies are distinguished from essential content participation. |
| E07 | PDF p. 6, Population of mental objects in I&DA, A9 and D2; Fig. 4; footnotes 13-14 | Document, Expression, Content, Concept and Proposition; subject relation; linguistic/iconic expression, discourse/message, assertion/hypothesis and information/complaint distinctions. |
| E08 | PDF pp. 6-7, Nature of the participating entities | Contents directly participate in reasoning; real-world entities are indirectly involved via concepts. Empty-fuel-tank, hypothesis, complaint and car-model examples. |
| E09 | PDF p. 7, Participation modes, A10-A13, D3-D6, T1-T3; footnote 15 | Patient/Data specialization of participation; input temporal intent; model-to-calibrate conjunction. D4 visibly leaves y unbound; A13 is an existential-cutoff implication. |
| E10 | PDF pp. 7-8, The modeling primitive: KnowledgeRole; Fig. 5; footnote 16 | Anti-rigidity/external dependence and formal/material roles; identity criteria; content-dependent knowledge-role meta-properties; input/output classification. |
| E11 | PDF p. 8, Discussion | Modeling questions separate representation type/subject, data versus result and reasoning type; ongoing comparison with CommonKADS is described, not a completed measured result. |
| E12 | PDF pp. 8-9, Related ontological work | SUMO/provenance, DnS/I&DA and COM compared; proposed correspondences and differences; DnS region-parameter example versus OntoKADS sign roles; intentions/methods/goals remain expansion work. |
| E13 | PDF p. 9, Conclusion | Ontology expansion and TERMINAE/OntoSpec environment are work in progress; no packaged implementation or completed evaluation reported here. |
| E14 | PDF pp. 9-10, References 1-23 | Bibliography identifies original I&DA 2004 and COM FOIS2004 and the earlier OntoKADS2004 workshop work; citations are discovery links, not substituted full-text evidence. |

## Closure boundary

This completes a source-bound critical paper dossier, not independent scientific acceptance, a reasoner run, author-experiment reproduction, formal-artifact completion or a Clariceptify model change. Named findings and technical tasks remain unresolved where stated. Disposition: DEFER_TO_OWNER_AFTER_SYNTHESIS; supported overlap is recorded, but no reuse/alignment/extension/rejection is applied to Clariceptify.
