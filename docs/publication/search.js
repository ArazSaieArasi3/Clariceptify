'use strict';
fetch('concept-index.json').then(response=>response.json()).then(records=>{
  const query=document.getElementById('query'), results=document.getElementById('results'), count=document.getElementById('count');
  function show(){
    const terms=query.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    const selected=records.filter(row=>terms.every(term=>(row.id+' '+row.name+' '+row.definition+' '+row.domain).toLowerCase().includes(term)));
    count.textContent=selected.length+' of '+records.length+' concepts';results.replaceChildren();
    selected.forEach(row=>{const card=document.createElement('article'), heading=document.createElement('h2'), link=document.createElement('a'), meta=document.createElement('p'), definition=document.createElement('p');link.href=row.url;link.textContent=row.id+' · '+row.name;heading.append(link);meta.textContent=row.domain+' · '+row.stereotype;definition.textContent=row.definition;card.append(heading,meta,definition);results.append(card);});
  }
  query.addEventListener('input',show);show();
}).catch(()=>{document.getElementById('count').textContent='Search could not load. Use the complete catalogue.';});
