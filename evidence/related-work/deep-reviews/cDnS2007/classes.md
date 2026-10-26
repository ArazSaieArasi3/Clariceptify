# cDnS2007: selected class glossary

Issue #269. All explicitly declared local named owl:Class IRIs in selected documents. External redeclarations are retained in censuses, not relabeled local. No inference.

Every definition below is a short reviewer paraphrase of the source comment. A comment may be incomplete, informal or ambiguous; logical constraints are recorded separately. MISSING means no source definition comment was found in the selected bytes, not that no definition exists anywhere.

| Module | Local classes | External redeclarations | Source version |
|---|---|---|---|
| cDnS | 12 | 0 | ['1.1', 'Created by Aldo Gangemi\nVersion 1.1 aligns cDnS with the axiomatization in the article JAAMAS 2008.'] |

Source: http://www.ontologydesignpatterns.org/ont/cdns/cDnS.owl. SHA256 `f0d7b6c795fe9e1a699eda2d80089371336869e981e938648edd5db88358658a`. All named declarations and outgoing constraints: [cDnS census](artifact-census.json).

| Class IRI | Definition / missing state | Named superclasses | Notes |
|---|---|---|---|
| http://www.loa-cnr.it/ontologies/cDnS.owl#Entity | Anything admitted within the selected domain. | http://www.w3.org/2002/07/owl#Thing |  |
| http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity | A primitive used to construct social reality. | http://www.loa-cnr.it/ontologies/cDnS.owl#Entity |  |
| http://www.loa-cnr.it/ontologies/cDnS.owl#NonSchematicEntity | An entity outside the schematic category; source wording is ambiguous. | http://www.loa-cnr.it/ontologies/cDnS.owl#Entity | The comment negates schematic membership but its following explanation can be read inconsistently. Use the declared disjointness as a separate formal observation; do not silently repair the source. |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Description | A communicable conceptualization dependent on social agents. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity |  |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Situation | A relational context viewed through a description. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity |  |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Concept | A category defined within one description. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity |  |
| http://www.loa-cnr.it/ontologies/cDnS.owl#SocialAgent | A socially constituted bearer of shared conceptualizations. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity |  |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Collection | A group whose membership has shared criteria. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity |  |
| http://www.loa-cnr.it/ontologies/cDnS.owl#InformationObject | Historically situated information independent of a particular physical carrier. | http://www.loa-cnr.it/ontologies/cDnS.owl#SchematicEntity |  |
| http://www.loa-cnr.it/ontologies/cDnS.owl#GroundEntity | An entity contextualized through description. | http://www.loa-cnr.it/ontologies/cDnS.owl#Entity |  |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Bundle | Multiple descriptions combined through common satisfaction or collection characterization. | http://www.loa-cnr.it/ontologies/cDnS.owl#Description |  |
| http://www.loa-cnr.it/ontologies/cDnS.owl#Configuration | A collection of parts unified by a description. | http://www.loa-cnr.it/ontologies/cDnS.owl#Collection |  |

Full labels, definition/annotation hashes, exact source IRIs/predicates, deprecated status, equivalence counts and constraint pointers are retained in [classes.yaml](classes.yaml).

Local classes: 12; source comment candidates: 12; missing source definitions: 0.

Imported glossary: NO_DECLARED_IMPORTS. No declared imports in this one retained core; related unacquired modules remain outside its scope.

Reasoning: NOT_EXECUTED. Historical paper fidelity: NOT_ESTABLISHED. Model change: NONE.
