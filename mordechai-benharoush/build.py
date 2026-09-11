import base64, re, markdown, pathlib

ROOT = pathlib.Path(__file__).parent
from PIL import Image
def sz(p): return Image.open(ROOT/"docs"/p).size
def b64(p): return "data:image/jpeg;base64," + base64.b64encode((ROOT/"docs"/p).read_bytes()).decode()

report_html = markdown.markdown((ROOT/"REPORT.md").read_text(encoding="utf-8"), extensions=["tables"])
changelog_html = markdown.markdown((ROOT/"CHANGELOG.md").read_text(encoding="utf-8"))
# grade badges inside tables
GRADES = {"מאומת": "g-v", "כמעט ודאי": "g-nc", "ככל הנראה": "g-l", "טעון אימות": "g-u", "נשלל": "g-x"}
def badge(m):
    w = m.group(1)
    return f'<span class="grade {GRADES[w]}">{w}</span>'
report_html = re.sub(r'\*\*(מאומת|כמעט ודאי|ככל הנראה|טעון אימות|נשלל)\*\*', badge, report_html)
report_html = re.sub(r'<td>(מאומת|כמעט ודאי|ככל הנראה|טעון אימות|נשלל)', lambda m: f'<td><span class="grade {GRADES[m.group(1)]}">{m.group(1)}</span>', report_html)
# heading ids for nav
def hid(m):
    lvl, txt = m.group(1), m.group(2)
    num = re.match(r'([\d.]+)\.?\s', txt)
    i = "s" + num.group(1).rstrip(".").replace(".", "-") if num else re.sub(r'\W+', '-', txt)[:30]
    return f'<h{lvl} id="{i}">{txt}</h{lvl}>'
report_html = re.sub(r'<h([23])>(.*?)</h\1>', hid, report_html)

EV = [
 ("ev_yalkut_1954_row.jpg", "ראיה 1 · השורה בילקוט הפרסומים 407, עמ' 647 — רשימה 10, מחוז חיפה, נפת חדרה",
  "«בנערוש · מרדושי → בן הרוש · מרדכי · מגדים · 12.12.54» — השם הקודם (שם משפחה ושם פרטי), השם החדש, מקום המגורים, תאריך אישור השינוי. עמודת מספר הזהות מושחרת בסריקה.",
  "https://igra-images.genealogy.org.il/1948_68_nc/1955_nc_13_407_1.jpg", "docs/yalkut_407_p647.jpg"),
 ("ev_yalkut_1954_header.jpg", "ראיה 2 · כותרת הרשימה — \"הודעה בדבר שינויי שם\"",
  "\"שינויי שמות האנשים המפורטים להלן נרשמו ביחידות רישום התושבים, האגף למרשם התושבים, משרד הפנים\" · רשימה מס' 10 · מחוז חיפה — נפת חדרה · עמודות: השם הקודם, השם החדש, מקום המגורים, מספר הזהות, תאריך אישור השינוי.",
  "https://igra-images.genealogy.org.il/1948_68_nc/1955_nc_13_407_1.jpg", "docs/yalkut_407_p647.jpg"),
 ("ev_yalkut_1954_footer.jpg", "ראיה 3 · כותרת תחתית העמוד",
  "«ילקוט הפרסומים 407, ח' בניסן תשט\"ו, 31.3.1955» · עמ' 647 — הציטוט הביבליוגרפי של הגיליון.",
  "https://igra-images.genealogy.org.il/1948_68_nc/1955_nc_13_407_1.jpg", "docs/yalkut_407_p647.jpg"),
]
gallery = "".join(f'''
<figure class="ev">
  <a href="{loc}" target="_blank" rel="noopener"><img src="{b64(f)}" alt="{t}" width="{sz(f)[0]}" height="{sz(f)[1]}" loading="lazy"></a>
  <figcaption><strong>{t}</strong><span>{c}</span>
  <span class="links"><a href="{ext}" target="_blank" rel="noopener">הסריקה המלאה ב-IGRA</a> · <a href="{loc}" target="_blank" rel="noopener">עותק מקומי</a></span></figcaption>
</figure>''' for f, t, c, ext, loc in EV)

