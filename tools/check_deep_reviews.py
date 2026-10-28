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
    if 'labeled_formula_population' in d:
        pop = d['labeled_formula_population']
        labels = [r.get('formula_label') for r in d['commitments']]
        require(pop['count'] == len(pop['labels']) == len(set(labels)) and
                labels == pop['labels'] and
                all(r.get('normalized_formula') and r.get('formula_page') in
                    d['coverage']['visual_pages'] for r in d['commitments']),
                'incomplete or duplicated labeled-formula ledger')
        if d['work_id'] == 'COM2004':
            require(set(labels) == {f'D{i}' for i in range(1, 16)} |
                    {f'A{i}' for i in range(1, 6)} and
                    pop['definitions'] == 15 and pop['axioms'] == 5,
                    'changed COM source-label population')
            literal = next(r for r in d['commitments'] if r['formula_label'] == 'D14')
            require(literal['normalized_formula'] ==
                    'MES(x) := PER(x) or BEL(x) or DES(x) or INT(x)',
                    'COM source PER silently repaired to another predicate')
            require(all(v is None for v in d['artifact']['machine_class_populations'].values()),
                    'Paper taxonomy promoted to machine class population')
        if d['work_id'] == 'BDI2020':
            named = {'BelO', 'DesO', 'BelP', 'DesP', 'Dec', 'Int-Dec', 'IntO', 'IntP'}
            core = [r for r in d['commitments'] if r['variant'].startswith('CORE_')]
            require(len(core) == len(named) and
                    {r['source_label'] for r in core} == named and
                    d['paper_expression_scope']['do_not_union_alternatives_into_core'],
                    'BDI alternative or hypothesis promoted to named core')
            bel = next(r for r in core if r['source_label'] == 'BelO')
            require(bel['normalized_formula'] ==
                    'Dispositional belief SubClassOf (realized_in only Occurrent belief)',
                    'BDI literal only restriction changed into existence')
            trigger = next(r for r in d['commitments'] if r['formula_label'] == 'TRIGGER-INT-PARTHOOD')
            require(trigger['normalized_formula'] == 'Tmin(i) SubClassOf Occurrent belief',
                    'BDI source Tmin silently repaired')
            require(all(v is None for v in d['artifact']['machine_class_populations'].values()) and
                    d['paper_expression_scope']['machine_axiom_count'] is None,
                    'BDI paper inventory promoted to machine population')
        if d['work_id'] == 'BDI2026Preprint':
            numbered = [r for r in d['commitments'] if 'formula_number' in r]
            require([r['formula_number'] for r in numbered] == list(range(1, 79)) and
                    [r['formula_label'] for r in numbered] == [str(n) for n in range(1, 79)],
                    'incomplete BDI2026 numbered source population')
            expressions = {r['formula_number']: r['normalized_formula'] for r in numbered}
            require(all(expressions[a] == expressions[b] for a, b in [(14, 39), (15, 40), (21, 41)]),
                    'BDI2026 printed duplicate silently changed')
            literal = {2: 'WorldState SubClassOf (isPerceivedBy only Agent)',
                       28: 'MentalProcess SubClassOf (isTriggeredBy only MentalEntity)',
                       75: 'TimeInterval SubClassOf (hasStartTime exactly 1 TimeInstant)',
                       76: 'TimeInterval SubClassOf (hasEndTime max 1 TimeInstant)',
                       77: 'MentalEntity SubClassOf (atTime some TemporalEntity)',
                       78: 'MentalEntity SubClassOf (hasValidity some TemporalEntity)'}
            require(all(expressions[n] == value for n, value in literal.items()),
                    'BDI2026 source quantification silently changed')
            boxes = d['figure_inventory']['class_boxes']
            catalog_boxes = [r['label'] for r in d['catalog'] if r.get('kind') == 'FIGURE_CLASS']
            require(len(boxes) == len(set(boxes)) == 22 and 'GoalProcess' in boxes and
                    len(catalog_boxes) == 22 and set(catalog_boxes) == set(boxes),
                    'incomplete BDI2026 paper figure taxonomy')
            require(d['identity']['arxiv_version'] == '2511.17162v2' and
                    d['identity']['final_journal_byte_equivalence'] == 'NOT_ESTABLISHED',
                    'BDI2026 preprint promoted to final journal equivalence')
            sources = {r['path']: r for r in d['artifact']['selected_files']}
            require(sources['bdi/bdi.ttl']['version_info'] == ['0.5'] and
                    sources['bdi-dul/bdi-dul.rdf']['declared_import_iris'] == [
                        'http://www.ontologydesignpatterns.org/ont/d0.owl',
                        'https://w3id.org/fossr/bdi/ontology/0.3/'],
                    'BDI2026 pinned core/alignment version mismatch hidden')
            require(all(v is None for v in d['artifact']['machine_class_populations'].values()) and
                    d['paper_expression_scope']['machine_axiom_count'] is None,
                    'BDI2026 paper counts promoted to machine census')
    if d['work_id'] == 'CognitiveAtlas2011':
        pop = d['paper_population']
        require(pop['basis'] == 'AUTHOR_REPORTED' and pop['source_year'] == 2011 and
                [pop[k] for k in ['current_terms', 'mental_constructs', 'tasks', 'terms_with_definitions']] ==
                [904, 708, 196, 795] and
                pop['definition_adequacy'] == 'MOST_ACKNOWLEDGED_INSUFFICIENT' and
                not pop['independently_reproduced'],
                'Cognitive Atlas historical status promoted to verified adequacy')
        require(all(v is None for v in d['artifact']['machine_class_populations'].values()) and
                d['paper_formalization']['dl_axiom_population'] is None and
                d['paper_formalization']['numbered_formula_count'] == 0,
                'Cognitive Atlas paper terms promoted to machine population')
        require(d['artifact']['formal_version'] == '0.3' and
                d['artifact']['historical_paper_fidelity'] == 'NOT_ESTABLISHED',
                'Cognitive Atlas filename promoted to historical version identity')
        require(d['implementation_scope']['literature_relation'] == 'citesForInformation' and
                d['implementation_scope']['theory_testing'] == 'FUTURE_NOT_AVAILABLE_IN_PAPER',
                'Cognitive Atlas future or informative relation promoted to implemented support')
    if d['work_id'] == 'EmotionsOnto2014':
        study = d['study_population']
        require(study['basis'] == 'AUTHOR_REPORTED' and
                study['target'] == 'EPF_PRODUCT_EXPERIENCE_NOT_EMOTION_DETECTION' and
                [study[k] for k in ['participants', 'women', 'men', 'minutes', 'choices_per_participant']] ==
                [14, 7, 7, 30, 1] and study['recognition_accuracy'] is None and
                study['causal_emotion_change'] is None and not study['independently_reproduced'],
                'EmotionsOnto product responses promoted to recognition or causal validation')
        require(all(v is None for v in d['artifact']['machine_class_populations'].values()) and
                d['artifact']['original_2014_sha256'] is None and
                d['artifact']['historical_fidelity'] == 'NOT_ESTABLISHED',
                'EmotionsOnto later extension promoted to original class population')
        require(d['paper_formalization']['numbered_formula_count'] == 0 and
                d['paper_formalization']['quantification_of_printed_trigger_restriction'] ==
                'NOT_SPECIFIED_AS_DL_FORMULA', 'EmotionsOnto prose promoted to a printed DL formula')
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


