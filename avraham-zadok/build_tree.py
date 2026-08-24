# -*- coding: utf-8 -*-
"""עץ משפחת צדוק–פריינטה — מקווה ישראל. SVG ידני, RTL. פלט: tree.html
שבע שכבות: שושלת ארואס (שלמה→יוסף→מרים) ומשפחת פריינטה (אברהם→יצחק פפו),
משפחת צדוק/צאלח (אברהם צאלח∞סעדה→אהרון), האחיות פריינטה, ילדי רוזה ואהרון,
ואברהם ∞ רחל ובניהם."""
import html
import re as _re
_line4 = open('report.md', encoding='utf-8').read().split(chr(10))[3]
_m = _re.findall(r'מהדורה (\d+)', _line4)
TREE_ED = _m[0] if _m else '?'
import datetime as _dt, os as _os
_os.environ.setdefault('TZ','Asia/Jerusalem')
try:
    import time as _t; _t.tzset()
except Exception:
    pass
BUILD_STAMP = _dt.datetime.now().strftime('%d.%m.%Y, %H:%M')

W, H = 1648, 1000
DX = 140  # global left-shift: trims the dead left margin (gen-label column was 256px wide)
BW, BH = 184, 66
GAP = 208  # couple center-to-center

def esc(s): return html.escape(s, quote=True)

def box(cx, y, name, sub, cls="person", w=BW, h=BH):
    cx = cx - DX
    left = cx - w/2
    tsp = "".join(f'<tspan x="{cx}" y="{y+38+i*14}">{esc(ln)}</tspan>' for i,ln in enumerate(sub.split("|")) if ln)
    return (f'<g class="{cls}"><rect x="{left}" y="{y}" width="{w}" height="{h}" rx="8"/>'
            f'<text class="nm" x="{cx}" y="{y+23}" text-anchor="middle">{esc(name)}</text>'
            f'<text class="sb" text-anchor="middle">{tsp}</text></g>')

def hline(x1,x2,y,c="ln"): return f'<line class="{c}" x1="{x1-DX}" y1="{y}" x2="{x2-DX}" y2="{y}"/>'
def vline(x,y1,y2,c="ln"): return f'<line class="{c}" x1="{x-DX}" y1="{y1}" x2="{x-DX}" y2="{y2}"/>'

def couple(cx, y, rname, rsub, lname, lsub, cls, c="ln"):
    """rname on the right (cx+GAP/2), lname on the left. Returns union x=cx."""
    r, l = cx+GAP/2, cx-GAP/2
    s = box(r, y, rname, rsub, cls) + box(l, y, lname, lsub, cls)
    s += hline(r-BW/2, l+BW/2, y+BH/2, c)   # marriage line
    return s, cx

def connect(xu, ytop, xc, ychild, c="ln"):
    """orthogonal drop from a union point (xu,ytop) to a child box top (xc,ychild)."""
    ym = (ytop+ychild)/2
    return vline(xu, ytop, ym, c) + hline(xu, xc, ym, c) + vline(xc, ym, ychild, c)

S=[f'<svg id="famtree" role="img" aria-labelledby="famtree-t famtree-d" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial, sans-serif" direction="rtl">']
S.append('<title id="famtree-t">עץ משפחת צדוק–פריינטה — שבע שורות דורות</title>'
         '<desc id="famtree-d">תרשים שושלת בשבע שורות. בראש: שלמה ושמחה ארואץ (ילידי גיברלטר, מפקד יפו 1855) '
         'ולצדם ענף אלעזר ומסודה, וכן משפחת צאלח מצנעא. משם: יוסף וגרסיה ארואס ואחיו משה ואליהו; '
         'הסבים יצחק פפו פריינטה ומרים ארואס מזה ואברהם וסעדה צדוק מזה; ההורים אהרון צדוק ושושנה רוזה פריינטה '
         'ואחיהם; חמשת ילדיהם ובהם אברהם צדוק (נושא המחקר); ואברהם ורחל ושני בניהם.</desc>')
S.append('''<style>
 #famtree rect.bg{fill:#ffffff;stroke:none}
 #famtree g rect{fill:#fbf7ef;stroke:#8a6d3b;stroke-width:1.8}
 #famtree .person rect{fill:#fdfaf3;stroke:#8a6d3b}
 #famtree .subject rect{fill:#f4d58d;stroke:#b8860b;stroke-width:3}
 #famtree .parent rect{fill:#eef3f7;stroke:#3b6d8a}
 #famtree .frainte rect{fill:#e9f3f1;stroke:#3b7a6d}
 #famtree .arwas rect{fill:#eaf0f6;stroke:#4a6fa5}
 #famtree .zadok rect{fill:#f6efe6;stroke:#a5764a}
 #famtree .misc rect{fill:#f4f1ea;stroke:#857a61;stroke-dasharray:4 4}
 #famtree .unk rect{fill:#f2f2f0;stroke:#7d7d7d;stroke-dasharray:4 4}
 #famtree .nm{font-size:14px;font-weight:700;fill:#2b2b2b}
 #famtree .sb{font-size:10.5px;fill:#555}
 #famtree .frainte .nm{fill:#204f45}#famtree .arwas .nm{fill:#243f66}#famtree .zadok .nm{fill:#6b4423}
 #famtree .misc .nm,#famtree .unk .nm{font-size:12px;font-weight:400;fill:#6b5f45}
 #famtree .ln{stroke:#8a6d3b;stroke-width:1.8;fill:none}
 #famtree .my{fill:#8a6508;font-size:10px;font-weight:700}
 #famtree .mybg{fill:#ffffff;stroke:none}
 #famtree .gen{fill:#7a7156;font-size:12px;font-weight:700}
 #famtree .rootln{stroke:#8a6d3b;stroke-width:1.6;fill:none;stroke-dasharray:5 4;opacity:.75}
</style>''')
S.append(f'<rect class="bg" x="0" y="0" width="{W}" height="{H}"/>')

