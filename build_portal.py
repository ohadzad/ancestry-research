#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the archive portal (index.html at the repo root) from research_registry.json.

Adding a research = adding an entry to research_registry.json and re-running this.
Run from the repository root, with the project venv:
  ~/.venvs/ancestry-research/bin/python build_portal.py
"""
import json, os, sys, html, re, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

reg = json.load(open('research_registry.json', encoding='utf-8'))
site = reg['site']
researches = reg['researches']

e = lambda s: html.escape(s or '', quote=True)

try:
    from PIL import Image as _Image
except Exception:                                    # pragma: no cover
    _Image = None


def dims(path):
    """Intrinsic width/height, so a cover cannot shift the card while it loads."""
    if _Image is None:
        return ''
    try:
        with _Image.open(urllib.parse.unquote(path)) as im:
            return ' width="%d" height="%d"' % (im.width, im.height)
    except Exception:
        return ''


CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0; font-family:Georgia,"Times New Roman","Frank Ruehl CLM",serif;
     background:#faf7f2; color:#2b2620; line-height:1.75;}
a{color:#7a4a2b; text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:1000px; margin:0 auto; padding:0 20px 80px}
header.top{border-bottom:1px solid #d8d0c2; background:#f2ede4;}
header.top .wrap{padding-top:46px; padding-bottom:34px}
h1{font-size:2.35rem; margin:0 0 6px; letter-spacing:-.01em}
.surnames{color:#6f675b; font-size:1rem; letter-spacing:.06em; margin:0 0 18px}
.intro{max-width:66ch; margin:0; font-size:1.03rem; color:#4a4238}
.note{max-width:66ch; margin:14px 0 0; font-size:.9rem; color:#6f675b}
h2.sec{font-size:1.02rem; letter-spacing:.14em; color:#6f675b; font-weight:normal;
       margin:52px 0 18px; padding-bottom:8px; border-bottom:1px solid #e3dbcd}

.card{display:grid; grid-template-columns:150px 1fr; gap:26px; background:#fff;
      border:1px solid #d8d0c2; border-radius:12px; padding:24px 26px;
      box-shadow:0 2px 10px rgba(0,0,0,.05)}
.card + .card{margin-top:22px}
.cover img{width:100%; display:block; border:1px solid #d8d0c2; border-radius:6px; background:#f7f3ec}
.cover figcaption{font-size:.72rem; color:#6f675b; line-height:1.5; margin-top:7px}
.badge{display:inline-block; font-size:.72rem; letter-spacing:.09em; border-radius:999px;
       padding:3px 11px; border:1px solid #b9a98c; color:#7a6a4c; background:#fbf6ea;
       vertical-align:middle; margin-inline-start:10px}
.card h3{margin:0 0 2px; font-size:1.5rem}
.card h3 .aka{color:#6f675b; font-weight:normal}
.life{margin:0 0 4px; color:#5a5142; font-size:.95rem}
.edition{margin:0 0 14px; color:#6f675b; font-size:.82rem}
.summary{margin:0 0 18px; color:#3c352c}
.stats{display:flex; flex-wrap:wrap; gap:26px; margin:0 0 20px; padding:14px 0;
       border-top:1px solid #eee6d8; border-bottom:1px solid #eee6d8}
.stats div{min-width:78px}
.stats b{display:block; font-size:1.4rem; line-height:1.2; color:#7a4a2b; font-weight:normal}
.stats span{font-size:.76rem; color:#6f675b}
.links{display:flex; flex-wrap:wrap; gap:9px; margin:0}
.skip{position:absolute; inset-inline-start:-9999px; top:0; z-index:99;
  background:#fdfaf5; color:#5a3a1e; padding:10px 16px; border:1px solid #7a4a2b;
  border-radius:0 0 8px 0; font-family:system-ui,sans-serif; font-size:14px}
.skip:focus{inset-inline-start:0}
.btn{display:inline-block; border:1px solid #cfc4b0; border-radius:8px; padding:7px 15px;
     font-size:.9rem; background:#fbf8f2; color:#5a4632}
.btn:hover{background:#f2ebdd; text-decoration:none}
.btn.primary{background:#7a4a2b; border-color:#7a4a2b; color:#fdfaf5}
.btn.primary:hover{background:#683e23}

.people{display:grid; grid-template-columns:repeat(auto-fill,minmax(268px,1fr)); gap:12px}
.person{display:block; background:#fff; border:1px solid #e0d8ca; border-radius:10px;
        padding:13px 16px; color:inherit}
.person:hover{border-color:#b9a98c; background:#fffdf8; text-decoration:none}
.person .pn{font-size:1.02rem; color:#2b2620}
.person .pd{font-size:.8rem; color:#6f675b; margin-top:1px}
.person .pd bdi{unicode-bidi:isolate}
.person .ps{font-size:.86rem; color:#5a5142; margin-top:5px; line-height:1.55}

.method{background:#f5f1e8; border:1px solid #e3dbcd; border-radius:10px; padding:18px 22px;
        font-size:.93rem; color:#4a4238; max-width:78ch}
.method ul{margin:10px 0 0; padding-inline-start:20px}
.method li{margin:5px 0}
footer{margin-top:60px; padding-top:22px; border-top:1px solid #e3dbcd;
       font-size:.83rem; color:#6f675b}
nav.toc{margin:26px 0 0; font-size:.9rem}
nav.toc ul{list-style:none; margin:0; padding:0; display:flex; flex-wrap:wrap; gap:8px 14px}
nav.toc a{border-bottom:1px solid #e3dbcd; padding-bottom:2px}
@media (max-width:640px){
  .card{grid-template-columns:1fr; gap:18px}
  /* a 132px frame inside a 350px card left the cover a strip in a white field */
  .cover{width:100%}
  h1{font-size:1.85rem}
}
"""

