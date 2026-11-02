"""Bounded domain-review integrity and conjunctive-query checks (not an OWL reasoner)."""
from pathlib import Path
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]

class ReviewError(ValueError):
    pass


def require(value, message):
    if not value:
        raise ReviewError(message)


def load(path):
    return yaml.safe_load((ROOT / path).read_text())


def records(path):
    return {x['id']: x for x in load(path)['records']}


def ancestors(cid, gens):
    parents = {}
    for row in gens.values():
        parents.setdefault(row['child_id'], set()).add(row['parent_id'])
    result, pending = {cid}, [cid]
    while pending:
        current = pending.pop()
        for parent in parents.get(current, set()):
            if parent not in result:
                result.add(parent)
                pending.append(parent)
    return result


def graph(fixture, concepts, relations, gens):
    nodes = {n['id']: n['concept_id'] for n in fixture['nodes']}
    require(len(nodes) == len(fixture['nodes']), 'duplicate node')
    require(set(nodes.values()) <= concepts.keys(), 'unknown concept')
    edges = [(e['relation_id'], e['source'], e['target']) for e in fixture['edges']]
    require(len(edges) == len(set(edges)), 'duplicate edge')
    for rid, source, target in edges:
        require(rid in relations and source in nodes and target in nodes, 'unknown edge endpoint or relation')
        rel = relations[rid]
        require(rel['source_id'] in ancestors(nodes[source], gens), 'source type mismatch')
        require(rel['target_id'] in ancestors(nodes[target], gens), 'target type mismatch')
    return nodes, edges


def answers(fixture, query, concepts, relations, gens):
    """Evaluate only the declared finite graph join; absent answer is not inconsistency."""
    nodes, edges = graph(fixture, concepts, relations, gens)
    bindings = [dict(query['anchors'])]
    require(all(n in nodes for n in query['anchors'].values()), 'unknown anchor')
    for pattern in query['patterns']:
        rid, source_var, target_var = pattern
        require(rid in relations, 'unknown query relation')
        expanded = []
        for binding in bindings:
            for edge_rid, source, target in edges:
                if edge_rid != rid:
                    continue
                candidate = dict(binding)
                for var, node in ((source_var, source), (target_var, target)):
                    if var in candidate and candidate[var] != node:
                        break
                    candidate[var] = node
                else:
                    expanded.append(candidate)
        bindings = expanded
    return [b for b in bindings if all(b[a] != b[z] for a, z in query.get('distinct', []))]


