# -*- coding: utf-8 -*-
"""What search engines and link previews read: canonical, Open Graph, JSON-LD.

Everything here is derived from data the archive already publishes — the
registry entry of each research (name, life line, couple) and the project's own
configuration — so no fact reaches the markup that is not on the page itself.
The site's address lives once, as `site.base_url` in research_registry.json;
with no address configured every helper returns '' and the pages are unchanged.
"""
import html as _h
import json
import os
import re
import urllib.parse

ARCHIVE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
_REGISTRY = os.path.join(ARCHIVE, 'research_registry.json')
FAVICON = 'favicon.svg'
OG_WIDTH = 1200


def registry():
    try:
        with open(_REGISTRY, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def base_url():
    b = registry().get('site', {}).get('base_url', '') or ''
    return b if b.endswith('/') else (b + '/' if b else '')


def research(slug):
    return next((r for r in registry().get('researches', []) if r.get('slug') == slug), {})


def url(*parts):
    """Absolute address of an archive-relative path; '' without a base_url."""
    b = base_url()
    if not b:
        return ''
    rel = '/'.join(p.strip('/') for p in parts if p)
    if rel.endswith('index.html'):
        rel = rel[:-len('index.html')]
    return b + urllib.parse.quote(rel, safe='/')


def plain(text, limit=None):
    """Tags out, entities resolved, whitespace folded — and cut at a word."""
    # a block boundary separates words; an inline tag (<b>, <a>) sits inside one
    t = re.sub(r'</?(?:p|br|li|div|h\d|ul|ol|tr|td)\b[^>]*>', ' ', text or '')
    t = re.sub(r'\s+', ' ', _h.unescape(re.sub(r'<[^>]+>', '', t))).strip()
    t = re.sub(r'\s+([,.;:)])', r'\1', t)
    if limit and len(t) > limit:
        t = t[:limit].rsplit(' ', 1)[0].rstrip(' ,;:—-') + '…'
    return t


# ---- the person, from the registry's life line ------------------------------

def _iso(d):
    """'16.4.1929' → '1929-04-16', '1/2021' or '1.2006' → '2021-01', '1939' → '1939'."""
    d = d.strip()
    m = re.fullmatch(r'(\d{1,2})\.(\d{1,2})\.(\d{4})', d)
    if m:
        return f'{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}'
    m = re.fullmatch(r'(\d{1,2})[./](\d{4})', d)
    if m:
        return f'{m.group(2)}-{int(m.group(1)):02d}'
    return d if re.fullmatch(r'\d{4}', d) else ''


def _end(part):
    """One end of a life line: (iso date, place) — either may be ''."""
    part = part.strip()
    if not part:
        return '', ''
    head, _, rest = part.partition(',')
    iso = _iso(head)
    if iso:
        return iso, rest.strip()
    # no date: a place alone ("— חולון") says where, not that the life ended there
    return '', ''


def person(r):
    """schema.org Person for a research subject, or {}."""
    if not r.get('name'):
        return {}
    p = {'@type': 'Person', 'name': r['name']}
    # `aka` on a card can list the family's surnames rather than the person's
    # own names; an explicit `alternate_names` list overrides it
    aka = r.get('alternate_names')
    if aka is None:
        aka = [a.strip(' "\'״') for a in re.split(r'[·,]', r.get('aka', ''))
               if a.strip(' "\'״')]
    if aka:
        p['alternateName'] = aka
    life = r.get('life', '')
    born, _, died = life.partition('—')
    bd, bp = _end(born)
    dd, dp = _end(died)
    if bd:
        p['birthDate'] = bd
    if bp:
        p['birthPlace'] = {'@type': 'Place', 'name': bp}
    if dd:
        p['deathDate'] = dd
    if dp:
        p['deathPlace'] = {'@type': 'Place', 'name': dp}
    for c in registry().get('site', {}).get('couples', []):
        if r.get('slug') in c.get('slugs', []):
            other = [research(s) for s in c['slugs'] if s != r.get('slug')]
            names = [o['name'] for o in other if o.get('name')]
            if names:
                p['spouse'] = [{'@type': 'Person', 'name': n} for n in names]
    return p


# ---- the head --------------------------------------------------------------

def og_image(root, path):
    """A ~1200px copy of the page's lead picture, archive-relative, or ''."""
    if not path:
        return ''
    from . import figures
    full = os.path.join(root, path)
    if not os.path.exists(full):
        return ''
    rel = figures.thumb(root, path, width=OG_WIDTH, quality=80)
    return os.path.relpath(os.path.join(root, rel), ARCHIVE).replace(os.sep, '/')


def _ld(obj):
    s = json.dumps(obj, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    return f'<script type="application/ld+json">{s}</script>\n'


def head(page_url, title, description, image_rel='', image_alt='', kind='article',
         ld=()):
    """canonical + favicon + Open Graph + Twitter + JSON-LD for one page."""
    b = base_url()
    if not b or not page_url:
        return ''
    e = lambda s: _h.escape(s or '', quote=True)
    site_name = registry().get('site', {}).get('title', '')
    img = url(image_rel) if image_rel else ''
    out = [f'<link rel="canonical" href="{e(page_url)}">',
           f'<link rel="icon" href="{e(url(FAVICON))}" type="image/svg+xml">',
           f'<meta property="og:type" content="{kind}">',
           '<meta property="og:locale" content="he_IL">',
           f'<meta property="og:site_name" content="{e(site_name)}">',
           f'<meta property="og:title" content="{e(title)}">',
           f'<meta property="og:description" content="{e(description)}">',
           f'<meta property="og:url" content="{e(page_url)}">']
    if img:
        out += [f'<meta property="og:image" content="{e(img)}">',
                f'<meta property="og:image:alt" content="{e(image_alt or title)}">',
                '<meta name="twitter:card" content="summary_large_image">']
    else:
        out.append('<meta name="twitter:card" content="summary">')
    return '\n'.join(out) + '\n' + ''.join(_ld(o) for o in ld if o)


def breadcrumbs(*crumbs):
    """BreadcrumbList from (name, absolute url) pairs."""
    items = [{'@type': 'ListItem', 'position': i, 'name': n, 'item': u}
             for i, (n, u) in enumerate(crumbs, 1) if u]
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList',
            'itemListElement': items} if len(items) > 1 else {}


def article(page_url, headline, description, about, image_rel='', modified=''):
    site = registry().get('site', {})
    a = {'@context': 'https://schema.org', '@type': 'Article',
         'headline': headline[:110], 'description': description,
         'inLanguage': 'he', 'url': page_url, 'mainEntityOfPage': page_url,
         'author': {'@type': 'Organization', 'name': site.get('title', ''), 'url': base_url()},
         'publisher': {'@type': 'Organization', 'name': site.get('title', ''), 'url': base_url()},
         'isPartOf': {'@type': 'WebSite', 'name': site.get('title', ''), 'url': base_url()}}
    if about:
        a['about'] = about
    if image_rel:
        a['image'] = url(image_rel)
    if modified:
        a['dateModified'] = modified
    return a


def iso_date(text):
    """The first dd.mm.yyyy in a line such as 'עודכן 13.09.2026 · מהדורה 47'."""
    m = re.search(r'(\d{1,2})\.(\d{1,2})\.(\d{4})', text or '')
    return f'{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}' if m else ''


# ---- the research pages ----------------------------------------------------

def project_head(cfg, which, filename, updated='', lead_image=''):
    """The head block for one of a project's pages.

    ``which`` is 'story', 'report' or 'tree'. Titles and descriptions differ by
    page, so the story and the full report stop competing for the same search.
    """
    b = base_url()
    if not b:
        return '', None, None
    r = research(cfg.slug)
    name = r.get('name') or cfg.title
    t, d = titles(cfg, which)
    page = url(cfg.slug, filename)
    img = og_image(cfg.root, lead_image) or (r.get('cover') or '')
    alt = (cfg.story.portrait_alt if (cfg.story and cfg.story.portrait == lead_image) else '') \
        or r.get('cover_alt', '') or name
    who = person(r)
    crumbs = [(registry().get('site', {}).get('title', ''), b),
              (name, url(cfg.slug, cfg.story_name() if cfg.story else cfg.main_html))]
    if which == 'report':
        crumbs.append(('הדוח המלא', page))
    elif which == 'tree':
        crumbs.append(('עץ המשפחה', page))
    ld = [article(page, t, d, who, img, iso_date(updated)) if which != 'tree' else {},
          breadcrumbs(*crumbs)]
    return head(page, t, d, img, alt, 'article', ld), t, d


def titles(cfg, which):
    """(title, description) for a project page."""
    r = research(cfg.slug)
    name = r.get('name') or cfg.title
    lead = r.get('seo_title') or cfg.story_title or cfg.title
    if which == 'story':
        desc = r.get('seo_description') or (plain(cfg.story.lede, 160) if cfg.story else '')
        return lead, desc or plain(cfg.meta_description, 160)
    if which == 'tree':
        return (f'עץ המשפחה של {name}',
                plain(f'עץ המשפחה של {name}, {r.get("life", "")} — '
                      f'הדורות, בני הזוג והילדים, כפי שעלו מן המסמכים.', 160))
    return f'{name} — הדוח המלא: מסמכים ומקורות', plain(cfg.meta_description, 160)


def set_title(html, title):
    """Swap the page's <title> for the search title (the h1 is left alone)."""
    return re.sub(r'<title>.*?</title>', f'<title>{_h.escape(title)}</title>', html,
                  count=1, flags=re.S)


def set_description(html, desc):
    tag = f'<meta name="description" content="{_h.escape(desc, quote=True)}">'
    if re.search(r'<meta name="description"[^>]*>', html):
        return re.sub(r'<meta name="description"[^>]*>', lambda m: tag, html, count=1)
    return html.replace('</title>', '</title>\n' + tag, 1)


def inject(html, block):
    return html.replace('</head>', block + '</head>', 1) if block else html


# ---- the sitemap -----------------------------------------------------------

_CANON = re.compile(r'<link rel="canonical" href="([^"]+)">')
_MOD = re.compile(r'"dateModified":"([\d-]+)"')


def sitemap(paths):
    """sitemap.xml text for the archive-relative pages that are their own canonical."""
    rows = []
    for rel in paths:
        full = os.path.join(ARCHIVE, rel)
        try:
            text = open(full, encoding='utf-8').read()
        except OSError:
            continue
        m = _CANON.search(text)
        if not m or m.group(1) != url(rel):
            continue          # redirects, raw copies and pages that point elsewhere
        mod = _MOD.search(text)
        last = f'<lastmod>{mod.group(1)}</lastmod>' if mod else ''
        rows.append(f'  <url><loc>{_h.escape(m.group(1))}</loc>{last}</url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + '\n'.join(sorted(set(rows))) + '\n</urlset>\n'), len(set(rows))
