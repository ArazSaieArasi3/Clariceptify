"""Build and read back the explicitly frozen alpha.2.1 input baseline."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TAG = 'v0.1.0-alpha.2.1'
SOURCE = 'fe347d2e62262f1cd43558d2330438f433f64f1d'
TREE = '5ac2c0e112081479a898d58aa831e55891dcd1ec'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def digest(value):
    return hashlib.sha256(value).hexdigest()


def build(request_path, output):
    request = json.loads(Path(request_path).read_text())
    if (request['tag'], request['source_commit'], request['source_tree']) != (TAG, SOURCE, TREE):
        raise ValueError('Request is outside the frozen alpha.2.1 contract')
    if git('rev-parse', SOURCE + '^{tree}').decode().strip() != TREE:
        raise ValueError('Source tree mismatch')
    names = git('ls-tree', '-r', '--name-only', SOURCE).decode().splitlines()
    if len(names) != 76:
        raise ValueError('Unexpected frozen snapshot membership')
    files = {}
    for name in names:
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or path.suffix.lower() in {'.docx', '.pdf', '.svg', '.html', '.zip'}:
            raise ValueError('Unexpected path or raw document')
        data = git('show', SOURCE + ':' + name)
        data.decode('utf-8')
        if b'\x00' in data:
            raise ValueError('Unexpected binary input')
        files[name] = data
    results = {}
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        for name, content in files.items():
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        for checker in ['check_repository_language', 'check_bootstrap', 'check_model_import', 'check_requirements', 'check_source_support']:
            cmd = [sys.executable, str(root / 'tools' / (checker + '.py'))]
            if checker == 'check_repository_language':
                cmd += names
            run = subprocess.run(cmd, cwd=root, check=True, capture_output=True, text=True)
            result = json.loads(run.stdout)
            if checker == 'check_bootstrap':
                # Filesystem traversal order is not part of a check's meaning.
                result['checks'] = sorted(result['checks'])
            if result['status'] != 'PASS':
                raise ValueError('Frozen-source check failed: ' + checker)
            results[checker] = result
    checks = {'source_commit': SOURCE, 'source_tree': TREE, 'status': 'PASS',
              'scope': 'Frozen input/record/graph integrity only; not semantic acceptance', 'results': results}
    checks_bytes = encoded(checks)
    manifest = {'tag': TAG, 'source_commit': SOURCE, 'source_tree': TREE,
                'package_kind': 'candidate-baseline-prerelease', 'stable_semantic_release': False, 'doi': None,
                'scope': 'Controlled conceptual model, retrospective ORSD and qualified source/candidate import',
                'included_counts': {'concepts': 137, 'subject_domains': 20, 'foundations_layers': 1,
                                    'associations': 174, 'generalizations': 122, 'textual_constraints': 24,
                                    'needs': 48, 'cq_contracts': 38, 'source_records': 53,
                                    'concept_support_records': 137, 'related_work_labels': 19},
                'limits': ['candidate model; not semantically accepted', 'requirements satisfaction not_assessed',
                           'source qualifications inherited; related-work labels not reverified',
                           'diagram reconciliation and complete typed traceability pending',
                           'formal ontology and independent review absent', 'no DOI or stable semantic release',
                           'raw inputs and third-party full texts excluded', 'repository reuse license remains pending'],
                'check_results_sha256': digest(checks_bytes),
                'files': {name: digest(content) for name, content in sorted(files.items())}}
    manifest_bytes = encoded(manifest)
    files['PACKAGE-MANIFEST.json'] = manifest_bytes
    files['CHECK-RESULTS.json'] = checks_bytes
    files['SHA256SUMS'] = ''.join(digest(content) + '  ' + name + '\n' for name, content in sorted(files.items())).encode()
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, content in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    payload = stream.getvalue()
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        if archive.testzip() is not None or set(archive.namelist()) != set(files):
            raise ValueError('Archive membership/readback mismatch')
        if any(archive.read(name) != content for name, content in files.items()):
            raise ValueError('Archive byte mismatch')
    assets = {f'clariceptify-{TAG}-baseline.zip': payload,
              'PACKAGE-MANIFEST.json': manifest_bytes, 'CHECK-RESULTS.json': checks_bytes}
    assets['SHA256SUMS'] = ''.join(digest(content) + '  ' + name + '\n' for name, content in sorted(assets.items())).encode()
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    for name, content in assets.items():
        (out / name).write_bytes(content)
    return {'status': 'PASS', 'tag': TAG, 'source_commit': SOURCE, 'source_tree': TREE,
            'source_files': len(names), 'archive_members': len(files), 'checks': list(results),
            'assets': {name: digest(content) for name, content in assets.items()}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('request')
    parser.add_argument('output')
    args = parser.parse_args()
    print(json.dumps(build(args.request, args.output), indent=2))
