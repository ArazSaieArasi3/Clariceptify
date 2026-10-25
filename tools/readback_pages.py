"""Compare actual public Pages bytes with the exact locally built manifests."""
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor
import argparse, hashlib, json, time


def fetch(base, path):
    request = Request(base.rstrip('/') + '/' + quote(path, safe='/'),
                      headers={'User-Agent': 'Clariceptify-publication-readback/1.0',
                               'Cache-Control': 'no-cache'})
    try:
        with urlopen(request, timeout=45) as response:
            if response.status != 200:
                raise ValueError(f'Unexpected public response: {path}')
            return response.read()
    except HTTPError as error:
        raise ValueError(f'Public readback HTTP {error.code}: {path}') from error


def readback(root, base, attempts=6):
    root = Path(root)
    expected_root = (root / 'publication-manifest.json').read_bytes()
    # A deployment can briefly serve its previous CDN generation. Never accept it.
    for attempt in range(attempts):
        actual_root = fetch(base, 'publication-manifest.json')
        if actual_root == expected_root:
            break
        if attempt + 1 == attempts:
            raise ValueError('Public deployment manifest differs from the exact build')
        time.sleep(5)
    publication = json.loads(actual_root)
    routes = [publication['current']] + publication['frozen']
    checked = []
    for item in routes:
        route = item['route']
        raw = fetch(base, route + 'publication-manifest.json')
        if hashlib.sha256(raw).hexdigest() != item['manifest_sha256']:
            raise ValueError(f'Public route manifest mismatch: {route}')
        manifest = json.loads(raw)
        if manifest['source_commit'] != item['source_commit']:
            raise ValueError('Source identity mismatch')
        # Check every rendered reader page and all search/style/script assets,
        # including every concept, domain, source and guide page. Large frozen
        # diagram bytes are bound by the route manifest; sample the actual SVG too.
        paths = [p for p in manifest['output_sha256']
                 if p.endswith(('.html', '.css', '.js')) or p in
                 {'concept-index.json', 'wiki-title-map.json', 'source/model/diagrams/generated/full.svg'}]
        def verify(path):
            actual = hashlib.sha256(fetch(base, route + path)).hexdigest()
            if actual != manifest['output_sha256'][path]:
                raise ValueError(f'Public byte mismatch: {route}{path}')
        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(verify, paths))
        checked.append({'route': route, 'source_commit': item['source_commit'],
                        'documentation_version': item['version'],
                        'checked_output_files': len(paths),
                        'manifest_sha256': item['manifest_sha256'],
                        'concepts': manifest['concepts'],
                        'domains': manifest['domains'],
                        'principal_cqs': manifest['principal_cqs'],
                        'local_link_audit': manifest['audit']})
    return {'status': 'PASS', 'public_url': base, 'routes': checked,
            'scope': 'Actual HTTP bytes for both route manifests, all HTML/CSS/JS, search index and complete SVG; local link/anchor audit is build evidence. Not semantic or human acceptance.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--url', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = readback(args.build, args.url)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
