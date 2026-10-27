"""Check research-dossier provenance and closure boundaries, not scientific truth."""
from pathlib import Path
import hashlib
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = 'evidence/related-work/deep-reviews'
PROTECTED = ('model/', 'requirements/', 'ontology/', 'ontologies/', 'formal/',
             'fixtures/', 'releases/', 'docs/decisions/', 'docs/research/manuscript')


def protected_fingerprint(root):
    members = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in root.rglob('*') if p.is_file()
               and (str(p.relative_to(root)).startswith(PROTECTED)
                    or str(p.relative_to(root)) == 'CITATION.cff')}
    return {'files': len(members), 'sha256': hashlib.sha256(
        json.dumps(members, sort_keys=True, separators=(',', ':')).encode()).hexdigest()}


def validate_artifact_census(report, binding):
    if report['source_sha256'] != binding['source_sha256']:
        raise ValueError('Artifact census source substitution')
    if report['reasoner_execution'] != 'NOT_EXECUTED' or report['inference_counts'] is not None:
        raise ValueError('Inventory promoted to inference')
    if report['semantic_acceptance'] != 'NOT_ASSESSED' or report['source_redistributed']:
        raise ValueError('Inventory scope promoted')
    if report['counts'] != binding['counts'] or report['explicit_triples'] != binding['explicit_triples']:
        raise ValueError('Census population mismatch')
    for kind, count in report['counts'].items():
        records = report[kind]
        if len(records) != count or len({r['iri'] for r in records}) != count:
            raise ValueError('Incomplete or duplicate named-entity inventory')
        if any(not r.get('declarations_and_constraints') for r in records):
            raise ValueError('Missing entity declarations/constraints')


def validate_dossier(d, entry, dimensions):
    def require(condition, message):
        if not condition:
            raise ValueError(entry['id'] + ': ' + message)
    require(d['work_id'] == entry['id'] and d['issue'] == entry['issue'], 'work/issue mismatch')
    require(d['source']['sha256'] == entry['sha256'] and
            d['source']['filename'] == entry['filename'], 'changed source identity')
    require(d['source']['pdf_pages'] == entry['pdf_pages'], 'changed page population')
    require(d['boundary']['model_change'] == 'NONE' and
            d['boundary']['adoption'] == 'OWNER_DECISION_REQUIRED' and
            d['boundary']['independent_expert_review'] == 'NOT_PERFORMED', 'unauthorized promotion')
    evidence = {e['id']: e for e in d['evidence']}
    require(len(evidence) == len(d['evidence']), 'duplicate evidence ID')
    for e in evidence.values():
        require(e['locator'] and e['summary'], 'empty evidence locator/summary')
        if e.get('source_kind', 'PAPER') == 'PAPER':
            require(e['pages'] and all(isinstance(p, int) and 1 <= p <= entry['pdf_pages'] for p in e['pages']), 'invalid evidence page')
        elif e['source_kind'] == 'REPOSITORY':
            require(e.get('path') and
                    re.fullmatch(r'[0-9a-f]{40}', e.get('commit', '')) and
                    re.fullmatch(r'[0-9a-f]{64}', e.get('sha256', '')), 'unpinned repository evidence')
        elif e['source_kind'] == 'ARTIFACT':
            require(re.fullmatch(r'[0-9a-f]{64}', e.get('sha256', '')) and
                    e.get('url', '').startswith(('http://', 'https://')), 'unpinned artifact evidence')
        else:
            require(e['source_kind'] == 'SPECIFICATION' and
                    e.get('url', '').startswith('https://'), 'unidentified specification evidence')
    require(set(d['dimensions']) == set(dimensions), 'missing shared review dimension')
    statements = list(d['dimensions'].values())
    for section in ['catalog', 'commitments', 'scenarios', 'findings', 'questions', 'synthesis']:
        require(isinstance(d[section], list) and d[section], 'missing ' + section)
        ids = [r['id'] for r in d[section]]
        require(len(ids) == len(set(ids)), 'duplicate IDs in ' + section)
        statements.extend(d[section])
    statements.extend(d['evaluation'].values())
    statements.extend(d.get('relation_index', []))
    statements.extend(d['artifact'].get('class_reviews', []))
    for row in statements:
        require(row.get('statement') and row.get('evidence'), 'unbound statement')
        require(set(row['evidence']) <= set(evidence), 'dangling evidence reference')
        require(row['basis'] in {'AUTHOR_REPORTED', 'REVIEWER_INTERPRETATION',
                                'EXECUTED', 'NOT_REPORTED', 'UNKNOWN'}, 'untyped evidence')
        if row['basis'] == 'EXECUTED':
            require(row.get('execution_ref'), 'execution without inspectable result')
    require(set(d['evaluation']) == {'Verification', 'Validation', 'Evaluation', 'Assessment', 'Assurance'}, 'missing VVEAA function')
    if 'formula_population' in d:
        pop = d['formula_population']
        expected = list(range(pop['first'], pop['last'] + 1))
        require(pop['count'] == len(expected) and
                [r.get('formula_number') for r in d['commitments']] == expected,
                'incomplete or duplicated numbered-display ledger')
    if d['status'] == 'REVIEW_COMPLETE':
        require(d['coverage']['read_pages'] == list(range(1, entry['pdf_pages'] + 1)), 'incomplete full-text reading')
        require(d['coverage']['units'] and all(u['status'] == 'REVIEWED' and
                u.get('evidence') and set(u['evidence']) <= set(evidence)
                for u in d['coverage']['units']), 'unreviewed paper unit')
        require(d['coverage']['visual_pages'] and d['coverage']['catalog_boundary'], 'missing visual/catalog boundary')
        require(d['artifact']['issue'] in entry['artifact_issues'] and
                d['artifact']['version_relation'] and d['artifact']['status'], 'artifact boundary missing')
    else:
        require(d['status'] == 'IN_PROGRESS', 'invalid review state')


