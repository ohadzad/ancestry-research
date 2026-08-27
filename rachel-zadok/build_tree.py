# -*- coding: utf-8 -*-
"""Strulovits-Rappaport family — classic drop-line descendant chart (v5, enlarged type).
Conventions: one box per person (name + birth-death years), spouses joined by a
horizontal marriage line labeled with the wedding year, drop line from each union
to a sibling bus, children in birth order (RTL: eldest right), oldest generation on top."""

W, H = 2400, 1840
COL  = {'m': '#a0392e', 's': '#3a7d44', 'r': '#b8860b', 'u': '#8a8177'}
FILL = {'m': '#fdf3f1', 's': '#f2f8f3', 'r': '#fdf6e3', 'u': '#f7f5f1'}

PW, PH = 210, 84      # person box
SW, SH = 220, 80      # small (sibling) box
boxes, lines, labels = [], [], []

def box(cx, cy, w, h, fate, name, dates, sub=None, small=False):
    boxes.append((cx-w/2, cy-h/2, w, h, fate, name, dates, sub, small))
    return cx, cy

def line(d): lines.append(d)
def mlabel(x, y, txt): labels.append((x, y, txt))

def couple(cx, cy, right, left, wed=None, gap=64, rw=None, lw=None):
    """right/left = (fate,name,dates,sub). Marriage line between boxes, label above."""
    rw = rw or PW; lw = lw or PW
    rx, lx = cx + gap/2 + rw/2, cx - gap/2 - lw/2
    box(rx, cy, rw, PH, right[0], right[1], right[2], right[3] if len(right)>3 else None)
    box(lx, cy, lw, PH, left[0],  left[1],  left[2],  left[3]  if len(left)>3 else None)
    line(f'M {rx-rw/2} {cy} H {lx+lw/2}')
    if wed: mlabel(cx, cy-PH/2-8, wed)
    return cx, cy

def elbow(x1, y1, x2, y2):
    my = (y1+y2)/2
    line(f'M {x1} {y1} V {my} H {x2} V {y2}')

def drop(x, y1, y2): line(f'M {x} {y1} V {y2}')
def bus(y, x1, x2): line(f'M {x1} {y} H {x2}')

# ---------------- Generation 0 ----------------
g0 = 110
c0 = couple(1620, g0, ('u','משה רפפורט','המאה ה-19','אוקרמזו'),
                      ('u','יֶנטה שפיגל','המאה ה-19', None))

# ---------------- Generation 1 ----------------
g1 = 330
c_leib = couple(2145, g1, ('u','לייב סטרולוביץ','המאה ה-19','קושלובו'),
                          ('u','ריבקה (נאיוביץ/שפשוביץ?)','המאה ה-19', None))
c_ged  = couple(1620, g1, ('u','גדליה רפפורט','נ׳ 1.4.1846 · נפ׳ 1908/9','בעל האחוזות של אוקרמזו'),
                          ('u','אסתר כץ','נפ׳/נפרדו לפני 1884','אשתו השנייה'))
mlabel(1500, g1+PH/2+20, 'נשא גם את ריבקה גרוסמן, ומ-6.8.1884 את מינדל ברקוביץ (1865 – לפני 8.1944)')
c_berl = couple(760, g1, ('u','ברל (דב) פרקש','המאה ה-19','דנילובו'),
                         ('u','גיטל','המאה ה-19', None))
c_stei = box(300, g1, PW, PH, 'u', 'משפחת שטיינר', 'קירלהאזה (קורולבו)', None)
elbow(1620, g0+PH/2, 1620, g1-PH/2)   # Moshe=Jenta -> Gedalia

# ---------------- Generation 2 ----------------
g2 = 570
c_yaak = couple(1875, g2, ('u','יעקב סטרולוביץ','נ׳ 15.1.1870 · נפ׳ 1945','שרד בהסתתרות; מת בחוסט'),
                          ('m','שרה רפפורט','נ׳ 1/1876 · נפ׳ 1944','נרצחה באושוויץ'),
                wed='נישואים דתיים, ~1892')
c_betz = couple(530, g2, ('m','בצלאל פרקש','נ׳ 1873 · נפ׳ 1944','נרצח באושוויץ'),
                         ('m','אסתר שטיינר','נ׳ 1879 · נפ׳ 1944','נרצחה באושוויץ'))
