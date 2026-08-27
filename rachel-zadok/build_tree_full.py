# -*- coding: utf-8 -*-
"""Strulovits-Rappaport family — FULL extended descendant chart (v1).
All documented persons incl. Gedalia's children and the siblings' children."""

W, H = 2400, 2230
COL  = {'m': '#a0392e', 's': '#3a7d44', 'r': '#b8860b', 'u': '#8a8177'}
FILL = {'m': '#fdf3f1', 's': '#f2f8f3', 'r': '#fdf6e3', 'u': '#f7f5f1'}

PW, PH = 210, 84
boxes, lines, labels = [], [], []

def box(cx, cy, w, h, fate, name, dates, sub=None, small=False):
    boxes.append((cx-w/2, cy-h/2, w, h, fate, name, dates, sub, small))
    return cx, cy

def line(d): lines.append(d)
def mlabel(x, y, txt): labels.append((x, y, txt))

def couple(cx, cy, right, left, wed=None, gap=64, rw=None, lw=None):
    rw = rw or PW; lw = lw or PW
    rx, lx = cx + gap/2 + rw/2, cx - gap/2 - lw/2
    box(rx, cy, rw, PH, right[0], right[1], right[2], right[3] if len(right)>3 else None)
    box(lx, cy, lw, PH, left[0],  left[1],  left[2],  left[3]  if len(left)>3 else None)
    line(f'M {rx-rw/2} {cy} H {lx+lw/2}')
    if wed: mlabel(cx, cy-PH/2-8, wed)
    return cx, cy

def drop(x, y1, y2): line(f'M {x} {y1} V {y2}')
def bus(y, x1, x2): line(f'M {x1} {y} H {x2}')

# ---------------- Generation 0 ----------------
g0 = 110
couple(1620, g0, ('u','משה רפפורט','המאה ה-19','אוקרמזו'),
                 ('u','יֶנטה שפיגל','המאה ה-19', None))
couple(1000, g0, ('u','זלמן ברקוביץ','המאה ה-19','קרצ׳ונפלבה'),
                 ('u','פריידא קאופמן','המאה ה-19', None))
mlabel(1000, g0+PH/2+16, 'הוריה של מינדל, אשתו השלישית של גדליה')

# ---------------- Generation 1 ----------------
g1 = 330
couple(2145, g1, ('u','לייב סטרולוביץ','המאה ה-19','קושלובו'),
                 ('u','ריבקה (נאיוביץ/שפשוביץ?)','המאה ה-19', None))
couple(1620, g1, ('u','גדליה רפפורט','נ׳ 1.4.1846 · נפ׳ 1908/9','בעל האחוזות של אוקרמזו'),
                 ('u','אסתר כץ','נפ׳/נפרדו לפני 1884','אשתו השנייה'))
mlabel(1345, g1+PH/2+40, 'נשא גם את ריבקה גרוסמן, ומ-6.8.1884 את מינדל ברקוביץ (1865 - לפני 8.1944), בת זלמן ופריידא')
couple(760, g1, ('u','ברל (דב) פרקש','המאה ה-19','דנילובו'),
                ('u','גיטל','המאה ה-19', None))
box(300, g1, PW, PH, 'u', 'משפחת שטיינר', 'קירלהאזה (קורולבו)', None)
drop(1620, g0+PH/2, g1-PH/2)   # Moshe=Jenta -> Gedalia

# ---------------- Gedalia's children (all wives), birth order RTL ----------------
gG = 562; GH = 104; GW = 185
kids_g = [
 ('u','שיינדל (זיסוביץ)','נ׳ 1869','בת ריבקה גרוסמן|⚭ לזר זיסוביץ; בנה גדליה נ׳ 1909'),
 # שרה (1876) — יורדת למטה, חריץ ייעודי
 ('u','נתן','נ׳ 1879','בן אסתר כץ; סוחר עצים|⚭ ברטה וייס 1906; בנו גדליה נ׳ 1910'),
 ('u','אלדר','נ׳ 11/1885','בן מינדל ברקוביץ; בנקאי|מנכ״ל הבנק הנאג׳סלשי; ⚭ חוה וייס 1909'),
 ('u','ברטה','נ׳ 1889','בת מינדל'),
 ('u','יוסף-דוד','נ׳ 16.10.1891','בן גדליה ומינדל (דף עד: "גדלי" + "מינדה ברקוביץ")|נספה באושוויץ 26.5.1942'),
 ('u','פרידריקה','נ׳ 1894','בת מינדל; נישאה 1914'),
 ('u','זלמן','נ׳ 1897','בן מינדל'),
 ('u','הרמן','נ׳ 1904','נפטר בן 7 שבועות'),
 ('u','מאיר','נ׳ 1908','בן מינדל; טכנאי שיניים|⚭ רוזה נוילינגר (חוסט, 1912)|הודעת "מבוקש" נגדם, 1944'),
]
busG_y = 468
drop(1620, g1+PH/2, busG_y)
xsG = [2280 - i*200 for i in range(9)]
bus(busG_y, min(xsG), max(xsG))
for x,(f,n,d,s) in zip(xsG, kids_g):
    drop(x, busG_y, gG-GH/2); box(x, gG, GW, GH, f, n, d, s, small=True)
