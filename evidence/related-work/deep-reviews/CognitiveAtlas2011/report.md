# The Cognitive Atlas: Toward a Knowledge Foundation for Cognitive Neuroscience

Work: `CognitiveAtlas2011` | Issue: #79 | State: `REVIEW_COMPLETE`

Reviewed version: Frontiers in Neuroinformatics5:17, 6 September 2011, complete 11-page publisher PDF. Input: `CognitiveAtlas-2011.pdf`, 11 PDF pages, SHA256 `c69f953e6bde21e40e9408124b2ef1c2aa53ff5131bdb1dac8dca4adac92fed4`.

The structured `review.yaml` is the evidence authority; this report is derived. This is an AI-assisted critical review, not independent expert acceptance. Clariceptify is unchanged; later use requires an owner decision.

## Identity and reading coverage

All 11 article/PDF pages coincide. Received 31 March, accepted 17 August and published 6 September 2011 are separate dates. The paper describes the contemporary MySQL-backed knowledge base and generated OWL. Retained 2015 export snapshot, formal header 0.3, original paper-linked repository current commit, 2017 discussion-only repository and current website are not asserted equivalent to the 2011 paper. All quantities below identify their source/time/population.

Complete ontology-bearing paper catalog: mental constructs/tasks/conditions/indicators/contrasts, lexical/collaborative/provenance distinctions, reused vocabularies, every figure category/field/relation/example, scope exclusions, applications and implementation boundaries. The paper has no numbered formal equations, no tables and no appendices; 18 commitment groups are attributed prose/diagram analyses, not machine axioms. Paper does not enumerate all >800/904 vocabulary entries, so no complete released-class glossary is inferred. No eight-item cap applies to this paper catalog.

| Paper unit | Coverage | Evidence |
|---|---|---|
| Title/authors/abstract/editor-reviewer notes, dates and DOI | REVIEWED | E01 |
| Introduction and What is the problem? | REVIEWED | E02 |
| Ambiguous terminology | REVIEWED | E02 |
| Tasks versus constructs | REVIEWED | E03 |
| Toward an ontology for cognition, both pages | REVIEWED | E04 |
| The Cognitive Atlas and process/task guiding principle | REVIEWED | E05 |
| Structure of knowledge base and Mental concepts | REVIEWED | E05 |
| Mental tasks | REVIEWED | E06 |
| Experimental conditions | REVIEWED | E06 |
| Indicators | REVIEWED | E06 |
| Contrasts, including p.5 continuation | REVIEWED | E06 |
| Figure 1 complete concept schema | REVIEWED | E07 |
| Figure 2 complete task schema | REVIEWED | E08 |
| Relations introduction and Basic ontological relations | REVIEWED | E09 |
| Relations between processes and tasks | REVIEWED | E10 |
| Relations among tasks | REVIEWED | E10 |
| Literature relations | REVIEWED | E11 |
| Relations to observed data | REVIEWED | E11 |
| Technical infrastructure, all paragraphs and paper GitHub link | REVIEWED | E12 |
| Benefits/challenges of collaborative knowledge building, opening across pp.6-7 | REVIEWED | E13 |
| Capturing and resolving disagreement | REVIEWED | E13 |
| Curation | REVIEWED | E13 |
| Utility introduction and Clearer vocabulary | REVIEWED | E14 |
| Figure 3 disambiguation screenshot | REVIEWED | E14 |
| Improved query expansion across pp.7-8 | REVIEWED | E15 |
| Metadata annotation/meta-analysis | REVIEWED | E16 |
| Theory testing | REVIEWED | E16 |
| Translational mental health research | REVIEWED | E17 |
| Figure 4 complete five-layer illustration/caption/callout | REVIEWED | E17 |
| Present status/future plans across pp.9-10 | REVIEWED | E18 |
| Conclusion and Acknowledgments | REVIEWED | E19 |
| All 39 references and conflict/rights notices | REVIEWED | E01, E19 |
| All 10 numbered footnotes and cross-reference mismatch: CogPO points to footnote 2 rather than 3 | REVIEWED | E02, E04, E05, E12, E13, E18 |

## Common review dimensions

### D1_identity_coverage

All 11 PDF/article pages, four figures including every schema field and the 13-node five-layer empirical illustration, 10 numbered footnotes and 39 references were read and visually checked. No tables, appendices or numbered equations occur. Nine authors/date/DOI match publisher metadata. 2011 paper, 2015 export header 0.3, paper-linked repository and current website remain version-distinct. [REVIEWER_INTERPRETATION; E01, E07, E08, E14, E17, E19, M01, R01, R03, R04]

### D2_problem_contribution

The paper addresses ambiguous cognitive terminology and the task/construct conflation that undermines cross-study integration. It contributes a collaborative knowledge base separating mental constructs from experiments and contrast-specific measurement claims, with discussion/sense management and standard access. It does not claim a complete cognitive theory or validate all mental-to-brain mappings. [REVIEWER_INTERPRETATION; E02, E03, E04, E05, E06, E10, E13, E14, E18]

### D3_method

Manual source analysis and three-author curation seed >800 terms; schema/interaction design, native relational implementation and feedback from a small investigator group support iterative development. The paper cites interaction-design work and describes collaborative curation but no named ontology-engineering protocol, systematic search/inclusion method, quantified usability/expert agreement study or reproducible requirements-to-test matrix. [REVIEWER_INTERPRETATION; E05, E12, E13, E18, E19]

### D4_requirements

Needs include precise sense selection, distinguishing a task from a contrast/construct, recording relations/disagreement/citations and linking external data. Source examples and reviewer adverse cases below retain the intended use. There is no numbered CQ suite or complete operational acceptance test set; reviewer reconstructed query needs are not attributed as author-tested CQs. [REVIEWER_INTERPRETATION; E02, E03, E06, E10, E11, E14, E15, E16, E18]

### D5_concepts

Catalog covers latent construct versus physical realization, optional process/representation distinction, task/condition/indicator/contrast, task collections, sense/term/definition and contributor/curator/discussion/citation roles. Every named diagram vocabulary and example is included. These are paper concepts, not a complete list of all 904 2011 terms or selected OWL class IRIs. [REVIEWER_INTERPRETATION; E05, E06, E07, E08, E11, E13, E14, E17, E18]

### D6_relations_formalization

Selected is-a/part-of/transformation-of/preceded-by, contrast-bound measured-by, task descent and citation/lexical/collaboration links are preserved with scope. Spatial and participation/agent relations are expressly excluded. No numbered DL/FOL axioms, property characteristics, cardinalities, signed arithmetic implementation or exact class/individual semantics are supplied. Figure captions distinguish empirical associations from formal ontological relations. [REVIEWER_INTERPRETATION; E06, E07, E08, E09, E10, E11, E17]

### D7_grounding

Paper reuses SKOS, CogPO and selected OBO RO relations plus Dublin Core/SIOC/SWAN/CiTO/NEMO metadata or application vocabularies. It does not establish BFO/DOLCE/UFO upper grounding or an exact imported edition. Later export includes BFO1.1/CogPO2011 namespace hints but no declared imports. Latent constructs, neural realizations, agency participation and temporal identity remain delimited rather than silently completed. [REVIEWER_INTERPRETATION; E05, E07, E08, E09, E11, E12, R02, R03]

### D8_artifact_correspondence

Exact paper author GitHub link was followed, current public commit/tree checked and generator bytes pinned. Official retained 13-file export and separate two-file discussion repository are independently identified; selected source blobs match API hashes. Header metadata parse succeeded, while generation, pickle loading, complete class glossary, imports, reasoning and SPARQL were not executed. Source license notices and historical correspondence remain separate. [REVIEWER_INTERPRETATION; E12, E18, R01, R02, R03, R04]

