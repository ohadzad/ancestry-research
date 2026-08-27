# -*- coding: utf-8 -*-
"""The page shell: hero, sticky navigation, in-page search, person index, footer."""
import html as _h
import json
import re
import urllib.parse

from . import theme

SECTIONS = [
    ('report', 'הדוח'),
    ('tree', 'עץ המשפחה'),
    ('gallery', 'מסמכי מפתח'),
    ('people', 'אינדקס אנשים'),
    ('index', 'אינדקס מקורות'),
    ('changelog', 'יומן מהדורות'),
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
    meta = ' · '.join(x for x in [edition, f'נבנה {stamp}'] if x)
    return (f'<header class="hero"><div class="hero-in">{crumb}'
            f'<h1>{_h.escape(cfg.title)}</h1>'
            f'<p class="subject">{cfg.subject}</p>'
            f'<div class="meta">{meta}</div>{spine}</div></header>')


def nav(present, chapters):
    secs = ''.join(f'<a href="#{sid}">{label}</a>'
                   for sid, label in SECTIONS if sid in present)
    chs = ''.join(f'<a href="#{sid}" title="{_h.escape(full)}">{_h.escape(short)}</a>'
                  for sid, short, full in chapters)
    # the results list sits directly after the input (tab order) but is
    # positioned out of flow (so showing it never changes the nav's height)
    return (
        '<nav class="nav" aria-label="ניווט ראשי"><div class="nav-in">'
        f'<div class="nav-row"><span class="lbl">מקטעים</span>{secs}'
        '<div class="qwrap">'
        '<input id="q" type="search" placeholder="חיפוש בעמוד…" '
        'aria-label="חיפוש בפרקים ובאינדקס האנשים" autocomplete="off" '
        'role="combobox" aria-autocomplete="list" aria-controls="qres" '
        'aria-expanded="false" hidden>'
        '<div id="qres" role="region" aria-label="תוצאות החיפוש" aria-live="polite" hidden></div>'
        '</div></div>'
        f'<details class="chapters-wrap" open><summary class="lbl">פרקים</summary>'
        f'<div class="nav-row chapters">{chs}</div></details>'
        '</div></nav>')


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
    return ('<hr><section id="people"><h2>אינדקס האנשים</h2>'
            '<p class="note">כל אדם שהדוח מתעד, עם קישור אל הפרק שבו הוא נדון. '
            'שדה החיפוש שבראש העמוד מחפש גם בכתיבים החלופיים של השמות.</p>'
            f'<div class="people">{"".join(cards)}</div></section>')


def search_index(chapters, cfg):
    items = [{'t': full, 'h': '#' + sid, 'k': 'פרק'} for sid, _s, full in chapters]
    for p in cfg.people:
        if p.anchor:
            items.append({'t': p.name + (' — ' + p.role if p.role else ''),
                          'h': p.anchor, 'k': 'אדם',
                          'x': (p.aka + ' ' + p.dates).strip()})
    for label, anchor, kind, aka in cfg.search_extra:
        items.append({'t': label, 'h': anchor, 'k': kind, 'x': aka})
    return items


_JS = """
(function(){
  var IDX = %s;
  var q = document.getElementById('q'), res = document.getElementById('qres');
  function norm(s){ return (s||'').replace(/["'\u05b0-\u05c7]/g,'').toLowerCase(); }
  function clear(){ res.textContent=''; res.hidden=true; if(q) q.setAttribute('aria-expanded','false'); }
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
      out.forEach(function(o){
        var a = document.createElement('a'); a.href = o.h; a.textContent = o.t;
        var k = document.createElement('span'); k.className='k'; k.textContent=o.k;
        a.appendChild(k); res.appendChild(a);
      });
    } else {
      var p = document.createElement('p'); p.className='nores';
      p.textContent='לא נמצאו תוצאות בכותרות ובאינדקס האנשים. לחיפוש בגוף הטקסט: Ctrl+F';
      res.appendChild(p);
    }
    res.hidden = false; q.setAttribute('aria-expanded','true');
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
  function offset(){
    if (!nav) return;
    var h = Math.ceil(nav.getBoundingClientRect().height) + 14;
    document.documentElement.style.setProperty('--anchor-off', h + 'px');
  }
  var det = document.querySelector('.chapters-wrap');
  // on a phone the open chapter strip costs a quarter of the viewport
  if (det && matchMedia('(max-width:40rem)').matches) det.removeAttribute('open');
  offset(); addEventListener('resize', offset);
  if (det) det.addEventListener('toggle', offset);
  var top = document.querySelector('.top');
  function topvis(){ var on = scrollY > 900;
    top.classList.toggle('show', on); top.setAttribute('tabindex', on ? '0' : '-1'); }
  if (top){ top.setAttribute('tabindex','-1'); addEventListener('scroll', topvis, {passive:true}); }
  // a lazy image that never entered the viewport prints as an empty frame,
  // and a fetch started inside beforeprint is not awaited — so the whole set
  // is promoted once the page has settled, and again as a backstop
  function eager(){
    [].forEach.call(document.querySelectorAll('img[loading="lazy"]'),
                    function(i){ i.loading='eager'; });
  }
  addEventListener('load', function(){ setTimeout(eager, 1200); });
  addEventListener('beforeprint', eager);
  // only a table that actually overflows is a scroll region worth a tab stop
  function scrollables(){
    [].forEach.call(document.querySelectorAll('.tablewrap'), function(w){
      var over = w.scrollWidth - w.clientWidth > 1;
      if (over){ w.tabIndex = 0; w.setAttribute('role','region');
                 w.setAttribute('aria-label','טבלה — ניתנת לגלילה אופקית'); }
      else { w.removeAttribute('tabindex'); w.removeAttribute('role');
             w.removeAttribute('aria-label'); }
    });
  }
  scrollables(); addEventListener('resize', scrollables);
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


def page(cfg, edition, stamp, body_sections, chapters, present):
    idx = json.dumps(search_index(chapters, cfg), ensure_ascii=False)\
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
<a class="top" href="#top" aria-label="חזרה לראש העמוד" tabindex="-1">↑</a>
<span id="top"></span>
{hero(cfg, edition, stamp)}
{nav(present, chapters)}
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
