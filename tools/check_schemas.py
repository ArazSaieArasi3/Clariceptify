"""Validate record shapes and stable ID uniqueness; no adequacy judgment."""
from pathlib import Path
import copy
import hashlib
import json
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
MODEL = {'concept': 'concepts', 'domain': 'domains', 'relation': 'relations',
         'generalization': 'generalizations', 'constraint': 'constraints'}


def load():
    tables, schemas, inputs = {}, {}, {}
    for kind, name in MODEL.items():
        path = 'model/' + name + '.yaml'
        tables[kind] = yaml.safe_load((ROOT / path).read_text())['records']
        schema_path = 'model/schema/' + kind + '.schema.json'
        schemas[kind] = json.loads((ROOT / schema_path).read_text())
        for item in [path, schema_path]:
            inputs[item] = hashlib.sha256((ROOT / item).read_bytes()).hexdigest()
    for name, file, key, schema_kind in [
            ('FR', 'functional', 'records', 'need'), ('QR', 'quality', 'records', 'need'),
            ('LR', 'future', 'requirements', 'need'), ('CQ', 'competency-questions', 'records', 'cq'),
            ('LCQ', 'future', 'exploratory_questions', 'cq')]:
        path = 'requirements/' + file + '.yaml'
        tables[name] = yaml.safe_load((ROOT / path).read_text())[key]
        schema_path = 'requirements/schema/' + schema_kind + '.schema.json'
        schemas[name] = json.loads((ROOT / schema_path).read_text())
        for item in [path, schema_path]:
            inputs[item] = hashlib.sha256((ROOT / item).read_bytes()).hexdigest()
    for schema in schemas.values():
        Draft202012Validator.check_schema(schema)
    return tables, schemas, inputs


def inspect(tables, schemas):
    errors, seen = [], set()
    for name, rows in tables.items():
        validator = Draft202012Validator(schemas[name])
        for number, row in enumerate(rows, 1):
            for error in validator.iter_errors(row):
                errors.append({'code': 'schema_violation', 'table': name, 'row': number,
                               'id': row.get('id'), 'field': '/'.join(map(str, error.path)), 'reason': error.message})
            identity = row.get('id')
            if isinstance(identity, str):
                if identity in seen:
                    errors.append({'code': 'duplicate_id', 'table': name, 'row': number, 'id': identity})
                seen.add(identity)
                if name in ['FR', 'QR', 'LR', 'CQ', 'LCQ'] and not identity.startswith(name + '-'):
                    errors.append({'code': 'wrong_id_namespace', 'table': name, 'row': number, 'id': identity})
    return errors


def check():
    tables, schemas, inputs = load()
    errors = inspect(tables, schemas)
    if errors:
        raise ValueError(errors[:20])
    negatives = []
    for label, change, code in [
            ('missing model definition', lambda t: t['concept'][0].pop('definition'), 'schema_violation'),
            ('missing record ID', lambda t: t['domain'][0].pop('id'), 'schema_violation'),
            ('duplicate concept ID', lambda t: t['concept'].append(copy.deepcopy(t['concept'][0])), 'duplicate_id'),
            ('duplicate requirement ID', lambda t: t['FR'].append(copy.deepcopy(t['FR'][0])), 'duplicate_id'),
            ('missing adverse case', lambda t: t['QR'][0].pop('adverse_case'), 'schema_violation'),
            ('invalid origin', lambda t: t['FR'][0].update(origin='UNKNOWN'), 'schema_violation'),
            ('wrong CQ namespace', lambda t: t['CQ'][0].update(id='LCQ-99'), 'wrong_id_namespace'),
            ('fabricated computed answer', lambda t: t['CQ'][0].update(answer_status='computed'), 'schema_violation')]:
        changed = copy.deepcopy(tables)
        change(changed)
        if code not in {error['code'] for error in inspect(changed, schemas)}:
            raise AssertionError('Expected rejection missing: ' + label)
        negatives.append(label)
    return {'status': 'PASS', 'scope': 'Model/need/CQ record shapes and identifier uniqueness only',
            'counts': {name: len(rows) for name, rows in tables.items()}, 'negative_cases_rejected': negatives,
            'input_file_sha256': inputs,
            'limits': ['Counts describe the observed input, not fixed adequacy thresholds.',
                       'Schema validity does not establish endpoint integrity, satisfaction or philosophical soundness.']}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
