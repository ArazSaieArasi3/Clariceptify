# The Ontology for Conceptual Characterization of Ontologies

Work: `CLR-RW-O4OA` | Issue: #73 | State: `REVIEW_COMPLETE`

Reviewed version: ER2023, LNCS14320, printed 105-124; first online 2023-10-29. Input: `O4OA-2023-owner.pdf`, 20 PDF pages, SHA256 `de09a79471af857d251231429988f2025d3f02b6983073c13e249e19aebcf0df`.

The structured `review.yaml` is the evidence authority; this report is derived. This is an AI-assisted critical review, not independent expert acceptance. Clariceptify is unchanged; later use requires an owner decision.

## Identity and reading coverage

Exact 20-page owner-supplied conference paper only. Current author CQ/documentation resources, O4OA project and light gO4OA variant are separate dated inputs; no historical2023 byte/axiom parity is presumed.

Complete selected paper: all 20 pages, all eight figures (seven OntoUML fragments and one tool example), ten numbered footnotes and 66 bibliography entries. Complete paper-level type/role/relator and relational distinctions are cataloged; all machine class counts remain unknown. Mental Concept and Concept-as-Term-role remain separate. No numbered tables, formulas or appendices; no full OCL/Alloy listing. Source abbreviations in Figure 8 are not reconstructed. Current linked CQs are separate, not silently counted as printed paper questions.

| Paper unit | Coverage | Evidence |
|---|---|---|
| Title/abstract/publication block | REVIEWED | E01 |
| Section1 Introduction | REVIEWED | E02 |
| Section2 Ontologies and FAIR | REVIEWED | E03 |
| Section3 opening | REVIEWED | E03 |
| Section3.1 Methodology/stakeholders/questions | REVIEWED | E04 |
| Section3.2 Ontology characterization | REVIEWED | E05, E06 |
| Section3.3 Domain cloud | REVIEWED | E07, E08 |
| Section3.4 Network characterization | REVIEWED | E09, E10, E11, E12, E13, E14 |
| Section3.5 Semi-automatic support | REVIEWED | E15, E16 |
| Section4 Evaluation | REVIEWED | E17 |
| Section5 Related work | REVIEWED | E18 |
| Section6 Conclusions | REVIEWED | E19 |
| Acknowledgments | REVIEWED | E19 |
| References1-66 | REVIEWED | E20 |
| Figure1 | REVIEWED | E06 |
| Figure2 | REVIEWED | E08 |
| Figure3 | REVIEWED | E10 |
| Figure4 | REVIEWED | E11 |
| Figure5 | REVIEWED | E12 |
| Figure6 | REVIEWED | E13 |
| Figure7 | REVIEWED | E14 |
| Figure8 | REVIEWED | E16 |
| Footnote1 | REVIEWED | E20 |
| Footnote2 | REVIEWED | E04 |
| Footnote3 | REVIEWED | E04 |
| Footnote4 | REVIEWED | E04 |
| Footnote5 | REVIEWED | E05 |
| Footnote6 | REVIEWED | E07 |
| Footnote7 | REVIEWED | E15 |
| Footnote8 | REVIEWED | E15 |
| Footnote9 | REVIEWED | E18 |
| Footnote10 | REVIEWED | E18 |

## Common review dimensions

### D1_identity_coverage

Five-author ER2023 paper, DOI 10.1007/978-3-031-47262-6_6, printed 105-124, all 20 owner-supplied PDF pages. Eight figures, ten notes and 66 references inspected; full paper, not a later specification. [AUTHOR_REPORTED; E01, E20]

### D2_problem_contribution

Resolve specialist/engineer conceptual misalignment via a UFO-grounded artifact metaontology, domain concept/definition cloud and ontology-network relations; fairness/effectiveness claims remain author-reported. [AUTHOR_REPORTED; E01, E02, E03, E19]

### D3_method

SABiO; collaborative elicitation, classification literature, OntoUML/OCL and package-level Alloy instantiation, plus microservice prototype. Selection and elicitation reproducibility details are limited. [AUTHOR_REPORTED; E04, E05, E15, E17]

### D4_requirements

Stakeholder perspectives and external CQs drive scope; no full CQ list or five-step framework sequence printed. Current linked CQ data is separately retained; reconstructed positive/adverse cases are explicitly reviewer interpretations. External current-cqs.yaml has 24 author-documentation rows: three groups and 21 subordinate questions; not executed results or proven historical2023 contents. [AUTHOR_REPORTED; E04, E17, E23]

### D5_concepts

All visible types in seven model figures, mental/syntactic distinctions, domain and methodological primitives and named relation groups cataloged. Figure 8 data nodes are examples, not released model classes. [AUTHOR_REPORTED; E05, E06, E07, E08, E10, E11, E12, E13, E14, E15, E16]

### D6_relations_formalization

Generalization sets, relators/material associations, subset annotations, component/member multiplicities and profiles are retained. No numbered formulas, printed OCL/Alloy code or complete axiom set; source inconsistencies remain explicit. [AUTHOR_REPORTED; E06, E08, E10, E11, E12, E13, E14, E17, E19]

### D7_grounding

Paper states UFO through OntoUML without exact release; direct/indirect grounding is conceptual. Stakeholder responsibilities and mental/trope discussion do not form a full action/agent/decision theory. Current UFO-A/B/C/gUFO docs remain separate. [AUTHOR_REPORTED; E01, E04, E07, E12, E13, E21]

### D8_artifact_correspondence

Literal paper/author links, redirects, current CQ resource and GitLab metadata/tree endpoints actually checked and hashed; repository tree HTTP403 leaves source commit, exact model release and full class/import census unknown. Separate light-variant tree pinned at3be36c642b2cfca33de3d0788471bc185880bde8; selected metadata/README inspected, no formal root in five files. Supporting44-page specification acquired for91 only. [EXECUTED; E21, E22, E23, E26]

### D9_evaluation

Author-reported CQs, modular Alloy checks, prototype navigation and cybersecurity cases are separated from reviewer source inspection. No independent solver, user study, FAIR score, benchmark or global consistency test was executed. [AUTHOR_REPORTED; E15, E16, E17, E19]

### D10_critical_synthesis

Reuse/align only as candidate source-backed comparison input. Retain prior conceptualization/definition/network support and critical typing, formalization and evidence limits. Technical91, comparison252 and synthesis126 remain open; no model/manuscript/release adoption. [AUTHOR_REPORTED; E07, E14, E17, E19, E22]

