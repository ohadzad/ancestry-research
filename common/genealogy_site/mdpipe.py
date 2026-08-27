# -*- coding: utf-8 -*-
"""Markdown -> HTML, plus the document-level transforms every report needs."""
import html as _h
import re

import markdown as _md

from . import bidi

_DIV_LINE = re.compile(r'^\s*</?div[^>]*>\s*$', re.M)
_EMPTY_THEAD = re.compile(r'<thead>\s*<tr>(?:\s*<th[^>]*>\s*</th>)+\s*</tr>\s*</thead>', re.S)


_FENCE = re.compile(r'^:::[ \t]*([\w-]+)[ \t]*\n(.*?)^:::[ \t]*$', re.M | re.S)


def to_html(text, extensions=('tables',)):
    """Markdown to HTML.

    Two conventions beyond plain Markdown:
      * a bare ``<div dir="rtl">`` wrapper line is dropped (it is there for
        editors that preview the raw file);
      * a ``::: name`` … ``:::`` fence becomes ``<div class="name">`` with its
        contents processed as Markdown.
    """
    text = _DIV_LINE.sub('', text)
    blocks = {}

    def _fence(m):
        key = f'GSFENCE{len(blocks)}X'
        blocks[key] = (m.group(1), m.group(2))
        return '\n\n' + key + '\n\n'

    text = _FENCE.sub(_fence, text)
    html = _md.markdown(text, extensions=list(extensions))
    for key, (cls, body) in blocks.items():
        inner = _md.markdown(body, extensions=list(extensions))
        html = html.replace(f'<p>{key}</p>', f'<div class="{cls}">{inner}</div>')
        html = html.replace(key, f'<div class="{cls}">{inner}</div>')
    return _EMPTY_THEAD.sub('', html)


# ---------------------------------------------------------------- headings --
_H = re.compile(r'<h([234])>(.*?)</h\1>', re.S)
_TAGS = re.compile(r'<[^>]+>')


def _slug(text, seen):
    """A stable, readable id. Hebrew survives; collisions get a hash suffix."""
    plain = _TAGS.sub('', text).strip()
    s = re.sub(r"[^\w֐-׿'׳״-]+", '-', plain, flags=re.U).strip('-')
    s = re.sub(r'-{2,}', '-', s)[:60] or 'h'
    if s in seen:
        stem, i = s, 2
        while s in seen:
            s = f'{stem}-{i}'
            i += 1
    seen.add(s)
    return s


def anchor_headings(html, legacy_aliases=None, seen=None):
    """Give every h2/h3/h4 an id. Returns (html, toc) where toc lists the h2s.

    ``legacy_aliases`` maps an old published id to a regex matched against the
    heading text. The alias is emitted as an empty span before that heading, so
    links published against an earlier numbering keep landing on the right
    chapter even after chapters are inserted.
    """
    aliases = dict(legacy_aliases or {})
    seen = set() if seen is None else seen
    toc = []

    def sub(m):
        lvl, inner = m.group(1), m.group(2)
        sid = _slug(inner, seen)
        plain = _TAGS.sub('', inner).strip()
        prefix = ''
        if lvl == '2':
            toc.append((sid, plain))
            for old, pat in list(aliases.items()):
                if re.search(pat, plain):
                    prefix += f'<span id="{old}" class="legacy-anchor"></span>'
                    del aliases[old]
        return f'{prefix}<h{lvl} id="{sid}">{inner}</h{lvl}>'

    out = _H.sub(sub, html)
    # whatever is left in `aliases` matched no heading: a published link that
    # now points nowhere, which the caller reports
    return out, toc, sorted(aliases)


def toc_label(text, limit=26, overrides=None):
    """Shorten a chapter title for the sticky nav without losing its subject.

    ``overrides`` lets a project name a chapter whose full title does not
    shorten well.
    """
    t = _h.unescape(text).strip()
    for pat, label in (overrides or {}).items():
        if re.search(pat, t):
            return label
    m = re.match(r'^פרק\s+(\S+?)\s*[—–-]\s*(.+)$', t)
    if m:
        t = f'{m.group(1)} · {m.group(2)}'
    if len(t) > limit and ':' in t:
        head = t.split(':')[0]
        if len(head) >= 10:
            t = head
    if len(t) <= limit:
        return t
    return t[:limit - 1].rstrip(' ,;:·־-') + '…'


# ------------------------------------------------------------------ chips ---
RANKS = [
    ('מאומת', 'v1'), ('מאומתת', 'v1'), ('מאומתים', 'v1'), ('מאומתות', 'v1'),
    ('כמעט ודאי', 'v2'), ('כמעט ודאית', 'v2'),
    ('ככל הנראה', 'v3'),
    ('טעון אימות', 'v4'), ('טעונה אימות', 'v4'), ('טעונים אימות', 'v4'),
    ('טעונות אימות', 'v4'), ('טעון בירור', 'v4'), ('טרם נבדק', 'v4'), ('טרם נבדקו', 'v4'),
]
_RANK_RE = re.compile(
    r'<strong>(' + '|'.join(re.escape(w) for w, _ in sorted(RANKS, key=lambda x: -len(x[0]))) + r')</strong>')
_RANK_CLASS = {w: c for w, c in RANKS}


_LABEL_BEFORE = re.compile(r'(?:^|[>\s(\[—–·:,]|&nbsp;)$')


