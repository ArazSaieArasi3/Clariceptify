"""Validate current review evidence without promoting historical protocol snapshots."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    def read(path):
        return yaml.safe_load((root / path).read_text())
    manifest = read('evidence/related-work/artifact-inputs.yaml')
    index = read('evidence/related-work/review-index.yaml')
    concepts = {row['id']: row for row in read('model/concepts.yaml')['records']}
    for binding in index['model_bindings']:
        concept = concepts[binding['concept_id']]
        if binding['label'] != concept['label_en'] or binding['definition_sha256'] != hashlib.sha256(concept['definition'].encode()).hexdigest():
            raise ValueError('Stale comparison target')
    for spec in manifest['artifacts']:
        report = json.loads((root / ('evaluation/related-work/artifacts/' + spec['id'] + '.json')).read_text())
        review = read('evidence/related-work/artifacts/' + spec['id'] + '.yaml')
        if report['source_sha256'] != spec['sha256'] or review['artifact_sha256'] != spec['sha256']:
            raise ValueError('Artifact source identity mismatch')
        evidence = review['count_evidence']
        if hashlib.sha256((root / evidence['path']).read_bytes()).hexdigest() != evidence['sha256']:
            raise ValueError('Changed inspection report')
        if review['counts'] != report['counts'] or report['counts']['local_named_owl_classes'] != len(report['local_named_class_iris']):
            raise ValueError('Unreconciled count populations')
        if report['counts']['inferred_classes'] is not None or report['reasoner_execution'] != 'NOT_EXECUTED':
            raise ValueError('Unperformed reasoning promoted')
        if set(review['selected_iri_locators']) != {row['iri'] for row in report['selected_axioms']}:
            raise ValueError('Missing axiom locator')
        if review['license']['source_redistributed'] or review['reuse']['source_imported_into_Clariceptify']:
            raise ValueError('Unexpected third-party redistribution or import')
    for id in ['DnS', 'cDnS', 'DULConceptualization', 'DUL']:
        record = read('evidence/related-work/reviews/' + id + '.yaml')
        if not all(row.get('locator') and row.get('observation') for row in record['observations']):
            raise ValueError('Missing source locator')
        if record['comparison']['model_change'] != 'NONE' or record['comparison']['novelty_priority'] != 'NOT_ASSESSED':
            raise ValueError('Review wave exceeds its scientific scope')
    if read('evidence/related-work/reviews/DUL.yaml')['access']['state'] != 'PARTIAL_REVIEW_ACCESS_GAP':
        raise ValueError('Unavailable chapter promoted to reviewed')
    if {row['issue'] for row in index['completed_deliverables']} != {68, 69, 71, 87, 89}:
        raise ValueError('Closure population changed')
    return {'status': 'PASS', 'paper_or_documentation_reviews': 3,
            'partial_literature_reviews': 1, 'artifact_inspections': 3,
            'closure_ready_deliverables': 5,
            'scope': 'Record identity, locators, typed count populations and missing-evidence boundaries; not independent scientific acceptance.'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
