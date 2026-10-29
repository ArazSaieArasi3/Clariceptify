"""Render the Cognitive Atlas technical authority and complete glossary guide."""
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]


def render_catalog(c):
    lines=['# Cognitive Atlas: complete selected class and definition register','',
        'Issue #241. Selected `cogat.v2.owl` has formal header 0.3 and source SHA256 `'+c['source_sha256']+'`.','',
        '| Population | Count |','|---|---:|',
        '| Local declared named classes | 1696 |','| External class declarations | 2 |',
        '| Local classes with nonempty source definition | 1232 |','| Empty definition annotations | 55 |',
        '| No definition annotation | 409 |','| Local class IRIs with two source identifiers | 101 |','',
        'Every selected declaration appears in [classes.jsonl](cognitiveatlas/classes.jsonl), including '
        'all labels/identifiers, hierarchy, equivalence, constraints, annotation digests, provenance and '
        'explicit definition gaps. The [attributed definition register](cognitiveatlas/source-definitions.jsonl) '
        'preserves all available original wording, including empty fields and ambiguous records. '
        'It is a separately licensed CC-BY-SA 3.0 US content extract; it is not mass-generated paraphrase '
        'or a claim that all 1696 definitions were independently validated. Read its '
        '[attribution and license scope](cognitiveatlas/ATTRIBUTION.md).','',
        'The 101 mixed construct/contrast identifiers are retained as ambiguity, not assigned an '
        'arbitrary preferred identity. Missing text is never invented. These are 1696 local class IRIs, '
        'not the 2011 paper population of 904 terms or the live website population.','',
        'No declared imports occur. Referenced undeclared classes/properties and BFO/CogPO namespace '
        'hints are recorded separately in the [census](../../evaluation/related-work/cognitiveatlas/technical-census.json); '
        'they do not prove a foundational import or alignment.','',
        'The [technical review](artifacts/CognitiveAtlas.md) retains eight source-bound questions and '
        'actual profile/reasoner results. No Clariceptify scientific artifact or release changed.','']
    return '\n'.join(lines)


def render_review(r):
    lines=['# Cognitive Atlas: bounded technical review','',
        'Issue #241. '+r['status']+'.','',
        'The selected later OWL export is inspected independently of the completed 2011 paper review. '
        'Every selected class and definition availability state is accounted for. Source defects '
        'and historical limits remain findings, not repaired author artifacts.','',
        '| Check | Observed result |','|---|---|',
        '| Complete class register | 1696 local and two external declarations; 101 mixed identifier collisions |',
        '| Definition availability | 1232 nonempty, 55 empty and 409 absent among local classes |',
        '| Object properties | Three local and one external declaration; seven used restriction properties |',
        '| OWL2 DL profile | FAIL: 7341 undeclared-entity violations under the recorded OWLAPI validator |',
        '| Loaded logical ontology | Consistent, no unsatisfiable named classes returned |',
        '| Isolated HermiT expectations | 14/14 expected consistency/adverse outcomes reproduced |',
        '| Author generator / pickle / historical reproduction | Not executed; both raw RDF input parses fail |','',
        'Consistency does not establish correct conceptual identity or definition adequacy. '
        'The complete [class guide](../cognitiveatlas-class-catalog.md) links the structured declarations '
        'and separately attributed original definitions. No artificial class definitions are invented.','']
    for q in r['questions']:
        lines+=['## '+q['id']+': '+q['title'],'', q['result'],'',
                'Locators: '+ '; '.join(q['locators'])+'.','',
                'Evidence: '+', '.join('['+k+'](../../../'+r['evidence'][k]['path']+')' for k in q['evidence'])+'.','']
    lines+=['## Findings for comparison #254 and synthesis #126','','| ID | Finding |','|---|---|']
    for f in r['findings']:lines+=['| '+f['id']+': '+f['title']+' | '+f['detail']+' |']
    lines+=['','## Reproduce and interpret','',
        'Keep exact original files outside the repository using the [source manifest](../corpus/cognitiveatlas-inputs.yaml). '
        'Install `requirements-cognitiveatlas-review.txt`. The original Python 2 generator is not ported '
        'or executed, and no pickle is loaded.','',
        '```bash',
        'python tools/inspect_cognitive_atlas.py census --source-dir /external/cogat --output /external/census.json --catalog-dir /external/catalog',
        'python tools/inspect_cognitive_atlas.py static --source-dir /external/cogat --output /external/static.json',
        'python tools/inspect_cognitive_atlas.py reason --source-dir /external/cogat --output /external/semantics.json --private-dir /external/reasoner-inputs',
        'python tools/check_cognitiveatlas_review.py --source-dir /external/cogat',
        '```','',
        'The [descriptive corpus baseline](../../../docs/research/source-review-descriptives.md) summarizes '
        'the completed deep-reading wave and selected formal roots with separate units. It does not '
        'close the remaining technical inspections, six comparison batches or final synthesis.','',
        'Source definition text is an attributed CC-BY-SA 3.0 US extract. Project code, source code '
        'notices, the separate MIT discussion repository, the exact OWL source and current website '
        'remain distinct license/version scopes. The original ontology/source files are not redistributed. '
        'No independent expert acceptance, historical 2011 equivalence, automatic alignment, '
        'Clariceptify model/requirements/fixtures/manuscript change or new release is claimed.','']
    return '\n'.join(lines)


if __name__=='__main__':
    c=yaml.safe_load((ROOT/'evidence/related-work/cognitiveatlas-class-catalog.yaml').read_text())
    r=yaml.safe_load((ROOT/'evidence/related-work/artifacts/CognitiveAtlas.yaml').read_text())
    (ROOT/'evidence/related-work/cognitiveatlas-class-catalog.md').write_text(render_catalog(c))
    (ROOT/'evidence/related-work/artifacts/CognitiveAtlas.md').write_text(render_review(r))
