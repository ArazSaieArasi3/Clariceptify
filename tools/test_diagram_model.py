"""Negative regression checks for the current diagram audit, not semantic review."""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from lxml import etree as ET
from check_diagram_model import audit, NS
ROOT=Path(__file__).resolve().parents[1]
SVG=ROOT/'model/diagrams/generated/full.svg'
class DiagramAuditTests(unittest.TestCase):
    def altered(self, mutate):
        root=ET.parse(str(SVG));mutate(root)
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'full.svg';root.write(str(p))
            self.assertEqual(audit(ROOT,p.parent,p)['status'],'FAIL')
    def test_baseline(self):self.assertEqual(audit(ROOT,SVG.parent,SVG)['status'],'PASS')
    def test_id(self):self.altered(lambda r:r.xpath('//s:g[@class="node"]',namespaces=NS)[0].set('data-registry-id','WRONG'))
    def test_stereotype(self):self.altered(lambda r:r.xpath('//s:g[@class="node"]',namespaces=NS)[0].set('data-stereotype','wrong'))
    def test_direction(self):self.altered(lambda r:r.xpath('//s:g[@class="edge"]',namespaces=NS)[0].set('data-target','wrong'))
    def test_multiplicity(self):
        def edit(r):r.xpath('//s:g[@class="edge" or @class="edge-labels"]//s:text[@text-anchor="middle"]',namespaces=NS)[0].text='999'
        self.altered(edit)
    def test_missing_node(self):
        def edit(r):
            n=r.xpath('//s:g[@class="node"]',namespaces=NS)[0];n.getparent().remove(n)
        self.altered(edit)
    def test_geometry(self):self.altered(lambda r:r.xpath('//s:g[@class="edge"]//s:path',namespaces=NS)[0].set('d','M0,0 C1,1 2,2 3,3'))
    def test_domain_color(self):self.altered(lambda r:r.xpath('//s:g[@class="node"]//s:polygon',namespaces=NS)[0].set('fill','#010203'))
    def test_label_layer_order(self):
        def edit(r):
            layer=r.xpath('//s:g[@id="edge-label-layer"]',namespaces=NS)[0]
            parent=layer.getparent();parent.remove(layer);parent.insert(0,layer)
        self.altered(edit)
    def test_label_ownership(self):
        self.altered(lambda r:r.xpath('//s:g[@class="edge-labels"]',namespaces=NS)[0].set('data-edge-ref','missing'))
if __name__=='__main__':unittest.main()
