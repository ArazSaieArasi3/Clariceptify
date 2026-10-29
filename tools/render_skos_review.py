"""Render the source-bound SKOS document review, not an artifact validation."""
from pathlib import Path
import json,yaml
ROOT=Path(__file__).resolve().parents[1]
def render(r,data):
 lines=['# SKOS Reference: 2009 document critical review','',f"Issue #76 | {r['status']} | Reviewed {r['reviewed_on']}",'','This is an AI-assisted review of the W3C Recommendation and its official errata, not a journal-paper review, schema validation or adoption decision.','',
 '[Pinned Reference]('+r['identity']['source_url']+') | [Structured review](SKOS.yaml) | [Document inventory](../../../evaluation/related-work/skos/document-census.json) | [Reading ledger](../../../evaluation/related-work/skos/reading-ledger.json) | [Errata review](../../../evaluation/related-work/skos/errata-review.json)','',
 'SHA256: `'+r['identity']['source_sha256']+'`. Exact bytes match the retained acquisition manifest. Editors: '+', '.join(r['identity']['editors'])+'.','',r['source_synopsis']['text'],'','## Coverage and populations','',
 'Read 143 numbered/appendix headings, 62 semantic statements, 90 numbered examples and two text subproperty diagrams. No substantive image figures occur; two badges are excluded. Source examples were inspected, not run.','',r['coverage']['count_policy'],'',r['coverage']['semantic_statement_scope'],'',
 'The separate Primer is not represented as fully reviewed. The official errata are retained separately; they do not overwrite the archived Reference bytes.','',
 '## Critical review dimensions','']
 for name,d in r['dimensions'].items():lines+=['- **'+name.replace('_',' ')+':** '+d['judgment']+' [Locator]('+d['locator']+').']
 lines+=['','## Findings and follow-up questions','']
 for f in r['findings']:lines+=['- **'+f['id']+':** '+f['judgment']+' [Locator]('+f['locator']+'). Follow-up: #238, #253, #126.']
 lines+=['','## Official corrections and their scope','']
 for e in data['errata']['entries']:lines+=['- ['+e['id']+']('+e['locator']+'): '+e['reviewer_disposition']+' Scope: `'+e['scope']+'`.']
 lines+=['','## Reviewer-constructed adverse cases','']
 for a in r['adverse_cases']:lines+=['- **'+a['id']+':** '+a['scenario']+' Disposition: `'+a['expected']+'`. This is conceptual analysis, not an executed reasoner test.']
 lines+=['','## Reading ledger','',
 'All semantic statement and example identifiers are bound to source-row/table hashes in the machine-readable ledger. An inspection state records reading, not a semantic PASS. Two unanchored XL summary headings use their actual nearest section locator; no invented anchor is created.','',
 '| Heading | Source location | State |','|---|---|---|']
 for s in r['coverage']['sections']:lines+=['| '+s['title']+' | [Source]('+r['identity']['source_url']+'#'+s['locator_anchor']+') | '+s['state']+' |']
 lines+=['','## VVEAA and claim ceiling','']
 for k,v in r['evaluation'].items():lines+=['- **'+k+':** '+v]
 lines+=['','## Decision and closure','',r['closure_boundary'],'','Recommendation: retain as an alignment/reuse candidate; defer adoption and novelty judgments to #238/#253/#126. No model, requirements, fixtures, manuscript or release changes.','',
 'Raw HTML and source illustrations are not redistributed. Source rights remain separate from the repository license.','',
 'Checks: `python tools/check_skos_review.py`; optional exact private-input verification adds `--source path/to/SKOS-reference.html --errata path/to/SKOS-errata.html`. Structural PASS does not establish scientific correctness.','']
 return '\n'.join(lines)
if __name__=='__main__':
 p=ROOT/'evidence/related-work/reviews/SKOS.yaml';r=yaml.safe_load(p.read_text());data={k:json.loads((ROOT/v['path']).read_text()) for k,v in r['evidence'].items()};p.with_suffix('.md').write_text(render(r,data))