# rows (top = oldest)
yGG, yG, y0, y1, y2, y3, y4 = 34, 168, 302, 452, 610, 758, 896

# ---- Arwas family origin (row yGG): Shlomo Arwas (probable father of Yosef) ----
c_gg = 1100
s,_ = couple(c_gg, yGG, "שלמה ארואץ (ארואס)", "~1823 גיברלטר · עלה 1833 / רישום 1839|בנקאי 1855 · חלפן (פנקס הקונסוליה)|נפ׳ יפו 1868?", "שמחה ארואץ", "אם יוסף|(מפקד מונטיפיורי 1855)", "arwas"); S.append(s)
S.append(box(620, yGG, "משפחת צאלח — צנעא, תימן", "צורפים מדורי דורות|רבנים, דיינים ומחברים", "unk", w=300))
# ---- Elazar Aruets branch (row yGG, right): probable brother of Shlomo (census 1855) ----
c_el = 1566
s,_ = couple(c_el, yGG, "אלעזר ארואץ", "~1831 גיברלטר · עלה 1833|כותנה 1855 · מזרנים (פנקס), יפו", "מסודה ארואץ", "אשת אלעזר|(מפקד מונטיפיורי 1855)", "arwas"); S.append(s)
# dashed "brothers" tie between the two couples
S.append(hline(c_gg+GAP/2+BW/2, c_el-GAP/2-BW/2, yGG+BH/2, "rootln"))
_bx = (c_gg+GAP/2+BW/2 + c_el-GAP/2-BW/2)/2 - DX
S.append(f'<rect class="mybg" x="{_bx-22}" y="{yGG+BH/2-9}" width="44" height="15"/>')
S.append(f'<text class="my" x="{_bx}" y="{yGG+BH/2+3}" text-anchor="middle">אחים?</text>')

# ---- great-grandparents (row yG): Yosef∞Garcia Arwas ; Avraham Frainte ----
c_ag = 1100
s,_ = couple(c_ag, yG, "יוסף ארואס", "~1845 (1869) · «41» ב-1893 · צראף|טופס 1893: «בן Solomon Arwas»", "גרסיה ארואס", "אם מרים · ב-1893 רשומה שרה (29)", "arwas"); S.append(s)
x_avf = 1440
S.append(box(x_avf, yG, "אברהם פריינטה", "אבי יצחק פפו", "frainte"))
# dashed origin connector -> Yosef∞Garcia union (family origin, not proven parentage)
S.append(connect(c_gg, yGG+BH, c_ag, yG, "rootln"))
# ---- Yosef's brothers (census 1855): Moshe & Eliahu — sibling bus from Shlomo∞Simha union ----
moshe_c, elia_c = 842, 712
ar_bus = (yGG+BH+yG)/2
S.append(hline(elia_c, c_gg, ar_bus, "ln"))
S.append(vline(moshe_c, ar_bus, yG, "ln")); S.append(vline(elia_c, ar_bus, yG, "ln"))
S.append(box(moshe_c, yG, "משה · מיכאל", "בני שלמה|משה ~1849|(מפקד 1855)|מיכאל ~1864|«בן שלום/שלמה»|1895 · 1904 · 1906", "arwas", w=112, h=124))
S.append(box(elia_c, yG, "אליהו ארואץ", "~1852 · בן שלמה (1893)|חלפן יפו 1873 → עזה|«השקפה» 1904 · נפ׳ 1906?", "arwas", w=162, h=82))
gaza_c = 428
S.append(box(gaza_c, yG, "בית אליהו בעזה — 1893", "תעודת נתין בריטי 24, קונסוליית יפו|«Father’s Name: Shalom Arrwas (dead)»|רעייתו פרו (36)|משה 17 · רחל 14 · מרים 12|סולטנה 10 · יעקב 4 · שלמה 2", "arwas", w=286, h=118))
S.append(hline(gaza_c+143, elia_c-81, yG+33, "ln"))
# ---- Elazar & Mesoda's sons (census 1855) ----
elsons_c = 1662
S.append(connect(c_el, yGG+BH, elsons_c, yG, "ln"))
S.append(box(elsons_c, yG, "בני אלעזר", "יוסף אליהו (~1856) · רחמים (~1864) · יעקב (~1865)|תעודה 12, יפו 12.1.1904: «בן Eliazar»|ובהערות הפקיד: «Orig. from Gibraltar»|בנו אזר (21) נרשם בעזה חודש אחר כך|יעקב ורחמים — «בן Azor/Azar» בטפסי 1896-1912", "misc", w=244, h=112))