b_alad = box(1250, g2, SW, SH, 'u', 'אלדר רפפורט', 'נ׳ 11/1885', 'בן מינדל ברקוביץ; בנקאי — מנכ״ל הבנק הנאג׳סלשי')
elbow(1620, g1+PH/2, 1250, g2-SH/2)   # Gedalia -> Aladar box
yaak_rx = 1875+32+PW/2; sara_lx = 1875-32-PW/2
betz_rx = 530+32+PW/2;  este_lx = 530-32-PW/2
elbow(2145, g1+PH/2, yaak_rx, g2-PH/2)   # Leib -> Yaakov box
elbow(1620, g1+PH/2, sara_lx, g2-PH/2)   # Gedalia -> Sara box
elbow(760,  g1+PH/2, betz_rx, g2-PH/2)   # Berl -> Betzalel box
elbow(300,  g1+PH/2, este_lx, g2-PH/2)   # Steiner -> Ester box

# ---------------- Generation 3: Arye=Rivka + siblings ----------------
g3 = 830
c_ar = couple(1120, g3, ('m','אריה-לייב סטרולוביץ-רפפורט','נ׳ 3/1894 · נפ׳ 1944?','סוחר עורות; מת מרעב באושוויץ (עדות)'),
                        ('m','רבקה-רוזה פרקש','נ׳ 25.4.1904 · נפ׳ 1944','נרצחה באושוויץ 1944; המועד לא ידוע'),
              wed='⚭ (נישואים דתיים)', rw=250)
arye_x  = 1120+32+250/2   # 1277
rivro_x = 1120-32-PW/2    # 983

# Arye's 13 siblings (birth order, RTL eldest right) — three rows
sibA1 = [
 ('m','ריבקה (גדלוביץ)','נ׳ 1896 · נפ׳ 1944','אפשה; בתה אסתר שרדה'),
 ('m','אסתר','נ׳ 1897 · נפ׳ 1942',None),
 ('m','רחל (קליין)','נ׳ 1899 · נפ׳ 1944','מונקץ׳'),
 ('m','מנדל','נ׳ 1900 · נפ׳ 1944','⚭ רוחל הרשקוביץ, 1938'),
]
sibA2 = [
 ('m','גיטל (וולף)','נ׳ 1902 · נפ׳ 1944','⚭ אלכסנדר וולף, 1933'),
 ('u','סימה','נ׳ 1904','גורלה לא תועד'),
 ('m','יצחק','נ׳ 1905 · נפ׳ 1944','נספה במאוטהאוזן'),
 ('u','חיה','נ׳ 1907','גורלה לא תועד'),
]
sibA3 = [
 ('s','נתן','נ׳ 1908','שרד'),
 ('m','גדליה','נ׳ 1911','נרצח בשואה'),
 ('u','שרה (פוירוורקר)','נ׳ 1912','נאג׳בוצ׳קו'),
 ('s','פייגה (פאני, לבוביץ)','נ׳ 1914','תאומה; שרדה בהסתתרות'),
 ('s','פפי','נ׳ 1914','תאומה; שרדה; ככה"נ זו שנספתה בתאונה אחרי השחרור'),
]
busA_y = 690
line(f'M 1875 {g2+PH/2} V {busA_y}')          # from Yaakov=Sara union
rowA1_y, rowA2_y, rowA3_y = 820, 990, 1160
P = 240
xs1 = [2270 - i*P for i in range(len(sibA1))]
xs2 = [2270 - i*P for i in range(len(sibA2))]
xs3 = [2270 - i*P for i in range(len(sibA3))]
FEED = 2392
bus(busA_y, arye_x, FEED)               # bus spans Arye..feeder
drop(arye_x, busA_y, g3-PH/2)
for x,(f,n,d,s) in zip(xs1,sibA1):
    drop(x, busA_y, rowA1_y-SH/2); box(x, rowA1_y, SW, SH, f, n, d, s, small=True)
# feeder line at far right descends to second and third buses
busA2_y = rowA1_y + SH/2 + 35
drop(FEED, busA_y, busA2_y); bus(busA2_y, FEED, min(xs2))
for x,(f,n,d,s) in zip(xs2,sibA2):
    drop(x, busA2_y, rowA2_y-SH/2); box(x, rowA2_y, SW, SH, f, n, d, s, small=True)
