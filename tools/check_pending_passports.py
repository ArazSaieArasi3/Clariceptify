"""Integrity of bounded source passports; not automatic source-meaning verification."""
import argparse
import hashlib
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {1: ['CLR-C0005', 'CLR-C0011', 'CLR-C0035', 'CLR-C0038', 'CLR-C0076'],
            2: ['CLR-C0079', 'CLR-C0098', 'CLR-C0102', 'CLR-C0111', 'CLR-C0131']}

class PassportError(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise PassportError(message)

def read(path):
    return yaml.safe_load((ROOT / path).read_text())

def validate(report, batch):
    require(report['issue'] == 111 + batch, 'issue identity')
    require(report['task_id'] == f'R2-SRC-00{batch}', 'task identity')
    require(report['frozen_ids'] == EXPECTED[batch], 'frozen selection')
    require(report['status'] == 'BOUNDED_SOURCE_REVIEW_COMPLETE_WITH_OPEN_FINDINGS', 'review not semantic approval')
    require(report['semantic_acceptance'] == 'not_assessed' and report['model_changes'] == 'none', 'semantic gate')
    require(report['model_tree'] == '3e2d5b627af1b92cdb70c6bd7198868fa784e977', 'model tree')
    require(len(report['baseline_commit']) == 40, 'baseline ref')
    required = {'model/concepts.yaml', 'model/relations.yaml', 'model/generalizations.yaml',
                'model/constraints.yaml', 'evidence/concept-support.yaml', 'evidence/source-register.yaml',
                'evidence/related-work/review-protocol.yaml', 'docs/decisions/source-support-import.md'}
    require(required <= report['input_bindings'].keys(), 'input bindings')
    for path, digest in report['input_bindings'].items():
        require(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, f'stale input {path}')
    concepts = {r['id']: r for r in read('model/concepts.yaml')['records']}
    supports = {r['concept_id']: r for r in read('evidence/concept-support.yaml')['records']}
    sources = {s['id']: s for s in report['sources']}
    require(len(sources) == len(report['sources']), 'duplicate source')
    for source in sources.values():
        for field in ('title', 'authors', 'version_or_date', 'url', 'locator', 'access_scope',
                      'paraphrase', 'independence_lineage', 'license_copyright'):
            require(isinstance(source.get(field), str) and source[field].strip(), f'missing source {field}')
        require(source['url'].startswith('https://'), 'source URL')
    original_sources = {s.get('original_source_id') for s in sources.values()}
    rows = report['concepts']
    require([r['concept_id'] for r in rows] == EXPECTED[batch], 'five exact records')
    for i, row in enumerate(rows, 1):
        cid = row['concept_id']; concept = concepts[cid]; support = supports[cid]
        require(row['label'] == concept['label_en'], 'changed label')
        require(row['frozen_definition'] == concept['definition'], 'changed definition')
        require(row['frozen_stereotype'] == concept['ontouml_stereotype'], 'changed stereotype')
        require(row['source_locator'] == concept['source_locator'], 'changed provenance')
        require(row['original_support_record'] == support, 'changed original support')
        require(row['original_citations_inspected'] == support['source_ids'], 'lost original citations')
        require(set(support['source_ids']) <= original_sources, 'missing original source metadata')
        require(row['preserve_imported_support'] == support['support_type'] == 'P', 'support promotion')
        require(row['typing_approval'] == 'not_assessed', 'typing promotion')
        require(row['proposed_delta']['status'] == 'unapproved_research_only', 'proposal promoted')
        require(row['decision_route']['issue'] == 129 and row['decision_route']['status'] == 'awaiting_joint_user_decision', 'decision gate')
        require(row['finding_id'] == f'SRC{111 + batch}-F{i:02d}', 'finding identity')
        for field in ('uncertainty', 'next_decision', 'original_passage_status', 'overall_outcome'):
            require(row.get(field), f'missing {field}')
        require(len(row['clause_support']) >= 2, 'missing clause comparison')
        for clause in row['clause_support']:
            require(clause['status'] in {'supported', 'partial', 'not_verified', 'mismatch', 'local_policy_not_source_claim'}, 'unsupported status')
            require(set(clause['evidence']) <= sources.keys(), 'unknown source reference')
            if clause['status'] in {'supported', 'partial', 'mismatch'}:
                require(clause['evidence'], 'evidence missing for support/comparison')
    return len(rows)

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--batch', type=int, choices=[1, 2], required=True)
    batch = parser.parse_args().batch
    n = validate(read(f'evidence/passports/pending-batch-{batch}.yaml'), batch)
    print(f'PASS: batch {batch}, {n} source-passport integrity checks; source interpretation/typing not automatically validated')

if __name__ == '__main__':
    main()