### D9_evaluation

Evidence is an implemented prototype with schema figures and sense screenshot, author-reported 904 entries/795 definitions/<900 relations, external prior studies and proposed utility. Most initial definitions are expressly insufficient; no controlled precision/recall, mapping accuracy, user agreement or reasoning benchmark is reported. Eight-task prior work, six-reference illustration and literature Jaccard association are not fresh CA evaluation populations. [REVIEWER_INTERPRETATION; E07, E08, E14, E15, E16, E17, E18, E19]

### D10_critical_synthesis

Strong overlap with Clariceptify concerns theory-bound conceptual claims, terms/senses, contributors, rationale/disagreement and evidence links. Limits include optional undeclared formal semantics, missing measured-claim context, citation polarity implementation gap, incomplete definitions, coarse tasks and later export/type differences. Retain these as comparison/test proposals in #241/#254/#126; no automatic alignment, new novelty claim or model/release change follows. [REVIEWER_INTERPRETATION; E03, E05, E10, E11, E13, E14, E16, E18, R02, R03]

## Conceptual catalog

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| C001 / Mental concept / latent construct | A theoretically postulated unobservable construct; the knowledge-base entity denotes the construct rather than its physical brain instantiation. Not every concept is required to be categorized as a process or representation. | REVIEWER_INTERPRETATION; E05 |
| C002 / Mental process | A proposed kind of mental concept operating on representations; paper permits non-representational cognition and does not mandate this taxonomy for every concept. | REVIEWER_INTERPRETATION; E05 |
| C003 / Mental representation | A possible mental entity standing in relation to a physical arrangement or abstract concept, including another mental entity. Its existence is not mandatory for all accepted theories. | REVIEWER_INTERPRETATION; E05 |
| C004 / Physical instantiation / brain tissue | Realization of a mental construct is distinguished from what the knowledge-base record refers to. Paper supplies no complete realization/dependence axiom. | REVIEWER_INTERPRETATION; E05 |
| C005 / Mental task / psychological task | A prescribed activity to engage/manipulate mental function for investigation, not identical to the latent process being studied; overt response is optional. | REVIEWER_INTERPRETATION; E05, E06 |
| C006 / Experimental condition | Subset of an experiment defining a manipulation, including categorical or parametric conditions. Reuses CogPO condition schema. | REVIEWER_INTERPRETATION; E06 |
| C007 / Indicator | A recorded quantitative or qualitative analysis variable, including response time/accuracy and physiological measurements. The original implementation emphasizes behavioral indicators. | REVIEWER_INTERPRETATION; E06 |
| C008 / Contrast | A function over experimental conditions and their indicators; may be one condition, a baseline comparison or a linear/nonlinear combination. The process-measurement claim attaches here rather than directly to the task label. | REVIEWER_INTERPRETATION; E06, E10 |
| C009 / Task collection / battery | Collection of related tasks, illustrated by CNP Memory Battery and SWAN collection reuse; distinct from a task subtype or contrast. | REVIEWER_INTERPRETATION; E08 |
| C010 / Concept definition | Editable initial definition attached to a term; source explicitly acknowledges most 2011 definitions would be insufficient to experts. Text presence is not logical sufficiency. | REVIEWER_INTERPRETATION; E07, E18 |
| C011 / Concept sense | A separate meaning of a term created when conceptual disagreement is irreconcilable; has its own page and task relationships. | REVIEWER_INTERPRETATION; E14 |
| C012 / Disambiguation page | Routes an ambiguous original term to distinct sense pages rather than treating them as equivalent. Figure 3 gives cognitive and temperament behavioral-inhibition senses. | REVIEWER_INTERPRETATION; E14 |
| C013 / Synonym / alternate label | Different expressions considered to refer to the same process while retaining original terms. Lexical synonymy is not by itself owl:equivalentClass or sameAs. | REVIEWER_INTERPRETATION; E02, E14 |
| C014 / Term / label / title | Surface expression used to identify a mental concept/task; multiple meanings or multiple names motivate explicit concept/term separation. | REVIEWER_INTERPRETATION; E02, E07, E14 |
| C015 / Assertion / theoretical claim | Relations express theoretical commitments linking concepts or contrasts, which can be discussed and cited. A relation statement is not automatically an uncontested scientific fact. | REVIEWER_INTERPRETATION; E09, E10, E11, E13 |
| C016 / Discussion / forum | Integrated discussion for concepts and relations keeps disagreements/history available beside editable content. It is not the mental process being described. | REVIEWER_INTERPRETATION; E07, E13 |
| C017 / Literature citation / bibliography | Reference metadata associated with an entity or relation. The implemented informative-citation link is weaker than evidential support or refutation. | REVIEWER_INTERPRETATION; E07, E11 |
| C018 / Contributor / curator | People contribute and resolve disputes; three named authors curate the initial vocabulary and core/volunteer curators act as needed. No formal agent/role ontology or measured consensus outcome is given. | REVIEWER_INTERPRETATION; E05, E13 |
| C019 / Native relational database / generated OWL | Knowledge is stored in MySQL and transformed to OWL; export may omit collaboration/provenance information and is not the semantic authority for all native content. | REVIEWER_INTERPRETATION; E12, R02 |
| C020 / Bipartite process-task organization | Separate linked ontologies motivate measurement links; within-layer concept and task relations also exist, so the entire graph is not claimed globally bipartite. | REVIEWER_INTERPRETATION; E05, E09, E10 |
| C021 / Task phylogeny / adaptation / variant | Historical/conceptual descent is distinguished from small variations; proposed distinction depends on whether results can be combined in meta-analysis. No algorithmic threshold is supplied. | REVIEWER_INTERPRETATION; E10 |
| C022 / Empirical association / observed data | External data links and literature co-occurrence connect levels of knowledge. They do not establish causality, identity or a unique biological realization. | REVIEWER_INTERPRETATION; E11, E17 |
| C023 / Evidence-based curation / consensus | Community views are elicited but curation should consider evidence rather than popular vote alone. No formal decision procedure, voting threshold or agreement metric is supplied. | REVIEWER_INTERPRETATION; E13 |
| C024 / Fork / merge | Collaborative operations used when discussion cannot reconcile differences; detailed identifier migration, link redistribution and merge rules remain unspecified. | REVIEWER_INTERPRETATION; E13, E14 |
| C025 / Polysemy / synonymy | One label with multiple meanings versus multiple labels for similar content; query expansion must preserve the intended sense. | REVIEWER_INTERPRETATION; E02, E14, E15 |
| C026 / Construct validity | Whether a contrast/manipulation measures the intended latent construct; disputed Stroop/N-back examples show that naming a task after a process is insufficient. | REVIEWER_INTERPRETATION; E03, E06 |
| C027 / Meta-analysis / commensurability | Combining empirical results requires compatible tasks/metadata. The paper uses this as a task-identity criterion without defining a reproducible test. | REVIEWER_INTERPRETATION; E10, E16 |
| C028 / Theory / covariance-structure comparison | Different cognitive theories could predict different task covariance structures; this is explicitly future functionality, not a completed CA experiment. | REVIEWER_INTERPRETATION; E16 |
| C029 / Forward / reverse inference maps | External NeuroSynth mappings are reported for concept terms; they are linked external products, not inferential validation of every CA relation. | REVIEWER_INTERPRETATION; E18 |
| C030 / Jaccard association | Figure 4 edge width represents PubMed co-occurrence strength described as a Jaccard coefficient. No counted search sets, date, query table or reproducible edge-weight calculation is supplied. | REVIEWER_INTERPRETATION; E17 |
| C031 / Cognitive scope | Cognition is used broadly to include emotion and motivation, without claiming exhaustive coverage of all possible mental entities. | REVIEWER_INTERPRETATION; E02 |
| C032 / Dimensions / symptoms / syndromes | Translational research motivation connects dimensional cognition to psychiatric labels. This is an illustrative research framework, not a clinical classifier or validated intervention. | REVIEWER_INTERPRETATION; E17 |
| C033 / Personalization / mining / integration | Proposed tracking/recommendations, literature-mined candidate relations and broader external database links; separate future plans from already-reported integrations. | REVIEWER_INTERPRETATION; E18 |
| C034 / skos:Concept | Paper mental-concept modeling target; later exporter rewrites SKOS resources to OWL classes, requiring a separate level-of-representation check. | REVIEWER_INTERPRETATION; E05, E07, R02 |
| C035 / SKOS labels/definition/scheme | prefLabel, altLabel, definition and inScheme provide lexical and organization metadata; not sufficient mental-process identity axioms. | REVIEWER_INTERPRETATION; E07, E08 |
| C036 / Dublin Core metadata | Figure fields reuse dc:identifier, dc:Title, dc:Contributor and dc:Date exactly as printed, including capitalization. RDF namespace/term variants need technical reconciliation. | REVIEWER_INTERPRETATION; E07, E08 |
| C037 / SIOC Forum | Referenced schema for discussion content; no complete forum/argument ontology is presented. | REVIEWER_INTERPRETATION; E07, E08 |
| C038 / SWAN Citation Ontology / citations:Citation | Diagram bibliography reference, distinct from prose CiTO citation typing. Paper does not establish their exact equivalence. | REVIEWER_INTERPRETATION; E07, E08, E11 |
| C039 / SWAN Collections Ontology / collections:Collection | External collection category for task battery. | REVIEWER_INTERPRETATION; E08 |
| C040 / CogPO task category | Prose names Behavioral Experimental Paradigm; diagram prints cogpo:BehavioralExperiment. Exact ontology IRI/edition correspondence must be checked separately. | REVIEWER_INTERPRETATION; E06, E08 |
| C041 / CogPO condition category | Behavioral Experimental Paradigm Condition in prose, diagram cogpo:BehavioralExperimentParadigmCondition; source strings are preserved without inventing an equivalence. | REVIEWER_INTERPRETATION; E06, E08 |
| C042 / CogPO contrast category | Behavioral Experimental Paradigm Contrast in prose, diagram cogpo:BehavioralExperimentParadigmContrast. | REVIEWER_INTERPRETATION; E06, E08 |
| C043 / NEMO / nemo:ERP_activity | Diagram reuse relating an electrophysiological indicator to an external vocabulary. No complete NEMO import or definition is supplied by the article. | REVIEWER_INTERPRETATION; E08 |
| C044 / OBO Relational Ontology | Conceptual source of selected basic relations, with spatial and participation relations explicitly excluded. This is not proof of adopting BFO or any exact upper-ontology edition. | REVIEWER_INTERPRETATION; E09 |
| C045 / CiTO / citesForInformation | Citation-typing vocabulary; only informative citation relation is reported implemented, despite richer support/refutation possibilities. | REVIEWER_INTERPRETATION; E11 |
| C046 / Gene Ontology | Motivating analogy and possible external functional annotations/integration; GO's successful use is not a CA evaluation result. | REVIEWER_INTERPRETATION; E04, E11, E18 |
| C047 / MeSH | Historical biomedical search vocabulary criticized for coarse/outdated/mixed cognitive categories and poor route expansion. Not a controlled contemporary retrieval benchmark. | REVIEWER_INTERPRETATION; E04, E15 |
| C048 / Foundational Model of Anatomy / Brainmap | External brain-structure/data resources; their name or reference is not CA upper-foundation grounding. | REVIEWER_INTERPRETATION; E11 |
| C049 / ACT-R / SOAR / non-representational theories | Background theory alternatives motivating broad coverage and optional representation commitments; not imported CA modules. | REVIEWER_INTERPRETATION; E04, E05 |
| C050 / RDF / SPARQL / OWL export | Interoperability mechanisms described in 2011; current availability and actual generation/query tests are not established by paper description alone. | REVIEWER_INTERPRETATION; E12 |
| C051 / PubMed / Entrez | Citation and historical literature-association service; no 2011 searches were rerun here. | REVIEWER_INTERPRETATION; E02, E11, E12, E15, E17 |
| C052 / PubAtlas / PubBrain / PhenoWiki | Author-reported integration for associations, brain atlas mapping and quantitative annotations; no fresh integration test here. | REVIEWER_INTERPRETATION; E18 |
| C053 / NeuroSynth / SumsDB / NeuroLex | External inference/data/lexicon resources; distinguish reported existing maps from proposed direct links and future lexicon inclusion. | REVIEWER_INTERPRETATION; E18 |
| C054 / Working memory: maintenance / manipulation / temporal | Three source senses illustrated by delayed response, letter-number sequencing and radial-arm-maze paradigms; not declared equivalent. | REVIEWER_INTERPRETATION; E02 |
| C055 / Working memory / short-term memory / active maintenance | Terminology overlap is qualified by sense; not an unconditional identity across every theory or export version. | REVIEWER_INTERPRETATION; E02, E07 |
| C056 / Sternberg item-recognition task | High/low load contrasts may concern working memory while match/mismatch contrasts need not; one task can support different theoretical interpretations. | REVIEWER_INTERPRETATION; E03 |
| C057 / Color-word Stroop task / Stroop effect | Congruent, incongruent and neutral conditions with signed contrasts. Labeling it an inhibition task is disputed; measured-by link is a theory-bound claim. | REVIEWER_INTERPRETATION; E03, E06, E10 |
| C058 / N-back / continuous performance task | Figure 2 task descent and condition/contrast structure; N-back validity is disputed in the introduction. | REVIEWER_INTERPRETATION; E03, E08 |
| C059 / CNP Memory Battery | Named task collection in Figure 2, not a mental concept. | REVIEWER_INTERPRETATION; E08 |
| C060 / Cognitive control / response selection / task-set switching | Literature-based many-to-many task associations illustrate unstable construct terminology; not new class declarations counted from the article. | REVIEWER_INTERPRETATION; E03 |
| C061 / Declarative memory / explicit memory | Synonym illustration; memory retrieval, memory encoding and memory consolidation illustrate part/precedence/transformation relations. | REVIEWER_INTERPRETATION; E07, E09, E14 |
| C062 / Behavioral inhibition: cognitive / temperament | Figure 3 two senses; cognitive response inhibition concerns actions, temperament concerns shyness/social anxiety. Screenshot is a positive disambiguation example, not proof every ambiguous term is resolved. | REVIEWER_INTERPRETATION; E14 |
| C063 / Sublexical route / phonological assembly | Phrase-specific retrieval and possible related-term expansion; drug-administration route is an adverse expansion outcome. | REVIEWER_INTERPRETATION; E15 |
| C064 / Categorization / recognition memory | Single-process versus separate-process theories illustrate future covariance-model comparison. | REVIEWER_INTERPRETATION; E16 |
| C065 / Schizophrenia / Bipolar Disorder / ADHD | Three syndrome labels in Figure 4; illustrative association nodes, not diagnostic criteria. | REVIEWER_INTERPRETATION; E17 |
| C066 / WM Updating / Response Inhibition | Two cognitive nodes in Figure 4, distinct from syndrome or brain-system nodes. | REVIEWER_INTERPRETATION; E17 |
| C067 / DL PFC / VL PFC | Two neural-system nodes; callout links response inhibition and VLPFC activity through Stop Signal Task contrasts. | REVIEWER_INTERPRETATION; E17 |
| C068 / Dopamine D1 / Dopamine D2 / Adrenergic A2a | Three signaling-pathway labels printed in Figure 4; retain source categorization without inferring molecular identity/causality. | REVIEWER_INTERPRETATION; E17 |
| C069 / COMT / DRD2 / ADRA2a | Three gene labels exactly as printed in Figure 4; not converted into inferred genetic associations. | REVIEWER_INTERPRETATION; E17 |
| C070 / Stop Signal Task: stop versus go | Callout ties task contrast, response inhibition, VLPFC activity and six referenced reports; relation/provenance example only. | REVIEWER_INTERPRETATION; E17 |
| C071 / Response time / accuracy / fMRI activation map / ERP component amplitude | Four indicators in Figure 2. These are heterogeneous measurement products, not identical to the task or the latent construct. | REVIEWER_INTERPRETATION; E06, E08 |
| C072 / BrainMap / SumsDB / Neurosynth / OpenFMRI | Four named imaging database boxes in Figure 2, connected empirically rather than via a claimed formal class hierarchy. | REVIEWER_INTERPRETATION; E08 |
| C073 / is-a / relation | mental concept -> broader mental concept: Selected OBO relation, exemplified by declarative memory/memory. Does not establish an OWL class-versus-SKOS individual policy by itself. | REVIEWER_INTERPRETATION; E09 |
| C074 / part-of / relation | entity -> containing entity: Cognitive-part examples and task-collection membership occur. Different uses need typing and cannot all silently become one mereology. | REVIEWER_INTERPRETATION; E07, E08, E09 |
| C075 / transformation-of / relation | mental entity -> prior-form mental entity: Example consolidated versus encoded memory; no complete temporal transformation/identity theory is given. | REVIEWER_INTERPRETATION; E09 |
| C076 / preceded-by / relation | mental process -> earlier mental process: Memory consolidation preceded by encoding; source gives no explicit transitivity, irreflexivity or endpoint restrictions. | REVIEWER_INTERPRETATION; E09 |
| C077 / measured by / measured-by / relation | mental process or concept -> task contrast: A theoretical measurement claim about a particular contrast; never infer a task/construct identity or causal realization relation from this alone. | REVIEWER_INTERPRETATION; E06, E07, E08, E10 |
| C078 / descended-from / descended_from / relation | task -> antecedent task: Task adaptation/phylogeny, distinct from is-a; commensurability motivates task-versus-variant distinction. | REVIEWER_INTERPRETATION; E08, E10 |
| C079 / has_condition / relation | task -> experimental condition: Printed Figure 2 connector, without a complete property/cardinality axiom. | REVIEWER_INTERPRETATION; E08 |
| C080 / has_contrast / relation | task -> contrast: Printed Figure 2 connector; a task can support multiple contrasts. | REVIEWER_INTERPRETATION; E08 |
| C081 / includes_condition / relation | contrast -> participating condition: Figure 2 connector; it does not specify signed weights, arithmetic or indicator binding. | REVIEWER_INTERPRETATION; E08 |
| C082 / synonym / altLabel / relation | term or concept -> alternate expression: Retains original terms rather than automatic merging; equivalence strength requires an explicit semantics. | REVIEWER_INTERPRETATION; E14, E07 |
| C083 / citesForInformation / relation | entity or assertion -> citation: Only implemented literature relation reported; not automatically supports/refutes. | REVIEWER_INTERPRETATION; E11 |
| C084 / supports / refutes / relation | citation -> claim, intended evidential role: Described CiTO potential, not claimed implemented in the 2011 release. | REVIEWER_INTERPRETATION; E11 |
| C085 / has_participant / has_agent / relation | process -> continuant participant/agent: Deliberately excluded because latent-entity participation is unresolved. Do not count as implemented agency support. | REVIEWER_INTERPRETATION; E09 |
| C086 / spatial relations / relation | spatially located entities: Excluded from the selected OBO relation set; no spatial-location model is supplied. | REVIEWER_INTERPRETATION; E09 |
| C087 / identifier / Title / Contributor / Date / relation | record -> metadata value: Dublin Core-inspired fields printed in both schemas; actual namespace and term capitalization require checking. | REVIEWER_INTERPRETATION; E07, E08 |
| C088 / prefLabel / altLabel / definition / inScheme / relation | concept record -> label/definition/scheme: SKOS references printed in Figures1/2; textual definition and scheme membership are distinct from logical class definitions. | REVIEWER_INTERPRETATION; E07, E08 |
| C089 / discussion / bibliography / relation | entity or relation -> forum/citation: Collaborative/provenance links, distinct from psychological or biological relation types. | REVIEWER_INTERPRETATION; E07, E08, E11, E13 |
| C090 / empirical association / literature link strength / relation | cross-level entities -> associated entities: Figure 4 Jaccard-weighted literature associations, not formal inheritance or causal edges. | REVIEWER_INTERPRETATION; E17 |
| C091 / fork / merge / sense routing / relation | original concept page -> revised or separate sense pages: Knowledge-base revision operations; paper supplies no complete formal version/identity/migration rules. | REVIEWER_INTERPRETATION; E13, E14 |