def validate_cognitive_figure_ledger(dossier, ledger):
    if (ledger['source_sha256'] != dossier['source']['sha256'] or
            ledger['work_id'] != 'CognitiveAtlas2011' or
            [f['number'] for f in ledger['figures']] != [1, 2, 3, 4] or
            [f['pdf_page'] for f in ledger['figures']] != [4, 5, 8, 9]):
        raise ValueError('Incomplete or substituted Cognitive Atlas figure population')
    task, senses, empirical = ledger['figures'][1:]
    if task['contrast_literal'] != '0-back minus 2-back' or task['conditions'] != ['0-back', '1-back', '2-back']:
        raise ValueError('Cognitive Atlas printed contrast silently reversed')
    if senses['senses'] != ['behavioral inhibition (cognitive)', 'behavioral inhibition (temperament)']:
        raise ValueError('Cognitive Atlas distinct senses silently collapsed')
    if (empirical['edge_kind'] != 'PROPOSED_EMPIRICAL_ASSOCIATION_NOT_CLASS_HIERARCHY' or
            len(empirical['layers']) != 5 or sum(map(len, empirical['layers'].values())) != 13 or
            ledger['machine_class_count'] is not None):
        raise ValueError('Cognitive Atlas empirical illustration promoted to class hierarchy')


