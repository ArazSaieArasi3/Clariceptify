#!/usr/bin/env python3
"""Validate retained-reference identities, not source truth or scientific review."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit
import yaml

EXPECTED = ['CLR-RW-EFO', 'CLR-RW-cDnS', 'CLR-RW-DULConceptualization', 'CLR-RW-DUL', 'CLR-RW-LMM', 'CLR-RW-Representation', 'CLR-RW-CMO', 'CLR-RW-O4OA', 'CLR-RW-COM', 'CLR-RW-IDA', 'CLR-RW-DnS', 'CLR-RW-OntoKADS', 'CLR-RW-BDI', 'CLR-RW-DOLCEMental', 'CLR-RW-IAO', 'CLR-RW-OntoLex', 'CLR-RW-SKOS', 'CLR-RW-EmotionsCognition', 'CLR-RW-CognitiveAtlas', 'CLR-RW-PleaEpistemic', 'CLR-RW-EpistemicReferential', 'CLR-RW-RealistMentalRepresentation', 'CLR-SRC0014', 'CLR-RW-ConceptsInContext']
SUPPLEMENT = set(EXPECTED[19:]) - {'CLR-SRC0014'}
PATHS = ['evidence/related-work/reference-crosswalk.yaml', 'evidence/related-work/supplemental-reference-register.yaml', 'evidence/related-work/reference-crosswalk.md']

def require(condition, message):
    if not condition:
        raise ValueError(message)

def check(root):
    def read(path):
        return yaml.safe_load((root / path).read_text())
    cross, supplement = read(PATHS[0]), read(PATHS[1])
    candidates = read('evidence/related-work/candidate-register.yaml')['records']
    sources = read('evidence/source-register.yaml')['records']
    candidate_ids = [r['candidate_id'] for r in candidates]
    source_ids = [r['id'] for r in sources]
    rows, added = cross['records'], supplement['records']
    require([r['reference_row'] for r in rows] == list(range(1, 25)), '24 ordered collection rows required')
    require([r['canonical_id'] for r in rows] == EXPECTED, 'canonical IDs changed or duplicated')
    require(set(EXPECTED[:19]) <= set(candidate_ids), 'original candidate identity missing')
    require(len(candidate_ids) == len(set(candidate_ids)), 'duplicate existing candidate ID')
    require(len(source_ids) == len(set(source_ids)), 'duplicate bibliography ID')
    require({'CLR-SRC0014', 'CLR-SRC0039'} <= set(source_ids), 'existing bibliography crosslinks missing')
    require(len(added) == 4 and {r['candidate_id'] for r in added} == SUPPLEMENT, 'exactly four supplementary identities required')
    require(not SUPPLEMENT.intersection(candidate_ids + source_ids), 'supplement duplicates existing ID')
    bibliography = ' '.join(r['citation_ieee_input'] for r in sources).casefold()
    require('10.46743/2160-3715/2022.5633' in next(r['citation_ieee_input'] for r in sources if r['id'] == 'CLR-SRC0014'), 'LION identity drift')
    require('https://www.w3.org/TR/skos-reference/' in next(r['citation_ieee_input'] for r in sources if r['id'] == 'CLR-SRC0039'), 'SKOS identity drift')
    for row in rows:
        expected_path = ('evidence/related-work/candidate-register.yaml' if row['canonical_id'] in EXPECTED[:19] else 'evidence/source-register.yaml' if row['canonical_id'] == 'CLR-SRC0014' else PATHS[1])
        require(row['register_path'] == expected_path and (root / expected_path).is_file(), 'wrong register path')
        require(row['bibliography_crosslinks'] == (['CLR-SRC0039'] if row['canonical_id'] == 'CLR-RW-SKOS' else []), 'crosslink changed or duplicated')
    urls = []
    for record in added:
        require(record['metadata_status'] == 'recovered_not_reverified' and record['access_status'] == 'not_checked', 'unverified metadata/access promoted')
        require(record['full_text_review'] == 'not_assessed' and record['review_evidence'] == [], 'unperformed review promoted')
        require(record['citation_ready'] is False and record['article_inclusion'] == 'not_decided' and record['paper_review_issue'] is None, 'invented citation/inclusion/task decision')
        require(record['recovered_label'].casefold() not in bibliography, 'supplement duplicates bibliography title')
        require(record['resources'], 'missing public source locator')
        for resource in record['resources']:
            url = resource['url']; parsed = urlsplit(url)
            require(parsed.scheme == 'https' and bool(parsed.hostname) and not parsed.username and not parsed.password, 'invalid public locator')
            require(parsed.hostname in {'doi.org', 'ceur-ws.org', 'hal.science'} and not parsed.query, 'private conversation/local locator')
            require(resource['locator_status'] == 'recovered_not_reverified', 'locator verification invented')
            require(url.casefold() not in bibliography, 'supplement duplicates bibliography URL')
            urls.append(url)
    require(len(urls) == 5 and len(set(urls)) == 5, 'supplement locator missing/duplicated')
    for path in PATHS:
        text = (root / path).read_text()
        require(not any('\u0600' <= c <= '\u06ff' for c in text), 'non-English repository text')
        require('chatgpt.com/' not in text and 'chat.openai.com/' not in text and '/workspace/' not in text, 'private provenance leaked')
    return {'result': 'PASS', 'collection_rows': 24, 'original_candidate_crosslinks': 19, 'existing_bibliography_only_identity': 1, 'supplementary_leads': 4, 'supplementary_public_locators': 5}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(check(args.root), sort_keys=True))
