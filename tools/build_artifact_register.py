"""Snapshot governed artifact identities; paths are locators, not identities."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REF = 'c5db7525fa3989fce292c6961e686dc4f25c9314'

# Keep these identifiers when a locator changes. Do not derive identity from paths.
FAMILIES = {
    'CLR-MODEL': ('conceptual-model', 'model', [
        ('CLR-MODEL-CONCEPT', 'model/concepts.yaml'),
        ('CLR-MODEL-DOMAIN', 'model/domains.yaml'),
        ('CLR-MODEL-RELATION', 'model/relations.yaml'),
        ('CLR-MODEL-GENERALIZATION', 'model/generalizations.yaml'),
        ('CLR-MODEL-CONSTRAINT', 'model/constraints.yaml')]),
    'CLR-ORSD': ('requirements', 'requirements', [
        ('CLR-ORSD-FR', 'requirements/functional.yaml'),
        ('CLR-ORSD-QR', 'requirements/quality.yaml'),
        ('CLR-ORSD-CQ', 'requirements/competency-questions.yaml'),
        ('CLR-ORSD-FUTURE', 'requirements/future.yaml'),
        ('CLR-ORSD-SCOPE', 'requirements/scope-and-scenarios.yaml')]),
    'CLR-SOURCES': ('source-evidence', 'evidence', [
        ('CLR-SOURCE-REGISTER', 'evidence/source-register.yaml'),
        ('CLR-CONCEPT-SUPPORT', 'evidence/concept-support.yaml'),
        ('CLR-BIBLIOGRAPHY', 'evidence/bibliography.md'),
        ('CLR-RELATED-CANDIDATES', 'evidence/related-work/candidate-register.yaml')]),
    'CLR-MIGRATION': ('migration', 'traceability', [
        ('CLR-MIGRATION-LEDGER', 'traceability/migration/entity-ledger.yaml'),
        ('CLR-INPUT-MANIFEST', 'traceability/migration/source-manifest.yaml'),
        ('CLR-INPUT-INTEGRITY', 'traceability/migration/input-integrity.yaml')]),
    'CLR-DOC-REPO': ('documentation', 'docs', [
        ('CLR-DOC-AUTHORITY', 'docs/decisions/artifact-authority.md'),
        ('CLR-DOC-VERSIONS', 'docs/decisions/artifact-versioning.md'),
        ('CLR-DOC-RELEASE-POLICY', 'docs/decisions/release-policy.md'),
        ('CLR-DOC-R1-SCOPE', 'docs/decisions/r1-scope.md')]),
    'CLR-EVALUATION': ('evaluation', 'evaluation', [
        ('CLR-EVAL-MODEL-IMPORT', 'evaluation/model-import-report.json'),
        ('CLR-EVAL-MODEL-STRUCTURE', 'evaluation/model-structure-report.json'),
        ('CLR-EVAL-REQUIREMENTS', 'evaluation/requirements-integrity.json'),
        ('CLR-EVAL-SOURCE-SUPPORT', 'evaluation/source-support-integrity.json'),
        ('CLR-EVAL-RELATED-REGISTRATION', 'evaluation/related-work-registration.json'),
        ('CLR-EVAL-ALPHA2-READBACK', 'evaluation/baseline-preview-publication.json'),
        ('CLR-EVAL-ALPHA2-1-BUILD', 'evaluation/baseline-preview-build-alpha2-1.json')])
}


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def sha(data):
    return hashlib.sha256(data).hexdigest()


def snapshot(ref=DEFAULT_REF):
    commit = git('rev-parse', ref + '^{commit}').decode().strip()
    records = []
    for family_id, (kind, authority, members) in FAMILIES.items():
        fingerprints = {}
        for asset_id, path in members:
            data = git('show', commit + ':' + path)
            fingerprints[path] = sha(data)
            parsed = yaml.safe_load(data) if path.endswith('.yaml') else {}
            if isinstance(parsed, dict) and path.startswith('model/'):
                if parsed['asset_id'] != asset_id:
                    raise ValueError('Declared model asset identity drift: ' + path)
            revision = (parsed.get('model_revision') or parsed.get('input_revision')) if isinstance(parsed, dict) else None
            records.append({'asset_id': asset_id, 'kind': 'model-registry' if path.startswith('model/') else kind,
                            'owner': 'ArazSaieArasi3/Clariceptify:' + authority,
                            'status': 'imported_candidate' if path.startswith('model/') else 'recorded_baseline',
                            'location_kind': 'file', 'location': path, 'component_ids': [],
                            'version': {'revision': revision or 'storage-snapshot', 'semantic_version': None,
                                        'source_ref': 'commit:' + commit, 'content_sha256': fingerprints[path],
                                        'fingerprint_scheme': 'sha256-file'},
                            'applicability': 'Storage revision only. Semantic acceptance and evaluation applicability require their own evidence.'})
        combined = sha(json.dumps(fingerprints, sort_keys=True, separators=(',', ':')).encode())
        records.append({'asset_id': family_id, 'kind': kind,
                        'owner': 'ArazSaieArasi3/Clariceptify:' + authority,
                        'status': 'candidate_collection', 'location_kind': 'collection', 'location': None,
                        'component_ids': [asset_id for asset_id, _ in members],
                        'version': {'revision': 'input-r1-rev1' if family_id == 'CLR-MODEL' else 'storage-snapshot',
                                    'semantic_version': None, 'source_ref': 'commit:' + commit,
                                    'content_sha256': combined, 'fingerprint_scheme': 'sha256-path-digest-map'},
                        'applicability': 'Composition fingerprint; not a semantic release number or inherited assessment.'})
    for asset_id, kind, status in [
            ('CLR-FIG-FULL', 'diagram', 'not_materialized'),
            ('CLR-DOC-SPEC', 'documentation', 'not_generated'),
            ('CLR-MANUSCRIPT', 'manuscript', 'external_draft_not_distributed'),
            ('CLR-ONTOLOGY-FORMAL', 'formal-ontology', 'absent'),
            ('CLR-RDB', 'relational-projection', 'absent')]:
        records.append({'asset_id': asset_id, 'kind': kind,
                        'owner': 'ArazSaieArasi3/Clariceptify:' + kind, 'status': status,
                        'location_kind': 'unavailable', 'location': None, 'component_ids': [],
                        'version': {'revision': None, 'semantic_version': None, 'source_ref': None,
                                    'content_sha256': None, 'fingerprint_scheme': 'not_available'},
                        'applicability': ('Draft input SRC-ARTICLE and its inherited digest remain in the input manifest; no current synchronized manuscript is materialized here.'
                                          if kind == 'manuscript' else 'Unavailable at this storage snapshot; do not infer implementation or acceptance.')})
    receipt_path = ROOT / 'evaluation/baseline-preview-publication-alpha2-1.json'
    receipt_bytes = receipt_path.read_bytes()
    receipt = json.loads(receipt_bytes)
    if receipt['status'] != 'PASS' or receipt['tag'] != 'v0.1.0-alpha.2.1':
        raise ValueError('Verified package receipt required')
    package = next(item for item in receipt['assets'] if item['name'].endswith('.zip'))
    records.append({'asset_id': 'CLR-PACKAGE', 'kind': 'release-package',
                    'owner': 'ArazSaieArasi3/Clariceptify:releases', 'status': 'published_prerelease',
                    'location_kind': 'external_asset', 'location': package['url'], 'component_ids': [],
                    'version': {'revision': receipt['tag'], 'semantic_version': None,
                                'source_ref': 'tag:' + receipt['tag'],
                                'content_sha256': package['digest'].removeprefix('sha256:'),
                                'fingerprint_scheme': 'sha256-download'},
                    'applicability': 'Published engineering package, distinct from model semantic acceptance; exact source membership is in its manifest.'})
    return {'schema_version': '0.1.0', 'asset_id': 'CLR-TRACE-ARTIFACTS', 'snapshot_ref': 'commit:' + commit,
            'auxiliary_inputs': [{'path': str(receipt_path.relative_to(ROOT)), 'sha256': sha(receipt_bytes)}],
            'authority': 'Project artifact metadata, distinct from the modeled conceptualization classes.',
            'identity_policy': 'Stable asset IDs survive locator changes. Family membership and new/retired artifacts require explicit disposition.',
            'fingerprint_policy': 'File SHA-256 hashes raw stored bytes. Collection SHA-256 hashes UTF-8 JSON of the sorted path-to-digest map using compact separators. It is a revision fingerprint, not an entity identifier.',
            'self_binding': 'This register and its new schema/checker are versioned by their containing commit and later package manifest; they are excluded from their own frozen input fingerprint to avoid recursion.',
            'package_binding': 'Engineering package revisions are tracked separately in releases/ requests and evaluation/*publication*.json; CLR-PACKAGE is not the model semantic version.',
            'records': sorted(records, key=lambda row: row['asset_id'])}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ref', default=DEFAULT_REF)
    parser.add_argument('--output', default=str(ROOT / 'traceability/artifacts.yaml'))
    args = parser.parse_args()
    result = snapshot(args.ref)
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(result, sort_keys=False, allow_unicode=True))
    print(json.dumps({'status': 'PASS', 'records': len(result['records']), 'snapshot_ref': result['snapshot_ref']}))