def card(r):
    p = []
    p.append('<article class="card" id="research-%s">' % e(r['slug']))
    if r.get('cover'):
        img = ('<img src="%s" alt="%s" loading="lazy"%s>'
               % (e(r['cover']), e(r.get('cover_alt','')), dims(r['cover'])))
        if r.get('cover_href'):
            img = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (e(r['cover_href']), img)
        p.append('<figure class="cover" style="margin:0">%s<figcaption>%s</figcaption></figure>'
                 % (img, e(r.get('cover_alt',''))))
    else:
        p.append('<div class="cover"></div>')
    p.append('<div>')
    aka = (' <span class="aka">%s</span>' % e(r['aka'])) if r.get('aka') else ''
    badge = ('<span class="badge">%s</span>' % e(r['state_label'])) if r.get('state_label') else ''
    # the badge sits outside the heading text: a screen reader announcing the
    # heading should say the person's name, not the project's status label
    p.append('<h3>%s%s</h3>%s' % (e(r['name']), aka, badge))
    if r.get('life'):    p.append('<p class="life">%s</p>' % e(r['life']))
    if r.get('edition'): p.append('<p class="edition">%s</p>' % e(r['edition']))
    if r.get('summary'): p.append('<p class="summary">%s</p>' % e(r['summary']))
    if r.get('stats'):
        p.append('<div class="stats">' + ''.join(
            '<div><b>%s</b><span>%s</span></div>' % (e(s['n']), e(s['l'])) for s in r['stats']) + '</div>')
    if r.get('links'):
        p.append('<p class="links">' + ''.join(
            '<a class="btn%s" href="%s">%s</a>' % (' primary' if l.get('primary') else '', e(l['href']), e(l['label']))
            for l in r['links']) + '</p>')
    p.append('</div></article>')
    return '\n'.join(p)

RANGE_RE = re.compile(r'^[\d\s\u2013\u2014/?.\-]+$')

def dates(txt):
    """A pure numeric range must be isolated as LTR, or bidi flips it
    ('1929 – 2021' would render as '2021 – 1929' inside an RTL block)."""
    txt = txt or ''
    if txt and RANGE_RE.match(txt):
        return '<bdi dir="ltr">%s</bdi>' % e(txt)
    return e(txt)