## Relations and formal commitments

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| K01 / Task/construct separation | The schema separates latent mental concepts from prescribed tasks and uses contrast-level measurement links; it does not equate tasks with the processes they are named after. | REVIEWER_INTERPRETATION; E03, E05, E06, E10 |
| K02 / Theory-neutral optional subdivision | Representations/processes are possible mental-concept subclasses but not required; this accommodates non-representational theories. No mandatory covering axiom is printed. | REVIEWER_INTERPRETATION; E05 |
| K03 / SKOS and export representation levels | Paper models mental concepts with skos:Concept; later script rewrites source SKOS elements into owl:Class. Actual interpretation and identity require separate technical comparison. | REVIEWER_INTERPRETATION; E05, R02 |
| K04 / Prescribed task without overt behavior | A task can be an experimental stimulation without motor response; observable behavior is not a necessary condition for this task category. | REVIEWER_INTERPRETATION; E06 |
| K05 / Condition versus indicator versus contrast | Condition is manipulation context, indicator is recorded variable, contrast is a function of condition measurements. A contrast edge alone does not encode the numeric function. | REVIEWER_INTERPRETATION; E06, E08 |
| K06 / Stroop signed contrast examples | Source prose gives incongruent minus congruent and incongruent minus neutral as Stroop-effect contrasts. This is illustrative arithmetic, not numbered ontology axioms or independently computed scores. | REVIEWER_INTERPRETATION; E06 |
| K07 / N-back contrast sign retained | Figure 2 labels its example 0-back minus 2-back. Retain that orientation, rather than silently substituting 2-back minus 0-back; its relation to expected measurement polarity needs an explicit interpretation. | REVIEWER_INTERPRETATION; E08 |
| K08 / Basic relation selection and exclusion | is-a/part-of/transformation-of/preceded-by are adopted; spatial and process-participant/agent relations are excluded. Property characteristics are not stated as DL axioms. | REVIEWER_INTERPRETATION; E09 |
| K09 / Contrast-bound measured-by | Mental process is related to the contrast that is hypothesized to manipulate/measure it. The claim is theoretical and does not prove construct validity. | REVIEWER_INTERPRETATION; E10 |
| K10 / Task descent and commensurability | descended-from is historical/conceptual adaptation, not automatically subclassing. The source uses meta-analysis compatibility to distinguish derivation from minor variants without an operational criterion. | REVIEWER_INTERPRETATION; E10 |
| K11 / Informative citation implementation limit | Current cited implementation has one literature relation equivalent to citesForInformation; richer CiTO support/refutation is described, not implemented as reported. | REVIEWER_INTERPRETATION; E11 |
| K12 / Native store/export distinction | MySQL is the native store; OWL is generated for interoperability. No lossless semantic round-trip or complete export of discussion/conflict metadata is demonstrated. | REVIEWER_INTERPRETATION; E12, R02 |
| K13 / No empirical data storage | The paper repeatedly distinguishes storing knowledge/annotations from linking to external empirical datasets; do not claim internal patient, genetic or imaging data. | REVIEWER_INTERPRETATION; E11, E18 |
| K14 / Discussion and evidence-based curation | Concept/relation disagreements are exposed and curated with community evidence; consensus quality, traceable decisions and preservation of minority theories are not formally guaranteed. | REVIEWER_INTERPRETATION; E13 |
| K15 / Forked senses versus synonyms | Forking produces distinct sense pages with separate task relations; synonym designation retains terms. Neither operation automatically establishes OWL equivalence or identity. | REVIEWER_INTERPRETATION; E14 |
| K16 / Empirical cross-level association | Figure 4 edges reflect proposed empirical links and literature Jaccard association, not inheritance, causation or a biological mechanism proof. | REVIEWER_INTERPRETATION; E17 |
| K17 / 2011 status is author-reported population | Initial >800 curated terms differs from later 904 entries (708 constructs+196 tasks).795 definitions are explicitly often insufficient; fewer than 900 relation statements is not a relation-type count. | REVIEWER_INTERPRETATION; E05, E18 |
| K18 / Future utility boundary | Precision/recall improvement, richer meta-analysis, theory testing and translation are proposed uses; theory testing is explicitly unsupported at that time. No new controlled utility experiment is reported. | REVIEWER_INTERPRETATION; E15, E16, E17, E18 |

