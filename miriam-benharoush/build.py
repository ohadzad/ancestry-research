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
 ("ev_marie_1949.jpg", "ראיה 1 · מרי דהן, פנקס 1949, מספר סידורי 1617 (שורה 7 בעמוד)",
  "«Dahan Marie · 10 ans · Chalom Yacot · M. · A.M. Tail. ind. · 54» — שם; 10 ans = בת עשר; הורים; M. = מרוקאית; A.M. Tail. ind. = ככל הנראה \"Ancien Mellah, Tailleur indigène\" (המלאח הישן, חייט מקומי — פענוח); 54 = ככל הנראה שנת היציאה 1954. השורות שמעל ומתחת נשארו לעיגון.",
  "https://igra-images.genealogy.org.il/AIU_Morocco/AIU_MA_240.1_40.jpg", "docs/AIU_MA_240.1_40.jpg"),
 ("ev_rebeca_1950.jpg", "ראיה 2 · רבקה (Rébéca) דהן, פנקס 1950, מספר סידורי 1878 (שורה 8 בעמוד)",
  "«Dahan Rébéca · 7 ans · Chalom ~ Yacot · … oct 55 · a quitté» — 7 ans = בת שבע; oct 55 = אוקטובר 1955; a quitté = עזבה (את בית הספר). תא תאריך הכניסה בשורה ריק — ראו ראיה 4.",
  "https://igra-images.genealogy.org.il/AIU_Morocco/AIU_MA_240.1_51.jpg", "docs/AIU_MA_240.1_51.jpg"),
 ("ev_rachel_1953.jpg", "ראיה 3 · רחל דהן, פנקס 1953, מספר סידורי 3054 (שורה 4 בעמוד)",
  "«Dahan Rachel · 6 ans · Chalom Yacot · [absente?] · Oct 53» — 6 ans = בת שש; עמודת הלאום מסומנת בסוגר \"כנ\"ל\" מהשורה הראשונה (Marocaine); המילה בעמודת המגורים והמקצוע נקראת כ-absente (נעדרת) ולא פוענחה בוודאות; Oct 53 = אוקטובר 1953 בסימן \"כנ\"ל\".",
  "https://igra-images.genealogy.org.il/AIU_Morocco/AIU_MA_240.2_00028.jpg", "docs/AIU_MA_240.2_00028.jpg"),
 ("ev_header_1950.jpg", "ראיה 4 · כותרת עמוד 1950 ושורה 1871 — הבסיס להיקש תאריך הכניסה",
  "בשורה הראשונה בעמוד (מס' 1871, Sebbag Fréha) רשום בעמודת הכניסה \"Février 50\" (פברואר 1950); בשורות שאחריה, ובהן שורת רבקה (1878), התא ריק. מכאן ההיקש שהרישום נעשה בתחילת 1950 — ככל הנראה, לא קריאה.",
  "https://igra-images.genealogy.org.il/AIU_Morocco/AIU_MA_240.1_51.jpg", "docs/AIU_MA_240.1_51.jpg"),
 ("ev_header_1949.jpg", "ראיה 5 · מפתח העמודות — כותרות הפנקס (1949)",
  "מימין לשמאל בסריקה (הפנקס בצרפתית, משמאל לימין): מס' סידורי · שם ושם פרטי · תאריך לידה או גיל משוער · שמות ההורים · לאום · מגורי ההורים · תאריך כניסה · תאריך יציאה · סיבת היציאה · הערות.",
  "https://igra-images.genealogy.org.il/AIU_Morocco/AIU_MA_240.1_40.jpg", "docs/AIU_MA_240.1_40.jpg"),
]
gallery = "".join(f'''
<figure class="ev">
  <a href="{loc}" target="_blank" rel="noopener"><img src="{b64(f)}" alt="{t}" width="{sz(f)[0]}" height="{sz(f)[1]}" loading="lazy"></a>
  <figcaption><strong>{t}</strong><span>{c}</span>
  <span class="links"><a href="{ext}" target="_blank" rel="noopener">הסריקה המלאה ב-IGRA</a> · <a href="{loc}" target="_blank" rel="noopener">עותק מקומי</a></span></figcaption>
</figure>''' for f, t, c, ext, loc in EV)

