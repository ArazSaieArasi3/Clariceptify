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


class EmotionsOntoBoundaryTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / BASE
        self.dossier = yaml.safe_load((base / 'EmotionsOnto2014/review.yaml').read_text())
        self.ledger = yaml.safe_load((base / 'EmotionsOnto2014/figure-ledger.yaml').read_text())
        self.entry = next(r for r in yaml.safe_load((base / 'register.yaml').read_text())['acquired_papers']
                          if r['id'] == 'EmotionsOnto2014')
        self.dimensions = yaml.safe_load((base / 'protocol.yaml').read_text())['dimensions']

    def reject_dossier(self, message):
        with self.assertRaisesRegex(ValueError, message):
            validate_dossier(self.dossier, self.entry, self.dimensions)

    def reject_figure(self, message):
        from check_deep_reviews import validate_emotions_figure_ledger
        with self.assertRaisesRegex(ValueError, message):
            validate_emotions_figure_ledger(self.dossier, self.ledger)

    def test_positive_product_experience_is_not_recognition_accuracy(self):
        self.dossier['study_population']['recognition_accuracy'] = 1.0
        self.reject_dossier('responses promoted')

    def test_forced_choice_is_not_a_multilabel_rating(self):
        self.dossier['study_population']['choices_per_participant'] = 14
        self.reject_dossier('responses promoted')

    def test_paper_taxonomy_is_not_released_class_count(self):
        self.dossier['artifact']['machine_class_populations']['local'] = 39
        self.reject_dossier('original class population')

    def test_later_extension_does_not_prove_original_fidelity(self):
        self.dossier['artifact']['historical_fidelity'] = 'VERIFIED'
        self.reject_dossier('extension promoted')

    def test_context_arrows_are_not_silently_reversed(self):
        node = next(n for n in self.ledger['figures'][1]['nodes'] if n['label'] == 'dul:Situation')
        node['parents'] = ['dul:SocialObject']
        self.reject_figure('arrows silently repaired')

    def test_eight_application_labels_do_not_replace_fourteen_instrument_labels(self):
        self.ledger['figures'][4]['pleasant'].pop()
        self.reject_figure('questionnaire/result population')

    def test_altered_counts_cannot_pass_by_recounting_total(self):
        self.ledger['table']['counts']['admiration'] = 14
        self.dossier['study_population']['category_counts']['admiration'] = 14
        self.ledger['table']['total'] = 22
        self.reject_figure('questionnaire/result population')


class RepresentationBoundaryTests(unittest.TestCase):
    def setUp(self):
        folder = ROOT / BASE / 'CLR-RW-Representation'
        self.dossier = yaml.safe_load((folder / 'review.yaml').read_text())
        self.ledger = yaml.safe_load((folder / 'content-ledger.yaml').read_text())
        self.inspection = json.loads((ROOT / self.dossier['artifact']['reading_inspection']['path']).read_text())

    def reject(self, pattern):
        from check_deep_reviews import validate_representation_content
        with self.assertRaisesRegex(ValueError, pattern):
            validate_representation_content(self.dossier, self.ledger, self.inspection)

    def test_supplement_page_cannot_be_omitted(self):
        self.inspection['supplement']['read_pages'].pop()
        self.reject('reading coverage')

    def test_author_theorem_is_not_an_executed_proof(self):
        self.dossier['artifact']['theorem_proof_execution'] = 'PASS'
        self.reject('promoted to retained bytes')

    def test_retrieved_text_is_not_retained_pdf(self):
        self.inspection['supplement']['raw_pdf_sha256'] = 'a' * 64
        self.inspection['supplement']['raw_pdf_retained'] = True
        self.reject('promoted to retained bytes')

    def test_d11_free_variable_cannot_be_silently_repaired(self):
        record = next(r for r in self.dossier['commitments'] if r['formula_label'] == 'D11')
        record['normalized_formula'] = record['normalized_formula'].replace('exists o,r,p,p2 ', 'exists o,r,p,p2,f ')
        self.reject('silently repaired')

    def test_labeled_formula_cannot_be_omitted(self):
        self.dossier['commitments'].pop()
        self.reject('labeled formal population')

    def test_table_selection_cannot_be_normalized_to_one_level(self):
        self.ledger['tables'][0]['rows'][2]['checked'] = 'content'
        self.reject('selection/realization')

    def test_predicate_table_is_not_machine_class_census(self):
        self.dossier['artifact']['machine_class_populations']['local'] = 41
        self.reject('promoted to retained bytes')

    def test_supplement_c_table_row_cannot_be_lost(self):
        self.ledger['supplement_tables'][1]['predicate_names'].pop()
        self.reject('predicate population')