tree = '''
<svg class="tree" viewBox="-10 0 790 300" role="img" aria-label="עץ משפחה: יונה ויקוט בן הרוש, בנם מרדכי, ואשתו מרים לבית דהן">
 <defs><style>
  .p{fill:var(--card);stroke:var(--line);stroke-width:1.2}
  .p.focus{stroke:var(--accent);stroke-width:2}
  .n{font-family:var(--display);font-size:17px;fill:var(--ink)}
  .m{font-family:var(--body);font-size:12px;fill:var(--muted)}
  .e{stroke:var(--line);stroke-width:1.5;fill:none}
  .e.marr{stroke-dasharray:4 3}
 </style></defs>
 <path class="e" d="M385 62 V120 M385 120 V150"/>
 <path class="e marr" d="M350 62 H420"/>
 <path class="e marr" d="M475 195 H545"/>
 <rect class="p" x="180" y="30" width="170" height="62" rx="4"/>
 <text class="n" x="265" y="55" text-anchor="middle">יונה בן הרוש</text>
 <text class="m" x="265" y="78" text-anchor="middle">אביו (משפחה) · טעון אימות</text>
 <rect class="p" x="420" y="30" width="170" height="62" rx="4"/>
 <text class="n" x="505" y="55" text-anchor="middle">יקוט בן הרוש</text>
 <text class="m" x="505" y="78" text-anchor="middle">אמו (משפחה) · טעון אימות</text>
 <rect class="p focus" x="290" y="150" width="185" height="80" rx="4"/>
 <text class="n" x="382" y="176" text-anchor="middle">מרדכי בן הרוש</text>
 <text class="m" x="382" y="195" text-anchor="middle"><tspan direction="ltr" unicode-bidi="isolate">1931</tspan> – <tspan direction="ltr" unicode-bidi="isolate">2010</tspan> (משפחה) · עלה 1947/48</text>
 <text class="m" x="382" y="213" text-anchor="middle">"מרדושי בנערוש", מגדים 1954? — טעון אימות</text>
 <rect class="p" x="545" y="160" width="185" height="62" rx="4"/>
 <text class="n" x="637" y="185" text-anchor="middle">מרים לבית דהן</text>
 <text class="m" x="637" y="206" text-anchor="middle">אשתו · 1939, מכנאס · עלתה 1956</text>
 <text class="m" x="385" y="275" text-anchor="middle">קו מקווקו — נישואין · מסגרת ירוקה — נושא הדף</text>
</svg>'''

