import io
from pathlib import Path
import unittest
import zipfile
from test_publish import p, example

class EditionLabelTests(unittest.TestCase):
    def test_omitted_label_preserves_evening_bytes(self):
        old = example()
        explicit = example()
        explicit['edition_label'] = 'EVENING EDITION'
        self.assertEqual(p.build_epub(old), p.build_epub(explicit))

    def test_morning_label_is_escaped_and_valid(self):
        edition = example()
        edition['edition_label'] = 'MORNING & <SPECIAL>'
        p.validate_edition(edition, Path('editions/2026/10/10/edition.json'))
        data, _, _ = p.build_epub(edition)
        with zipfile.ZipFile(io.BytesIO(data)) as book:
            cover = book.read('OEBPS/cover.xhtml')
        self.assertIn(b'MORNING &amp; &lt;SPECIAL&gt;', cover)
        self.assertNotIn(b'EVENING EDITION', cover)
        p.validate_epub(data)

    def test_invalid_labels(self):
        for label in ('', '   ', 'x' * 81, None, 42):
            with self.subTest(label=label):
                edition = example()
                edition['edition_label'] = label
                with self.assertRaises(ValueError):
                    p.validate_edition(edition, Path('editions/2026/10/10/edition.json'))
