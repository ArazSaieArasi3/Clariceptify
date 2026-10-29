# LMM2008: selected class glossary

Issue #270. All explicitly declared local named owl:Class IRIs in selected documents. External redeclarations are retained in censuses, not relabeled local. No inference.

Every definition below is a short reviewer paraphrase of the source comment. A comment may be incomplete, informal or ambiguous; logical constraints are recorded separately. MISSING means no source definition comment was found in the selected bytes, not that no definition exists anywhere.

| Module | Local classes | External redeclarations | Source version |
|---|---|---|---|
| LMM_L1 | 8 | 11 | ["1.8\n1.2 \n- contains fine-tuning of cross-context relations. Now, the formalization pathway goes from expression to meaning to reference to formal entity to formal expression.\n1.3 \n- has all elements with English labels. Moreover, I added the relatedMeaning property, which allows to query across all object properties that have a Meaning in both domain and range.\n1.4 \n- has a new relation: hasInterpretant, based on Peirce's semiotics, which is applied between any two Expression(s), where the second provides an interpretive context for the first.\n1.5 \n- fixes a bug in the domain and range of isContextOf, now both generalized to dul:Entity, and consequently, Context is equivalently defined as anything that isContextOf some dul:Entity; some comments have also been edited.\n1.6 \n- added equivalentClass axiom between lmm:Meaning and dul:SocialObject (simplifies applications).\n1.7 \n- aligned all locally defined object properties to dul:associatedWith.\n1.8\n- simplified several restrictions in the semiotic pattern core, for improving reasoning performance."] |

Source: http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl. SHA256 `955518d71f6feb09f9a31a226d329e9f6fe1cdc4d91b735b15cf28d45e5802fb`. All named declarations and outgoing constraints: [LMM_L1 census](LMM_L1-census.json).

| LMM_L2 | 21 | 20 | ['1.2\n1.1\n- Edited annotations\n- Added class: Gloss\n- Added property: hasCoInterpretant\n1.2\n- Simplified several restrictions (in non-lossy way) in order to reduce complexity of reasoning'] |

Source: http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl. SHA256 `512f7a2c877a446144415c96c2da531eb51a9843fa82719d9a629466046dc240`. All named declarations and outgoing constraints: [LMM_L2 census](LMM_L2-census.json).

| Class IRI | Definition / missing state | Named superclasses | Notes |
|---|---|---|---|
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#CoText | Textual surroundings selected by a construction rule. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Collection; http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl#LinguisticObject; http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Context |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#ConstructionRule | A specification for producing an entity. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Context | Something providing a setting for another entity. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Entity |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Expression | Information conveying meaning or denoting a referent. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#InformationObject |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#KnowledgeCommunity | Agents sharing a conceptual paradigm. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Community; http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Context |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Meaning | A conceptualization connected to expression or interpretation. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#SocialObject |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Paradigm | The conceptual setting of an expressed meaning. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description; http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Context |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Reference | An entity denoted or interpreted within the semiotic model. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Entity |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#AnalyticFeature | A role identifying evidence used during analysis. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Role |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#AssociativeContext | Textual surroundings selected through corpus associations. | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#CoText | The comment starts by calling this an associative rule although its declared superclass is CoText; annotation wording needs paper/artifact reconciliation in #260. |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#AssociativeRule | **MISSING SOURCE DEFINITION** | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#ConstructionRule | The superclass is recorded separately; it does not supply an author definition. No definition was invented from the class name. |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#ConceptExpression | A term conveying meaning and denoting a collection. | http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl#Term; http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Expression |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#ConceptReference | The collection of individuals sharing a named type. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#TypeCollection; http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#MultipleReference |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#ContextualExpression | A term whose referent depends on deixis or anaphora. | http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl#Term; http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Expression |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#ContextualReference | An individual referent identified through contextual expression. | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#IndividualReference |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#EnumeratedExpression | A contextual expression listing a plural referent. | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#ContextualExpression | The comment calls this an AnaphoricExpression while its asserted superclass is ContextualExpression. Preserve the source alias discrepancy; see #260/#274. |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#ExperimentalSetting | A plan specifying an experiment and its analytical roles. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Plan |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#ExtensionalReference | A collection identified through an explicit or contextual enumeration. | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#MultipleReference |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#Gloss | Text explaining a lexical item informally. | http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl#Text |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#IndividualReference | A referent instantiated under a concept. | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Reference |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#LSARule | **MISSING SOURCE DEFINITION** | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#AssociativeRule | The superclass is recorded separately; it does not supply an author definition. No definition was invented from the class name. |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#LatentContext | **MISSING SOURCE DEFINITION** | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#AssociativeContext | The superclass is recorded separately; it does not supply an author definition. No definition was invented from the class name. |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#MultipleReference | A collection serving as a semiotic referent. | http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Collection; http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Reference |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#Name | A proper noun identifying an individual referent. | http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl#Term; http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#Expression |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#NamedEntity | An individual referent identified through a name. | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#IndividualReference |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#PolyrhematicConceptExpression | A multiword concept expression with a potential head word. | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#ConceptExpression |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#SimpleConceptExpression | A simple expression identifying a class-related referent. | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#ConceptExpression | The comment uses ClassReference as a denotation target while its asserted denotes restriction uses ConceptReference. The source alias correspondence remains unestablished; see deep paper review #260 and technical follow-up #274. |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#SyntacticContext | Textual surroundings determined by syntactic structure. | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#CoText |  |
| http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl#SyntacticRule | **MISSING SOURCE DEFINITION** | http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#ConstructionRule | The superclass is recorded separately; it does not supply an author definition. No definition was invented from the class name. |

Full labels, definition/annotation hashes, exact source IRIs/predicates, deprecated status, equivalence counts and constraint pointers are retained in [classes.yaml](classes.yaml).

Local classes: 29; source comment candidates: 25; missing source definitions: 4.

Imported glossary: COMPLETE_IRI_ACCOUNTING_WITH_EXPLICIT_DEFINITION_GAPS. All 154 distinct IRIs are accounted for: 29 LMM, 46 IOLite, 78 DUL and builtin owl:Thing. Sixteen source classes lack comments and two DUL comments only repeat labels. Coverage is not complete definition adequacy, historical equivalence or semantic acceptance.

Reasoning: NOT_EXECUTED. Historical paper fidelity: NOT_ESTABLISHED. Model change: NONE.