## Conceptual catalog

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| C01 / Ontology (Artifact) | Identity-bearing artifact kind at the root of the displayed classifications; distinguish artifact from its domain and mental content. | REVIEWER_INTERPRETATION; E06, E10, E11, E12, E14 |
| C02 / Operational Ontology | Artifact classified by implementation applicability, rather than automatically a well-defined or grounded one. | REVIEWER_INTERPRETATION; E06, E10 |
| C03 / Reference Ontology | Artifact used to represent a conceptual account of a domain and support operational counterparts. | REVIEWER_INTERPRETATION; E06, E10 |
| C04 / Foundational Ontology | Generality subkind for highly general ontological categories, not a named release. | REVIEWER_INTERPRETATION; E06, E12, E13 |
| C05 / Non-Foundational Ontologies | Complementary displayed generality subkind, partitioned into domain/task/application. | REVIEWER_INTERPRETATION; E06, E13 |
| C06 / Core Ontology | Displayed subkind of Domain Ontology; note 5 instead says Core is more general. Exact discrepancy remains open. | REVIEWER_INTERPRETATION; E06 |
| C07 / Domain Ontology | Specific-domain generality subkind; in the literal figure it is the parent of Core. | REVIEWER_INTERPRETATION; E06 |
| C08 / Application Ontology | Generality subkind covering application-specific domain/task context; not inferred equivalent to an OWL module. | REVIEWER_INTERPRETATION; E06 |
| C09 / Task Ontology | Generality subkind for task/process/activity conceptualizations. | REVIEWER_INTERPRETATION; E06 |
| C10 / Term (syntax) | Syntactic object kind; its Concept role is distinguished from the prose mental/trope sense of Concept. | REVIEWER_INTERPRETATION; E08 |
| C11 / Policy | Document kind in the disjoint Figure 2 specializations; no exhaustive document coverage or source-reliability guarantee inferred. | REVIEWER_INTERPRETATION; E08 |
| C12 / Standard | Document kind in the disjoint Figure 2 specializations; no exhaustive document coverage or source-reliability guarantee inferred. | REVIEWER_INTERPRETATION; E08 |
| C13 / Gray Literature | Document kind in the disjoint Figure 2 specializations; no exhaustive document coverage or source-reliability guarantee inferred. | REVIEWER_INTERPRETATION; E08 |
| C14 / White Literature | Document kind in the disjoint Figure 2 specializations; no exhaustive document coverage or source-reliability guarantee inferred. | REVIEWER_INTERPRETATION; E08 |
| C15 / Encyclopedia | Document kind in the disjoint Figure 2 specializations; no exhaustive document coverage or source-reliability guarantee inferred. | REVIEWER_INTERPRETATION; E08 |
| C16 / Specification | Category both in document classification and at the top of language specification refinement; no release identity inferred. | REVIEWER_INTERPRETATION; E08, E11 |
| C17 / Concept (abstract object) | Literal role box specializing Term, not an independently represented mental Concept kind. | REVIEWER_INTERPRETATION; E08 |
| C18 / Source | Relationally dependent rolemixin specializing Documents in Figure 2; broader information-source prose needs correspondence checks. | REVIEWER_INTERPRETATION; E08 |
| C19 / Documents | Category gathering document individuals with heterogeneous identity criteria. | REVIEWER_INTERPRETATION; E08 |
| C20 / Concept Definition | Relator mediating the displayed Concept role and Source, and composed into Domain Description; not automatically a truth assertion. | REVIEWER_INTERPRETATION; E08, E10 |
| C21 / Domain Description | Relator linking conceptualization and its representation language; one or more definition components are shown. | REVIEWER_INTERPRETATION; E08, E10 |
| C22 / Implementation | Role of Operational Ontology mediated with an implementation language by Ontology Schema. | REVIEWER_INTERPRETATION; E10 |
| C23 / Conceptualization | Role of Reference Ontology in this artifact metamodel; not equated with an episode of human conceptualizing. | REVIEWER_INTERPRETATION; E10 |
| C24 / Well-defined Ontology | Figure 3 role specializing Ontology Schema (a relator), not directly the Operational Ontology artifact; terminology does not establish adequacy. | REVIEWER_INTERPRETATION; E10 |
| C25 / Ontological Reference | Figure 3 role specializing Domain Description (a relator), not directly Reference Ontology; preserve these identity levels. | REVIEWER_INTERPRETATION; E10 |
| C26 / Language | Identity-bearing kind partitioned into computational/non-computational subtypes in the displayed fragment. | REVIEWER_INTERPRETATION; E10 |
| C27 / Non-Computational Language | Figure 3 uses subtype stereotype; representation-language role is below it. Do not silently call it subkind or prove exhaustiveness of all real languages. | REVIEWER_INTERPRETATION; E10 |
| C28 / Computational Language | Displayed subkind supporting Implementation Language role. | REVIEWER_INTERPRETATION; E10 |
| C29 / Representation Language | Role in Domain Description; prose also says Modeling Language, with correspondence retained rather than a new unproved class equivalence. | REVIEWER_INTERPRETATION; E10 |
| C30 / Implementation Language | Role mediated with an Implementation by Ontology Schema. | REVIEWER_INTERPRETATION; E10 |
| C31 / Ontology Schema | Relator for an implementation and implementation language; not itself a database schema imported or executed here. | REVIEWER_INTERPRETATION; E10 |
| C32 / Ontological Support | Relator behind implementationFor, mediating well-defined ontology and ontological reference roles. | REVIEWER_INTERPRETATION; E10 |
| C33 / Metamodel | Displayed subkind of Model, eligible for ontology-constrained role. | REVIEWER_INTERPRETATION; E11, E12 |
| C34 / Model | Kind used as the identity-bearing parent for metamodels. | REVIEWER_INTERPRETATION; E11, E12 |
| C35 / Ontology-Driven Modeling Language | Displayed subkind with a concrete-language role; OASIS and OntoUML illustrate domain/foundation driven variants. | REVIEWER_INTERPRETATION; E11, E12 |
| C36 / Ontology-Constrained Metamodel | Role of Metamodel mediated with an ontology supplying constraints. | REVIEWER_INTERPRETATION; E11, E12 |
| C37 / Ontological Constraints | Role of ontology artifact in the drives association; no complete OCL constraints printed. | REVIEWER_INTERPRETATION; E11, E12 |
| C38 / Concrete Ontology-Driven Language | Role participating in specification, with CODL {subsets CL} annotation. | REVIEWER_INTERPRETATION; E11, E12 |
| C39 / Ontology-Driven Metamodel | Relator connecting ontological constraints and constrained metamodel. | REVIEWER_INTERPRETATION; E11, E12 |
| C40 / Abstract Ontology-Driven Language | Literally a relator specializing Ontology-Driven Metamodel; not silently retyped as a Language kind. | REVIEWER_INTERPRETATION; E11, E12 |
| C41 / Ontology-Driven Language Specification | Relator mediated with abstract/concrete language sides; specializes Specification in the Figure 4 fragment. | REVIEWER_INTERPRETATION; E11, E12 |
| C42 / Ontological Foundation Constraints | Role of Foundational Ontology supplying foundational constraints; OFC {subsets OC} is printed. | REVIEWER_INTERPRETATION; E12, E13 |
| C43 / Direct Ontological Foundation | Foundational-ontology role refining Ontological Foundation. | REVIEWER_INTERPRETATION; E12, E13 |
| C44 / Foundational Ontology-Driven Metamodel | Relator specializing Ontology-Driven Metamodel and supporting the indirect-foundation refinement. | REVIEWER_INTERPRETATION; E12, E13 |
| C45 / Ontological Foundation | Rolemixin whose direct and indirect refinements permit different bearers; not an actual import declaration. | REVIEWER_INTERPRETATION; E12, E13 |
| C46 / Indirect Ontological Foundation | Role refining foundation and foundational ontology-driven metamodel in the diagram; actual model required for full semantics. | REVIEWER_INTERPRETATION; E12, E13 |
| C47 / Well-grounded Ontology | Role of Non-Foundational Ontologies in Ontological Grounding; conceptual grounding does not certify FAIR compliance. | REVIEWER_INTERPRETATION; E13 |
| C48 / Ontological Grounding | Relator behind groundedOver, mediating well-grounded ontology and ontological foundation. | REVIEWER_INTERPRETATION; E13 |
| C49 / Composite Ontology | Subkind with subOntology component relation and two-or-more parts shown. | REVIEWER_INTERPRETATION; E14 |
| C50 / Atomic Ontology | Complementary subkind to Composite Ontology in a complete disjoint set. | REVIEWER_INTERPRETATION; E14 |
| C51 / Ontology Network | Collective formed through membership of at least two ontology artifacts, not the same as ontology composition or reuse. | REVIEWER_INTERPRETATION; E14 |
| C52 / Reused Ontology | One role in Reusability; not disjoint from Reuser Ontology. | REVIEWER_INTERPRETATION; E14 |
| C53 / Reuser Ontology | The other reuse role; overlap allows chains and needs a separate path-cycle constraint. | REVIEWER_INTERPRETATION; E14 |
| C54 / Reusability | Relator deriving the displayed reuse material relation; not an empirical reuse-success metric. | REVIEWER_INTERPRETATION; E14 |
| C55 / Mental Concept / trope sense | Prose cognitive building block or mental representation discussed using UFO tropes; not the figure Term-role population. | AUTHOR_REPORTED; E07 |
| C56 / Object Kind / Trope Kind | Source contrasts syntactic Term object kind with the mental/trope notion; no OWL class census follows. | AUTHOR_REPORTED; E07 |
| C57 / Identity Principle | Principle invoked to identify individuals; its adequacy does not supply persistent identifiers or search services. | AUTHOR_REPORTED; E03 |
| C58 / Rigidity / cross-world identity | Modal ontological metaproperty invoked by the authors, distinct from persistent technical identity or discoverability. | AUTHOR_REPORTED; E03 |
| C59 / Kind / Subkind / Subtype | OntoUML identity/classification stereotypes used across the fragments; literal subtype label is retained. | AUTHOR_REPORTED; E06, E10 |
| C60 / Role / Rolemixin / Category | Dependent roles and cross-identity classifications used by the reference model; not modelled cognitive actions by default. | AUTHOR_REPORTED; E07, E08, E12 |
| C61 / Relator / material / mediation | Reification pattern used to ground associations in mediating relators; derivation/cardinalities require the actual model. | AUTHOR_REPORTED; E08, E10, E11, E13, E14 |
| C62 / Functional part-whole / componentOf | Composition distinction used for descriptions and composite ontologies; not identical to network membership. | AUTHOR_REPORTED; E08, E14 |
| C63 / Collective membership / memberOf | Ontology-network membership is a collective relation; separate from component composition. | AUTHOR_REPORTED; E14 |
| C64 / Weak Supplementation Pattern | Source invokes supplementation to motivate parts; reviewer distinguishes a proper-part supplement condition from a blanket two-parts claim about every whole. | AUTHOR_REPORTED; E14 |
| C65 / Ontological perspective | Engineer concern with foundation, real-world semantics and explicit characterization. | AUTHOR_REPORTED; E02, E04 |
| C66 / Domain perspective | Specialist concern with relevant knowledge, terminology, sources and practical domain requirements. | AUTHOR_REPORTED; E02, E04 |
| C67 / Ontology Engineer | Stakeholder can elicit requirements or act as project client depending on context; no disjoint person partition asserted. | AUTHOR_REPORTED; E04 |
| C68 / Domain Specialist / Cybersecurity specialist | Stakeholder contributes domain concepts, standards and requirements. | AUTHOR_REPORTED; E04, E15 |
| C69 / Literature Review Specialist | Member of the elicitation group, without a separately printed agent ontology or participant count. | AUTHOR_REPORTED; E04 |
| C70 / Ontological commitment | Perspective-dependent commitments should remain compatible across representations; no complete logic of commitment printed. | AUTHOR_REPORTED; E02, E09 |
| C71 / Cloud of concepts | Term/definition/source field enabling alternative domain usages across ontologies; not itself a proved consensus or truth set. | AUTHOR_REPORTED; E07, E15, E16 |
| C72 / Competence Questions / CQs | Requirements guide scope and evaluation; complete questions are external rather than printed in the paper. | AUTHOR_REPORTED; E04, E23 |
| C73 / SABiO | Adopted engineering methodology; methodological adoption is not evidence that every process obligation passed. | AUTHOR_REPORTED; E04, E17 |
| C74 / FAIR / findability / accessibility / interoperability / reusability | Normative guiding principles used to motivate classifications and network analysis; no scored compliance matrix in the paper. | AUTHOR_REPORTED; E01, E03, E19 |
| C75 / Applicability level | Reference/operational classification dimension; later prose also says Application Level. | AUTHOR_REPORTED; E05, E09 |
| C76 / Generality / knowledge kind | Classification into foundation/non-foundation and domain/task/application/core; literal Core mismatch remains. | AUTHOR_REPORTED; E05, E06 |
| C77 / Formalization level | Language-related classification dimension, not identical to computational expressiveness or decidability. | AUTHOR_REPORTED; E05 |
| C78 / Axiomatization level / lightweight / heavyweight | Distinction based on language/axiomatic commitments; article does not enumerate all corresponding model types. | AUTHOR_REPORTED; E05 |
| C79 / Expressiveness / decidability | Language capabilities and computational restrictions discussed as implementation concerns; no semantics-preserving translation proved. | AUTHOR_REPORTED; E05, E09 |
| C80 / UFO / UFO-A / UFO-B / UFO-C | Paper claims UFO grounding through OntoUML and uses A/B/C as a composition/reuse example; modules are not release editions. | AUTHOR_REPORTED; E01, E04, E14 |
| C81 / DOLCE | Illustrative foundational alternative in FAIR discussion, not O4OA grounding or a formal import. | AUTHOR_REPORTED; E03 |
| C82 / OntoUML / OCL | Reference modeling language and reported constraint language; no OCL code printed and no tool run performed by this review. | AUTHOR_REPORTED; E02, E17, E19 |
| C83 / OASIS / O3 | Illustrative ontology-driven domain-specific language and its grounding ontology; not an adopted O4OA import. | AUTHOR_REPORTED; E12 |
| C84 / F4OC / classification framework | Associated framework with five steps mentioned but not itemized in this article; current website uses other naming, not silently normalized. | AUTHOR_REPORTED; E03, E17, E21 |
| C85 / Operational prototype / microservices | Author-reported MongoDB, NodeJS/Express API, Angular Material frontend and Docker implementation. | AUTHOR_REPORTED; E15 |
| C86 / Regex traversal / API graph navigation | Syntactic recursive retrieval is reported; semantic reasoning is a future direction. | AUTHOR_REPORTED; E15, E16, E19 |
| C87 / Alloy instantiation / possible worlds | Package-level validation technique reported by authors; scopes, commands and outcomes are not reproduced here. | AUTHOR_REPORTED; E17 |
| C88 / Reuse transitive closure / acyclicity | Additional constraint reported after observing overlapping reuse roles; predicate is not printed. | AUTHOR_REPORTED; E17 |
| C89 / Persistence and API constraints | Authors split enforcement between storage and services; shared semantic behavior is not demonstrated by the article. | AUTHOR_REPORTED; E17 |
| C90 / Risk and associated concepts | Case discussion cites 18 Risk definitions and related Level of Risk, Residual Risk, Risk Criteria and eleven others; no full list or semantic alignment printed. | AUTHOR_REPORTED; E15 |
| C91 / Vulnerability | Figure 8 term with six abbreviated definition snippets, six source identifiers and two ontology uses; none establishes accepted equivalence. | AUTHOR_REPORTED; E16 |
| C92 / ISO/IEC 27032:2012 / ISO/IEC 27000:2018 | Referential cybersecurity terminology sources selected by the authors, not guarantee of universal consensus. | AUTHOR_REPORTED; E15, E16 |
| C93 / STIX / MAEC / NIST / ITU / CVE / CWE | Compared source families and displayed uses; source identity, version, quality and definition context require provenance. | AUTHOR_REPORTED; E15, E16 |
| C94 / OMV / printed OVM / ontology base / ontology document | Related metadata approach distinguishes conceptualization and realization; article criticism of its FAIRness is not independently established. | AUTHOR_REPORTED; E18 |
| C95 / SSN / oneM2M / SAREF / ODI / IoT / WoT | Related interoperability examples, not O4OA imports or reproduced comparative evaluation; standards provenance checked separately. | AUTHOR_REPORTED; E18, E24, E25 |
| C96 / Dublin Core / VoID / metadata repositories / Watson / AgroPortal | Related metadata vocabularies and repository applications; no complete feature or quality comparison in the article. | AUTHOR_REPORTED; E18 |
| C97 / Ontological Technical Depth | Future industrial-evaluation notion named in conclusion; no printed operational metric or measured results. | AUTHOR_REPORTED; E19 |

