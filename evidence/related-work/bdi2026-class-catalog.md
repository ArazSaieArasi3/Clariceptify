# BDI 2026: complete selected class glossary

Issue #250. Distinct URI subjects explicitly owl:Class or rdfs:Class; BDI and d0 local namespaces separate. Alignment references are not new declarations. RDF/XML serialization isomorphic to Turtle is not counted twice. Unrelated modules and data-instance types are not class declarations.

All comment/definition annotations inspected. Publish short attributed reviewer paraphrases and annotation digests, never bulk raw comments. Incomplete, absent and prose-only deprecation states stay explicit. No independently accepted logical definition or human validation is inferred.

22 BDI domain classes, three external metadata/test declarations and ten d0 classes are accounted for here. The 78 DUL classes reuse the [existing source-pinned glossary](dul-class-catalog.md); they are not duplicated.

One BDI Belief comment ends mid-sentence. Three external class declarations have no definition in the selected source. Missing definitions are not invented. The exact alignment import of BDI0.3 is unavailable; its full population remains unknown.

| Module | Class / label | Source definition state | Attributed reviewer paraphrase |
|---|---|---|---|
| bdi/bdi.ttl | [Vocabulary](http://purl.org/vocommons/voaf#Vocabulary) | NOT_REPORTED_IN_SELECTED_SOURCE | NOT_REPORTED |
| bdi/bdi.ttl | [CompetencyQuestionVerification](https://w3id.org/OWLunit/ontology/CompetencyQuestionVerification) | NOT_REPORTED_IN_SELECTED_SOURCE | NOT_REPORTED |
| bdi/bdi.ttl | [TestSuite](https://w3id.org/OWLunit/ontology/TestSuite) | NOT_REPORTED_IN_SELECTED_SOURCE | NOT_REPORTED |
| bdi/bdi.ttl | [Action](https://w3id.org/fossr/ontology/bdi/Action) | PRESENT_COMMENT_CANDIDATE | An activity that an agent actually performs, distinguished from an activity specification. |
| bdi/bdi.ttl | [Agent](https://w3id.org/fossr/ontology/bdi/Agent) | PRESENT_COMMENT_CANDIDATE | An autonomous perceiver and actor whose beliefs, desires and intentions guide its conduct. |
| bdi/bdi.ttl | [Belief](https://w3id.org/fossr/ontology/bdi/Belief) | PARTIAL_COMMENT_CANDIDATE | An agent takes a state of affairs to hold, without a guarantee that it matches reality. |
| bdi/bdi.ttl | [Belief Formation](https://w3id.org/fossr/ontology/bdi/BeliefProcess) | PRESENT_COMMENT_CANDIDATE | A cognitive operation that forms or revises belief through observation, inference or communication. |
| bdi/bdi.ttl | [Desire](https://w3id.org/fossr/ontology/bdi/Desire) | PRESENT_COMMENT_CANDIDATE | A motivational preference for an outcome that does not itself commit the agent to act. |
| bdi/bdi.ttl | [Desire Formation](https://w3id.org/fossr/ontology/bdi/DesireProcess) | PRESENT_COMMENT_CANDIDATE | An operation that develops or changes an agent's motivational preferences. |
| bdi/bdi.ttl | [Goal](https://w3id.org/fossr/ontology/bdi/Goal) | PRESENT_COMMENT_CANDIDATE | A preferred outcome used to orient later commitment and planning; its comment overlaps desire terminology. |
| bdi/bdi.ttl | [Goal Process](https://w3id.org/fossr/ontology/bdi/GoalProcess) | PRESENT_COMMENT_CANDIDATE | An operation that turns broad preferences into more specific outcomes to pursue. |
| bdi/bdi.ttl | [Intention](https://w3id.org/fossr/ontology/bdi/Intention) | PRESENT_COMMENT_CANDIDATE | A deliberative commitment to pursue an outcome or course of action under perceived conditions. |
| bdi/bdi.ttl | [Intention Formation](https://w3id.org/fossr/ontology/bdi/IntentionProcess) | PRESENT_COMMENT_CANDIDATE | An operation that selects and refines commitments in light of desires and resources. |
| bdi/bdi.ttl | [Justification](https://w3id.org/fossr/ontology/bdi/Justification) | PRESENT_COMMENT_CANDIDATE | A stated rationale or evidence offered in support of mental content. |
| bdi/bdi.ttl | [Mental entity](https://w3id.org/fossr/ontology/bdi/MentalEntity) | PRESENT_COMMENT_CANDIDATE | A general category spanning mental states and the cognitive processes that operate on them. |
| bdi/bdi.ttl | [Mental Process](https://w3id.org/fossr/ontology/bdi/MentalProcess) | PRESENT_COMMENT_CANDIDATE | A cognitive operation that considers, produces or changes mental content. |
| bdi/bdi.ttl | [Mental state](https://w3id.org/fossr/ontology/bdi/MentalState) | PRESENT_COMMENT_CANDIDATE | An internal cognitive or affective condition that can change with context or reasoning. |
| bdi/bdi.ttl | [Plan](https://w3id.org/fossr/ontology/bdi/Plan) | PRESENT_COMMENT_CANDIDATE | A structured description of steps by which an agent proposes to pursue an outcome. |
| bdi/bdi.ttl | [Plan](https://w3id.org/fossr/ontology/bdi/PlanExecution) | PRESENT_COMMENT_CANDIDATE | The situated enactment of a plan, distinct from its prospective specification. |
| bdi/bdi.ttl | [Planning](https://w3id.org/fossr/ontology/bdi/Planning) | PRESENT_COMMENT_CANDIDATE | A cognitive operation that organizes candidate steps and resources into a plan. |
| bdi/bdi.ttl | [Task](https://w3id.org/fossr/ontology/bdi/Task) | PRESENT_COMMENT_CANDIDATE | The specification of an intended activity in a plan, distinct from its enactment. |
| bdi/bdi.ttl | [Temporal entity](https://w3id.org/fossr/ontology/bdi/TemporalEntity) | PRESENT_COMMENT_CANDIDATE | A general representation of temporal points and extended spans. |
| bdi/bdi.ttl | [Time istant](https://w3id.org/fossr/ontology/bdi/TimeInstant) | PRESENT_COMMENT_CANDIDATE | A temporal point used to anchor occurrences or interval boundaries. |
| bdi/bdi.ttl | [Time interval](https://w3id.org/fossr/ontology/bdi/TimeInterval) | PRESENT_COMMENT_CANDIDATE | A temporal span used to represent an occurrence or validity extent. |
| bdi/bdi.ttl | [World state](https://w3id.org/fossr/ontology/bdi/WorldState) | PRESENT_COMMENT_CANDIDATE | A contextual environmental condition represented or perceived by an agent. |
| d0 | [activity](http://www.ontologydesignpatterns.org/ont/d0.owl#Activity) | PRESENT_COMMENT_CANDIDATE | A deliberately caused action or task, grouping planned specifications and occurrences when data are ambiguous. |
| d0 | [characteristic](http://www.ontologydesignpatterns.org/ont/d0.owl#Characteristic) | PRESENT_COMMENT_CANDIDATE | An aspect or dimensional attribute of something, spanning several possible formal categories. |
| d0 | [cognitive entity](http://www.ontologydesignpatterns.org/ont/d0.owl#CognitiveEntity) | PRESENT_COMMENT_CANDIDATE | Cognitive phenomena that may be modeled at object, occurrence, attribute or public-concept levels. |
| d0 | [CollectiveEntity](http://www.ontologydesignpatterns.org/ont/d0.owl#CollectiveEntity) | PRESENT_COMMENT_CANDIDATE | A broad category spanning socially constituted collections and distributed aggregates. |
| d0 | [domain](http://www.ontologydesignpatterns.org/ont/d0.owl#Domain) | PRESENT_COMMENT_CANDIDATE | An organized field of knowledge synthesizing subjects and other cultural content. |
| d0 | [event](http://www.ontologydesignpatterns.org/ont/d0.owl#Event) | PRESENT_COMMENT_CANDIDATE | A broad event-or-event-type category; its comment expressly marks it deprecated. |
| d0 | [eventuality](http://www.ontologydesignpatterns.org/ont/d0.owl#Eventuality) | PRESENT_COMMENT_CANDIDATE | A category grouping occurrences, activities, types and relational settings without forcing their disambiguation. |
| d0 | [location](http://www.ontologydesignpatterns.org/ont/d0.owl#Location) | PRESENT_COMMENT_CANDIDATE | A broad location category spanning geographic entities, situated artifacts and spatial representations. |
| d0 | [subject](http://www.ontologydesignpatterns.org/ont/d0.owl#Subject) | PRESENT_COMMENT_CANDIDATE | Anything treated as the focus of an informational or communicative act. |
| d0 | [system](http://www.ontologydesignpatterns.org/ont/d0.owl#System) | PRESENT_COMMENT_CANDIDATE | An organized physical, social or abstract whole whose components have interdependencies. |

## Identity, hierarchy and constraints

The [structured authority](bdi2026-class-catalog.yaml) records every exact IRI, label basis, source hash, comment digest/locator, deprecated flag, named superclass, equivalence, direct and incoming disjointness, complete n-ary disjoint group and constraint pointer. The [census](../../evaluation/related-work/bdi2026/technical-census.json) also preserves property axioms and separates declarations, undeclared class-position references, anonymous expressions and builtin vocabulary.

d0 Event is described as deprecated in prose, without an owl:deprecated true assertion. d0 versionInfo contains entries1.2 through1.5, without a versionIRI;DUL4.2 is the current exact retrieved root. These bytes do not establish historical paper equivalence.

Core0.5 has no imports. The alignment references d0 and BDI0.3;d0 imports DUL. The acquired foundation closure has 89 distinct declared named IRIs, including owl:Thing. Three core external redeclarations (VOAF/OWLUnit) are metadata/test vocabulary, not three additional BDI domain concepts or an acquired upstream definition glossary.

No Clariceptify model change, independent expert approval or accepted reuse.
