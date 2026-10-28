"""Validate source-access accounting and LMM evidence without private-source access."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    folder = root / 'evidence/related-work/corpus'
    inventory = yaml.safe_load((folder / 'access-inventory.yaml').read_text())
    rows = inventory['records']
    if len(rows) != 19 or len({row['candidate_id'] for row in rows}) != 19:
        raise ValueError('Original candidate denominator drift')
    missing = yaml.safe_load((folder / 'download-requests.yaml').read_text())['requests']
    expected = {row['candidate_id'] for row in rows if row['access_status'] == 'FULL_TEXT_NOT_ACQUIRED'}
    expected |= {row['id'] for row in inventory['additional_work_or_version_records'] if row['status'] == 'FULL_TEXT_NOT_ACQUIRED'}
    if {row['id'] for row in missing} != expected or len(missing) != len(expected):
        raise ValueError('Missing-text request population mismatch')
    if 'owner_intake_revision' in inventory:
        receipt = json.loads((root / inventory['owner_intake_revision']['receipt']).read_text())
        if receipt['frozen_archive_modified'] or receipt['exact_paper_population'] != 19:
            raise ValueError('Owner intake changed frozen archive or paper population')
        supplied = receipt['records']
        if len(supplied) != 6 or len({r['work_id'] for r in supplied}) != 6:
            raise ValueError('Owner intake source population mismatch')
        inputs = {r.get('candidate_id', r.get('id')): r for r in
                  rows + inventory['additional_work_or_version_records']}
        for r in supplied:
            current = inputs[r['work_id']]
            if (current['filename'] != r['filename'] or current['sha256'] != r['sha256'] or
                    current.get('access_status', current.get('status')) != 'ACQUIRED' or
                    r['raw_source_public'] or not r['review_pages'] or
                    r['review_pages'] != sorted(set(r['review_pages'])) or
                    any(p < 1 or p > r['container_pdf_pages'] for p in r['review_pages'])):
                raise ValueError('Owner intake source identity or page scope drift')
    for row in rows:
        if row['access_status'] == 'ACQUIRED' and not (row['filename'] and len(row['sha256'] or '') == 64):
            raise ValueError('Acquired source lacks exact identity')
    archive = json.loads((folder / 'archive-record.json').read_text())
    if archive['readback'] != 'ALL_MEMBERS_AND_DIGESTS_VERIFIED' or archive['availability'] != 'SAVED_OWNER_ACCESSIBLE_ARCHIVE':
        raise ValueError('Archive is not saved and verified')
    raw_manifest = (root / archive['source_manifest']).read_bytes()
    manifest = json.loads(raw_manifest)
    if hashlib.sha256(raw_manifest).hexdigest() != archive['source_manifest_sha256'] or len(manifest['members']) != archive['registered_source_members']:
        raise ValueError('Archive manifest identity mismatch')
    repos = json.loads((folder / 'repository-snapshots.json').read_text())
    if len(repos) != archive['repository_snapshots'] or any(row['status'] != 'SNAPSHOT_ACQUIRED' or len(row['commit']) != 40 for row in repos):
        raise ValueError('Unpinned repository snapshot')
    paper = yaml.safe_load((root / 'evidence/related-work/reviews/LMM.yaml').read_text())
    artifact = yaml.safe_load((root / 'evidence/related-work/artifacts/LMM.yaml').read_text())
    if paper['access']['sha256'] != artifact['paper_binding']['paper_sha256']:
        raise ValueError('Paper/artifact binding drift')
    for module in artifact['modules']:
        raw = (root / module['report']).read_bytes()
        report = json.loads(raw)
        if hashlib.sha256(raw).hexdigest() != module['report_sha256'] or report['counts'] != module['counts']:
            raise ValueError('LMM inspection evidence changed')
        if report['reasoner_execution'] != 'NOT_EXECUTED' or report['counts']['inferred_classes'] is not None:
            raise ValueError('Unperformed inference promoted')
    if artifact['paper_binding']['historical_axiom_fidelity'] != 'NOT_ASSESSED':
        raise ValueError('Historical paper/artifact identity overclaimed')
    tasks = json.loads((folder / 'extension-tasks.json').read_text())
    if len({row['id'] for row in tasks}) != len(tasks) or any(not row.get('issue') or not row.get('acs') for row in tasks):
        raise ValueError('Unregistered extension tasks')
    return {'status': 'PASS', 'original_candidate_labels': 19,
            'missing_text_requests': len(missing), 'repository_snapshots': len(repos),
            'registered_extension_tasks': len(tasks), 'lmm_modules_inspected': 2,
            'scope': 'Public accounting, saved-archive receipt and evidence identity; not completed corpus review or independent semantic acceptance.'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