def validate_emotions_figure_ledger(dossier, ledger):
    if (ledger['source_sha256'] != dossier['source']['sha256'] or
            ledger['work_id'] != 'EmotionsOnto2014' or
            [f['number'] for f in ledger['figures']] != [1, 2, 3, 4, 5] or
            [f['pdf_page'] for f in ledger['figures']] != [6, 8, 10, 11, 12]):
        raise ValueError('Incomplete or substituted EmotionsOnto figure population')
    taxonomy = ledger['figures'][1]
    nodes = {n['label']: n for n in taxonomy['nodes']}
    if (len(nodes) != len(taxonomy['nodes']) or len(nodes) != 39 or
            any(p not in nodes for n in nodes.values() for p in n['parents']) or
            {r['label'] for r in dossier['catalog'] if r.get('kind') == 'FIGURE2_CATEGORY'} != set(nodes)):
        raise ValueError('Incomplete EmotionsOnto paper taxonomy')
    if (nodes['dul:Situation']['parents'] != ['dul:SocialObject', 'SocialContext', 'EnvironmentalContext'] or
            nodes['Interface']['parents'] != ['PersonalContext']):
        raise ValueError('EmotionsOnto source context arrows silently repaired')
    instrument = ledger['figures'][4]
    names = instrument['pleasant'] + instrument['unpleasant']
    counts = ledger['table']['counts']
    if (len(names) != len(set(names)) or len(names) != 14 or set(names) != set(counts) or
            counts != dossier['study_population']['category_counts'] or
            {k: v for k, v in counts.items() if v} != {'admiration': 6, 'satisfaction': 4, 'fascination': 4} or
            sum(counts.values()) != ledger['table']['total'] or ledger['table']['total'] != 14 or
            ledger['machine_class_count'] is not None):
        raise ValueError('EmotionsOnto questionnaire/result population changed')


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
    class_numbers = inventory.get('class_diagram_numbers')
    if class_numbers is not None and (len(class_numbers) != len(set(class_numbers)) or
            not set(class_numbers) <= {f['number'] for f in figures} or
            any((f.get('kind') == 'CLASS_DIAGRAM') != (f['number'] in class_numbers) for f in figures)):
        raise ValueError('Diagram kind/class population mismatch')
    class_key = 'class_box_labels' if class_numbers is not None else 'class_box_labels_figures2_6'
    item_key = 'figure_items' if inventory.get('count_policy') == 'PRINTED_ITEMS_NOT_ONLY_BOXES' else 'figure_boxes'
    expected = {item_key: sum(len(f['nodes']) for f in figures),
                'distinct_labels_all_figures': len({n['label'] for f in figures for n in f['nodes']}),
                class_key: len({n['label'] for f in figures
                                if (f['number'] in class_numbers if class_numbers is not None else f['number'] != 1)
                                for n in f['nodes']}),
                'slot_occurrences': len(slots), 'distinct_printed_property_names': len(names)}
    if inventory['counts'] != expected:
        raise ValueError('Diagram display population mismatch')
    if dossier['work_id'] == 'COM2004':
        nodes = figures[0]['nodes']
        mapping = {n['id']: n for n in nodes}
        catalog = [r for r in dossier['catalog'] if r.get('diagram_figure') == 1]
        if (len(mapping) != len(nodes) or len(catalog) != len(nodes) or
                {r['symbol'] for r in catalog} != set(mapping) or
                any(r['diagram_parent'] != mapping[r['symbol']]['paper_parent'] for r in catalog)):
            raise ValueError('Incomplete paper-taxonomy category/hierarchy catalog')
        edges = {(e['child'], e['parent']) for e in figures[0]['edges']}
        parents = {(n['id'], n['paper_parent']) for n in nodes if n['paper_parent']}
        if (len(edges) != len(figures[0]['edges']) or edges != parents or
                any(parent not in mapping for _, parent in edges)):
            raise ValueError('Incomplete paper-taxonomy edge inventory')


