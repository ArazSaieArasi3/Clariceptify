# cDnS-journal-2008: selected class glossary

Issue #267. All51 declared named owl:Class IRIs, deduplicated by IRI, across selected collInt25, mapped ground14 and retained cDnS12. The original import endpoints failed; the explicit namespace/file map is not historical byte-fidelity proof.

Every definition below is a short reviewer paraphrase of the source comment. A comment may be incomplete, informal or ambiguous; logical constraints are recorded separately. MISSING means no source definition comment was found in the selected bytes, not that no definition exists anywhere.

| Module | Local classes | External redeclarations | Source version |
|---|---|---|---|
| collInt | 25 | 0 | ['1.0', '1.0, created by Aldo Gangemi'] |

Source: http://www.loa-cnr.it/ontologies/collInt.owl. SHA256 `379ada879ccf8e87bc912635f9bebd25df004b033dfa3f65c165480772679200`. All named declarations and outgoing constraints: [collInt census](collInt-census.json).

| ground | 14 | 0 | ['1.0', '1.0, created by Aldo Gangemi'] |

Source: http://www.ontologydesignpatterns.org/ont/cdns/ground.owl. SHA256 `ac10db67bbb3fd7b611ea492c5ae828889974892329b61f1f75e8ba45b57182b`. All named declarations and outgoing constraints: [ground census](ground-census.json).

| cDnS | 12 | 0 | ['1.1', 'Created by Aldo Gangemi\nVersion 1.1 aligns cDnS with the axiomatization in the article JAAMAS 2008.'] |

Source: http://www.ontologydesignpatterns.org/ont/cdns/cDnS.owl. SHA256 `f0d7b6c795fe9e1a699eda2d80089371336869e981e938648edd5db88358658a`. All named declarations and outgoing constraints: [cDnS census](../cDnS2007/artifact-census.json).

