# -*- coding: utf-8 -*-
"""Quality gates. Every check returns a list of problem strings."""
import html as _h
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


def _git_tracked(root, cached_only=False):
    """Paths (relative to `root`) that git tracks under it — with cached_only=False also
    untracked-but-not-ignored files. None when `root` is not inside a git checkout."""
    import subprocess
    args = ['git', 'ls-files', '-z', '--cached'] + ([] if cached_only else ['--others', '--exclude-standard']) + ['.']
    try:
        out = subprocess.run(args, cwd=root, capture_output=True, check=True).stdout
    except Exception:
        return None
    if not out and cached_only:
        return None
    return {os.path.normpath(p.decode('utf-8', 'replace')) for p in out.split(b'\0') if p}


def _git_ignored(root, t):
    import subprocess
    try:
        r = subprocess.run(['git', 'check-ignore', '-q', t], cwd=root, capture_output=True)
        return r.returncode == 0
    except Exception:
        return False


def local_links_exist(html, root, label='', git_check=True):
    """A link target must exist on disk — and, in a git checkout, must not be ignored:
    an ignored file will not reach the published site even though the build sees it."""
    bad = []
    for t in sorted(_local_targets(html)):
        if not t:
            continue
        if not os.path.exists(os.path.join(root, t)):
            bad.append(f'{label}קישור פנימי ללא קובץ: {t}')
        elif git_check and _git_ignored(root, t):
            bad.append(f'{label}קישור לקובץ שמוחרג מ-git (לא יפורסם): {t}')
    return bad


def untracked_link_targets(html, root):
    """Warnings: link targets that exist and are not ignored, but were never `git add`-ed —
    a build passes, a publish of the page would 404 on them. Empty outside a git checkout."""
    tracked = _git_tracked(root, cached_only=True)
    if tracked is None:
        return []
    return [f'קישור לקובץ שאינו במעקב git — יש להוסיפו (git add): {t}'
            for t in sorted(_local_targets(html))
            if t and not t.startswith('..') and os.path.exists(os.path.join(root, t))
            and os.path.normpath(t) not in tracked]


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


# codepoints with no glyph in the serif/sans stacks this theme uses: they ship
# as an empty box. Add to this list, never assume a symbol renders.
TOFU = {
    '\U0001F5CE': 'U+1F5CE 🗎 — use U+1F4C4 📄',
    '\U0001F5CB': 'U+1F5CB — use U+1F4C4 📄',
    '\U0001F5CF': 'U+1F5CF — use U+1F4C4 📄',
    '\U0001F5B9': 'U+1F5B9 — use U+1F4C4 📄',
    '\u2317': 'U+2317 — no glyph in common stacks',
}


def glyph_coverage(html):
    return [f'תו ללא גליף בגופני העמוד: {why} ({html.count(ch)} מופעים)'
            for ch, why in TOFU.items() if ch in html]


def template_leakage(html):
    """A %% or {{ that survived into the output.

    The engine mixes %-formatted strings (the inline JS) with f-strings (the
    CSS). A literal % in the wrong one either crashes the build or, worse,
    ships a declaration the browser silently drops.
    """
    bad = []
    # a literal quoted inside <code> is documentation, not leakage
    body = re.sub(r'<code\b.*?</code>', '', _SCRIPT.sub('', html), flags=re.S)
    n = len(re.findall(r'%%', body))
    if n:
        bad.append(f'סימן %% דלף לפלט: {n}')
    n = len(re.findall(r'(?<![{])\{\{(?![{])|(?<![}])\}\}(?![}])', body))
    if n:
        bad.append(f'סוגריים מסולסלים כפולים בפלט: {n}')
    return bad


_HREF_FILE = re.compile(
    r'<a\b[^>]*\bhref="(?!https?://|#|mailto:)([^"]*\.'
    r'(?:jpe?g|JPG|png|gif|webp|pdf|json|txt|md|mp3|wav|m4a|csv|xlsx?))"[^>]*>')


def source_links_open_out(html):
    """A source file that replaces the page costs the reader their place.

    The report is tens of thousands of pixels long; returning from a scan
    reloads the whole document. Source files open beside it.
    """
    bad = [m.group(0)[:70] for m in _HREF_FILE.finditer(html)
           if 'target=' not in m.group(0)]
    if not bad:
        return []
    return [f'קישור לקובץ מקור שאינו נפתח בלשונית נפרדת: {len(bad)}', '   ' + bad[0]]


# an archival scan is not a web asset: above this the page must serve a copy
IMAGE_BUDGET = 320_000