## Relations and formal commitments

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| K01 / Independent artifact partitions | Reference/Operational and Foundation/Non-foundation are independent complete disjoint partitions in Figure 1, not one four-way partition. | AUTHOR_REPORTED; E06 |
| K02 / Core hierarchy inconsistency | Literal Core -> Domain contrasts with note 5 generality; preserve both until exact artifact and intended meaning are checked. | REVIEWER_INTERPRETATION; E05, E06 |
| K03 / Mental versus syntactic Concept | Mental/trope prose and Concept-as-Term-role figure are separate senses; no identity or equivalence inferred. | REVIEWER_INTERPRETATION; E07, E08 |
| K04 / Source and document typing | Figure 2 Source specializes Documents; document specializations are disjoint but no complete set label is printed. | AUTHOR_REPORTED; E08 |
| K05 / Definition mediation | Concept Definition mediates the Concept role and Source; describes is material and has a visible derivation link. No full derivation formula printed. | AUTHOR_REPORTED; E08 |
| K06 / Definition composition | Figure 2 and 3 label Concept Definition 1..* / Domain Description 1 on componentOf; distinguish that fragment from global source-sharing claims. | AUTHOR_REPORTED; E08, E10 |
| K07 / Reference and implementation roles | Conceptualization specializes Reference Ontology; Implementation specializes Operational Ontology. A mental act is not thereby a conceptualization artifact. | AUTHOR_REPORTED; E09, E10 |
| K08 / Language partition | Figure 3 has complete/disjoint computational and non-computational branches, literal subtype/subkind stereotypes and their dependent roles. | AUTHOR_REPORTED; E10 |
| K09 / Schema and description relators | Domain Description mediates conceptualization/representation language; Ontology Schema mediates implementation/implementation language. | AUTHOR_REPORTED; E10 |
| K10 / Implementation support | implementationFor is shown between Well-defined Ontology and Ontological Reference and grounded by Ontological Support; no all-operational-ontologies adequacy theorem follows. | REVIEWER_INTERPRETATION; E09, E10 |
| K11 / Prior-reference norm | The assertion that there should be no operational ontology without a prior reference is a design norm, not a demonstrated fact about all ontology histories. | REVIEWER_INTERPRETATION; E09 |
| K12 / Ontology-driven metamodel | drives is material, with OC annotation, via Ontology-Driven Metamodel mediation; explicit constraints are not enumerated. | AUTHOR_REPORTED; E11 |
| K13 / Language specification | Literal specifies' relates abstract and concrete ontology-driven language sides; Abstract Ontology-Driven Language is a relator subtype. | AUTHOR_REPORTED; E11, E12 |
| K14 / Subset annotations | CODL {subsets CL} and OFC {subsets OC} are preserved as displayed role/constraint annotations, not expanded into invented quantifiers. | AUTHOR_REPORTED; E11, E12 |
| K15 / Foundation routes | Direct/indirect foundation distinctions and foundation-driven metamodel refinements are displayed; conceptual grounding differs from an OWL import. | REVIEWER_INTERPRETATION; E12, E13 |
| K16 / Grounding mediation | groundedOver is a material relation derived through Ontological Grounding, with Well-grounded Ontology and Ontological Foundation participants. | AUTHOR_REPORTED; E13 |
| K17 / Composition and atomicity | Composite and Atomic partition Ontology Artifact; componentOf subOntology is annotated with at least two parts and shareable/irreflexive/asymmetric/acyclic/transitive profile. | AUTHOR_REPORTED; E14 |
| K18 / Membership differs from composition | formedBy uses memberOf with Ontology Artifact 2..* / Ontology Network 1; neither is the reuse material relation. | AUTHOR_REPORTED; E14 |
| K19 / Reuse role overlap | Reused/Reuser roles have a complete but not disjoint set. Disjointness would suppress legal intermediate roles in reuse chains. | REVIEWER_INTERPRETATION; E14, E17 |
| K20 / Cycle avoidance requires a path condition | Authors report a transitive-closure predicate to avoid reuse cycles, but provide no printed predicate, scope or executed witness in this paper. A closure operator alone is not the no-cycle condition. | REVIEWER_INTERPRETATION; E17 |
| K21 / Supplementation scope | Source simplification of weak supplementation is not a general proof that every whole has two components; distinguish proper parthood, disjoint supplement and the selected diagram minimum. | REVIEWER_INTERPRETATION; E14 |
| K22 / Definitions are not automatically equivalent | The cloud retains many source descriptions of Risk/Vulnerability; retrieving shared labels or strings does not establish semantic identity, truth or consensus. | REVIEWER_INTERPRETATION; E15, E16 |
| K23 / Syntactic versus semantic operation | Recursive regex/graph retrieval and navigation are reported; reasoning about semantics/context/commitments and further logical implementations are future work. | AUTHOR_REPORTED; E15, E16, E19 |
| K24 / No full printed axiom set | Article explicitly omits axioms due to space and plans full formalization. OntoUML generalizations/cardinalities remain real diagram commitments; no numbered DL/FOL/OCL formulas or Alloy code printed. | AUTHOR_REPORTED; E19, E20 |
| K25 / Modular validation boundary | Alloy instantiation of individual packages does not by itself validate their full composition or the storage/API translation. No reviewer solver execution occurred. | REVIEWER_INTERPRETATION; E17 |
| K26 / Grounding versus FAIR | Author assertion of being FAIR is recorded as a claim; neither UFO labels nor a persistent internal identity establish an independently tested F/A/I/R profile. | REVIEWER_INTERPRETATION; E03, E19 |