tree = '''
<svg class="tree" viewBox="-10 0 790 330" role="img" aria-label="עץ משפחה: שלום ויקוט דהן, בנותיהם מרים, רבקה ורחל, ובעלה של מרים מרדכי בן הרוש">
 <defs><style>
  .p{fill:var(--card);stroke:var(--line);stroke-width:1.2}
  .p.focus{stroke:var(--accent);stroke-width:2}
  .n{font-family:var(--display);font-size:17px;fill:var(--ink)}
  .m{font-family:var(--body);font-size:12px;fill:var(--muted)}
  .e{stroke:var(--line);stroke-width:1.5;fill:none}
  .e.marr{stroke-dasharray:4 3}
 </style></defs>
 <path class="e" d="M265 62 V120 H647 M287 120 V150 M467 120 V150 M647 120 V150"/>
 <path class="e marr" d="M160 200 H205"/>
 <path class="e marr" d="M230 62 H300"/>
 <rect class="p" x="60" y="30" width="170" height="62" rx="4"/>
 <text class="n" x="145" y="55" text-anchor="middle">שלום דהן</text>
 <text class="m" x="145" y="78" text-anchor="middle">חייט? במלאח הישן, מכנאס (פענוח) · ירושלים</text>
 <rect class="p" x="300" y="30" width="170" height="62" rx="4"/>
 <text class="n" x="385" y="55" text-anchor="middle">יקוט דהן</text>
 <text class="m" x="385" y="78" text-anchor="middle">ירושלים</text>
 <rect class="p focus" x="205" y="150" width="165" height="70" rx="4"/>
 <text class="n" x="287" y="176" text-anchor="middle">מרים (מרי) בן הרוש</text>
 <text class="m" x="287" y="195" text-anchor="middle">לבית דהן · נולדה <tspan direction="ltr" unicode-bidi="isolate">1939</tspan> (ת"ז; פנקס 1949)</text>
 <text class="m" x="287" y="211" text-anchor="middle">מכנאס, עלייה 1956, חולון</text>
 <rect class="p" x="385" y="150" width="165" height="70" rx="4"/>
 <text class="n" x="467" y="176" text-anchor="middle">רבקה דהן</text>
 <text class="m" x="467" y="195" text-anchor="middle"><tspan direction="ltr" unicode-bidi="isolate">~1943</tspan> (פנקס 1950)</text>
 <text class="m" x="467" y="211" text-anchor="middle">עזבה את ביה"ס באוקטובר 1955</text>
 <rect class="p" x="565" y="150" width="165" height="70" rx="4"/>
 <text class="n" x="647" y="176" text-anchor="middle">רחל דהן</text>
 <text class="m" x="647" y="195" text-anchor="middle"><tspan direction="ltr" unicode-bidi="isolate">~1947</tspan> (פנקס 1953)</text>
 <rect class="p" x="0" y="170" width="160" height="62" rx="4"/>
 <text class="n" x="80" y="195" text-anchor="middle">מרדכי בן הרוש</text>
 <text class="m" x="80" y="216" text-anchor="middle">בעלה · 1931 – 2010 · בן יונה ויקוט (משפחה)</text>
 <text class="m" x="385" y="300" text-anchor="middle">קו מקווקו — נישואין · מסגרת ירוקה — נושאת המחקר · שנים עם ~ נגזרות מגיל בפנקס</text>
</svg>'''

# adjust: the marriage edge should join Mordechai (right edge x=155,y=211) to Miriam (x=215)
html = f'''<title>מרים בן הרוש לבית דהן</title>
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
 <div class="eyebrow">תיק מחקר משפחתי · מהדורה 4 · 11.09.2026</div>
 <h1>מרים בן הרוש לבית דהן</h1>
 <p class="sub">ממכנאס לחולון: מה מספרים פנקסי אליאנס, רשימות העולים ומאגרי IGRA על מרים, הוריה שלום ויקוט ואחיותיה רבקה ורחל — וכל טענה עם המקור שלה.</p>
 <div class="strip">
  <div><b>3</b><span>רשומות פנקס אליאנס עם ההורים Chalom · Yacot</span></div>
  <div><b dir="ltr">~70</b><span>רשומות "דהן" ממכנאס שנבדקו</span></div>
  <div><b>19</b><span>קבצי רשימות עולים 1955–1957 שנסרקו</span></div>
  <div><b>5</b><span>שאלות פתוחות למשפחה ולארכיונים</span></div>
 </div>
 <div class="legend">סולם ודאות: <span class="grade g-v">מאומת</span> <span class="grade g-nc">כמעט ודאי</span> <span class="grade g-l">ככל הנראה</span> <span class="grade g-u">טעון אימות</span> <span class="grade g-x">נשלל</span></div>
</header>
<nav class="toc" aria-label="ניווט"><a href="#s1">תמצית</a><a href="#s2">נקודת המוצא</a><a href="#s3">מכנאס</a><a href="#s4">הזיהוי</a><a href="#s5">מה לא נמצא</a><a href="#tree">עץ</a><a href="#gallery">ראיות</a><a href="#s7">פעולות</a><a href="#s8">מקורות</a><a href="#changelog">מהדורות</a></nav>
<main>
{report_html.replace('<h2 id="s6">6. עץ המשפחה</h2>', '<h2 id="s6">6. עץ המשפחה</h2><span id="tree"></span>' + tree)}
<h2 id="gallery">גלריית ראיות</h2>
<p>כל חיתוך נלקח מסריקת הפנקס המקורית (CAHJP דרך IGRA), לא מכרטיס תוצאות. לחיצה על התמונה פותחת את העותק המקומי של הדף המלא; הקישור החיצוני מוביל לסריקה בשרת IGRA.</p>
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
