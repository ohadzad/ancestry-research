#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the archive portal (index.html) and the person index (people.html).

Adding a research = adding an entry to research_registry.json and re-running this.
Run from the repository root, with the project venv:
  ~/.venvs/ancestry-research/bin/python build_portal.py

The portal's job is to say, in one screen, who these people are and how they are
related — not to explain the method. A first-time reader could not tell from the
old page that Rachel and Avraham were a couple, or that Miriam and Mordechai
were; that is now the first thing the page shows.
"""
import json, os, sys, html, re, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

reg = json.load(open('research_registry.json', encoding='utf-8'))
site = reg['site']
researches = reg['researches']
BY_SLUG = {r['slug']: r for r in researches}

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


def front(r):
    """Where a reader should land: the story when there is one, else the report."""
    return r.get('story_href') or r.get('report_href') or r['links'][0]['href']


CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0; font-family:Georgia,"Times New Roman","Frank Ruehl CLM",serif;
     background:#faf7f2; color:#2b2620; line-height:1.75;}
a{color:#7a4a2b; text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:1000px; margin:0 auto; padding:0 20px 80px}
header.top{border-bottom:1px solid #d8d0c2; background:#f2ede4;}
header.top .wrap{padding-top:40px; padding-bottom:30px}
h1{font-size:2.35rem; margin:0 0 10px; letter-spacing:-.01em}
.lede{max-width:66ch; margin:0 0 26px; font-size:1.06rem; color:#4a4238}
.crumb{font-size:.86rem; color:#6f675b; margin:0 0 14px}
h2.sec{font-size:1.02rem; letter-spacing:.14em; color:#6f675b; font-weight:normal;
       margin:52px 0 18px; padding-bottom:8px; border-bottom:1px solid #e3dbcd}

/* the family map: two couples, four faces, four links */
.couples{display:flex; flex-wrap:wrap; gap:16px}
.couple{flex:1 1 340px; background:#fff; border:1px solid #d8d0c2; border-radius:12px;
        padding:12px 14px 14px}
.couple-label{display:block; font-size:.76rem; letter-spacing:.1em; color:#6f675b;
              margin-bottom:10px}
.pair{display:grid; grid-template-columns:1fr 1fr; gap:10px}
.who{display:block; color:inherit; border-radius:8px; padding:8px; border:1px solid transparent}
.who:hover{background:#fdfaf3; border-color:#e3dbcd; text-decoration:none}
.who img{width:100%; height:auto; aspect-ratio:1/1; object-fit:cover;
         object-position:center top;
         border:1px solid #d8d0c2; border-radius:6px; background:#f7f3ec; display:block}
.who .wn{display:block; font-size:1.02rem; margin-top:8px; line-height:1.35}
.who .wd{display:block; font-size:.8rem; color:#6f675b; line-height:1.45; margin-top:3px}
.who .wgo{display:block; font-size:.78rem; color:#7a4a2b; margin-top:5px}

.card{display:grid; grid-template-columns:150px 1fr; gap:26px; background:#fff;
      border:1px solid #d8d0c2; border-radius:12px; padding:22px 26px;
      box-shadow:0 2px 10px rgba(0,0,0,.05)}
.card + .card{margin-top:18px}
.cover img{width:100%; display:block; border:1px solid #d8d0c2; border-radius:6px; background:#f7f3ec}
.cover figcaption{font-size:.72rem; color:#6f675b; line-height:1.5; margin-top:7px}
.badge{display:inline-block; font-size:.72rem; letter-spacing:.09em; border-radius:999px;
       padding:3px 11px; border:1px solid #b9a98c; color:#7a6a4c; background:#fbf6ea;
       vertical-align:middle; margin-inline-start:10px}
.card h3{margin:0 0 2px; font-size:1.5rem}
.card h3 .aka{color:#6f675b; font-weight:normal}
.life{margin:0 0 4px; color:#5a5142; font-size:.95rem}
.edition{margin:0 0 12px; color:#6f675b; font-size:.82rem}
.summary{margin:0 0 14px; color:#3c352c}
.counts{margin:0 0 16px; font-size:.82rem; color:#6f675b}
.counts b{font-weight:normal; color:#7a4a2b}
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
.pfilter{margin:0 0 22px}
.pfilter input{font:inherit; font-size:.95rem; padding:8px 14px; border:1px solid #d8d0c2;
               border-radius:999px; background:#fff; color:#2b2620; min-width:min(24rem,100%)}
.pfilter input:focus-visible{outline:2px solid #7a4a2b; outline-offset:1px}
.pcount{font-size:.84rem; color:#6f675b; margin:0 0 14px}

.method{background:#f5f1e8; border:1px solid #e3dbcd; border-radius:10px; padding:18px 22px;
        font-size:.93rem; color:#4a4238; max-width:78ch}
.method ul{margin:10px 0 0; padding-inline-start:20px}
.method li{margin:5px 0}
footer{margin-top:60px; padding-top:22px; border-top:1px solid #e3dbcd;
       font-size:.83rem; color:#6f675b}
@media (max-width:640px){
  .card{grid-template-columns:1fr; gap:18px}
  /* a 132px frame inside a 350px card left the cover a strip in a white field */
  .cover{width:100%}
  h1{font-size:1.85rem}
  .couple{flex-basis:100%}
}
"""


