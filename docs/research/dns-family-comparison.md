# First bounded comparison: the DnS family

Input: R1 v0.1.0, model input-r1-rev1, main 45415798a6ba307e6e98d7591595ca2ca370e154.
Review date: 2026-10-25. This is the first execution wave under the frozen
[protocol](../../evidence/related-work/review-protocol.yaml), not the complete
corpus synthesis under #126 or the prerelease under #135. The original candidate
register, R1 model and historical evidence reports retain their original identities.

| Evidence object | Exact reviewed source | Supported overlap | Disposition |
| --- | --- | --- | --- |
| DnS | Gangemi and Mika, OTM 2003; institutional 18-page PDF | Context, descriptions, situations, intentional interpretation and communication | Candidate alignment; review #68 |
| cDnS paper | Gangemi, Lehmann and Catenacci, Dagstuhl 2007; 40-page PDF | Agent/community-relative redescription, information, internal representations and time | Candidate alignment; review #69 |
| cDnS artifact | Official cDnS.owl 1.1; header refers to JAAMAS 2008 | Asserted description/concept/entity/situation/agent relations | Selected artifact inspection #87; no 2007/2008 axiom equivalence inferred |
| Conceptualization documentation | Author-issued Conceptualization.owl 0.1, marked preliminary | Internal representation, assumption, belief, knowledge and action-oriented adoption | Embedded documentation review #71; no standalone paper invented |
| Conceptualization artifact | Same 0.1 bytes, explicitly importing pinned DUL 4.2 | Nested existential restrictions and attitude subproperties | Selected artifact inspection #89; compatibility with the original historical import remains unassessed |
| DUL chapter | Presutti and Gangemi, 2016, DOI 10.3233/978-1-61499-676-7-81 | Metadata verified; full text unavailable | #70 stays open; no chapter-content finding |
| DUL artifact | Official DUL.owl 4.2, served as Turtle | Agent conceptualization, description, classification, expression and satisfaction | Technical inspection recorded; #88 retains #70 prerequisite |

## Reproducible populations

| Artifact | Local named owl:Class IRIs | External named classes explicitly declared in the document | Named classes in pinned asserted import closure | Inferred classes |
| --- | ---: | ---: | ---: | --- |
| cDnS 1.1 | 12 | 0 | 12 | Not computed |
| DUL 4.2 | 78 | 1 | 79 | Not computed |
| Conceptualization 0.1 | 1 | 0 | 80 | Not computed |

These are unique URI subjects explicitly typed owl:Class. Anonymous class
expressions are excluded. DUL explicitly declares owl:Thing, which is external to
its namespace. Conceptualization's closure includes that declaration and the 78
DUL classes. No counts are inferred and no published conceptual-catalog count is
substituted for an OWL count. Exact URLs, hashes, formats, imports and selected
axioms are in the [input manifest](../../evidence/related-work/artifact-inputs.yaml)
and [machine reports](../../evaluation/related-work/artifacts/).

## Consequences for the research argument

The claim that prior ontologies do not represent conceptualization, agent-relative
interpretation or internal representation is not defensible against these sources.
Their overlap is substantive. Current evidence supports retaining these works as
close comparators; it does not support discarding them as merely generic upper
ontologies.

A narrower comparison target is Clariceptify's explicit episode participation,
recorded conceptual decisions (CLR-C0021), and justification content (CLR-C0065).
The [review index](../../evidence/related-work/review-index.yaml) binds the actual
model definitions. A future scenario must test whether these distinctions are
already expressible in each comparator, what specialization is necessary, and
whether Clariceptify adds useful explicit constraints. These are proposed questions,
not an established novelty or superiority result. No model bytes change in this wave.

Two translation cautions matter. The Conceptualization internal-representation
restriction uses nested existentials; it does not enforce identity between the
realizing cognitive system and the conceptualizing Agent. Also, DUL's current
version removes several disjointness commitments found in older variants. Exact
versioned constraints, rather than label similarity, must govern any alignment.
The selected graph inspection is not an entailment or satisfiability proof.

## Completion and next bounded packages

Five deliverables are ready for closure: #68, #69, #71, #87 and #89. The reviews
record source versions, exact locators, access and evaluation limits, overlap,
counterevidence and reuse decisions. DUL chapter #70 and its dependent #88 remain
open. No full-text access limitation has been converted into scientific acceptance.
The complete comparison-preview prerequisites remain unchanged.

1. Complete #70 when the 2016 chapter is obtainable, then reconcile #88.
2. Work next on LMM #72/#90 and O4OA #73/#91 in separate paper/artifact packages;
   an access blocker in one source need not stall independent work.
3. Assess #135 only after all its exact prerequisites, with explicit incomplete
   states; finish the broader #126 synthesis after its separate corpus dependencies.
4. Carry supported findings into R2 domain/source/CQ assessment and final manuscript
   work. Neither this wave nor passing CI is independent scientific review.
