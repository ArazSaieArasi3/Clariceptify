"""One public integrity entrypoint with exact source and validator provenance."""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKERS = ['check_repository_language', 'check_schemas', 'check_model_structure',
            'check_requirements', 'check_source_support', 'check_traceability', 'check_bootstrap',
            'check_reference_views', 'check_conceptualization_fixtures', 'check_review_state', 'check_publication_metadata']


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args]).decode().strip()


def run(output):
    output = Path(output).resolve()
    if output.is_relative_to(ROOT):
        raise ValueError('Keep generated run reports outside the evaluated repository')
    names = subprocess.check_output(['git', '-C', str(ROOT), 'ls-files', '--cached', '--others', '--exclude-standard', '-z']).decode().rstrip('\0').split('\0')
    fingerprints = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in sorted(set(names))}
    source_digest = hashlib.sha256(json.dumps(fingerprints, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    source = {'commit': git('rev-parse', 'HEAD'), 'tree': git('rev-parse', 'HEAD^{tree}'),
              'source_path_digest_sha256': source_digest, 'files': fingerprints,
              'file_inventory_policy': 'Tracked and non-ignored untracked files; generated reports are outside this tree.',
              'working_tree_status': git('status', '--porcelain', '--untracked-files=all')}
    if source['working_tree_status']:
        # Local edits may be inspected, but are never represented as a clean commit.
        source['binding_state'] = 'working_tree_differs_from_commit'
    else:
        source['binding_state'] = 'clean_tracked_snapshot'
    reports, statuses = {}, {}
    for name in CHECKERS:
        if any(value != 'PASS' for value in statuses.values()):
            statuses[name] = 'NOT_RUN'
            continue
        result = subprocess.run([sys.executable, str(ROOT / 'tools' / (name + '.py'))],
                                cwd=ROOT, capture_output=True, text=True, timeout=180)
        try:
            report = json.loads(result.stdout)
        except json.JSONDecodeError:
            report = {'status': 'FAIL', 'error': (result.stderr or result.stdout)[-5000:]}
        if name == 'check_bootstrap' and 'checks' in report:
            report['checks'] = sorted(report['checks'])
        statuses[name] = 'PASS' if result.returncode == 0 and report.get('status') == 'PASS' else 'FAIL'
        reports[name + '.json'] = encoded(report)
    reports['SOURCE-FINGERPRINT.json'] = encoded(source)
    manifest = {'status': 'PASS' if all(value == 'PASS' for value in statuses.values()) else 'FAIL',
                'scope': 'Public integrity checks only; not semantic acceptance or independent review',
                'source': {key: value for key, value in source.items() if key != 'files'},
                'checks': statuses,
                'runtime': {'python': platform.python_version(),
                            'jsonschema': importlib.metadata.version('jsonschema'),
                            'PyYAML': importlib.metadata.version('PyYAML')},
                'ci_context': {name: os.environ.get(name) for name in
                               ['GITHUB_EVENT_NAME', 'GITHUB_SHA', 'GITHUB_RUN_ID', 'GITHUB_RUN_ATTEMPT', 'PR_HEAD_SHA']},
                'validator_file_sha256': {path: digest for path, digest in fingerprints.items() if path.startswith('tools/') and path.endswith('.py')},
                'report_sha256': {name: hashlib.sha256(content).hexdigest() for name, content in reports.items()}}
    output.mkdir(parents=True, exist_ok=True)
    for name, content in reports.items():
        (output / name).write_bytes(content)
    (output / 'RUN-MANIFEST.json').write_bytes(encoded(manifest))
    summary = {'status': manifest['status'], 'source_commit': source['commit'], 'source_tree': source['tree'],
               'source_fingerprint': source_digest, 'binding_state': source['binding_state'], 'checks': statuses,
               'manifest_sha256': hashlib.sha256(encoded(manifest)).hexdigest()}
    print('INTEGRITY_SUMMARY ' + json.dumps(summary, sort_keys=True))
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    raise SystemExit(run(args.output)['status'] != 'PASS')
