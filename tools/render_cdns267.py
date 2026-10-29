"""Render the eight-category cDnS core followup with negative results intact."""
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
PATH='evidence/related-work/artifacts/cDnS-core-followup.yaml'
def render(r):
 lines=['# cDnS1.1: core profile and eight correspondence checks','',
 'Issue #267 | '+r['status']+' | 2026-10-29','',
 'The unchanged selected core has 12 named classes, 47 object properties, 411 RDF triples, 14 anonymous restrictions and no declared imports. Its header refers to JAAMAS2008; exact 2007/2008 release fidelity remains unestablished. Existing complete selected-class catalogues are reused, not replaced.','',
 '| Actual operation | Recorded outcome |','|---|---|',
 '| Exact input and retained census reconciliation | PASS |',
 '| OWLAPI OWL2 DL profile | FAIL: one non-simple-property minimum-cardinality violation |',
 '| HermiT construction on unchanged full core | Refused for hasProperPart cardinality |',
 '| Logical consistency / unsatisfiable classes | NOT_ESTABLISHED / null |',
 '| Asserted RDF queries | 8/8 expected ASK results; source-structure checks only |',
 '| Whole-core positive/adverse consistency scenarios | Not executed after reasoner refusal |',
 '| Source repair or approximate surrogate | Not performed |','',
 '[Structured review](cDnS-core-followup.yaml) | [Actual execution receipt](../../../evaluation/related-work/cdns267/execution.json) | [Existing complete core glossary](../deep-reviews/cDnS2007/classes.md) | [Separately mapped extension glossary](../deep-reviews/cDnS-journal-2008/classes.md)','',
 '## Profile finding and safe execution boundary','',
 'Bundle requires at least two hasProperPart fillers while hasProperPart is declared transitive. OWLAPI reports this as a non-simple property in ObjectMinCardinality; HermiT raises IllegalArgumentException for the same restriction. Tool refusal is not an inconsistency proof. The source was not stripped, cardinality was not weakened and transitivity was not removed.','',r['harness_decision'],'',
 '## Eight selected comparisons','']
 for q in r['questions']:
  lines+=['### '+q['id']+': '+q['title'],'',q['disposition']+'. '+q['interpretation'],'','Locators: '+ '; '.join(q['artifact_locators'])+'.','',
   'Positive scenario: '+q['positive_scenario'],'','Adverse scenario: '+q['adverse_scenario'],'','Scenario execution: '+q['scenario_execution']+'. The corresponding asserted source query is recorded separately.','']
 lines+=['## Findings and later use','','| Finding | Source question | Utilization categories |','|---|---|---|']
 for f in r['findings']:lines.append('| '+f['id']+': '+f['title']+' | '+f['question_id']+' | '+', '.join(f['utilization_categories'])+' |')
 lines+=['','Apply the [maintained U01-U13 plan](../../../docs/research/review-utilization-plan.md). These comparisons feed #251 and #126; no model adequacy or accepted equivalence is inferred.','']
 for x in r['candidate_uses']:lines.append('- '+x['source_question']+' -> '+', '.join(x['model_ids'])+': '+x['proposal']+' Status: '+x['status']+'.')
 lines+=['','## Reproduce and interpret','',
 'Obtain cDnS.owl with the recorded SHA256 outside the repository. Install requirements-bdi-review.txt for the pinned RDFLib/JPype/HermiT dependencies.','',
 '```bash','python tools/inspect_cdns267.py --source /external/cDnS.owl --output /external/execution.json','python tools/check_cdns267.py --source /external/cDnS.owl','```','',
 'The selected root imports nothing. The separately mapped collInt/ground/core catalogue is contextual evidence, not a loaded or reasoned extension in this followup. Original-host compatibility and the full 141/147-display theories remain outside this execution. No full source text, raw ontology, source repair, independent expert approval, Clariceptify model/requirements/fixtures/manuscript change or release is introduced.','']
 return '\n'.join(lines)
if __name__=='__main__':
 r=yaml.safe_load((ROOT/PATH).read_text());(ROOT/PATH).with_suffix('.md').write_text(render(r))