def validate_dlp_intake(report, binding):
    """Check retained structural evidence without promoting it to a manual glossary."""
    if report['archive']['sha256'] != binding['source_sha256']:
        raise ValueError('DLP source substitution')
    if (report['historical_2003_fidelity'] != 'NOT_ESTABLISHED' or report['paper_class_count'] is not None or
            report['reasoner_execution'] != 'NOT_EXECUTED' or report['inferred_counts'] is not None or
            report['semantic_acceptance'] != 'NOT_ASSESSED' or report['model_change'] != 'NONE'):
        raise ValueError('DLP intake promoted to historical/semantic acceptance')
    modules = report['modules']
    if (report['module_population'] != len(modules) or
            len({m['filename'] for m in modules}) != len(modules) or
            len({m['ontology_iri'] for m in modules}) != len(modules)):
        raise ValueError('Incomplete or duplicate DLP module population')
    union = set()
    for m in modules:
        classes = m['declared_named_class_iris']
        local = {iri for iri in classes if iri.startswith(m['namespace'])}
        candidates = m['local_definition_candidates']
        if (len(classes) != len(set(classes)) or len(classes) != m['declared_named_owl_classes_all_namespaces'] or
                len(local) != m['local_named_owl_classes'] or
                len(classes) - len(local) != m['external_named_class_redeclarations'] or
                {c['iri'] for c in candidates} != local or len(candidates) != len(local)):
            raise ValueError('Incomplete DLP declared class/comment inventory')
        if any(c['definition_review'] != 'PENDING' or c['public_raw_comment_text'] or
               ((c['comment_count'] > 0) != bool(c['comment_sha256'])) for c in candidates):
            raise ValueError('DLP comment intake promoted to manual definition')
        union.update(classes)
    if len(union) != report['asserted_archive_union']['counts']['named_owl_classes']:
        raise ValueError('DLP class union population mismatch')
    mapping = {m['ontology_iri']: m for m in modules}
    visited, pending, unresolved = set(), [report['asserted_archive_union']['root_iri']], set()
    while pending:
        iri = pending.pop()
        if iri in visited:
            continue
        if iri not in mapping:
            unresolved.add(iri)
            continue
        visited.add(iri)
        pending.extend(mapping[iri]['declared_import_iris'])
    if (sorted(visited) != report['asserted_archive_union']['resolved_modules'] or
            sorted(unresolved) != report['asserted_archive_union']['unresolved_declared_imports']):
        raise ValueError('DLP supplied import closure mismatch')


def validate_class_review_coverage(dossier, catalog):
    reviews = dossier['artifact']['class_reviews']
    if (len(reviews) != len(catalog['classes']) or
            {r['iri'] for r in reviews} != {r['iri'] for r in catalog['classes']}):
        raise ValueError('Manual class reviews omit or duplicate a catalogued class')


