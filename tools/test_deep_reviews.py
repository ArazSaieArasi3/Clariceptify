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


if __name__ == '__main__':
    unittest.main()
