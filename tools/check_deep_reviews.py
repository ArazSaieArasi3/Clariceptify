"""Check research-dossier provenance and closure boundaries, not scientific truth."""
from pathlib import Path
import hashlib
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = 'evidence/related-work/deep-reviews'
PROTECTED = ('model/', 'requirements/', 'ontology/', 'ontologies/', 'formal/',
             'fixtures/', 'releases/', 'docs/decisions/', 'docs/research/manuscript')


def protected_fingerprint(root):
    members = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in root.rglob('*') if p.is_file()
               and (str(p.relative_to(root)).startswith(PROTECTED)
                    or str(p.relative_to(root)) == 'CITATION.cff')}
    return {'files': len(members), 'sha256': hashlib.sha256(
        json.dumps(members, sort_keys=True, separators=(',', ':')).encode()).hexdigest()}


def validate_dossier(d, entry, dimensions):
    def require(condition, message):
        if not condition:
            raise ValueError(entry['id'] + ': ' + message)
    require(d['work_id'] == entry['id'] and d['issue'] == entry['issue'], 'work/issue mismatch')
    require(d['source']['sha256'] == entry['sha256'] and
            d['source']['filename'] == entry['filename'], 'changed source identity')
    require(d['source']['pdf_pages'] == entry['pdf_pages'], 'changed page population')
    require(d['boundary']['model_change'] == 'NONE' and
            d['boundary']['adoption'] == 'OWNER_DECISION_REQUIRED' and
            d['boundary']['independent_expert_review'] == 'NOT_PERFORMED', 'unauthorized promotion')
    evidence = {e['id']: e for e in d['evidence']}
    require(len(evidence) == len(d['evidence']), 'duplicate evidence ID')
    for e in evidence.values():
        require(e['locator'] and e['summary'], 'empty evidence locator/summary')
        if e.get('source_kind', 'PAPER') == 'PAPER':
            require(e['pages'] and all(isinstance(p, int) and 1 <= p <= entry['pdf_pages'] for p in e['pages']), 'invalid evidence page')
        else:
            require(e['source_kind'] == 'REPOSITORY' and e.get('path') and
                    re.fullmatch(r'[0-9a-f]{40}', e.get('commit', '')) and
                    re.fullmatch(r'[0-9a-f]{64}', e.get('sha256', '')), 'unpinned repository evidence')
    require(set(d['dimensions']) == set(dimensions), 'missing shared review dimension')
    statements = list(d['dimensions'].values())
    for section in ['catalog', 'commitments', 'scenarios', 'findings', 'questions', 'synthesis']:
        require(isinstance(d[section], list) and d[section], 'missing ' + section)
        ids = [r['id'] for r in d[section]]
        require(len(ids) == len(set(ids)), 'duplicate IDs in ' + section)
        statements.extend(d[section])
    statements.extend(d['evaluation'].values())
    for row in statements:
        require(row.get('statement') and row.get('evidence'), 'unbound statement')
        require(set(row['evidence']) <= set(evidence), 'dangling evidence reference')
        require(row['basis'] in {'AUTHOR_REPORTED', 'REVIEWER_INTERPRETATION',
                                'EXECUTED', 'NOT_REPORTED', 'UNKNOWN'}, 'untyped evidence')
        if row['basis'] == 'EXECUTED':
            require(row.get('execution_ref'), 'execution without inspectable result')
    require(set(d['evaluation']) == {'Verification', 'Validation', 'Evaluation', 'Assessment', 'Assurance'}, 'missing VVEAA function')
    if d['status'] == 'REVIEW_COMPLETE':
        require(d['coverage']['read_pages'] == list(range(1, entry['pdf_pages'] + 1)), 'incomplete full-text reading')
        require(d['coverage']['units'] and all(u['status'] == 'REVIEWED' and
                u.get('evidence') and set(u['evidence']) <= set(evidence)
                for u in d['coverage']['units']), 'unreviewed paper unit')
        require(d['coverage']['visual_pages'] and d['coverage']['catalog_boundary'], 'missing visual/catalog boundary')
        require(d['artifact']['issue'] in entry['artifact_issues'] and
                d['artifact']['version_relation'] and d['artifact']['status'], 'artifact boundary missing')
    else:
        require(d['status'] == 'IN_PROGRESS', 'invalid review state')


def check(root=ROOT):
    base = root / BASE
    protocol = yaml.safe_load((base / 'protocol.yaml').read_text())
    register = yaml.safe_load((base / 'register.yaml').read_text())
    expected = json.loads((base / 'baseline-protection.json').read_text())
    if protected_fingerprint(root) != expected['fingerprint']:
        raise ValueError('Research-only boundary violated: protected scientific baseline changed')
    entries = register['acquired_papers'] + register['waiting_for_owner']
    if len({r['id'] for r in entries}) != len(entries) or len({r['issue'] for r in entries}) != len(entries):
        raise ValueError('Duplicate paper identity or primary issue')
    if len(register['acquired_papers']) != 12 or len(register['waiting_for_owner']) != 7:
        raise ValueError('Changed approved paper population; record a protocol revision')
    inventory = yaml.safe_load((root / 'evidence/related-work/corpus/access-inventory.yaml').read_text())
    inputs = {r.get('filename'): r for r in inventory['records'] + inventory['additional_work_or_version_records'] if r.get('filename')}
    done = []
    for entry in register['acquired_papers']:
        if inputs[entry['filename']]['sha256'] != entry['sha256']:
            raise ValueError('Paper identity diverges from retained corpus')
        path = base / entry['id'] / 'review.yaml'
        if not path.exists():
            if entry['state'] != 'QUEUED':
                raise ValueError('Missing review for claimed progress')
            continue
        d = yaml.safe_load(path.read_text())
        validate_dossier(d, entry, protocol['dimensions'])
        if entry['state'] != d['status']:
            raise ValueError('Register/review state mismatch')
        from render_deep_review import render
        if (path.parent / 'report.md').read_text() != render(d):
            raise ValueError('Stale readable report')
        if d['status'] == 'REVIEW_COMPLETE':
            done.append(entry['id'])
    for entry in register['waiting_for_owner']:
        if entry['state'] != 'BLOCKED_ON_FULL_TEXT' or entry.get('sha256') is not None:
            raise ValueError('Missing full text promoted')
    return {'status': 'PASS', 'acquired_papers': 12, 'completed_deep_reviews': done,
            'queued_papers': sum(r['state'] == 'QUEUED' for r in register['acquired_papers']),
            'waiting_for_owner': 7, 'protected_baseline': expected['fingerprint'],
            'scope': 'Provenance, coverage declarations and state boundaries; not independent semantic validation.'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