def validate_candidate_census(dossier, report, binding):
    validate_artifact_census(report, binding)
    if (report['provenance']['authority'] != 'THIRD_PARTY_MIRROR_NOT_AUTHOR_RELEASE' or
            report['provenance']['paper_2011_fidelity'] != 'NOT_ESTABLISHED' or
            report['provenance']['path_date_is_release_date'] or report['model_change'] != 'NONE'):
        raise ValueError('Candidate mirror promoted to original author release')
    local = {r['iri'] for r in report['classes'] if r['iri'].startswith(binding['local_namespace'])}
    reviews = dossier['artifact']['class_reviews']
    if len(reviews) != len(local) or {r['iri'] for r in reviews} != local:
        raise ValueError('Incomplete candidate local class reviews')


def validate_printed_query(dossier, record):
    if (record['source_sha256'] != dossier['source']['sha256'] or
            hashlib.sha256(record['query'].encode()).hexdigest() != record['query_sha256']):
        raise ValueError('Printed query source substitution')
    if (record['state'] != 'PARSE_REJECTED' or not record['error'] or
            record['endpoint_execution'] != 'NOT_EXECUTED' or record['historical_engine'] != 'NOT_IDENTIFIED'):
        raise ValueError('Syntax observation promoted to historical query execution')


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
        if 'figure_ledger' in d:
            binding = d['figure_ledger']
            raw = (root / binding['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest() != binding['sha256']:
                raise ValueError('Changed Cognitive Atlas figure ledger bytes')
            if d['work_id'] == 'CognitiveAtlas2011':
                validate_cognitive_figure_ledger(d, yaml.safe_load(raw))
            elif d['work_id'] == 'EmotionsOnto2014':
                validate_emotions_figure_ledger(d, yaml.safe_load(raw))
            else:
                raise ValueError('Unknown paper figure-ledger contract')
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
        if 'dlp_intake' in d['artifact']:
            binding = d['artifact']['dlp_intake']
            raw = (root / binding['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest() != binding['sha256']:
                raise ValueError('Changed DLP intake evidence')
            intake = json.loads(raw)
            validate_dlp_intake(intake, binding)
            if hashlib.sha256((root / intake['generator']['path']).read_bytes()).hexdigest() != intake['generator']['sha256']:
                raise ValueError('Changed DLP intake generator')
        if 'candidate_census' in d['artifact']:
            binding = d['artifact']['candidate_census']
            raw = (root / binding['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest() != binding['sha256']:
                raise ValueError('Changed candidate census')
            candidate = json.loads(raw)
            validate_candidate_census(d, candidate, binding)
            generator = candidate['generator']
            if hashlib.sha256((root / generator['path']).read_bytes()).hexdigest() != generator['sha256']:
                raise ValueError('Changed candidate census generator')
        if 'syntax_check' in d['artifact']:
            binding = d['artifact']['syntax_check']
            raw = (root / binding['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest() != binding['sha256']:
                raise ValueError('Changed printed query check')
            validate_printed_query(d, json.loads(raw))
        if 'reading_recovery' in d['artifact']:
            binding = d['artifact']['reading_recovery']
            raw = (root / binding['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest() != binding['sha256']:
                raise ValueError('Changed reading recovery evidence')
            recovery = json.loads(raw)
            if (recovery['source_sha256'] != d['source']['sha256'] or
                    recovery['recovery']['ocr_pages'] != d['coverage']['read_pages'] or
                    recovery['human_or_AI_visual_inspection']['pages'] != d['coverage']['visual_pages']):
                raise ValueError('Incomplete or substituted reading recovery')
        if 'reading_inspection' in d['artifact']:
            binding = d['artifact']['reading_inspection']
            raw = (root / binding['path']).read_bytes()
            record = json.loads(raw)
            if (hashlib.sha256(raw).hexdigest() != binding['sha256'] or
                    record['source_sha256'] != d['source']['sha256'] or
                    record['read_pages'] != d['coverage']['read_pages'] or
                    record['visual_inspection']['pages'] != d['coverage']['visual_pages'] or
                    record['semantics_or_solver_executed'] != 'NOT_EXECUTED'):
                raise ValueError('Incomplete or substituted paper inspection record')
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
