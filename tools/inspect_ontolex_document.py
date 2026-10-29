"""Inspect the pinned 2016 document structure; no ontology parsing or reasoning."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
import hashlib,json,re
SHA='ce0996a09f6ab97633c0aaad0b6eb02120615f2f4b8d5aa5c4b2558ce5f5c9b2'
URL='https://www.w3.org/2016/05/ontolex/'
def digest(b):return hashlib.sha256(b).hexdigest()
class Document(HTMLParser):
 def __init__(self):
  super().__init__();self.headings=[];self.images=[];self.anchors=[];self.heading=None;self.buffer=[];self.current=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.anchors.append(a['id'])
  if tag in ('h2','h3','h4'):
   self.heading={'level':int(tag[1]),'anchor':a.get('id')};self.buffer=[]
  if tag=='img' and 'logos/W3C' not in a.get('src',''):
   self.images.append({'url':urljoin(URL,a['src']),'relative_url':a['src'],'nearest_heading':self.current})
 def handle_data(self,data):
  if self.heading is not None:self.buffer.append(data)
 def handle_endtag(self,tag):
  if self.heading is not None and tag=='h'+str(self.heading['level']):
   h={**self.heading,'title':' '.join(''.join(self.buffer).split())}
   self.headings.append(h);self.current=h['anchor'];self.heading=None;self.buffer=[]
def inspect(path):
 b=Path(path).read_bytes()
 if digest(b)!=SHA:raise ValueError('Wrong source bytes')
 p=Document();p.feed(b.decode('utf-8'))
 numbered=[h for h in p.headings if re.match(r'^\d+(?:\.\d+)*\.? ',h['title'])]
 terms=[h for h in p.headings if h['title'].endswith(('(Class)','(Object Property)','(Datatype Property)'))]
 return {'source_sha256':SHA,'source_bytes':len(b),'source_url':URL,'headings':p.headings,'numbered_sections':numbered,'term_heading_inventory':terms,'images':p.images,'anchors':sorted(set(p.anchors)),'population_policy':'HTML headings and non-logo image occurrences; document terms are not a count of asserted or inferred ontology classes.','reasoner_execution':'NOT_EXECUTED'}
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('output',type=Path);a=p.parse_args();a.output.write_text(json.dumps(inspect(a.source),indent=2,sort_keys=True)+'\n')
