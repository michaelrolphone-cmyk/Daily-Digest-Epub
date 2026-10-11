import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

SPEC = importlib.util.spec_from_file_location('publish', Path(__file__).resolve().parents[1] / 'tools' / 'publish.py')
p = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(p)


def example(d='2026-10-10'):
    return {'schema_version': 1, 'date': d, 'title': 'Test & Digest', 'subtitle': 'A < B', 'language': 'en', 'timezone': 'America/Boise', 'published_at': d + 'T21:30:00-06:00', 'reporting_cutoff': d + 'T21:00:00-06:00', 'editor_note': 'Test edition.', 'front_page': ['test'], 'articles': [{'id': 'test', 'section': 'News', 'title': 'A & B', 'dek': 'A careful account.', 'timing': 'Test', 'paragraphs': [{'text': 'Testing XML: <script> & punctuation.', 'refs': [1]}], 'sources': [{'title': 'Source', 'publisher': 'Example', 'url': 'https://example.org/?a=1&b=2', 'published': d}]}]}


class PublisherTests(unittest.TestCase):
    def test_valid_edition(self):
        p.validate_edition(example(), Path('editions/2026/10/10/edition.json'))

    def test_invalid_reference(self):
        e = example(); e['articles'][0]['paragraphs'][0]['refs'] = [2]
        with self.assertRaises(ValueError): p.validate_edition(e, Path('editions/2026/10/10/edition.json'))

    def test_invalid_source(self):
        e = example(); e['articles'][0]['sources'][0]['url'] = 'javascript:alert(1)'
        with self.assertRaises(ValueError): p.validate_edition(e, Path('editions/2026/10/10/edition.json'))

    def test_date_path(self):
        with self.assertRaises(ValueError): p.validate_edition(example(), Path('editions/2026/10/09/edition.json'))

    def test_future_source(self):
        e = example(); e['articles'][0]['sources'][0]['published'] = '2026-10-11'
        with self.assertRaises(ValueError): p.validate_edition(e, Path('editions/2026/10/10/edition.json'))

    def test_cutoff(self):
        e = example(); e['reporting_cutoff'] = '2026-10-10T23:00:00-06:00'
        with self.assertRaises(ValueError): p.validate_edition(e, Path('editions/2026/10/10/edition.json'))

    def test_empty(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError): p.generate(Path(temp))

    def test_reproducible_and_escaped(self):
        a, _, _ = p.build_epub(example()); b, _, _ = p.build_epub(example())
        self.assertEqual(a, b)
        with zipfile.ZipFile(io.BytesIO(a)) as z:
            self.assertIn(b'&lt;script&gt;', z.read('OEBPS/test.xhtml'))
            self.assertEqual(z.infolist()[0].compress_type, zipfile.ZIP_STORED)
            self.assertIn('OEBPS/toc.ncx', z.namelist())
            self.assertIn('OEBPS/nav.xhtml', z.namelist())
        self.assertEqual(p.validate_epub(a)['title'], 'Test & Digest')

    def test_catalog_order_and_checksum(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for d in ('2026-10-09', '2026-10-10'):
                target = root / 'editions' / d.replace('-', '/') / 'edition.json'
                target.parent.mkdir(parents=True); target.write_text(json.dumps(example(d)))
            out = p.generate(root)
            latest = json.loads(out['latest.json'])
            self.assertEqual(latest['date'], '2026-10-10')
            self.assertEqual(out['latest.epub'], out[latest['path']])
            self.assertEqual(latest['sha256'], p.hashlib.sha256(out['latest.epub']).hexdigest())
            self.assertEqual(latest['size_bytes'], len(out['latest.epub']))
            self.assertEqual(len(json.loads(out['catalog.json'])['editions']), 2)
            ET.fromstring(out['catalog.opds'])

    def test_correction_changes_hash(self):
        a = example(); b = copy.deepcopy(a)
        b['articles'][0]['paragraphs'][0]['text'] += ' Correction.'
        self.assertNotEqual(p.build_epub(a)[0], p.build_epub(b)[0])

    def test_import_existing_epub(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); directory = root / 'editions/2026/10/10'
            directory.mkdir(parents=True)
            data, _, _ = p.build_epub(example())
            (directory / 'daily-digest-2026-10-10.epub').write_bytes(data)
            out = p.generate(root)
            self.assertEqual(out['latest.epub'], data)
            self.assertTrue(json.loads(out['latest.json'])['imported'])

    def test_broken_link_rejected(self):
        data, _, _ = p.build_epub(example())
        output = io.BytesIO()
        with zipfile.ZipFile(io.BytesIO(data)) as source, zipfile.ZipFile(output, 'w') as target:
            for entry in source.infolist():
                content = source.read(entry.filename)
                if entry.filename == 'OEBPS/test.xhtml': content = content.replace(b'href="nav.xhtml"', b'href="missing.xhtml"')
                target.writestr(entry, content)
        with self.assertRaises(ValueError): p.validate_epub(output.getvalue())


if __name__ == '__main__': unittest.main()
