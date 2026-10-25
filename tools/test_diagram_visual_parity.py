"""Meaningful negative cases: valid hashes alone must not hide displaced content."""
from pathlib import Path
import hashlib
import json
import shutil
import tempfile
import unittest
import fitz
import check_diagram_visual_parity as audit

class VisualParityBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        self.original=audit.ROOT
        for name in ('model','tools','evaluation/diagrams'):
            shutil.copytree(self.original/name,self.root/name,dirs_exist_ok=True)
        audit.ROOT=self.root

    def tearDown(self):
        audit.ROOT=self.original
        self.temp.cleanup()

    def test_stale_pdf_bytes_rejected(self):
        p=self.root/'model/diagrams/generated/atlas.pdf'
        p.write_bytes(p.read_bytes()+b'\n% changed bytes\n')
        with self.assertRaisesRegex(ValueError,'differs from build receipt'):
            audit.run()

    def test_displacement_rejected_even_with_matching_new_hash(self):
        p=self.root/'model/diagrams/generated/full.pdf'
        original=fitz.open(p)
        moved=fitz.open();page=moved.new_page(width=original[0].rect.width,height=original[0].rect.height)
        rect=original[0].rect+(2,0,2,0)
        page.show_pdf_page(rect,original,0)
        moved.save(p.with_name('shifted.pdf'))
        original.close();moved.close()
        p.write_bytes(p.with_name('shifted.pdf').read_bytes())
        receipt=self.root/'evaluation/diagrams/pdf-atlas-build.json'
        record=json.loads(receipt.read_text())
        record['outputs']['full.pdf']['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
        receipt.write_text(json.dumps(record))
        result=audit.run()
        self.assertEqual(result['status'],'FAIL')
        self.assertTrue(any(r['check']=='pdf_complete_curve_controls' for r in result['failures']))
        self.assertTrue(any(r['check']=='pdf_text_position' for r in result['failures']))

if __name__=='__main__':
    unittest.main()