busA3_y = rowA2_y + SH/2 + 35
drop(FEED, busA2_y, busA3_y); bus(busA3_y, FEED, min(xs3))
for x,(f,n,d,s) in zip(xs3,sibA3):
    drop(x, busA3_y, rowA3_y-SH/2); box(x, rowA3_y, SW, SH, f, n, d, s, small=True)

# Rivka-Roza's 5 siblings (left side) — two rows
sibB1 = [
 ('m','גולדה-ארנקה (פוקס)','נ׳ 1899 · נפ׳ 1944','וישק; לילי ושרה שרדו'),
 ('m','אליהו','נ׳ 1901 · נפ׳ 1944','+4 ילדיו'),
 ('m','זיסל-לייב','נ׳ 1906 · נפ׳ 1944',None),
]
sibB2 = [
 ('m','חנה','נ׳ 1909 · נפ׳ 1944','חוסט'),
 ('m','רחל','נ׳ 1913 · נפ׳ 1944/5','אורמזובה'),
]
busB_y = 690
line(f'M 530 {g2+PH/2} V {busB_y}')
xsB1 = [740 - i*P for i in range(len(sibB1))]   # 740,500,260
xsB2 = [740 - i*P for i in range(len(sibB2))]   # 740,500
FEEDB = 136
bus(busB_y, rivro_x, FEEDB)
drop(rivro_x, busB_y, g3-PH/2)
for x,(f,n,d,s) in zip(xsB1,sibB1):
    drop(x, busB_y, rowA1_y-SH/2); box(x, rowA1_y, SW, SH, f, n, d, s, small=True)
busB2_y = rowA1_y + SH/2 + 35
drop(FEEDB, busB_y, busB2_y); bus(busB2_y, FEEDB, max(xsB2))
for x,(f,n,d,s) in zip(xsB2,sibB2):
    drop(x, busB2_y, rowA2_y-SH/2); box(x, rowA2_y, SW, SH, f, n, d, s, small=True)
mlabel(440, rowA2_y+SH/2+28, 'ועוד שמונה: מנדל (1897) והרמן (1918) — גורלם לא נודע; שישה מתו בילדותם (בעץ המלא)')

# ---------------- Generation 4: the five children ----------------
g4 = 1400
bus4_y = 1300
line(f'M 1120 {g3+PH/2} V {bus4_y}')
d_dov  = box(1900, g4, PW, PH, 's', 'דב', 'נ׳ 1924? · נפ׳ 1998', 'פרטיזנים; רמתיים')
d_sima = box(1670, g4, PW, PH, 'm', 'סימה (Sari)', 'נ׳ 26.12.1926 · נפ׳ 1944/5', 'מתה בשטוטהוף (עדות), אסירה 38443')
c_rach = couple(1290, g4, ('r','רחל ("רוצי")','נ׳ 16.4.1929 · נפ׳ 1/2021','אושוויץ→שטוטהוף (38444)→טורן; חולון'),
                          ('u','אברהם צדוק','יליד מקווה ישראל','הכירו במקווה ישראל, 1946'))
d_ged  = box(890, g4, PW, PH, 's', 'גדליהו (גיולה) רף', 'נ׳ 3.3.1931 · נפ׳ 2008', 'אסיר בוכנוולד 54982 · ⚭ יוכבד · ממקימי אילניה')
d_gita = box(660, g4, PW, PH, 'm', 'גיטה', 'נ׳ 26.3.1936 · נפ׳ 1944', 'נרצחה באושוויץ, בת 8')
rach_x = 1290+32+PW/2
bus(bus4_y, 660, 1900)
for x in (1900, 1670, rach_x, 890, 660):
    drop(x, bus4_y, g4-PH/2)

# ---------------- Generation 5 ----------------
g5 = 1620
e1 = box(1900, g5, PW, 72, 'u', 'אורית · מרב', 'בנות דב', 'רמתיים')
line(f'M 1900 {g4+PH/2} V {g5-36}')
e2 = box(1290, g5, PW, 72, 'u', 'עדו · זיו', 'בני רחל ואברהם', 'חולון')
line(f'M 1290 {g4+PH/2} V {g5-36}')
e3 = box(890, g5, PW+70, 72, 'u', 'אריה (1955) · זאב (1964) · רבקה ("ריקה")', 'ילדי גדליהו ויוכבד · אילניה', 'ריקה: נ׳ 10.8.1958, נפלה בצה״ל 12.5.1977')
line(f'M 890 {g4+PH/2} V {g5-36}')

