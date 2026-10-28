"""Derive a readable report from the structured paper dossier."""
from pathlib import Path
import argparse
import yaml


def render(d):
    out = [f"# {d['identity']['title']}", '',
           f"Work: `{d['work_id']}` | Issue: #{d['issue']} | State: `{d['status']}`", '',
           f"Reviewed version: {d['identity']['version']}. Input: `{d['source']['filename']}`, "
           f"{d['source']['pdf_pages']} PDF pages, SHA256 `{d['source']['sha256']}`.", '',
           'The structured `review.yaml` is the evidence authority; this report is derived. '
           'This is an AI-assisted critical review, not independent expert acceptance. '
           'Clariceptify is unchanged; later use requires an owner decision.', '',
           '## Identity and reading coverage', '', d['identity']['boundary'], '',
           d['coverage']['catalog_boundary'], '',
           '| Paper unit | Coverage | Evidence |', '|---|---|---|']
    def refs(row):
        return ', '.join(row['evidence'])
    for u in d['coverage']['units']:
        out.append(f"| {u['unit']} | {u['status']} | {refs(u)} |")
    out += ['', '## Common review dimensions', '']
    for key, r in d['dimensions'].items():
        out += [f"### {key}", '', f"{r['statement']} [{r['basis']}; {refs(r)}]", '']
    sections = [('catalog', 'Conceptual catalog'), ('commitments', 'Relations and formal commitments'),
                       ('scenarios', 'Requirements, examples and adverse cases'), ('findings', 'Critical findings'),
                       ('questions', 'Unresolved questions'), ('synthesis', 'Inputs for later synthesis')]
    if d.get('relation_index'):
        sections.insert(2, ('relation_index', 'Complete paper relation index'))
    for key, title in sections:
        out += [f'## {title}', '', '| ID / item | Analysis | Basis / evidence |', '|---|---|---|']
        for r in d[key]:
            statement = r['statement'].replace('|', '\\|').replace('\n', '<br>')
            out.append(f"| {r['id']} / {r['label']} | {statement} | {r['basis']}; {refs(r)} |")
        out.append('')
    out += ['## Evaluation evidence', '']
    for key, r in d['evaluation'].items():
        out += [f"- **{key}:** {r['statement']} [{r['basis']}; {refs(r)}]"]
    out += ['', '## Artifact and repository boundary', '',
            f"Technical follow-up: #{d['artifact']['issue']}. State: `{d['artifact']['status']}`.", '',
            d['artifact']['version_relation'], '']
    if d['artifact'].get('class_reviews'):
        out += [d['artifact'].get('class_reviews_heading', '### Every named class in the retained local core'), '',
                '| ID / class | Manual constraint/correspondence review | Evidence |', '|---|---|---|']
        for r in d['artifact']['class_reviews']:
            out.append(f"| {r['id']} / {r['label']} | {r['statement']} | {r['basis']}; {refs(r)} |")
        out.append('')
    out += ['## Evidence index', '',
            '| ID | Exact source locator | Source-grounded summary |', '|---|---|---|']
    for e in d['evidence']:
        out.append(f"| {e['id']} | {e['locator']} | {e['summary'].replace('|', chr(47))} |")
    out += ['', '## Closure boundary', '', d['closure_boundary'], '']
    return '\n'.join(out)


def render_limited(d, receipt):
    """Render the explicitly different owner-summary evidence scope."""
    out = ['# ' + d['identity']['title'] + ': limited-summary review', '',
           f"Work: `{d['work_id']}` | Issue: #{d['issue']} | State: `{d['status']}`", '',
           'Content evidence: owner-provided Google Quick Read, with separately attributed '
           'bibliographic checks and one qualifying indexed lead. Original full text, '
           'figures and exact formula glyphs remain unreviewed. This completed limited task '
           'is counted separately from the 18 completed full-paper reviews.', '',
           '[Citation-use guide](citation-guide.md) | [Summary receipt](summary-receipt.yaml) | '
           '[Structured review](limited-review.yaml)', '',
           '## Supplied-summary coverage', '', '| Unit | Owner-summary locator | Coverage |',
           '|---|---|---|']
    for u in receipt['units']:
        out.append(f"| {u['id']} / {u['label']} | {u['owner_summary_locator']} | REVIEWED_AS_SECONDARY_SUMMARY |")
    claims = {r['id']: r for r in receipt['claims']}
    out += ['', '## Every supplied claim and critical assessment', '',
            '| Claim | Faithful summary paraphrase | Critical assessment |', '|---|---|---|']
    for r in d['claim_reviews']:
        claim = claims[r['summary_claim_id']]
        out.append('| ' + ' | '.join(x.replace('|', '/') for x in
                   [claim['id'], claim['statement'], r['statement']]) + ' |')
    out += ['', '## Common analytical dimensions', '']
    for key, r in d['dimensions'].items():
        out += ['### ' + key, '', r['statement'] + ' [' + ', '.join(r['evidence']) + ']', '']
    for key, title in [('catalog', 'Summary-level conceptual catalog'),
                       ('relations', 'Reported relation distinctions'),
                       ('scenarios', 'Positive and adverse reconstructions'),
                       ('findings', 'Critical findings'), ('questions', 'Open research questions')]:
        out += ['## ' + title, '', '| ID / item | Analysis | Evidence |', '|---|---|---|']
        for r in d[key]:
            out.append('| ' + ' | '.join(x.replace('|', '/') for x in
                       [r['id'] + ' / ' + r['label'], r['statement'], ', '.join(r['evidence'])]) + ' |')
        out.append('')
    out += ['## Evaluation evidence', '']
    for key, r in d['evaluation'].items():
        out += ['- **' + key + ':** ' + r['statement']]
    out += ['', '## Separately attributed metadata and indexed evidence', '']
    for e in d['additional_evidence']:
        out += ['- ' + e['id'] + ' / ' + e['source_kind'] + ': ' + e['url'] + '. ' + e['locator']]
    out += ['', '## Citation and closure', '', d['citation_guidance']['bibliographic_reference'], '',
            d['citation_guidance']['evidence_qualification'], '', d['closure_boundary'], '']
    return '\n'.join(out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dossier', type=Path)
    args = parser.parse_args()
    d = yaml.safe_load(args.dossier.read_text())
    if d.get('review_kind') == 'OWNER_SUMMARY_LIMITED_CRITICAL_REVIEW':
        receipt = yaml.safe_load((Path(__file__).resolve().parents[1] /
                                  d['summary_receipt']['path']).read_text())
        output = render_limited(d, receipt)
    else:
        output = render(d)
    args.dossier.with_name('report.md').write_text(output)
