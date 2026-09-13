# -*- coding: utf-8 -*-
"""The page shell: hero, sticky navigation, in-page search, person index, footer."""
import html as _h
import json
import re
import urllib.parse

from . import mdpipe, theme

# Six destinations at most, in one row. The chapter strip that used to sit
# under them cost a quarter of a phone screen and spoke in the language of the
# researcher's own filing ("4 · נשללו"); it now lives as a table of contents at
# the top of the report, where the full titles fit.
SECTIONS = [
    ('report', 'הדוח'),
    ('tree', 'עץ המשפחה'),
    ('gallery', 'מסמכי מפתח'),
    ('people', 'אינדקס אנשים'),
    ('index', 'אינדקס מקורות'),
]


def hero(cfg, edition, stamp):
    crumb = ''
    if cfg.breadcrumb:
        href, label = cfg.breadcrumb
        crumb = f'<div class="crumb"><a href="{href}">← {label}</a></div>'
    spine = ''
    if cfg.spine:
        spine = '<div class="spine">' + ''.join(
            f'<div><b>{f.value}</b><span>{f.label}</span></div>' for f in cfg.spine) + '</div>'
    # `edition` reads "עודכן <date> · מהדורה N"; when the page was built the same
    # day, repeating the date as "נבנה" says nothing and reads as noise
    parts = [edition] + ([] if stamp in edition else [f'נבנה {stamp}'])
    meta = ' · '.join(x for x in parts if x)
    return (f'<header class="hero"><div class="hero-in">{crumb}'
            f'<h1>{_h.escape(cfg.title)}</h1>'
            f'<p class="subject">{cfg.subject}</p>'
            f'<div class="meta">{meta}</div>{spine}</div></header>')


def nav(present, chapters, story_href=''):
    secs = ''.join(f'<a href="#{sid}">{label}</a>'
                   for sid, label in SECTIONS if sid in present)
    back = (f'<a class="nav-story" href="{story_href}">הסיפור →</a>'
            if story_href else '')
    # the results list sits directly after the input (tab order) but is
    # positioned out of flow (so showing it never changes the nav's height)
    return (
        '<nav class="nav" aria-label="ניווט ראשי"><div class="nav-in">'
        f'<div class="nav-row">{back}{secs}'
        # on a phone the whole row scrolls in one line; the field itself opens
        # from this button, so the search costs no vertical space until it is used
        '<button type="button" class="qtoggle" aria-expanded="false" '
        'aria-controls="q">חיפוש</button>'
        '<div class="qwrap">'
        '<input id="q" type="search" placeholder="חיפוש בפרקים, אנשים ומקורות…" '
        'aria-label="חיפוש בפרקים, באנשים ובמקורות" autocomplete="off" '
        'aria-controls="qres" hidden>'
        '<div id="qres" role="region" aria-label="תוצאות החיפוש" aria-live="polite" hidden></div>'
        '</div></div>'
        '</div></nav>')


def toc(chapters):
    """The report's table of contents, at the top of the report itself.

    Full chapter titles, where there is room for them — a nav chip truncated to
    "5 · המשפחה במסמכים" carries no scent for a reader who has not already read
    the chapter."""
    if not chapters:
        return ''
    items = ''.join(f'<li><a href="#{sid}">{_h.escape(full)}</a></li>'
                    for sid, _short, full in chapters)
    return ('<details class="toc"><summary>תוכן העניינים — תשעה פרקים</summary>'
            f'<ol class="toc-list">{items}</ol></details>')


# --------------------------------------------------------------- the story --
# The story page answers, from its first screen: who was this, what is certain,
# what is still open, and where are the photographs. Everything that makes the
# report an auditable record — the rejected candidates, the negative findings,
# the method — stays in the report, one click away.

STORY_SECTIONS = [
    ('timeline', 'ציר הזמן'),
    ('docs', 'המסמכים'),
    ('tree', 'עץ המשפחה'),
    ('open', 'מה עוד פתוח'),
]