# ---- grandparents (row y0): Yitzhak Pepo ∞ Miriam ; Avraham Tzalach ∞ Saada ----
c_m = 1252   # maternal grandparents union
s,_ = couple(c_m, y0, "יצחק (פפו) פריינטה", "~1860/62 ירושלים - 31.12.1944 (כהן: 1942?)|מדור מייסדי מקווה ישראל", "מרים ארואס", "~1875 יפו - ז׳ תמוז תרע״ו (1916)|קבורה בטרומפלדור", "frainte"); S.append(s)
c_p = 620    # paternal grandparents union
s,_ = couple(c_p, y0, "אברהם צדוק (צאלח)", "נפטר בעדן ~1900", "סעדה צדוק (צאלח)", "נספתה ברעב צנעא 1904", "zadok"); S.append(s)
S.append(connect(620, yGG+BH, c_p, y0, "rootln"))
# connectors into grandparents; Yosef∞Garcia -> sibling bus (Miriam + her brother Shlomo)
shby_c = 940
ar2_bus = (yG+BH+y0)/2
S.append(vline(c_ag, yG+BH, ar2_bus, "ln"))
S.append(hline(shby_c, c_m-GAP/2, ar2_bus, "ln"))
S.append(vline(c_m-GAP/2, ar2_bus, y0, "ln"))              # -> Miriam (left box)
S.append(vline(shby_c, ar2_bus, y0, "ln"))                 # -> Shlomo b. Yosef
S.append(box(shby_c, y0, "שלמה ארואס (בן יוסף)", "~1875? · רישומי הקונסוליה 1902-03|ע״ש סבו (ככל הנראה) · בנו יוסף ~1910", "arwas", w=196))
S.append(connect(x_avf, yG+BH, c_m+GAP/2, y0, "ln"))       # Avraham Frainte -> Yitzhak (right box)

# ---- parents' generation (row y1): Frainte siblings + Aharon ----
roza_c, hana_c, vict_c, flor_c, mfr_c, bros_c = 860, 1035, 1185, 1335, 1495, 1672
S.append(box(bros_c, y1, "יוסף · רפאל · אברהם", "אחים נוספים (מתוך 9)", "misc", w=168))
S.append(box(mfr_c, y1, "משה פרינטה", "בן יצחק · נשוי לרבקה (בת דניאל?)|פנקס הבוגרים ת״א 1944", "frainte", w=160))
S.append(box(flor_c, y1, "פלורין", "לימים בלומברג", "frainte", w=138))
S.append(box(vict_c, y1, "ויקטוריה", "לימים בכר", "frainte", w=138))
S.append(box(hana_c, y1, "חנה", "לבית פריינטה|(גרסיה ביטרן)", "frainte", w=138))
S.append(box(roza_c, y1, "שושנה רוזה", "לבית פריינטה · 31.12.1902 - 3.4.1979|אם אברהם · קבורה בחולון לצד אהרון", "parent"))
aharon_c = 596
S.append(box(aharon_c, y1, "אהרון צדוק", "~1895 - 18.11.1981 · יליד צנעא|עלה 1914 · אופה ומזכיר הפועלים|קבור בחולון", "parent"))
# maternal grandparents union -> sibling bus
sib_bus = y1-34
S.append(vline(c_m, y0+BH, sib_bus, "ln"))
S.append(hline(roza_c, bros_c, sib_bus, "ln"))
for c in (roza_c,hana_c,vict_c,flor_c,mfr_c,bros_c): S.append(vline(c, sib_bus, y1, "ln"))
# paternal grandparents union -> Aharon; + Aharon's siblings (perished, Sana'a 1904)
S.append(connect(c_p, y0+BH, aharon_c, y1, "ln"))
tzs_c = 400
tz_bus = (y0+BH+y1)/2
S.append(hline(tzs_c, c_p, tz_bus, "ln"))
S.append(vline(tzs_c, tz_bus, y1, "ln"))
S.append(box(tzs_c, y1, "יוסף, אחיו הצעיר של אהרון", "נספה ברעב צנעא תרס״ד (1904)|עם אמו · השם — ספר המשפחה", "unk", w=176))
# marriage Roza ∞ Aharon
un_p = (roza_c-BW/2 + aharon_c+BW/2)/2
S.append(hline(aharon_c+BW/2, roza_c-BW/2, y1+BH/2, "ln"))
S.append(f'<rect class="mybg" x="{un_p-DX-31}" y="{y1+BH/2-16}" width="62" height="14"/>')
S.append(f'<text class="my" x="{un_p-DX}" y="{y1+BH/2-5}" text-anchor="middle">מקווה ישראל</text>')

# ---- children of Roza & Aharon (row y2) ----
kids=[("יעל","1923 - 9.8.1996|∞ בן-ציון פרחי · 1943","person"),("מרים","«קיקה» · 1927? · חוקוק","person"),
      ("אברהם צדוק","נ׳ 16.9.1925* · נפ׳ 2017|פלמ״ח / קרייתי","subject"),
      ("איציק","(יצחק) · 1933?","person"),("יוסי","(יוסף) · 1948?","person")]
