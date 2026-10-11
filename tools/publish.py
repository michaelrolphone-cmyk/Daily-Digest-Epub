#!/usr/bin/env python3
"""Build deterministic, offline EPUB newspapers and static download catalogs.

Python 3.10+, standard library only. No network requests or news generation.
"""
from __future__ import annotations
import argparse
from collections import OrderedDict
from datetime import date, datetime, timezone
from html import escape
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit
import uuid
import xml.etree.ElementTree as ET
import zipfile
from zoneinfo import ZoneInfo

REPOSITORY = 'michaelrolphone-cmyk/Daily-Digest-Epub'
RAW = f'https://raw.githubusercontent.com/{REPOSITORY}/main/'
OPF = 'http://www.idpf.org/2007/opf'
DC = 'http://purl.org/dc/elements/1.1/'
XHTML = 'http://www.w3.org/1999/xhtml'
CSS = '''body { margin: 5%; line-height: 1.4; text-align: left; }
h1 { font-size: 1.65em; line-height: 1.12; margin: .7em 0; }
h2 { font-size: 1.2em; line-height: 1.2; margin: 1.2em 0 .5em; }
p { margin: 0 0 .8em; orphans: 2; widows: 2; }
a { color: inherit; text-decoration: underline; }
.kicker { font-size: .85em; font-weight: bold; letter-spacing: .06em; }
.dek { font-size: 1.08em; }
.meta, .sources { font-size: .85em; }
.masthead { border-top: .18em solid; border-bottom: .08em solid; padding: .7em 0; }
.rule { border-top: .08em solid; padding-top: .8em; margin-top: 1em; }
ol { padding-left: 1.5em; }
li { margin-bottom: .55em; }
.sup { font-size: .75em; vertical-align: super; }
'''


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def iso_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    require(parsed.tzinfo is not None, 'Timestamp must include a timezone')
    return parsed


def utc(value: str) -> str:
    return iso_time(value).astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def xhtml(title: str, body: str, language: str = 'en') -> bytes:
    return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
            f'<html xmlns="{XHTML}" xmlns:epub="http://www.idpf.org/2007/ops" '
            f'xml:lang="{escape(language)}" lang="{escape(language)}">'
            f'<head><title>{escape(title)}</title><link rel="stylesheet" '
            'type="text/css" href="style.css"/></head>'
            f'<body>{body}</body></html>').encode('utf-8')


def validate_edition(edition: dict, path: Path) -> None:
    require(edition.get('schema_version') == 1, 'Unsupported edition schema')
    d = edition['date']
    require(re.fullmatch(r'\d{4}-\d{2}-\d{2}', d) is not None, 'Invalid date format')
    date.fromisoformat(d)
    require(tuple(path.parent.parts[-3:]) == tuple(d.split('-')), 'Directory/date mismatch')
    published = iso_time(edition['published_at'])
    cutoff = iso_time(edition['reporting_cutoff'])
    tz = ZoneInfo(edition.get('timezone', 'America/Boise'))
    require(cutoff <= published, 'Reporting cutoff is after publication')
    require(cutoff.astimezone(tz).date().isoformat() == d, 'Cutoff/date mismatch')
    for key in ('title', 'subtitle', 'language', 'editor_note'):
        require(isinstance(edition.get(key), str) and bool(edition[key].strip()), f'Missing {key}')
    articles = edition['articles']
    require(isinstance(articles, list) and len(articles) > 0, 'No articles')
    ids = set()
    for article in articles:
        ident = article['id']
        require(re.fullmatch('[a-z][a-z0-9-]*', ident) is not None, 'Invalid article ID')
        require(ident not in ids, 'Duplicate article ID')
        ids.add(ident)
        for key in ('section', 'title', 'dek', 'timing'):
            require(bool(article.get(key)), f'Missing article {key}')
        sources = article['sources']
        require(len(sources) > 0, 'Article requires sources')
        for source in sources:
            require(bool(source.get('title')) and bool(source.get('publisher')), 'Source needs attribution')
            require(urlsplit(source['url']).scheme == 'https', 'Source URL must use HTTPS')
            require(bool(urlsplit(source['url']).netloc), 'Invalid source URL')
            if source.get('published'):
                require(date.fromisoformat(source['published']) <= cutoff.astimezone(tz).date(), 'Future source')
        require(len(article['paragraphs']) > 0, 'Empty article')
        used = set()
        for p in article['paragraphs']:
            require(isinstance(p.get('text'), str) and p['text'].strip(), 'Empty paragraph')
            require(p.get('kind', 'reporting') in ('reporting', 'analysis', 'context'), 'Invalid paragraph kind')
            references = p.get('refs', [])
            require(p.get('kind', 'reporting') == 'analysis' or bool(references), 'Reporting/context needs sources')
            for ref in references:
                require(type(ref) is int and 1 <= ref <= len(sources), 'Invalid source reference')
                used.add(ref)
        require(used == set(range(1, len(sources) + 1)), 'Unused source')
    for ident in edition.get('front_page', []):
        require(ident in ids, 'Unknown front-page article')