# adjust: the marriage edge should join Mordechai (right edge x=155,y=211) to Miriam (x=215)
html = f'''<title>מרדכי בן הרוש</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;500;700&family=Assistant:wght@400;600&display=swap">
<style>
:root{{--bg:#FAF8F3;--card:#FFFFFF;--ink:#1E2A32;--muted:#5E6B73;--line:#D9D4C7;--accent:#1F6F5B;--accent-ink:#0F4A3B;--flag:#9A3B2F;--amber:#8A6A12;--display:"Frank Ruhl Libre",Georgia,"Times New Roman",serif;--body:"Assistant","Segoe UI",Arial,sans-serif;color-scheme:light}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#151A1D;--card:#1E2529;--ink:#ECE9E1;--muted:#A5ADB3;--line:#36404A;--accent:#5FB89E;--accent-ink:#8ED7BF;--flag:#E08476;--amber:#D8B457;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#151A1D;--card:#1E2529;--ink:#ECE9E1;--muted:#A5ADB3;--line:#36404A;--accent:#5FB89E;--accent-ink:#8ED7BF;--flag:#E08476;--amber:#D8B457;color-scheme:dark}}
html{{direction:rtl}}
body{{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.65;margin:0;padding-block:0 4rem;padding-inline:clamp(16px,4vw,40px)}}
.wrap{{max-width:74ch;margin:0 auto}}
header.hero{{padding-block:2.5rem 1.5rem;border-bottom:1px solid var(--line)}}
.eyebrow{{font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-ink);font-weight:600}}
h1{{font-family:var(--display);font-weight:500;font-size:clamp(2rem,5vw,3rem);line-height:1.15;margin:.3rem 0 .6rem;text-wrap:balance}}
.sub{{color:var(--muted);font-size:1.05rem;max-width:60ch}}
.strip{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1rem;margin-top:1.6rem}}
.strip div{{border-top:2px solid var(--accent);padding-top:.5rem}}
.strip b{{display:block;font-family:var(--display);font-size:1.7rem;font-weight:500;font-variant-numeric:tabular-nums}}
.strip span{{font-size:.85rem;color:var(--muted)}}
nav.toc{{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:.5rem 0;margin-bottom:1.5rem;z-index:2;font-size:.9rem;display:flex;flex-wrap:wrap;gap:.3rem 1rem}}
nav.toc a{{color:var(--accent-ink);text-decoration:none}}
nav.toc a:hover,nav.toc a:focus-visible{{text-decoration:underline}}
h2{{font-family:var(--display);font-weight:500;font-size:1.65rem;margin:2.6rem 0 .8rem;text-wrap:balance}}
h3{{font-family:var(--display);font-weight:500;font-size:1.2rem;margin:1.8rem 0 .5rem}}
p{{margin:0 0 1rem}}
a{{color:var(--accent-ink)}}
table{{border-collapse:collapse;width:100%;font-size:.93rem;margin:.6rem 0 1.2rem;font-variant-numeric:tabular-nums}}
.tbl{{overflow-x:auto}}
th,td{{text-align:right;vertical-align:top;padding:.45rem .6rem;border-bottom:1px solid var(--line)}}
th{{font-weight:600;color:var(--muted);font-size:.8rem;letter-spacing:.04em}}
ol,ul{{padding-inline-start:1.4rem}} li{{margin-bottom:.35rem}}
.grade{{display:inline-block;font-size:.75rem;font-weight:600;padding:.05rem .5rem;border-radius:2px;border:1px solid currentColor;white-space:nowrap}}
.g-v{{color:var(--accent-ink)}} .g-nc{{color:var(--accent-ink);border-style:dashed}} .g-l{{color:var(--amber)}} .g-u{{color:var(--flag)}} .g-x{{color:var(--muted);text-decoration:line-through}}
.legend{{display:flex;flex-wrap:wrap;gap:.6rem;font-size:.85rem;color:var(--muted);margin:.8rem 0 0}}
.tree{{width:100%;height:auto;background:var(--card);border:1px solid var(--line);border-radius:4px;padding:.5rem;box-sizing:border-box;margin:1rem 0}}
.ev{{margin:0 0 1.6rem;background:var(--card);border:1px solid var(--line);border-radius:4px;padding:.6rem}}
.ev img{{width:100%;height:auto;display:block;border:1px solid var(--line)}}
.ev figcaption{{font-size:.9rem;padding:.6rem .2rem 0;display:grid;gap:.25rem}}
.ev figcaption strong{{font-family:var(--display);font-weight:500;font-size:1.02rem}}
.ev .links{{color:var(--muted)}}
.note{{border-inline-start:3px solid var(--accent);padding:.4rem .9rem;background:var(--card);margin:1rem 0;font-size:.95rem}}
footer{{margin-top:3rem;border-top:1px solid var(--line);padding-top:1rem;font-size:.85rem;color:var(--muted)}}
@media (prefers-reduced-motion:no-preference){{html{{scroll-behavior:smooth}}}}
@media (max-width:480px){{body{{font-size:16px}} .strip{{grid-template-columns:1fr 1fr}}}}
</style>
<div class="wrap">
<header class="hero">
 <div class="eyebrow">תיק מחקר משפחתי · מהדורה 1 · 11.09.2026 · דף נלווה למחקר על <a href="../miriam-benharoush/">מרים בן הרוש</a></div>
 <h1>מרדכי בן הרוש</h1>
 <p class="sub">בן יונה ויקוט, יליד מרוקו 1931, עלה ב-1947 או 1948: מה נבדק, מי המועמד היחיד שנשאר פתוח, ומה נשלל — כל טענה עם המקור שלה.</p>
 <div class="strip">
  <div><b>1</b><span>מועמד פתוח — מגדים 1954</span></div>
  <div><b>6</b><span>רשומות שנשללו</span></div>
  <div><b>16/29</b><span>קובצי רשימות עולים 1947–49 שנקראו</span></div>
  <div><b>5</b><span>שאלות פתוחות</span></div>
 </div>
 <div class="legend">סולם ודאות: <span class="grade g-v">מאומת</span> <span class="grade g-nc">כמעט ודאי</span> <span class="grade g-l">ככל הנראה</span> <span class="grade g-u">טעון אימות</span> <span class="grade g-x">נשלל</span></div>
</header>
<nav class="toc" aria-label="ניווט"><a href="#s1">תמצית</a><a href="#s2">נקודת המוצא</a><a href="#s3">המועמד הפתוח</a><a href="#s4">נשללו</a><a href="#s5">מה לא נמצא</a><a href="#tree">עץ</a><a href="#gallery">ראיות</a><a href="#s7">פעולות</a><a href="#s8">מקורות</a><a href="#changelog">מהדורות</a></nav>
<main>
{report_html.replace('<h2 id="s6">6. עץ המשפחה</h2>', '<h2 id="s6">6. עץ המשפחה</h2><span id="tree"></span>' + tree)}
<h2 id="gallery">גלריית ראיות</h2>
<p>החיתוכים נלקחו מסריקת עמוד 647 של ילקוט הפרסומים 407 (ספריית המשפטים ע"ש דוד י. לייט, אוניברסיטת תל אביב, דרך IGRA). לחיצה על התמונה פותחת את העותק המקומי של העמוד המלא; הקישור החיצוני מוביל לסריקה בשרת IGRA.</p>
{gallery}
<h2 id="changelog">יומן מהדורות</h2>
{changelog_html.replace('<h1>יומן מהדורות</h1>','').replace('<h2>','<h3>').replace('</h2>','</h3>')}
</main>
<footer>קבצי עבודה: <a href="THREADS.md">THREADS.md</a> · <a href="NEGATIVES.md">NEGATIVES.md</a> · <a href="BLOCKERS.md">BLOCKERS.md</a> · <a href="TOOLSTATE.md">TOOLSTATE.md</a> · <a href="CHANGELOG.md">CHANGELOG.md</a> · מקור הדוח: <a href="REPORT.md">REPORT.md</a></footer>
</div>
'''
html = html.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
(ROOT/"index.html").write_text(html, encoding="utf-8")
head, body = html.split("</style>", 1)
(ROOT/"report.html").write_text('<!doctype html>\n<html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">' + head + "</style></head><body>" + body + "</body></html>", encoding="utf-8")