# שרה — חריץ בין שיינדל לנתן, יורדת אל זוג יעקב=שרה
line(f'M 2180 {busG_y} V 745 H 1738 V 758')
mlabel(2180, 660, 'שרה (1876) ↓')

# ---------------- Generation 2 ----------------
g2 = 800
couple(1875, g2, ('u','יעקב סטרולוביץ','נ׳ 15.1.1870 · נפ׳ 1945','שרד בהסתתרות; מת בחוסט'),
                 ('m','שרה רפפורט','נ׳ 1/1876 · נפ׳ 1944','נרצחה באושוויץ'),
        wed='נישואים דתיים, ~1892')
couple(530, g2, ('m','בצלאל פרקש','נ׳ 1873 · נפ׳ 1944','"Czallo/Czulo" ברשומות|נרצח באושוויץ'),
                ('m','אסתר שטיינר','נ׳ 1879 · נפ׳ 1944','ילידת קירלהאזה|נרצחה באושוויץ'))
yaak_rx = 1875+32+PW/2; sara_lx = 1875-32-PW/2
betz_rx = 530+32+PW/2;  este_lx = 530-32-PW/2
line(f'M 2145 {g1+PH/2} V 440 H 2390 V 725 H {yaak_rx} V {g2-PH/2}')  # Leib -> Yaakov
line(f'M 760 {g1+PH/2} V 700 H {betz_rx} V {g2-PH/2}')                # Berl -> Betzalel
line(f'M 300 {g1+PH/2} V 700 H {este_lx} V {g2-PH/2}')                # Steiner -> Ester

# ---------------- Generation 3: Arye=Rivka + siblings (with their children) ----------------
g3 = 1090
c_ar = couple(1120, g3, ('m','אריה-לייב סטרולוביץ-רפפורט','נ׳ 3/1894 · נפ׳ 1944?','סוחר עורות; מת מרעב באושוויץ (עדות)'),
                        ('m','רבקה-רוזה פרקש','נ׳ 25.4.1904 · נפ׳ 1944','נרצחה באושוויץ 1944; המועד לא ידוע'),
              wed='⚭ (נישואים דתיים)', rw=250)
arye_x  = 1120+32+250/2
rivro_x = 1120-32-PW/2

SW, SH = 232, 112
sibA1 = [
 ('m','ריבקה (גדלוביץ)','נ׳ 1896 · נפ׳ 1944','⚭ יצחק גדלוביץ, אפשה|אסתר (שרדה), מרדכי, לייב, שמיל, פרקש'),
 ('m','אסתר','נ׳ 1897 · נפ׳ 1942','בתה רגינה נ׳ 1927'),
 ('m','רחל (קליין)','נ׳ 1899 · נפ׳ 1944','⚭ דוד קליין|מונקץ׳/קרצקי'),
 ('m','מנדל','נ׳ 1900 · נפ׳ 1944','⚭ רוחל הרשקוביץ, 1938|גדליה, משה, רגינה†, אסתר, +בן ובת'),
]
sibA2 = [
 ('m','גיטל (וולף)','נ׳ 1902 · נפ׳ 1944','⚭ אלכסנדר וולף, 1933|טקהאזה'),
 ('u','סימה','נ׳ 1904','גורלה לא תועד'),
 ('m','יצחק','נ׳ 1905 · נפ׳ 1944','רווק, סוחר ויערן|נספה במאוטהאוזן'),
 ('u','חיה','נ׳ 1907','גורלה לא תועד'),
]
sibA3 = [
 ('s','נתן (Neso)','נ׳ 1908','שרד; ברשימות החוזרים בקושלובו'),
 ('m','גדליה','נ׳ 1911','רווק, יערן; נרצח בשואה'),
 ('u','שרה (פוירוורקר)','נ׳ 1912','⚭ יוזף פוירוורקר, נאג׳בוצ׳קו|בנם גיולה נ׳ 20.6.1943'),
 ('s','פייגה (פאני, לבוביץ)','נ׳ 1914','תאומה; שרדה בהסתתרות|הגישה דפי עד על אחיה'),
 ('s','פפי','נ׳ 1914','תאומה; שרדה|ככה"נ זו שנספתה בתאונה אחרי השחרור'),
]
busA_y = 940
drop(1875, g2+PH/2, busA_y)
rowA1_y, rowA2_y, rowA3_y = 1090, 1290, 1490
P = 248
xs1 = [2270 - i*P for i in range(len(sibA1))]
xs2 = [2270 - i*P for i in range(len(sibA2))]
xs3 = [2270 - i*P for i in range(len(sibA3))]
FEED = 2392
bus(busA_y, arye_x, FEED)
drop(arye_x, busA_y, g3-PH/2)
for x,(f,n,d,s) in zip(xs1,sibA1):
    drop(x, busA_y, rowA1_y-SH/2); box(x, rowA1_y, SW, SH, f, n, d, s, small=True)
