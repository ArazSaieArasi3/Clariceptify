"""Render the bounded official-document review, not a paper or formal-artifact review."""
from pathlib import Path
import json,yaml
ROOT=Path(__file__).resolve().parents[1]
def render(r,images):
 lines=['# OntoLex-Lemon: 2016 official-document critical review','',
 f"Issue #75 | {r['status']} | Reviewed {r['reviewed_on']}",'',
 'This is an AI-assisted review of the official Community Group Report, not a W3C Standard, journal paper, formal-artifact validation, or independent scientific acceptance.','',
 '[Pinned source]('+r['identity']['source_url']+') | [Structured review](OntoLex.yaml) | [Document inventory](../../../evaluation/related-work/ontolex/document-census.json) | [Image inspection](../../../evaluation/related-work/ontolex/image-inspection.json)','',
 'SHA256: `'+r['identity']['source_sha256']+'`. Exact bytes match the retained acquisition manifest. Editors: '+', '.join(r['identity']['editors'])+'.','',
 '## Short source synopsis','',r['source_synopsis']['text'],'',
 '## Critical review dimensions','']
 for name,d in r['dimensions'].items():lines+=['- **'+name.replace('_',' ')+':** '+d['judgment']+' [Source locator]('+d['locator']+').']
 lines+=['','## Findings and retained questions','']
 for f in r['findings']:lines+=['- **'+f['id']+':** '+f['judgment']+' [Source locator]('+f['locator']+'). Follow-up: '+', '.join('#'+str(x) for x in f['next_issues'])+'.']
 lines+=['','## Illustration discrepancies','',
 'Every non-logo image was visually inspected. These are document-level observations; none establishes an OWL inconsistency. Enlarged inspection disproved an initial suspected language-arrow swap in F48.','']
 for f in images['images']:
  if f.get('reviewer_observation'):lines+=['- **'+f['id']+':** '+f['reviewer_observation']+' [Image]('+f['url']+').']
 lines+=['','## Reviewer-constructed adverse cases','']
 for a in r['adverse_cases']:lines+=['- **'+a['id']+':** '+a['scenario']+' Expected review disposition: `'+a['expected']+'`. Execution: `'+a['execution']+'`.']
 lines+=['','## Reading coverage','',r['coverage']['count_policy'],'',
 '| Section | Reading state |','|---|---|']
 for s in r['coverage']['numbered_sections']:lines+=['| ['+s['title']+']('+r['identity']['source_url']+'#'+s['anchor']+') | '+s['state']+' |']
 lines+=['','## VVEAA and interpretation limits','']
 for k,v in r['evaluation'].items():lines+=['- **'+k+':** '+v]
 lines+=['','## Decision and closure','',
 'Recommendation: alignment/reuse candidate; adoption deferred. No ontology import, model edit or manuscript change performed. Artifact counts, formal tests and full class definitions remain #237; comparison #253 and synthesis #126 remain separate.','',r['closure_boundary'],'',
 'The report contains original reviewer commentary and source locators. Raw source HTML and images are not redistributed. The source rights notice is retained by link, not converted into a claim of relicensing permission.','',
 'Validation: `python tools/check_ontolex_review.py`; exact private-input reparse: add `--source path/to/OntoLex-specification.html`. Structural PASS does not establish scientific correctness.','']
 return '\n'.join(lines)
if __name__=='__main__':
 p=ROOT/'evidence/related-work/reviews/OntoLex.yaml';r=yaml.safe_load(p.read_text());imgs=json.loads((ROOT/r['evidence']['images']['path']).read_text());p.with_suffix('.md').write_text(render(r,imgs))
