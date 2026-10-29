"""Check source-audit coverage and glossary provenance, without semantic acceptance."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import yaml
from render_source_audit import ROOT, render_audit, render_catalog


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def retained_source_digests(root):
    manifests = ['artifact-inputs.yaml', 'corpus/lmm-inputs.yaml',
                 'corpus/cdns2008-inputs.yaml', 'corpus/emotions2015-inputs.yaml']
    return {row['sha256'] for name in manifests
            for row in yaml.safe_load(
                (root / 'evidence/related-work' / name).read_text())['artifacts']}


def validate_audit(audit, expected_ids):
    rows = audit['records']
    if len(rows) != len(expected_ids) or {r['id'] for r in rows} != set(expected_ids):
        raise ValueError('Incomplete or duplicate source-audit population')
    discovery = {r['id'] for r in audit['discovery_attempts']}
    for row in rows:
        repo = row['repository']
        if repo['global_absence_claim'] or 'DOES_NOT_EXIST' in repo['state']:
            raise ValueError('Bounded discovery promoted to global absence')
        if not set(repo['evidence']) <= discovery:
            raise ValueError('Unknown discovery evidence')
        if 'NOT_IDENTIFIED' in repo['state'] and not repo['evidence']:
            raise ValueError('Negative discovery without search evidence')
        f = row['foundation']
        if f['edition'] is not None and not f.get('edition_evidence'):
            raise ValueError('Unsupported foundation edition')
        if f['basis'] == 'UNKNOWN' and (f['family'] is not None or f['edition'] is not None or f['relation'] != 'UNKNOWN'):
            raise ValueError('Unknown foundation promoted')
        if not f['locator'] or not row['next_issues']:
            raise ValueError('Unbound source follow-up')
        c = row['class_coverage']
        if c['catalog_path'] is None and any(c[k] is not None for k in ['local_classes', 'source_definition_candidates', 'missing_source_definitions']):
            raise ValueError('Class count without complete selected glossary')
        if c['reasoner_execution'] != 'NOT_EXECUTED':
            raise ValueError('Audit promoted to semantic execution')
    if audit['boundary']['model_change'] != 'NONE' or audit['boundary']['semantic_acceptance'] != 'NOT_ASSESSED':
        raise ValueError('Source audit promoted to model acceptance')


def validate_catalog(catalog, censuses):
    classes = catalog['classes']
    if len({r['iri'] for r in classes}) != len(classes):
        raise ValueError('Duplicate class glossary IRI')
    for m in catalog['modules']:
        census = censuses[m['id']]
        if census['source_sha256'] != m['source_sha256']:
            raise ValueError('Glossary source substitution')
        declared = {r['iri'] for r in census['classes']}
        local = {x for x in declared if x.startswith(m['namespace'])}
        rows = [r for r in classes if r['module'] == m['id']]
        if {r['iri'] for r in rows} != local or len(rows) != len(local):
            raise ValueError('Incomplete local class glossary')
        if m['local_named_classes'] != len(local) or m['external_named_class_redeclarations'] != len(declared - local):
            raise ValueError('Local/external class population mismatch')
        if m['actual_imports'] != census['declared_import_iris']:
            raise ValueError('Glossary import substitution')
        for r in rows:
            definition = r['source_definition']
            paraphrase = r['reviewer_definition']
            if r['source_sha256'] != m['source_sha256'] or not r['constraint_ref']:
                raise ValueError('Unpinned class provenance')
            if definition['status'] == 'NOT_REPORTED_IN_SELECTED_SOURCE':
                if paraphrase['text'] is not None or paraphrase['basis'] != 'MISSING_SOURCE_DEFINITION' or definition['annotation_sha256'] is not None:
                    raise ValueError('Missing definition silently invented')
            elif definition['status'] == 'PRESENT_COMMENT_CANDIDATE':
                if (not paraphrase['text'] or paraphrase['basis'] != 'REVIEWER_PARAPHRASE' or
                        not re.fullmatch(r'[0-9a-f]{64}', definition['annotation_sha256'] or '')):
                    raise ValueError('Unbound definition paraphrase')
            else:
                raise ValueError('Unknown definition state')
            if definition['raw_text_public'] or definition['logical_sufficiency'] != 'NOT_INFERRED_FROM_COMMENT':
                raise ValueError('Comment promoted to logical definition')
    if {r['module'] for r in classes} != {m['id'] for m in catalog['modules']}:
        raise ValueError('Unknown class module')
    expected_counts = {'local_classes': len(classes),
                       'source_definition_candidates': sum(r['source_definition']['status'] == 'PRESENT_COMMENT_CANDIDATE' for r in classes),
                       'missing_source_definitions': sum(r['source_definition']['status'] == 'NOT_REPORTED_IN_SELECTED_SOURCE' for r in classes),
                       'reviewer_reconstructions': 0, 'inferred_classes': None}
    if catalog['counts'] != expected_counts:
        raise ValueError('Glossary definition population mismatch')
    if catalog['logical_inference'] != 'NOT_EXECUTED' or catalog['model_change'] != 'NONE':
        raise ValueError('Glossary promoted to semantic/model acceptance')
    imported = catalog['imported_glossary']
    allowed_import_states = {'PENDING_DEFINITION_GLOSSARY', 'NO_DECLARED_IMPORTS',
                             'ALL_SELECTED_MAPPED_IMPORT_CLASS_COMMENTS_ACCOUNTED_FOR',
                             'COMPLETE_IRI_ACCOUNTING_WITH_EXPLICIT_DEFINITION_GAPS',
                             'PINNED_DUL_GLOSSARY_ACCOUNTED_FOR_WITH_EXPLICIT_GAPS'}
    if imported['state'] not in allowed_import_states:
        raise ValueError('Unqualified imported definitions promoted')
    if imported.get('unique_external_classes_pending') and imported['state'] != 'PENDING_DEFINITION_GLOSSARY':
        raise ValueError('Pending imported definitions promoted')


def verify_raw(catalog, source_dir):
    from rdflib import Graph, OWL, RDF, RDFS, URIRef
    for m in catalog['modules']:
        path = source_dir / m['source_filename']
        if digest(path) != m['source_sha256']:
            raise ValueError('Retained raw source substitution')
        graph = Graph().parse(path, format='xml')
        local = {str(s) for s in graph.subjects(RDF.type, OWL.Class)
                 if isinstance(s, URIRef) and str(s).startswith(m['namespace'])}
        if local != {r['iri'] for r in catalog['classes'] if r['module'] == m['id']}:
            raise ValueError('Raw source/glossary population mismatch')
        for r in catalog['classes']:
            if r['module'] != m['id']:
                continue
            iri = URIRef(r['iri'])
            comments = sorted(str(x) for x in graph.objects(iri, RDFS.comment))
            expected = hashlib.sha256(json.dumps(comments, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest() if comments else None
            if expected != r['source_definition']['annotation_sha256']:
                raise ValueError('Changed raw definition annotation')
            if sorted(str(x) for x in graph.objects(iri, RDFS.subClassOf) if isinstance(x, URIRef)) != r['named_superclasses']:
                raise ValueError('Changed asserted class hierarchy')
            if sum(1 for _ in graph.objects(iri, OWL.equivalentClass)) != r['equivalent_expressions']:
                raise ValueError('Changed class equivalence population')


def check(root=ROOT, source_dir=None):
    from check_deep_reviews import validate_artifact_census
    base = root / 'evidence/related-work/deep-reviews'
    register = yaml.safe_load((base / 'register.yaml').read_text())
    audit = yaml.safe_load((base / 'source-audit.yaml').read_text())
    expected = [r['id'] for k in ['acquired_papers', 'waiting_for_owner',
                                'limited_evidence_papers', 'separate_document_tasks']
                for r in register.get(k, [])]
    validate_audit(audit, expected)
    if (base / 'source-audit.md').read_text() != render_audit(audit):
        raise ValueError('Stale source-audit reader')
    known_sources = retained_source_digests(root)
    summary = []
    for path in sorted(base.rglob('classes.yaml')):
        catalog = yaml.safe_load(path.read_text())
        censuses = {}
        for m in catalog['modules']:
            raw = root / m['census_path']
            if digest(raw) != m['census_sha256'] or m['source_sha256'] not in known_sources:
                raise ValueError('Unpinned class census')
            census = json.loads(raw.read_text())
            validate_artifact_census(census, census)
            gen = census['generator']
            if digest(root / gen['path']) != gen['sha256']:
                raise ValueError('Changed class census generator')
            censuses[m['id']] = census
        validate_catalog(catalog, censuses)
        if source_dir is not None:
            verify_raw(catalog, source_dir)
        if path.with_suffix('.md').read_text() != render_catalog(catalog):
            raise ValueError('Stale class glossary reader')
        summary.append({'work_id': catalog['work_id'], **catalog['counts']})
    by_path = {str(p.relative_to(root)): yaml.safe_load(p.read_text()) for p in base.rglob('classes.yaml')}
    dul_path = 'evidence/related-work/dul-class-catalog.yaml'
    if any(r['class_coverage']['catalog_path'] == dul_path for r in audit['records']):
        from check_dul_class_catalog import validate
        dul = yaml.safe_load((root / dul_path).read_text())
        if validate(dul)['status'] != 'PASS':
            raise ValueError('Invalid DUL complete glossary')
        by_path[dul_path] = {'counts': {'local_classes': dul['counts']['local_classes'],
            'source_definition_candidates': dul['counts']['classes_with_comment_candidates'],
            'missing_source_definitions': dul['counts']['classes_without_comment']}}
    for r in audit['records']:
        c = r['class_coverage']
        if c['catalog_path']:
            counts = by_path[c['catalog_path']]['counts']
            if any(c[k] != counts[k] for k in ['local_classes', 'source_definition_candidates', 'missing_source_definitions']):
                raise ValueError('Audit/glossary count disagreement')
    return {'status': 'PASS', 'source_records': len(expected), 'catalogs': summary,
            'raw_source_reconciliation': 'PASS' if source_dir is not None else 'NOT_RUN_RAW_SOURCES_PRIVATE',
            'scope': 'Exact declared class populations, definition availability and evidence boundaries; not semantic acceptance.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path)
    args = parser.parse_args()
    print(json.dumps(check(source_dir=args.source_dir), indent=2))
