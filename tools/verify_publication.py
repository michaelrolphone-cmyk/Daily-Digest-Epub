#!/usr/bin/env python3
"""Read public X4 endpoints and verify the published files, without credentials."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from urllib.request import Request, urlopen

from publish import RAW, validate_epub

MAX_BYTES = 64 * 1024 * 1024

def download(url: str) -> tuple[bytes, int]:
    request = Request(url, headers={'User-Agent': 'Daily-Digest-publication-check/1',
                                    'Cache-Control': 'no-cache'})
    with urlopen(request, timeout=30) as response:
        status = response.status
        if status != 200:
            raise ValueError(f'Unexpected HTTP status {status}: {url}')
        data = response.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise ValueError(f'Public response exceeds size limit: {url}')
        return data, status


def verify(root: Path) -> dict:
    expected = json.loads((root / 'latest.json').read_text())
    # Reject an unexpected repository/path before making the public request.
    date = expected['date']
    path = f'editions/{date.replace("-", "/")}/daily-digest-{date}.epub'
    if expected['path'] != path or expected['download_url'] != RAW + path:
        raise ValueError('The published metadata changed the X4 download contract')
    local = (root / path).read_bytes()
    last_error = None
    for attempt in range(6):
        try:
            remote, status = download(expected['download_url'])
            if remote != local:
                raise ValueError('Dated public EPUB differs from validated build')
            validate_epub(remote)
            metadata_bytes, metadata_status = download(RAW + 'latest.json')
            metadata = json.loads(metadata_bytes)
            if metadata != expected:
                raise ValueError('Public latest.json differs from validated metadata')
            newest, newest_status = download(RAW + 'latest.epub')
            if newest != remote:
                raise ValueError('Public latest.epub differs from dated issue')
            return {'verified_at': datetime.now(timezone.utc).isoformat(),
                    'date': date, 'download_url': expected['download_url'],
                    'epub_http_status': status, 'latest_metadata_http_status': metadata_status,
                    'latest_epub_http_status': newest_status, 'size_bytes': len(remote),
                    'sha256': hashlib.sha256(remote).hexdigest(),
                    'matches_validated_build': True, 'attempts': attempt + 1}
        except (OSError, ValueError, KeyError) as error:
            last_error = error
            if attempt < 5:
                time.sleep(5)
    raise RuntimeError(f'Public download verification failed: {last_error}')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    record = verify(args.root)
    target = args.root / 'validation/public-download.json'
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record, indent=2))

if __name__ == '__main__':
    main()