def people_grid(r):
    if not r.get('people'): return ''
    items = ''.join(
        '<a class="person" href="%s"><span class="pn">%s</span>'
        '<div class="pd">%s</div><div class="ps">%s</div></a>'
        % (e(q['h']), e(q['n']), dates(q.get('d','')), e(q.get('s','')))
        for q in r['people'])
    return ('<h2 class="sec" id="people-%s">אנשים בארכיון — %s</h2>\n<div class="people">%s</div>'
            % (e(r['slug']), e(r['name']), items))


def toc(researches):
    """The portal is 4,600px tall; without this the only way down is scrolling."""
    li = []
    for r in researches:
        li.append('<li><a href="#research-%s">%s</a></li>' % (e(r['slug']), e(r['name'])))
    for r in researches:
        if r.get('people'):
            li.append('<li><a href="#people-%s">אנשים — %s</a></li>'
                      % (e(r['slug']), e(r['name'])))
    li.append('<li><a href="#method">איך הארכיון הזה בנוי</a></li>')
    return ('<nav class="toc" aria-label="מחקרים"><ul>%s</ul></nav>' % ''.join(li))

body = []
body.append('<a class="skip" href="#main">דילוג לתוכן</a>')
body.append('<header class="top"><div class="wrap">')
body.append('<h1>%s</h1>' % e(site['title']))
body.append('<p class="surnames">%s</p>' % e(site['surnames']))
body.append('<p class="intro">%s</p>' % e(site['intro']))
if site.get('note'): body.append('<p class="note">%s</p>' % e(site['note']))
body.append(toc(researches))
body.append('</div></header>')
body.append('<main id="main"><div class="wrap">')
body.append('<h2 class="sec" id="researches">מחקרים</h2>')
for r in researches:
    body.append(card(r))
for r in researches:
    body.append(people_grid(r))
body.append('<h2 class="sec" id="method">איך הארכיון הזה בנוי</h2>')
body.append("""<div class="method">
כל מחקר כאן נבנה לפי אותה שיטה, וכל קביעה שבו ניתנת לבדיקה עצמאית:
<ul>
<li><b>מקור כפול לכל עובדה</b> — קישור אל הרשומה בארכיון המקורי, וקישור אל עותק שמור שלה כאן.</li>
<li><b>הראיה היא המסמך עצמו</b> — כל תצלום בגלריה הוא חיתוך מן העמוד המקורי, ולחיצה עליו פותחת את הקובץ המלא.</li>
<li><b>סולם ודאות אחיד</b> — מאומת · כמעט ודאי · ככל הנראה · טעון אימות · נשלל. מה שלא אומת נאמר במפורש.</li>
<li><b>ציטוט בשפת המקור מלווה בתרגום</b> — הונגרית, גרמנית, צ׳כית ואנגלית מתורגמות במקום.</li>
<li><b>גם ממצא שלילי נרשם</b> — היעדר מתועד ברשומה הוא בעצמו מידע.</li>
</ul>
</div>""")
body.append('</div></main>')
body.append('<footer>ארכיון מחקר משפחתי. המסמכים שמורים לצד הדוחות, כדי שהמחקר יישאר בר־אימות גם בלי חיבור לארכיונים המקוונים.</footer>')

out = ('<!DOCTYPE html>\n<html lang="he" dir="rtl">\n<head>\n'
       '<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
       '<title>' + e(site['title']) + '</title>\n'
       '<meta name="description" content="' + e(site['intro'][:160]) + '">\n'
       '<style>' + CSS + '</style>\n</head>\n<body>\n' + '\n'.join(body) + '\n</body>\n</html>\n')

open('index.html', 'w', encoding='utf-8').write(out)
print('portal written: index.html, %d KB' % (len(out) // 1024))

# ---- link check: every relative target must exist on disk ----
targets = set(re.findall(r'(?:href|src)="(?!https?:|#|mailto:|data:)([^"]+)"', out))
missing = []
for t in sorted(targets):
    path = urllib.parse.unquote(t.split('#')[0])
    if not path:
        continue
    if path.endswith('/'):
        path = path + 'index.html'
    if not os.path.exists(path):
        missing.append(t)
if missing:
    print('BROKEN LOCAL TARGETS:')
    for m in missing:
        print('  -', m)
    sys.exit(1)
print('link check: all %d relative targets exist' % len(targets))
