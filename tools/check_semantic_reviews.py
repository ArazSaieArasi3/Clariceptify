"""Versioned semantic-review integrity and explicitly bounded finite predicates."""
import argparse
import hashlib
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]
SLUGS = dict(zip(range(114,123), ['mental-content','process-product','description-referent','goal-intention-perspective','context-scope','quality-evaluation','sortal-identity','roles','modes-relators']))
class SemanticReviewError(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise SemanticReviewError(message)

def read(path):
    return yaml.safe_load((ROOT/path).read_text())

def validate(report, issue):
    require(report['issue']==issue, 'issue identity')
    require(report['status']=='BOUNDED_SEMANTIC_REVIEW_COMPLETE_WITH_OPEN_FINDINGS', 'review status')
    require(report['semantic_acceptance']=='not_assessed' and report['model_changes']=='none', 'semantic gate')
    require(report['expert_review']=='not_performed', 'expert gate')
    require(report['model_tree']=='3e2d5b627af1b92cdb70c6bd7198868fa784e977', 'model tree')
    require(len(report['baseline_commit'])==40, 'baseline ref')
    required={'model/concepts.yaml','model/relations.yaml','model/generalizations.yaml','model/constraints.yaml','evidence/concept-support.yaml','evidence/source-register.yaml','evidence/related-work/review-protocol.yaml','docs/decisions/artifact-authority.md','docs/decisions/artifact-versioning.md'}
    require(required<=report['input_bindings'].keys(), 'input family missing')
    for path,digest in report['input_bindings'].items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest, 'stale input '+path)
    require(report['bounded_commitment'] and len(report['case_review'])>1, 'substantive cases missing')
    sources={s['id']:s for s in report['source_refs']}
    require(sources and len(sources)==len(report['source_refs']), 'source identity')
    for ref in sources.values():
        path=ROOT/ref['path']; require(hashlib.sha256(path.read_bytes()).hexdigest()==ref['sha256'], 'source record drift')
        src=yaml.safe_load(path.read_text());require(src['id']==ref['id'], 'source mismatch')
        for field in ['url','locator','paraphrase','title']:
            require(src.get(field), 'source metadata missing '+field)
        require(src.get('authors') or src.get('editors'), 'source author/editor attribution missing')
        require(src.get('version',src.get('version_date')), 'source edition missing')
    all_ids=set();captured_ids=set()
    require(set(report['model_snapshot'])=={'model/concepts.yaml','model/relations.yaml','model/generalizations.yaml','model/constraints.yaml'}, 'missing snapshot family')
    for path,rows in report['model_snapshot'].items():
        actual={r['id']:r for r in read(path)['records']};all_ids.update(actual)
        captured_ids.update(r['id'] for r in rows)
        require(len({r['id'] for r in rows})==len(rows), 'duplicate model snapshot')
        for row in rows: require(row['id'] in actual and actual[row['id']]==row, 'model snapshot changed')
    require(report['findings'], 'findings missing')
    for i,f in enumerate(report['findings'],1):
        require(f['id']==f'SEM{issue}-F{i:02d}', 'finding identity')
        require(f['decision_gate']=='unapproved_joint_user_decision_129', 'decision promoted')
        require(f.get('observation',f.get('finding')), 'finding evidence missing')
        affected=set(f.get('model_ids',f.get('affected_ids',[])))
        require(affected<=all_ids, 'unknown affected id')
        require(affected<=captured_ids, 'cited snapshot missing')
        require(set(f.get('source_ids',f.get('sources',[])))<=sources.keys(), 'unknown source')
    return len(report['findings'])

# These predicates implement only named finite examples. They are not a native
# OntoUML validator, empirical cognitive measurement or full constraint execution.
# Empty sets are explicitly complete synthetic fixture data, not missing-world
# information; a failed empty-union test does not establish referent nonexistence.
def single_bearer(bearers):
    return len(set(bearers))==1

def shared_distinct_agents(state_bearers, participants):
    return len(set(state_bearers))>=2 and set(state_bearers)<=set(participants)

def one_origin(origins):
    return len(set(origins))==1

def exclusive_referent(branch_targets):
    return sum(len(set(targets)) for targets in branch_targets.values())==1

def aligned_agent(bearer,participants):
    return bearer in participants

def atomic_result(artifacts,criteria,origins,episode_artifacts,episode_criteria):
    return (len(set(artifacts))==len(set(criteria))==len(set(origins))==1
            and set(artifacts)<=set(episode_artifacts) and set(criteria)<=set(episode_criteria))

