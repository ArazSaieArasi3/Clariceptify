#!/usr/bin/env python3
"""Validate source identities and matrix coverage for the bounded third comparison."""
from pathlib import Path
import hashlib
import yaml

ROOT=Path(__file__).resolve().parents[1]
DIMENSIONS={'agency_activity','content_expression_referent','episode_decision_rationale','formal_evaluation_limits'}
WORKS={'OntoLex','SKOS','EmotionsCognition'}


def check(root=ROOT):
    d=yaml.safe_load((root/'evidence/related-work/comparisons/batch-3.yaml').read_text())
    assert (d['batch_id'],d['issue'],d['scope']['synthesis_target'])==('R2-CMP-003',253,126)
    assert d['model']['accepted_equivalences']==[] and d['scope']['owner_decision']=='OWNER_DECISION_REQUIRED'
    model=root/d['model']['path']
    assert hashlib.sha256(model.read_bytes()).hexdigest()==d['model']['sha256']
    ids={x['id'] for x in yaml.safe_load(model.read_text())['records']}
    sources=d['source_columns']
    assert set(sources)==WORKS
    for name,s in sources.items():
        p=s.get('document',s.get('paper'))
        r=yaml.safe_load((root/p['review']).read_text())
        recorded=(r['identity']['source_sha256'] if name!='EmotionsCognition' else r['source']['sha256'])
        assert recorded==p['sha256'],name
        a=yaml.safe_load((root/s['artifact']['review']).read_text())
        digest=(a['source']['selected_core']['sha256'] if name=='OntoLex' else
                a['source']['selected_root_sha256'] if name=='SKOS' else a['identity']['selected_sha256'])
        assert digest==s['artifact']['sha256'],name
        assert (root/s['artifact']['class_catalog']).exists()
        assert (root/s['repository']['discovery']).exists()
        assert s['access_license']['raw_redistributed'] is False
        assert s['foundation']['alignment']=='NOT_ACCEPTED'
        assert s['classes']['glossary_complete_for_selected_root'] is True
    cells=d['matrix'];assert len(cells)==12 and len({c['id'] for c in cells})==12
    assert {(c['work'],c['dimension']) for c in cells}=={(w,dim) for w in WORKS for dim in DIMENSIONS}
    for c in cells:
        assert set(c['model_ids'])<=ids
        assert all(c[k] for k in ('paper_locators','artifact_locators','native_support','required_specialization','unsupported_inference','counterevidence','unknowns'))
        assert all('yaml' in x or 'census' in x for x in c['artifact_locators'])
    assert d['scenario']['common'] and d['scenario']['adverse'] and d['scenario']['status']=='CONCEPTUAL_REVIEW_ONLY'
    for v in d['candidate_mappings']:
        assert set(v['model_ids'])<=ids
        assert set(v['supporting_cells']+v['contrary_cells'])<={c['id'] for c in cells}
        assert v['status']=='OWNER_DECISION_REQUIRED' and v['equivalence']=='NOT_ESTABLISHED'
    assert d['synthesis_export']['target_issue']==126 and d['limits']['no_corpus_wide_novelty_claim'] is True
    assert d['limits']['model_change']=='NONE' and d['limits']['raw_external_sources_redistributed'] is False
    print('R2-CMP-003: three pinned sources, 12 cells, model IDs, adverse scenario and synthesis boundaries PASS')

if __name__=='__main__':check()
