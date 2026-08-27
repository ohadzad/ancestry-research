# -*- coding: utf-8 -*-
"""Quality gates. Every check returns a list of problem strings."""
import os
import re
import urllib.parse


_SCRIPT = re.compile(r'<script\b.*?</script>', re.S)


def _local_targets(html):
    html = _SCRIPT.sub('', html)
    out = set()
    for m in re.finditer(r'(?:href|src)="([^"#?][^"]*)"', html):
        t = m.group(1)
        if t.startswith(('http://', 'https://', 'mailto:', 'data:', '#')):
            continue
        out.add(urllib.parse.unquote(t.split('#')[0].split('?')[0]))
    return out


def local_links_exist(html, root, label=''):
    bad = []
    for t in sorted(_local_targets(html)):
        if not t:
            continue
        if not os.path.exists(os.path.join(root, t)):
            bad.append(f'{label}קישור פנימי ללא קובץ: {t}')
    return bad


def anchors_resolve(html):
    ids = set(re.findall(r'\sid="([^"]+)"', html))
    bad = []
    for m in re.finditer(r'href="#([^"]+)"', _SCRIPT.sub('', html)):
        if m.group(1) not in ids:
            bad.append(f'עוגן פנימי ללא יעד: #{m.group(1)}')
    return sorted(set(bad))


def duplicate_ids(html):
    ids = re.findall(r'\sid="([^"]+)"', html)
    seen, dup = set(), set()
    for i in ids:
        if i in seen:
            dup.add(i)
        seen.add(i)
    return [f'מזהה כפול: {i}' for i in sorted(dup)]


_OPAQUE = re.compile(r'<(svg|style|script|pre)\b.*?</\1>', re.S)
_TAGS = re.compile(r'<[^>]+>')


def _prose(html):
    t = re.sub(r'<bdi[^>]*>.*?</bdi>', '', html, flags=re.S)
    t = _OPAQUE.sub('', t)
    t = re.sub(r'<code\b.*?</code>', '', t, flags=re.S)
    # a NUL rather than a space: a tag boundary breaks a run, so two short
    # fragments either side of <em> are not mistaken for one long one
    return _TAGS.sub('\x00', t)


def markup_integrity(html):
    bad = []
    for tag in ('em', 'strong', 'bdi', 'figure', 'figcaption', 'section', 'table', 'div'):
        o = len(re.findall(rf'<{tag}\b', html))
        c = len(re.findall(rf'</{tag}>', html))
        if o != c:
            bad.append(f'תגיות לא מאוזנות: <{tag}> {o} מול {c}')
    n = len(re.findall(r'<a\b[^>]*>(?:(?!</a>).)*?<a\b', html, re.S))
    if n:
        bad.append(f'קישורים מקוננים: {n}')
    n = len(re.findall(r'<bdi\b[^>]*>(?:(?!</bdi>).)*?<bdi\b', html, re.S))
    if n:
        bad.append(f'מעטפות כיווניות מקוננות: {n}')
    n = (len(re.findall(r'<em>[^<]*<strong>[^<]*</em>', html))
         + len(re.findall(r'<strong>[^<]*<em>[^<]*</strong>', html)))
    if n:
        bad.append(f'הדגשות מוצלבות: {n}')
    for tag in ('em', 'strong', 'figure', 'section'):
        depth = 0
        for m in re.finditer(rf'<{tag}\b[^>]*>|</{tag}>', html):
            depth += -1 if m.group(0).startswith('</') else 1
            if depth < 0:
                bad.append(f'תגית </{tag}> ללא פתיחה (מיקום {m.start()})')
                break
            if depth > 1 and tag in ('em', 'figure'):
                bad.append(f'<{tag}> מקונן (מיקום {m.start()})')
                break
    for m in re.finditer(r'<(style|script|svg)\b.*?</\1>', html, re.S):
        if '<bdi' in m.group(0):
            bad.append(f'מעטפת כיווניות בתוך <{m.group(1)}>')
            break
    return bad


_TRAIL = re.compile(r'[,;:.]$')


def bidi_hygiene(html):
    """Every rule in bidi.RULES is re-run over the prose; a survivor is a hole.

    Deriving the gate from the rule list means a rule that stops matching —
    a project whose reference codes use a different separator, say — is
    reported instead of shipping reversed.
    """
    from . import bidi
    bad = []
    for b in re.findall(r'<bdi[^>]*>(.*?)</bdi>', html, re.S):
        if b.count('(') != b.count(')'):
            bad.append(f'סוגריים לא מאוזנים במעטפת כיווניות: {b[:60]}')
        # a Latin sentence may legitimately end in a full stop; a bare number
        # range may not — there the punctuation belongs to the Hebrew clause
        if (_TRAIL.search(b) and not re.search(r'[A-Za-zÀ-ɏ]', b)
                and not re.search(r'\d\.\d+$', b)):
            bad.append(f'פיסוק עברי נלכד במעטפת כיווניות: {b[:60]}')
    t = _prose(html)
    for i, (rx, _rep) in enumerate(bidi.RULES, 1):
        n = len(rx.findall(t))
        if n:
            bad.append(f'רצף ללא מעטפת כיווניות (כלל {i}): {n}')
    return bad[:10]