def images_are_light(html, root):
    """The page must not serve the archival original."""
    bad = []
    for src in sorted(set(re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', html))):
        if src.startswith(('http', 'data:')):
            continue
        p = os.path.join(root, urllib.parse.unquote(src))
        try:
            n = os.path.getsize(p)
        except OSError:
            continue
        if n > IMAGE_BUDGET:
            bad.append(f'תמונה כבדה מדי לעמוד ({n // 1024}KB): {src}')
    return bad[:6]


def entity_hygiene(html):
    """A double-escaped entity: &amp;quot; where &quot; was meant."""
    n = len(re.findall(r'&amp;(?:quot|amp|lt|gt|#\d+|nbsp);', html))
    return [f'ישות HTML שקודדה פעמיים: {n}'] if n else []


_TAG = re.compile(r'<[^>]+>')
# an <svg> family tree carries the name of every person in it; those labels are a
# diagram, not reading, and counting them as prose would penalise a big tree
_SCRIPT_STYLE = re.compile(r'<(script|style|svg)\b.*?</\1>', re.S | re.I)

# Gates on the shape of a page, not on its correctness. Each number is the point
# at which a reader stops reading: a lede that runs past a screenful stops being
# an abstract, and a navigation bar with more than six destinations stops being
# a map.
LEDE_MAX = 1200         # characters of rendered text — an abstract, not a chapter
STORY_WORDS_MAX = 1800
NAV_LINKS_MAX = 6


def _text(html):
    return _TAG.sub(' ', _SCRIPT_STYLE.sub('', html))


def reading_shape(html, is_story=False):
    """The lede, the navigation row, and (on a story page) the whole page length."""
    out = []
    # the lede holds only paragraphs, so its own closing tag is the first one
    m = re.search(r'<div class="lede">(.*?)</div>', html, re.S)
    if m:
        n = len(_h.unescape(_text(m.group(1))).strip())
        if n > LEDE_MAX:
            out.append(f'הלִיד ארוך מדי: {n} תווים (המרב {LEDE_MAX}) — '
                       f'מה שמעבר לתקציר שייך לפרק 1')
    nav = re.search(r'<nav class="nav".*?</nav>', html, re.S)
    if nav:
        n = len(re.findall(r'<a\b', nav.group(0)))
        if n > NAV_LINKS_MAX:
            out.append(f'בניווט {n} קישורים (המרב {NAV_LINKS_MAX})')
    if is_story:
        words = len(_h.unescape(_text(html)).split())
        if words > STORY_WORDS_MAX:
            out.append(f'עמוד הסיפור ארוך מדי: {words} מילים (המרב {STORY_WORDS_MAX})')
    return out


def no_build_paths(html):
    """The page must not explain its own directory layout to the reader.

    The changelog is exempt: an entry that records the removal of such a mention
    has to be able to name it.
    """
    # only the opening of the page: naming the folder inside the method chapter
    # is a researcher talking to a researcher, and belongs there
    head = html.split('<h2', 1)[0]
    head = re.sub(r'<head\b.*?</head>', '', head, flags=re.S | re.I)
    body = _text(head)
    return (['הטקסט הגלוי מזכיר את תיקיית docs/ — פרט בנייה, לא תוכן לקורא']
            if re.search(r'(?<![\w/.-])docs/(?![\w])', body) else [])


def cross_page_anchors(html, other_html, other_name, label=''):
    """Every deep link into the other page must land on an id that exists there.

    The story page is built entirely out of links into the report; a renamed
    heading would silently turn all of them into links to the top of a 47,000-pixel
    document.
    """
    ids = set(re.findall(r'\sid="([^"]+)"', other_html))
    bad = []
    quoted = urllib.parse.quote(other_name)
    for m in re.finditer(r'href="([^"#]*)#([^"]+)"', html):
        target, frag = m.group(1), m.group(2)
        if urllib.parse.unquote(target) != other_name and target != quoted:
            continue
        if frag not in ids:
            bad.append(f'{label}קישור עמוק אל עוגן שאינו קיים ב{other_name}: #{frag}')
    return sorted(set(bad))


def run_all(html, root, patterns=()):
    problems = []
    for fn in (markup_integrity, bidi_hygiene, markdown_leftovers, images_have_alt,
               attribute_hygiene, entity_hygiene, anchors_resolve, duplicate_ids,
               search_targets_resolve, glyph_coverage, template_leakage,
               source_links_open_out):
        problems += fn(html)
    problems += images_are_light(html, root)
    problems += local_links_exist(html, root)
    problems += prose_files_exist(html, root)
    problems += privacy(html, patterns)
    return problems


_ID_NEAR = re.compile(r'(?:זהות|ת\.?ז\.?|ת"ז)[^\n]{0,40}?\b(\d{7,9})\b|\b(\d{7,9})\b[^\n]{0,40}?(?:זהות|ת\.?ז\.?|ת"ז)')
_APPROX_YEAR = re.compile(r'~\s?19\d\d')


def ledger_privacy(root, published_ids=(), md_glob=('*.md',), warn=None):
    """Scan every git-tracked markdown file of the project (ledgers included — they are
    served by GitHub Pages like everything else) for identity numbers that were not
    explicitly cleared for publication, and for approximate birth years ("~1954") of
    living people. Returns problem strings."""
    import glob as _g
    tracked = _git_tracked(root)
    bad = []
    for pat in md_glob:
        for f in sorted(set(_g.glob(os.path.join(root, pat)))):
            rel = os.path.normpath(os.path.relpath(f, root))
            if tracked is not None and rel not in tracked:
                continue
            if os.path.basename(f).startswith('audit-'):
                continue
            txt = open(f, encoding='utf-8', errors='replace').read()
            for m in _ID_NEAR.finditer(txt):
                n = m.group(1) or m.group(2)
                if n not in published_ids:
                    bad.append(f'{rel}: מספר זהות שלא אושר לפרסום ({n[:2]}…{n[-2:]})')

            if warn is not None:
                for m in _APPROX_YEAR.finditer(txt):
                    if int(m.group(0)[-4:]) >= 1940:
                        warn.append(f'{rel}: שנת לידה משוערת "{m.group(0)}" — לוודא שאינה של אדם חי שנמסרה בעל-פה (9.6)')
    return sorted(set(bad))
