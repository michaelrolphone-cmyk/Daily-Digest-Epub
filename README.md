# Daily Digest

A dated archive of original, source-linked daily newspapers in EPUB format, designed for offline e-ink reading.

## Download endpoints

- Latest newspaper: [`latest.epub`](https://raw.githubusercontent.com/michaelrolphone-cmyk/Daily-Digest-Epub/main/latest.epub)
- Latest edition metadata: [`latest.json`](https://raw.githubusercontent.com/michaelrolphone-cmyk/Daily-Digest-Epub/main/latest.json)
- All editions, newest first: [`catalog.json`](https://raw.githubusercontent.com/michaelrolphone-cmyk/Daily-Digest-Epub/main/catalog.json)
- OPDS acquisition feed: [`catalog.opds`](https://raw.githubusercontent.com/michaelrolphone-cmyk/Daily-Digest-Epub/main/catalog.opds)
- Human-readable archive: [ARCHIVE.md](ARCHIVE.md)

The repository is public. These raw download URLs require no GitHub sign-in. They are distribution endpoints, not a claim that any particular X4 firmware already implements automatic catalog downloads.

## Organization

```text
editions/YYYY/MM/DD/
  edition.json                       # editable article text, source URLs, dates
  daily-digest-YYYY-MM-DD.epub         # generated, archived issue
  paper.md                           # generated readable article text
  metadata.json                      # generated download record + SHA-256
latest.epub                          # byte-identical copy of newest archived issue
latest.json                          # small newest-edition download record
catalog.json                         # complete newest-first catalog
catalog.opds                         # OPDS 1.2 acquisition feed
ARCHIVE.md                           # browse by year and month
index.html                           # simple static archive page
schema/edition.schema.json           # authoring format
schema/catalog.schema.json           # download catalog format
tools/publish.py                      # dependency-free builder and catalog updater
.github/workflows/publish.yml         # builds on source changes; no scheduled news generation
```

## Add a daily paper

Copy an existing `edition.json` into the next `editions/YYYY/MM/DD/` directory, update its date, publication time, article text, and sources, then run:

```sh
python3 tools/publish.py
python3 tools/publish.py --check
git add editions latest.epub latest.json catalog.json catalog.opds ARCHIVE.md index.html
git commit -m "Publish daily digest YYYY-MM-DD"
git push
```

Alternatively, commit the new `edition.json` alone. The publishing workflow builds and commits the EPUB, checksums, and indexes on `main`. It does not research or invent tomorrow's news; each day's editorial input must be supplied.

An externally produced EPUB can also be placed at `editions/YYYY/MM/DD/daily-digest-YYYY-MM-DD.epub` without an `edition.json`. The catalog builder will inspect its package metadata and include it. A date has exactly one archived issue. Revise that date in place for corrections; Git history preserves earlier revisions, and checksum changes allow clients to detect corrections.

## X4 download contract

Fetch `latest.json`, compare the `(date, sha256)` pair with the locally stored issue, and download its `download_url` only when different. Download into a temporary file, verify `size_bytes` and `sha256`, then atomically rename it into the local newspaper library. Preserve the previous good file on interruption or failed validation. The archive URL is preferred over `latest.epub` during a download because it remains date-specific. SHA-256 detects corruption; it is not a digital signature.

A client can browse historical issues through `catalog.json` or a compatible OPDS client through `catalog.opds`. Use HTTPS with certificate verification. Cached GitHub raw responses can briefly lag a publication; on a mismatch, keep the last valid issue and retry later. No firmware or installed application is modified by this repository.

## Editorial and reading format

Each issue identifies its edition date and reporting cutoff. Daily reporting, earlier developments, and analysis are labeled separately. Articles are original summaries and analysis, not copied publisher articles. Sources and publication dates are retained beside each article, and outbound links are optional for reading: all article text is included offline.

The EPUB is reflowable, uses conservative XHTML and monochrome styling, includes both EPUB navigation and an NCX table of contents, and does not embed fonts, scripts, remote images, or DRM. Structural validation is automated; hardware-specific rendering still requires testing on the reader.
