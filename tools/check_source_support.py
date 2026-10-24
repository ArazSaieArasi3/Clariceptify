from pathlib import Path
import copy,json,hashlib,yaml

ROOT=Path(__file__).resolve().parents[1]


def problems(sources,links,concepts):
    errors=[];source_ids={r['id'] for r in sources};concept_ids={r['id'] for r in concepts}
    if len(source_ids)!=len(sources):errors.append('duplicate_source')
    if len({r['concept_id'] for r in links})!=len(links):errors.append('duplicate_support')
    for r in links:
        if r['concept_id'] not in concept_ids:errors.append('dangling_concept')
        if any(s not in source_ids for s in r['source_ids']):errors.append('dangling_source')
        if r['support_type'] not in ['D','B','P']:errors.append('invalid_support_type')
        if r['passage_verification']!='not_reverified_in_import':errors.append('unsupported_passage_claim')
        if r['typing_approval']!='not_assessed':errors.append('unsupported_typing_claim')
    for c in concepts:
        r=next((r for r in links if r['concept_id']==c['id']),None)
        if not r or c['source_reference_ids']!=r['source_ids']:errors.append('binding_drift')
    return errors


def check():
    sources=yaml.safe_load((ROOT/'evidence/source-register.yaml').read_text())['records']
    links=yaml.safe_load((ROOT/'evidence/concept-support.yaml').read_text())['records']
    concepts=yaml.safe_load((ROOT/'model/concepts.yaml').read_text())['records']
    assert not problems(sources,links,concepts),problems(sources,links,concepts)
    assert len(sources)==53 and len(links)==len(concepts)==137
    negatives=[]
    for label,field,value,expected in [('absent source','source_ids',['CLR-SRC9999'],'dangling_source'),('fabricated passage verification','passage_verification','verified','unsupported_passage_claim'),('fabricated typing approval','typing_approval','approved','unsupported_typing_claim')]:
        changed=copy.deepcopy(links);changed[0][field]=value;assert expected in problems(sources,changed,concepts);negatives.append(label)
    from collections import Counter
    assert dict(Counter(r['support_type'] for r in links))=={'B':83,'D':44,'P':10}
    return {'status':'PASS','scope':'source/support registry integrity only','references':len(sources),'concept_support_records':len(links),'negative_cases_rejected':negatives,
            'files':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['evidence/source-register.yaml','evidence/concept-support.yaml','model/concepts.yaml']},
            'full_text_verification':'not_assessed'}


if __name__=='__main__':print(json.dumps(check(),indent=2))
