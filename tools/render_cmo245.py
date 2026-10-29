#!/usr/bin/env python3
"""Render the bounded CMO candidate glossary and reader from retained evidence."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'evidence/related-work'
NAMESPACE = 'http://purl.org/twc/ontologies/cmo.owl#'
LINES = {
    'Quality': '124-128', 'Relation': '129-133', 'Type': '134-138',
    'Universal': '139-150', 'UniversalClass': '152-163',
    'UniversalQuality': '165-174', 'UniversalRelation': '176-186',
    'IAO_0000030': '122', 'Entity': '188',
    'IndependentContinuant': '190', 'Thing': '192', 'Concept': '194-195',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def catalog(root=ROOT):
    census_path = root / BASE / 'deep-reviews/CMO/mirror-census.json'
    review_path = root / BASE / 'deep-reviews/CMO/review.yaml'
    census = json.loads(census_path.read_text())
    review = yaml.safe_load(review_path.read_text())
    reviewed = {x['iri']: x for x in review['artifact']['class_reviews']}
    classes = []
    for item in census['classes']:
        iri = item['iri']
        name = iri.rsplit('#', 1)[-1].rsplit('/', 1)[-1]
        local = item['local']
        source = reviewed.get(iri)
        if local != (source is not None):
            raise ValueError('Incomplete reviewed class population')
        comments = item['source_comment_count']
        see_also = item['seeAlso_literal_count']
        state = ('COMMENT_CANDIDATE' if comments else
                 'DESCRIPTIVE_SEEALSO_LITERAL_NO_COMMENT' if see_also else
                 'NO_DEFINITION_IN_SELECTED_MIRROR')
        classes.append({
            'iri': iri,
            'population': 'LOCAL_DECLARATION' if local else 'EXTERNAL_REDECLARATION_NOT_RESOLVED_IMPORT',
            'label': item['labels'][0] if item['labels'] else None,
            'source_locator': f"private archive member CMO-db-32f457a.n3 lines {LINES[name]}; census classes[{len(classes)}]",
            'source_definition_state': state,
            'source_comment_sha256': item['source_comment_sha256'],
            'source_seeAlso_literal_sha256': item['seeAlso_literal_sha256'],
            'reviewer_paraphrase': source['statement'].split('Source-attributed reviewer paraphrase and constraint review: ', 1)[-1] if source else None,
            'review_evidence': ['CMO:' + x for x in source['evidence']] if source else [],
            'asserted_named_superclasses': [
                x['object']['iri'] for x in item['declarations_and_constraints']
                if x['predicate'].endswith('#subClassOf') and 'iri' in x['object']],
            'asserted_equivalent_expressions': sum(x['predicate'].endswith('#equivalentClass')
                                                   for x in item['declarations_and_constraints']),
            'explicit_deprecated': any(x['predicate'].endswith('#deprecated')
                                       for x in item['declarations_and_constraints']),
            'asserted_constraints': item['declarations_and_constraints'],
            'constraint_ref': f"evidence/related-work/deep-reviews/CMO/mirror-census.json#classes/{len(classes)}",
        })
    referenced = set()
    for section in ('classes', 'object_properties'):
        for row in census[section]:
            for c in row['declarations_and_constraints']:
                if c['predicate'].endswith(('#subClassOf', '#domain', '#range', '#onClass')):
                    if 'iri' in c['object']:
                        referenced.add(c['object']['iri'])
                    else:
                        for x in c['object'].get('anonymous_expression', []):
                            if x['predicate'].endswith('#onClass'):
                                referenced.add(x['object']['iri'])
    declarations = {x['iri'] for x in classes}
    if not referenced <= declarations:
        raise ValueError('Unaccounted class reference')
    return {
        'schema_version': '1.0', 'issue': 245, 'work_id': 'CMO',
        'scope': 'One complete third-party mirror candidate root; original 2011 author release and imported closure not identified.',
        'source_sha256': census['source_sha256'],
        'census_sha256': digest(census_path),
        'paper_dossier_sha256': digest(review_path),
        'source_license': 'NOT_IDENTIFIED_IN_SELECTED_FILE',
        'counts': {
            'local_classes': sum(x['population'] == 'LOCAL_DECLARATION' for x in classes),
            'external_redeclarations': sum(x['population'] != 'LOCAL_DECLARATION' for x in classes),
            'referenced_named_classes': len(referenced),
            'referenced_local_classes': sum(x.startswith(NAMESPACE) for x in referenced),
            'referenced_external_classes': sum(not x.startswith(NAMESPACE) for x in referenced),
            'local_source_comment_candidates': sum(x['population'] == 'LOCAL_DECLARATION' and x['source_definition_state'] == 'COMMENT_CANDIDATE' for x in classes),
            'local_descriptive_seeAlso_without_comment': sum(x['population'] == 'LOCAL_DECLARATION' and x['source_definition_state'] == 'DESCRIPTIVE_SEEALSO_LITERAL_NO_COMMENT' for x in classes),
            'local_missing_descriptive_annotations': sum(x['population'] == 'LOCAL_DECLARATION' and x['source_definition_state'] == 'NO_DEFINITION_IN_SELECTED_MIRROR' for x in classes),
            'local_explicit_deprecated': sum(x['population'] == 'LOCAL_DECLARATION' and x['explicit_deprecated'] for x in classes),
            'imported_closure_classes': None, 'inferred_classes': None,
            'original_author_release_classes': None,
        },
        'direct_imports': census['declared_import_iris'],
        'unresolved_imports': census['declared_import_iris'],
        'imported_definitions_complete': False,
        'referenced_class_iris': sorted(referenced),
        'classes': classes,
        'machine_reasoner': 'NOT_EXECUTED',
        'paper_fidelity': 'NOT_ESTABLISHED',
        'model_change': 'NONE',
    }


def render_catalog(c):
    lines = [
        '# CMO: selected third-party root class glossary', '',
        'Issue #245. Exact mirror SHA256 `' + c['source_sha256'] + '`. ' + c['scope'],
        '',
        'The 12 rows below account for every explicit named class declaration: seven local and five external redeclarations. '
        'An external declaration is not an acquired import definition. The cited constraints are retained in the structured catalog and full census; comments are paraphrased, not redistributed.',
        '',
        '| Class IRI | Local? | Label | Source annotation / paraphrase | Named superclass | N3 locator |',
        '|---|---|---|---|---|---|',
    ]
    for r in c['classes']:
        description = r['reviewer_paraphrase'] or 'No source definition in the selected mirror; external definition not acquired.'
        description = r['source_definition_state'] + ': ' + description
        lines.append('| ' + ' | '.join([
            r['iri'], 'yes' if r['population'] == 'LOCAL_DECLARATION' else 'external',
            r['label'] or 'none', description.replace('|', '/'),
            '; '.join(r['asserted_named_superclasses']) or 'none',
            r['source_locator'].split(';')[0].replace('private archive member ', ''),
        ]) + ' |')
    lines += [
        '',
        'Four local Universal-family classes additionally have anonymous representedBy minQualifiedCardinality 0 restrictions; they are fully indexed in [the structured catalog](CMO-class-catalog.yaml) and [the complete mirror census](../deep-reviews/CMO/mirror-census.json). No positive representation witness follows from a zero minimum.',
        '',
        'Referenced class IRIs in asserted subclass, domain, range and onClass slots: '
        + str(c['counts']['referenced_named_classes']) + ' ('
        + str(c['counts']['referenced_local_classes']) + ' local; '
        + str(c['counts']['referenced_external_classes']) + ' external). '
        'Explicit local deprecated markers: 0. Imported-closure, inferred and original-release populations: unknown.',
        '',
        'The IAO and SKOS direct imports are unversioned and unresolved. BFO1.1 IRIs are references in this mirror, not a declared BFO import or proof of the original paper edition. Source license is unidentified in the selected file. '
        'The [technical review](CMO.md) records eight bounded findings and the decision for #255/#126. No formal import, equivalence, reasoner result or Clariceptify model change is accepted.',
        '',
    ]
    return '\n'.join(lines)


def render_review(d):
    c = d['population']
    lines = [
        '# CMO: bounded technical artifact review', '',
        'Issue #245. Checked ' + d['checked_on'] + ' against Clariceptify baseline `' + d['baseline_commit'] + '`. '
        'The selected [CEUR paper](' + d['source']['paper_url'] + ') and '
        '[pinned third-party mirror](' + d['source']['mirror_url'] + ') have separate identities.',
        '',
        'The original paper-linked PURL returned 404 in the recorded probe. The mirror N3 file has '
        + str(c['selected_mirror_explicit_triples']) + ' explicit triples, '
        + str(c['selected_mirror_local_named_classes']) + ' local classes and '
        + str(c['selected_mirror_external_class_redeclarations']) + ' external redeclarations. '
        'Original 2011 author release/version correspondence is unverified. '
        'Its path date does not establish a release date; no source-file license was identified.',
        '',
        '[Complete selected class glossary](CMO-class-catalog.md) and [structured catalog](CMO-class-catalog.yaml). '
        'The original and imported class populations remain unknown.',
        '',
        '| Check | Source locator | Bounded result |',
        '|---|---|---|',
    ]
    for x in d['checks']:
        lines.append('| ' + x['id'] + ': ' + x['question'] + ' | ' + x['locator'].replace('|', '/') +
                     ' | ' + x['outcome'].replace('|', '/') + ' |')
    lines += [
        '', '## Scenario and disposition', '',
        '**Positive:** ' + d['scenarios']['positive'], '',
        '**Adverse:** ' + d['scenarios']['adverse'], '',
        d['decision']['export'], '',
        'The selected mirror is a candidate for comparison, with no accepted equivalence or owner adoption. '
        'Historical import closure, full-theory reasoner execution, original query/plot reproduction and independent expert review remain open. '
        'No model, requirement, fixture, manuscript or release change was made.',
        '',
    ]
    return '\n'.join(lines)


def write(root=ROOT):
    art = root / BASE / 'artifacts'
    c = catalog(root)
    (art / 'CMO-class-catalog.yaml').write_text(yaml.safe_dump(c, sort_keys=False, allow_unicode=True, width=110))
    (art / 'CMO-class-catalog.md').write_text(render_catalog(c))
    d = yaml.safe_load((art / 'CMO.yaml').read_text())
    (art / 'CMO.md').write_text(render_review(d))


if __name__ == '__main__':
    write()