## Complete paper relation index

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| R01 / is-a | mental concept -> broader mental concept: Selected OBO relation, exemplified by declarative memory/memory. Does not establish an OWL class-versus-SKOS individual policy by itself. | REVIEWER_INTERPRETATION; E09 |
| R02 / part-of | entity -> containing entity: Cognitive-part examples and task-collection membership occur. Different uses need typing and cannot all silently become one mereology. | REVIEWER_INTERPRETATION; E07, E08, E09 |
| R03 / transformation-of | mental entity -> prior-form mental entity: Example consolidated versus encoded memory; no complete temporal transformation/identity theory is given. | REVIEWER_INTERPRETATION; E09 |
| R04 / preceded-by | mental process -> earlier mental process: Memory consolidation preceded by encoding; source gives no explicit transitivity, irreflexivity or endpoint restrictions. | REVIEWER_INTERPRETATION; E09 |
| R05 / measured by / measured-by | mental process or concept -> task contrast: A theoretical measurement claim about a particular contrast; never infer a task/construct identity or causal realization relation from this alone. | REVIEWER_INTERPRETATION; E06, E07, E08, E10 |
| R06 / descended-from / descended_from | task -> antecedent task: Task adaptation/phylogeny, distinct from is-a; commensurability motivates task-versus-variant distinction. | REVIEWER_INTERPRETATION; E08, E10 |
| R07 / has_condition | task -> experimental condition: Printed Figure 2 connector, without a complete property/cardinality axiom. | REVIEWER_INTERPRETATION; E08 |
| R08 / has_contrast | task -> contrast: Printed Figure 2 connector; a task can support multiple contrasts. | REVIEWER_INTERPRETATION; E08 |
| R09 / includes_condition | contrast -> participating condition: Figure 2 connector; it does not specify signed weights, arithmetic or indicator binding. | REVIEWER_INTERPRETATION; E08 |
| R10 / synonym / altLabel | term or concept -> alternate expression: Retains original terms rather than automatic merging; equivalence strength requires an explicit semantics. | REVIEWER_INTERPRETATION; E14, E07 |
| R11 / citesForInformation | entity or assertion -> citation: Only implemented literature relation reported; not automatically supports/refutes. | REVIEWER_INTERPRETATION; E11 |
| R12 / supports / refutes | citation -> claim, intended evidential role: Described CiTO potential, not claimed implemented in the 2011 release. | REVIEWER_INTERPRETATION; E11 |
| R13 / has_participant / has_agent | process -> continuant participant/agent: Deliberately excluded because latent-entity participation is unresolved. Do not count as implemented agency support. | REVIEWER_INTERPRETATION; E09 |
| R14 / spatial relations | spatially located entities: Excluded from the selected OBO relation set; no spatial-location model is supplied. | REVIEWER_INTERPRETATION; E09 |
| R15 / identifier / Title / Contributor / Date | record -> metadata value: Dublin Core-inspired fields printed in both schemas; actual namespace and term capitalization require checking. | REVIEWER_INTERPRETATION; E07, E08 |
| R16 / prefLabel / altLabel / definition / inScheme | concept record -> label/definition/scheme: SKOS references printed in Figures1/2; textual definition and scheme membership are distinct from logical class definitions. | REVIEWER_INTERPRETATION; E07, E08 |
| R17 / discussion / bibliography | entity or relation -> forum/citation: Collaborative/provenance links, distinct from psychological or biological relation types. | REVIEWER_INTERPRETATION; E07, E08, E11, E13 |
| R18 / empirical association / literature link strength | cross-level entities -> associated entities: Figure 4 Jaccard-weighted literature associations, not formal inheritance or causal edges. | REVIEWER_INTERPRETATION; E17 |
| R19 / fork / merge / sense routing | original concept page -> revised or separate sense pages: Knowledge-base revision operations; paper supplies no complete formal version/identity/migration rules. | REVIEWER_INTERPRETATION; E13, E14 |

