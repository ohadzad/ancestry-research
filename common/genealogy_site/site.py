# -*- coding: utf-8 -*-
"""The publishable mirror under site/."""
import os
import re
import shutil

# never published: build scratch, editor droppings, the mirror itself
SKIP = ('site', '__pycache__', '.DS_Store', 'Thumbs.db', 'thumbs.db', '*.pyc')


def mirror(cfg, files, ignore=SKIP):
    out = cfg.p('site')
    if os.path.isdir(out):
        shutil.rmtree(out)          # a real failure here must not pass silently
    os.makedirs(out, exist_ok=True)
    docs = cfg.p('docs')
    if os.path.isdir(docs):
        pats = tuple(ignore) + tuple(cfg.privacy_file_patterns)
        shutil.copytree(docs, os.path.join(out, 'docs'), dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(*pats))
    for f in files:
        src = cfg.p(f)
        if os.path.exists(src):
            dst = os.path.join(out, f)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
    open(os.path.join(out, '.nojekyll'), 'w').close()
    return out


def sweep_thumbs(cfg, html):
    """Delete cached thumbnails no page that references this project still uses."""
    d = cfg.p('docs', 'thumbs')
    if not os.path.isdir(d):
        return []
    sources = [html]
    for ref in cfg.thumb_referrers:
        path = cfg.p(ref)
        if os.path.exists(path):
            sources.append(open(path, encoding='utf-8').read())
    keep = set()
    for text in sources:
        keep |= set(re.findall(r'["\'][^"\']*docs/thumbs/([^"\']+)["\']', text))
    gone = []
    for name in sorted(os.listdir(d)):
        if name not in keep:
            os.remove(os.path.join(d, name))
            gone.append(name)
    return gone