class DulChapterBoundaryTests(unittest.TestCase):
    def setUp(self):
        folder = ROOT / BASE / 'CLR-RW-DUL'
        self.dossier = yaml.safe_load((folder / 'review.yaml').read_text())
        self.ledger = yaml.safe_load((folder / 'content-ledger.yaml').read_text())

    def reject(self, pattern):
        from check_deep_reviews import validate_dul_figure_ledger
        with self.assertRaisesRegex(ValueError, pattern):
            validate_dul_figure_ledger(self.dossier, self.ledger)

    def test_book_scope_is_not_whole_book_reading(self):
        register = yaml.safe_load((ROOT / BASE / 'register.yaml').read_text())
        entry = next(r for r in register['acquired_papers'] if r['issue'] == 70)
        dimensions = yaml.safe_load((ROOT / BASE / 'protocol.yaml').read_text())['dimensions']
        self.dossier['coverage']['read_pages'] = list(range(1, 390))
        with self.assertRaisesRegex(ValueError, 'incomplete full-text reading'):
            validate_dossier(self.dossier, entry, dimensions)

    def test_time_indexed_illustration_is_not_native_dul_pattern(self):
        next(p for p in self.ledger['patterns'] if p['id'] == '5.3.13')['origin'] = 'EXTRACTED_FROM_DUL'
        self.reject('external illustration')

    def test_matrix_abstract_parthood_cannot_be_silently_repaired(self):
        self.ledger['figures'][0]['rows'][0]['pairs'].append(['Abstract (Region)', 'Abstract (Region)'])
        self.ledger['figures'][0]['rows'][1]['pairs'].pop()
        self.reject('silently repaired')

    def test_component_nontransitivity_is_not_intransitivity(self):
        next(p for p in self.ledger['patterns'] if p['id'] == '5.3.7.1')['logical_boundary']['intransitivity'] = 'ASSERTED'
        self.reject('intransitivity')

    def test_pattern_cannot_be_omitted(self):
        self.ledger['patterns'].pop()
        self.reject('subpattern source population')

    def test_diagram_is_not_machine_class_population(self):
        self.ledger['machine_class_count'] = 8
        self.reject('historical machine acceptance')

    def test_current_root_does_not_establish_historical_parity(self):
        self.dossier['artifact']['historical_axiom_fidelity'] = 'VERIFIED'
        self.reject('historical machine acceptance')

    def test_prose_commitments_are_not_printed_numbered_formulas(self):
        self.dossier['paper_formalization']['numbered_formula_count'] = 28
        self.reject('historical machine acceptance')