def who_tile(r):
    img = ''
    if r.get('cover'):
        img = ('<img src="%s" alt="" loading="lazy"%s>'
               % (e(r['cover']), dims(r['cover'])))
    return ('<a class="who" href="%s">%s<span class="wn">%s</span>'
            '<span class="wd">%s</span><span class="wgo">%s ←</span></a>'
            % (e(front(r)), img, e(r['name']), e(r.get('life', '')),
               'הסיפור' if r.get('story_href') else 'למחקר'))


def couples_map():
    out = []
    for c in site.get('couples', []):
        tiles = ''.join(who_tile(BY_SLUG[s]) for s in c['slugs'] if s in BY_SLUG)
        out.append('<div class="couple"><span class="couple-label">%s</span>'
                   '<div class="pair">%s</div></div>' % (e(c.get('label', '')), tiles))
    return '<div class="couples">%s</div>' % ''.join(out) if out else ''


def card(r):
    p = []
    p.append('<article class="card" id="research-%s">' % e(r['slug']))
    if r.get('cover'):
        img = ('<img src="%s" alt="%s" loading="lazy"%s>'
               % (e(r['cover']), e(r.get('cover_alt', '')), dims(r['cover'])))
        if r.get('cover_href'):
            img = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (e(r['cover_href']), img)
        p.append('<figure class="cover" style="margin:0">%s<figcaption>%s</figcaption></figure>'
                 % (img, e(r.get('cover_alt', ''))))
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
    # one sentence, not a paragraph: the card's job is to send the reader to the
    # right person, and the research page does the explaining
    if r.get('one_liner'):
        p.append('<p class="summary">%s</p>' % e(r['one_liner']))
    if r.get('stats'):
        # the four big numbers were process metrics with no readable heading;
        # as one muted line they still say how much work is behind the page
        p.append('<p class="counts">' + ' · '.join(
            '<b>%s</b> %s' % (e(s['n']), e(s['l'])) for s in r['stats']) + '</p>')
    links = []
    if r.get('story_href'):
        links.append('<a class="btn primary" href="%s">הסיפור</a>' % e(r['story_href']))
        links.append('<a class="btn" href="%s">הדוח המלא</a>' % e(r['report_href']))
    else:
        links.append('<a class="btn primary" href="%s">למחקר המלא</a>' % e(r['report_href']))
    p.append('<p class="links">' + ''.join(links) + '</p>')
    p.append('</div></article>')
    return '\n'.join(p)


RANGE_RE = re.compile(r'^[\d\s–—/?.\-]+$')


def dates(txt):
    """A pure numeric range must be isolated as LTR, or bidi flips it
    ('1929 – 2021' would render as '2021 – 1929' inside an RTL block)."""
    txt = txt or ''
    if txt and RANGE_RE.match(txt):
        return '<bdi dir="ltr">%s</bdi>' % e(txt)
    return e(txt)


def people_grid(r):
    if not r.get('people'):
        return ''
    items = ''.join(
        '<a class="person" href="%s"><span class="pn">%s</span>'
        '<div class="pd">%s</div><div class="ps">%s</div></a>'
        % (e(q['h']), e(q['n']), dates(q.get('d', '')), e(q.get('s', '')))
        for q in r['people'])
    return ('<h2 class="sec" id="people-%s">%s</h2>\n<div class="people">%s</div>'
            % (e(r['slug']), e(r['name']), items))


FILTER_JS = """
(function(){
  var q=document.getElementById('pf'), cnt=document.getElementById('pc');
  if(!q) return;
  var cards=[].slice.call(document.querySelectorAll('.person'));
  var heads=[].slice.call(document.querySelectorAll('h2.sec[id^="people-"]'));
  var total=cards.length;
  function norm(s){ return (s||'').replace(/["']/g,'').toLowerCase(); }
  function run(){
    var v=norm(q.value.trim()), shown=0;
    cards.forEach(function(c){
      var on = !v || norm(c.textContent).indexOf(v)!==-1;
      c.hidden=!on; if(on) shown++;
    });
    heads.forEach(function(h){
      var grid=h.nextElementSibling, any=false;
      [].forEach.call(grid.querySelectorAll('.person'),function(c){ if(!c.hidden) any=true; });
      h.hidden=!any; grid.hidden=!any;
    });
    cnt.textContent = v ? (shown ? shown+' מתוך '+total : 'אין התאמה — נסו שם אחר או כתיב אחר')
                        : total+' אנשים בארכיון';
  }
  q.addEventListener('input', run); run();
})();
"""