## Complete paper relation index

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| R01 / Generalization and generalization sets | All visible fragments, stereotypes and complete/disjoint annotations are retained in figures.yaml; typed diagrams are not a released-class census. | AUTHOR_REPORTED; E06, E08, E10, E11, E12, E13, E14 |
| R02 / describes | Material association between displayed Concept and Source mediated by Concept Definition; left/right read marker retained without assuming a directed RDF property. | AUTHOR_REPORTED; E08 |
| R03 / componentOf / definitions | Definition-to-Domain Description composition, with literal 1..* and 1 endpoints. | AUTHOR_REPORTED; E08, E10 |
| R04 / usedToRepresent | Representation-language/conceptualization material association mediated by Domain Description. | AUTHOR_REPORTED; E10 |
| R05 / usedToImplement | Implementation-language/implementation material association mediated by Ontology Schema. | AUTHOR_REPORTED; E10 |
| R06 / implementationFor | Material association mediated by Ontological Support, not direct string identity between implementations/reference artifacts. | AUTHOR_REPORTED; E10 |
| R07 / drives / drives' | Constraint-bearing ontology and constrained metamodel linked through base/foundational metamodel relators; OC/OFC subset note preserved. | AUTHOR_REPORTED; E11, E12 |
| R08 / specifies' / prose specifys | Abstract/concrete language material association linked to specification relator; spelling and prime variation retained. | AUTHOR_REPORTED; E11, E12 |
| R09 / groundedOver / prose groundingOver | Foundation association mediated by Ontological Grounding, not a declared import statement. | AUTHOR_REPORTED; E13, E14 |
| R10 / subOntology / componentOf | Functional composition with printed shareability and strict relation profile; separate from membership and reuse. | AUTHOR_REPORTED; E14 |
| R11 / formedBy / memberOf | Collective network membership with printed 2..* /1 multiplicities. | AUTHOR_REPORTED; E14 |
| R12 / reuse / prose reuses | Material reuse relation and Reusability mediator, with separate reported cycle constraint. | AUTHOR_REPORTED; E14, E17 |
| R13 / mediation and derivation | Every displayed relator-participant association and dashed material-derivation link are inventoried at figure level; absent quantifiers remain unknown. | AUTHOR_REPORTED; E08, E10, E11, E12, E13, E14 |
| R14 / Tool source/definition/term/use links | Figure 8 colored source-to-definition, definition-to-term and definition-to-ontology links illustrate navigation; no new ontology relation declaration inferred. | AUTHOR_REPORTED; E16 |