## Requirements, examples and adverse cases

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| S01 / Working-memory polysemy | Maintenance, manipulation and temporal/spatial memory senses share a label but differ in intended construct/task context. A query over the label alone can mix evidence. | REVIEWER_INTERPRETATION; E02 |
| S02 / Synonym-aware maintenance retrieval | Short-term memory and active-maintenance terminology can inform retrieval for a specified sense, with relevance/noise tradeoffs preserved. | REVIEWER_INTERPRETATION; E02, E15 |
| S03 / Sternberg within-task contrast | High-versus-low load and probe-match-versus-mismatch contrasts in one task need not measure the same process. Do not attach all measurement claims directly to the task name. | REVIEWER_INTERPRETATION; E03 |
| S04 / Stroop inhibition dispute | Alternative accounts dispute active inhibition as the cause of the Stroop effect; citation and claimant context matter even if the task and contrast are agreed. | REVIEWER_INTERPRETATION; E03, E10 |
| S05 / N-back construct validity | A task commonly labeled working memory may have disputed construct validity; the generated ontology label is not empirical confirmation. | REVIEWER_INTERPRETATION; E03, E08 |
| S06 / Passive stimulation task | A movie-viewing imaging experiment can be a task without an overt motor response. Requiring an action output would exclude this intended case. | REVIEWER_INTERPRETATION; E06 |
| S07 / Signed Stroop difference | Incongruent-minus-congruent and incongruent-minus-neutral are distinct contrast functions, requiring conditions and indicators rather than one task-level link. | REVIEWER_INTERPRETATION; E06 |
| S08 / N-back sign reversal | Figure 2 source contrast is 0-back minus 2-back; reversing it changes the sign even if both link the same conditions. includes_condition edges alone do not encode weights or polarity. | REVIEWER_INTERPRETATION; E08 |
| S09 / Task adaptation versus variant | A descended-from task may require separate meta-analysis treatment if its outputs are not commensurate; same name or superficial structural similarity is insufficient. | REVIEWER_INTERPRETATION; E10 |
| S10 / Informative citation without support | A citation mentioning a claim can supply context or opposition rather than support. citesForInformation must not be promoted to an evidential-support relation. | REVIEWER_INTERPRETATION; E11 |
| S11 / Behavioral-inhibition sense split | Cognitive inhibition of actions and temperament/shyness senses occupy separate pages and measurement relations after disambiguation. | REVIEWER_INTERPRETATION; E14 |
| S12 / Synonyms without forced merge | Declarative/explicit-memory expressions are retained while marked synonymous; this does not by itself authorize collapsing every concept/version resource. | REVIEWER_INTERPRETATION; E14 |
| S13 / Fork with stale measurement links | If a disputed concept is split, earlier citations/contrasts may apply to only one new sense. Paper does not define automatic reassignment or versioned provenance rules. | REVIEWER_INTERPRETATION; E13, E14 |
| S14 / Sublexical route query | Historical PubMed expansion adds drug-administration routes to a cognitive phrase. Proposed sense-specific expansion has no independently measured precision/recall gain here. | REVIEWER_INTERPRETATION; E15 |
| S15 / Latent variables and eight tasks | The cited 2009 task/process analysis motivates future meta-analysis. Its eight-task dataset is not a new evaluation or rerun of this 2011 CA prototype. | REVIEWER_INTERPRETATION; E16 |
| S16 / Competing categorization theories | Single-versus-separate cognitive processes could yield different covariance predictions. Authors explicitly say CA cannot yet perform this theory testing. | REVIEWER_INTERPRETATION; E16 |
| S17 / Stop-go response inhibition and VLPFC | Figure 4 callout relates a task contrast, cognitive label and brain activation, with six cited reports. Neither citation count nor edge width proves a causal neural mechanism. | REVIEWER_INTERPRETATION; E17 |
| S18 / Same literature association, different mechanism | Co-occurrence can reflect shared terminology or publication patterns; the same Jaccard value need not mean the same biological relation or construct validity. | REVIEWER_INTERPRETATION; E17 |
| S19 / Present-but-insufficient definition | 795 defined terms out of 904 does not imply expert-accepted definitions; authors say most are insufficient. Missing 109 is arithmetic from reported totals, not a recreated database audit. | REVIEWER_INTERPRETATION; E18 |
| S20 / Class versus concept record | Converting a SKOS concept record to owl:Class can change what it denotes and how relations are interpreted. A byte-level string replacement is not a proved semantics-preserving transformation. | REVIEWER_INTERPRETATION; E05, R02 |
| S21 / External linked data | Imaging/genetic/brain-structure resources are linked rather than stored; reproducible results depend on external versions, query dates and availability. | REVIEWER_INTERPRETATION; E11, E18 |
| S22 / Excluded agency participation | A request for the agent participating in a latent process is outside the implemented relation set described in the paper. A curator/contributor metadata field is not a substitute has_agent relation. | REVIEWER_INTERPRETATION; E09, E13 |

