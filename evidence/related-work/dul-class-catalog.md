# DUL 4.2 complete local-class glossary

Issue #88. Source-pinned research evidence; no Clariceptify model change.

Source SHA256: `e5f6429596d2c7014730bad85aaaa9c39530235f27f596cd0e7ce85e6bbcba66`. Current root: 78 local named classes plus a separate `owl:Thing` redeclaration. No declared imports or deprecated classes.

Annotation review: 69 classes carry comment candidates; 67 support short reviewer paraphrases; two comments merely restate labels; nine classes have no prose comment. There are no reviewer reconstructions. 4 classes have asserted equivalent-class expressions, recorded separately from prose availability.

Every paraphrase below is attributed to the named class comment in the selected DUL root, not quoted text or an independent definition. The YAML retains exact IRI, annotation hashes, hierarchy, equivalent expressions, all outgoing structural constraints and explicit missing states. It is the complete evidence record.

| Class | Attributed reviewer paraphrase / gap | Named direct superclass(es) | Constraint ID |
| --- | --- | --- | --- |
| [Abstract](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Abstract) | An entity outside spatial and temporal location, including mathematical structures. | Entity | DUL-C001 |
| [Action](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Action) | An event involving an agent and execution of a task, commonly situated within a plan. | Event | DUL-C002 |
| [Agent](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent) | An object treated as capable of agency, whether a physical bearer or a socially constituted agent. | Object | DUL-C003 |
| [Amount](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Amount) | Quantity considered without committing to a measurement procedure. | Region | DUL-C004 |
| [BiologicalObject](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#BiologicalObject) | No prose comment in selected root. | PhysicalBody | DUL-C005 |
| [ChemicalObject](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#ChemicalObject) | No prose comment in selected root. | PhysicalBody | DUL-C006 |
| [Classification](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Classification) | A situation recording which concept classifies an entity at a specified time. | TimeIndexedRelation | DUL-C007 |
| [Collection](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Collection) | A first-order grouping united by shared characteristics, distinguished from both a logical class and an aggregate. | SocialObject | DUL-C008 |
| [Collective](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Collective) | A collection of agents; collective membership alone does not make that collection a social agent. | Collection | DUL-C009 |
| [CollectiveAgent](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#CollectiveAgent) | A social agent whose action is carried out by members of a corresponding collective, unified through a description. | SocialAgent | DUL-C010 |
| [Community](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Community) | No prose comment in selected root. | CollectiveAgent | DUL-C011 |
| [Concept](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Concept) | A socially constituted entity defined within a description and potentially reused elsewhere to classify entities. | SocialObject | DUL-C012 |
| [Configuration](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Configuration) | A collection organized by a unifying schema expressible as a description. | Collection | DUL-C013 |
| [Contract](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Contract) | Agreement content connecting two or more parties around an undertaking to be performed. | Description | DUL-C014 |
| [Description](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description) | A social representation of a conceptualization that frames situations through concepts it defines or uses. | SocialObject | DUL-C015 |
| [Design](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Design) | A description of an entity's structural and functional arrangement, typically informed by construction or repurposing reasons. | Description | DUL-C016 |
| [DesignedArtifact](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#DesignedArtifact) | A physical artifact with an accompanying design, excluding mere reuse of an unchanged natural object. | PhysicalArtifact | DUL-C017 |
| [DesignedSubstance](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#DesignedSubstance) | No prose comment in selected root. | DesignedArtifact, FunctionalSubstance | DUL-C018 |
| [Diagnosis](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Diagnosis) | A description interpreting a system's situation, for example to explain deviations or regulate its behavior. | Description | DUL-C019 |
| [Entity](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Entity) | Whatever a modeler elects to discuss, including hypothetical or imagined referents. | None asserted | DUL-C020 |
| [Event](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event) | A physical, social, or mental occurrence, process, or state; alternative interpretations can be represented through distinct situations. | Entity | DUL-C021 |
| [EventType](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#EventType) | A concept supplying a description-dependent interpretation or expectation for events. | Concept | DUL-C022 |
| [FormalEntity](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#FormalEntity) | An abstract formally defined entity considered independently of its social use, unlike socially situated concepts or information objects. | Abstract | DUL-C023 |
| [FunctionalSubstance](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#FunctionalSubstance) | No prose comment in selected root. | Substance | DUL-C024 |
| [Goal](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Goal) | A description of a situation an agent wants to obtain, often linked to a plan for obtaining it. | Description | DUL-C025 |
| [Group](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Group) | A collective agent whose acting members conceptualize a shared social relation. | CollectiveAgent | DUL-C026 |
| [InformationEntity](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#InformationEntity) | An umbrella for information content and its concrete realizations when their distinction is intentionally left open. | Entity | DUL-C027 |
| [InformationObject](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#InformationObject) | Information content considered separately from the concrete forms that realize it. | InformationEntity, SocialObject | DUL-C028 |
| [InformationRealization](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#InformationRealization) | A concrete embodiment or performance of information content, also capable of realizing information about itself. | InformationEntity | DUL-C029 |
| [LocalConcept](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#LocalConcept) | A concept defined by exactly one description; other descriptions may use it without becoming its defining description. | Concept | DUL-C030 |
| [Method](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method) | A description guiding problem-solving actions, potentially followed through different plans. | Description | DUL-C031 |
| [Narrative](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Narrative) | No prose comment in selected root. | Description | DUL-C032 |
| [NaturalPerson](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#NaturalPerson) | A person considered as a physical human individual. | Person, PhysicalAgent | DUL-C033 |
| [Norm](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Norm) | Label-only comment; no adequate descriptive definition. | Description | DUL-C034 |
| [Object](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object) | A physical, social, or mental object or substance, understood as spatially located and participating in events. | Entity | DUL-C035 |
| [ObjectAggregate](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#ObjectAggregate) | An aggregate of distributed objects belonging to one collection; the commentary cautions that the shared-collection condition is not captured by an OWL equivalence. | None asserted | DUL-C036 |
| [Organism](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Organism) | A physical object possessing biological characteristics, with reproduction presented as typical rather than universally mandatory. | BiologicalObject, PhysicalAgent | DUL-C037 |
| [Organization](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Organization) | A conventionally instituted, internally organized social agent that acts through agents occupying designated roles. | SocialAgent | DUL-C038 |
| [Parameter](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Parameter) | A concept that selects or constrains values represented by regions, including measurement conventions. | Concept | DUL-C039 |
| [Parthood](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Parthood) | A reified situation for a time-qualified part-to-whole relation; additional mereological behavior requires appropriate rules or chains. | TimeIndexedRelation | DUL-C040 |
| [Pattern](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Pattern) | An observed or proposed invariance whose concrete occurrence may be represented as a situation. | Relation | DUL-C041 |
| [Person](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Person) | An umbrella for ordinary talk of persons when physical and social personhood are not distinguished. | Agent | DUL-C042 |
| [Personification](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Personification) | A socially constructed agentive entity arising through a cultural interpretation of some other entity. | SocialAgent | DUL-C043 |
| [PhysicalAgent](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#PhysicalAgent) | A physical object able to conceptualize descriptions for planning action and able to act for a social agent. | Agent, PhysicalObject | DUL-C044 |
| [PhysicalArtifact](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#PhysicalArtifact) | A physical object interpreted through a plan, including intentional reuse without structural redesign. | PhysicalObject | DUL-C045 |
| [PhysicalAttribute](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#PhysicalAttribute) | A region representing a physical object's value along a physical dimension. | Region | DUL-C046 |
| [PhysicalBody](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#PhysicalBody) | A physical object considered without foregrounding any artifactual function, at a chosen level of physical organization. | PhysicalObject | DUL-C047 |
| [PhysicalObject](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#PhysicalObject) | An object occupying its own spatial region; associated mass is typical but epistemically qualified in the commentary. | Object | DUL-C048 |
| [PhysicalPlace](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#PhysicalPlace) | A physical object whose location is intrinsic to how it is identified. | PhysicalObject | DUL-C049 |
| [Place](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Place) | A location dependent on social or cognitive identification, contextual entities, events, or signs rather than solely a dimensional region. | SocialObject | DUL-C050 |
| [Plan](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Plan) | A description specifying a goal to be achieved through its execution. | Description | DUL-C051 |
| [PlanExecution](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#PlanExecution) | A situation proactively satisfying a plan, with subplan executions treated as proper parts. | Situation | DUL-C052 |
| [Process](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Process) | A provisional event category emphasizing evolution or weak dependence on agents, tasks, and plans. | Event | DUL-C053 |
| [Project](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Project) | A plan organizing multiple roles and tasks around a structured set of subgoals and an overall goal. | Plan | DUL-C054 |
| [Quality](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality) | A dependent aspect of an individual entity, distinguished from the region used to encode its value. | Entity | DUL-C055 |
| [Region](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region) | A portion of a dimensional space usable as an entity's quality value, distinct from an ordinary datatype literal. | Abstract | DUL-C056 |
| [Relation](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Relation) | A socially situated description of a relation-like arrangement whose argument positions can be represented by concepts. | Description | DUL-C057 |
| [Right](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Right) | A legally supported entitlement of an agent to obtain something from another under stated conditions. | Description | DUL-C058 |
| [Role](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Role) | A concept used to classify objects. | Concept | DUL-C059 |
| [Set](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Set) | No prose comment in selected root. | FormalEntity | DUL-C060 |
| [Situation](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation) | A description-framed view of entities that can represent a relational context or reified multi-argument relation. | Entity | DUL-C061 |
| [SocialAgent](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#SocialAgent) | An agent whose socially communicated existence and capacity for action depend on physical agents acting for it. | Agent, SocialObject | DUL-C062 |
| [SocialObject](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#SocialObject) | An object constituted through communication and expressed through information, rather than existing independently of social communication. | Object | DUL-C063 |
| [SocialObjectAttribute](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#SocialObjectAttribute) | A dimensional region used to characterize a social object, such as a judgment or statistical value. | Region | DUL-C064 |
| [SocialPerson](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#SocialPerson) | A social agent depending on a particular natural person for action, without requiring identical lifetimes. | Person, SocialAgent | DUL-C065 |
| [SocialRelation](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#SocialRelation) | Label-only comment; no adequate descriptive definition. | Relation | DUL-C066 |
| [SpaceRegion](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#SpaceRegion) | A region in a specified spatial dimensional system used for locating entities rather than representing nonspatial characteristics. | Region | DUL-C067 |
| [SpatioTemporalRegion](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#SpatioTemporalRegion) | No prose comment in selected root. | Region | DUL-C068 |
| [Substance](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Substance) | A physical body whose boundaries need not be intentionally specified by a design. | PhysicalBody | DUL-C069 |
| [Task](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Task) | An event type specifying an action to perform; its defining plan may differ from the plan chosen to execute it. | EventType | DUL-C070 |
| [Theory](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Theory) | A description representing assumptions for explaining or characterizing a subject, including scientific and everyday theories. | Description | DUL-C071 |
| [TimeIndexedRelation](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#TimeIndexedRelation) | A situation adding a time argument to the context of a binary relation. | Situation | DUL-C072 |
| [TimeInterval](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#TimeInterval) | A region of a dimensional system used to represent temporal extent. | Region | DUL-C073 |
| [Transition](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Transition) | A situation coordinating before-and-after situations, an event, a process, objects, and temporal intervals to describe change. | Situation | DUL-C074 |
| [TypeCollection](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#TypeCollection) | A collection representing the maximal extension of a named type, distinct from a concept's intensional role. | Collection | DUL-C075 |
| [UnitOfMeasure](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#UnitOfMeasure) | A parameter applied to regions to support measurement through datatype values. | Parameter | DUL-C076 |
| [Workflow](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Workflow) | A plan structuring roles and tasks, typically for an organization's work. | Plan | DUL-C077 |
| [WorkflowExecution](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#WorkflowExecution) | No prose comment in selected root. | Situation | DUL-C078 |

## Interpretation and limits

A complete glossary accounts for every class and every missing definition; it does not fill source gaps or prove semantic adequacy. `WorkflowExecution` has an explicit equivalent-class expression despite its absent prose comment. The nine missing annotations and two insufficient label-restatement comments remain distinct from source licensing or ontology consistency.

The selected root is not an established 2016 release. IOLite definitions belong to #271. Imported patterns, paper diagrams and conceptual vocabulary are separate populations. No reasoning or independent expert validation is claimed by this catalog.

Recheck with `python tools/check_dul_class_catalog.py --source PATH_TO_PRIVATE_DUL_TURTLE`. Without `--source`, the checker validates only public-record integrity; it cannot verify original bytes.
