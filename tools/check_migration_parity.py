"""Re-extract authorized frozen inputs in isolation; never overwrite the model."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import shutil
import tempfile
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ['model/' + name + '.yaml' for name in
           ['concepts', 'domains', 'relations', 'generalizations', 'constraints']] + [
    'requirements/' + name + '.yaml' for name in
    ['functional', 'quality', 'competency-questions', 'future', 'scope-and-scenarios']] + [
    'evidence/source-register.yaml', 'evidence/concept-support.yaml', 'evidence/bibliography.md']
if (ROOT / 'traceability/requirements-model.yaml').exists():
    OUTPUTS.append('traceability/requirements-model.yaml')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def differences(current, reconstructed):
    return [{'path': name, 'current_sha256': sha(current / name),
             'reconstructed_sha256': sha(reconstructed / name),
             'status': 'identical' if (current / name).read_bytes() == (reconstructed / name).read_bytes() else 'different'}
            for name in OUTPUTS]


def reconstruct(spec, orsd, destination):
    expected = {row['source_id']: row['sha256'] for row in
                yaml.safe_load((ROOT / 'traceability/migration/input-integrity.yaml').read_text())['records']}
    for source_id, path in [('SRC-SPEC', spec), ('SRC-ORSD', orsd)]:
        if sha(path) != expected[source_id]:
            raise ValueError('Frozen input digest mismatch: ' + source_id)
    shutil.copytree(ROOT, destination, ignore=shutil.ignore_patterns('.git', '__pycache__'))
    for script, source in [('import_selected_model', spec), ('import_orsd', orsd), ('import_source_support', spec)]:
        descriptor = importlib.util.spec_from_file_location('isolated_' + script, ROOT / 'tools' / (script + '.py'))
        module = importlib.util.module_from_spec(descriptor)
        descriptor.loader.exec_module(module)
        module.ROOT = destination
        module.generate(source)
    if (ROOT / 'traceability/requirements-model.yaml').exists():
        descriptor = importlib.util.spec_from_file_location('isolated_witnesses', ROOT / 'tools/import_requirement_witnesses.py')
        module = importlib.util.module_from_spec(descriptor)
        descriptor.loader.exec_module(module)
        module.ROOT = destination
        payload = module.generate(orsd)
        (destination / 'traceability/requirements-model.yaml').write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True))


def check(spec, orsd):
    spec, orsd = Path(spec).resolve(), Path(orsd).resolve()
    before = {name: sha(ROOT / name) for name in OUTPUTS}
    with tempfile.TemporaryDirectory() as directory:
        temp = Path(directory) / 'reconstructed'
        reconstruct(spec, orsd, temp)
        parity = differences(ROOT, temp)
        if any(row['status'] != 'identical' for row in parity):
            raise ValueError('Reconstruction drift: ' + str([row['path'] for row in parity if row['status'] != 'identical']))
        # Exercise the detector against a plausible semantic change, without altering source files.
        path = temp / 'model/concepts.yaml'
        data = yaml.safe_load(path.read_text())
        data['records'][0]['definition'] += ' Altered reconstruction fixture.'
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
        if next(row['status'] for row in differences(ROOT, temp) if row['path'] == 'model/concepts.yaml') != 'different':
            raise AssertionError('Changed definition escaped parity detection')
        from docx import Document
        changed = Path(directory) / 'altered-valid-spec.docx'
        doc = Document(spec)
        doc.add_paragraph('Input boundary fixture.')
        doc.save(changed)
        try:
            reconstruct(changed, orsd, Path(directory) / 'rejected-output')
        except ValueError:
            pass
        else:
            raise AssertionError('Changed valid DOCX accepted')
        if (Path(directory) / 'rejected-output').exists():
            raise AssertionError('Rejected input created outputs')
    if before != {name: sha(ROOT / name) for name in OUTPUTS}:
        raise AssertionError('Parity check modified governed outputs')
    manifest = yaml.safe_load((ROOT / 'traceability/migration/source-manifest.yaml').read_text())
    inventory = []
    for source in manifest['sources']:
        source_id = source['id']
        if source_id in ['SRC-SPEC', 'SRC-ORSD']:
            disposition = 'reconstructed_selected_projection_byte_identical'
            verification = 'actual_source_bytes_rehashed_and_imports_replayed'
        elif source['access'] == 'identified_not_materialized_in_this_wave':
            disposition = 'identified_unmaterialized_input; no byte-parity claim'
            verification = 'not_verified'
        else:
            disposition = 'historical_or_consumer_input; raw redistribution excluded; not whole-model authority'
            verification = 'inherited_manifest_hash_only_in_this_check'
        inventory.append({'source_id': source_id, 'revision': source['revision'],
                          'disposition': disposition, 'verification': verification,
                          'raw_distribution': source['raw_distribution']})
    return {'schema_version': '0.1.0', 'task_id': 'R1-019.b', 'status': 'PASS_SCOPED',
            'scope': 'Selected specification/ORSD extraction parity and explicit migration dispositions; not semantic equivalence to all historical content',
            'inputs': {'SRC-SPEC': sha(spec), 'SRC-ORSD': sha(orsd)}, 'compared_outputs': parity,
            'source_inventory_dispositions': inventory,
            'intentional_projection_differences': [
                {'id': 'CLR-MIG-D001', 'difference': 'DOCX tables/paragraphs become controlled YAML and bibliography views.',
                 'disposition': 'accepted extraction/serialization change; all compared governed outputs are byte-identical to isolated re-extraction'},
                {'id': 'CLR-MIG-D002', 'difference': 'One source relationship table partitions into associations and directed generalizations.',
                 'disposition': 'preserve 174 association rows and 122 generalization rows, endpoints, multiplicities and locators; no extra partition axioms'},
                {'id': 'CLR-MIG-D003', 'difference': 'Input display names/reference numbers receive stable local record IDs.',
                 'disposition': 'controlled record-key allocation; not adjudicated historical identity or source replacement'},
                {'id': 'CLR-MIG-D004', 'difference': 'ORSD table 6 contains 30 candidate witness rows not in the original requirements import.',
                 'disposition': ('resolved by #34 in traceability/requirements-model.yaml; candidates remain unassessed'
                                 if (ROOT / 'traceability/requirements-model.yaml').exists()
                                 else 'explicit follow-up #34; missing witness links do not establish unsatisfied or satisfied needs')},
                {'id': 'CLR-MIG-D005', 'difference': 'ORSD table 9 repeats the 21 domain vocabulary views.',
                 'disposition': 'secondary ORSD representation; model/domain and membership authority remains the selected specification; not a second editor'},
                {'id': 'CLR-MIG-D006', 'difference': 'Stage-1 support was imported from the actual specification, not the separate JSON bytes.',
                 'disposition': 'representation decision retained; separate JSON byte parity remains not_verified'},
                {'id': 'CLR-MIG-D007', 'difference': 'Older core/wider inventory and their previous assessments are not copied wholesale.',
                 'disposition': 'deliberate scope exclusion; candidate lineage and unselected records remain in the migration ledger; no old PASS inheritance'},
                {'id': 'CLR-MIG-D008', 'difference': 'Diagram, atlas, raw documents and synchronized manuscript are not published model authority.',
                 'disposition': 'raw inputs excluded; diagram approval/reconciliation #41/#42 and later outputs remain pending'},
                {'id': 'CLR-MIG-D009', 'difference': 'Engineering schemas, metadata, trace links and release controls are new local artifacts.',
                 'disposition': 'explicit project metadata; not additional conceptualization classes or a semantic expansion'}],
            'input_counts_not_permanent_invariants': {'concepts': 137, 'subject_domains': 20, 'foundations_layers': 1,
                                                     'associations': 174, 'generalizations': 122, 'textual_constraints': 24,
                                                     'needs': 48, 'cq_contracts': 38, 'references': 53, 'support_records': 137},
            'negative_cases': ['modified reconstructed definition detected', 'changed valid DOCX rejected before output creation'],
            'governed_outputs_unchanged': True, 'upstream_edits': False, 'canonical_ownership_handover': 'not_completed',
            'limits': ['Only the selected frozen projection is re-extracted; full historical/thesis equivalence is not asserted.',
                       'No fresh source full-text verification, semantic adequacy, requirement satisfaction or expert approval.',
                       'Missing inputs, candidate lineage and deferred witness/diagram work remain explicit.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--spec', required=True)
    parser.add_argument('--orsd', required=True)
    parser.add_argument('--output', default=str(ROOT / 'traceability/migration/parity-report.yaml'))
    args = parser.parse_args()
    report = check(args.spec, args.orsd)
    Path(args.output).write_text(yaml.safe_dump(report, sort_keys=False, allow_unicode=True))
    print(json.dumps({'status': report['status'], 'outputs_byte_identical': len(report['compared_outputs']),
                      'dispositions': len(report['intentional_projection_differences']),
                      'source_inventory': len(report['source_inventory_dispositions'])}))
