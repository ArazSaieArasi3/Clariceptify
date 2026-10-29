# LMM L1/L2 paper-to-artifact correspondence

Issue #274. [Structured eight-question authority](LMM-correspondence.yaml), [exact execution receipt](../../../evaluation/related-work/lmm274/execution.json), [bounded historical-root discovery](../../../evaluation/related-work/lmm274/discovery.json). Research-only comparison; Clariceptify model and release unchanged.

The source is the seven-page [2008 LMM paper](../deep-reviews/LMM2008/review.yaml), SHA256 `e32e763cfc0c9b50f146cbf2d65bb81828b5176f16a822eebbd5cb75fb598903`. Current selected inputs are LMM_L2 1.2 (`512f7a2c...`), LMM_L1 1.8 (`955518d7...`), IOLite 1.8 (`15f8ac17...`) and DUL 4.2 (`e5f64295...`); complete hashes and import IRIs are in the [input manifest](../corpus/lmm-inputs.yaml). All four exact official files were reacquired with matching hashes and loaded offline without source changes. These versions are **not certified as the original 2008 release**. The exact LMM_Alignments.owl cited by the paper was not acquired; bounded 2026-10-29 HTTP/HTTPS probes returned 403 or redirected to HTML. No global repository absence follows.

## Results

| Question | Current-file result and paper correspondence |
| --- | --- |
| Q01 Historical alignment root | Original alignment OWL unavailable; current L1/L2 are not a substitute. |
| Q02 Expression/Meaning/Reference | Current Expression accepts an `expresses` **or** `denotes` existential arm, unlike the figure's displayed `expresses` minimum one. Meaning requires an expressing Expression. Old `interprets` names are not automatically the current `hasInterpretation` pair. |
| Q03 Conceptual levels | A Concept individual and its `isInstanceOf` reference can coexist. This does not equate a concept individual with an OWL class or turn figure arrows into `rdfs:subClassOf`. Situation/Reference/Context and Description/Meaning placements are version-specific. |
| Q04 Context | A Context with no **named** interpretation is consistent; its existential `isContextOf` witness may be anonymous. The selected axioms do not demonstrate a joined agent, speech act, expression, meaning, referent and intention or a disambiguation algorithm. |
| Q05 Reference/membership | IndividualReference needs concept and collection witnesses; explicitly denying either is inconsistent. MultipleReference with no named member remains consistent, while ExtensionalReference with `hasMember` forced empty is inconsistent. Paper membership wording versus figure/example remains qualified. |
| Q06 Expression distinctions | Name/ContextualExpression and ConceptExpression/Name co-instantiation are inconsistent. Distinct Name and ConceptExpression individuals can have the same label. Spelling is not an individual-identity rule or a polysemy benchmark. |
| Q07 Definitions | All 29 local classes were previously catalogued: 25 have comment candidates; AssociativeRule, LSARule, LatentContext and SyntacticRule have none. Three comment-versus-axiom names diverge: AssociativeContext/rule, EnumeratedExpression/AnaphoricExpression, SimpleConceptExpression/ClassReference. No upstream correction or invented definition. |
| Q08 Lexical alignment | WordNet hypernymy versus `specializes` is illustrative in the paper. Without exact alignment axioms, no representative direction, all-resource compatibility or semantic equivalence was executed. |

## Executed evidence and limits

The exact four-document asserted import closure passes the recorded OWL2 DL profile. HermiT 1.3.8.1099 reports the selected root consistent with no unsatisfiable named classes. All **13 isolated positive/adverse expectations** match observed consistency. Each test stores canonical N-Triples, SHA256, expected and observed results; the generator and tool versions are in the receipt. These are bounded logical checks, not validation, historical reconstruction, reasoner proof of all paper diagrams, or measured lexical performance. Zero asserted SPARQL queries and zero exact alignment-root tests were run.

The complete selected LMM local glossary is 8 L1 plus 21 L2 classes; the 154-IRI asserted closure includes imported DUL/IOLite terms and `owl:Thing`, with separate [shared glossaries](../deep-reviews/shared-foundations/IOLite/README.md) and [DUL review](DUL-technical-review.md). Raw third-party bytes are kept outside the public repository. No header redistribution license was established. Eight findings feed #252/#126; two actual Clariceptify-ID candidate uses remain `OWNER_DECISION_REQUIRED`, with no accepted mapping.