def _story_link(href, label):
    return f'<a href="{href}">{label}</a>' if href else ''


def story_hero(cfg, story, updated, report_href):
    crumb = ''
    if cfg.breadcrumb:
        href, label = cfg.breadcrumb
        crumb = f'<div class="crumb"><a href="{href}">← {label}</a></div>'
    spine = ''
    facts = cfg.story_spine or cfg.spine
    if facts:
        spine = '<div class="spine">' + ''.join(
            f'<div><b>{f.value}</b><span>{f.label}</span></div>' for f in facts) + '</div>'
    portrait = ''
    if story.portrait:
        alt = _h.escape(story.portrait_alt or cfg.title, quote=True)
        cap = (f'<figcaption>{story.portrait_caption}</figcaption>'
               if story.portrait_caption else '')
        portrait = (f'<figure class="portrait"><img src="{story.portrait}" alt="{alt}" '
                    f'decoding="async">{cap}</figure>')
    subject = cfg.story_subject or cfg.subject
    upd = f'<div class="meta">{updated}</div>' if updated else ''
    return (f'<header class="hero story-hero"><div class="hero-in">{crumb}'
            f'<div class="hero-cols">{portrait}<div class="hero-text">'
            f'<h1>{_h.escape(cfg.story_title or cfg.title)}</h1>'
            f'<p class="subject">{subject}</p>{upd}</div></div>'
            f'{spine}</div></header>')


def story_nav(present, report_href):
    links = ''.join(f'<a href="#{sid}">{label}</a>'
                    for sid, label in STORY_SECTIONS if sid in present)
    return ('<nav class="nav" aria-label="ניווט ראשי"><div class="nav-in">'
            f'<div class="nav-row">{links}'
            f'<a class="nav-report" href="{report_href}">הדוח המלא ←</a>'
            '</div></div></nav>')


def verdicts_block(story):
    """Three columns: what is certain, what is probable, what is still open."""
    if not story.verdicts:
        return ''
    cols = []
    for v in story.verdicts:
        chip = mdpipe.rank_chip(v.rank)
        items = ''.join(
            f'<li>{text}{(" " + _story_link(href, "בדוח")) if href else ""}</li>'
            for text, href in v.lines)
        cols.append(f'<div class="verdict"><h3>{_h.escape(v.title)} {chip}</h3>'
                    f'<ul>{items}</ul></div>')
    return f'<div class="verdicts">{"".join(cols)}</div>'


def timeline_block(story):
    """The life in order — the one thing the report never shows."""
    if not story.timeline:
        return ''
    rows = []
    for b in story.timeline:
        chip = mdpipe.rank_chip(b.rank)
        place = f'<span class="tl-place">{b.place}</span>' if b.place else ''
        # the date is the row's handle: it is what the eye scans down
        when = f'<div class="tl-when"><b>{b.when}</b>{place}</div>'
        more = _story_link(b.href, 'בדוח ←')
        tail = f'<span class="tl-more">{more}</span>' if more else ''
        rows.append(f'<li class="tl">{when}'
                    f'<div class="tl-what"><p>{b.what}</p>'
                    f'<div class="tl-foot">{chip}{tail}</div></div></li>')
    note = f'<p class="note">{story.timeline_note}</p>' if story.timeline_note else ''
    return f'{note}<ol class="timeline">{"".join(rows)}</ol>'


def docs_block(cfg, story, root_thumb):
    """Key documents as cards: picture, date, what it proves, how sure."""
    if not story.docs:
        return ''
    cards = []
    for d in story.docs:
        img = root_thumb(d.img)
        alt = _h.escape(f'{d.title} — {d.when}', quote=True)
        chip = mdpipe.rank_chip(d.rank)
        more = _story_link(d.href, 'בדוח ←')
        pos = f' style="object-position:{d.focus}"' if d.focus != 'center top' else ''
        pic = (f'<img src="{img}" alt="{alt}" loading="lazy" decoding="async"{pos}>'
               if img else '')
        # the whole card is the click target for the scan; the report link is
        # a second, explicit destination
        cards.append(
            f'<figure class="doccard"><a class="doc-img" href="{d.img}">{pic}</a>'
            f'<figcaption><span class="doc-when">{d.when}</span>'
            f'<b>{d.title}</b><span class="doc-proves">{d.proves}</span>'
            f'<span class="doc-foot">{chip}{more}</span></figcaption></figure>')
    note = f'<p class="note">{story.docs_note}</p>' if story.docs_note else ''
    return f'{note}<div class="doccards">{"".join(cards)}</div>'


