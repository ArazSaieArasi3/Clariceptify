"""Adverse tests for unsupported review closure and evidence promotion."""
import copy
import json
import unittest
import yaml
from check_deep_reviews import ROOT, BASE, validate_dossier, validate_artifact_census


class ReviewBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.base = ROOT / BASE
        self.register = yaml.safe_load((self.base / 'register.yaml').read_text())
        self.entry = self.register['acquired_papers'][0]
        self.dimensions = yaml.safe_load((self.base / 'protocol.yaml').read_text())['dimensions']
        self.dossier = yaml.safe_load((self.base / self.entry['id'] / 'review.yaml').read_text())

    def reject(self, mutate):
        d = copy.deepcopy(self.dossier)
        mutate(d)
        with self.assertRaises(ValueError):
            validate_dossier(d, self.entry, self.dimensions)

    def test_source_substitution(self):
        self.reject(lambda d: d['source'].update(sha256='0' * 64))

    def test_incomplete_reading(self):
        self.reject(lambda d: d['coverage']['read_pages'].pop())

    def test_dangling_evidence(self):
        self.reject(lambda d: d['findings'][0].update(evidence=['MISSING']))

    def test_missing_shared_dimension(self):
        self.reject(lambda d: d['dimensions'].pop(next(iter(self.dimensions))))

    def test_model_adoption_promotion(self):
        self.reject(lambda d: d['boundary'].update(adoption='AUTOMATICALLY_APPLIED'))

    def test_false_executed_claim(self):
        self.reject(lambda d: d['findings'][0].update(basis='EXECUTED'))

    def test_unreviewed_unit(self):
        self.reject(lambda d: d['coverage']['units'][0].update(status='PENDING'))

    def test_unbound_artifact_task(self):
        self.reject(lambda d: d['artifact'].update(issue=999999))

    def cdns(self):
        entry = next(e for e in self.register['acquired_papers'] if e['id'] == 'cDnS2007')
        d = yaml.safe_load((self.base / 'cDnS2007/review.yaml').read_text())
        return d, entry

    def test_numbered_display_omission(self):
        d, entry = self.cdns()
        d['commitments'].pop(20)
        with self.assertRaisesRegex(ValueError, 'numbered-display ledger'):
            validate_dossier(d, entry, self.dimensions)

    def test_numbered_display_duplicate(self):
        d, entry = self.cdns()
        d['commitments'][1]['formula_number'] = 1
        with self.assertRaisesRegex(ValueError, 'numbered-display ledger'):
            validate_dossier(d, entry, self.dimensions)

    def reject_census(self, mutation, message):
        d, _ = self.cdns()
        binding = d['artifact']['census']
        report = json.loads((ROOT / binding['path']).read_text())
        mutation(report)
        with self.assertRaisesRegex(ValueError, message):
            validate_artifact_census(report, binding)

    def test_named_class_omission(self):
        self.reject_census(lambda r: r['classes'].pop(), 'named-entity inventory')

    def test_census_source_substitution(self):
        self.reject_census(lambda r: r.update(source_sha256='0' * 64), 'source substitution')

    def test_census_is_not_inference(self):
        self.reject_census(lambda r: r.update(inference_counts=123), 'promoted to inference')


class SourceAuditBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.base = ROOT / BASE
        self.audit = yaml.safe_load((self.base / 'source-audit.yaml').read_text())
        self.expected = [r['id'] for r in self.audit['records']]
        self.catalog = yaml.safe_load((self.base / 'LMM2008/classes.yaml').read_text())
        self.censuses = {m['id']: json.loads((ROOT / m['census_path']).read_text()) for m in self.catalog['modules']}

    def reject_catalog(self, mutation, pattern):
        from check_source_audit import validate_catalog
        mutation(self.catalog)
        with self.assertRaisesRegex(ValueError, pattern):
            validate_catalog(self.catalog, self.censuses)

    def test_complete_glossary_rejects_omitted_class(self):
        self.reject_catalog(lambda d: d['classes'].pop(), 'Incomplete local')

    def test_missing_definition_cannot_be_invented(self):
        def mutate(d):
            r = next(r for r in d['classes'] if r['reviewer_definition']['text'] is None)
            r['reviewer_definition']['text'] = 'A definition guessed from the name'
        self.reject_catalog(mutate, 'silently invented')

    def test_census_source_cannot_be_substituted(self):
        self.reject_catalog(lambda d: d['modules'][0].update(source_sha256='0' * 64), 'source substitution')

    def test_local_glossary_does_not_complete_imports(self):
        self.reject_catalog(lambda d: d['imported_glossary'].update(state='COMPLETE'), 'imported definitions promoted')

    def test_comment_is_not_logical_definition(self):
        self.reject_catalog(lambda d: d['classes'][0]['source_definition'].update(logical_sufficiency='PROVED'), 'logical definition')

    def test_search_failure_is_not_repository_nonexistence(self):
        from check_source_audit import validate_audit
        self.audit['records'][0]['repository']['global_absence_claim'] = True
        with self.assertRaisesRegex(ValueError, 'global absence'):
            validate_audit(self.audit, self.expected)

    def test_unversioned_foundation_cannot_become_bfo1(self):
        from check_source_audit import validate_audit
        r = next(r for r in self.audit['records'] if r['id'] == 'IAO2015')
        r['foundation']['edition'] = 'BFO1'
        with self.assertRaisesRegex(ValueError, 'Unsupported foundation edition'):
            validate_audit(self.audit, self.expected)

    def test_source_audit_cannot_omit_paper(self):
        from check_source_audit import validate_audit
        self.audit['records'].pop()
        with self.assertRaisesRegex(ValueError, 'source-audit population'):
            validate_audit(self.audit, self.expected)


class LmmCoverageTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / BASE / 'LMM2008'
        self.dossier = yaml.safe_load((base / 'review.yaml').read_text())
        self.diagrams = yaml.safe_load((base / 'diagrams.yaml').read_text())
        self.catalog = yaml.safe_load((base / 'classes.yaml').read_text())

    def test_missing_numbered_figure_rejected(self):
        from check_deep_reviews import validate_diagram_inventory
        self.diagrams['figures'].pop()
        with self.assertRaisesRegex(ValueError, 'diagram population'):
            validate_diagram_inventory(self.dossier, self.diagrams)

    def test_diagram_source_substitution_rejected(self):
        from check_deep_reviews import validate_diagram_inventory
        self.diagrams['source_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'source substitution'):
            validate_diagram_inventory(self.dossier, self.diagrams)

    def test_unindexed_figure_property_rejected(self):
        from check_deep_reviews import validate_diagram_inventory
        self.dossier['relation_index'].pop(0)
        with self.assertRaisesRegex(ValueError, 'diagram property'):
            validate_diagram_inventory(self.dossier, self.diagrams)

    def test_all_local_class_reviews_required(self):
        from check_deep_reviews import validate_class_review_coverage
        self.dossier['artifact']['class_reviews'].pop()
        with self.assertRaisesRegex(ValueError, 'omit or duplicate'):
            validate_class_review_coverage(self.dossier, self.catalog)


class DnsCoverageTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / BASE / 'DnS2003'
        self.dossier = yaml.safe_load((base / 'review.yaml').read_text())
        self.diagrams = yaml.safe_load((base / 'diagrams.yaml').read_text())
        binding = self.dossier['artifact']['dlp_intake']
        self.intake = json.loads((ROOT / binding['path']).read_text())

    def test_process_actions_cannot_be_promoted_to_classes(self):
        from check_deep_reviews import validate_diagram_inventory
        self.diagrams['class_diagram_numbers'].append(4)
        with self.assertRaisesRegex(ValueError, 'kind/class population'):
            validate_diagram_inventory(self.dossier, self.diagrams)

    def reject_intake(self, mutate, message):
        from check_deep_reviews import validate_dlp_intake
        mutate(self.intake)
        with self.assertRaisesRegex(ValueError, message):
            validate_dlp_intake(self.intake, self.dossier['artifact']['dlp_intake'])

    def test_later_archive_cannot_become_original_paper(self):
        self.reject_intake(lambda d: d.update(historical_2003_fidelity='IDENTICAL'), 'historical/semantic')

    def test_class_omission_cannot_complete_intake(self):
        def omit(d):
            m = next(m for m in d['modules'] if m['filename'] == 'ExtendedDnS.owl')
            m['local_definition_candidates'].pop()
        self.reject_intake(omit, 'class/comment inventory')

    def test_comment_availability_is_not_manual_definition(self):
        self.reject_intake(lambda d: d['modules'][0]['local_definition_candidates'][0].update(
            definition_review='COMPLETE'), 'manual definition')

    def test_missing_supplied_import_cannot_be_hidden(self):
        def add_import(d):
            m = next(m for m in d['modules'] if m['filename'] == 'ExtendedDnS.owl')
            m['declared_import_iris'].append('https://example.org/unavailable.owl')
        self.reject_intake(add_import, 'import closure')


class CmoCoverageTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / BASE / 'CMO'
        self.dossier = yaml.safe_load((base / 'review.yaml').read_text())
        self.census = json.loads((base / 'mirror-census.json').read_text())
        self.diagrams = yaml.safe_load((base / 'diagrams.yaml').read_text())
        self.query = json.loads((ROOT / self.dossier['artifact']['syntax_check']['path']).read_text())

    def test_mirror_is_not_original_release(self):
        from check_deep_reviews import validate_candidate_census
        self.census['provenance']['path_date_is_release_date'] = True
        with self.assertRaisesRegex(ValueError, 'original author release'):
            validate_candidate_census(self.dossier, self.census, self.dossier['artifact']['candidate_census'])

    def test_every_candidate_local_class_review_required(self):
        from check_deep_reviews import validate_candidate_census
        self.dossier['artifact']['class_reviews'].pop()
        with self.assertRaisesRegex(ValueError, 'candidate local class'):
            validate_candidate_census(self.dossier, self.census, self.dossier['artifact']['candidate_census'])

    def test_chart_labels_are_not_class_boxes(self):
        from check_deep_reviews import validate_diagram_inventory
        self.diagrams['class_diagram_numbers'].append(4)
        with self.assertRaisesRegex(ValueError, 'kind/class population'):
            validate_diagram_inventory(self.dossier, self.diagrams)

    def test_parser_rejection_cannot_become_endpoint_reproduction(self):
        from check_deep_reviews import validate_printed_query
        self.query['endpoint_execution'] = 'HINTS_RESULTS_REPRODUCED'
        with self.assertRaisesRegex(ValueError, 'historical query execution'):
            validate_printed_query(self.dossier, self.query)


class ComSourceBoundaryTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / BASE
        self.dossier = yaml.safe_load((base / 'COM2004/review.yaml').read_text())
        self.diagrams = yaml.safe_load((base / 'COM2004/diagrams.yaml').read_text())
        self.entry = next(r for r in yaml.safe_load((base / 'register.yaml').read_text())['acquired_papers']
                          if r['id'] == 'COM2004')
        self.dimensions = yaml.safe_load((base / 'protocol.yaml').read_text())['dimensions']

    def test_labeled_formula_omission_is_rejected(self):
        self.dossier['commitments'].pop(4)
        with self.assertRaisesRegex(ValueError, 'labeled-formula ledger'):
            validate_dossier(self.dossier, self.entry, self.dimensions)

    def test_silent_source_typo_repair_is_rejected(self):
        formula = next(r for r in self.dossier['commitments'] if r['formula_label'] == 'D14')
        formula['normalized_formula'] = formula['normalized_formula'].replace('PER(', 'PES(')
        with self.assertRaisesRegex(ValueError, 'silently repaired'):
            validate_dossier(self.dossier, self.entry, self.dimensions)

    def test_paper_taxonomy_is_not_a_machine_class_count(self):
        self.dossier['artifact']['machine_class_populations']['local'] = 50
        with self.assertRaisesRegex(ValueError, 'machine class population'):
            validate_dossier(self.dossier, self.entry, self.dimensions)

    def test_named_paper_category_omission_is_rejected(self):
        from check_deep_reviews import validate_diagram_inventory
        self.dossier['catalog'].pop(0)
        with self.assertRaisesRegex(ValueError, 'taxonomy category'):
            validate_diagram_inventory(self.dossier, self.diagrams)

    def test_missing_taxonomy_edge_is_rejected(self):
        from check_deep_reviews import validate_diagram_inventory
        self.diagrams['figures'][0]['edges'].pop()
        with self.assertRaisesRegex(ValueError, 'taxonomy edge'):
            validate_diagram_inventory(self.dossier, self.diagrams)


class BdiVariantBoundaryTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / BASE
        self.dossier = yaml.safe_load((base / 'BDI2020/review.yaml').read_text())
        self.entry = next(r for r in yaml.safe_load((base / 'register.yaml').read_text())['acquired_papers']
                          if r['id'] == 'BDI2020')
        self.dimensions = yaml.safe_load((base / 'protocol.yaml').read_text())['dimensions']

    def validate(self):
        validate_dossier(self.dossier, self.entry, self.dimensions)

    def test_unlabeled_expression_omission_is_rejected(self):
        self.dossier['commitments'].pop(16)
        with self.assertRaisesRegex(ValueError, 'labeled-formula ledger'):
            self.validate()

    def test_reductive_alternative_is_not_adopted_core(self):
        alternative = next(r for r in self.dossier['commitments'] if r['formula_label'] == 'REDUCE-INT-DES')
        alternative['variant'] = 'CORE_COMMON'
        with self.assertRaisesRegex(ValueError, 'promoted to named core'):
            self.validate()

    def test_only_must_not_silently_become_some(self):
        belief = next(r for r in self.dossier['commitments'] if r['source_label'] == 'BelO')
        belief['normalized_formula'] = belief['normalized_formula'].replace('only', 'some')
        with self.assertRaisesRegex(ValueError, 'changed into existence'):
            self.validate()

    def test_printed_tmin_must_not_be_silently_repaired(self):
        trigger = next(r for r in self.dossier['commitments'] if r['formula_label'] == 'TRIGGER-INT-PARTHOOD')
        trigger['normalized_formula'] = trigger['normalized_formula'].replace('Tmin', 'TRmin')
        with self.assertRaisesRegex(ValueError, 'Tmin silently repaired'):
            self.validate()

    def test_later_machine_class_count_cannot_be_substituted(self):
        self.dossier['artifact']['machine_class_populations']['local'] = 99
        with self.assertRaisesRegex(ValueError, 'machine population'):
            self.validate()


class FossrSourceBoundaryTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / BASE
        self.dossier = yaml.safe_load((base / 'BDI2026Preprint/review.yaml').read_text())
        self.entry = next(r for r in yaml.safe_load((base / 'register.yaml').read_text())['acquired_papers']
                          if r['id'] == 'BDI2026Preprint')
        self.dimensions = yaml.safe_load((base / 'protocol.yaml').read_text())['dimensions']

    def validate(self):
        validate_dossier(self.dossier, self.entry, self.dimensions)

    def test_recount_cannot_hide_omitted_numbered_source_formula(self):
        self.dossier['commitments'].pop(12)
        pop = self.dossier['labeled_formula_population']
        pop['labels'] = [r['formula_label'] for r in self.dossier['commitments']]
        pop['count'] = len(pop['labels'])
        with self.assertRaisesRegex(ValueError, 'numbered source population'):
            self.validate()

    def test_typing_only_does_not_silently_gain_a_trigger_witness(self):
        self.dossier['commitments'][27]['normalized_formula'] = (
            'MentalProcess SubClassOf (isTriggeredBy some MentalEntity)')
        with self.assertRaisesRegex(ValueError, 'quantification silently changed'):
            self.validate()

    def test_source_duplicate_does_not_become_a_new_axiom(self):
        self.dossier['commitments'][38]['normalized_formula'] = 'Belief SubClassOf (motivates only Desire)'
        with self.assertRaisesRegex(ValueError, 'printed duplicate silently changed'):
            self.validate()

    def test_figure_only_goal_process_cannot_disappear(self):
        self.dossier['figure_inventory']['class_boxes'].remove('GoalProcess')
        self.dossier['catalog'] = [r for r in self.dossier['catalog'] if r['label'] != 'GoalProcess']
        with self.assertRaisesRegex(ValueError, 'paper figure taxonomy'):
            self.validate()

    def test_alignment_import_is_not_silently_updated_to_current_core(self):
        alignment = next(r for r in self.dossier['artifact']['selected_files'] if r['path'].endswith('.rdf'))
        alignment['declared_import_iris'][1] = 'https://w3id.org/fossr/bdi/ontology/0.5/'
        with self.assertRaisesRegex(ValueError, 'version mismatch hidden'):
            self.validate()

    def test_preprint_doi_metadata_is_not_final_byte_equivalence(self):
        self.dossier['identity']['final_journal_byte_equivalence'] = 'VERIFIED'
        with self.assertRaisesRegex(ValueError, 'final journal equivalence'):
            self.validate()

    def test_reported_class_count_is_not_an_independent_census(self):
        self.dossier['artifact']['machine_class_populations']['local'] = 22
        with self.assertRaisesRegex(ValueError, 'paper counts promoted'):
            self.validate()


class CognitiveAtlasBoundaryTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / BASE
        self.dossier = yaml.safe_load((base / 'CognitiveAtlas2011/review.yaml').read_text())
        self.ledger = yaml.safe_load((base / 'CognitiveAtlas2011/figure-ledger.yaml').read_text())
        self.entry = next(r for r in yaml.safe_load((base / 'register.yaml').read_text())['acquired_papers']
                          if r['id'] == 'CognitiveAtlas2011')
        self.dimensions = yaml.safe_load((base / 'protocol.yaml').read_text())['dimensions']

    def reject_dossier(self, message):
        with self.assertRaisesRegex(ValueError, message):
            validate_dossier(self.dossier, self.entry, self.dimensions)

    def reject_figure(self, message):
        from check_deep_reviews import validate_cognitive_figure_ledger
        with self.assertRaisesRegex(ValueError, message):
            validate_cognitive_figure_ledger(self.dossier, self.ledger)

    def test_definition_presence_cannot_become_verified_adequacy(self):
        self.dossier['paper_population']['definition_adequacy'] = 'EXPERT_ACCEPTED'
        self.reject_dossier('historical status promoted')

    def test_historical_terms_are_not_parsed_classes(self):
        self.dossier['artifact']['machine_class_populations']['local'] = 904
        self.reject_dossier('terms promoted to machine')

    def test_v2_filename_does_not_mean_formal_version_two(self):
        self.dossier['artifact']['formal_version'] = '2'
        self.reject_dossier('filename promoted')

    def test_informative_citation_is_not_implemented_support(self):
        self.dossier['implementation_scope']['literature_relation'] = 'supports'
        self.reject_dossier('informative relation promoted')

    def test_signed_contrast_is_not_silently_reversed(self):
        self.ledger['figures'][1]['contrast_literal'] = '2-back minus 0-back'
        self.reject_figure('contrast silently reversed')

    def test_distinct_senses_are_not_silently_collapsed(self):
        self.ledger['figures'][2]['senses'] = ['behavioral inhibition']
        self.reject_figure('senses silently collapsed')

    def test_empirical_layers_are_not_class_hierarchy(self):
        self.ledger['figures'][3]['edge_kind'] = 'CLASS_HIERARCHY'
        self.reject_figure('illustration promoted')


if __name__ == '__main__':
    unittest.main()