busA2_y = rowA1_y + SH/2 + 34
drop(FEED, busA_y, busA2_y); bus(busA2_y, FEED, min(xs2))
for x,(f,n,d,s) in zip(xs2,sibA2):
    drop(x, busA2_y, rowA2_y-SH/2); box(x, rowA2_y, SW, SH, f, n, d, s, small=True)
busA3_y = rowA2_y + SH/2 + 34
drop(FEED, busA2_y, busA3_y); bus(busA3_y, FEED, min(xs3))
for x,(f,n,d,s) in zip(xs3,sibA3):
    drop(x, busA3_y, rowA3_y-SH/2); box(x, rowA3_y, SW, SH, f, n, d, s, small=True)

# Rivka-Roza's 13 siblings (left side) — all 14 children of Betzalel & Ester
# documented in the Danylovo-area civil records (JewishGen "Farkas" search, 18.08.2026)
sibB1 = [
 ('u','מנדל','נ׳ 26.4.1897','גורלו לא תועד'),
 ('m','גולדה-ארנקה (פוקס)','נ׳ 2.1.1899 · נפ׳ 1944','⚭ שמואל פוקס, וישק|לילי ושרה שרדו; עוד חמישה נספו'),
 ('m','אליהו','נ׳ 30.5.1901 · נפ׳ 1944','⚭ רוז׳נה (רייזל) זלמנוביץ, 1932|מכולת בדנילובו; גולדה†, איגנץ|נרצח עם ארבעת ילדיו'),
]
sibB2 = [
 ('m','זיסל-לייב (ליפוט)','נ׳ 7.10.1906 · נפ׳ 1944','⚭ סרנה (שרה) פוקס, 1930|ירקן; בנם הרמן (1941)†|נרצח עם שתי בנותיו'),
 ('m','חנה (הלנה)','נ׳ 9.2.1909 · נפ׳ 1944','⚭ יוסף פרקש, חוסט, 1928|בנם דוד (1936)†|נרצחה עם בנה חיים'),
 ('m','רחל (איצקוביץ)','נ׳ 22.11.1913 · נפ׳ 1944/5','⚭ הרש איצקוביץ, רוסקה פולה, 1935|ברל (1936), שרה (1938)|ייתכן "רחל פרקש" מעדות טורן'),
]
sibB3 = [
 ('u','הרמן','נ׳ 14.2.1918','גורלו לא תועד'),
 ('u','שישה שמתו בילדותם','1895–1920','לאיה (1895), הלנה (1903), רגינה (1911),|בן ללא שם (1912), זלמן (1912), צינה (1920)'),
]
busB_y = 940
drop(530, g2+PH/2, busB_y)
xsB1 = [740 - i*P for i in range(len(sibB1))]
xsB2 = [740 - i*P for i in range(len(sibB2))]
xsB3 = [740 - i*P for i in range(len(sibB3))]
FEEDB = 110
bus(busB_y, rivro_x, FEEDB)
drop(rivro_x, busB_y, g3-PH/2)
for x,(f,n,d,s) in zip(xsB1,sibB1):
    drop(x, busB_y, rowA1_y-SH/2); box(x, rowA1_y, SW, SH, f, n, d, s, small=True)
