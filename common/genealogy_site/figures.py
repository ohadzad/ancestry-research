# -*- coding: utf-8 -*-
"""Evidence figures: thumbnails, intrinsic sizes, placement in the prose."""
import hashlib
import html as _h
import os
import re

try:
    from PIL import Image as _Image
except Exception:                                   # pragma: no cover
    _Image = None


def thumb(root, path, width=340, quality=78):
    """Cache a small JPEG under docs/thumbs/ and return its relative path.

    Falls back to the original path when Pillow is unavailable.
    """
    if _Image is None:
        return path
    out_dir = os.path.join(root, 'docs', 'thumbs')
    os.makedirs(out_dir, exist_ok=True)
    src_abs = os.path.join(root, path)
    base = os.path.splitext(os.path.basename(path))[0]
    try:
        sig = hashlib.md5(f'{path}:{os.path.getmtime(src_abs)}'.encode()).hexdigest()[:6]
    except OSError:
        sig = hashlib.md5(path.encode()).hexdigest()[:6]
    rel = f'docs/thumbs/{base}_{width}_{sig}.jpg'
    out = os.path.join(root, rel)
    if not os.path.exists(out):
        im = _Image.open(src_abs)
        r = width / im.width
        im = im.resize((width, max(1, int(im.height * r))), _Image.LANCZOS).convert('RGB')
        im.save(out, 'JPEG', quality=quality)
    return rel


def dims(root, path):
    """Intrinsic width/height attributes, so the page does not shift while loading."""
    if _Image is None:
        return ''
    try:
        with _Image.open(os.path.join(root, path)) as im:
            return f' width="{im.width}" height="{im.height}"'
    except Exception:
        return ''


def figure(root, src, caption, local=None, online=None, alt=None, max_w=None):
    """One evidence figure: a crop that clicks through to the full original."""
    target = local or online or src
    links = []
    if local:
        links.append(f'<a href="{local}">המסמך המלא (בתיקייה)</a>')
    if online:
        links.append(f'<a href="{online}" target="_blank" rel="noopener">המקור המקוון ↗</a>')
    tail = f'<span class="figlinks">{" · ".join(links)}</span>' if links else ''
    style = f' style="max-width:{max_w}px"' if max_w else ''
    a = _h.escape(alt if alt is not None else re.sub(r'<[^>]+>', '', caption)[:120], quote=True)
    return (f'<figure{style}><a href="{target}">'
            f'<img src="{src}" alt="{a}" loading="lazy" decoding="async"{dims(root, src)}></a>'
            f'<figcaption>{caption}{tail}</figcaption></figure>')


def _aspect(root, path):
    """Width/height of the file, or None when it cannot be measured."""
    if _Image is None or root is None:
        return None
    try:
        with _Image.open(os.path.join(root, path)) as im:
            return im.width / im.height if im.height else None
    except Exception:
        return None


def gallery(items, root=None):
    """A scannable strip of key documents."""
    if not items:
        return ''
    out = ['<div class="gallery">']
    for src, href, cap in items:
        wh = dims(root, src) if root else ''
        cap_a = _h.escape(cap, quote=True)
        # a strip crop is far wider than the frame; cropping it to fill would
        # magnify it beyond its own resolution, so it is shown whole instead
        ar = _aspect(root, src)
        cls = ' class="contain"' if ar and ar > 2.4 else ''
        out.append(f'<a href="{href}"><img{cls} src="{src}" alt="{cap_a}" loading="lazy" '
                   f'decoding="async"{wh}><span>{cap}</span></a>')
    out.append('</div>')
    return ''.join(out)


def inject_after(html, anchor_regex, insert, on_missing=None):
    """Place a figure just after the paragraph or list item that argues for it."""
    m = re.search(anchor_regex, html)
    if not m:
        if on_missing:
            on_missing(anchor_regex)
        return html
    p = html.find('</p>', m.end())
    li = html.find('</li>', m.end())
    # after </p>, but *before* </li>: a <figure> is not a valid child of a list
    cands = [(i, l) for i, l in ((p, 4), (li, 0)) if i != -1]
    pos = (min(cands)[0] + min(cands)[1]) if cands else m.end()
    return html[:pos] + insert + html[pos:]