## Requirements, examples and adverse cases

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| S01 / Engineer and specialist | Both perspectives supply knowledge and requirements to consensual characterization; neither replaces the other. | AUTHOR_REPORTED; E02, E04 |
| S02 / Stakeholder role switching | An engineer can be requirements elicitor or project client in different contexts; do not create disjoint person classes from these roles. | AUTHOR_REPORTED; E04 |
| S03 / Reference to operational counterpart | Trace a reference model through language/schema to an operational artifact, preserving which commitments the implementation retains. | AUTHOR_REPORTED; E09, E10 |
| S04 / No prior reference adverse case | Given an operational artifact lacking a documented prior reference, mark missing support; do not infer that it cannot exist or satisfies the author norm. | REVIEWER_INTERPRETATION; E09 |
| S05 / Term and multiple sources | Retain one syntax with multiple source-specific definitions and ontology uses; label-based merging is insufficient. | AUTHOR_REPORTED; E07, E08, E15 |
| S06 / Mental Concept adverse case | A personal mental representation and a Term role in a document need independent identity/bearer accounts; refuse automatic equivalence. | REVIEWER_INTERPRETATION; E07, E08 |
| S07 / Core/Domain adverse case | A source design describing Core as more general must not be silently migrated using the opposite arrow in Figure 1. | REVIEWER_INTERPRETATION; E05, E06 |
| S08 / Direct grounding | Record a non-foundational conceptualization grounded through a foundational ontology; keep exact edition unknown if absent. | AUTHOR_REPORTED; E13 |
| S09 / Indirect grounding | Trace an ontology through its ontology-driven language and constrained metamodel; ask which commitments survive implementation. | AUTHOR_REPORTED; E11, E12 |
| S10 / OASIS/O3 and OntoUML/UFO | Use the printed examples to distinguish domain-driven from foundation-driven languages without asserting their formal import identity. | AUTHOR_REPORTED; E12 |
| S11 / UFO composition and reuse | A/B/C illustrate that components may also reuse another component; preserve both different relations. | AUTHOR_REPORTED; E14 |
| S12 / Reuse chain | A reuses B and B reuses C can put B in both roles without a cycle; role disjointness is an inappropriate blanket repair. | REVIEWER_INTERPRETATION; E14, E17 |
| S13 / Reuse cycle adverse case | A reuses B and B reuses A requires an explicit path-cycle prohibition; adding transitivity alone does not remove it. | REVIEWER_INTERPRETATION; E17 |
| S14 / Network singleton adverse case | One ontology by itself does not satisfy the displayed network two-member minimum; whether this covers every intended real network is a modeling decision. | REVIEWER_INTERPRETATION; E14 |
| S15 / Shared component | Printed shareable composition allows a component in several composites; do not infer exclusive ownership from part-whole alone. | REVIEWER_INTERPRETATION; E14 |
| S16 / Risk terminology | The authors report eighteen Risk definitions and further risk-associated terms; no automatic consensus follows. | AUTHOR_REPORTED; E15 |
| S17 / Vulnerability trace | Follow the displayed term through six snippets and six source identifiers to CVE/CWE ontology uses; do not complete truncated text. | AUTHOR_REPORTED; E16 |
| S18 / Unreliable source adverse case | A listed source or technical record is provenance, not proof of an authoritative or context-adequate definition. | REVIEWER_INTERPRETATION; E15, E16 |
| S19 / Modular satisfiability adverse case | Individually plausible packages can conflict after composition; require an integrated bounded check before claiming whole-model consistency. | REVIEWER_INTERPRETATION; E17 |
| S20 / Persistence/API mismatch adverse case | A storage-accepted reuse edge can violate an API cycle check; require common versioned enforcement fixtures. | REVIEWER_INTERPRETATION; E17 |
| S21 / Grounded but inaccessible adverse case | A UFO-grounded artifact behind an unresolvable or inaccessible endpoint does not become FAIR merely from its modeling language. | REVIEWER_INTERPRETATION; E03, E19, E22 |
| S22 / Domain generalization | Cybersecurity demonstrations motivate other domains, but no cross-domain controlled effectiveness study is printed. | REVIEWER_INTERPRETATION; E17, E19 |
| S23 / Externally listed CQs | Use current author CQ JSON and prose mappings as separate versioned input; do not report those answers as executed paper tests. | REVIEWER_INTERPRETATION; E04, E23 |

