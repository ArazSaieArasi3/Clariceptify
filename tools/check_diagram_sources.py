"""Validate the source/approval contracts; optionally audit recovered private inputs."""
from pathlib import Path
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
import zipfile
import yaml
ROOT = Path(__file__).resolve().parents[1]
NS = {'s': 'http://www.w3.org/2000/svg', 'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def check(directory=None):
    manifest = yaml.safe_load((ROOT / 'model/diagrams/source-manifest.yaml').read_text())
    approval = yaml.safe_load((ROOT / 'model/diagrams/approval-state.yaml').read_text())
    records = {r['source_id']: r for r in manifest['inputs']}
    if not set(records) == {'SRC-SVG', 'SRC-FULLPDF', 'SRC-ATLAS', 'SRC-SPEC'}:
        raise ValueError("Diagram source contract mismatch: set(records) == {'SRC-SVG', 'SRC-FULLPDF', 'SRC-ATLAS', 'SRC-SPEC'}")
    if not len(records) == len(manifest['inputs']):
        raise ValueError("Diagram source contract mismatch: len(records) == len(manifest['inputs'])")
    for sid, r in records.items():
        if not (len(r['sha256']) == 64 and int(r['sha256'], 16) >= 0):
            raise ValueError("Diagram source contract mismatch: len(r['sha256']) == 64 and int(r['sha256'], 16) >= 0")
        if not (r['size_bytes'] > 0 and r['raw_distribution'] == 'not_committed'):
            raise ValueError("Diagram source contract mismatch: r['size_bytes'] > 0 and r['raw_distribution'] == 'not_committed'")
        if not approval['input_sha256'][sid] == r['sha256']:
            raise ValueError("Diagram source contract mismatch: approval['input_sha256'][sid] == r['sha256']")
    if not manifest['editable_source']['native_ontouml_project'] == 'not_recovered':
        raise ValueError("Diagram source contract mismatch: manifest['editable_source']['native_ontouml_project'] == 'not_recovered'")
    if not manifest['editable_source']['original_generator'] == 'not_recovered':
        raise ValueError("Diagram source contract mismatch: manifest['editable_source']['original_generator'] == 'not_recovered'")
    if not approval['decision']['human_scientific_acceptance'] == 'not_established_by_available_evidence':
        raise ValueError("Diagram source contract mismatch: approval['decision']['human_scientific_acceptance'] == 'not_established_by_available_evidence'")
    if not approval['decision']['canonical_model_state'] == 'imported_candidate':
        raise ValueError("Diagram source contract mismatch: approval['decision']['canonical_model_state'] == 'imported_candidate'")
    checks = ['source IDs unique and complete', 'sizes and SHA-256 formats valid', 'approval bindings equal source bindings', 'native source and generator limitations preserved', 'candidate and unverified scientific acceptance preserved']
    if directory is not None:
        directory = Path(directory)
        for sid, r in records.items():
            b = (directory / r['filename']).read_bytes()
            if not (len(b) == r['size_bytes'] and hashlib.sha256(b).hexdigest() == r['sha256']):
                raise ValueError(sid)
        t = ET.parse(directory / records['SRC-SVG']['filename'])
        if not len(t.findall('.//s:g[@class="node"]', NS)) == 137:
            raise ValueError('Diagram source contract mismatch: len(t.findall(\'.//s:g[@class="node"]\', NS)) == 137')
        edges = t.findall('.//s:g[@class="edge"]', NS)
        if not len(edges) == 296:
            raise ValueError('Diagram source contract mismatch: len(edges) == 296')
        if not sum((e.get('data-stereotype') == 'Generalization' for e in edges)) == 122:
            raise ValueError("Diagram source contract mismatch: sum((e.get('data-stereotype') == 'Generalization' for e in edges)) == 122")
        if not 'approved specification' in t.find('s:desc', NS).text:
            raise ValueError("Diagram source contract mismatch: 'approved specification' in t.find('s:desc', NS).text")
        with zipfile.ZipFile(directory / records['SRC-SPEC']['filename']) as z:
            doc = ET.fromstring(z.read('word/document.xml'))
        body = doc.find('w:body', NS)
        paragraphs = [''.join((t.text or '' for t in p.findall('.//w:t', NS))) for p in body.findall('w:p', NS)]
        if not 'review candidate' in paragraphs[2]:
            raise ValueError("Diagram source contract mismatch: 'review candidate' in paragraphs[2]")
        if not 'owner approval' in paragraphs[3]:
            raise ValueError("Diagram source contract mismatch: 'owner approval' in paragraphs[3]")
        checks += ['all four recovered input sizes and digests verified', 'SVG named 137 nodes and 296 edges including 122 generalizations', 'actual SVG desc approval wording and DOCX paragraphs 3/4 conflict verified']
    return {'status': 'PASS', 'scope': 'Source identity and approval evidence only; no semantic acceptance or complete visual parity', 'private_input_audit': 'performed' if directory else 'not_run', 'checks': checks, 'input_sha256': {sid: r['sha256'] for sid, r in records.items()}}
if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--inputs')
    a = p.parse_args()
    print(json.dumps(check(a.inputs), indent=2, sort_keys=True))
