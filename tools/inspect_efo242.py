"""Inspect the publisher EFO PDF and paper inventory without manufacturing OWL classes."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PDF_SHA = '8cf3372ac6bd19b88dfc15f07485695a6aab0f45d91d7864afef6f5f353729a6'
REVIEW_PATH = ROOT / 'evidence/related-work/deep-reviews/EFO/review.yaml'
SELECTED = [('F01', 'A2', 'K02', 'PDF p.15 / printed p.67'),
            ('F02', 'A4', 'K04', 'PDF p.16 / printed p.68'),
            ('F03', 'A9', 'K09', 'PDF p.16 / printed p.68'),
            ('F04', 'A11', 'K11', 'PDF p.17 / printed p.69'),
            ('F05', 'A12', 'K12', 'PDF p.17 / printed p.69'),
            ('F06', 'D1-D2', 'K13+K14', 'PDF p.17 / printed p.69'),
            ('F07', 'A14', 'K16', 'PDF p.17 / printed p.69'),
            ('F08', 'A15', 'K17', 'PDF p.17 / printed p.69')]


def inspect(pdf):
    data = pdf.read_bytes()
    if hashlib.sha256(data).hexdigest() != PDF_SHA:
        raise ValueError('PDF bytes differ from the publisher-reviewed identity')
    review_bytes = REVIEW_PATH.read_bytes()
    review = yaml.safe_load(review_bytes)
    if review['source']['sha256'] != PDF_SHA or review['status'] != 'REVIEW_COMPLETE':
        raise ValueError('Paper review is not bound to this exact PDF')
    info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
    pages = int(re.search(r'^Pages:\s*(\d+)', info, re.M).group(1))
    if pages != 21:
        raise ValueError('Unexpected publisher PDF pagination')
    text = subprocess.check_output(['pdftotext', '-f', '15', '-l', '17', '-layout', str(pdf), '-'], text=True)
    for anchor in ('A2', 'A4', 'A9', 'A11', 'A12', 'A14', 'A15', 'D1', 'D2',
                   'présentAt', 'existsAsSuch', 'existsInItself', 'object(y,x)', 'represents(x,y)'):
        if not re.search(r'(?<![\w])' + re.escape(anchor) + r'(?![\w])', text):
            raise ValueError(f'Printed formula anchor not extracted: {anchor}')
    figure = [x for x in review['catalog'] if x['statement'].startswith('FIGURE_CATEGORY:')]
    if len(figure) != 33 or len({x['id'] for x in figure}) != 33:
        raise ValueError('Paper figure population changed')
    by_key = {x['label']: x for x in review['commitments']}
    selected = []
    for identifier, label, review_id, locator in SELECTED:
        keys = [label] if label != 'D1-D2' else ['D1', 'D2']
        if any(key not in by_key for key in keys):
            raise ValueError('Paper commitment missing from deep review')
        selected.append({'id': identifier, 'printed_label': label, 'review_id': review_id,
                         'locator': locator, 'source_anchor_extracted': True,
                         'bounded_reading': ' '.join(by_key[key]['statement'] for key in keys)})
    return {
        'issue': 242, 'source_pdf_sha256': PDF_SHA,
        'source_url': 'https://periodicos.ufmg.br/index.php/advances-kr/article/view/59175/49600',
        'pdf_pages': pages, 'paper_review_sha256': hashlib.sha256(review_bytes).hexdigest(),
        'population': {'figure_category_labels': 33, 'paper_category_iri_count': None,
                       'executable_root': None, 'local_owl_classes': None,
                       'imported_owl_classes': None, 'referenced_owl_classes': None,
                       'deprecated_owl_classes': None, 'inferred_owl_classes': None},
        'figure_categories': [{'paper_id': x['id'], 'label': x['label'],
                               'attributed_paraphrase': x['statement'].split(': ', 1)[1],
                               'locator': 'Figure 1, PDF p.10 / printed p.62',
                               'owl_iri': None, 'owl_definition': None,
                               'formal_hierarchy': None, 'status': 'PAPER_FIGURE_LABEL_ONLY'} for x in figure],
        'selected_commitments': selected,
        'source_discrepancies': ['A4 accented présentAt versus presentAt',
                                 'A12 existsAsSuch versus surrounding existsInItself and D1-D2',
                                 'A11 inverse uniqueness is not uniqueness of object per concept',
                                 'A14/A15 mixed reference-status propagation is conditionally incompatible under normalized D1/D2'],
        'execution': 'PDF SHA and page count verified; formula anchors extracted by pdftotext; figure visually reviewed in deep dossier and in this review. No FOL parser, theorem prover, OWL profile or reasoner run.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--output', type=Path, default=ROOT / 'evaluation/related-work/efo242/paper-catalog.json')
    args = parser.parse_args()
    receipt = inspect(args.pdf)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'pdf_sha256': receipt['source_pdf_sha256'], 'pages': receipt['pdf_pages'],
                      'figure_labels': len(receipt['figure_categories']),
                      'selected': len(receipt['selected_commitments'])}, indent=2))