busB2_y = rowA1_y + SH/2 + 34
drop(FEEDB, busB_y, busB2_y); bus(busB2_y, FEEDB, max(xsB2))
for x,(f,n,d,s) in zip(xsB2,sibB2):
    drop(x, busB2_y, rowA2_y-SH/2); box(x, rowA2_y, SW, SH, f, n, d, s, small=True)
busB3_y = rowA2_y + SH/2 + 34
drop(FEEDB, busB2_y, busB3_y); bus(busB3_y, FEEDB, max(xsB3))
for x,(f,n,d,s) in zip(xsB3,sibB3):
    drop(x, busB3_y, rowA3_y-SH/2); box(x, rowA3_y, SW, SH, f, n, d, s, small=True)

# ---------------- Generation 4: the five children ----------------
g4 = 1750
bus4_y = 1650
drop(1120, g3+PH/2, bus4_y)
box(1900, g4, PW, PH, 's', 'דב', 'נ׳ 1924? · נפ׳ 1998', 'פרטיזנים; רמתיים')
box(1670, g4, PW, PH, 'm', 'סימה (Sari)', 'נ׳ 26.12.1926 · נפ׳ 1944/5', 'מתה בשטוטהוף (עדות), אסירה 38443')
couple(1290, g4, ('r','רחל ("רוצי")','נ׳ 16.4.1929 · נפ׳ 1/2021','אושוויץ→שטוטהוף (38444)→טורן; חולון'),
                 ('u','אברהם צדוק','יליד מקווה ישראל','הכירו במקווה ישראל, 1946'))
box(890, g4, PW, PH, 's', 'גדליהו (גיולה) רף', 'נ׳ 3.3.1931 · נפ׳ 2008', 'אסיר בוכנוולד 54982 · ⚭ יוכבד · ממקימי אילניה')
box(660, g4, PW, PH, 'm', 'גיטה (Gizela)', 'נ׳ 26.3.1936 · נפ׳ 1944', 'נרצחה באושוויץ, בת 8')
rach_x = 1290+32+PW/2
bus(bus4_y, 660, 1900)
for x in (1900, 1670, rach_x, 890, 660):
    drop(x, bus4_y, g4-PH/2)

# ---------------- Generation 5 ----------------
g5 = 1965
box(1900, g5, PW, 72, 'u', 'אורית · מרב', 'בנות דב', 'רמתיים')
drop(1900, g4+PH/2, g5-36)
box(1290, g5, PW, 72, 'u', 'עדו · זיו', 'בני רחל ואברהם', 'חולון')
drop(1290, g4+PH/2, g5-36)
box(890, g5, PW+70, 72, 'u', 'אריה (1955) · זאב (1964) · רבקה ("ריקה")', 'ילדי גדליהו ויוכבד · אילניה', 'ריקה: נ׳ 10.8.1958, נפלה בצה״ל 12.5.1977')
drop(890, g4+PH/2, g5-36)

# ---------------- Generation 6 ----------------
g6 = 2125
box(1290, g6, PW+110, 66, 'u', 'שישה נכדים לרחל ולאברהם', '"סבתא, ביום השואה אני אזמין אותך ואתגאה בך"', None)
drop(1290, g5+36, g6-33)

# ---------------- render ----------------
def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

parts=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="\'David Libre\',\'Frank Ruhl Libre\',Georgia,serif" direction="rtl">',
       f'<rect width="{W}" height="{H}" fill="#faf7f2"/>']
for d in lines:
    parts.append(f'<path d="{d}" fill="none" stroke="#a89d8a" stroke-width="1.9"/>')
for (x,y,w,h,fate,name,dates,sub,small) in boxes:
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{FILL[fate]}" stroke="{COL[fate]}" stroke-width="2"/>')
    subs = [] if not sub else (sub.split('|') if isinstance(sub,str) else list(sub))
    fs_n = 15.5 if small else 18
    fs_d = 12.5 if small else 14
    fs_s = 11 if small else 12.5
    n_lines = 2 + len(subs)
    lh = 17 if small else 20
    total = lh + len(subs)*14
    yy = y + h/2 - total/2 + 6
    parts.append(f'<text x="{x+w/2}" y="{yy:.0f}" text-anchor="middle" font-size="{fs_n}" font-weight="bold" fill="#2b2620">{esc(name)}</text>')
    yy += lh
    parts.append(f'<text x="{x+w/2}" y="{yy:.0f}" text-anchor="middle" font-size="{fs_d}" fill="#4a4238">{esc(dates)}</text>')
    for s in subs:
        yy += 14.5
        parts.append(f'<text x="{x+w/2}" y="{yy:.0f}" text-anchor="middle" font-size="{fs_s}" fill="#6a6154">{esc(s)}</text>')