def check(slug, issue, domain_number, count):
    report = load(f'evaluation/domain-adequacy/{slug}.yaml')
    require((report['issue'], report['task_id'], report['domain_id']) ==
            (issue, f'R2-DOM-{domain_number:02d}', f'CLR-D{domain_number:04d}'), 'report identity')
    require(report['status'] == 'BOUNDED_DOMAIN_REVIEW_COMPLETE_WITH_OPEN_SEMANTIC_QUESTIONS', 'review status')
    require(report['model_revision'] == 'input-r1-rev1', 'model revision')
    require(len(report['baseline_commit']) == 40, 'baseline commit')
    required = {'model/domains.yaml','model/concepts.yaml','model/relations.yaml',
                'model/generalizations.yaml','model/constraints.yaml','requirements/functional.yaml',
                'requirements/competency-questions.yaml','evidence/concept-support.yaml',
                'docs/research/gap-comparison.yaml'}
    require(required <= report['input_bindings'].keys(), 'missing input binding')
    for path, digest in report['input_bindings'].items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, f'stale input: {path}')
    domains, concepts, relations, gens, constraints, frs, cqs = map(records, (
        'model/domains.yaml','model/concepts.yaml','model/relations.yaml','model/generalizations.yaml',
        'model/constraints.yaml','requirements/functional.yaml','requirements/competency-questions.yaml'))
    support = {x['concept_id']: x for x in load('evidence/concept-support.yaml')['records']}
    domain = domains[report['domain_id']]
    require((domain['label_en'],domain['purpose']) == (report['domain_name'],report['purpose']), 'domain identity/purpose')
    members = {x['id'] for x in concepts.values() if x['primary_domain_id']==report['domain_id']}
    require(len(members)==count==report['scope']['primary_domain_concepts'], 'member count')
    require(members==set(report['scope']['domain_member_ids']), 'member set')
    require(len(report['concept_review'])==count and {x['id'] for x in report['concept_review']}==members, 'review completeness')
    for row in report['concept_review']:
        actual, source = concepts[row['id']], support[row['id']]
        require((row['label'],row['stereotype'],row['definition']) ==
                (actual['label_en'],actual['ontouml_stereotype'],actual['definition']), 'concept binding')
        require(row['source_support']==source['support_type'], 'support binding')
        require(row['source_locator']==actual['source_locator'], 'concept locator')
        require(row['support_locator']==source['source_locator'], 'support locator')
        require(row['source_passages']==source['input_source_locations'], 'source passage locator')
        require(source['passage_verification']=='not_reverified_in_import' and source['typing_approval']=='not_assessed', 'support ceiling')
        require(bool(row['finding']), 'missing concept finding')
    require(set(report['scope']['relevant_requirements']) <= frs.keys(), 'requirements')
    require(set(report['scope']['relevant_cqs']) <= cqs.keys(), 'CQs')
    for q in report['domain_questions']:
        require(set(q['model_ids']) <= concepts.keys(), 'question concepts')
        require(set(q['relation_ids']) <= relations.keys(), 'question relations')
        require(set(q['constraint_ids']) <= constraints.keys(), 'question constraints')
        for cqid in q['cqs']:
            require(cqid in cqs and cqid in report['scope']['relevant_cqs'], 'question CQ')
            cq = cqs[cqid]
            require(cq['requirement_id'] in report['scope']['relevant_requirements'], 'CQ requirement binding')
            require(cq['test_execution']=='not_executed' and cq['answer_status']=='not_computed', 'full CQ promoted')
    for cid in report['constraint_review']:
        require(cid in constraints and constraints[cid]['execution_status']=='not_executed', 'constraint execution promoted')
        require(report['constraint_review'][cid] == constraints[cid]['text'], 'constraint text binding')
    query = report['selected_query']
    results = {}
    for kind, expected in [('positive',True),('adverse',False)]:
        scenario = report['scenarios'][kind]
        fixture = load(scenario['locator'])
        require(fixture['id']==scenario['id'] and fixture['model_revision']==report['model_revision'], 'fixture identity')
        require(fixture['expected_selected_answer'] is expected, 'fixture expectation')
        result = answers(fixture,query,concepts,relations,gens)
        require(bool(result) is expected, f'{kind} query outcome')
        results[kind] = len(result)
    require(report['scenarios']['conceptual_countercase']['execution']=='NOT_EXECUTED', 'countercase overclaim')
    require(len(report['findings']) >= 3, 'missing findings')
    require(len({x['id'] for x in report['findings']})==len(report['findings']), 'duplicate findings')
    known_ids = concepts.keys() | relations.keys() | constraints.keys() | frs.keys() | cqs.keys() | gens.keys()
    for finding in report['findings']:
        require(set(finding['evidence_ids']) <= known_ids, 'finding evidence identifier')
        require(bool(finding['route']) and bool(finding['contrary']), 'finding followup/ceiling')
    cells = {x['id'] for i in range(1,7) for x in load(f'evidence/related-work/comparisons/batch-{i}.yaml')['matrix']}
    require(set(report['source_comparison']['source_cells']) <= cells, 'comparison cell')
    require(report['decision']['semantic_adequacy']=='NOT_ASSESSED', 'semantic overclaim')
    require(all(report['decision'][k]=='NONE' for k in ('model_change','requirements_change','manuscript_change','release_change')), 'scope expansion')
    require(report['decision']['domain_name']=='KEEP' and report['decision']['no_class_quota'] is True, 'domain/quota boundary')
    require(f'[{report["domain_name"]} domain assessment]' in (ROOT/'README.md').read_text(), 'README link')
    return {'status':'PASS','issue':issue,'domain_members':count,'questions':len(report['domain_questions']),
            'findings':len(report['findings']),'selected_query_answers':results,
            'cq_execution':'NOT_EXECUTED','semantic_adequacy':'NOT_ASSESSED'}