def validate_epub(data: bytes) -> dict:
    """Offline structural checks; CI additionally runs the official EPUBCheck."""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        entries = z.infolist()
        require(bool(entries) and entries[0].filename == 'mimetype', 'mimetype must be first')
        require(entries[0].compress_type == zipfile.ZIP_STORED, 'mimetype must be uncompressed')
        require(z.read('mimetype') == b'application/epub+zip', 'Invalid mimetype')
        names = z.namelist()
        require(len(names) == len(set(names)), 'Duplicate ZIP entries')
        require(sum(e.file_size for e in entries) < 64 * 1024 * 1024, 'EPUB exceeds validation size limit')
        for name in names:
            require(not name.startswith('/') and '..' not in PurePosixPath(name).parts, 'Unsafe ZIP path')
        require(z.testzip() is None, 'ZIP CRC failure')
        container = ET.fromstring(z.read('META-INF/container.xml'))
        rootfile = container.find('.//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile')
        require(rootfile is not None, 'Missing package rootfile')
        package_path = rootfile.attrib['full-path']
        package = ET.fromstring(z.read(package_path))
        folder = posixpath.dirname(package_path)
        manifest = package.find(f'{{{OPF}}}manifest')
        require(manifest is not None, 'Missing manifest')
        items = {item.attrib['id']: item for item in manifest}
        require(len(items) == len(list(manifest)), 'Duplicate manifest IDs')
        for item in items.values():
            href = item.attrib['href']
            require(not urlsplit(href).scheme, 'Remote manifest resource')
            require(posixpath.normpath(posixpath.join(folder, unquote(href))) in names, 'Missing manifest resource')
        spine = package.find(f'{{{OPF}}}spine')
        require(spine is not None and len(spine) > 0, 'Empty spine')
        for item in spine:
            require(item.attrib['idref'] in items, 'Invalid spine reference')
        docs = {}
        for name in names:
            if name.endswith(('.xhtml', '.html', '.ncx', '.opf', '.xml')):
                root = ET.fromstring(z.read(name))
                docs[name] = root
                id_list = [e.attrib['id'] for e in root.iter() if 'id' in e.attrib]
                require(len(id_list) == len(set(id_list)), 'Duplicate XML IDs')
        for name, root in docs.items():
            if not name.endswith(('.xhtml', '.html', '.ncx')):
                continue
            for node in root.iter():
                local = node.tag.rsplit('}', 1)[-1]
                require(local not in ('script', 'iframe'), 'Active content is not allowed')
                for attribute in ('href', 'src'):
                    if attribute not in node.attrib:
                        continue
                    target = urlsplit(node.attrib[attribute])
                    if target.scheme or target.netloc:
                        require(local == 'a' and attribute == 'href' and target.scheme == 'https', 'Remote or unsafe resource')
                        continue
                    dest = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(target.path))) if target.path else name
                    require(dest in names, f'Broken link: {name} -> {dest}')
                    if target.fragment:
                        require(dest in docs and any(e.attrib.get('id') == unquote(target.fragment) for e in docs[dest].iter()), 'Broken fragment')
        title = package.findtext(f'.//{{{DC}}}title')
        language = package.findtext(f'.//{{{DC}}}language') or 'en'
        modified = next((e.text for e in package.findall(f'.//{{{OPF}}}meta') if e.attrib.get('property') == 'dcterms:modified'), None)
        require(bool(title), 'Missing EPUB title')
        return {'title': title, 'language': language, 'modified': modified}