def finite_checks(issue):
    checks={
      114:lambda:[('one bearer',single_bearer(['a']),True),('two bearers',single_bearer(['a','b']),False),('shared distinct agents',shared_distinct_agents(['a','b'],['a','b']),True),('same-agent states not shared',shared_distinct_agents(['a','a'],['a','b']),False)],
      115:lambda:[('one origin',one_origin(['e1']),True),('second origin',one_origin(['e1','e2']),False),('unknown origin not accepted',one_origin([]),False)],
      116:lambda:[('one referent',exclusive_referent({'object':[],'event':['e']}),True),('empty union',exclusive_referent({'object':[],'event':[]}),False),('two branches',exclusive_referent({'object':['o'],'event':['e']}),False)],
      117:lambda:[('aligned bearer',aligned_agent('a',['a','b']),True),('nonparticipant bearer',aligned_agent('c',['a','b']),False)],
      119:lambda:[('atomic aligned result',atomic_result(['a'],['c'],['e'],['a'],['c']),True),('two criteria',atomic_result(['a'],['c','d'],['e'],['a'],['c','d']),False),('wrong target',atomic_result(['b'],['c'],['e'],['a'],['c']),False)],
      122:lambda:[('single mode bearer',single_bearer(['r']),True),('orphan mode',single_bearer([]),False),('duplicate distinct bearers',single_bearer(['r','s']),False)]}.get(issue,lambda:[])()
    for label,observed,expected in checks: require(observed==expected,'finite predicate '+label)
    return len(checks)

def structural_checks(issue):
    if issue not in {120,121,122}:
        return []
    concepts={r['id']:r for r in read('model/concepts.yaml')['records']}
    gens=read('model/generalizations.yaml')['records'];relations=read('model/relations.yaml')['records']
    def ancestors(cid):
        seen=set();todo=[cid]
        while todo:
            child=todo.pop()
            for g in gens:
                if g['child_id']==child and g['parent_id'] not in seen:
                    seen.add(g['parent_id']);todo.append(g['parent_id'])
        return seen
    if issue==120:
        kinds=[cid for cid,c in concepts.items() if c['ontouml_stereotype']=='«kind»']
        require(kinds==['CLR-C0057'],'declared kind census changed')
        require('CLR-C0083' in ancestors('CLR-C0057'),'information object hierarchy')
        return ['one declared kind, graph ancestor confirmed; identity semantics not proven']
    if issue==121:
        roles=[cid for cid,c in concepts.items() if c['ontouml_stereotype']=='«role»']
        require(set(roles)=={'CLR-C0007','CLR-C0010','CLR-C0042','CLR-C0088','CLR-C0137'},'role census changed')
        for cid in roles:
            providers={p for p in ancestors(cid) if concepts[p]['ontouml_stereotype']=='«kind»'}
            require(providers=={'CLR-C0057'},'role identity-provider path')
        return ['five role identity-provider paths checked; anti-rigidity not mechanically proven']
    modes=[cid for cid,c in concepts.items() if c['ontouml_stereotype']=='«mode»']
    require(len(modes)==8,'mode census changed')
    for cid in modes+['CLR-C0058','CLR-C0062']:
        rows=[r for r in relations if r['ontouml_stereotype']=='«characterization»' and r['target_id'] in ancestors(cid)|{cid}]
        require(len(rows)==1 and rows[0]['source_multiplicity']=='1','mode bearer path')
    require(not any(c['ontouml_stereotype']=='«relator»' for c in concepts.values()),'relator baseline changed')
    require(not any(r['ontouml_stereotype']=='«mediation»' for r in relations),'mediation baseline changed')
    return ['eight modes and two inherited subkind bearer paths checked; zero declared relators/mediations, not a defect claim']

def main():
    p=argparse.ArgumentParser();p.add_argument('--issue',type=int,choices=range(114,123),required=True);n=p.parse_args().issue
    findings=validate(read('evaluation/semantic-reviews/'+SLUGS[n]+'.yaml'),n);count=finite_checks(n)
    for observation in structural_checks(n):print('STRUCTURAL_OBSERVATION:',observation)
    print(f'PASS: review {n} integrity, {findings} open findings, {count} finite predicate checks; not complete model semantics or expert approval')
if __name__=='__main__':main()