class O4oaBoundaryTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / BASE
        self.dossier = yaml.safe_load((base / 'CLR-RW-O4OA/review.yaml').read_text())
        self.ledger = yaml.safe_load((base / 'CLR-RW-O4OA/figures.yaml').read_text())
        self.entry = next(e for e in yaml.safe_load((base / 'register.yaml').read_text())['acquired_papers']
                          if e['id'] == 'CLR-RW-O4OA')
        self.dimensions = yaml.safe_load((base / 'protocol.yaml').read_text())['dimensions']

    def reject_dossier(self, text):
        with self.assertRaisesRegex(ValueError, text):
            validate_dossier(self.dossier, self.entry, self.dimensions)

    def reject_figure(self, text):
        from check_deep_reviews import validate_o4oa_figure_ledger
        with self.assertRaisesRegex(ValueError, text):
            validate_o4oa_figure_ledger(self.dossier, self.ledger)

    def test_dataset_concepts_are_not_machine_classes(self):
        self.dossier['artifact']['machine_class_populations']['local_named_classes'] = 161
        self.reject_dossier('case population promoted')

    def test_reported_modular_analysis_is_not_global_consistency(self):
        self.dossier['paper_formalization']['global_consistency'] = 'PASS'
        self.reject_dossier('reported modular analysis promoted')

    def test_future_axioms_are_not_a_printed_complete_formalization(self):
        self.dossier['paper_formalization']['printed_ocl_or_alloy_code'] = True
        self.reject_dossier('omitted formalism')

    def test_supporting_specification_is_not_deep_reviewed(self):
        self.dossier['artifact']['supporting_specification']['status'] = 'REVIEW_COMPLETE'
        self.reject_dossier('supporting specification')

    def test_core_hierarchy_cannot_be_silently_repaired(self):
        row = next(r for r in self.ledger['figures'][0]['generalizations'] if r['child'] == 'Core Ontology')
        row['child'], row['parent'] = row['parent'], row['child']
        self.reject_figure('Core/Domain source discrepancy')

    def test_mental_concept_is_not_the_term_role(self):
        row = next(r for r in self.ledger['figures'][1]['nodes'] if r['label'] == 'Concept (abstract object)')
        row['stereotype'] = 'kind'
        self.reject_figure('mental Concept collapsed')

    def test_relator_role_is_not_an_artifact_subclass(self):
        row = next(r for r in self.ledger['figures'][2]['generalizations'] if r['child'] == 'Ontological Reference')
        row['parent'] = 'Reference Ontology'
        self.reject_figure('relator-role identity level')

    def test_legal_reuse_chains_keep_role_overlap(self):
        row = next(r for r in self.ledger['figures'][6]['generalization_sets'] if 'Reused Ontology' in r['members'])
        row['disjoint'] = True
        self.reject_figure('legal reuse-role overlap')

    def test_membership_does_not_inherit_composition_profile(self):
        row = next(r for r in self.ledger['figures'][6]['relations'] if r['name'] == 'formedBy')
        row['stereotype'] = 'componentOf'
        self.reject_figure('profiles exchanged')

    def test_current_cq_mapping_is_not_solver_execution(self):
        from check_deep_reviews import validate_o4oa_cqs
        record = yaml.safe_load((ROOT / BASE / 'CLR-RW-O4OA/current-cqs.yaml').read_text())
        record['query_or_solver_execution'] = 'PASS'
        with self.assertRaisesRegex(ValueError, 'current CQ documentation promoted'):
            validate_o4oa_cqs(record)


class MentalNeedsBoundaryTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / BASE / 'CLR-RW-DOLCEMental'
        self.dossier = yaml.safe_load((base / 'review.yaml').read_text())
        self.ledger = yaml.safe_load((base / 'content-ledger.yaml').read_text())

    def reject(self, text):
        from check_deep_reviews import validate_mental_content_ledger
        with self.assertRaisesRegex(ValueError, text):
            validate_mental_content_ledger(self.dossier, self.ledger)

    def change_formula(self, label, value):
        next(r for r in self.dossier['commitments'] if r['formula_label'] == label)['normalized_formula'] = value
        next(r for r in self.ledger['formulas'] if r['label'] == label)['literal_ascii'] = value

    def test_incomplete_d6_cannot_be_silently_closed(self):
        formula = next(r for r in self.dossier['commitments'] if r['formula_label'] == 'd6')['normalized_formula']
        self.change_formula('d6', formula + ')))')
        self.reject('incomplete printed d6 silently repaired')

    def test_absolute_need_constraint_is_not_biconditional(self):
        self.change_formula('d12', 'need3(x,y,t) <-> egoal(x,y,t) & need0(x,y,t)')
        self.reject('one-way d12 promoted')

    def test_global_content_identity_is_not_only_per_time(self):
        self.change_formula('a6', "about1(x,y,t) & about1(x,y',t) -> y = y'")
        self.reject('global content identity weakened')

    def test_instrumental_need_does_not_require_mental_need(self):
        self.ledger['need_relation_inclusions']['need1_or_need2_implies_need0'] = True
        self.reject('overlapping uses promoted')

    def test_association_figure_is_not_a_class_hierarchy(self):
        self.ledger['figures'][0]['kind'] = 'CLASS_HIERARCHY'
        self.reject('association diagram promoted')

    def test_conditional_argument_is_not_a_full_theory_countermodel(self):
        self.dossier['paper_formalization']['full_theory_collapse'] = 'PROVED'
        self.reject('conditional critique or author/future claim promoted')

    def test_author_consistency_claim_is_not_independent_result(self):
        self.dossier['paper_formalization']['independent_consistency'] = 'PASS'
        self.reject('conditional critique or author/future claim promoted')

    def test_future_indexing_is_not_implemented(self):
        self.dossier['paper_formalization']['future_satisfier_indexing'] = 'IMPLEMENTED'
        self.reject('conditional critique or author/future claim promoted')

    def test_draft_file_is_not_exact_published_formula_identity(self):
        self.dossier['artifact']['paper_formula_identity'] = 'EXACTLY_EQUIVALENT'
        self.reject('selected draft inspection promoted')


class JournalAndLimitedSourceBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.base = ROOT / BASE
        self.register = yaml.safe_load((self.base / 'register.yaml').read_text())
        self.entry = next(r for r in self.register['acquired_papers'] if r['issue'] == 263)
        self.dossier = yaml.safe_load((self.base / self.entry['id'] / 'review.yaml').read_text())
        self.dimensions = yaml.safe_load((self.base / 'protocol.yaml').read_text())['dimensions']

    def reject_dossier(self, pattern):
        with self.assertRaisesRegex(ValueError, pattern):
            validate_dossier(self.dossier, self.entry, self.dimensions)

    def test_proceedings_authors_cannot_replace_journal_identity(self):
        self.dossier['identity']['authors'].extend(['Jos Lehmann', 'Carola Catenacci'])
        self.reject_dossier('journal/proceedings identity')

    def test_last_six_journal_displays_cannot_be_omitted(self):
        self.dossier['commitments'] = self.dossier['commitments'][:141]
        self.reject_dossier('numbered-display ledger')

    def test_critical_reading_does_not_certify_an_owl_profile(self):
        self.dossier['paper_formalization']['profile_execution'] = 'PASS'
        self.reject_dossier('reading promoted')

    def test_class_glossary_does_not_certify_original_release(self):
        self.dossier['artifact']['historical_fidelity'] = 'ESTABLISHED'
        self.reject_dossier('mapped journal artifacts promoted')

    def test_complete_figure_population_is_required(self):
        from check_deep_reviews import validate_journal_ledger
        ledger = yaml.safe_load((ROOT / self.dossier['journal_ledger']['path']).read_text())
        import_map = json.loads((ROOT / self.dossier['artifact']['import_map']['path']).read_text())
        ledger['figures'][1]['node_labels'].pop()
        with self.assertRaisesRegex(ValueError, 'journal content ledger'):
            validate_journal_ledger(self.dossier, ledger, import_map)

    def test_mapped_imports_do_not_verify_original_host_bytes(self):
        from check_deep_reviews import validate_journal_ledger
        ledger = yaml.safe_load((ROOT / self.dossier['journal_ledger']['path']).read_text())
        import_map = json.loads((ROOT / self.dossier['artifact']['import_map']['path']).read_text())
        import_map['original_host_import_bytes_verified'] = True
        with self.assertRaisesRegex(ValueError, 'import file map promoted'):
            validate_journal_ledger(self.dossier, ledger, import_map)

    def reject_limited(self, mutation):
        from check_deep_reviews import validate_limited_evidence_entry
        entry = copy.deepcopy(self.register['limited_evidence_papers'][0])
        mutation(entry)
        with self.assertRaisesRegex(ValueError, 'summary exception promoted'):
            validate_limited_evidence_entry(entry)

    def test_summary_is_not_full_paper_completion(self):
        self.reject_limited(lambda r: r.update(state='REVIEW_COMPLETE'))

    def test_owner_removed_pdf_gate_is_preserved(self):
        self.reject_limited(lambda r: r.update(full_text_required_for_current_scope=True))

    def test_missing_primary_hash_cannot_be_invented(self):
        self.reject_limited(lambda r: r.update(sha256='0' * 64))

    def test_owner_summary_cannot_be_called_primary_full_text(self):
        self.reject_limited(lambda r: r.update(evidence_basis='PRIMARY_FULL_TEXT'))


if __name__ == '__main__':
    unittest.main()
