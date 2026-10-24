"""Offline bootstrap contract checks; these do not validate ontology semantics."""
from pathlib import Path
import json
import re
import copy
import hashlib
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def check():
    results = []
    def record(name, condition):
        if not condition:
            raise AssertionError(name)
        results.append(name)

    schemas = {p.stem.removesuffix('.schema'): json.loads(p.read_text())
               for p in (ROOT/'model/schema').glob('*.schema.json')}
    record('five declared record schema families', len(schemas) == 5)
    for name, schema in schemas.items():
        Draft202012Validator.check_schema(schema)
        record('valid JSON Schema: '+name, True)
    base = {'lifecycle': 'candidate', 'introduced_version': 'input-r1-rev1',
            'source_locator': 'fixture:synthetic-record'}
    valid = {
        'concept': dict(base, id='CLR-C0001', label_en='Example', definition='A synthetic contract example.',
                        ufo_type='Endurant / information object', ontouml_stereotype='subkind',
                        primary_domain_id='CLR-D0001', is_abstract=None),
        'domain': dict(base, id='CLR-D0001', label_en='Example domain', purpose='A synthetic purpose.',
                       description='A schema fixture, not a proposed subject domain.', layer='subject'),
        'relation': dict(base, id='CLR-R0001', label_en='represents', source_id='CLR-C0001', target_id='CLR-C0002',
                         source_multiplicity='0..*', target_multiplicity='1', ontouml_stereotype=None, connector='solid'),
        'generalization': dict(base, id='CLR-G0001', child_id='CLR-C0002', parent_id='CLR-C0001',
                               set_completeness='unknown', set_disjointness='unknown'),
        'constraint': dict(base, id='CLR-SC0001', text='A synthetic textual contract.', referenced_ids=['CLR-C0001'],
                           enforcement='textual', execution_status='not_executed'),
    }
    for name, item in valid.items():
        record('positive fixture accepted: '+name, not list(Draft202012Validator(schemas[name]).iter_errors(item)))
    negative = []
    item=copy.deepcopy(valid['concept']);del item['definition'];negative.append(('concept','missing definition',item))
    item=copy.deepcopy(valid['concept']);item['id']='Example v1';negative.append(('concept','label/version as identity',item))
    item=copy.deepcopy(valid['domain']);item['layer']='new independent module';negative.append(('domain','invented layer',item))
    item=copy.deepcopy(valid['relation']);item['target_multiplicity']='N/A';negative.append(('relation','association with N/A cardinality',item))
    item=copy.deepcopy(valid['relation']);item['target_id']='CLR-R0002';negative.append(('relation','relation ID used as concept endpoint',item))
    item=copy.deepcopy(valid['generalization']);item['source_multiplicity']='0..*';negative.append(('generalization','association field on generalization',item))
    item=copy.deepcopy(valid['generalization']);item['set_completeness']='assumed complete';negative.append(('generalization','unqualified set completeness',item))
    item=copy.deepcopy(valid['constraint']);item['execution_status']='proven';negative.append(('constraint','unsupported execution state',item))
    item=copy.deepcopy(valid['constraint']);item['referenced_ids']=['CLR-C0001','CLR-C0001'];negative.append(('constraint','duplicate affected reference',item))
    for name, reason, item in negative:
        record('negative fixture rejected: '+reason, bool(list(Draft202012Validator(schemas[name]).iter_errors(item))))

    # Ledger is explicitly a candidate read model, not an accepted semantic registry.
    ledger=yaml.safe_load((ROOT/'traceability/migration/entity-ledger.yaml').read_text())
    rows=ledger['selected_concepts']
    record('selected input has 137 reservations', len(rows)==137)
    record('reservation keys unique',len({x['proposed_record_id'] for x in rows})==len(rows))
    record('source locators unique',len({x['source_locator'] for x in rows})==len(rows))
    record('reservations remain semantically unaccepted',all(x['reservation_status']=='reserved_not_semantically_accepted' for x in rows))
    links=[v for row in rows for v in row['legacy_candidates']]
    record('all label-based candidates remain unassessed',all(v['semantic_identity']=='not_assessed' and v['correspondence_status'].startswith('candidate_') for v in links))
    record('legacy IDs qualified by source family/ref',all(v['source_commit'] and v['source_registry'] and v['source_family'] for v in links))

    integrity=yaml.safe_load((ROOT/'traceability/migration/input-integrity.yaml').read_text())
    for row in integrity['records']:
        if row['verification']=='bytes_hashed':
            record('input digest syntax: '+row['source_id'],bool(re.fullmatch('[0-9a-f]{64}',row['sha256'])))
            record('input byte count: '+row['source_id'],isinstance(row['size_bytes'],int) and row['size_bytes']>0)
        else:
            record('unmaterialized digest explicitly absent: '+row['source_id'],row['sha256'] is None)
    record('ledger bound to selected source digest', ledger['source_spec_sha256']==integrity['records'][0]['sha256'])
    manifest=yaml.safe_load((ROOT/'.research/manifest.yaml').read_text())
    profile=yaml.safe_load((ROOT/'.research/ogcm-rf-profile.yaml').read_text())
    record('research identity consistent',manifest['research']['id']==profile['implementation']['research_id']=='R-001')
    record('repository is local destination',manifest['repository']['name']=='Clariceptify' and profile['implementation']['repository']=='ArazSaieArasi3/Clariceptify')
    record('method ref pinned consistently',profile['framework']['framework_ref']==manifest['methodology']['ogcm_rf']['framework_ref'] and bool(re.fullmatch('commit:[0-9a-f]{40}',profile['framework']['framework_ref'])))
    record('conformance remains not assessed',profile['framework']['conformance_level']=='not_assessed')
    record('stable semantic release and ontology IRI absent',profile['identity_and_release']['current_semantic_release'] is None and profile['identity_and_release']['ontology_iri'] is None)
    for md in ROOT.rglob('*.md'):
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',md.read_text()):
            if re.match(r'^[a-z]+:',target) or target.startswith('#'):
                continue
            record('local link resolves: '+str(md.relative_to(ROOT))+':'+target,(md.parent/target.split('#')[0]).exists())
    files={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
           for p in sorted(ROOT.rglob('*')) if p.is_file() and '.git' not in p.parts
           and '__pycache__' not in p.parts and p.name!='bootstrap-report.json'}
    return {'status':'PASS','scope':'local bootstrap contracts and candidate-ledger integrity only',
            'checks_passed':len(results),'positive_schema_fixtures':5,'negative_schema_fixtures':len(negative),
            'checks':results,'checked_file_sha256':files,
            'not_assessed':['semantic adequacy','full OntoUML validity','joint satisfiability','requirement satisfaction',
                            'expert acceptance','actual public release or DOI','unmaterialized input bytes']}


if __name__=='__main__':
    result=check()
    print(json.dumps(result,ensure_ascii=False,indent=2))