def validate_diagram_inventory(dossier, inventory):
    binding = dossier['diagram_inventory']
    if inventory['source_sha256'] != dossier['source']['sha256'] or binding['source_sha256'] != inventory['source_sha256']:
        raise ValueError('Diagram source substitution')
    figures = inventory['figures']
    if (inventory['work_id'] != dossier['work_id'] or inventory['figure_population'] != len(figures) or
            [f['number'] for f in figures] != binding['figures']):
        raise ValueError('Incomplete or duplicate diagram population')
    for figure in figures:
        if (figure['pdf_page'] not in dossier['coverage']['visual_pages'] or
                figure['inspection'] != 'VISUALLY_REVIEWED' or not figure['nodes']):
            raise ValueError('Unreviewed diagram population')
    slots = [slot for f in figures for n in f['nodes'] for slot in n['slots']]
    names = {s.split(' : ')[0] for s in slots}
    indexed = [r['printed_name'] for r in dossier['relation_index'] if 'printed_name' in r]
    if len(indexed) != len(set(indexed)) or set(indexed) != names:
        raise ValueError('Unindexed or duplicate diagram property')
    expected = {'figure_boxes': sum(len(f['nodes']) for f in figures),
                'distinct_labels_all_figures': len({n['label'] for f in figures for n in f['nodes']}),
                'class_box_labels_figures2_6': len({n['label'] for f in figures if f['number'] != 1 for n in f['nodes']}),
                'slot_occurrences': len(slots), 'distinct_printed_property_names': len(names)}
    if inventory['counts'] != expected:
        raise ValueError('Diagram display population mismatch')


def validate_class_review_coverage(dossier, catalog):
    reviews = dossier['artifact']['class_reviews']
    if (len(reviews) != len(catalog['classes']) or
            {r['iri'] for r in reviews} != {r['iri'] for r in catalog['classes']}):
        raise ValueError('Manual class reviews omit or duplicate a catalogued class')


