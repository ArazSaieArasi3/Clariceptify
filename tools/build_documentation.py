"""Project controlled English guide/registers into source-bound HTML and Wiki views."""
from pathlib import Path
from html import escape,unescape
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import argparse,hashlib,json,posixpath,re,shutil
import markdown,yaml

ROOT=Path(__file__).resolve().parents[1]
REPO='https://github.com/ArazSaieArasi3/Clariceptify'
GUIDES=['Home','Overview','Conceptual-Model','Requirements-and-CQs','Sources','Quality','Visualization','Reproduce','Versions','Citation','Limitations','Research-Roadmap']
NAV=[('index.html','Overview'),('concepts.html','Concepts'),('domains.html','Domains'),('relations.html','Relations'),('requirements.html','Requirements / CQs'),('quality.html','Evidence'),('diagram.html','Diagram'),('roadmap.html','Research'),('search.html','Search'),('downloads.html','Downloads')]
ALLOWED_DIRS={'.github','.research','docs','model','requirements','evidence','traceability','evaluation','tools','releases'}
ROOT_FILES={'README.md','CHANGELOG.md','CONTRIBUTING.md','CITATION.cff','LICENSE','LICENSE-MIT','LICENSE-CC-BY-4.0','THIRD-PARTY-NOTICES.md','requirements-dev.txt','requirements-docs.txt','requirements-diagrams.txt','AGENTS.md','.gitignore'}
SUFFIXES={'.md','.yaml','.yml','.json','.jsonl','.csv','.svg','.pdf','.png','.jpg','.jpeg','.webp','.py','.txt','.cff','.bib','.css','.js'}

def digest(data):return hashlib.sha256(data).hexdigest()
def encoded(data):return (json.dumps(data,indent=2,sort_keys=True)+'\n').encode()
def inventory(root):
    result={}
    for p in root.rglob('*'):
        if not p.is_file() or p.is_symlink() or '__pycache__' in p.parts or '.git' in p.parts:continue
        name=p.relative_to(root).as_posix();first=name.split('/')[0]
        if name in ROOT_FILES or (first in ALLOWED_DIRS and p.suffix in SUFFIXES):result[name]=p
    return result
def destination(name):return 'source/'+str(Path(name).with_suffix('.html')) if name.endswith('.md') else 'source/'+name
def link_for(name,page):return posixpath.relpath(destination(name),posixpath.dirname(page) or '.')
def guide_wiki(root,source_ref):
    views={}
    for name in GUIDES:
        p=root/'docs/guide'/f'{name}.md';text=p.read_text()
        def replace(match):
            label,target=match.group(1),match.group(2)
            if urlsplit(target).scheme or target.startswith('#'):return match.group(0)
            path,sep,fragment=target.partition('#');resolved=posixpath.normpath(posixpath.join('docs/guide',path))
            if resolved in {f'docs/guide/{g}.md' for g in GUIDES}:return '['+label+']('+Path(resolved).stem+(sep+fragment if sep else '')+')'
            return '['+label+']('+REPO+'/blob/'+source_ref+'/'+resolved+(sep+fragment if sep else '')+')'
        views[name+'.md']=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',replace,text)
    views['_Sidebar.md']='# Reader guide\n\n'+'\n'.join('- ['+g.replace('-',' ')+']('+g+')' for g in GUIDES)+'\n'
    views['_Footer.md']='Scientific core [v0.1.0]('+REPO+'/releases/tag/v0.1.0) | Documentation v0.1.1 | [Limitations](Limitations)\n'
    return views

def wiki_publication_plan():
    # GitHub's native title is not the Markdown filename stem: literal hyphens
    # become a different page from the controlled space-separated title slug.
    return [{'source_file':name+'.md','native_title':name.replace('-',' '),
             'wiki_slug':name} for name in GUIDES+['_Sidebar','_Footer']]

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.add(attrs['id'])
        for key in ('href','src','data'):
            if key in attrs:self.links.append(attrs[key])

def audit_site(folder):
    folder=Path(folder);pages={}
    for p in folder.rglob('*.html'):
        parser=Links();parser.feed(p.read_text());pages[p.relative_to(folder).as_posix()]=parser
    broken=[];links=0
    for name,parser in pages.items():
        for url in parser.links:
            parts=urlsplit(unescape(url))
            if parts.scheme or parts.netloc or url.startswith('data:'):continue
            links+=1;target=posixpath.normpath(posixpath.join(posixpath.dirname(name),unquote(parts.path))) if parts.path else name
            if not (folder/target).exists():broken.append({'page':name,'url':url,'kind':'missing_path'})
            elif parts.fragment and target in pages and parts.fragment not in pages[target].ids:broken.append({'page':name,'url':url,'kind':'missing_anchor'})
    if broken:raise ValueError('Broken generated links: '+json.dumps(broken[:12]))
    return {'status':'PASS','html_pages':len(pages),'local_links_checked':links,'broken_links':0}

