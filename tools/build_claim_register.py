"""Record bounded claims and an explicitly unsynchronized manuscript binding."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
INPUT_REF = 'commit:09531fe2df12f3a68a2239f16228f0f0db621fb6'


def generate():
    bindings = {}

    def bind(path):
        bindings[path] = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        return path

    def read(path):
        bind(path)
        return yaml.safe_load((ROOT / path).read_text())

    concepts = read('model/concepts.yaml')['records']
    by_label = {row['label_en']: row['id'] for row in concepts}
    model_counts = {'concepts': len(concepts)}
    for name in ['domains', 'relations', 'generalizations', 'constraints']:
        model_counts[name] = len(read('model/' + name + '.yaml')['records'])
    links = read('evaluation/generated-links.json')
    witnesses = read('evaluation/requirement-witnesses.json')
    parity = read('traceability/migration/parity-report.yaml')
    sources = read('evidence/source-register.yaml')['records']
    support = read('evidence/concept-support.yaml')['records']
    for path in ['traceability/links.yaml', 'traceability/requirements-model.yaml',
                 'requirements/functional.yaml', 'requirements/quality.yaml',
                 'requirements/competency-questions.yaml', 'requirements/future.yaml',
                 'evaluation/source-support-integrity.json', 'evaluation/model-structure-report.json',
                 'docs/decisions/r1-scope.md', 'evidence/related-work/candidate-register.yaml']:
        bind(path)
    receipt = read('evaluation/baseline-preview-publication-alpha2-1.json')
    manifest = read('traceability/migration/source-manifest.yaml')
    integrity = read('traceability/migration/input-integrity.yaml')
    article = next(row for row in manifest['sources'] if row['id'] == 'SRC-ARTICLE')
    article_hash = next(row['sha256'] for row in integrity['records'] if row['source_id'] == 'SRC-ARTICLE')
    claims = [
        {'id': 'CLR-CL001', 'claim_class': 'recorded_observation', 'status': 'supported_within_scope',
         'text': 'The selected specification/ORSD projection is reproducible as the governed model, requirement, source and candidate-witness outputs.',
         'facts': {'compared_outputs': len(parity['compared_outputs']), 'model_record_counts': model_counts},
         'evidence_paths': ['traceability/migration/parity-report.yaml'],
         'boundary': 'Byte-identical extraction of the two frozen inputs only; not equivalence to the entire thesis or wider historical model.'},
        {'id': 'CLR-CL002', 'claim_class': 'recorded_observation', 'status': 'supported_within_scope',
         'text': 'The current project trace graph matches its declared structural/source/witness fields with resolvable endpoints and exact revision/digest bindings.',
         'facts': {'edges': links['edges'], 'link_types_used': len(links['by_type'])},
         'evidence_paths': ['traceability/links.yaml', 'evaluation/generated-links.json'],
         'boundary': 'A bounded generated projection and integrity result; not semantic sufficiency, satisfiability or complete research-graph coverage.'},
        {'id': 'CLR-CL003', 'claim_class': 'recorded_observation', 'status': 'supported_within_scope',
         'text': 'Retrospective ORSD contracts retain their original IDs and candidate witnesses without reporting satisfaction or computed answers.',
         'facts': {'fr_cq_pairs': witnesses['fr_cq_pairs'], 'quality_dispositions': witnesses['quality_dispositions'],
                   'future_pairs': witnesses['future_pairs'], 'satisfaction': witnesses['satisfaction'],
                   'cq_execution': witnesses['cq_execution'], 'answers': witnesses['answers']},
         'evidence_paths': ['traceability/requirements-model.yaml', 'evaluation/requirement-witnesses.json'],
         'boundary': 'Transfer/contract integrity only. Retrospective reconstruction is not prospective stakeholder agreement or empirical assessment.'},
        {'id': 'CLR-CL004', 'claim_class': 'recorded_observation', 'status': 'supported_within_scope',
         'text': 'Concept-source records preserve qualified input screening with explicit pending support.',
         'facts': {'source_records': len(sources), 'concept_support_records': len(support),
                   'D': sum(row['support_type'] == 'D' for row in support),
                   'B': sum(row['support_type'] == 'B' for row in support),
                   'P': sum(row['support_type'] == 'P' for row in support)},
         'evidence_paths': ['evidence/source-register.yaml', 'evidence/concept-support.yaml', 'evaluation/source-support-integrity.json'],
         'boundary': 'Inherited bibliography/screening qualifications; not fresh full-text review, independent source confirmation or typing approval.'},
        {'id': 'CLR-CL005', 'claim_class': 'proposed_interpretation', 'status': 'proposed_for_review',
         'text': 'The model is intended to make purposeful conceptualization inspectable by distinguishing episodes, conceptualizers, goals, perspectives and explicit conceptual artifacts.',
         'facts': {'candidate_concept_ids': [by_label[label] for label in
                   ['Conceptualization', 'Conceptualizer', 'Goal', 'Perspective', 'Conceptual Artifact']]},
         'evidence_paths': ['model/concepts.yaml', 'docs/decisions/r1-scope.md'],
         'boundary': 'Purpose and explicit representational distinctions, proposed for philosophical/domain review; not philosophical consensus or established ontological adequacy.'},
        {'id': 'CLR-CL006', 'claim_class': 'recorded_observation', 'status': 'supported_within_scope',
         'text': 'An engineering candidate-baseline prerelease is published with verified tag, source membership and public asset digests.',
         'facts': {'tag': receipt['tag'], 'source_commit': receipt['source_commit'], 'source_files': receipt['source_file_count']},
         'evidence_paths': ['evaluation/baseline-preview-publication-alpha2-1.json'],
         'boundary': 'Alpha.2.1 freezes the earlier import baseline; the later graph, witnesses and this register on main are outside that frozen package. No stable semantic release or DOI.'},
        {'id': 'CLR-CL007', 'claim_class': 'working_contribution', 'status': 'proposed_for_review',
         'text': 'A source-traced conceptual account intended to clarify conceptualization commitments and expose their relations to requirements, evidence and assessment.',
         'facts': {'comparison_state': 'pending_R2_critical_review'},
         'evidence_paths': ['docs/decisions/r1-scope.md', 'evidence/related-work/candidate-register.yaml'],
         'boundary': 'Working contribution wording only. Comparative gap, novelty, coverage, superiority and scientific priority require the planned critical reviews.'}]
    return {'schema_version': '0.1.0', 'asset_id': 'CLR-CLAIM-REGISTER', 'input_snapshot_ref': INPUT_REF,
            'status': 'bounded_working_claims_not_scientific_acceptance', 'input_file_sha256': dict(sorted(bindings.items())),
            'applicability_policy': 'A claim applies only to its recorded inputs and evidence scope. Changed relevant bytes require re-evaluation, not inherited PASS.',
            'claims': claims,
            'manuscript_binding': {'asset_id': 'CLR-MANUSCRIPT', 'working_title': 'An Ontology for Representing Conceptualization Knowledge',
                                   'source_id': 'SRC-ARTICLE', 'input_filename': article['filename'], 'recorded_revision': article['revision'],
                                   'inherited_input_sha256': article_hash,
                                   'current_public_manuscript': 'not_materialized', 'model_evidence_alignment': 'not_assessed',
                                   'figure_state': 'Input manifest records a figure-page placeholder; a reconciled current figure is not materialized.',
                                   'figure_state_verification': 'Inherited source-manifest record; draft layout not freshly inspected in this task.',
                                   'layout_target': 'IEEE conference; eight-page ceiling; reserved model-figure page',
                                   'public_article_upload': 'not_performed', 'doi': None,
                                   'next_binding_work': 'Reconcile figure and evidence first; rewrite/bind the manuscript in PUB-001 through PUB-008.'},
            'deferred_claims': ['novelty or first-of-kind priority', 'complete semantic adequacy or universal philosophical agreement',
                                'all-requirement satisfaction or executed CQs', 'independent expert acceptance',
                                'whole-model formal consistency or joint satisfiability', 'stable semantic release or issued DOI']}


if __name__ == '__main__':
    path = ROOT / 'docs/research/claim-register.yaml'
    path.parent.mkdir(parents=True, exist_ok=True)
    result = generate()
    path.write_text(yaml.safe_dump(result, sort_keys=False, allow_unicode=True))
    print(json.dumps({'status': 'PASS', 'claims': len(result['claims']), 'manuscript': result['manuscript_binding']['model_evidence_alignment']}))