## Critical findings

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| F01 / Specific measurement granularity | Separating latent construct, prescribed task, condition, indicator and contrast is a substantial prior contribution. It avoids treating the name of an experiment as a validated process measurement. | REVIEWER_INTERPRETATION; E03, E05, E06, E10 |
| F02 / Explicit disagreement and sense lifecycle | Discussion, evidence-sensitive curation, forking and synonym retention address conceptual plurality directly. This overlaps with conceptualization/rationale/agent concerns and must be included in later novelty comparison. | REVIEWER_INTERPRETATION; E13, E14 |
| F03 / Representation neutrality has a formal cost | Optional process/representation categories accommodate broad theories but provide no complete covering/disjointness/identity/dependence axioms. Do not infer a fully axiomatized cognitive foundation. | REVIEWER_INTERPRETATION; E05, E09 |
| F04 / Schema arrows do not settle class/individual semantics | SKOS concepts, examples, class inheritance, metadata-property references and empirical database links appear in visual schemas. A uniform mapping of all arrows to OWL subclass or all records to classes is not justified. | REVIEWER_INTERPRETATION; E07, E08, R02 |
| F05 / Measured-by needs claim and context provenance | A measurement link is a disputed theoretical claim about a specific contrast, not a universal causal guarantee. A binary relation alone may lose theory, condition/indicator choice, population, evidence and disagreement context. | REVIEWER_INTERPRETATION; E03, E06, E10, E11 |
| F06 / Condition membership omits arithmetic | A contrast may be nonlinear or signed; includes_condition alone does not preserve coefficient, ordering, baseline or indicator. Figure 2's 0-minus 2 orientation is kept literally for later technical testing. | REVIEWER_INTERPRETATION; E06, E08 |
| F07 / Task descent is not subclass identity | Historical adaptation, subtype relations and meta-analytic commensurability are different concepts. The paper gives no executable threshold for deciding task speciation or inheritable features. | REVIEWER_INTERPRETATION; E10 |
| F08 / Agency and spatial semantics expressly excluded | has_participant/has_agent and spatial relations are omitted. Bibliographic contributors and community curators are represented socially, without resolving participation in a latent mental process. | REVIEWER_INTERPRETATION; E09, E13 |
| F09 / Citation polarity implementation gap | Paper discusses CiTO support/refutation capability but reports only informative citation implemented. Figure 1 SWAN citation references are not automatically identical to CiTO typed evidence. | REVIEWER_INTERPRETATION; E07, E11 |
| F10 / Definition presence is not adequacy | 904 entries=708 mental constructs+196 tasks;795 have definitions but authors judge most insufficient to experts. These are 2011 author-reported records, not complete valid class definitions or present website counts. | REVIEWER_INTERPRETATION; E18 |
| F11 / Relation quantities are not property populations | Fewer than 900 relations means database relation statements, not 900 property types; >800 initial terms and 904 later entries describe different stages. Neither is an independently parsed OWL class count. | REVIEWER_INTERPRETATION; E05, E18 |
| F12 / Utility gains remain largely prospective | Schema/screenshot and developmental status demonstrate a prototype, not controlled gains in precision/recall, neuroscientific prediction, mapping accuracy or expert agreement. Theory testing is explicitly future functionality. | REVIEWER_INTERPRETATION; E12, E14, E15, E16, E18 |
| F13 / Cross-level edges are empirical proposals | Figure 4 Jaccard association and six-reference callout are not entailment, causal direction, molecular mechanism or clinical validation. No reproducible query/date/count table is supplied for the illustrated weights. | REVIEWER_INTERPRETATION; E17 |
| F14 / Native database versus OWL export | Paper uses MySQL with generated OWL, leaving richer data outside formal export. A lossless or semantically equivalent round-trip of statements/discussions/claims is not shown. | REVIEWER_INTERPRETATION; E12, R02 |
| F15 / Later generator changes representation | Pinned generator rewrites skos:Concept to owl:Class and introduces its own measured_by/measures/domain/range choices. These need exact all-class/constraint reconciliation in #241, not silent attribution to the 2011 diagrams. | REVIEWER_INTERPRETATION; E05, E07, E08, R02, R03 |
| F16 / Formal version and repository roles differ | Selected cogat.v 2.owl has formal header 0.3, not version 2. Export repository is distinct from the two-file MIT discussion repository and the author link printed in 2011. Current-source availability does not establish historical byte identity. | REVIEWER_INTERPRETATION; E12, R01, R03, R04 |
| F17 / Namespace does not establish foundation edition | Paper reuses SKOS/CogPO/OBO RO; later BFO 1.1 namespace strings without declared imports do not establish paper BFO grounding, exact imported definitions or an accepted alignment. | REVIEWER_INTERPRETATION; E05, E08, E09, R02, R03 |
| F18 / Forking and curation execution not measured | Evidence-based consensus is a design goal. The paper supplies no fork/merge lineage rule, decision threshold, conflict-resolution success metric or measured curator agreement. | REVIEWER_INTERPRETATION; E13, E14, E18 |
| F19 / License and source identity stay separate | Open-access paper notice, screenshot site badge, generator author terms and discussion-repository MIT notice concern different materials. No blanket reuse permission or upstream change is inferred. | REVIEWER_INTERPRETATION; E01, E14, R02, R04 |
| F20 / Editorial and integration boundaries | p.10 CogPO cross-reference points to footnote 2 though CogPO is footnote 3. Existing PubAtlas/PubBrain/PhenoWiki and NeuroSynth-map reports remain distinct from planned NeuroLex/finer-task/animal-literature integration. No current endpoint or integration test was performed. | REVIEWER_INTERPRETATION; E18, E19 |