def build(root,output,source_ref,version='v0.1.1'):
    root=Path(root).resolve();output=Path(output).resolve()
    if output.is_relative_to(root):raise ValueError('Keep documentation output outside its source tree')
    if output.exists():shutil.rmtree(output)
    output.mkdir(parents=True);files=inventory(root);inputs={n:digest(p.read_bytes()) for n,p in sorted(files.items())}
    css=(root/'docs/publication/site.css').read_text();(output/'site.css').write_text(css)
    def shell(title,body,page):
        prefix=posixpath.relpath('.',posixpath.dirname(page) or '.')
        nav=''.join('<a href="'+prefix+'/'+p+'"'+(' aria-current="page"' if p==page else '')+'>'+escape(t)+'</a>' for p,t in NAV)
        side=''.join('<li><a href="'+link_for('docs/guide/'+g+'.md',page)+'">'+escape(g.replace('-',' '))+'</a></li>' for g in GUIDES)
        return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Clariceptify conceptualization knowledge reference and evidence"><title>'+escape(title)+' | Clariceptify</title><link rel="stylesheet" href="'+prefix+'/site.css"></head><body><a class="skip" href="#content">Skip to content</a><header><a class="brand" href="'+prefix+'/index.html">Clariceptify</a><p>Conceptualization knowledge · core v0.1.0 · documentation '+escape(version)+'</p><nav aria-label="Primary">'+nav+'</nav></header><div class="layout"><aside aria-label="Reader guide"><h2>Reader guide</h2><ul>'+side+'</ul><p><a href="'+REPO+'/wiki">GitHub Wiki</a></p><p><a href="'+prefix+'/publication-manifest.json">Source and version</a></p><p><a href="https://arazsaiearasi3.github.io/Clariceptify/versions.html">Current and frozen versions</a></p></aside><main id="content">'+body+'</main></div><footer>Conceptual baseline, candidate scientific commitments. <a href="'+link_for('docs/known-limitations.md',page)+'">Evidence limits</a> · <a href="'+REPO+'/releases/tag/v0.1.0">Published core</a> · <a href="'+REPO+'">Repository</a><p>Source '+escape(source_ref)+' · This reader projection does not add semantic or expert acceptance.</p></footer></body></html>'
    def render_md(name,page=None):
        page=page or destination(name)
        body=markdown.markdown(files[name].read_text(),extensions=['tables','fenced_code','toc','sane_lists'])
        def rewrite(match):
            key,url=match.group(1),unescape(match.group(2));parts=urlsplit(url)
            if parts.scheme or parts.netloc or url.startswith('#'):return match.group(0)
            target=posixpath.normpath(posixpath.join(posixpath.dirname(name),unquote(parts.path)))
            if target.startswith('../') or target.startswith('/'):raise ValueError('Source link escapes repository: '+url)
            if target in files:out=link_for(target,page)
            elif (root/target).is_dir():out=posixpath.relpath('source/'+target.rstrip('/')+'/index.html',posixpath.dirname(page) or '.')
            else:raise ValueError('Source link target missing: '+name+' -> '+target)
            if parts.fragment:out+='#'+parts.fragment
            return key+'="'+escape(out,quote=True)+'"'
        body=re.sub(r'(href|src)="([^"]+)"',rewrite,body)
        title=next((line.lstrip('# ') for line in files[name].read_text().splitlines() if line.startswith('# ')),Path(name).stem)
        return shell(title,body,page)
    def write(page,data):
        p=output/page;p.parent.mkdir(parents=True,exist_ok=True)
        if isinstance(data,bytes):p.write_bytes(data)
        else:p.write_text(data)
    for name,path in sorted(files.items()):
        write(destination(name),render_md(name) if name.endswith('.md') else path.read_bytes())
    # Directory links are valid navigable projections, including documentation indexes.
    directories={str(Path(name).parent) for name in files}
    for name in list(directories):directories.update(str(p) for p in Path(name).parents)
    for directory in sorted(directories):
        if directory=='.':continue
        page='source/'+directory+'/index.html'
        children=sorted(n for n in files if str(Path(n).parent)==directory)
        body='<h1>'+escape(directory)+'</h1><ul>'+''.join('<li><a href="'+link_for(n,page)+'">'+escape(Path(n).name)+'</a></li>' for n in children)+'</ul>'
        write(page,shell(directory,body,page))
    for page,name in [('relations.html','docs/reference/relations/README.md'),('quality.html','docs/guide/Quality.md'),('roadmap.html','docs/guide/Research-Roadmap.md')]:write(page,render_md(name,page))
    concepts=yaml.safe_load((root/'model/concepts.yaml').read_text())['records'];domains=yaml.safe_load((root/'model/domains.yaml').read_text())['records']
    concepts_by_id={r['id']:r for r in concepts};domain_by_id={r['id']:r for r in domains}
    domain_body='<h1>Domains and responsibilities</h1><p>Twenty subject domains and Foundations. Primary membership is catalogue organization, not a completed domain adequacy assessment.</p><table><thead><tr><th>Domain</th><th>Purpose</th><th>Description</th></tr></thead><tbody>'
    for d in domains:domain_body+='<tr><td><a href="'+destination('docs/reference/domains/'+d['id']+'.md')+'">'+escape(d['label_en'])+'</a></td><td>'+escape(d['purpose'])+'</td><td>'+escape(d['description'])+'</td></tr>'
    write('domains.html',shell('Domains and responsibilities',domain_body+'</tbody></table>','domains.html'))
    downloads='<h1>Use the published baseline</h1><p><a href="'+REPO+'/releases/tag/v0.1.0">Actual v0.1.0 release, package and public checksums</a>. Documentation '+escape(version)+' presents unchanged scientific core v0.1.0.</p><h2>Diagrams and tables</h2><ul>'
    for name in ['model/diagrams/generated/full.svg','model/diagrams/generated/full.pdf','model/diagrams/generated/atlas.pdf']+sorted(n for n in files if n.startswith('docs/reference/exports/') and n.endswith('.csv')):downloads+='<li><a href="'+destination(name)+'">'+escape(Path(name).name)+'</a></li>'
    downloads+='</ul><h2>Citation and rights</h2><p><a href="'+destination('CITATION.cff')+'">CITATION.cff</a> · <a href="'+destination('LICENSE')+'">Scoped licenses</a> · <a href="'+destination('docs/guide/Reproduce.md')+'">Reproduce the baseline</a></p><p>Research material is CC-BY-4.0; original code is MIT under the scope notice. Source and typing qualifications remain explicit. No DOI is issued.</p>'
    write('downloads.html',shell('Use the published baseline',downloads,'downloads.html'))
    search=[{'id':r['id'],'name':r['label_en'],'definition':r['definition'],'domain':domain_by_id[r['primary_domain_id']]['label_en'],'stereotype':r['ontouml_stereotype'],'url':destination('docs/reference/concepts/'+r['id']+'.md')} for r in concepts]
    write('concept-index.json',encoded(search));write('search.js',(root/'docs/publication/search.js').read_bytes())
    search_body='<h1>Find a concept</h1><p>All 137 registered concepts; candidate definitions, stereotypes, domains and qualified sources.</p><label for="query">Search names, IDs and definitions</label><input id="query" type="search" autocomplete="off" placeholder="Conceptualization, intention, representation..."><p id="count" aria-live="polite"></p><div id="results"></div><script src="search.js" defer></script>'
    write('search.html',shell('Find a concept',search_body,'search.html'))
    table='<h1>Complete conceptual catalogue</h1><p><a href="search.html">Search all concepts</a>. Counts and presentation do not establish semantic adequacy.</p><table><thead><tr><th>ID / concept</th><th>Domain</th><th>OntoUML</th><th>Project definition</th></tr></thead><tbody>'
    for r in search:table+='<tr><td><a href="'+r['url']+'">'+escape(r['id']+' '+r['name'])+'</a></td><td>'+escape(r['domain'])+'</td><td>'+escape(r['stereotype'])+'</td><td>'+escape(r['definition'])+'</td></tr>'
    write('concepts.html',shell('Complete conceptual catalogue',table+'</tbody></table>','concepts.html'))
    cq=yaml.safe_load((root/'requirements/competency-questions.yaml').read_text())['records'];witness=yaml.safe_load((root/'traceability/requirements-model.yaml').read_text())['records'];witness={r['cq_id']:r for r in witness}
    body='<h1>Requirements and competency questions</h1><p>All thirty principal FR/CQ pairs. The ORSD is retrospective. Witnesses remain candidates; global execution is not performed.</p><table><thead><tr><th>IDs</th><th>Question</th><th>Expected / adverse case</th><th>Candidate concepts</th><th>Execution / answer</th></tr></thead><tbody>'
    for q in cq:
        w=witness[q['id']];links='; '.join('<a href="'+destination('docs/reference/concepts/'+i+'.md')+'">'+escape(concepts_by_id[i]['label_en'])+'</a>' for i in w['candidate_concept_ids'])
        body+='<tr id="'+q['id']+'"><td>'+escape(q['requirement_id']+' / '+q['id'])+'</td><td>'+escape(q['question'])+'</td><td>'+escape(q['acceptance'])+'<hr>'+escape(q['adverse_case'])+'</td><td>'+links+'</td><td>'+escape(q['test_execution']+' / '+q['answer_status'])+'</td></tr>'
    write('requirements.html',shell('Requirements and CQs',body+'</tbody></table>','requirements.html'))
    image=destination('model/diagrams/generated/full.svg')
    diagram='<h1>Read the complete diagram</h1><p>diagram-r1.2 · 137 concepts. Open the SVG to zoom or use the overlapping A3 atlas.</p><p><a href="'+image+'">Open full SVG</a> · <a href="'+destination('model/diagrams/generated/full.pdf')+'">Vector PDF</a> · <a href="'+destination('model/diagrams/generated/atlas.pdf')+'">A3 atlas</a></p><a href="'+image+'"><img src="'+image+'" alt="Complete Clariceptify OntoUML conceptual model, diagram revision r1.2"></a><p>Scoped element and paint-order checks are recorded; native OntoUML validation and independent expert review are not claimed.</p>'
    write('diagram.html',shell('Complete diagram',diagram,'diagram.html'))
    home='<h1>Make conceptualization knowledge inspectable</h1><p class="lead">Who conceptualizes, what is produced, how it is represented, and which reasons support the choices.</p><div class="note">Published conceptual baseline <strong>v0.1.0</strong>. Documentation '+escape(version)+' presents the same scientific core. Source support, CQ execution and expert-review qualifications remain explicit.</div><div class="cards">'
    for href,title,description in [('concepts.html','Understand the model','137 concepts across twenty subject domains and Foundations; complete definitions and qualified references.'),('requirements.html','Inspect requirements','Thirty FR/CQ contracts, candidate witnesses, expected answers and adverse cases.'),('diagram.html','Read the diagram','Same-source SVG, vector PDF and 69-page A3 detail atlas.'),('quality.html','Examine the evidence','Actual checks, owner scope acceptance, missing scientific evidence and the VVEAA plan.')]:home+='<article><h2>'+title+'</h2><p>'+description+'</p><a href="'+href+'">'+title+'</a></article>'
    home+='</div><h2>Read and reproduce</h2><p>Follow the reader guide, look up a term, inspect source qualifications or read the next research gates. Wiki and Pages are generated from one curated guide.</p><p><a href="'+destination('docs/guide/Home.md')+'">Read the guide</a> · <a href="search.html">Find a concept</a> · <a href="'+destination('docs/guide/Reproduce.md')+'">Reproduce the baseline</a> · <a href="roadmap.html">Release sequence</a></p>'
    write('index.html',shell('Conceptualization knowledge',home,'index.html'))
    wiki=guide_wiki(root,source_ref);wiki_dir=output/'wiki-source';wiki_dir.mkdir()
    for name,text in wiki.items():(wiki_dir/name).write_text(text)
    write('wiki-title-map.json',encoded(wiki_publication_plan()))
    write('publication-manifest.json',encoded({'status':'BUILD_IN_PROGRESS'}))
    audit=audit_site(output)
    outputs={p.relative_to(output).as_posix():digest(p.read_bytes()) for p in sorted(output.rglob('*')) if p.is_file() and p.relative_to(output).as_posix()!='publication-manifest.json'}
    record={'schema_version':'1.0','artifact_state':'BUILT','documentation_version':version,'scientific_core':'v0.1.0','source_commit':source_ref,'source_path_digest_sha256':digest(json.dumps(inputs,sort_keys=True,separators=(',',':')).encode()),'input_sha256':inputs,'output_sha256':outputs,'guide_pages':len(GUIDES),'wiki_files':len(wiki),'concepts':len(concepts),'domains':len(domains),'principal_cqs':len(cq),'audit':audit,'claim_boundary':'Reader projection and engineering checks; not new semantic/source/CQ/expert acceptance.'}
    write('publication-manifest.json',encoded(record));return record

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--output',type=Path,required=True);p.add_argument('--source-ref',required=True);p.add_argument('--version',default='v0.1.1');a=p.parse_args()
    result=build(a.root,a.output,a.source_ref,a.version);print(json.dumps({k:v for k,v in result.items() if k not in {'input_sha256','output_sha256'}},indent=2))