# ---------------- Generation 6 ----------------
g6 = 1780
f1 = box(1290, g6, PW+110, 66, 'u', 'שישה נכדים לרחל ולאברהם', '"סבתא, ביום השואה אני אזמין אותך ואתגאה בך"', None)
line(f'M 1290 {g5+36} V {g6-33}')

# ---------------- render ----------------
def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

parts=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="\'David Libre\',\'Frank Ruhl Libre\',Georgia,serif" direction="rtl">',
       f'<rect width="{W}" height="{H}" fill="#faf7f2"/>']
for d in lines:
    parts.append(f'<path d="{d}" fill="none" stroke="#a89d8a" stroke-width="1.9"/>')
for (x,y,w,h,fate,name,dates,sub,small) in boxes:
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{FILL[fate]}" stroke="{COL[fate]}" stroke-width="2"/>')
    fs_n = 17 if small else 18
    fs_d = 13.5 if small else 14
    fs_s = 12 if small else 12.5
    n_lines = 2 + (1 if sub else 0)
    yy = y + h/2 - (n_lines-1)*9.5 + 5 - (2 if n_lines==3 else 0)
    parts.append(f'<text x="{x+w/2}" y="{yy:.0f}" text-anchor="middle" font-size="{fs_n}" font-weight="bold" fill="#2b2620">{esc(name)}</text>')
    yy += 20
    parts.append(f'<text x="{x+w/2}" y="{yy:.0f}" text-anchor="middle" font-size="{fs_d}" fill="#4a4238">{esc(dates)}</text>')
    if sub:
        yy += 17
        parts.append(f'<text x="{x+w/2}" y="{yy:.0f}" text-anchor="middle" font-size="{fs_s}" fill="#6a6154">{esc(sub)}</text>')
for (x,y,txt) in labels:
    parts.append(f'<rect x="{x-len(txt)*3.9}" y="{y-13}" width="{len(txt)*7.8}" height="18" fill="#faf7f2"/>')
    parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="13" fill="#8a7a55" font-style="italic">{esc(txt)}</text>')
parts.append('</svg>')
svg='\n'.join(parts)

html=f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>עץ המשפחה — רחל צדוק לבית סטרולוביץ-רפפורט</title>
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
  <h1>עץ משפחת סטרולוביץ-רפפורט ופרקש</h1>
  <div class="sub">משפחתה של רחל צדוק (״רוצי״), 16.04.1929 וולובה — 01/2021 חולון · שבעה דורות · קו הנישואין מסומן בין בני זוג, וילדים תלויים מקו האחים לפי סדר לידה · נערך 27.08.2026</div>
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
  תאריכים: "נ׳" = נולד/ה, "נפ׳" = נפטר/ה (שנה בלבד כשהיום המדויק אינו ידוע; "?" = הערכה/טעון אימות; "ככה"נ" = ככל הנראה). שנות נישואים מצוינות היכן שתועדו (גיטל–וולף 1933, מנדל–רוחל 1938, גדליה–מינדל 1884); שנת נישואי יעקב ושרה (~1892) היא אומדן מלידת הבכור.
  מטעמי מקום אין העץ מציג את שאר ילדי גדליה רפפורט (שיינדל — מריבקה גרוסמן; נתן — אחיה המלא של שרה, בן אסתר כץ; יוסף-דוד, ברטה, פרידריקה, זלמן, הרמן ומאיר — אחיו המלאים של אלדר ממינדל ברקוביץ) — פירוטם בפרק ב' של הדוח. רפפורט שאול (חברת רפסודות העצים של אוקרמזו-מיידנקה) אינו בעץ: קשרו המשפחתי המדויק טרם הוכח ברשומות.
  מקורות: הרשומות האזרחיות של מרמרוש (JewishGen, פונד 1606) · מפקד 1921 (Hungaricana) · יד ושם · ארולסן/שטוטהוף · עדות רחל (2009) · הפירוט המלא בדוח ובאינדקס.
</div>
</body>
</html>'''
import re as _re_bidi
# RTL guard: an en dash between digits reverses the two number runs; a hyphen does not
html = _re_bidi.sub(r'(\d)\u2013(\d)', r'\1-\2', html)
open('עץ_משפחה_גרפי.html','w',encoding='utf-8').write(html)
print('written', len(html))
