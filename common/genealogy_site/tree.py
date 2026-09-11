# -*- coding: utf-8 -*-
"""The family-tree embed."""
import os
import re

_SVG = re.compile(r'(<svg.*?</svg>)', re.S)
_LEGEND = re.compile(r'(<div class="legend">.*?</div>)', re.S)
_FOOT = re.compile(r'<div class="foot">(.*?)</div>', re.S)


KINDS = ('html_extract', 'svg_file')


def load(cfg, warn=None):
    """Return (svg, legend_html, foot_html) from whichever source the project declares."""
    if cfg.tree is None:
        return '', '', ''
    if cfg.tree.kind not in KINDS:
        raise ValueError(f'TreeSource.kind לא מוכר: {cfg.tree.kind!r}')
    path = cfg.p(cfg.tree.path)
    if not os.path.exists(path):
        if warn:
            warn(f'קובץ העץ שהוצהר אינו קיים: {cfg.tree.path}')
        return '', '', ''
    raw = open(path, encoding='utf-8').read()
    if cfg.tree.kind == 'svg_file':
        return raw, '', ''
    m = _SVG.search(raw)
    svg = m.group(1) if m else ''
    lg = _LEGEND.search(raw)
    ft = _FOOT.search(raw)
    foot = f'<p class="tree-foot">{ft.group(1).strip()}</p>' if ft else ''
    return svg, (lg.group(1) if lg else ''), foot


_ID = re.compile(r'\sid="([^"]+)"')


def strip_ids(svg):
    """Remove ids from an SVG copy so duplicated markup cannot clash."""
    return _ID.sub('', svg)


_WRAP = re.compile(r'<div class="(?:wrap|chart)"[^>]*>')

# the standalone page is a project file the engine must not rewrite in place;
# what it publishes is a generated copy with the same scroll-and-zoom frame the
# report's embed has. Without it the diagram is scaled to 46% on a phone and the
# 12px sub-labels are read at ~5.5px.
_VIEW_CSS = """
:root{--tree-zoom:1}
.wrap,.chart{overflow:auto; -webkit-overflow-scrolling:touch}
.wrap>svg,.chart>svg{width:calc(100% * var(--tree-zoom,1));
  min-width:min(100%, calc(48rem * var(--tree-zoom,1)));
  max-width:none; height:auto; display:block; margin:0 auto}
.tree-zoom{display:flex; gap:.4rem; align-items:center; justify-content:center;
  font-family:'Assistant','Segoe UI',Arial,sans-serif; font-size:.82rem;
  color:#5e6b73; padding:6px 12px 0}
.tree-zoom button{font:inherit; line-height:1; min-width:2rem; min-height:2rem;
  border:1px solid #dbe0d8; border-radius:6px; background:#fff; color:#1e2a32; cursor:pointer}
.tree-zoom button:hover{background:rgba(0,0,0,.04)}
@media (max-width:40rem){
  :root{--tree-zoom:1.6}
  .wrap,.chart{max-height:78vh}
}
@media print{ .tree-zoom{display:none}
  .wrap>svg,.chart>svg{width:auto; min-width:0; max-width:100%} }
"""

_VIEW_JS = """
(function(){
  var z = parseFloat(getComputedStyle(document.documentElement)
            .getPropertyValue('--tree-zoom')) || 1;
  var out = document.getElementById('tz-val');
  function show(){ document.documentElement.style.setProperty('--tree-zoom', z);
    if (out) out.textContent = '\\u00d7' + (Math.round(z*100)/100); }
  [].forEach.call(document.querySelectorAll('[data-tz]'), function(b){
    b.addEventListener('click', function(){
      var v = b.getAttribute('data-tz');
      z = (v === 'fit') ? 1 : Math.min(4, Math.max(1, Math.round((z + parseFloat(v)*0.25)*100)/100));
      show();
    });
  });
  show();
})();
"""

_VIEW_BAR = ('<div class="tree-zoom">'
             '<span>הגדלה</span>'
             '<button type="button" data-tz="-1" aria-label="הקטנה">−</button>'
             '<output id="tz-val">×1</output>'
             '<button type="button" data-tz="1" aria-label="הגדלה">+</button>'
             '<button type="button" data-tz="fit">התאמה לרוחב</button>'
             '</div>')


def standalone(cfg, warn=None):
    """Publish a zoomable copy of the project's standalone tree page.

    Returns the generated file name relative to the project root, or '' when
    there is nothing to generate. The project's own page is left untouched.
    """
    href = cfg.tree.page_href if cfg.tree else None
    if not href or not href.lower().endswith('.html'):
        return '', ''
    src = cfg.p(href)
    if not os.path.exists(src):
        return '', ''
    raw = open(src, encoding='utf-8').read()
    if not _WRAP.search(raw):
        if warn:
            warn(f'עמוד העץ העצמאי בלי מיכל תרשים מוכר; לא נוצרה גרסה מתכווננת: {href}')
        return '', ''

    def wrap(m):
        tag = m.group(0)
        if 'tabindex' not in tag:
            tag = tag[:-1] + ' tabindex="0" role="group" aria-label="עץ המשפחה">'
        return _VIEW_BAR + tag

    html = raw.replace('</head>', f'<style>{_VIEW_CSS}</style></head>', 1)
    html = _WRAP.sub(wrap, html, count=1)
    html = html.replace('</body>', f'<script>{_VIEW_JS}</script></body>', 1)
    return html, href[:-5] + '-view.html'


def embed(cfg, svg, legend, foot='', page_href=None):
    if not svg:
        return ''
    btn = ''
    href = page_href or (cfg.tree.page_href if cfg.tree else '')
    if href:
        btn = (f'<a class="btn" href="{href}" target="_blank" '
               f'rel="noopener">פתיחת העץ בעמוד נפרד ↗</a>')
    if '<title' not in svg[:400]:
        svg = re.sub(r'(<svg\b[^>]*>)',
                     r'\1<title>עץ המשפחה — התרשים המלא; פירוט מילולי באינדקס האנשים</title>',
                     svg, count=1)
    svg = re.sub(r'<svg\b(?![^>]*\brole=)', '<svg role="img"', svg, count=1)
    zoom = ('<div class="tree-zoom">'
            '<span id="tree-zoom-label">הגדלה</span>'
            '<button type="button" data-tree-zoom="-1" aria-label="הקטנה">−</button>'
            '<output id="tree-zoom-val" aria-labelledby="tree-zoom-label">×1</output>'
            '<button type="button" data-tree-zoom="1" aria-label="הגדלה">+</button>'
            '<button type="button" data-tree-zoom="fit">התאמה לרוחב</button>'
            '</div>')
    return (f'<div class="tree-embed" role="group" aria-label="עץ המשפחה" tabindex="0">{svg}</div>'
            f'{zoom}{legend}{foot}'
            f'<p class="tree-hint">גלילה אופקית בתוך המסגרת מציגה את העץ במלואו, '
            f'וכפתורי ההגדלה שמעליה מגדילים את הכתב; בהדפסה הוא מקבל עמוד לרוחב משלו.</p>{btn}')
