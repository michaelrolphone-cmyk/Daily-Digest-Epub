import hashlib
import io
import json
from pathlib import Path
import unittest
import zipfile
from test_publish import p, example

class CoverTopicsTests(unittest.TestCase):
    def test_omission_preserves_original_default(self):
        original = example()
        explicit = example()
        explicit['cover_topics'] = 'World · Technology · Science · The West'
        self.assertEqual(p.build_epub(original), p.build_epub(explicit))

    def test_custom_topics_are_escaped(self):
        edition = example()
        edition['cover_topics'] = 'Physics & <ESP32>'
        p.validate_edition(edition, Path('editions/2026/10/10/edition.json'))
        blob, _, _ = p.build_epub(edition)
        with zipfile.ZipFile(io.BytesIO(blob)) as book:
            cover = book.read('OEBPS/cover.xhtml')
        self.assertIn(b'Physics &amp; &lt;ESP32&gt;', cover)
        self.assertNotIn(b'The West', cover)
        p.validate_epub(blob)

    def test_invalid_topics(self):
        for value in ('', '   ', 'x' * 121, None, 42):
            with self.subTest(value=value):
                edition = example()
                edition['cover_topics'] = value
                with self.assertRaises(ValueError):
                    p.validate_edition(edition, Path('editions/2026/10/10/edition.json'))

    def test_october_10_archive_is_byte_identical(self):
        path = Path(__file__).resolve().parents[1] / 'editions/2026/10/10/edition.json'
        original = json.loads(path.read_text())
        blob, _, _ = p.build_epub(original)
        self.assertEqual(hashlib.sha256(blob).hexdigest(),
            'c1ef28325389fe7b7088ff890ab9a1427eb8cf0ec98ad7ff0fa5087632cdde23')