## Unresolved questions

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Q01 / Exact root, every class and historical provenance | Choose the already-scoped cogat.v 2.owl candidate, inventory every local/external/referenced/deprecated class and missing definition, and compare selected export header 0.3 with the separate paper-linked generator/source. Record any true 2011 correspondence limits; do not sum releases or reuse paper 904 as a class count. | REVIEWER_INTERPRETATION; E12, E18, R01, R02, R03, R04 |
| Q02 / SKOS concept to OWL class semantics | Reconcile lexical concept records, class declarations, stable identifiers and class/instance/reference levels in raw RDF and generated OWL. Assess whether transformation preserves the intended meaning rather than merely syntactic output. | REVIEWER_INTERPRETATION; E05, E07, E08, R02 |
| Q03 / Measurement direction, domain, range and inverse | Inspect measured_by and measures IRIs, task-versus-contrast targets, declared domain/range and any inverse relation. Preserve exact generated source differences and test a correct contrast link plus an adverse task-only or wrong-kind filler. | REVIEWER_INTERPRETATION; E06, E08, E10, R02, R03 |
| Q04 / Conditions, indicators and signed contrast structure | Check every selected contrast/condition class and restriction against diagrams, including source 0-back minus 2-back orientation, task nesting and indicator provenance. Distinguish membership from signed functional semantics and missing expression fields. | REVIEWER_INTERPRETATION; E06, E08, R02 |
| Q05 / Basic relation mappings and foundations | Trace is-a/part-of/transformation-of/preceded-by/descended-from mappings, all referenced undeclared classes, namespaces and direct imports. Distinguish OBO RO conceptual reuse and BFO1.1/CogPO2011 namespace hints from a verified foundation edition/import closure. | REVIEWER_INTERPRETATION; E08, E09, E10, R02, R03 |
| Q06 / Definitions, citation polarity and source provenance | For all selected classes locate author definition annotations or explicit missing states. Inspect CiTO/SWAN, informative citations versus support/refutation and whether contributor/date/relation evidence survives export. No comment text or citation count becomes logical adequacy. | REVIEWER_INTERPRETATION; E07, E11, E18, R02 |
| Q07 / Disagreement, synonym and fork lineage | Determine which sense/discussion/synonym/merge assertions actually exist in the selected artifact. Check a two-sense example and a stale-link counterexample without inventing identity or expert consensus semantics. | REVIEWER_INTERPRETATION; E13, E14, R02, R03 |
| Q08 / Reproducible generation and bounded semantic execution | Bind raw data tables/dumps, source licenses and exact generator/tool versions. Use only declared safe, reproducible parsing/profile/query/reasoner checks; generator and serialized input execution are not assumed by paper closure. Report concrete blockers and no historical/current-equivalence claim. | REVIEWER_INTERPRETATION; E12, E18, R01, R02, R03, R04 |

## Inputs for later synthesis

| ID / item | Analysis | Basis / evidence |
|---|---|---|
| Y01 / Prior conceptualization workflow | Preserve explicit discussion, curators/contributors, sense forks and evidence-sensitive decisions as prior conceptual knowledge lifecycle structure; do not claim such concerns absent from prior cognitive ontologies. | REVIEWER_INTERPRETATION; E13, E14 |
| Y02 / Measurement versus mental-content mapping | Use construct/task/contrast distinctions and theory-sensitive measured-by as candidate comparisons. Shared labels or RDF access do not justify equivalence with Clariceptify entities. | REVIEWER_INTERPRETATION; E03, E05, E06, E10 |
| Y03 / Candidate scenario bank | Keep disputed Stroop/N-back interpretation, signed contrast, informative-but-opposing citation and stale links after sense fork as later candidate tests, not adopted fixtures or requirements. | REVIEWER_INTERPRETATION; E03, E08, E11, E14 |
| Y04 / Provenance and representation lessons | Separate native knowledge base, generated OWL, current API and historical paper; report all-class definitions/imports and missing source semantics before alignment proposals. | REVIEWER_INTERPRETATION; E12, E18, R01, R02, R03, R04 |
| Y05 / Comparison and queue routing | Paper #79 is complete within its reading boundary; technical #241, comparison #254 and synthesis #126 remain open. All three batch 4 paper inputs have complete deep dossiers but artifact work is unfinished. Next acquired full paper is #262. | REVIEWER_INTERPRETATION; E01, E18, E19 |
| Y06 / Owner decision | All candidate reuse/extension decisions remain DEFER_TO_OWNER_AFTER_SYNTHESIS; no model, manuscript, requirement or release changes follow from this paper review. | REVIEWER_INTERPRETATION; E01, E19 |

## Evaluation evidence

- **Verification:** Authors describe schema relations, database-to-OWL and RDF/SPARQL services, but provide no executed OWL profile/reasoner/regression results in this selected paper. We verified retained hashes/API blob correspondence and parsed selected header metadata only. Figures and prose are not a machine satisfiability proof; #241 owns exact declarations/constraints and tests. [REVIEWER_INTERPRETATION; E07, E08, E09, E12, R01, R02, R03, R04]
- **Validation:** Manual vocabulary curation by three authors and feedback from a small investigator group support design relevance. Sample size/protocol/agreement statistics and expert adequacy criteria are not reported; most available definitions are explicitly judged insufficient. A published paper's reviewer names do not validate this dossier. [REVIEWER_INTERPRETATION; E01, E05, E13, E18]
- **Evaluation:** Prototype figures/screenshots and 2011 content totals characterize development. No controlled retrieval, mapping accuracy, curation outcome, usability or performance benchmark is reported. Eight-task earlier research, six-reference edge illustration and Wikipedia/GO evidence are cited prior examples rather than fresh CA evaluation. Proposed theory testing is explicitly unsupported. [REVIEWER_INTERPRETATION; E04, E13, E14, E15, E16, E17, E18]
- **Assessment:** The paper candidly preserves disagreement, optional representations, excluded agency/spatial relations, coarse task detail and incomplete definitions. Reviewer adverse cases delimit measurement/context, synonym/fork semantics, empirical association and later class-export differences without a corpus-wide quality score. [REVIEWER_INTERPRETATION; E03, E05, E09, E10, E11, E13, E14, E17, E18, R02]
- **Assurance:** DOI/date/source hashes, public author/project repositories and metadata conventions support scholarly and technical provenance. They do not certify expert consensus, sustained interoperability, lossless export or historical-version equivalence. Code, data, paper and discussion-repository license statements remain separate. Clariceptify scientific bytes and release status are protected independently. [REVIEWER_INTERPRETATION; E01, E12, E18, E19, R01, R02, R03, R04]

