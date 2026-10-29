"""Render source-bound BDI glossary/review authorities; no semantic evaluation."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def cell(text):
    return str(text if text is not None else 'NOT_REPORTED').replace('|', '/').replace('\n', ' ')


def render_catalog(c):
    lines = ['# BDI 2026: complete selected class glossary', '',
             'Issue #250. ' + c['declaration_policy'], '', c['definition_policy'], '',
             '22 BDI domain classes, three external metadata/test declarations and ten d0 classes '
             'are accounted for here. The 78 DUL classes reuse the '
             '[existing source-pinned glossary](dul-class-catalog.md); they are not duplicated.', '',
             'One BDI Belief comment ends mid-sentence. Three external class declarations have no '
             'definition in the selected source. Missing definitions are not invented. '
             'The exact alignment import of BDI0.3 is unavailable; its full population remains unknown.', '',
             '| Module | Class / label | Source definition state | Attributed reviewer paraphrase |',
             '|---|---|---|---|']
    for r in c['classes']:
        lines.append('| ' + ' | '.join(map(cell, [r['module'], f"[{r['label']}]({r['iri']})",
            r['source_definition']['status'], r['reviewer_definition']['text']])) + ' |')
    lines += ['', '## Identity, hierarchy and constraints', '',
              'The [structured authority](bdi2026-class-catalog.yaml) records every exact IRI, '
              'label basis, source hash, comment digest/locator, deprecated flag, named superclass, '
              'equivalence, direct and incoming disjointness, complete n-ary disjoint group and '
              'constraint pointer. The [census](../../evaluation/related-work/bdi2026/technical-census.json) '
              'also preserves property axioms and separates declarations, undeclared class-position '
              'references, anonymous expressions and builtin vocabulary.', '',
              'd0 Event is described as deprecated in prose, without an owl:deprecated true assertion. '
              'd0 versionInfo contains entries1.2 through1.5, without a versionIRI;DUL4.2 is the '
              'current exact retrieved root. These bytes do not establish historical paper equivalence.', '',
              'Core0.5 has no imports. The alignment references d0 and BDI0.3;d0 imports DUL. '
              'The acquired foundation closure has 89 distinct declared named IRIs, including owl:Thing. '
              'Three core external redeclarations (VOAF/OWLUnit) are metadata/test vocabulary, not '
              'three additional BDI domain concepts or an acquired upstream definition glossary.', '',
              'No Clariceptify model change, independent expert approval or accepted reuse.', '']
    return '\n'.join(lines)


def render_review(r):
    s = r['execution_summary']
    lines = ['# FOSSR BDI 2026: bounded technical review', '',
             'Issue #250. ' + r['status'] + '.', '',
             'The exact official core0.5 and alignment are inspected separately. '
             'Negative outcomes and the missing BDI0.3 import remain findings; '
             'review completion does not certify the source or adopt it into Clariceptify.', '',
             '| Check | Observed outcome |', '|---|---|',
             '| Complete glossary | 22 core local classes, three external declarations and ten d0 classes; shared DUL78 glossary |',
             '| OWL2 DL profile | FAIL: reserved rdf:type declared an annotation property |',
             '| Loaded core logical consistency | Consistent; no unsatisfiable named core classes returned |',
             '| Bounded consistency/adverse cases | ' + str(s['semantic_cases']['passed']) + '/' + str(s['semantic_cases']['total']) + ' expected outcomes reproduced; includes two inconsistent author datasets |',
             '| Asserted SPARQL executions | 17/36 exact expected binding matches across two unchanged datasets; 19 mismatches |',
             '| Exact full alignment validation | BLOCKED: BDI0.3 import HTTP404; no substitution |',
             '| OWLUnit / LLM / SEMAS reproduction | Not executed; zero paid API calls |', '',
             'All30 adverse-case expectations being reproduced does not mean that30 author requirements '
             'passed. Both author datasets are inconsistent with core0.5, and a single modifies edge '
             'forces a contradiction through disjoint domain classes. HermiT results concern the '
             'logical ontology loaded by OWLAPI, not an OWL2 DL-conformance certificate.', '',
             '## Eight technical questions', '']
    for q in r['questions']:
        lines += ['### ' + q['id'] + ': ' + q['title'], '', q['result'], '',
                  'Locators: ' + '; '.join(q['locators']) + '.', '',
                  'Evidence: ' + ', '.join('[' + k + '](../../../' + r['evidence'][k]['path'] + ')' for k in q['evidence']) + '.', '']
    lines += ['## Findings retained for comparison', '', '| Finding | Observation |', '|---|---|']
    for f in r['findings']:
        lines.append('| ' + f['id'] + ': ' + cell(f['title']) + ' | ' + cell(f['detail']) + ' |')
    lines += ['', 'All findings feed #256 and #126. No author file is silently repaired. '
              'Source versions, namespaces, entailment regimes and paper metric populations remain distinct.', '',
              '## Reproduce', '',
              'Use the pinned [source manifest](../corpus/bdi2026-inputs.yaml), keep raw files outside '
              'the repository and install `requirements-bdi-review.txt`. The inspector verifies '
              'every input digest before parsing; it makes no implicit network imports.', '',
              '```bash',
              'python tools/inspect_bdi2026.py census --source-dir /external/inputs --output /external/census.json',
              'python tools/inspect_bdi2026.py cqs --source-dir /external/inputs --output /external/cqs.json',
              'python tools/inspect_bdi2026.py reason --source-dir /external/inputs --output /external/semantics.json --private-dir /external/reasoner-inputs',
              'python tools/check_bdi2026_review.py --source-dir /external/inputs',
              '```', '',
              'The default public checker checks recorded evidence/provenance and rendered parity; '
              'it does not rerun HermiT, issue requests to remote sources or validate all meanings.', '',
              'Root MIT and ontology CC-BY-4.0 notices are separate. No raw third-party sources or '
              'annotation corpus are redistributed. Full alignment validation remains unavailable '
              'without exact0.3 bytes; foundation names do not establish historical edition equality. '
              'Adoption requires the owner decision after comparison/synthesis. '
              'Model, requirements, fixtures, manuscript and release changes: NONE.', '']
    return '\n'.join(lines)


def run():
    catalog = yaml.safe_load((ROOT / 'evidence/related-work/bdi2026-class-catalog.yaml').read_text())
    review = yaml.safe_load((ROOT / 'evidence/related-work/artifacts/BDI2026.yaml').read_text())
    (ROOT / 'evidence/related-work/bdi2026-class-catalog.md').write_text(render_catalog(catalog))
    (ROOT / 'evidence/related-work/artifacts/BDI2026.md').write_text(render_review(review))


if __name__ == '__main__':
    run()
