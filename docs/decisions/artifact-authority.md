# Artifact authority and composition

Decision date: 2026-10-24. Status: adopted for the R1 preparation scope. Evidence: issue [#4](https://github.com/ArazSaieArasi3/Clariceptify/issues/4).

## Semantic composition

When imported and accepted, `model/domains.yaml`, `concepts.yaml`, `relations.yaml`, `generalizations.yaml` and `constraints.yaml` jointly define the conceptual model. All entries use stable IDs. Membership links a concept to one primary domain. Associations use source/target IDs; generalizations use child/parent IDs. A constraint references affected entity IDs and its interpretation/enforcement status. Definitions, stereotypes, multiplicities and qualified constraints belong to these registries, not to a diagram alone.

Schemas under `model/schema/` define record contracts. Schema validity is not referential integrity or semantic adequacy. Unknown semantic judgments remain not_assessed. When sources conflict, record a finding rather than silently selecting a representation as truth.

## Authority by family

| Family | Authority | Derived representations |
|---|---|---|
| Conceptual commitments | model/*.yaml after controlled import | diagram, tables, reference pages |
| Requirements and CQ contracts | requirements/*.yaml | ORSD reports |
| Evidence and support qualifications | evidence/ | bibliography and evidence summaries |
| Cross-artifact bindings | traceability/ | matrices and graphs |
| Actual evaluation/review results | evaluation/ | dashboards and prose summaries |
| Explanations and rationale | docs/ and decision records | published documentation surfaces |
| Frozen package membership | releases/<version>/manifest | archive and citation bindings |

Model registries are initially planned, not already imported. An input DOCX retains its historical wording and hash; its controlled extraction becomes the editable destination after parity and disposition. The article and thesis are consumers/evidence, not alternate model editors. OWL is absent at this station; later formal sources may be authoritative for the formal layer only, with explicit conceptual mapping.

## Controlled correction

Change semantic source first; identify affected IDs, requirements, constraints, figures, claims and evaluations; record the change; regenerate affected displays; rerun relevant checks; re-review changed judgments. Generated files must identify their upstream ref and generator. Do not fix a generated label by redefining semantics only in the figure.

The class Relation and other conceptualization classes are distinct from engineering metadata records about this project. A project evidence record is not automatically an instance of the modeled Evidence class. Wiki/Pages are future publication surfaces, not independent authorities.