## Critical findings

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| F01 / Substantial prior conceptualization support | The work already treats conceptualization/reference artifacts, definitions, perspectives, commitments and networks. A later novelty claim must identify a finer distinction than merely reifying conceptualization. | REVIEWER_INTERPRETATION; E01, E02, E07, E10 |
| F02 / Two perspectives are a strength | Explicit specialist/engineer contributions make terminology and ontology commitments traceable in a common setting; no communication-effect metric is printed. | REVIEWER_INTERPRETATION; E02, E04, E19 |
| F03 / FAIR is argued, not audited | The conclusion infers FAIRness from being well-grounded/well-defined. No indicator-level F/A/I/R assessment, access experiment or independent score appears. | REVIEWER_INTERPRETATION; E03, E19 |
| F04 / Identity and findability differ | Modal identity and rigidity are not sufficient implementation conditions for persistent identifiers, indexing, access or reuse licensing. | REVIEWER_INTERPRETATION; E03 |
| F05 / Classification choice lacks measured coverage | Most accepted/comprehensive claims motivate selected dimensions but no search protocol, frequency census or completeness measure is printed. | REVIEWER_INTERPRETATION; E05 |
| F06 / Core ordering conflicts | Figure 1 makes Core specialize Domain, while note 5 places Core more generally. Current author documentation repeats Domain including Core; historical intent remains unproved. | REVIEWER_INTERPRETATION; E05, E06, E21 |
| F07 / Concept identity shifts | Mental/trope prose, syntactic Term kind and Concept role labeled abstract object do not automatically share identity, dependence or cognitive bearer. | REVIEWER_INTERPRETATION; E07, E08 |
| F08 / Sources and document scope | Source is a rolemixin under Documents in Figure 2, while prose describes any relevant source. Dataset/service/record boundaries and source reliability are not fully defined. | REVIEWER_INTERPRETATION; E07, E08, E16 |
| F09 / Definition packaging is explicit but limited | Definition relators and 1..*/1 composition are concrete prior support. Sharing identical definitions across descriptions, versions and commitments requires exact identity/cardinality checks. | REVIEWER_INTERPRETATION; E08, E10 |
| F10 / Normative prior-reference requirement | Should-not-have-operational-without-reference is a design recommendation; the article does not show that all existing operational ontologies satisfy it. | REVIEWER_INTERPRETATION; E09 |
| F11 / Mixed language classification needs care | Computational versus non-computational partition and language roles are shown, but expressive and computational properties need selected language semantics. | REVIEWER_INTERPRETATION; E10, E11, E12 |
| F12 / Metamodel reification is already present | Constraints, specification and ontology-driven metamodel relators provide substantial prior artifact-level structure; abstract language is literally a relator in the diagrams. | REVIEWER_INTERPRETATION; E11, E12 |
| F13 / Grounding is not import or adequacy | Direct/indirect grounding is a conceptual relation, not an acquired formal import, exact UFO version or accepted alignment to Clariceptify. | REVIEWER_INTERPRETATION; E12, E13, E21 |
| F14 / Reuse/composition/membership distinction is useful | The source explicitly separates overlapping reuse, functional composition and network collective membership, each with different profiles. | REVIEWER_INTERPRETATION; E14 |
| F15 / Weak supplementation overstatement | The broad every-whole/two-parts gloss needs proper-part and disjoint-supplement qualification; the selected min-two component design is not a generic mereology theorem. | REVIEWER_INTERPRETATION; E14 |
| F16 / Network membership cardinality is restrictive | The printed 2..*/1 membership entails a selected one-network-per-artifact reading; versioning and multi-network reuse need the exact model, not an assumed correction. | REVIEWER_INTERPRETATION; E14 |
| F17 / Reuse roles must remain overlapping | The complete but non-disjoint role set permits legal chains. Authors report a separate cycle constraint; disjoint roles would overcorrect. | REVIEWER_INTERPRETATION; E14, E17 |
| F18 / Alloy evidence remains author-reported | No Alloy input, solver version, scope, commands, trace or independent run is in the selected paper/retrieved tree. Modular analysis does not establish integrated consistency. | REVIEWER_INTERPRETATION; E17, E22 |
| F19 / Full formalization is explicitly incomplete | Conclusion postpones full axioms. No printed OCL rules or complete axiom set can be reconstructed as author formulas; diagram commitments remain separately inventoried. | REVIEWER_INTERPRETATION; E02, E17, E19 |
| F20 / Prototype counts are not class counts | 161 concepts, 73 sources and 18 Risk definitions are reported case-dataset populations; they are neither released model classes nor independently verified complete datasets. | REVIEWER_INTERPRETATION; E15 |
| F21 / Retrieval does not yet reason about meaning | Authors explicitly describe syntactic regex traversal and leave semantic reasoning/context/commitment analytics to future work. | REVIEWER_INTERPRETATION; E15, E19 |
| F22 / Vulnerability screenshot is illustrative | Six abbreviated definitions plus source and use links show a trace route, not definition equivalence, source reliability, inference accuracy or the full data population. | REVIEWER_INTERPRETATION; E16 |
| F23 / Storage/API semantics are split | Enforcement across persistence and service needs consistency, transactional/concurrent behavior and translation checks; architecture names do not provide these results. | REVIEWER_INTERPRETATION; E15, E17 |
| F24 / General-purpose effectiveness not demonstrated | Case examples and claimed domain independence do not establish performance across other domains, user populations or industrial workflows. | REVIEWER_INTERPRETATION; E17, E19 |
| F25 / Related-work standards provenance requires correction | The blanket W3C label for SSN/oneM2M/SAREF is overbroad: checked historical SAREF metadata is ETSI and oneM2M cited cover is a oneM2M Partners draft. No standards-quality ranking follows. | REVIEWER_INTERPRETATION; E18, E24, E25 |
| F26 / OMV criticism is not independent evidence | Article assertions that OMV is not FAIR or lacks grounding are not an executed FAIR audit or complete comparison; preserve OMV/OVM spelling variation. | REVIEWER_INTERPRETATION; E18 |
| F27 / Repository availability is scoped | O4OA metadata/docs respond200 but its tree API403. The separate gO4OA light repository has a pinned eight-entry tree containing only five files (README, ignore file, logos, metadata), no formal root identified there. Neither observation proves global absence or historical parity. | REVIEWER_INTERPRETATION; E21, E22 |
| F28 / Current CQ text is a separate source | External current JSON and prose verification are accessible but unpinned to a 2023 commit; not evidence that every CQ was tested or answered by the supplied paper. Their prose mappings give structural candidate coverage, but source/definition traversal alone does not decide equal/equivalent/similar meanings. | REVIEWER_INTERPRETATION; E04, E23 |
| F29 / Names and identity levels differ | F4OC versus later naming and relation aliases remain explicit. More deeply, Figure 3 Ontological Reference specializes Domain Description and Well-defined Ontology specializes Ontology Schema: these relator roles must not be mistaken for the artifact classes. | REVIEWER_INTERPRETATION; E03, E10, E11, E14, E21 |
| F30 / Clariceptify remains unchanged | This completed paper review provides candidate comparison inputs. All-class/glossary/implementation checks remain91; comparison252 and final synthesis126 remain open. | REVIEWER_INTERPRETATION; E01, E17, E19, E22 |