def rank_chips(html):
    """Render the certainty ladder as a chip only where it is used as a label.

    A label is a bolded rung that opens a clause — after a tag, a bracket, a
    dash, a colon or a comma. ``<strong>מאומת</strong>`` inside a running
    sentence is left as ordinary emphasis.
    """
    def sub(m):
        before = html[max(0, m.start() - 12):m.start()]
        after = html[m.end():m.end() + 2]
        if not _LABEL_BEFORE.search(before):
            return m.group(0)
        if after[:1] not in ('', ' ', '<', '.', ',', ')', ';', ':', '—', '–', '\n'):
            return m.group(0)
        w = m.group(1)
        return f'<span class="rank {_RANK_CLASS[w]}">{w}</span>'
    return _RANK_RE.sub(sub, html)


# ------------------------------------------------------------------ tables --
def wrap_tables(html):
    html = re.sub(r'<th(?![\w-])', '<th scope="col"', html)
    # the wrapper scrolls, so it must be reachable from the keyboard (WCAG 2.1.1)
    html = re.sub(r'<table\b[^>]*>',
                  lambda m: '<div class="tablewrap">' + m.group(0), html)
    return html.replace('</table>', '</table></div>')


# ------------------------------------------------------------- md figures ---
_MD_IMG = re.compile(r'<img alt="([^"]*)" src="([^"]+)"\s*/?>')


def number_figures(html, start=1):
    """Number every captioned <figure> in document order and label its caption.

    A figure without a caption is skipped and does not consume a number.
    Returns (html, count).
    """
    n = [start - 1]

    def sub(m):
        if '<figcaption>' not in m.group(0):
            return m.group(0)
        n[0] += 1
        return m.group(0).replace(
            '<figcaption>', f'<figcaption><span class="fignum">איור {n[0]}</span> — ', 1)

    html = re.sub(r'<figure\b[^>]*>.*?</figure>', sub, html, flags=re.S)
    return html, n[0] - start + 1


def markdown_images_to_figures(html, root=None):
    """`[![alt](crop)](full)` becomes a <figure>; the following <em> is its caption.

    When ``root`` is given, intrinsic width/height are written on every image so
    the page does not reflow while it loads.
    """
    from . import figures as _F
    # a linked image on its own line, optionally followed by an <em> caption paragraph
    pat = re.compile(
        r'<p><a href="([^"]+)"><img\b(?=[^>]*\balt="([^"]*)")(?=[^>]*\bsrc="([^"]+?)")[^>]*>'
        r'</a></p>'
        r'(?:\s*<p><em>((?:(?!</p>).)*?)</em></p>)?', re.S)

    def sub(m):
        href, alt, src, cap = m.group(1), m.group(2), m.group(3), m.group(4)
        caption = cap if cap else alt
        wh = _F.dims(root, src) if root else ''
        # `alt` arrives already escaped by the Markdown renderer; escaping it
        # a second time would publish &amp;quot; where &quot; was meant
        return (f'<figure><a href="{href}"><img src="{src}" alt="{alt}" '
                f'loading="lazy" decoding="async"{wh}></a>'
                f'<figcaption>{caption}</figcaption></figure>')

    html = pat.sub(sub, html)

    # a bare `![alt](src)` on its own line, with the same caption convention
    bare = re.compile(
        r'<p><img\b(?=[^>]*\balt="([^"]*)")(?=[^>]*\bsrc="([^"]+?)")[^>]*></p>'
        r'(?:\s*<p><em>((?:(?!</p>).)*?)</em></p>)?', re.S)

    def sub_bare(m):
        alt, src, cap = m.group(1), m.group(2), m.group(3)
        wh = _F.dims(root, src) if root else ''
        return (f'<figure><a href="{src}"><img src="{src}" alt="{alt}" '
                f'loading="lazy" decoding="async"{wh}></a>'
                f'<figcaption>{cap if cap else alt}</figcaption></figure>')

    return bare.sub(sub_bare, html)


_EXT_A = re.compile(r'(<a\b[^>]*\bhref="https?://[^"]*"[^>]*>)((?:(?!</a>).)*)(</a>)', re.S)


def mark_external(html):
    """Give every link that leaves the page the same small marker.

    The report's convention is a pair of links per source — the archive
    online, and the copy in the folder — so telling them apart at a glance
    is part of reading it, not decoration.
    """
    def sub(m):
        open_tag, inner = m.group(1), m.group(2)
        if 'target=' not in open_tag:
            open_tag = open_tag[:-1] + ' target="_blank" rel="noopener">'
        elif 'rel=' not in open_tag:
            open_tag = open_tag[:-1] + ' rel="noopener">'
        if '↗' in inner or '<img' in inner:
            return open_tag + inner + m.group(3)
        return (open_tag + inner
                + '<span class="ext" aria-hidden="true">↗</span>' + m.group(3))

    return _EXT_A.sub(sub, html)


# ---------------------------------------------------------------- helpers ---
def split_section(html, heading_regex):
    """Cut a trailing section out of a document. Returns (rest, section|'')."""
    m = re.search(heading_regex, html, re.S)
    if not m:
        return html, ''
    return html[:m.start()], html[m.start():]


def apply_transforms(html, transforms):
    for fn in transforms:
        html = bidi.apply_text(html, fn)
    return html