for (x,y,txt) in labels:
    parts.append(f'<rect x="{x-len(txt)*3.9}" y="{y-13}" width="{len(txt)*7.8}" height="18" fill="#faf7f2"/>')
    parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="13" fill="#8a7a55" font-style="italic">{esc(txt)}</text>')
parts.append('</svg>')
svg='\n'.join(parts)

html=f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>העץ המלא — משפחת סטרולוביץ-רפפורט ופרקש</title>
<style>
 body{{margin:0; background:#faf7f2; font-family:"David Libre","Frank Ruhl Libre",Georgia,serif; color:#2b2620;}}
 .head{{text-align:center; padding:26px 12px 4px;}}
 .head h1{{font-size:1.65rem; margin:0 0 4px;}}
 .head .sub{{color:#8a8177; font-size:.95rem;}}
 .legend{{display:flex; gap:18px; justify-content:center; flex-wrap:wrap; padding:10px 0 2px; font-size:.85rem;}}
 .legend span{{display:flex; align-items:center; gap:6px;}}
 .dot{{width:11px; height:11px; border-radius:50%; display:inline-block;}}
 .chart{{margin:0 auto; padding:6px 10px 8px; overflow-x:auto;}}
 .chart svg{{min-width:1700px; width:100%; height:auto; display:block;}}
 .foot{{max-width:1100px; margin:0 auto; border-top:1px solid #d8d0c2; padding:12px 16px 40px; font-size:.78rem; color:#8a8177; text-align:center;}}
</style>
</head>
<body>
<div class="head">
  <h1>העץ המלא — משפחת סטרולוביץ-רפפורט ופרקש</h1>
  <div class="sub">כל בני המשפחה המתועדים, כולל ילדי גדליה רפפורט מכל נשותיו וילדי האחים · משפחתה של רחל צדוק (״רוצי״), 16.04.1929 וולובה — 01/2021 חולון · נערך 27.08.2026</div>
</div>
<div class="legend">
  <span><span class="dot" style="background:#a0392e"></span> נרצחו בשואה</span>
  <span><span class="dot" style="background:#3a7d44"></span> שרדו</span>
  <span><span class="dot" style="background:#b8860b"></span> רחל</span>
  <span><span class="dot" style="background:#8a8177"></span> נפטרו לפני/אחרי השואה, גורלם לא תועד — או בני הדורות שאחרי</span>
</div>
<div class="chart">
{svg}
</div>
<div class="foot">
  תאריכים: "נ׳" = נולד/ה, "נפ׳" = נפטר/ה (שנה בלבד כשהיום המדויק אינו ידוע; "?" = הערכה/טעון אימות; "ככה"נ" = ככל הנראה). ילדי האחים מצוינים בתוך תיבת ההורה († = נפטר/ה בינקות; שנות הלידה של ילדי מנדל וריבקה — 1933–1941, פירוט בפרק ג'). שנות נישואים מצוינות היכן שתועדו. צד האם: תאריכי כל 14 ילדי בצלאל ואסתר — מהרשומות האזרחיות של אזור דנילובו (פונד 1606, אופוס 13; חיפוש "Farkas", 18.08.2026).
  רפפורט שאול (חברת רפסודות העצים של אוקרמזו-מיידנקה) אינו בעץ: קשרו המשפחתי טרם הוכח; רשומת לידה מועמדת — "Soel", נ׳ 3.11.1873 במרמרוש-סיגט, בן יוסל ומרים רפפורט (מאגר לידות מרמרוש) — מרמזת דווקא על ענף סיגט.
  מקורות: הרשומות האזרחיות של מרמרוש (JewishGen, פונד 1606) · מפקד 1921 (Hungaricana) · יד ושם · ארולסן/שטוטהוף · עדות רחל (2009) · הפירוט המלא בדוח ובאינדקס.
</div>
</body>
</html>'''
import re as _re_bidi
# RTL guard: an en dash between digits reverses the two number runs; a hyphen does not
html = _re_bidi.sub(r'(\d)\u2013(\d)', r'\1-\2', html)
open('עץ_משפחה_מורחב.html','w',encoding='utf-8').write(html)
print('written', len(html))
