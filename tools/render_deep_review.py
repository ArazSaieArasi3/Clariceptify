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
    for key, title in [('catalog', 'Conceptual catalog'), ('commitments', 'Relations and formal commitments'),
                       ('scenarios', 'Requirements, examples and adverse cases'), ('findings', 'Critical findings'),
                       ('questions', 'Unresolved questions'), ('synthesis', 'Inputs for later synthesis')]:
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
            d['artifact']['version_relation'], '', '## Evidence index', '',
            '| ID | Exact source locator | Source-grounded summary |', '|---|---|---|']
    for e in d['evidence']:
        out.append(f"| {e['id']} | {e['locator']} | {e['summary'].replace('|', chr(47))} |")
    out += ['', '## Closure boundary', '', d['closure_boundary'], '']
    return '\n'.join(out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dossier', type=Path)
    args = parser.parse_args()
    d = yaml.safe_load(args.dossier.read_text())
    args.dossier.with_name('report.md').write_text(render(d))
