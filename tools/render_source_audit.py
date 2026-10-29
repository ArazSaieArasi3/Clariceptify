"""Render the shared research source audit and complete selected class glossaries."""
from pathlib import Path
import posixpath
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'evidence/related-work/deep-reviews'


def cell(value):
    return str(value if value is not None else 'UNKNOWN').replace('|', '/').replace('\n', ' ')


def render_audit(audit):
    lines = ['# Repository, foundation and class-coverage audit', '',
             'Checked on ' + audit['checked_on'] + '. ' + audit['scope'], '',
             'The 23 rows are 19 exact paper/version records plus four separate documentation sources. '
             'Repository discovery, formal-file availability, paper review, class definitions and semantic tests are independent states. '
             'NOT_IDENTIFIED is bounded by the recorded searches; NOT_CHECKED is unfinished discovery. Neither means no repository exists.', '',
             'The latest-push and archive flags below are observations, not maintenance or quality ratings. '
             'UFO-A/B/C are modules; an unversioned BFO/UFO name does not establish BFO1/UFO1.', '',
             '| Exact source | Repository / public files | Foundation and relation | Local glossary | Next issue |',
             '|---|---|---|---|---|']
    for row in audit['records']:
        repo = row['repository']
        repos = '; '.join('[source](' + u + ')' for u in repo['urls'])
        f = row['foundation']
        c = row['class_coverage']
        coverage = c['state']
        if c['catalog_path']:
            relative = posixpath.relpath(c['catalog_path'], 'evidence/related-work/deep-reviews').replace('.yaml', '.md')
            coverage = f"[{c['local_classes']} classes]({relative}); {c['source_definition_candidates']} comment candidates; {c['missing_source_definitions']} missing"
        cells = [f"{row['id']} (#{row['primary_issue']})", repo['state'] + ('; ' + repos if repos else '') + '; ' + row['artifact_state'],
                 cell(f['family']) + '; ' + f['relation'] + '; edition: ' + cell(f['edition']), coverage,
                 ', '.join('#' + str(n) for n in row['next_issues'])]
        lines.append('| ' + ' | '.join(cell(x) for x in cells) + ' |')
    lines += ['', '## Retained public repository observations', '',
              '| Repository | Retained commit | Archived / disabled | Observed last push | Tracked files |', '|---|---|---|---|---|']
    for r in audit['repository_observations']:
        lines.append('| ' + ' | '.join([f"[{r['repository']}]({r['url']})", r['retained_commit'],
                     str(r['archived']) + ' / ' + str(r['disabled']), r['pushed_at'], str(r['tracked_files'])]) + ' |')
    lines += ['', audit['o4oa_repository_boundary'], '',
              '## Discovery log', '']
    for d in audit['discovery_attempts']:
        lines += ['### ' + d['id'] + ': ' + d['method'], '',
                  'Query: `' + d['query'] + '`. Checked: ' + d['checked_on'] + '.', '']
        if 'returned' in d:
            lines += ['Returned candidate names (limit ' + str(d['result_limit']) + '): ' +
                      (', '.join(d['returned']) if d['returned'] else 'none returned by this query') + '.', '']
        for url in d.get('checked_urls', []):
            lines += ['- ' + url]
        if d.get('checked_urls'):
            lines += ['']
        if 'outcome' in d:
            lines += [d['outcome'], '']
        lines += ['Limit: ' + d['limitation'], '']
    lines += ['## Interpretation and next work', '',
              'All-local-class glossaries account for every declared class in their selected module boundary. '
              'Comment candidates are not automatically sufficient logical definitions. Missing definitions stay visible; '
              'imported definitions remain separate. Read the [mandatory catalogue contract](catalog-contract.yaml) and '
              '[coverage guide](coverage-guide.md) before interpreting completion.', '',
              'For LMM, 29 local classes have been catalogued; four lack source definition comments. '
              'The remaining 125 unique asserted-closure class IRIs comprise 124 local DUL/IOLite classes and owl:Thing; '
              'the DUL 78-class glossary has nine absent and two label-only comments; the [IOLite shared glossary](shared-foundations/IOLite/README.md) accounts for all46 local classes with three absent comments. '
              'The separate [DUL technical review](../artifacts/DUL-technical-review.md) records 29 bounded HermiT cases. '
              'The source-audit table itself is a glossary/discovery record, not a reasoner run, historical equivalence or final synthesis.', '',
              'Clariceptify model change: NONE. Final synthesis #126 stays open; later adoption requires the owner decision.', '']
    return '\n'.join(lines)


def render_catalog(catalog):
    lines = ['# ' + catalog['work_id'] + ': selected class glossary', '',
             'Issue #' + str(catalog['issue']) + '. ' + catalog['population_policy'], '',
             'Every definition below is a short reviewer paraphrase of the source comment. '
             'A comment may be incomplete, informal or ambiguous; logical constraints are recorded separately. '
             'MISSING means no source definition comment was found in the selected bytes, not that no definition exists anywhere.', '',
             '| Module | Local classes | External redeclarations | Source version |', '|---|---|---|---|']
    for m in catalog['modules']:
        lines.append('| ' + ' | '.join(cell(m[k]) for k in ['id', 'local_named_classes', 'external_named_class_redeclarations', 'version']) + ' |')
        lines += ['', 'Source: ' + m['source_url'] + '. SHA256 `' + m['source_sha256'] + '`. '
                  'All named declarations and outgoing constraints: [' + m['id'] + ' census](' +
                  posixpath.relpath(m['census_path'],
                                   'evidence/related-work/deep-reviews/' + catalog['work_id']) + ').', '']
    lines += ['| Class IRI | Definition / missing state | Named superclasses | Notes |', '|---|---|---|---|']
    for r in catalog['classes']:
        definition = r['reviewer_definition']['text'] or '**MISSING SOURCE DEFINITION**'
        parents = '; '.join(r['named_superclasses']) or 'No named superclass asserted in this document'
        lines.append('| ' + ' | '.join(cell(x) for x in [r['iri'], definition, parents, '; '.join(r['notes'])]) + ' |')
    lines += ['', 'Full labels, definition/annotation hashes, exact source IRIs/predicates, deprecated status, '
              'equivalence counts and constraint pointers are retained in [classes.yaml](classes.yaml).', '',
              'Local classes: ' + str(catalog['counts']['local_classes']) + '; source comment candidates: ' +
              str(catalog['counts']['source_definition_candidates']) + '; missing source definitions: ' +
              str(catalog['counts']['missing_source_definitions']) + '.', '',
              'Imported glossary: ' + catalog['imported_glossary']['state'] + '. ' +
              catalog['imported_glossary']['limitation'], '',
              'Reasoning: NOT_EXECUTED. Historical paper fidelity: NOT_ESTABLISHED. Model change: NONE.', '']
    return '\n'.join(lines)


def write(root=ROOT):
    base = root / 'evidence/related-work/deep-reviews'
    audit = yaml.safe_load((base / 'source-audit.yaml').read_text())
    (base / 'source-audit.md').write_text(render_audit(audit))
    for path in base.rglob('classes.yaml'):
        path.with_suffix('.md').write_text(render_catalog(yaml.safe_load(path.read_text())))


if __name__ == '__main__':
    write()
