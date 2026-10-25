#!/usr/bin/env python3
"""Positive-only fixture contract tests; downstream negative fixture is not required."""
import copy
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('fixture_check', ROOT / 'tools/check_conceptualization_fixtures.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class FixtureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for rel in checker.INPUT_PATHS | {'evaluation/fixtures/conceptualization-positive.yaml'}:
            dest = self.root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / rel, dest)

    def tearDown(self):
        self.temp.cleanup()

    def mutate(self, fn, negative=False):
        file = self.root / ('evaluation/fixtures/conceptualization-negative.yaml' if negative else 'evaluation/fixtures/conceptualization-positive.yaml')
        obj = yaml.safe_load(file.read_text())
        fn(obj)
        file.write_text(yaml.safe_dump(obj, sort_keys=False))

    def rejects(self):
        with self.assertRaises((ValueError, KeyError, TypeError)):
            checker.run(self.root, positive_only=True)

    def test_baseline(self):
        result = checker.run(self.root, positive_only=True)
        self.assertEqual(result['status'], 'PASS')
        self.assertEqual(len(result['fixture_results']), 1)
        self.assertEqual(result['scope'], 'positive_only')
        self.assertFalse((self.root / 'evaluation/fixtures/conceptualization-negative.yaml').exists())

    def test_unknown_concept(self):
        self.mutate(lambda x: x['nodes'][0].update(concept_id='CLR-C9999')); self.rejects()

    def test_malformed_node_id(self):
        self.mutate(lambda x: x['nodes'][0].update(id='../episode')); self.rejects()

    def test_malformed_fixture_id(self):
        self.mutate(lambda x: x.update(id='unexpected')); self.rejects()

    def test_malformed_relation_id(self):
        self.mutate(lambda x: x['edges'][0].update(relation_id='CLR-Rbad')); self.rejects()

    def test_duplicate_node(self):
        self.mutate(lambda x: x['nodes'].append(copy.deepcopy(x['nodes'][0]))); self.rejects()

    def test_missing_agent(self):
        self.mutate(lambda x: x['required_roles'].update(agent='absent')); self.rejects()

    def test_collapsed_intention_goal(self):
        self.mutate(lambda x: x['required_roles'].update(mental_state='goal')); self.rejects()

    def test_unknown_edge(self):
        self.mutate(lambda x: x['edges'][0].update(relation_id='CLR-R9999')); self.rejects()

    def test_missing_endpoint(self):
        self.mutate(lambda x: x['edges'][0].update(target='absent')); self.rejects()

    def test_wrong_endpoint_type(self):
        self.mutate(lambda x: x['edges'][0].update(target='goal')); self.rejects()

    def test_no_participation(self):
        self.mutate(lambda x: x.update(edges=[e for e in x['edges'] if e['relation_id'] != 'CLR-R0054'])); self.rejects()

    def test_no_subject(self):
        self.mutate(lambda x: x.update(edges=[e for e in x['edges'] if e['relation_id'] not in checker.SUBJECT_RELATIONS])); self.rejects()

    def test_no_perspective_bearer(self):
        self.mutate(lambda x: x.update(edges=[e for e in x['edges'] if e['relation_id'] != 'CLR-R0008'])); self.rejects()

    def test_duplicate_requirement_link(self):
        self.mutate(lambda x: x['requirement_links'].append(copy.deepcopy(x['requirement_links'][0]))); self.rejects()

    def test_wrong_cq_pair(self):
        self.mutate(lambda x: x['requirement_links'][0].update(cq_id='CQ-02')); self.rejects()

    def test_changed_input(self):
        f = self.root / 'model/concepts.yaml'; f.write_text(f.read_text() + '\n'); self.rejects()

    def test_missing_binding(self):
        self.mutate(lambda x: x['input_bindings'].pop()); self.rejects()

    def test_no_global_status_write(self):
        before = {p: checker.sha(self.root / p) for p in checker.INPUT_PATHS}
        checker.run(self.root, positive_only=True)
        self.assertEqual(before, {p: checker.sha(self.root / p) for p in checker.INPUT_PATHS})


if __name__ == '__main__':
    unittest.main()
