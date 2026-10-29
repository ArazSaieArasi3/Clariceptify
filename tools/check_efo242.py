"""Verify the EFO paper-only receipt and negative executable-artifact boundary."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    d = yaml.safe_load((root / 'evidence/related-work/artifacts/EFO.yaml').read_text())
    c = json.loads((root / d['population']['catalog']).read_text())
    review_path = root / 'evidence/related-work/deep-reviews/EFO/review.yaml'
    review = yaml.safe_load(review_path.read_text())
    assert d['issue'] == c['issue'] == 242
    assert d['identity']['pdf_sha256'] == c['source_pdf_sha256'] == review['source']['sha256']
    assert hashlib.sha256(review_path.read_bytes()).hexdigest() == c['paper_review_sha256']
    assert c['pdf_pages'] == review['source']['pdf_pages'] == 21
    labels = [x for x in review['catalog'] if x['statement'].startswith('FIGURE_CATEGORY:')]
    assert len(labels) == len(c['figure_categories']) == d['population']['paper_figure_category_labels'] == 33
    assert [(x['id'], x['label']) for x in labels] == [(x['paper_id'], x['label']) for x in c['figure_categories']]
    assert all(x['owl_iri'] is None and x['owl_definition'] is None and x['formal_hierarchy'] is None for x in c['figure_categories'])
    assert len(c['selected_commitments']) == d['population']['selected_formula_groups'] == 8
    assert [x['printed_label'] for x in c['selected_commitments']] == d['selected_commitments']['ids']
    assert all(x['source_anchor_extracted'] for x in c['selected_commitments'])
    assert all(d['population'][k] is None for k in ('selected_owl_root', 'local_owl_classes',
              'imported_owl_classes', 'referenced_owl_classes', 'deprecated_owl_classes',
              'inferred_owl_classes', 'direct_imports', 'unresolved_imports'))
    assert d['foundation']['formal_import'] == 'UNKNOWN_NO_EXECUTABLE_ROOT'
    assert d['decision']['accepted_equivalences'] == []
    assert all(x == 'NONE' for x in d['boundary'].values())
    assert all(d['execution'][key].startswith('NOT_EXECUTED') for key in
               ('formal_root_parse', 'owl_profile', 'fol_theorem_prover'))
    assert '(../../evidence/related-work/artifacts/EFO.md)' in (root / 'docs/research/corpus-access.md').read_text()
    return {'status': 'PASS', 'paper_figure_labels': 33, 'selected_formula_groups': 8,
            'owl_class_population': None}


if __name__ == '__main__':
    print(check())
