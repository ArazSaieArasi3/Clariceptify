"""Render the bounded DnS module review and its complete selected glossary."""
from pathlib import Path
import yaml,json
ROOT=Path(__file__).resolve().parents[1]
def render_catalog(c):
 lines=['# DnS: complete selected ExtendedDnS397 class register','',
 'Issue #235. The later 2005 DLP3971 distribution is not proven identical to the 2003 paper. All 58 local and ten external declarations in the selected root are accounted for. All local classes have comments; non-agentive-figure defers its typology rather than supplying a distinguishing definition. External root declarations have no inline comments; their available comments are linked to the pinned direct DOLCE-Lite import. The full 95-class import closure is not an independently reviewed full import glossary.','',
 'The [structured register](dns235-class-catalog.yaml) retains exact IRIs, annotation hashes, source identities and qualifications. All hierarchy, equivalence, disjointness and anonymous constraint expressions are retained by IRI in the [exact census](../../evaluation/related-work/dns235/census.json). No source definition is certified as logically adequate.','',
 '| Class (local name) | Population | Definition state | Short attributed reviewer paraphrase |','|---|---|---|---|']
 for x in c['classes']:lines.append('| '+('DnS:' if x['population']=='LOCAL' else 'DOLCE-Lite:')+x['iri'].split('#')[-1]+' | '+x['population']+' | '+x['source_definition']['state']+' | '+x['reviewer_definition']['text']+' |')
 return '\n'.join(lines+['','Source: ISTC-CNR Laboratory for Applied Ontology, selected DLP3971 bytes. Original files and full source comments are not redistributed. [Bounded technical review](artifacts/DnS.md).',''])
def render_review(r):
 lines=['# DnS: bounded review of the later ExtendedDnS397 module','',
 'Issue #235. '+r['status']+'.','',
 'Official standalone DLP3971 distribution, copyright 2005, selected ExtendedDnS.owl header 397/classified. Exact 2003 paper fidelity remains NOT_ESTABLISHED. No current cDnS or DUL replacement is used.','',
 '| Observed population/check | Result |','|---|---|',
 '| Selected named classes | 58 local / ten external redeclarations |',
 '| Local source comments | 58 present; one insufficient typology placeholder |',
 '| Object-property declarations | 118 local / 15 external; zero datatype properties in selected root |',
 '| Actual imports | DOLCE-Lite, SpatialRelations, TemporalRelations; all supplied files resolved offline |',
 '| Four-document closure | 95 unique declared classes; not a global corpus count |',
 '| Recorded OWL2 DL profile | PASS under pinned OWLAPI |',
 '| Recorded HermiT baseline | Consistent; no unsatisfiable named classes returned |',
 '| Isolated semantic expectations | 15/15 expected positive/adverse outcomes reproduced |','',
 '[Complete selected class guide](../dns235-class-catalog.md) | [Structured authority](DnS.yaml) | [Census](../../../evaluation/related-work/dns235/census.json) | [Actual execution receipt](../../../evaluation/related-work/dns235/semantics.json)','']
 for q in r['questions']:lines+=['## '+q['id']+': '+q['title'],'',q['result'],'','Locators: '+q['locators']+'.','']
 lines+=['## Findings and planned use','','| Finding | Evidence-qualified conclusion | Utilization categories |','|---|---|---|']
 for f in r['findings']:lines.append('| '+f['id']+': '+f['title']+' | '+f['detail']+' | '+', '.join(f['utilization_categories'])+' |')
 lines+=['','## Candidate comparisons, not accepted mappings','','Use the [maintained utilization plan](../../../docs/research/review-utilization-plan.md). Comparison #251 and synthesis #126 retain their own prerequisites.','']
 for p in r['model_comparison_candidates']:lines.append('- '+p['source']+' -> '+', '.join(p['model_ids'])+': '+p['action']+' State: '+p['status']+'.')
 lines+=['','Reuse decision: '+r['reuse']['decision']+'.','',r['reuse']['positive_scenario'],'',r['reuse']['counterexample'],'',
 '## Reproduce and interpret','',
 'Obtain the exact official DLP3971.zip outside the repository. Install requirements-bdi-review.txt. The existing corpus/dlp3971-intake.json pins the archive and modules. No source rewriting or network import resolution occurs.','',
 '```bash','python tools/inspect_dns235.py census --source-dir /external/dns --output /external/census.json','python tools/inspect_dns235.py reason --source-dir /external/dns --private-dir /external/reasoning --output /external/semantics.json','python tools/check_dns235.py --source-dir /external/dns','```','',
 r['execution']['harness_note'],'',
 'OWL2 profile/reasoner outcomes concern loaded logical axioms under the recorded tools. They do not prove the earlier FOL formulas, a complete theory of conceptualization, source-definition adequacy or accepted alignment. Formula 14 and SWAP are not solver/execution claims. README LGPL-2.1-or-later applies to its source distribution; original ontology files/comments are not republished here. No Clariceptify model, requirements, fixtures, manuscript or release changed.','']
 return '\n'.join(lines)
if __name__=='__main__':
 c=yaml.safe_load((ROOT/'evidence/related-work/dns235-class-catalog.yaml').read_text());r=yaml.safe_load((ROOT/'evidence/related-work/artifacts/DnS.yaml').read_text())
 (ROOT/'evidence/related-work/dns235-class-catalog.md').write_text(render_catalog(c));(ROOT/'evidence/related-work/artifacts/DnS.md').write_text(render_review(r))