## Artifact and repository boundary

Technical follow-up: #241. State: `PAPER_LINKED_AND_OFFICIAL_EXPORT_SOURCES_PINNED_TECHNICAL_REVIEW_OPEN`.

Paper-linked poldrack/cogat generator was followed and pinned separately. The retained official cogat-ontology tree at a600c366e9e3d3647a85cbc2c6e53e78abcf1951 has 13 source files; selected ontology/cogat.v2.owl declares formal version 0.3, with no owl:imports. Its generator restructures source concepts as OWL classes and changes task/contrast relations. Distinct CognitiveAtlas/ontology repository has only README and MIT LICENSE. No historical 2011 byte identity, current website equivalence, lossless export, full class-definition glossary, import closure/profile/reasoner or query-generation success follows. #241 owns all selected class declarations/definitions and eight bounded deeper questions.

## Evidence index

| ID | Exact source locator | Source-grounded summary |
|---|---|---|
| E01 | Title/authors/abstract, editor/reviewer information, dates, DOI and rights on pp.1/11 | Nine authors; received 31 March, accepted 17 August, published 6 September 2011; DOI10.3389/fninf.2011.00017. Scholarly peer-review metadata is not independent expert acceptance of this dossier. |
| E02 | Introduction; What is the problem?; Ambiguous terminology; footnote 1 | 2011 background query 2613 papers; working-memory maintenance/manipulation/temporal senses, synonym/polysemy problems and broad cognitive scope including emotion/motivation. Not a current PubMed result. |
| E03 | Complete Tasks versus constructs subsection | Sternberg task contrasts, disputed Stroop inhibition and N-back validity; cognitive-control/task many-to-many associations and changing literature links. Task labels do not establish construct measurement. |
| E04 | Complete Toward an ontology for cognition; footnote 2 | Gruber-style shared specification, GO analogy, MeSH category critique, ACT-R/SOAR contrast and little consensus about mental units. Authors choose to capture disagreement instead of imposing small-group consensus. |
| E05 | The Cognitive Atlas; Structure of the knowledge base; Mental concepts; footnote 3 | Ease of participation, machine access, separate linked process/task ontologies, initial >800 terms curated by three authors; latent construct versus brain realization; optional representation/process subdivision and SKOS Concept modeling. |
| E06 | Mental tasks; Experimental conditions; Indicators; Contrasts, including continuation on p.5 | Prescribed task activity need not produce overt response; CogPO task/condition/contrast categories; quantitative/qualitative indicators; contrast is a function over conditions, including simple, linear and nonlinear comparisons. |
| E07 | Figure 1, complete concept schema and caption | Mental-concept cards plus SKOS, Dublin Core, SIOC and SWAN Citation vocabularies; ten central field labels, working-memory relation examples and measured-by continuation. Dashed reuse/inheritance drawing is not a complete OWL mapping. |
| E08 | Figure 2, complete task schema and caption | Task metadata/indicators, task collection, descended-from task, conditions, contrast and measured-by concept. CogPO/SWAN/NEMO references; imaging database line explicitly empirical. Example contrast is 0-back minus 2-back, not silently reversed. |
| E09 | Relations and Basic ontological relations | OBO RO is-a, part-of, transformation-of and preceded-by adopted conceptually; spatial and has_participant/has_agent relations deliberately excluded. Not all proposed relations implemented in current release. |
| E10 | Relations between processes/tasks; Relations among tasks | measured by targets a task contrast; descended-from expresses task phylogeny/adaptation, with meta-analytic commensurability guiding task-versus-variant distinction. These are not formal cardinality, inverse or identity axioms. |
| E11 | Literature relations; Relations to observed data | All entities including relations can carry citations; CiTO support/refutation is described but only citesForInformation is currently implemented. CA links to external data/entities rather than storing empirical data. |
| E12 | Complete Technical infrastructure; footnote 4 and author GitHub link | Native MySQL store, generated OWL, RDF/SPARQL interfaces and LAMP/AJAX/JSON infrastructure. Author-reported export/accessibility is distinguished from present or historical independent execution. |
| E13 | Benefits and challenges of collaborative knowledge building; Capturing and resolving disagreement; Curation; footnote 5 | Wikipedia lessons motivate integrated concept/relation discussion, evidence-based as-needed curation and fork/merge dispute handling; no measured CA agreement/quality outcome is supplied. |
| E14 | Utility introduction; Clearer vocabulary; Figure 3 and caption | Concept forking creates sense-specific pages plus a disambiguation page; synonyms retain separate terms. Figure 3 behavioral inhibition cognitive versus temperament meanings; screenshot license badge is site-specific. |
| E15 | Improved query expansion, complete example | Historical sublexical-route expansion wrongly brings in drug-administration routes; specific phrase/related-concept expansion proposed, with no precision/recall benchmark or current query execution. |
| E16 | Metadata annotation/meta-analysis; Theory testing | Potential fine-grained brain-process mapping, cited eight-task prior study and future covariance-structure comparison. Paper explicitly says system cannot yet support proposed theory testing. |
| E17 | Translational mental health research; Figure 4 and caption | Five levels: syndromes, cognition, neural systems, signaling pathways and genes, with 13 named nodes. Links are proposed empirical relations, width tied to PubMed Jaccard association; six-reference annotation callout is illustrative, not clinical or causal validation. |
| E18 | Present status and future plans, complete; footnotes 6-10 | Development began 2008; reports 904 terms=708 constructs+196 tasks, 795 definitions mostly acknowledged insufficient, fewer than 900 relations. Personalization/mining/finer tasks and new database/animal-literature links are future scope; some integrations already reported. |
| E19 | Conclusion, Acknowledgments, complete 39-item bibliography and conflict-of-interest statement | All 39 references read; funding and author declarations retained. Related ontology citations are not automatically imports or evidence that this project reproduced their experiments. |
| M01 | Publisher identity/date/DOI metadata; accessed 2026-10-28 | Official title, nine authors, 2011 date and DOI agree with retained complete PDF; selected PDF remains the reading authority. |
| R01 | CognitiveAtlas/cogat-ontology ata600c366e9e3d3647a85cbc2c6e53e78abcf1951: README.md | Official export repository calls this an initial translation effort; v2 reorganizes contrasts under tasks and adds measures. Not proof of 2011 fidelity. |
| R02 | CognitiveAtlas/cogat-ontology ata600c366e9e3d3647a85cbc2c6e53e78abcf1951: create_owl.v2.py | Later generator has Python 2 idioms and raw SKOS-to-owl:Class replacement; embeds namespace/relation/domain-range choices and versionString 0.3. Inspected, not executed. |
| R03 | CognitiveAtlas/cogat-ontology ata600c366e9e3d3647a85cbc2c6e53e78abcf1951: ontology/cogat.v2.owl | Selected retained RDF/XML ontology has header 0.3, no explicit imports and vocabulary references including BFO1.1/CogPO2011. Header parse is not a full class glossary/profile test. |
| R04 | Exact paper-linked poldrack/cogat at 8ae51f96b6116fb2b00ef70f9feac5bac8444071: create_owl.py | Author-linked generator exists and is pinned; source/data inputs and actual 2011 OWL-byte correspondence remain unverified. Author two-condition BSD-style code notice does not blanket-license ontology/data. |

## Closure boundary

Complete exact-paper #79 only after relevant integrity checks and merged PR. All-class/glossary/source-version/import/profile/semantic work remains OPEN in #241 under the explicit paper/module closure exception. #254 comparison and #126 synthesis remain open. No Clariceptify ontology, definitions, requirements, scientific fixtures, manuscript, release or adoption decision is changed.
