#!/usr/bin/env python3
"""Check CMO #245 evidence, complete selected glossary and optional private bytes."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

import yaml

from render_cmo245 import ROOT, catalog, render_catalog, render_review


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check(root=ROOT, archive=None):
    base = root / 'evidence/related-work'
    d = yaml.safe_load((base / 'artifacts/CMO.yaml').read_text())
    c = yaml.safe_load((base / 'artifacts/CMO-class-catalog.yaml').read_text())
    census = json.loads((base / 'deep-reviews/CMO/mirror-census.json').read_text())
    dossier_path = base / 'deep-reviews/CMO/review.yaml'
    dossier = yaml.safe_load(dossier_path.read_text())
    discovery_path = root / d['source']['discovery']
    discovery = json.loads(discovery_path.read_text())
    assert d['issue'] == c['issue'] == dossier['artifact']['issue'] == 245
    assert d['source']['work'] == c['work_id'] == dossier['work_id'] == 'CMO'
    assert d['source']['paper_sha256'] == dossier['source']['sha256']
    assert d['source']['mirror_sha256'] == census['source_sha256'] == discovery['mirror_acquisition']['sha256']
    assert d['source']['private_archive_sha256'] == discovery['retained_archive']['sha256']
    assert d['source']['mirror_commit'] == census['provenance']['commit']
    assert d['source']['mirror_git_blob_sha'] == census['provenance']['git_blob_sha']
    assert d['source']['declared_direct_imports'] == c['direct_imports'] == census['declared_import_iris']
    assert d['source']['original_author_executable_root'] is None
    assert d['source']['original_author_release_version'] is None
    assert not d['source']['global_absence_claim']
    assert d['source']['mirror_release_date'] is None
    assert d['source']['mirror_paper_fidelity'] == 'NOT_ESTABLISHED'
    assert c == catalog(root), 'Selected glossary or source constraint drift'
    assert (base / 'artifacts/CMO-class-catalog.md').read_text() == render_catalog(c)
    assert (base / 'artifacts/CMO.md').read_text() == render_review(d)
    assert len(c['classes']) == d['population']['selected_mirror_named_class_declarations'] == 12
    assert c['counts']['local_classes'] == d['population']['selected_mirror_local_named_classes'] == 7
    assert c['counts']['external_redeclarations'] == d['population']['selected_mirror_external_class_redeclarations'] == 5
    assert c['counts']['referenced_named_classes'] == 8
    assert c['counts']['referenced_local_classes'] == c['counts']['referenced_external_classes'] == 4
    assert c['counts']['local_source_comment_candidates'] == 6
    assert c['counts']['local_descriptive_seeAlso_without_comment'] == 1
    assert c['counts']['local_explicit_deprecated'] == 0
    assert c['counts']['imported_closure_classes'] is None and c['counts']['inferred_classes'] is None
    assert c['counts']['original_author_release_classes'] is None
    assert c['source_license'] == 'NOT_IDENTIFIED_IN_SELECTED_FILE'
    assert c['unresolved_imports'] == c['direct_imports'] and not c['imported_definitions_complete']
    assert len(d['checks']) == 8 and [x['id'] for x in d['checks']] == [f'T{i:02}' for i in range(1, 9)]
    assert all(x['locator'] and x['method'] and x['outcome'] for x in d['checks'])
    assert d['population']['selected_mirror_explicit_triples'] == census['explicit_triples'] == 147
    assert d['population']['selected_mirror_anonymous_restrictions'] == 4
    restrictions = []
    for row in census['classes']:
        for item in row['declarations_and_constraints']:
            for expression in item['object'].get('anonymous_expression', []):
                if expression['predicate'].endswith('#minQualifiedCardinality'):
                    restrictions.append((row['iri'], expression['object']['literal']))
    assert {name.rsplit('#', 1)[-1] for name, _ in restrictions} == {
        'Universal', 'UniversalClass', 'UniversalQuality', 'UniversalRelation'}
    assert all(n == '0' for _, n in restrictions)
    props = {p['iri']: p for p in census['object_properties']}
    ns = 'http://purl.org/twc/ontologies/cmo.owl#'
    assert ns + 'representedByType' not in props and ns + 'FiatEntity' not in {r['iri'] for r in census['classes']}
    universal = props[ns + 'representsUniversal']['declarations_and_constraints']
    assert any(x['object'].get('iri', '').endswith('#IrreflexiveProperty') for x in universal)
    represents = props[ns + 'represents']['declarations_and_constraints']
    assert not any(x['object'].get('iri', '').endswith('#IrreflexiveProperty') for x in represents)
    chain = props['http://www.w3.org/2004/02/skos/core#broaderTransitive']['declarations_and_constraints']
    assert any(x['predicate'].endswith('#propertyChainAxiom') for x in chain)
    assert d['foundation']['paper_edition'] is None and not d['foundation']['accepted_alignment']
    assert d['foundation']['mirror_bfo_formal_import'] is False
    assert all('bfo' not in iri.lower() for iri in d['source']['declared_direct_imports'])
    assert not d['decision']['accepted_equivalences']
    assert d['decision']['owner_status'] == 'OWNER_DECISION_REQUIRED'
    assert d['limits']['later_issues'] == [255, 126]
    model = yaml.safe_load((root / 'model/concepts.yaml').read_text())
    assert set(d['decision']['candidate_model_ids']) <= {r['id'] for r in model['records']}
    audit = yaml.safe_load((base / 'deep-reviews/source-audit.yaml').read_text())
    row = next(x for x in audit['records'] if x['id'] == 'CMO')
    assert row['class_coverage']['catalog_path'] == 'evidence/related-work/artifacts/CMO-class-catalog.yaml'
    assert row['class_coverage']['local_classes'] == 7
    assert row['class_coverage']['source_definition_candidates'] == 6
    assert row['class_coverage']['missing_source_definitions'] == 1
    assert row['technical_followup']['evidence'] == 'evidence/related-work/artifacts/CMO.yaml'
    assert row['next_issues'] == [255, 126]
    assert row['foundation']['edition'] is None
    assert all(d['limits'][k] == 'NONE' for k in ('model_change', 'requirements_change',
                                                  'fixtures_change', 'manuscript_change', 'release_change'))
    assert '(../../evidence/related-work/artifacts/CMO.md)' in (root / 'docs/research/corpus-access.md').read_text()
    raw = 'NOT_RUN_PRIVATE_ARCHIVE_OPTIONAL'
    if archive:
        from inspect_cmo_mirror import inspect
        content = Path(archive).read_bytes()
        assert digest(content) == d['source']['private_archive_sha256']
        with ZipFile(archive) as z:
            assert d['source']['private_member'] in z.namelist()
            source = z.read(d['source']['private_member'])
        assert digest(source) == d['source']['mirror_sha256']
        assert hashlib.sha1(b'blob ' + str(len(source)).encode() + b'\0' + source).hexdigest() == d['source']['mirror_git_blob_sha']
        # The private source is read only from the owner-accessible archive; never copied to public artifacts.
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmp:
            member = Path(tmp) / d['source']['private_member']
            member.write_bytes(source)
            assert inspect(member, d['source']['mirror_sha256']) == census
        raw = 'PASS_PRIVATE_ARCHIVE_AND_EXACT_CENSUS'
    return {'status': 'PASS', 'checks': len(d['checks']), 'local_classes': 7,
            'external_redeclarations': 5, 'imported_classes': None,
            'private_source': raw, 'reasoner': 'NOT_EXECUTED'}


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--archive', type=Path)
    args = p.parse_args()
    print(json.dumps(check(archive=args.archive), sort_keys=True))