## Unresolved questions

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Q01 / Exact roots and complete glossary | Pin an obtainable exact reference/operational model release, its tree/license/imports/modules and every selected class/type definition; keep absent populations null. Start with newly acquired44-page PROS-TR-2023-I specification v1, whose deep review is still pending; keep it distinct from the ER paper and metadata-only gO4OA tree. | REVIEWER_INTERPRETATION; E21, E22, E26 |
| Q02 / Typing, identity and diagram correspondence | Reconcile Core/Domain ordering, mental Concept versus Term role, Source/Document scope and role/relator refinements against the intended model. | REVIEWER_INTERPRETATION; E06, E07, E08, E10, E11, E12 |
| Q03 / Support and implementation constraints | Inspect material derivations, mediator participation, definition sharing and language/schema constraints; distinguish design norms from enforced restrictions. | REVIEWER_INTERPRETATION; E08, E09, E10, E17 |
| Q04 / Foundation correspondence | Record exact UFO/gUFO editions and direct/indirect grounding/import/translation evidence; current gO4OA documentation is a separate variant. | REVIEWER_INTERPRETATION; E12, E13, E21 |
| Q05 / Reuse, composition and network profiles | Check supplementation, strict component profiles, min-two and one-network cardinalities, legal role-overlap chains and actual cycle avoidance. | REVIEWER_INTERPRETATION; E14, E17 |
| Q06 / Definition provenance and context | Specify term/definition/source identities, version and context, divergent meanings, synonymy and source reliability without label-based equivalence. | REVIEWER_INTERPRETATION; E07, E08, E15, E16 |
| Q07 / Reproduce bounded model checks | Obtain exact OCL/Alloy files, scopes and commands, record modular and integrated checks separately, and trace current external CQs to selected constraints. | REVIEWER_INTERPRETATION; E17, E19, E23 |
| Q08 / Operational enforcement and evidence | Verify persistence/API translation with positive/adverse cases and separate case-dataset counts, syntactic navigation, future semantic reasoning and actual FAIR indicators. | REVIEWER_INTERPRETATION; E03, E15, E16, E17, E19 |

## Inputs for later synthesis

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Y01 / Prior overlap | Compare existing conceptualization artifacts, perspectives, commitments, source definitions and language-support relators before asserting novelty. | REVIEWER_INTERPRETATION; E02, E07, E10, E11 |
| Y02 / Terminology/provenance candidates | The source-definition-domain-description path is a candidate for a source-backed comparison scenario, not automatic adoption. | REVIEWER_INTERPRETATION; E08, E15, E16 |
| Y03 / Distinct network relations | Keep reuse, composition, membership and foundational grounding in separate comparison cells with exact evidence. | REVIEWER_INTERPRETATION; E12, E13, E14 |
| Y04 / Potential finer gaps | Individual conceptualizing episodes, decision/rationale/evidence, temporal context and semantic adjudication are not developed as a complete theory in this selected paper; evaluate against exact Clariceptify IDs later. | REVIEWER_INTERPRETATION; E04, E07, E17, E19 |
| Y05 / Assessment discipline | Do not inherit FAIR, consensus, semantic-reasoning or global-validity claims from author prose, architecture or modular Alloy checks. | REVIEWER_INTERPRETATION; E03, E15, E17, E19 |
| Y06 / Comparison and article revision deferred | After #86/#263/#77, integrate the source/version/definition/foundation matrix and determine bounded manuscript changes through #252/#126 and owner decision. | REVIEWER_INTERPRETATION; E01, E19, E21, E22 |

## Evaluation evidence

- **Verification:** Authors require CQ confrontation and report mappings externally; reviewer verified paper identity/coverage and current linked resources only, not CQ entailment or exact operational conformity. [REVIEWER_INTERPRETATION; E04, E17, E23]
- **Validation:** Authors report possible-world/Alloy package instantiation and additional cardinality/cycle constraints. No original execution logs, scope-complete integrated run or reviewer solver execution acquired. [AUTHOR_REPORTED; E17, E22]
- **Evaluation:** Cybersecurity use cases and navigation examples are reported with 161 concepts/73 sources/18 Risk definitions; no controlled utility, accuracy, performance or cross-domain measurement in this paper. [AUTHOR_REPORTED; E15, E16, E17]
- **Assessment:** Reviewer identifies substantial prior support and exact source discrepancies, but source-based critique is not independent domain-expert acceptance or an assessment of all current models. [REVIEWER_INTERPRETATION; E06, E07, E14, E17, E19]
- **Assurance:** Owner source digest, exact page/figure ledgers, hashed discovery and honest unknowns support traceability. They do not certify consensus, FAIRness, whole-model consistency, licensing or implementation quality. [REVIEWER_INTERPRETATION; E01, E20, E21, E22]

## Artifact and repository boundary

Technical follow-up: #91. State: `PUBLIC_METADATA_TREE_BLOCKED_TECHNICAL_REVIEW_OPEN`.

Paper is the2023 reference-model presentation and MongoDB/API prototype report. Current author documentation additionally describes UFO-A/B/C, gUFO/gO4OA and MongoO4OA. Checked O4OA repository-tree API returns403; no source commit, actual formal root/import/axiom population, license or historical2023 equivalence established. Full class/definition inventory and technical semantics remain #91. Current CQ/prose mappings are documentation claims, not rerun tests. Separate light-variant commit 3be36c642b2cfca33de3d0788471bc185880bde8 has a complete eight-entry tree with five files, metadata version 1.0 but no formal root found in that selected tree. Separate 44-page PROS-TR-2023-I specification v1 acquired for #91; it has not been deeply reviewed. Current linked CQ table has24 rows (three group and 21 subordinate questions), retained as short paraphrases in current-cqs.yaml.

## Evidence index