| Class IRI | Definition / missing state | Named superclasses | Notes |
|---|---|---|---|
| http://www.loa-cnr.it/ontologies/collInt.owl#AgentCollection | Collection restricted to social-agent members; a common externally visible property need not be conceptualized by its members. | http://www.loa-cnr.it/ontologies/cDnS.owl#Collection | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#AgentRole | Classifier whose fillers are social or physical agents. | http://www.loa-cnr.it/ontologies/cDnS.owl#Concept | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#Classification | Situation for recording a concept, classified entity and interval together. | http://www.loa-cnr.it/ontologies/cDnS.owl#Situation | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#ConstitutiveDescription | Description that introduces some social agent. | http://www.loa-cnr.it/ontologies/cDnS.owl#Description | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#Desire | Primitive descriptive representation of what an agent wants. | http://www.loa-cnr.it/ontologies/cDnS.owl#Description | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#EpistemicRelation | Norm-plan bundle organizing a community's shared core knowledge. | http://www.loa-cnr.it/ontologies/collInt.owl#NormPlanBundle | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#Goal | Desire contained as a proper part of some plan. | http://www.loa-cnr.it/ontologies/collInt.owl#Desire | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#GoalSituation | Situation satisfying a goal. | http://www.loa-cnr.it/ontologies/cDnS.owl#Situation | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#IntentionalCollective | Knowledge community unified by a plan. | http://www.loa-cnr.it/ontologies/collInt.owl#KnowledgeCommunity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#KnowledgeCollective | Normative collective unified by an epistemic relation carrying a paradigm. | http://www.loa-cnr.it/ontologies/collInt.owl#NormativeIntentionalCollective | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#KnowledgeCommunity | Collection of agents each sharing some knowledge corpus. | http://www.loa-cnr.it/ontologies/collInt.owl#AgentCollection | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#KnowledgeCorpus | Collection consisting of at least two descriptions. | http://www.loa-cnr.it/ontologies/cDnS.owl#Collection | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#KnowledgeRole | Concept classifying informational expressions of paradigm descriptions. | http://www.loa-cnr.it/ontologies/cDnS.owl#Concept | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#Norm | Regulatory description combining conventions, case interpretation and constraints on action schemas. | http://www.loa-cnr.it/ontologies/cDnS.owl#Description | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#NormApplication | Situation applying a norm to interpret another situation. | http://www.loa-cnr.it/ontologies/cDnS.owl#Situation | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#NormPlanBundle | Bundle containing mutually entrenched plan and norm descriptions. | http://www.loa-cnr.it/ontologies/cDnS.owl#Bundle | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#NormativeIntentionalCollective | Knowledge community unified by a norm-plan bundle. | http://www.loa-cnr.it/ontologies/collInt.owl#KnowledgeCommunity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#Organization | Social agent acted for by members of intentional collectives. | http://www.loa-cnr.it/ontologies/cDnS.owl#SocialAgent | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#Paradigm | Bundle of descriptions assumed within knowledge communities. | http://www.loa-cnr.it/ontologies/cDnS.owl#Bundle | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#Parameter | Concept classifying value-like regions, places, qualities or intervals. | http://www.loa-cnr.it/ontologies/ground.owl#DomainConcept | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#Plan | Action-schema description shared by an agent, using role/task concepts and containing a goal. | http://www.loa-cnr.it/ontologies/cDnS.owl#Description | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#PlanExecution | Situation proactively satisfying a plan. | http://www.loa-cnr.it/ontologies/cDnS.owl#Situation | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#Role | Concept classifying object-like entities and targeting tasks. | http://www.loa-cnr.it/ontologies/ground.owl#DomainConcept | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#SocialRelation | Epistemic relation assumed by agents within knowledge collectives. | http://www.loa-cnr.it/ontologies/collInt.owl#EpistemicRelation | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/collInt.owl#Task | Concept classifying action-like entities. | http://www.loa-cnr.it/ontologies/ground.owl#DomainConcept | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#Action | Ground-domain action interpreted under a description. | http://www.loa-cnr.it/ontologies/ground.owl#DomainEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#Aggregate | Ground entity treated as a sum of members or situation setting entities. | http://www.loa-cnr.it/ontologies/cDnS.owl#GroundEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#DomainConcept | Concept classifying only ground-domain entities. | http://www.loa-cnr.it/ontologies/cDnS.owl#Concept | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#DomainEntity | Generic ground entity classified through domain descriptions. | http://www.loa-cnr.it/ontologies/cDnS.owl#GroundEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#Event | Ground event given a descriptive interpretation. | http://www.loa-cnr.it/ontologies/ground.owl#DomainEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#IndividualConstruct | Individual grounding counterpart of a schematic entity. | http://www.loa-cnr.it/ontologies/cDnS.owl#GroundEntity; http://www.loa-cnr.it/ontologies/cDnS.owl#NonSchematicEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#InformationRealization | Physical support realizing an information object. | http://www.loa-cnr.it/ontologies/cDnS.owl#GroundEntity; http://www.loa-cnr.it/ontologies/cDnS.owl#NonSchematicEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#Location | Ground entity used to locate something in a descriptive frame. | http://www.loa-cnr.it/ontologies/ground.owl#DomainEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#Object | Ground object interpreted within a descriptive frame. | http://www.loa-cnr.it/ontologies/ground.owl#DomainEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#PhysicalAgent | Ground entity acting for a social agent and constructing an individual counterpart. | http://www.loa-cnr.it/ontologies/cDnS.owl#GroundEntity; http://www.loa-cnr.it/ontologies/cDnS.owl#NonSchematicEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#Quality | Ground entity playing a quality role in a descriptive frame. | http://www.loa-cnr.it/ontologies/ground.owl#DomainEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#Region | Ground region interpreted by a description. | http://www.loa-cnr.it/ontologies/ground.owl#DomainEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#Substance | Ground nonschematic substance under a description. | http://www.loa-cnr.it/ontologies/cDnS.owl#NonSchematicEntity; http://www.loa-cnr.it/ontologies/ground.owl#DomainEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/ground.owl#TimeInterval | Ground interval used in a descriptive context. | http://www.loa-cnr.it/ontologies/ground.owl#DomainEntity | Current selected source, not a certified2008 original release. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Bundle | Multiple descriptions combined through common satisfaction or collection characterization. | http://www.loa-cnr.it/ontologies/cDnS.owl#Description | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Collection | A group whose membership has shared criteria. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Concept | A category defined within one description. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Configuration | A collection of parts unified by a description. | http://www.loa-cnr.it/ontologies/cDnS.owl#Collection | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Description | A communicable conceptualization dependent on social agents. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Entity | Anything admitted within the selected domain. | http://www.w3.org/2002/07/owl#Thing | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#GroundEntity | An entity contextualized through description. | http://www.loa-cnr.it/ontologies/cDnS.owl#Entity | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#InformationObject | Historically situated information independent of a particular physical carrier. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#NonSchematicEntity | An entity outside the schematic category; source wording is ambiguous. | http://www.loa-cnr.it/ontologies/cDnS.owl#Entity | The comment negates schematic membership but its following explanation can be read inconsistently. Use the declared disjointness as a separate formal observation; do not silently repair the source.; Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity | A primitive used to construct social reality. | http://www.loa-cnr.it/ontologies/cDnS.owl#Entity | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Situation | A relational context viewed through a description. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#SocialAgent | A socially constituted bearer of shared conceptualizations. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity | Reused same source digest and existing12-class glossary; journal-specific review does not assert historical byte equivalence. |

Full labels, definition/annotation hashes, exact source IRIs/predicates, deprecated status, equivalence counts and constraint pointers are retained in [classes.yaml](classes.yaml).

Local classes: 51; source comment candidates: 51; missing source definitions: 0.

Imported glossary: ALL_SELECTED_MAPPED_IMPORT_CLASS_COMMENTS_ACCOUNTED_FOR. Mapped closure only. Original-host parity, undeclared shares/isSharedBy, current1.0-to1.1 compatibility, profile and semantics remain open. owl:Thing is builtin, not a52nd local glossary item.

Reasoning: NOT_EXECUTED. Historical paper fidelity: NOT_ESTABLISHED. Model change: NONE.
