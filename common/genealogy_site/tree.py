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


def embed(cfg, svg, legend, foot=''):
    if not svg:
        return ''
    btn = ''
    if cfg.tree and cfg.tree.page_href:
        btn = (f'<a class="btn" href="{cfg.tree.page_href}" target="_blank" '
               f'rel="noopener">פתיחת העץ בעמוד נפרד ↗</a>')
    if '<title' not in svg[:400]:
        svg = re.sub(r'(<svg\b[^>]*>)',
                     r'\1<title>עץ המשפחה — התרשים המלא; פירוט מילולי באינדקס האנשים</title>',
                     svg, count=1)
    svg = re.sub(r'<svg\b(?![^>]*\brole=)', '<svg role="img"', svg, count=1)
    zoom = ('<div class="tree-zoom">'
            '<span id="tree-zoom-label">הגדלת העץ</span>'
            '<button type="button" data-tree-zoom="-1" aria-label="הקטנה">−</button>'
            '<output id="tree-zoom-val">100%</output>'
            '<button type="button" data-tree-zoom="1" aria-label="הגדלה">+</button>'
            '</div>')
    return (f'<div class="tree-embed" role="group" aria-label="עץ המשפחה" tabindex="0">{svg}</div>'
            f'{zoom}{legend}{foot}'
            f'<p class="tree-hint">גלילה אופקית בתוך המסגרת מציגה את העץ במלואו, '
            f'וכפתורי ההגדלה שמעליה מגדילים את הכתב; בהדפסה הוא מקבל עמוד לרוחב משלו.</p>{btn}')