def check(root=ROOT):
    base = root / BASE
    protocol = yaml.safe_load((base / 'protocol.yaml').read_text())
    register = yaml.safe_load((base / 'register.yaml').read_text())
    expected = json.loads((base / 'baseline-protection.json').read_text())
    if protected_fingerprint(root) != expected['fingerprint']:
        raise ValueError('Research-only boundary violated: protected scientific baseline changed')
    entries = register['acquired_papers'] + register['waiting_for_owner']
    if len({r['id'] for r in entries}) != len(entries) or len({r['issue'] for r in entries}) != len(entries):
        raise ValueError('Duplicate paper identity or primary issue')
    if len(register['acquired_papers']) != 12 or len(register['waiting_for_owner']) != 7:
        raise ValueError('Changed approved paper population; record a protocol revision')
    inventory = yaml.safe_load((root / 'evidence/related-work/corpus/access-inventory.yaml').read_text())
    inputs = {r.get('filename'): r for r in inventory['records'] + inventory['additional_work_or_version_records'] if r.get('filename')}
    done = []
    for entry in register['acquired_papers']:
        if inputs[entry['filename']]['sha256'] != entry['sha256']:
            raise ValueError('Paper identity diverges from retained corpus')
        path = base / entry['id'] / 'review.yaml'
        if not path.exists():
            if entry['state'] != 'QUEUED':
                raise ValueError('Missing review for claimed progress')
            continue
        d = yaml.safe_load(path.read_text())
        validate_dossier(d, entry, protocol['dimensions'])
        if 'diagram_inventory' in d:
            binding = d['diagram_inventory']
            raw = (root / binding['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest() != binding['sha256']:
                raise ValueError('Changed diagram inventory bytes')
            validate_diagram_inventory(d, yaml.safe_load(raw))
        if 'class_catalog' in d['artifact']:
            binding = d['artifact']['class_catalog']
            raw = (root / binding['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest() != binding['sha256']:
                raise ValueError('Changed manually reviewed class catalogue')
            validate_class_review_coverage(d, yaml.safe_load(raw))
        if 'discovery_execution' in d['artifact']:
            binding = d['artifact']['discovery_execution']
            if hashlib.sha256((root / binding['path']).read_bytes()).hexdigest() != binding['sha256']:
                raise ValueError('Changed discovery execution evidence')
        if entry['state'] != d['status']:
            raise ValueError('Register/review state mismatch')
        if 'census' in d['artifact']:
            binding = d['artifact']['census']
            raw = (root / binding['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest() != binding['sha256']:
                raise ValueError('Changed artifact census bytes')
            report = json.loads(raw)
            validate_artifact_census(report, binding)
            known_inputs = yaml.safe_load((root / 'evidence/related-work/artifact-inputs.yaml').read_text())
            if binding['source_sha256'] not in {r['sha256'] for r in known_inputs['artifacts']}:
                raise ValueError('Census source missing from retained-artifact input manifest')
            generator = report['generator']
            if hashlib.sha256((root / generator['path']).read_bytes()).hexdigest() != generator['sha256']:
                raise ValueError('Artifact inventory generator changed')
            if (len(d['artifact']['class_reviews']) != len(report['classes']) or
                    {r['iri'] for r in d['artifact']['class_reviews']} != {r['iri'] for r in report['classes']}):
                raise ValueError('Manual class coverage differs from the full local census')
        from render_deep_review import render
        if (path.parent / 'report.md').read_text() != render(d):
            raise ValueError('Stale readable report')
        if d['status'] == 'REVIEW_COMPLETE':
            done.append(entry['id'])
    for entry in register['waiting_for_owner']:
        if entry['state'] != 'BLOCKED_ON_FULL_TEXT' or entry.get('sha256') is not None:
            raise ValueError('Missing full text promoted')
    from check_source_audit import check as check_source_audit
    source_audit = check_source_audit(root)
    return {'status': 'PASS', 'source_audit': source_audit, 'acquired_papers': 12, 'completed_deep_reviews': done,
            'queued_papers': sum(r['state'] == 'QUEUED' for r in register['acquired_papers']),
            'waiting_for_owner': 7, 'protected_baseline': expected['fingerprint'],
            'scope': 'Provenance, coverage declarations and state boundaries; not independent semantic validation.'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