def build_epub(edition: dict) -> tuple[bytes, str, int]:
    language = edition['language']
    d = edition['date']
    human_date = date.fromisoformat(d).strftime('%A, %B %d, %Y').replace(' 0', ' ')
    articles = edition['articles']
    book_id = 'urn:uuid:' + str(uuid.uuid5(uuid.NAMESPACE_URL, f'https://github.com/{REPOSITORY}/editions/{d}'))
    source_count = len({s['url'] for a in articles for s in a['sources']})
    words = len(re.findall(r'\b[\w’\'-]+\b', ' '.join(p['text'] for a in articles for p in a['paragraphs'])))
    minutes = max(1, round(words / 200))
    cover = (f'<p class="kicker">EVENING EDITION · {escape(d)}</p>'
             '<h1 class="masthead">DAILY<br/>DIGEST</h1>'
             f'<p class="dek">{escape(edition["subtitle"])}</p>'
             f'<p>{escape(human_date)}</p>'
             f'<p class="meta">{len(articles)} articles · {source_count} sources · about {minutes} minutes</p>'
             '<p class="rule">World · Technology · Science · The West</p>'
             '<p><a href="front.xhtml">Start with the front page</a></p>'
             '<p><a href="nav.xhtml">Browse this edition</a></p>')
    chapters = [('cover', 'cover.xhtml', 'Daily Digest', xhtml('Daily Digest', cover, language))]
    front = '<h1>The Front Page</h1><p>' + escape(edition['editor_note']) + '</p>'
    lookup = {a['id']: a for a in articles}
    for ident in edition.get('front_page', []):
        a = lookup[ident]
        front += f'<h2><a href="{ident}.xhtml">{escape(a["title"])}</a></h2><p>{escape(a["dek"])}</p>'
    front += '<p class="rule meta">Headlines link to complete articles and their sources. Earlier developments are explicitly dated; this is not a claim that every story broke today.</p>'
    chapters.append(('front', 'front.xhtml', 'The Front Page', xhtml('The Front Page', front, language)))
    md = [f'# {edition["title"]}', edition['subtitle'], f'Reporting cutoff: {edition["reporting_cutoff"]} ({edition["timezone"]})', edition['editor_note']]
    for a in articles:
        content = f'<p class="kicker">{escape(a["section"])}</p><h1>{escape(a["title"])}</h1><p class="dek">{escape(a["dek"])}</p><p class="meta">{escape(a["timing"])}</p>'
        md.extend([f'## {a["section"]} — {a["title"]}', a['dek'], a['timing']])
        for p in a['paragraphs']:
            if p.get('heading'):
                content += '<h2>' + escape(p['heading']) + '</h2>'
                md.append('### ' + p['heading'])
            prefix = '<strong>Analysis. </strong>' if p.get('kind') == 'analysis' else ''
            refs = ''.join(f' <a class="sup" href="#source-{r}">[{r}]</a>' for r in p.get('refs', []))
            content += '<p>' + prefix + escape(p['text']) + refs + '</p>'
            md.append(('**Analysis.** ' if p.get('kind') == 'analysis' else '') + p['text'] + ''.join(f' [{r}]' for r in p.get('refs', [])))
        content += '<h2 class="rule">Sources</h2><ol class="sources">'
        md.append('### Sources')
        for i, s in enumerate(a['sources'], 1):
            when = s.get('published') or 'Undated reference; checked 2026-10-10' if d == '2026-10-10' else s.get('published') or f'Undated reference; checked {d}'
            label = f'{s["publisher"]} — {s["title"]}'
            content += f'<li id="source-{i}"><a href="{escape(s["url"], quote=True)}">{escape(label)}</a>. {escape(when)}.</li>'
            md.append(f'{i}. [{label}]({s["url"]}) — {when}.')
        content += '</ol><p class="meta"><a href="nav.xhtml">Contents</a></p>'
        chapters.append((a['id'], a['id'] + '.xhtml', a['title'], xhtml(a['title'], content, language)))
    colophon = ('<h1>About This Edition</h1>'
                f'<p>Edition date: {escape(d)}. Reporting cutoff: {escape(edition["reporting_cutoff"])} ({escape(edition["timezone"])}).</p>'
                '<p>Original AI-assisted summaries and analysis, compiled from the attributed sources. Claims by companies, governments, and parties to conflicts are identified as claims, not independent verification. Sources were checked for this edition; later revisions may differ.</p>'
                '<p>Analysis paragraphs are editorial reasoning. This paper is a selection, not an exhaustive record. Its source notes are links, not reproduced publisher articles. All reading text is included offline.</p>'
                '<p>Corrections should update this date’s source edition and publication timestamp. The catalog checksum identifies the corrected file; repository history preserves prior versions.</p>'
                '<p>Reflowable text, no embedded fonts, no scripts, no remote images, and no DRM. Display font and size remain reader-controlled. The newspaper does not modify reader firmware or enable unattended downloads.</p>'
                '<p><a href="nav.xhtml">Return to contents</a></p>')
    chapters.append(('about', 'about.xhtml', 'About This Edition', xhtml('About This Edition', colophon, language)))
    nav_body = '<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>'
    nav_body += ''.join(f'<li><a href="{href}">{escape(title)}</a></li>' for _, href, title, _ in chapters)
    nav_body += '</ol></nav><nav epub:type="landmarks"><h2>Start Reading</h2><ol><li><a epub:type="bodymatter" href="front.xhtml">Front page</a></li></ol></nav>'
    nav = ('nav', 'nav.xhtml', 'Contents', xhtml('Contents', nav_body, language))
    chapters.insert(2, nav)
    manifest = ''.join(f'<item id="{ident}" href="{href}" media-type="application/xhtml+xml"' + (' properties="nav"' if ident == 'nav' else '') + '/>' for ident, href, _, _ in chapters)
    spine = ''.join(f'<itemref idref="{ident}"/>' for ident, _, _, _ in chapters)
    package = (f'<?xml version="1.0" encoding="utf-8"?><package xmlns="{OPF}" version="3.0" unique-identifier="book-id" xml:lang="{escape(language)}">'
               f'<metadata xmlns:dc="{DC}"><dc:identifier id="book-id">{book_id}</dc:identifier>'
               f'<dc:title>{escape(edition["title"])}</dc:title><dc:creator>Daily Digest</dc:creator><dc:publisher>Daily Digest</dc:publisher>'
               f'<dc:language>{escape(language)}</dc:language><dc:date>{d}</dc:date><dc:description>{escape(edition["subtitle"])}</dc:description>'
               f'<meta property="dcterms:modified">{utc(edition["published_at"])}</meta></metadata>'
               f'<manifest>{manifest}<item id="css" href="style.css" media-type="text/css"/><item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/></manifest>'
               f'<spine toc="ncx">{spine}</spine></package>')
    navpoints = ''.join(f'<navPoint id="n{i}" playOrder="{i}"><navLabel><text>{escape(title)}</text></navLabel><content src="{href}"/></navPoint>' for i, (_, href, title, _) in enumerate(chapters, 1))
    ncx = (f'<?xml version="1.0" encoding="utf-8"?><ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="{escape(language)}">'
           f'<head><meta name="dtb:uid" content="{book_id}"/><meta name="dtb:depth" content="1"/><meta name="dtb:totalPageCount" content="0"/><meta name="dtb:maxPageNumber" content="0"/></head>'
           f'<docTitle><text>{escape(edition["title"])}</text></docTitle><navMap>{navpoints}</navMap></ncx>')
    members = {'META-INF/container.xml': b'<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>',
               'OEBPS/content.opf': package.encode(), 'OEBPS/toc.ncx': ncx.encode(), 'OEBPS/style.css': CSS.encode()}
    members.update({'OEBPS/' + href: data for _, href, _, data in chapters})
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w') as z:
        for name, data in [('mimetype', b'application/epub+zip')] + sorted(members.items()):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED if name == 'mimetype' else zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data, compresslevel=9)
    data = output.getvalue()
    validate_epub(data)
    return data, '\n\n'.join(md) + '\n', words