def markdown_leftovers(html):
    t = _prose(html)
    bad = []
    n = len(re.findall(r'\]\([^)\s]', t))
    if n:
        bad.append(f'קישורי Markdown שלא עובדו: {n}')
    n = len(re.findall(r'!\[[^\]]*\]\(', t))
    if n:
        bad.append(f'תחביר תמונה שלא עובד: {n}')
    n = len(re.findall(r'(?<![">=/\w])https?://', t))
    if n:
        bad.append(f'כתובות גולמיות בפרוזה: {n}')
    n = t.count('**')
    if n:
        bad.append(f'סימני הדגשה גולמיים: {n}')
    return bad


_IMG = re.compile(r'<img\b[^>]*>')


def images_have_alt(html):
    bad = []
    for m in _IMG.finditer(html):
        tag = m.group(0)
        a = re.search(r'\balt="([^"]*)"', tag)
        if a is None:
            bad.append(f'תמונה בלי טקסט חלופי: {tag[:70]}')
        elif re.search(r'\salt="[^"]*"[^>]*"', tag) and tag.count('"') % 2:
            bad.append(f'טקסט חלופי לא מצוטט כראוי: {tag[:70]}')
    return bad[:8]


def privacy(html, patterns):
    low = html.lower()
    return [f'דפוס פרטיות הופיע בעמוד: {p}' for p in patterns if p.lower() in low]


_WELLFORMED = re.compile(
    r'<[\w:-]+'
    r'(?:\s+[\w:.@-]+(?:=(?:"[^"]*"|\'[^\']*\'|[^\s>"\'`]+))?)*'
    r'\s*/?>$')


def attribute_hygiene(html):
    """Catch an attribute value that was broken open by an unescaped quote.

    Counting quotes is not enough — a value broken by a *pair* of quotes
    leaves an even count while silently swallowing the attributes after it.
    """
    bad = []
    for m in re.finditer(r'<(img|a|input|source|iframe)\b[^>]*>', html):
        tag = m.group(0)
        if not _WELLFORMED.match(tag):
            bad.append(f'תגית עם מבנה מאפיינים פגום: {tag[:80]}')
    return bad[:8]


_PROSE_FILE = re.compile(r'(?<![\w/])((?:docs|site)/[\w./-]+\.'
                         r'(?:jpe?g|png|gif|pdf|json|mp3|wav|txt|md|svg|webp))', re.I)


def prose_files_exist(html, root):
    """A file named in the prose but absent from disk: a link that never was."""
    bad = []
    for name in sorted(set(_PROSE_FILE.findall(_prose(html)))):
        if not os.path.exists(os.path.join(root, name)):
            bad.append(f'קובץ שהוזכר בפרוזה ואינו קיים: {name}')
    return bad[:8]


_IDX = re.compile(r'var IDX = (\[.*?\]);\n', re.S)


def search_targets_resolve(html):
    """The search index lives inside <script>, where the anchor gate cannot see it."""
    m = _IDX.search(html)
    if not m:
        return []
    try:
        import json
        idx = json.loads(m.group(1).replace('<\\/', '</'))
    except ValueError:
        return ['אינדקס החיפוש אינו JSON תקין']
    ids = set(re.findall(r'\sid="([^"]+)"', html))
    bad = [f'יעד חיפוש ללא עוגן: {it.get("h")} ({it.get("t", "")[:30]})'
           for it in idx if str(it.get('h', '')).startswith('#') and it['h'][1:] not in ids]
    return bad[:8]


def entity_hygiene(html):
    """A double-escaped entity: &amp;quot; where &quot; was meant."""
    n = len(re.findall(r'&amp;(?:quot|amp|lt|gt|#\d+|nbsp);', html))
    return [f'ישות HTML שקודדה פעמיים: {n}'] if n else []


def run_all(html, root, patterns=()):
    problems = []
    for fn in (markup_integrity, bidi_hygiene, markdown_leftovers, images_have_alt,
               attribute_hygiene, entity_hygiene, anchors_resolve, duplicate_ids,
               search_targets_resolve):
        problems += fn(html)
    problems += local_links_exist(html, root)
    problems += prose_files_exist(html, root)
    problems += privacy(html, patterns)
    return problems