def page(title, description, body, extra_script=''):
    script = ('<script>%s</script>' % extra_script) if extra_script else ''
    return ('<!DOCTYPE html>\n<html lang="he" dir="rtl">\n<head>\n'
            '<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>' + e(title) + '</title>\n'
            '<meta name="description" content="' + e(description[:160]) + '">\n'
            '<style>' + CSS + '</style>\n</head>\n<body>\n' + '\n'.join(body) +
            '\n' + script + '\n</body>\n</html>\n')


# ---------------------------------------------------------------- the portal --
body = []
body.append('<a class="skip" href="#main">דילוג לתוכן</a>')
body.append('<header class="top"><div class="wrap">')
body.append('<h1>%s</h1>' % e(site['title']))
body.append('<p class="lede">%s</p>' % site.get('lede', e(site.get('intro', ''))))
body.append(couples_map())
body.append('</div></header>')
body.append('<main id="main"><div class="wrap">')
body.append('<h2 class="sec" id="researches">ארבעת המחקרים</h2>')
for r in researches:
    body.append(card(r))
n_people = sum(len(r.get('people', [])) for r in researches)
body.append('<h2 class="sec" id="people">אנשים בארכיון</h2>')
body.append('<p class="summary">%d בני משפחה נדונים בדוחות, כל אחד עם קישור אל הפרק שבו הוא נדון. '
            '<a href="people.html">לאינדקס האנשים ←</a></p>' % n_people)
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
<p style="margin:12px 0 0">כל מחקר מוגש בשני עמודים: <b>הסיפור</b> — החיים לפי סדר הזמן, לקריאה
אחת; ו<b>הדוח המלא</b> — כל הראיות, המועמדים שנשללו, אינדקס המקורות והשיטה.</p>
</div>""")
body.append('</div></main>')
body.append('<footer>ארכיון מחקר משפחתי. המסמכים שמורים לצד הדוחות, כדי שהמחקר יישאר בר־אימות גם בלי חיבור לארכיונים המקוונים. · %s</footer>'
            % e(site.get('method_note', '')))

out = page(site['title'], site.get('intro', ''), body)
open('index.html', 'w', encoding='utf-8').write(out)
print('portal written: index.html, %d KB' % (len(out) // 1024))

# ----------------------------------------------------------- the person index --
pbody = []
pbody.append('<a class="skip" href="#main">דילוג לתוכן</a>')
pbody.append('<header class="top"><div class="wrap">')
pbody.append('<p class="crumb"><a href="index.html">← ארכיון מחקר המשפחה</a></p>')
pbody.append('<h1>אנשים בארכיון</h1>')
pbody.append('<p class="lede">כל בני המשפחה שנדונים בארבעת הדוחות, עם קישור אל הפרק שבו כל אחד '
             'נדון. חיפוש לפי שם, שנה או כתיב חלופי.</p>')
pbody.append('<div class="pfilter">'
             '<input id="pf" type="search" placeholder="חיפוש בשמות…" autocomplete="off" '
             'aria-label="חיפוש בשמות, בשנים ובכתיבים חלופיים"></div>')
pbody.append('<p class="pcount" id="pc" aria-live="polite"></p>')
pbody.append('</div></header>')
pbody.append('<main id="main"><div class="wrap">')
for r in researches:
    pbody.append(people_grid(r))
pbody.append('</div></main>')
pbody.append('<footer>ארכיון מחקר משפחתי · <a href="index.html">חזרה לארכיון</a></footer>')

pout = page('אנשים בארכיון — ' + site['title'],
            'אינדקס האנשים בארבעת מחקרי המשפחה', pbody, FILTER_JS)
open('people.html', 'w', encoding='utf-8').write(pout)
print('person index written: people.html, %d KB' % (len(pout) // 1024))

# ---- link check: every relative target must exist on disk ----
bad = []
for name, text in (('index.html', out), ('people.html', pout)):
    targets = set(re.findall(r'(?:href|src)="(?!https?:|#|mailto:|data:)([^"]+)"', text))
    for t in sorted(targets):
        path = urllib.parse.unquote(t.split('#')[0])
        if not path:
            continue
        if path.endswith('/'):
            path = path + 'index.html'
        if not os.path.exists(path):
            bad.append('%s → %s' % (name, t))
if bad:
    print('BROKEN LOCAL TARGETS:')
    for m in bad:
        print('  -', m)
    sys.exit(1)
print('link check: every relative target in both pages exists')
