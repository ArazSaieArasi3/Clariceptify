"""Render a blocked technical checkpoint without promoting document evidence."""
from pathlib import Path
import json,yaml
ROOT=Path(__file__).resolve().parents[1]
BASE='evidence/related-work/artifacts/O4OA.yaml'
def render(r,data):
 lines=['# O4OA: supporting specification and blocked technical review','',f"Issue #91 | {r['status']} | Checked {r['checked_on']}",'',
 '**Issue #91 remains open.** The supporting document review does not satisfy the unavailable formal-artifact, every-class/import, solver or API criteria.','',
 '[Structured checkpoint](O4OA.yaml) | [Document-only term inventory](O4OA-specification-terms.json) | [Official specification]('+r['identity']['source_url']+')','',
 'The exact 44-page PROS-TR-2023-I document v1 was read. Its front matter says ontology 2.6; the conclusion says 6.2. The ER2023 conference paper remains a separate source. No version identity has been silently repaired.','',
 '## What was actually inspected','',
 '- All 44 pages, 29 numbered figures, 16 numbered tables and 79 bibliography entries. Figures 28/29 are dense composite views; visual inspection is not a machine population census.',
 '- All 138 Table 5 rows: 125 descriptive candidates, 13 label-only candidates; one missing printed stereotype (XML DTDs). Short paraphrases preserve source spelling and missing information.',
 '- Three CQ groups with 21 subordinate questions and document coverage responses. These were read, not executed.',
 '- Current reference-project metadata is public but the repository-tree endpoint returns HTTP 403. No bypass was attempted.',
 '- The separate pinned gO4OA tree contains eight entries/five files and no identified formal ontology root. This does not establish global nonexistence.','',
 '## Eight technical obligations','', '| Question | State | Evidence-qualified result |','|---|---|---|']
 for q in r['questions']:lines+=['| '+q['id']+' | '+q['status']+' | '+q['judgment']+' |']
 lines+=['','## Source findings','']
 for f in r['findings']:lines+=['- **'+f['id']+':** '+f['judgment']+' ('+f['locator']+').']
 lines+=['','## Conceptual adverse cases, not executed tests','']
 for a in r['conceptual_adverse_cases']:lines+=['- **'+a['id']+':** '+a['scenario']+' '+a['disposition']]
 lines+=['','## Document term inventory','',
 'These are printed Table 5 rows, not released classes. Every machine-class IRI is null. Descriptive candidates are not certified logical definitions; label-only rows remain explicit.','',
 '| Row | Source label | Printed stereotype | PDF page | Source-definition state | Short reviewer paraphrase |','|---|---|---|---:|---|---|']
 for x in data['terms']['rows']:lines+=['| '+x['id']+' | '+x['source_label']+' | '+(x['source_stereotype'] or 'NOT_REPORTED')+' | '+str(x['pdf_page'])+' | '+x['definition_status']+' | '+x['reviewer_paraphrase']+' |']
 lines+=['','## Completion gate and required input','',r['closure']['required_input'],'',
 'Local/imported/inferred machine class populations remain unknown. No OCL/Alloy/HermiT/API execution, license permission, source correction, scientific adoption or model change is claimed. #252 and #126 remain separate dependent research tasks.','',
 'Checks validate evidence integrity and non-promotion boundaries, not source semantics: `python tools/check_o4oa_checkpoint.py`; optional `--source` verifies the exact private PDF hash and printed stereotype sequence.','',
 'Raw PDF, page images and extracted source definitions are not redistributed. Document rights and unavailable model rights remain separate from repository licenses.','']
 return '\n'.join(lines)
if __name__=='__main__':
 r=yaml.safe_load((ROOT/BASE).read_text());d={k:json.loads((ROOT/v['path']).read_text()) for k,v in r['evidence'].items()};(ROOT/BASE).with_suffix('.md').write_text(render(r,d))
