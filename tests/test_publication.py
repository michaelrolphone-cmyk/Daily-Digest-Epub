import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from test_publish import p, example

sys.modules.setdefault('publish', p)
spec = importlib.util.spec_from_file_location('verify_publication', Path(__file__).resolve().parents[1] / 'tools/verify_publication.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

class PublicDownloadTests(unittest.TestCase):
    def fixture(self, root):
        path = root / 'editions/2026/10/10/edition.json'
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(example()))
        for relative, data in p.generate(root).items():
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        return (root / 'latest.epub').read_bytes(), (root / 'latest.json').read_bytes()

    def test_public_endpoints_match(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            epub, metadata = self.fixture(root)
            with patch.object(v, 'download', side_effect=[(epub, 200), (metadata, 200), (epub, 200)]) as fetch:
                result = v.verify(root)
            self.assertEqual(fetch.call_count, 3)
            self.assertTrue(result['matches_validated_build'])
            self.assertEqual(result['size_bytes'], len(epub))

    def test_cached_mismatch_retries(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            epub, metadata = self.fixture(root)
            with patch.object(v, 'download', side_effect=[(b'old', 200), (epub, 200), (metadata, 200), (epub, 200)]), patch.object(v.time, 'sleep'):
                self.assertEqual(v.verify(root)['attempts'], 2)

    def test_persistent_failure_not_reported_as_success(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            with patch.object(v, 'download', return_value=(b'wrong', 200)), patch.object(v.time, 'sleep'):
                with self.assertRaises(RuntimeError):
                    v.verify(root)

    def test_changed_contract_rejected_before_network(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            _, metadata = self.fixture(root)
            data = json.loads(metadata)
            data['download_url'] = 'https://example.org/unexpected.epub'
            (root / 'latest.json').write_text(json.dumps(data))
            with patch.object(v, 'download') as fetch:
                with self.assertRaises(ValueError):
                    v.verify(root)
                fetch.assert_not_called()