kg=196; kcs=[un_p+2*kg-i*kg for i in range(5)]
ch_bus=y2-34
S.append(vline(un_p, y1+BH/2, ch_bus, "ln"))
S.append(hline(min(kcs),max(kcs),ch_bus,"ln"))
for (nm,sb,cls),c in zip(kids,kcs):
    S.append(vline(c, ch_bus, y2, "ln")); S.append(box(c, y2, nm, sb, cls))

# ---- Avraham ∞ Rachel (row y3) ----
av_c=kcs[2]
S.append(vline(av_c, y2+BH, y3+BH/2, "ln"))
rch_c=av_c-232
S.append(box(rch_c, y3, "רחל צדוק", "לבית רפפורט/פרקש|ניצולת שואה · 1950","person"))
S.append(hline(rch_c+BW/2, av_c, y3+BH/2, "ln"))   # reaches Avraham's drop-line at av_c (was av_c-BW/2 → 92px gap)
un3=(rch_c+BW/2+av_c)/2
S.append(f'<rect class="mybg" x="{un3-DX-16}" y="{y3+BH/2-16}" width="32" height="14"/>')
S.append(f'<text class="my" x="{un3-DX}" y="{y3+BH/2-5}" text-anchor="middle">1950</text>')
# ---- sons (row y4) ----
sc=[un3+104,un3-104]; s_bus=y4-30
S.append(vline(un3, y3+BH/2, s_bus,"ln")); S.append(hline(min(sc),max(sc),s_bus,"ln"))
for nm,c in zip(("עדו","זיו"),sc):
    S.append(vline(c,s_bus,y4,"ln")); S.append(box(c,y4,nm,"","person",w=152,h=56))

# ---- annex (editions 43-50): documented relatives whose exact link is still open ----
S.append(f'<text class="gen" x="1020" y="754" text-anchor="middle">{esc("שכבות שנוספו במהדורות 43-55 — מתועדים ברשומת מדינה, החוליה לעץ עדיין פתוחה")}</text>')
S.append(box(1000, 768, "שלושה בני שלמה ארואס — 1916-1944", "מרקו · צפניה 43 ירושלים תש״ח · «בן שלמה»|אלי · ירושלים 1944 ומפקד תש״ז · «בן שלמה»|— שניהם מרשומה מפורשת —|משה החייט · נווה שלום ת״א · נתין בריטי|בנו נקרא שלמה 1931 ⇒ אביו שלמה (ככל הנראה)|אחים? — טעון אימות", "unk", w=300, h=120))
S.append(box(1330, 768, "אברהם פריינטה — ירושלים 1948", "מפקד תש״ח, נחלת שבעה · «בית מכלוף»|בן 58 ⇒ יליד ~1890 · אשתו בוקס (45)|השערה: בן שמואל, אחיו של יצחק פפו|— דור האחיינים · טעון אימות", "unk", w=300, h=112))
S.append(f'<text class="gen" x="1495" y="754" text-anchor="middle">{esc("ענף מתועד — רק הזיהוי האחרון פתוח")}</text>')
S.append(box(1635, 768, "הענף שנשאר במצרים — 1904-1950", "רפאל בן מיכאל · יליד יפו ~1904|(טופס 33, יפו 31.1.1906 — «Raphael, 2»)|היה כבן עשר בגירוש נתיני בריטניה 1914|בניו שמעון (1934) ויוסף (1935) — קהיר|«שם האב: רפאל» · עלו ארצה 1950|זיהוי האב — ככל הנראה", "arwas", w=284, h=120))

# generation labels (far left)
for y,txt in [(yGG,"דור 6 · המוצא"),(yG,"דור 5"),(y0,"סבים וסבתות"),
              (y1,"ההורים"),(y2,"אברהם ואחיו"),(y3,"נישואין"),(y4,"בנים")]:
    S.append(f'<text class="gen" x="56" y="{y+BH/2}" text-anchor="middle">{esc(txt)}</text>')

for i,ln in enumerate([
  '* 16.9.1925 — מ-MyHeritage; עץ כהן (2005): 19.9.1925 — פער 3 ימים, טעון אימות (שנת 1925 מאומתת בכרטיס הפלמ״ח) · «נפ׳ ...?» — תאריכי פטירה מועמדים מגאון 1938',
  'אמה של רוזה — מרים ארואס (מאומת: דף הרישום והמצבה; ראו מקרא) · שימו לב: מרים ארואס ילידת ~1881 שבבית עזה היא אדם אחר']):
    S.append(f'<text class="sb" x="{W/2}" y="{H-26+i*15}" text-anchor="middle">{esc(ln)}</text>')
S.append('</svg>')
SVG="\n".join(S)