def open_block(story, report_href, report_label):
    items = ''.join(f'<li>{text}{(" " + _story_link(href, "בדוח")) if href else ""}</li>'
                    for text, href in story.open_questions)
    lst = f'<ul class="openq">{items}</ul>' if items else ''
    return (f'{lst}<p class="report-cta"><a class="btn big" href="{report_href}">'
            f'{report_label}</a></p>')


def story_page(cfg, story, updated, report_href, sections, present):
    js = _JS % '[]'
    title = _h.escape(cfg.story_title or cfg.title)
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{_h.escape(cfg.meta_description)}">
<meta name="color-scheme" content="light">
<style>{theme.css(cfg.palette)}</style>
</head>
<body class="story">
<a class="skip" href="#lede">דילוג לתוכן</a>
<a class="top" href="#top" aria-label="חזרה לראש העמוד" tabindex="-1">↑</a>
<span id="top"></span>
{story_hero(cfg, story, updated, report_href)}
{story_nav(present, report_href)}
<main>
{sections}
</main>
<footer>{cfg.footer_note}</footer>
<script>{js}</script>
</body>
</html>
"""


def ladder_legend(cfg, open_by_default=False):
    """The certainty ladder, spelled out where it is first used.

    Both pages grade from their opening sentence, while the chapter that defines
    the ladder sits at the far end of the report. One collapsed line at the top
    costs nothing and removes the guesswork.
    """
    chips = ''.join(
        f'<div class="rung">{mdpipe.rank_chip(w)}'
        f'<span>{mdpipe.RANK_HELP[mdpipe._RANK_CLASS[w]].split("—", 1)[1].strip()}</span></div>'
        for w in mdpipe.LADDER)
    terms = ''
    if cfg.glossary:
        rows = ''.join(f'<div class="term"><b>{_h.escape(t)}</b><span>{d}</span></div>'
                       for t, d in cfg.glossary)
        terms = f'<div class="terms">{rows}</div>'
    op = ' open' if open_by_default else ''
    return (f'<details class="ladder"{op}><summary>סולם הוודאות'
            f'{" ומונחי המחקר" if terms else ""} — מה המילים האלה אומרות</summary>'
            f'<div class="ladder-in"><div class="rungs">{chips}</div>{terms}</div></details>')


def people_section(cfg):
    if not cfg.people:
        return ''
    cards = []
    for p in cfg.people:
        # only & and " need escaping here; escaping the apostrophe would turn
        # the anchor into &#x27; and no longer match the heading id it targets
        href = p.anchor.replace('&', '&amp;').replace('"', '&quot;')
        name = (f'<a href="{href}">{_h.escape(p.name)}</a>'
                if p.anchor else _h.escape(p.name))
        # a dates string that carries Hebrew ("לפני 08/1944", "כיהן 1894–1924")
        # must stay in the RTL flow; the document-wide bidi pass wraps the
        # numeric runs inside it. Only an all-Latin/numeric string is isolated.
        dt = _h.escape(p.dates)
        if p.dates and not re.search(r'[\u0590-\u05ff]', p.dates):
            dt = f'<bdi dir="ltr">{dt}</bdi>'
        d = f'<span class="d">{dt}</span>' if p.dates else ''
        r = f'<span class="r">{_h.escape(p.role)}</span>' if p.role else ''
        aka = f'<span hidden>{_h.escape(p.aka)}</span>' if p.aka else ''
        cards.append(f'<div class="person"><b>{name}</b>{d}{r}{aka}</div>')
    legend = f' {cfg.people_legend}' if cfg.people_legend else ''
    return ('<hr><section id="people"><h2>אינדקס האנשים</h2>'
            '<p class="note">בני המשפחה המרכזיים בדוח, עם קישור אל הפרק שבו כל אחד נדון; העץ מציג את כולם. '
            'שדה החיפוש שבראש העמוד מחפש גם בכתיבים החלופיים של השמות.'
            f'{legend}</p>'
            f'<div class="people">{"".join(cards)}</div></section>')


_SEC_OR_H = re.compile(
    r'<section id="([^"]+)"|<h([3-5])\b[^>]*\sid="([^"]+)"[^>]*>(.*?)</h\2>', re.S)
_TAGS = re.compile(r'<[^>]+>')


def page_rows(body_html):
    """Search rows for everything below chapter level: sub-headings and sources.

    The chapter list alone covers nine headings out of some eighty; a reader
    searching for "ילקוט" or for a year that names a sub-section was told there
    were no results.
    """
    rows, cur = [], ''
    for m in _SEC_OR_H.finditer(body_html):
        if m.group(1):
            cur = m.group(1)
            continue
        lvl, hid, inner = m.group(2), m.group(3), m.group(4)
        text = _h.unescape(_TAGS.sub('', inner)).strip()
        if not text:
            continue
        if cur == 'report' and lvl == '3':
            rows.append({'t': text, 'h': '#' + hid, 'k': 'תת־פרק'})
        elif cur == 'index' and lvl in ('3', '4'):
            rows.append({'t': text, 'h': '#' + hid, 'k': 'מקור'})
        elif cur == 'changelog' and lvl == '3':
            rows.append({'t': text, 'h': '#' + hid, 'k': 'מהדורה'})
    return rows


def search_index(chapters, cfg, extra=()):
    items = [{'t': full, 'h': '#' + sid, 'k': 'פרק'} for sid, _s, full in chapters]
    for p in cfg.people:
        if p.anchor:
            items.append({'t': p.name + (' — ' + p.role if p.role else ''),
                          'h': p.anchor, 'k': 'אדם',
                          'x': (p.aka + ' ' + p.dates).strip()})
    for label, anchor, kind, aka in cfg.search_extra:
        items.append({'t': label, 'h': anchor, 'k': kind, 'x': aka})
    have = {it['h'] for it in items}
    items += [r for r in extra if r['h'] not in have]
    return items


_JS = """
(function(){
  var IDX = %s;
  var q = document.getElementById('q'), res = document.getElementById('qres');
  function norm(s){ return (s||'').replace(/["'\u05b0-\u05c7]/g,'').toLowerCase(); }
  function clear(){ res.textContent=''; res.hidden=true; }
  function run(){
    var v = norm(q.value.trim());
    res.textContent = '';
    if (v.length < 2){ clear(); return; }
    var out = [], i, it, hay;
    for (i=0;i<IDX.length && out.length<12;i++){
      it = IDX[i]; hay = norm(it.t + ' ' + (it.x||''));
      if (hay.indexOf(v) !== -1) out.push(it);
    }
    if (out.length){
      var head = document.createElement('p'); head.className='qcount';
      head.textContent = out.length === 1 ? 'תוצאה אחת'
                       : (out.length === 12 ? '12 התוצאות הראשונות' : out.length + ' תוצאות');
      res.appendChild(head);
      out.forEach(function(o){
        var a = document.createElement('a'); a.href = o.h; a.textContent = o.t;
        var k = document.createElement('span'); k.className='k'; k.textContent=o.k;
        // a space, or the accessible name reads "…ירושליםאדם"
        a.appendChild(document.createTextNode(' '));
        a.appendChild(k); res.appendChild(a);
      });
    } else {
      var p = document.createElement('p'); p.className='nores';
      p.textContent='לא נמצאו תוצאות בפרקים, באנשים ובמקורות. לחיפוש בגוף הטקסט: Ctrl+F';
      res.appendChild(p);
    }
    res.hidden = false;
  }
  function jump(h){
    // re-applying the hash after the list closes keeps the heading where the
    // browser put it, whatever else moved
    location.hash=''; location.hash=h;
  }
  if (q){
    q.hidden = false; clear();
    q.addEventListener('input', run);
    q.addEventListener('keydown', function(e){
      if (e.key==='Escape'){ q.value=''; clear(); return; }
      if (e.key==='ArrowDown'){ var a=res.querySelector('a'); if(a){ e.preventDefault(); a.focus(); } }
      if (e.key==='Enter'){ var f=res.querySelector('a'); if(f){ e.preventDefault(); f.click(); } }
    });
    res.addEventListener('keydown', function(e){
      var as = [].slice.call(res.querySelectorAll('a')), i = as.indexOf(document.activeElement);
      if (e.key==='ArrowDown' && i > -1 && as[i+1]){ e.preventDefault(); as[i+1].focus(); }
      if (e.key==='ArrowUp'){ e.preventDefault(); (i > 0 ? as[i-1] : q).focus(); }
      if (e.key==='Escape'){ q.value=''; clear(); q.focus(); }
    });
    res.addEventListener('click', function(e){
      var a = e.target.closest ? e.target.closest('a') : null;
      var h = a ? a.getAttribute('href') : '';
      setTimeout(function(){ clear(); q.value=''; offset(); if (h) jump(h); }, 60);
    });
  }
  var nav = document.querySelector('.nav');
  // the phone nav is one scrolling row; the search field opens from a button
  var qt = document.querySelector('.qtoggle');
  if (qt){
    qt.hidden = false;
    qt.addEventListener('click', function(){
      var on = !nav.classList.contains('qopen');
      nav.classList.toggle('qopen', on);
      qt.setAttribute('aria-expanded', on ? 'true' : 'false');
      if (on && q) q.focus(); else { if (q) q.value=''; if (res) clear(); }
      offset();
    });
  }
  function offset(){
    if (!nav) return;
    var h = Math.ceil(nav.getBoundingClientRect().height) + 14;
    document.documentElement.style.setProperty('--anchor-off', h + 'px');
  }
  offset(); addEventListener('resize', offset);
  var top = document.querySelector('.top');
  function topvis(){ var on = scrollY > 900;
    top.classList.toggle('show', on); top.setAttribute('tabindex', on ? '0' : '-1'); }
  if (top){ top.setAttribute('tabindex','-1'); addEventListener('scroll', topvis, {passive:true}); }
  // a lazy image that never entered the viewport prints as an empty frame,
  // and a fetch started inside beforeprint is not awaited — so the whole set
  // is promoted once the page has settled, and again as a backstop
  // A lazy image that never entered the viewport prints as an empty frame. But
  // promoting all of them on load would download the whole gallery for a reader
  // who never scrolls. So: promote once the reader has actually started reading,
  // and again at print time as a backstop.
  function eager(){
    [].forEach.call(document.querySelectorAll('img[loading="lazy"]'),
                    function(i){ i.loading='eager'; });
  }
  // a collapsed <details> prints as its summary alone; everything is opened for
  // the print run and put back afterwards
  var reopen = [];
  addEventListener('beforeprint', function(){
    reopen = [].filter.call(document.querySelectorAll('details'), function(d){ return !d.open; });
    reopen.forEach(function(d){ d.open = true; });
  });
  addEventListener('afterprint', function(){
    reopen.forEach(function(d){ d.open = false; }); reopen = [];
  });
  var promoted = false;
  function promoteOnce(){
    if (promoted) return;
    promoted = true;
    var idle = window.requestIdleCallback || function(f){ setTimeout(f, 600); };
    idle(eager);
  }
  addEventListener('scroll', promoteOnce, {passive:true, once:true});
  addEventListener('beforeprint', eager);
  // only a table that actually overflows is a scroll region worth a tab stop
  function scrollables(){
    [].forEach.call(document.querySelectorAll('.tablewrap'), function(w){
      var over = w.scrollWidth - w.clientWidth > 1;
      var cap = w.querySelector('caption');
      var name = 'טבלה' + (cap && cap.textContent ? ' — ' + cap.textContent : '');
      if (over){ w.tabIndex = 0; w.setAttribute('role','region');
                 w.setAttribute('aria-label', name + ' — ניתנת לגלילה אופקית'); }
      else { w.removeAttribute('tabindex'); w.removeAttribute('role');
             w.removeAttribute('aria-label'); }
    });
  }
  scrollables(); addEventListener('resize', scrollables);
  // the tree is laid out at fixed coordinates; zooming the frame is how a reader
  // gets its labels to a readable size without the boxes colliding
  // zoom 1 is "fit to width": the diagram is laid out at the frame's own width,
  // so the reader always has a state where the whole shape is on the screen,
  // and every step above it is stated relative to that (×1.5, ×2)
  var zoom = 1; // start at fit-to-width everywhere; readers zoom in with +
  var zval = document.getElementById('tree-zoom-val');
  function zshow(){
    document.documentElement.style.setProperty('--tree-zoom', zoom);
    if (zval) zval.textContent = '\\u00d7' + (Math.round(zoom * 100) / 100);
  }
  [].forEach.call(document.querySelectorAll('[data-tree-zoom]'), function(btn){
    btn.addEventListener('click', function(){
      var v = btn.getAttribute('data-tree-zoom');
      if (v === 'fit') zoom = 1;
      else zoom = Math.min(3, Math.max(1,
             Math.round((zoom + parseInt(v, 10) * 0.25) * 100) / 100));
      zshow();
    });
  });
  if (zval) zshow();
  var links = [].slice.call(document.querySelectorAll('.nav-row a[href^="#"]'));
  var targets = links.map(function(a){ return document.getElementById(a.getAttribute('href').slice(1)); });
  if ('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (!e.isIntersecting) return;
        var i = targets.indexOf(e.target);
        if (i < 0) return;
        links.forEach(function(a){ a.classList.remove('on'); });
        links[i].classList.add('on');
      });
    }, {rootMargin:'-20%% 0px -70%% 0px'});
    targets.forEach(function(t){ if (t) io.observe(t); });
  }
})();
"""


def page(cfg, edition, stamp, body_sections, chapters, present, extra_rows=(),
         story_href=''):
    idx = json.dumps(search_index(chapters, cfg, extra_rows), ensure_ascii=False)\
             .replace('</', '<\\/')
    js = _JS % idx
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_h.escape(cfg.title)}</title>
<meta name="description" content="{_h.escape(cfg.meta_description)}">
<meta name="color-scheme" content="light">
<style>{theme.css(cfg.palette)}</style>
</head>
<body>
<a class="skip" href="#report">דילוג לתוכן</a>
<a class="top" href="#top" aria-label="חזרה לראש העמוד" tabindex="-1">↑</a>
<span id="top"></span>
{hero(cfg, edition, stamp)}
{nav(present, chapters, story_href)}
<main>
{body_sections}
</main>
<footer>{cfg.footer_note}</footer>
<script>{js}</script>
</body>
</html>
"""


def index_stub(main_html, title):
    q = urllib.parse.quote(main_html)
    return (f'<!DOCTYPE html>\n<html lang="he" dir="rtl">\n<head>\n<meta charset="UTF-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<meta http-equiv="refresh" content="0; url={q}">\n<title>{_h.escape(title)}</title>\n'
            f'</head>\n<body style="font-family:Georgia,serif;background:#faf7f2;color:#2b2620;'
            f'text-align:center;padding-top:80px;">\n'
            f'<p>מעביר אל <a href="{q}">{_h.escape(main_html)}</a>…</p>\n'
            f'<script>location.replace("{q}");</script>\n</body>\n</html>\n')
