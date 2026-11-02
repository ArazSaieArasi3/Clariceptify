"""Failure-boundary tests for selected finite graph queries; no semantic validation."""
import copy
import unittest
from unittest.mock import patch
from domain_review_checks import answers, graph, load, records, ReviewError, check

class DomainReviewChecks(unittest.TestCase):
    def setUp(self):
        self.c = records('model/concepts.yaml')
        self.r = records('model/relations.yaml')
        self.g = records('model/generalizations.yaml')
        self.report = load('evaluation/domain-adequacy/language.yaml')
        self.pos = load(self.report['scenarios']['positive']['locator'])
        self.neg = load(self.report['scenarios']['adverse']['locator'])
        self.q = self.report['selected_query']
    def test_whole_report(self):
        self.assertEqual(check('language',101,10,12)['status'],'PASS')
    def test_positive(self):
        self.assertEqual(len(answers(self.pos,self.q,self.c,self.r,self.g)),1)
    def test_wrong_language(self):
        self.assertEqual(answers(self.neg,self.q,self.c,self.r,self.g),[])
    def test_missing_each_required_edge(self):
        for i in range(len(self.pos['edges'])):
            fixture=copy.deepcopy(self.pos);fixture['edges'].pop(i)
            self.assertEqual(answers(fixture,self.q,self.c,self.r,self.g),[])
    def test_unknown_relation(self):
        self.pos['edges'][0]['relation_id']='UNKNOWN'
        with self.assertRaises(ReviewError):graph(self.pos,self.c,self.r,self.g)
    def test_unknown_endpoint(self):
        self.pos['edges'][0]['target']='UNKNOWN'
        with self.assertRaises(ReviewError):graph(self.pos,self.c,self.r,self.g)
    def test_duplicate_node(self):
        self.pos['nodes'].append(self.pos['nodes'][0])
        with self.assertRaises(ReviewError):graph(self.pos,self.c,self.r,self.g)
    def test_duplicate_edge(self):
        self.pos['edges'].append(self.pos['edges'][0])
        with self.assertRaises(ReviewError):graph(self.pos,self.c,self.r,self.g)
    def test_wrong_type(self):
        self.pos['nodes'][0]['concept_id']='CLR-C0066'
        with self.assertRaises(ReviewError):graph(self.pos,self.c,self.r,self.g)
    def test_unknown_anchor(self):
        self.q['anchors']['message']='UNKNOWN'
        with self.assertRaises(ReviewError):answers(self.pos,self.q,self.c,self.r,self.g)
    def test_unrelated_syntax_not_joined(self):
        self.neg['nodes'].append({'id':'unrelated_syntax','concept_id':'CLR-C0117'})
        self.neg['edges'].append({'relation_id':'CLR-R0099','source':'other_language','target':'unrelated_syntax'})
        self.assertEqual(answers(self.neg,self.q,self.c,self.r,self.g),[])
    def test_report_tampering(self):
        mutations = [
            lambda r: r['input_bindings'].__setitem__('model/concepts.yaml','0'*64),
            lambda r: r['concept_review'][0].__setitem__('definition','Changed definition'),
            lambda r: r.__setitem__('status','PASS'),
            lambda r: r['constraint_review'].__setitem__('CLR-SC0009','Changed constraint'),
        ]
        for mutate in mutations:
            report=copy.deepcopy(self.report);mutate(report)
            def altered(path):
                return report if path=='evaluation/domain-adequacy/language.yaml' else load(path)
            with patch('domain_review_checks.load',side_effect=altered):
                with self.assertRaises(ReviewError):check('language',101,10,12)
    def test_wrong_report_identity(self):
        with self.assertRaises(ReviewError):check('language',102,10,12)

if __name__=='__main__':unittest.main()