def generate(root: Path) -> dict[str, bytes]:
    output = {}
    records = []
    directories = sorted(p for p in (root / 'editions').glob('*/*/*') if p.is_dir())
    for folder in directories:
        d = '-'.join(folder.parts[-3:])
        date.fromisoformat(d)
        require(re.fullmatch(r'\d{4}-\d{2}-\d{2}', d) is not None, 'Invalid archive path')
        relative = folder.relative_to(root).as_posix()
        name = f'daily-digest-{d}.epub'
        source = folder / 'edition.json'
        if source.exists():
            edition = json.loads(source.read_text(encoding='utf-8'))
            validate_edition(edition, source)
            data, markdown, words = build_epub(edition)
            published = utc(edition['published_at'])
            title, language = edition['title'], edition['language']
            summary = edition['subtitle']
            output[f'{relative}/paper.md'] = markdown.encode()
            extra = {'reporting_cutoff': edition['reporting_cutoff'], 'article_count': len(edition['articles']), 'word_count': words, 'estimated_reading_minutes': max(1, round(words / 200)), 'source_count': len({s['url'] for a in edition['articles'] for s in a['sources']})}
        else:
            existing = folder / name
            if not existing.exists():
                continue
            data = existing.read_bytes()
            info = validate_epub(data)
            title, language = info['title'], info['language']
            published = utc(info['modified']) if info['modified'] else d + 'T12:00:00Z'
            summary = 'Imported daily newspaper'
            extra = {'imported': True}
        relative_epub = f'{relative}/{name}'
        output[relative_epub] = data
        record = {'schema_version': 1, 'id': 'urn:daily-digest:' + d, 'date': d, 'title': title, 'summary': summary, 'language': language, 'published_at': published, 'filename': name, 'path': relative_epub, 'download_url': RAW + relative_epub, 'media_type': 'application/epub+zip', 'size_bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), **extra}
        output[f'{relative}/metadata.json'] = json_bytes(record)
        records.append(record)
    require(bool(records), 'No dated editions found')
    records.sort(key=lambda r: r['date'], reverse=True)
    latest = records[0]
    updated = max(r['published_at'] for r in records)
    catalog = {'schema_version': 1, 'title': 'Daily Digest', 'updated_at': updated, 'latest': latest, 'editions': records}
    output['catalog.json'] = json_bytes(catalog)
    output['latest.json'] = json_bytes(latest)
    output['latest.epub'] = output[latest['path']]
    atom = ('<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/terms/">'
            f'<id>https://github.com/{REPOSITORY}</id><title>Daily Digest</title><updated>{updated}</updated>'
            '<author><name>Daily Digest</name></author>'
            f'<link rel="self" href="{RAW}catalog.opds" type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>'
            f'<link rel="start" href="{RAW}catalog.opds" type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>')
    for r in records:
        atom += (f'<entry><id>{r["id"]}</id><title>{escape(r["title"])}</title><updated>{r["published_at"]}</updated><published>{r["published_at"]}</published>'
                 f'<summary>{escape(r["summary"])}</summary><dc:language>{escape(r["language"])}</dc:language><dc:issued>{r["date"]}</dc:issued><dc:publisher>Daily Digest</dc:publisher>'
                 f'<link rel="http://opds-spec.org/acquisition/open-access" href="{escape(r["download_url"])}" type="application/epub+zip" length="{r["size_bytes"]}"/></entry>')
    atom += '</feed>'
    ET.fromstring(atom)
    output['catalog.opds'] = atom.encode()
    archive = ['# Daily Digest archive', f'[Latest EPUB]({RAW}latest.epub) · [JSON catalog]({RAW}catalog.json) · [OPDS feed]({RAW}catalog.opds)']
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Daily Digest archive</title><style>body{max-width:46em;margin:2em auto;padding:0 1em;font-family:serif;line-height:1.5}li{margin-bottom:1em}</style></head><body><h1>Daily Digest</h1><p>Original, source-linked newspapers for offline reading.</p>'
    html += f'<p><a href="{RAW}latest.epub">Download latest EPUB</a> · <a href="{RAW}catalog.json">JSON catalog</a> · <a href="{RAW}catalog.opds">OPDS feed</a></p><ul>'
    month = None
    for r in records:
        if r['date'][:7] != month:
            month = r['date'][:7]
            archive.append('## ' + month)
        archive.append(f'- **{r["date"]}** — [{r["title"]}]({r["download_url"]}) · [Read text]({r["path"].rsplit("/",1)[0]}/paper.md)' if not r.get('imported') else f'- **{r["date"]}** — [{r["title"]}]({r["download_url"]})')
        html += f'<li><a href="{escape(r["download_url"])}">{escape(r["title"])}</a><br/>{escape(r["summary"])}</li>'
    html += '</ul><p>Static archive. No login, tracking scripts, or reader firmware changes.</p></body></html>'
    output['ARCHIVE.md'] = ('\n\n'.join(archive) + '\n').encode()
    output['index.html'] = html.encode()
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true', help='Check without modifying any files')
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        output = generate(root)
        changed = []
        for relative, data in output.items():
            path = root / relative
            if not path.exists() or path.read_bytes() != data:
                changed.append(relative)
                if not args.check:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    temp = path.with_suffix(path.suffix + '.tmp')
                    temp.write_bytes(data)
                    temp.replace(path)
        if args.check and changed:
            print('Out-of-date generated files:\n' + '\n'.join(changed), file=sys.stderr)
            return 1
        print(f'{"Checked" if args.check else "Built"} {len(output)} files; {len(changed)} changed.')
        return 0
    except (ValueError, KeyError, TypeError, OSError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f'Publication failed: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