| ID | Exact source locator | Source-grounded summary |
|---|---|---|
| E01 | PDF 1 / printed 105, title, abstract, publication block | Five-author ER2023 chapter identity, DOI, reference-metaontology contribution and UFO grounding; owner bytes contain an acquisition watermark, not an author affiliation. |
| E02 | PDF 2-3 / printed 106-107, section 1 | Divergent specialist/engineer perspectives motivate consensual conceptualization and ontology-network analysis; reference OntoUML/OCL and operational REST/NoSQL versions are reported. |
| E03 | PDF 3-4 / printed 107-108, section 2 | Authors connect identity/rigidity and foundations to FAIR and discuss implementation-versus-foundation biases; these are arguments rather than a FAIR audit. |
| E04 | PDF 5 / printed 109, section 3.1 and notes 2-4 | SABiO; multidisciplinary online elicitation and role switching; full CQs delegated to website; no participant/sample/protocol counts or CQ list printed. |
| E05 | PDF 5-7 / printed 109-111, section 3.2, note 5 | Applicability, generality, formalization and axiomatization classifications; lightweight/heavyweight; alternatives excluded by asserted acceptance and complexity considerations. |
| E06 | PDF 6 / printed 110, Figure 1 and note 5 | Nine-box classification diagram: Core Ontology generalizes to Domain Ontology, while note 5 describes Core as more general than Domain/Task/Application. Preserve the discrepancy. |
| E07 | PDF 7-8 / printed 111-112, section 3.3 and note 6 | Mental Concept/trope discussion versus Term syntax/object kind and Concept as a term role; Source, Documents and definition relator with domain-description composition. |
| E08 | PDF 8 / printed 112, Figure 2 | Twelve boxes including Concept (abstract object), Term (syntax), six document specializations, Source, Documents and two relators; 1..* definitions per description and one description per displayed component. |
| E09 | PDF 8-9 / printed 112-113, section 3.4 opening | Reference/operational distinction and normative prior-reference claim; Conceptualization/Implementation roles; language and schema mediations. |
| E10 | PDF 9 / printed 113, Figure 3 and following prose | Sixteen boxes; two language branches and role/relator/material relations; usedToRepresent, usedToImplement and implementationFor, plus definition composition. |
| E11 | PDF 9 / printed 113, section 3.4 and Figure 4 | Eleven boxes connect models/metamodels, constraints, abstract/concrete ontology-driven languages and their specification; printed specifies' contrasts with prose specifys. |
| E12 | PDF 10 / printed 114, Figure 5 and preceding text | Sixteen boxes and two grounding routes; direct/indirect foundation versus language/metamodel constraints. OASIS/O3 and OntoUML/UFO are illustrative examples. |
| E13 | PDF 10-11 / printed 114-115, Figure 6 and grounding prose | Nine-box grounding fragment; groundedOver material relation and Ontological Grounding relator; conceptual grounding is not a formal import declaration. |
| E14 | PDF 11 / printed 115, Figure 7 and reuse/composition prose | Seven boxes: composite/atomic partition, overlapping reused/reuser roles, Reusability and collective Ontology Network; component and member cardinalities/profiles; UFO-A/B/C example. |
| E15 | PDF 12 / printed 116, section 3.5 and notes 7-8 | Author-reported MongoDB/NodeJS/Express/Angular Material/Docker prototype; manually loaded data, 161 cybersecurity concepts, 73 sources, 18 Risk definitions; syntactic recursive/regex retrieval and future semantic reasoning. |
| E16 | PDF 13 / printed 117, Figure 8 and accompanying text | Fifteen-node example graph: one Vulnerability term, six definition snippets, six source identifiers and two ontology uses. API navigation is reported; screenshot is not a benchmark or full database export. |
| E17 | PDF 13-14 / printed 117-118, section 4 | Author-reported package-by-package Alloy instantiation/cardinality analysis; additional reuse cycle constraint; persistence/API enforcement split; evaluation details and case studies external. |
| E18 | PDF 14-15 / printed 118-119, section 5 and notes 9-10 | IoT/WoT, OMV (also printed OVM), metadata repositories, and domain-independent comparison claims; author groups SSN/oneM2M/SAREF as W3C standards, requiring attribution/correction. |
| E19 | PDF 15-16 / printed 119-120, section 6 and acknowledgments | Contributions and intended analytics/reasoning; explicitly no axioms included due to space, full axiomatization and further industrial evaluation future; ontology-driven/FAIR conclusion not independently tested. |
| E20 | Notes1-10; acknowledgments PDF 16; references PDF 17-20 / printed 121-124 | All ten numbered notes and all 66 numbered references inspected; no appendices, numbered tables, OCL/Alloy code blocks or numbered formulas in the selected paper. |
| E21 | https://bfmartins.gitlab.io/o4oa/content/o4oa.html; 2026-10-28; receipt evaluation/related-work/o4oa/discovery.json | Current author documentation consulted for linked CQ verification and UFO-A/B/C/gUFO variants. This is not a version-pinned 2023 formal artifact. |
| E22 | https://gitlab.com/api/v4/projects/bfmartins%2Fo4oa; 2026-10-28; receipt evaluation/related-work/o4oa/discovery.json | Public project metadata was retrieved; selected repository-tree API returned403. Commit/default branch/archival/license/test fields were not exposed in the retrieved metadata. |
| E23 | https://bfmartins.gitlab.io/o4oa/assets/data/cqs.json; 2026-10-28; receipt evaluation/related-work/o4oa/discovery.json | Current externally linked CQ JSON retrieved separately from the paper. Its rows are current documentation claims, not printed paper requirements or executed answers. |
| E24 | https://saref.etsi.org/core/v3.1.1/; selected publisher/cover metadata inspected 2026-10-28 | Historical SAREF3.1.1 author specification identifies ETSI SmartM2M and ETSI TS103264, rather than a blanket W3C standards origin; this external check does not assess SAREF grounding. |
| E25 | https://www.onem2m.org/images/pdf/TS-0012-Base_Ontology-V3_7_3.pdf; selected publisher/cover metadata inspected 2026-10-28 | The paper-cited TS0012 V3.7.3 cover identifies oneM2M Partners and a draft approval warning, not W3C. Cover metadata only; no full oneM2M review claimed. |
| E26 | bfmartins/go4oa at3be36c642b2cfca33de3d0788471bc185880bde8; README and scr/metadata/metadata.yaml; evaluation/related-work/o4oa/discovery.json | Selected current light-variant metadata declares version 1.0 and an OWL/Turtle intent. Eight-entry recursive tree has five files, no formal model identified; declared metadata and tool versions are not actual OWL bytes or executed tools. The separate 44-page technical specification was acquired for #91, not reviewed as this paper. |

## Closure boundary

Exact 20-page primary-paper critical review complete. Findings and candidate reuse are not accepted semantic changes. Full reference/operational type/class/definition/import/license/version/correspondence and bounded semantics stay #91; comparison #252 and final synthesis #126 remain OPEN. No ontology, requirements, fixtures, manuscript or release changes. Continue acquired primary texts #86, #263, #77 before synthesis; I&DA #84 still lacks retained full text.