html_doc=f'''<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>עץ משפחת צדוק–פריינטה — מקווה ישראל</title>
<style>
 :root{{--ink:#2b2b2b;--soft:#6b5a3a;--line:#d8ccb0;--gold:#8a5a00}}
 body{{background:#f3efe6;margin:0;font-family:Arial,sans-serif;color:var(--ink)}}
 header{{padding:20px 18px 6px;text-align:center}} h1{{margin:0;font-size:22px}}
 .sub{{color:var(--soft);font-size:13.5px;margin-top:4px;max-width:62ch;margin-inline:auto;line-height:1.6}}
 .wrap{{overflow-x:auto;-webkit-overflow-scrolling:touch;padding:12px}}
 .wrap:focus-visible{{outline:3px solid var(--gold);outline-offset:-3px}}
 svg{{min-width:1240px;max-width:{W}px;width:100%;height:auto;display:block;margin:0 auto;background:#fff;border:1px solid var(--line);border-radius:12px}}
 .legend{{max-width:74ch;margin:14px auto;background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 20px;font-size:13px;line-height:1.75}}
 .legend h2{{font-size:14.5px;margin:16px 0 4px;color:#5a4620;border-bottom:1px solid var(--line);padding-bottom:3px}}
 .legend h2:first-of-type{{margin-top:4px}}
 .legend p{{margin:6px 0}}
 .legend ul{{margin:6px 0;padding-inline-start:20px}} .legend li{{margin:3px 0}}
 .sw{{display:inline-block;width:15px;height:11px;border-radius:3px;vertical-align:middle;margin-left:6px;border:1px solid #8a6d3b}}
 a{{color:#7a4f12}} a:focus-visible{{outline:3px solid var(--gold);outline-offset:2px;border-radius:3px}}
 .backlink{{font-size:13.5px;margin:6px 0 2px}} .backlink a{{color:#7a4f12}}
 .printnote{{display:none}}
 @media print{{.printnote{{display:block;font-size:8pt;color:#5a4620;margin-top:4px}}}}
 footer{{text-align:center;color:#6f6045;font-size:12px;padding:10px}}
 @media (max-width:640px){{
   header{{padding:16px 14px 4px}} h1{{font-size:19px}} .wrap{{padding:8px 0}}
   .legend{{margin:12px 10px;padding:12px 14px;font-size:12.5px;border-radius:8px}}
 }}
 @media print{{
   @page{{size:A4 landscape;margin:12mm}}
   body{{background:#fff}} header{{padding:0;text-align:start}} h1{{font-size:12pt;margin:0}}
   .sub{{display:none}} .backlink{{display:none}}
   .wrap{{overflow:visible;padding:0;margin:0}}
   svg{{min-width:0!important;width:100%!important;max-width:none!important;border:none}}
   .legend{{max-width:none;border:none;padding:0;font-size:10.5px;line-height:1.5;break-before:page}}
   footer{{color:#444}}
 }}
</style></head><body>
<header><h1>עץ משפחת צדוק–פריינטה — מקווה ישראל</h1>
<div class="backlink"><a href="אברהם-צדוק.html">← חזרה למאמר המלא</a> · <a href="אברהם-צדוק.html#sources">רשימת המקורות</a></div>
<div class="sub">שבע שורות דורות — משלמה ושמחה ארואץ (גיברלטר ליפו, מפקד 1855) וממשפחת צאלח (צנעא) ועד בני אברהם. במסך צר: גללו לצדדים לתצוגה מלאה.</div></header>
<div class="wrap" tabindex="0" role="group" aria-label="תרשים עץ המשפחה — ניתן לגלול לצדדים">{SVG}</div>
<div class="printnote">התרשים מודפס על גיליון A4 לרוחב. לעותק גדול וקריא יותר: הדפיסו על גיליון A3, או הגדילו את התצוגה במסך.</div>
<div class="legend">
 <h2>מקרא הצבעים</h2>
 <p>
 <span class="sw" style="background:#f4d58d;border-color:#b8860b"></span> אברהם (נושא המחקר) &nbsp;·&nbsp;
 <span class="sw" style="background:#eef3f7;border-color:#3b6d8a"></span> ההורים (רוזה ואהרון) &nbsp;·&nbsp;
 <span class="sw" style="background:#e9f3f1;border-color:#3b7a6d"></span> פריינטה &nbsp;·&nbsp;
 <span class="sw" style="background:#eaf0f6;border-color:#4a6fa5"></span> ארואס (Arwas) &nbsp;·&nbsp;
 <span class="sw" style="background:#f6efe6;border-color:#a5764a"></span> צדוק / צאלח (תימן) &nbsp;·&nbsp;
 <span class="sw" style="background:#fbf7ef"></span> בני המשפחה.<br>
 קו מלא — קשר מתועד. קו מקווקו — קשר משוער או מסגרת־מוצא. סימן «?» אחרי תאריך — מועמד שטרם אומת.
 </p>

 <h2>מה נוסף במהדורות 43-55</h2>
 <ul>
  <li><b>ענף עזה.</b> תעודת רישום נתין בריטי מס' 24 (קונסוליית יפו, 10.4.1893) נוקבת בשדה «Father's Name»: <b>Shalom Arrwas (dead)</b> — ובכך מזהה את אליהו שבעזה כבנו של שלמה מגיברלטר. אתו נרשמו רעייתו <b>פרו</b> ושישה ילדים. אליהו זה הוא «האדון אליהו ארואץ» שידיעת «השקפה» מ-15.4.1904 מתארת כשולט בעדת עזה.</li>
  <li><b>הענף המקביל.</b> תעודה 25, מאותו יום: <b>Joseph Eliaho</b> בן <b>אלעזר</b>, סוחר בעזה — בן-דודו של אליהו, והוא החתום על מכתב התלונה נגדו. הידיעה מתעדת אפוא סכסוך בתוך המשפחה.</li>
  <li><b>ינואר 1904, יפו.</b> תעודה 11 מזהה את <b>מיכאל</b> כבן נוסף של שלמה — ובכך שלושת האחים שבספר המשפחה (יוסף, מיכאל, אליהו) עומדים כולם ברשומות בנות-זמנן; ותעודה 12, של יוסף אליהו בן אלעזר, נושאת בהערות הפקיד את המילים <b>«Orig. from Gibraltar»</b> — המקור השלישי והמפורש למוצא.</li>
  <li><b>נספח בתחתית העץ.</b> שני מתועדים ברשומת מדינה שהחוליה שלהם לעץ עדיין פתוחה: <b>מרקו ארוואס</b> (יליד מצרים 1916, «שם האב: שלמה») ו<b>אברהם פריינטה</b> (ירושלים 1948, בן 58 ⇒ יליד ~1890). שניהם מוצגים במסגרת מקווקוות ובדירוג «טעון אימות».</li>
  <li><b>ילדיהם של האחים (מהדורה 54).</b> טפסי הקונסוליה נוקבים גם בבני הבית. אצל <b>מיכאל בן שלום</b> ביפו: 1895 — רעייתו <b>רחל</b> (30), <b>בן ציון</b> (7) ו<b>פרידה</b> (4); 1903 — רעייתו <b>אטה</b> (20), בן ציון (14), פרידה (11), <b>רבקה</b> (6), <b>רחל</b> (3) ו<b>יוסף</b> (1). ו-1906 מוסיף ילד שישי, <b>רפאל</b> (2) — ילדיו במלואם: בן ציון, פרידה, רבקה, רחל, יוסף ורפאל. ואצל <b>אליהו</b> בעזה, 1893: פרו, משה, רחל, מרים, סולטנה, יעקב ושלמה. <b>תבנית שחוזרת בשני הבתים, והפקיד כתב אותה במפורש ב-1906 — «Eta age 23 — Wife 2nd»:</b> גיל הרעיה נמוך מכדי שתהיה אמם של הבכורים, מפני שהקונסוליה רשמה את הרעיה הנוכחית ואת כל ילדי האיש.</li>
  <li><b>הענף המצרי (מהדורה 55).</b> שני שאלוני רישום לעולה שנחתמו בחיפה ב-1950 מעמידים את <b>יוסף</b> (יליד קהיר 17.7.1935) ואת אחיו <b>שמעון</b> (31.6.1934), <b>שניהם בני רפאל</b>, אזרחים מצרים. רפאל בן מיכאל, יליד יפו ~1904, היה כבן עשר בגירוש נתיני בריטניה מיפו ב-1914 — ומכאן, ככל הנראה, הענף שנשאר במצרים ושבניו שבו ארצה שלושים ושש שנים אחר כך. השרשרת שלמה ← מיכאל ← רפאל <b>מאומתת</b> בשלושה טפסים; זיהוי «רפאל» שבשאלונים — <b>ככל הנראה</b>.</li>
  <li><b>הקו הישיר, ברשומת מדינה (מהדורה 53).</b> טופס קונסולרי 30 מיפו, 24.4.1893, נוקב «Youssef Arrwas · <b>Father's Name: Solomon Arwas</b> · Age 41»; ובעמוד הנגדי, טופס 31 מ-27.4.1893, משק ביתו: <b>שרה אשתו (29), שלמה (19), משה (14), רפאל (3) וריינה (10)</b> — כלומר <b>אחיה ואחותה של מרים בשמותיהם</b>, ולא רק שלמה שבספר המשפחה. מרים נעדרת כצפוי, שכן כבר נישאה. וטופס 43 מ-26.3.1902 מעמיד את <b>שלמה בן יוסף</b> עצמו — «Father: Yousef Arruas (<b>dead</b>) · Farmer · 27» — ובכך <b>תוחם את פטירת יוסף</b> בין אפריל 1893 למרץ 1902.</li>
  <li><b>שלושה בני שלמה (מהדורה 50).</b> לצד מרקו עומדים עתה עוד שניים מאותו דור שאביהם נקרא שלמה ארואס. <b>אלי</b> — תעודת נישואין ירושלים 2.4.1944 («בן שלמה ושמחה») ומפקד ירושלים תש״ז (עמודת «שם האב»: שלמה); הוא ראש משק הבית שבמפקד «משמר העם» תש״ח, ושני המקורות בלתי תלויים. <b>משה החייט</b> — נתין בריטי מלידה מנווה שלום שבתל אביב; שם אביו <b>אינו</b> רשום במסמך, והוא נגזר <b>ככל הנראה</b> מכך שבנו יליד 1931 נקרא שלמה. שהם <b>אחים</b> — טעון אימות; אין רשומה המעמידה שניים מהם יחד.</li>
 </ul>

 <h2>מניין באו הענפים</h2>
 <ul>
  <li><b>צד האם — ארואס/ארואץ:</b> ילידי גיברלטר שעלו ב-1833; מתועדים ביפו לכל המאוחר מ-1855 (יעד ההתיישבות ב-1833 עצמו אינו מתועד). במפקד מונטיפיורי 1855 מופיעה המשפחה במלואה: שלמה (32, "סוחר ובאנקיר") ואשתו שמחה, ובניהם יוסף (12), משה (6) ואליהו (3); לצדם ענף אלעזר ומסודה — ככל הנראה אחיו של שלמה, שעלה באותה שנה.</li>
  <li><b>צד האם — פריינטה:</b> יצחק (פפו) פריינטה מדור מייסדי מקווה ישראל (~1860/62 ירושלים, ממשפחה סלוניקאית - 31.12.1944 לפי הספר; עץ כהן: 1942 — טעון הכרעה ברשומת נחלת יצחק) ואשתו מרים ארואס מיפו (~1875 - 1916). שמונת ילדי משפחת פריינטה (הכתבה מ-1970 מנתה תשעה; ספר המשפחה — שמונה), ובהם שושנה רוזה — אמו של אברהם.</li>
  <li><b>צד האב — צאלח/צדוק:</b> משפחת צורפים, רבנים ודיינים מצנעא שבתימן. אהרון עלה בתשרי תרע"ה (1914) דרך נמל יפו, לאחר שאביו נפטר בעדן ואמו ואחיו הצעיר נספו ברעב 1904.</li>
 </ul>

 <h2>על מה נשען כל דור</h2>
 <ul>
  <li><b>הדורות התחתונים</b> — כרטיס החבר בעמותת דור הפלמ״ח וכתבת "למרחב" (1970).</li>
  <li><b>צד האב</b> — זיכרונות אהרון צדוק ומכתבו לנכדו (מקור ראשוני): לידה בצנעא (~1895-1898, המקורות חלוקים; בתיבה ננקב ~1895 על פי גיל 86 שברשומת הקבורה — מהדורה 38 — ובספר), משפחת צאלח, פטירת האב בעדן, רעב 1904, עלייה 1914. שם הסב אברהם — פנקס הבוחרים 1949 וכתובת אהרן ורוזה (מסמך ראשוני, מהדורה 35) — מאומת; שם הסבתא סעדה — MyHeritage + ספר המשפחה (שני מקורות משפחתיים לא בלתי-תלויים), ככל הנראה; האח יוסף, שנספה עם אמו — ספר המשפחה.</li>
  <li><b>מרים ארואס והוריה</b> יוסף וגרסיה — אוששו ב-Geni, ובמהדורה 35 גם בספר המשפחה: תאריך פטירתה נקרא מעל מצבתה בטרומפלדור (ז׳ בתמוז תרע״ו), ואביה יוסף מזוהה כסוכן הקניות של מקווה ישראל.</li>
  <li><b>פנקס נתיני בריטניה ביפו ("Register of British Subjects"):</b> בגיליון הפתיחה, שורה 1 — "Solomon Arruas · Gibraltar · Jaffa · Money Changer"; שורה 10 — "Azar Arruas · Gibraltar · Matress Maker"; ובגיליון 1873, שורה 12 — "Eliaho Arruas · Palestine · Money Changer". מאשש עצמאית את מוצא גיברלטר וסוגר את שרשרת המקצוע: באנקיר (1855) ← חלפן (גיליון הפתיחה) ← צראף אצל יוסף (1869) ← חלפן אצל אליהו (1873). עמודת התאריך בגיליון הפתיחה ריקה, ו-IGRA מאנדקס אותו פעמיים (1860 ו-1873) — שנת הרישום אינה נקבעת. זיהוי Solomon עם שלמה — כמעט ודאי; זיהוי Azar עם אלעזר, וממילא גם "מזרנים" שבתיבת אלעזר — ככל הנראה.</li>
  <li><b>יוסף ארואץ במפקד ירושלים 1866</b> (פריט 269) — מסביר מדוע רשומת הקונסוליה 1869 נוקבת ב"ירושלים" כעיר מוצאו אף שהמשפחה ביפו מ-1855: ירושלים היא ככל הנראה עיר מגוריו הקודמת ולא מקום לידתו. ההסבר עומד בכפוף לזיהוי, המדורג ככל הנראה.</li>
  <li><b>צאלח ← צדוק:</b> פנקס הבוחרים תש"ט של ירושלים מדפיס את שם המשפחה בשתי צורותיו — "צדוק (צאלח)" — ובילקוט הפרסומים תועדו קבוצות משפחתיות שהחליפו צאלח ← צדוק (1954-1977). אלה אינם בני המשפחה ואינם מזהים אותה, אך הם מאששים חיצונית את <b>הדפוס</b> שבבסיס עדותו של אהרון. דירוג: קיום הדפוס — מאומת; שכך אירע גם במשפחתו — כמעט ודאי.</li>
  <li><b>ענף פריינטה — הרובד היפואי:</b> מפקדי מונטיפיורי מתעדים את השם בארץ מ-1839 (ירושלים) וביפו מ-1866 — שלמה ואסתר (עלו 1858), שמחה האלמנה (עלתה 1868) וארבעה ילדים יתומים ונזקקים ב-1875. זהו המילייה שממנו יצא יצחק פפו למקווה ישראל בימי נטר, אך אין חוליה שמית מוכחת — טעון אימות.</li>
  <li><b>הורי יוסף — שלמה ושמחה</b> — כמעט ודאי ברמת המפקד (מפקד 1855 + רישום הקונסוליה הבריטית 1869: "יוסף בן סולומון, צראף"). זיהוי יוסף שבמפקד כאביה של מרים — ככל הנראה, ולכן גם השרשור המלא אל שלמה ושמחה — ככל הנראה.</li>
  <li><b>שנתוני רוזה ויעל</b> ושמות האבות אברהם ויצחק — פנקס הבוחרים תש"ט (1949), IGRA; לידת רוזה דויקה במהדורה 35 ל-31.12.1902 על פי דף רישום הלידות שבכתב יד אביה (ספר המשפחה). פטירת רוזה — 3.4.1979, חולון — נסגרה במהדורה 38 ברשומת הקבורה (כמעט ודאי; הספר ועץ כהן אוששו, מועמד תיק העיזבון נדחה). שנתוני שאר האחים — מרים (קיקה) 1927, יצחק 1933, יוסי 1948 — עץ כהן המשפחתי (2005), ככל הנראה; פטירת יעל — 9.8.1996, רשומת הקבורה (מהדורה 38).</li>
 </ul>

 <h2>סייגים</h2>
 <ul>
  <li><b>סימני «?» בתיבות</b> — נתונים שאין להם רשומה מאששת, בשלושה הקשרים. <b>(א) דור ההורים — נסגר במהדורה 38:</b> רשומות הקבורה בחולון (מרשם JOWBR, אינדקס מצבות מצולמות) נוקבות: אהרון — 18.11.1981 (כ"א בחשוון תשמ"ב), בן 86, אביו אברהם — בהלימה למודעת האבל ("דבר" 19.11.1981, מהדורה 36); רוזה — 3.4.1979 (ו' בניסן תשל"ט), בת 76, אביה יצחק — "אפריל 1979" של עץ כהן אושש ומועמד תיק העיזבון נדחה; קבורים זה לצד זה. דירוג: כמעט ודאי (אינדקס; צילומי המצבות — היעד המשלים). <b>(ב) שושלת ארואץ:</b> מועמדים מתוך מ"ד גאון, "יהודי המזרח בארץ ישראל" (1938), שרשם כי קברי חלק מהמשפחה נמצאים בבית העלמין הישן ביפו. שלמה 1868 — ככל הנראה (מתיישב עם היעדרו מרשומת 1869); יוסף 1894, אליהו 1906 ואברהם 1912 — טעונים אימות. מועמד נוסף אצל גאון, "אליעזר, נפ׳ 1865", לא הוצג בעץ: ההחרגה נשענה על ההנחה שאלעזר נרשם בקונסוליה ב-1873, אך רשומת Azar נמצאת בגיליון הפתיחה חסר-התאריכים ולכן הסתירה אינה מוכחת עוד — ההחרגה נשמרת מזהירות בלבד. <b>(ג) דור האחים:</b> שנתוני מרים (קיקה), איציק ויוסי — עץ כהן (2005) בלבד; פטירת יעל נסגרה במהדורה 38 — 9.8.1996, קריית שאול, בת אהרן ושושנה (רשומת הקבורה).</li>
  <li><b>אמה של רוזה</b> — <b>מרים ארואס</b>: דף רישום הלידות שבעיזבון יצחק נוקב במרים כאם הבכור (1891) וברוזה כילידת 31.12.1902, מצבת מרים נוקבת תרע"ו (1916), ולפי הספר נשא יצחק את סמוחה רק אחרי מות מרים. הצירוף — מאומת ברכיביו המסמכיים, כמעט ודאי בשלמותו; סמוחה הייתה המטפלת-החורגת מ-1916 ואילך.</li>
  <li><b>תאריך הלידה המדויק 16.9.1925</b> — מ-MyHeritage בלבד, ועץ כהן (2005) נוקב 19.9.1925 — פער שלושה ימים בין שני מקורות משפחתיים, ללא רשומה מכריעה; שנת 1925 מאומתת בכרטיס הפלמ״ח. סדר הלידה של האחים אינו ודאי.</li>
  <li><b>שלמה ארואס בן יוסף</b> (אחי מרים) קרוי ככל הנראה על שם סבו — פרשנות על סמך השם בלבד. שנת לידתו המוצהרת (~1875) זהה לשנת לידת מרים — תאומים או סטיית-גיל באחד המקורות; לא הוכרע, ומכאן סימן השאלה בתיבה. אחיו הצעיר של אהרון — <b>יוסף</b>, לפי ספר המשפחה ("אח ליוסף שהיה צעיר ממנו במעט", מהדורה 35); נספה עם אמו ברעב תרס"ד.</li>
  <li>פרטי בני הדור החי מובאים במידה מזערית, מטעמי פרטיות.</li>
 </ul>
</div>
<footer>מסמך מחקר משפחתי · מהדורה {TREE_ED} · גרסת בנייה: {BUILD_STAMP}</footer>
</body></html>'''
open('tree.html','w',encoding='utf-8').write(html_doc)
open('tree_svg.svg','w',encoding='utf-8').write(SVG)
print("tree.html written")
