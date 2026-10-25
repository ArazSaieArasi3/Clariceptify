"""Reproduce the CI-verified alpha.3 checkpoint without replacing older payloads."""
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
TAG = 'v0.1.0-alpha.3'
SOURCE = 'f4a3e233fc283c065a2c48297657878a4625d780'
TREE = '2bb9434358dcecce3a54c064462975dc09e3e604'
CI_RECEIPT_SHA = '97b811d89ccf64580ecd64eaf0393ab09444f27d080d3e8a9ada932e9bb42b99'
CHECKERS = ['check_repository_language', 'check_schemas', 'check_model_structure',
            'check_requirements', 'check_source_support', 'check_traceability', 'check_bootstrap']


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def digest(content):
    return hashlib.sha256(content).hexdigest()


def build(request_path, output):
    request = json.loads(Path(request_path).read_text())
    if (request['tag'], request['source_commit'], request['source_tree']) != (TAG, SOURCE, TREE):
        raise ValueError('Request outside the frozen alpha.3 contract')
    if git('rev-parse', SOURCE + '^{tree}').decode().strip() != TREE:
        raise ValueError('Frozen tree mismatch')
    ci_bytes = (ROOT / 'releases' / TAG / 'ci-readback.json').read_bytes()
    if digest(ci_bytes) != CI_RECEIPT_SHA or request['ci_readback_sha256'] != CI_RECEIPT_SHA:
        raise ValueError('Unreviewed CI receipt')
    ci = json.loads(ci_bytes)
    if ci['status'] != 'PASS' or ci['run_manifest']['status'] != 'PASS' or ci['source_fingerprint']['commit'] != SOURCE:
        raise ValueError('CI acceptance does not bind this source')
    if ci['source_fingerprint']['binding_state'] != 'clean_tracked_snapshot':
        raise ValueError('CI source was not a clean snapshot')
    names = git('ls-tree', '-r', '--name-only', SOURCE).decode().splitlines()
    if len(names) != 118:
        raise ValueError('Unexpected checkpoint membership')
    files = {}
    for name in names:
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or path.suffix.lower() in {'.docx', '.pdf', '.svg', '.html', '.zip'}:
            raise ValueError('Unexpected path or raw document')
        content = git('show', SOURCE + ':' + name)
        content.decode('utf-8')
        if b'\x00' in content:
            raise ValueError('Unexpected binary input')
        files[name] = content
    file_digests = {name: digest(content) for name, content in sorted(files.items())}
    if file_digests != ci['source_fingerprint']['files']:
        raise ValueError('Frozen files differ from actual CI inputs')
    results = {}
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        for name, content in files.items():
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        for checker in CHECKERS:
            command = [sys.executable, str(root / 'tools' / (checker + '.py'))]
            if checker == 'check_repository_language':
                command += names
            run = subprocess.run(command, cwd=root, check=True, capture_output=True, text=True, timeout=180)
            result = json.loads(run.stdout)
            if checker == 'check_bootstrap':
                result['checks'] = sorted(result['checks'])
            if result['status'] != 'PASS':
                raise ValueError('Frozen gate failed: ' + checker)
            if digest(encoded(result)) != ci['run_manifest']['report_sha256'][checker + '.json']:
                raise ValueError('Local/frozen gate result differs from actual CI: ' + checker)
            results[checker] = result
    checks_bytes = encoded({'status': 'PASS', 'source_commit': SOURCE, 'source_tree': TREE,
                            'scope': 'Frozen public integrity only; no semantic acceptance', 'results': results})
    manifest = {'tag': TAG, 'source_commit': SOURCE, 'source_tree': TREE,
                'package_kind': 'traceability-integrity-prerelease', 'stable_semantic_release': False, 'doi': None,
                'scope': 'Candidate model/ORSD/source baseline, scoped typed links and witnesses, bounded claims and public integrity/CI',
                'observed_record_counts': results['check_schemas']['counts'],
                'scoped_trace_edges': results['check_traceability']['edges'],
                'bounded_claims': results['check_traceability']['layers']['claim_register']['claims'],
                'ci_run_id': ci['api_run']['run_id'], 'ci_readback_sha256': CI_RECEIPT_SHA,
                'check_results_sha256': digest(checks_bytes),
                'builder_sha256': digest(Path(__file__).read_bytes()),
                'builder_location_note': 'Builder and publication receipt are maintained after the frozen input commit; identify this exact builder by its digest and publisher commit.',
                'limits': ['Candidate model; semantic adequacy and philosophical contribution not accepted',
                           'Requirements/witnesses unassessed; CQs unexecuted; support qualifications inherited',
                           'Scoped source/witness trace graph; not complete research-artifact coverage',
                           'Diagram and synchronized manuscript remain unreconciled',
                           'Formal ontology, relational projection and independent review absent',
                           'Raw documents/full texts excluded; reuse license/citation decisions pending',
                           'No stable semantic release or DOI'],
                'files': file_digests}
    manifest_bytes = encoded(manifest)
    files.update({'PACKAGE-MANIFEST.json': manifest_bytes, 'CHECK-RESULTS.json': checks_bytes,
                  'CI-READBACK.json': ci_bytes})
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
            raise ValueError('Archive bytes differ')
    assets = {f'clariceptify-{TAG}-traceability.zip': payload, 'PACKAGE-MANIFEST.json': manifest_bytes,
              'CHECK-RESULTS.json': checks_bytes, 'CI-READBACK.json': ci_bytes}
    assets['SHA256SUMS'] = ''.join(digest(content) + '  ' + name + '\n' for name, content in sorted(assets.items())).encode()
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    for name, content in assets.items():
        (out / name).write_bytes(content)
    return {'status': 'PASS', 'tag': TAG, 'source_commit': SOURCE, 'source_tree': TREE,
            'source_files': len(names), 'archive_members': len(files), 'ci_run_id': ci['api_run']['run_id'],
            'ci_gate_result_parity': 'all_seven_hashes_equal_actual_CI',
            'assets': {name: digest(content) for name, content in assets.items()}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('request')
    parser.add_argument('output')
    args = parser.parse_args()
    print(json.dumps(build(args.request, args.output), indent=2))
