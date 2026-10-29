"""Inspect exact SKOS Reference HTML; no RDF parsing or semantic execution."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
import hashlib,json,re
SHA='3aa00cd16ee4d86d3a19b75501bb317d0b0c134e1f4029e9f3098c4dd3669e4c'
URL='https://www.w3.org/TR/2009/REC-skos-reference-20090818/'
ERRATA_SHA='463583300db10b416a14f1b082a0e4f2852396637eddf9202126c1b2787ec802'
ERRATA_URL='https://www.w3.org/2006/07/SWD/SKOS/reference/20090811-errata'
def digest(b):return hashlib.sha256(b).hexdigest()
def norm(s):return ' '.join(s.split())
class Node:
 def __init__(self,tag='',attrs=None,parent=None):self.tag=tag;self.attrs=attrs or {};self.parent=parent;self.children=[]
 def text(self):return ''.join(c if isinstance(c,str) else c.text() for c in self.children)
 def walk(self):
  yield self
  for c in self.children:
   if isinstance(c,Node):yield from c.walk()
 def ancestor(self,tag):
  n=self
  while n and n.tag!=tag:n=n.parent
  return n
class Document(HTMLParser):
 def __init__(self):super().__init__();self.root=Node();self.current=self.root
 def handle_starttag(self,tag,attrs):
  n=Node(tag,dict(attrs),self.current);self.current.children.append(n)
  if tag not in {'meta','link','img','br','hr','input','area','base','embed','param','source','track','wbr'}:self.current=n
 def handle_startendtag(self,tag,attrs):self.handle_starttag(tag,attrs);self.handle_endtag(tag)
 def handle_endtag(self,tag):
  n=self.current
  while n.parent and n.tag!=tag:n=n.parent
  if n.parent:self.current=n.parent
 def handle_data(self,data):self.current.children.append(data)
def inspect(path):
 b=Path(path).read_bytes()
 if digest(b)!=SHA:raise ValueError('Wrong source bytes')
 p=Document();p.feed(b.decode('utf-8')); nodes=list(p.root.walk()); headings=[];statements=[];examples=[];diagrams=[];images=[];anchors=[];nearest=None
 for n in nodes:
  ident=n.attrs.get('id'); text=norm(n.text())
  if ident:anchors.append(ident)
  if re.fullmatch('h[1-6]',n.tag):
   nested=next((x.attrs['id'] for x in n.walk() if 'id' in x.attrs),None)
   siblings=n.parent.children if n.parent else []; pos=siblings.index(n) if n.parent else 0
   previous=next((x.attrs.get('id') for x in reversed(siblings[:pos]) if isinstance(x,Node) and x.tag=='a' and x.attrs.get('id')),None)
   anchor=ident or nested or previous
   if anchor:nearest=anchor
   headings.append({'key':f'H{len(headings)+1:03}','level':int(n.tag[1]),'anchor':anchor,'locator_anchor':anchor or nearest,'title':text})
  if ident and re.fullmatch('S[0-9]+',ident):
   row=n.ancestor('tr');statements.append({'id':ident,'section_anchor':nearest,'normalized_row_sha256':digest(norm(row.text()).encode())})
  if ident and re.fullmatch('example-[0-9]+',ident):
   table=n.ancestor('table');examples.append({'id':ident,'label':text,'section_anchor':nearest,'normalized_table_sha256':digest(norm(table.text()).encode())})
  if n.tag=='pre' and ('+—' in n.text() or '+-' in n.text()):diagrams.append({'id':f'TD{len(diagrams)+1:02}','section_anchor':nearest,'normalized_sha256':digest(text.encode()),'kind':'TEXT_SUBPROPERTY_TREE'})
  if n.tag=='img':images.append({'url':urljoin(URL,n.attrs.get('src','')),'alt':n.attrs.get('alt'),'role':'BADGE_NOT_CONTENT_FIGURE'})
 sections=[x for x in headings if re.match(r'^(?:\d+\.|[A-D]\.\d|Appendix [A-D]\.)',x['title'])]
 return {'source_sha256':SHA,'source_bytes':len(b),'source_url':URL,'headings':headings,'sections':sections,'statements':statements,'examples':examples,'text_diagrams':diagrams,'images':images,'anchors':sorted(set(anchors)),'counts':{'sections':len(sections),'semantic_statements':len(statements),'numbered_examples':len(examples),'text_diagrams':len(diagrams),'substantive_image_figures':0,'badges':len(images)},'population_policy':'Document headings, prose statements, examples and text diagrams only; not executable ontology class populations.','reasoner_execution':'NOT_EXECUTED'}
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('output',type=Path);a=p.parse_args();a.output.write_text(json.dumps(inspect(a.source),indent=2,sort_keys=True)+'\n')
