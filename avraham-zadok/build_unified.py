# -*- coding: utf-8 -*-
"""בונה מסמך HTML עצמאי אחד: דוח + עץ + גלריית ראיות + אינדקס מקורות, עם בדיקת קישורים.
פלט: אברהם-צדוק.html  (+ עותק site/)  ; נכשל בקול אם קישור מקומי שבור."""
import re, os, shutil, urllib.parse, markdown, base64, hashlib, html as _html

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

MAIN_HTML = "אברהם-צדוק.html"

def _edition_from(text, pattern):
    m = re.findall(pattern, text)
    return max(int(x) for x in m) if m else None


def md2html(text):
    return markdown.markdown(text, extensions=['extra','sane_lists','nl2br'])

report_md  = open('report.md', encoding='utf-8').read()
_ED_HEAD = _edition_from(report_md.split(chr(10))[3], r'מהדורה (\d+)')
_appendix = report_md.split('נספח ד', 1)[-1]
_ED_TABLE = max((int(x) for x in re.findall(r'^\| (\d+) \|', _appendix, re.M)), default=None)
_ED_LOG  = _edition_from(open('CHANGELOG.md', encoding='utf-8').read(), r'מהדורה (\d+)')
assert _ED_HEAD is not None, "EDITION GATE: no edition number in report header line"
_ed_bad=[]
if _ED_LOG and _ED_HEAD != _ED_LOG: _ed_bad.append(f"header says edition {_ED_HEAD} but CHANGELOG.md peaks at {_ED_LOG}")
if _ED_TABLE and _ED_HEAD != _ED_TABLE: _ed_bad.append(f"header says edition {_ED_HEAD} but appendix table peaks at {_ED_TABLE}")
assert not _ed_bad, "EDITION MISMATCH: " + "; ".join(_ed_bad)
EDITION = _ED_HEAD

sources_md = open('sources-index.md', encoding='utf-8').read()
tree_svg   = open('tree_svg.svg', encoding='utf-8').read()

import unicodedata
report_md_clean  = re.sub(r'^\s*</?div[^>]*>\s*$', '', report_md,  flags=re.M)
sources_md_clean = re.sub(r'^\s*</?div[^>]*>\s*$', '', sources_md, flags=re.M)

report_html  = md2html(report_md_clean)
sources_html = md2html(sources_md_clean)

# --- stable anchors for chapters, so the document map and cross-links actually jump ---
_toc = []
def _slug(plain):
    m = re.match(r'\s*([0-9]+)\.', plain)
    if m: return 's' + m.group(1)
    if 'נספח ד' in plain or 'יומן מהדורות' in plain: return 's-changelog'
    if 'נספח' in plain: return 's-appendix'
    if 'מקורות' in plain: return 'sources-top'
    return 's-' + hashlib.md5(plain.encode('utf-8')).hexdigest()[:6]

def _h2(m):
    txt = m.group(1); plain = re.sub(r'<[^>]+>', '', txt)
    aid = _slug(plain); _toc.append((aid, plain))
    return f'<h2 id="{aid}">{txt}</h2>'
report_html = re.sub(r'<h2>(.*?)</h2>', _h2, report_html, flags=re.S)

def _h3(m):
    txt = m.group(1); plain = re.sub(r'<[^>]+>', '', txt)
    mm = re.match(r'\s*([0-9]+(?:\.[0-9]+)+)', plain)
    aid = ('s' + mm.group(1).replace('.', '-')) if mm else \
          'sub-' + hashlib.md5(plain.encode('utf-8')).hexdigest()[:6]
    return f'<h3 id="{aid}">{txt}</h3>'
report_html = re.sub(r'<h3>(.*?)</h3>', _h3, report_html, flags=re.S)
report_html = re.sub(r'<h4>(.*?)</h4>',
                     lambda m: '<h4 id="%s">%s</h4>' % (
                         (lambda pl: ('s' + re.match(r'\s*([0-9.]+)', pl).group(1).rstrip('.').replace('.', '-'))
                          if re.match(r'\s*[0-9]+\.', pl)
                          else 'sub-' + hashlib.md5(pl.encode('utf-8')).hexdigest()[:6])(
                              re.sub(r'<[^>]+>','',m.group(1))),
                         m.group(1)), report_html, flags=re.S)

# the report supplies its own <h1> and edition line; the hero already carries both
report_html = re.sub(r'<h1>.*?</h1>', '', report_html, count=1, flags=re.S)
report_html = report_html.replace('<thead>\n<tr>\n<th></th>\n<th></th>\n</tr>\n</thead>', '')
report_html = re.sub(r'<thead>\s*<tr>\s*(<th[^>]*>\s*</th>\s*)+</tr>\s*</thead>', '', report_html)
report_html = re.sub(r'<p><strong>מסמך מחקר מתועד[^<]*</strong>\s*(<br\s*/?>)?\s*</p>', '', report_html, count=1)
sources_html = sources_html.replace('<h1>רשימת מקורות</h1>', '<h2 id="sources-top">נספח ג: רשימת מקורות</h2>', 1)

# --- Wikipedia-style citations: [[N]] in the prose -> numbered superscript linking to the
#     matching entry in the sources index, which links back to every place that cites it ---
SRC_ID = lambda n: 'src-' + n.replace('א','a').replace('ב','b').replace('ג','c').replace('ד','d')
_src_titles, _cited = {}, {}

def _src_head(m):
    num, rest = m.group(1), m.group(2)
    plain = re.sub(r'<[^>]+>', '', rest).strip()
    _src_titles[num] = plain
    return f'<h3 id="{SRC_ID(num)}"><span class="srcnum">{num}</span> {rest}</h3>'
sources_html = re.sub(r'<h3>\s*([0-9]+[אבגד]?)\.\s*(.*?)</h3>', _src_head, sources_html, flags=re.S)

def _cite(m):
    num = m.group(1)
    seq = _cited.setdefault(num, [])
    seq.append(len(seq) + 1)
    back = f'{SRC_ID(num)}-c{len(seq)}'
    title = _html.escape(_src_titles.get(num, 'מקור ' + num))[:160]
    return (f'<sup class="cite" id="{back}"><a href="#{SRC_ID(num)}" title="{title}">'
            f'[{num}]</a></sup>')
report_html = re.sub(r'\[\[([0-9]+[אבגד]?)\]\]', _cite, report_html)

# back-links: every source entry lists the places in the report that cite it
for num in list(_cited):
    sid = SRC_ID(num); n = len(_cited[num])
    links = ' '.join(f'<a href="#{sid}-c{i+1}" title="חזרה לאזכור בדוח">↑{i+1}</a>' for i in range(n))
    m = re.search(r'(<h3 id="%s">.*?</h3>)' % re.escape(sid), sources_html, flags=re.S)
    if m:
        sources_html = sources_html.replace(
            m.group(1), m.group(1) + f'<div class="backlinks"><b>מצוטט בדוח:</b> {links}</div>', 1)

# --- certainty ratings are the spine of this document: give them a visible chip ---
_RANK_RE = re.compile(r'<em>\((דירוג(?:(?!</em>).)*?)\)</em>', re.S)
def _rank(m):
    return '<em class="rank">' + m.group(1).replace('דירוג', '<b>דירוג</b>', 1) + '</em>'
report_html  = _RANK_RE.sub(_rank, report_html)
sources_html = _RANK_RE.sub(_rank, sources_html)

# the edition log is an appendix: it belongs after the bibliography, not inside the article
_m = re.search(r'(<h2 id="s-changelog">.*)$', report_html, flags=re.S)
changelog_html = _m.group(1) if _m else ''
if _m: report_html = report_html[:_m.start()]

# --- explicit intrinsic size + async decode on every evidence image (no layout shift) ---
try:
    from PIL import Image as _PILImage
except Exception:
    _PILImage = None
def _img_dims(path):
    if _PILImage is None or not os.path.exists(path): return ''
    try:
        with _PILImage.open(path) as im: return f' width="{im.width}" height="{im.height}"'
    except Exception: return ''

# --- Evidence gallery (crops click through to full original screenshot + external source) ---
EVID = [
    dict(crop="docs/evidence/palmach_details_zoom.png",
         full="docs/evidence/palmach_avraham_page.jpg",
         ext="https://palmach.org.il/veterans/veteranpage/?itemId=86681",
         title="כרטיס החבר — עמותת דור הפלמ״ח",
         cap="פרטי הליבה כפי שנמסרו בידי בניו: «בן רוזה ואהרון · נולד במקוה ישראל · 1925 · גויס 1942 · פל׳ ד׳, ההגנה, חטיבת קרייתי · נפטר 1/1/2017 · נקבר בתל אביב — ירקון». לחיצה על הראיה פותחת את המקור החיצוני; העותק המקומי המלא — בקישור שמתחת."),
    dict(crop="docs/evidence/nli_frainte_quote_zoom.png",
         full="docs/evidence/nli_frainte_book.jpg",
         ext="https://www.nli.org.il/he/books/NNL_ALEPH997010400325605171/NLI",
         title="ספר «משפחת פריינטה: מקוה ישראל» — הספרייה הלאומית",
         cap="הכריכה האחורית: המשפחה «ששורשיה נטועים... בבית הספר החקלאי מקוה ישראל... שמקורה ביהדות ספרד ושמיזגה לתוכה מזרח ומערב, אשכנז, תימן ומגרב». אישוש עצמאי לשיוך רוזה פריינטה למקווה ישראל ולמיזוג עם המוצא התימני. מס׳ מערכת 997010400325605171."),
    dict(crop="docs/evidence/lemerhav_1970_frainte_zoom.png",
         full="docs/evidence/lemerhav_1970_frainte_page.jpg",
         ext="https://www.nli.org.il/he/newspapers/?a=d&d=lmrv19700420-01.2.87",
         title="«למרחב», 20.4.1970 — משפחת פריינטה של מקווה ישראל",
         cap="כתבת מאה שנה למקווה ישראל, המוקדשת לנשים הראשונות של המוסד — ובהן משפחת פריינטה (משפחת אמו של אברהם). מתועדים בה יצחק פריינטה (מהתלמידים הראשונים בימי נטר), אשתו מרים ארואס מיפו, והבנות פלורין, ויקטוריה ורוזה. הכתבה מציינת ש«הבעל של רוזה היה האופה» (אהרון) ושבתה מרים הייתה חברת קיבוץ חוקוק («קיקה»)."),
    dict(crop="docs/evidence/frainte_shacham_photo.png",
         full="docs/evidence/nli_hukok_frainte_shacham_full.jpg",
         ext="https://www.nli.org.il/he/archives/NNL_ARCHIVE_AL997009692042205171/NLI",
         title="תצלום: משפחת פריינטה ושחם, מקווה ישראל (1947-1949)",
         cap="תצלום סטודיו מאוסף ארכיון קיבוץ חוקוק, שהוכן להצגה בערב «חיים שכאלה». כותר הפריט: «משפחת פריינטה ושחם, בית הספר במקווה, נעורים». נחלת הכלל. הערה: הרשומה אינה מזהה בשמות את האנשים בתמונה — הם אינם ידועים ואין לזהותם כרוזה/אהרון/אברהם."),
    dict(crop="docs/evidence/aharon_letter_zoom.png",
         full="docs/evidence/aharon_letter_page1.png",
         ext="https://www.nli.org.il/he/books/NNL_ALEPH990019450240205171/NLI",
         title="מכתב אהרון צדוק לנכדו (1971/72) — מקור ראשוני",
         cap="תעתיק מכתבו האוטוביוגרפי של אהרון צדוק לנכדו גיל שחם, למשימת בר-המצווה «דור לדור יביע אומר» (חוקוק): «נולדתי בצנעא עיר הבירה של תימן, שם משפחתנו (צאלח)... כאן בארץ ישראל הפכנו את הכינוי צאלח לצדוק». המכתב מתעד את יתמותו, רעב 1904, נדודיו ועלייתו ביפו בתשרי תרע\"ה 1914. הקישור החיצוני — רשומת «שבות תימן» בספרייה הלאומית, המאמתת את היותו עורך-שותף של הקובץ."),
    dict(crop="docs/evidence/isa_1948_jerusalem_pariente_zoom.png",
         full="docs/evidence/isa_1948_jerusalem_pariente_form_full.png",
         ext="https://www.archives.gov.il/details/001righ",
         title="מפקד תש\"ח, נחלת שבעה — משק הבית פריינטה (ספטמבר 1948)",
         cap="«פריינטה · אברהם · בעל הבית · ז · נשוי · גיל 58» ולצדו «פריינטה · בוקס · אשתו · נ · נשואה · גיל 45». גיל 58 בספטמבר 1948 גוזר לידה בסביבות 1890 — הדור שאחרי יצחק (פפו) פריינטה. שם אביו של יצחק היה אברהם ואחיו שמואל נותר בירושלים; נכד הנושא את שם הסב הוא תבנית קרייה ספרדית מובהקת, ומכאן ההשערה שזהו בן-דודה של רוזה. הטופס הוא הגרסה הקצרה («האם עדיין גר בכתובת הנ׳ל») ואין בו שם אב או מקום לידה. (דירוג: נתוני הטופס — מאומת, נקראו מן הסריקה; השיוך לשושלת — טעון אימות.)"),
    dict(crop="docs/evidence/isa_1948_jerusalem_arwas_zoom.png",
         full="docs/evidence/isa_1948_jerusalem_arwas_form_full.png",
         ext="https://www.archives.gov.il/details/001ri28",
         title="מפקד «משמר העם» ירושלים תש\"ח — משק הבית ארואץ (3.5.1948)",
         cap="טופס האוכלוסיה מס' 7, «בית מדג'וק» שבמחנה יהודה: «ארואץ · אליהו · ראש המשפחה · 1913 · עדה: יהודי ס' · שנת העליה לא\"י: 1924 · הנתינות: בריטית»; רעייתו «סול», בת בכור, ילידת 1922 בתורקיה, עלתה 1936; בנם «יואל», יליד 1945 בירושלים. הנתינות הבריטית היא סמן אפשרי המבחין בין ענף ארואס הגיברלטרי (נתיני בריטניה ביפו מ-1839) לבין משפחת ארואץ המרוקאית שבחסות צרפת. לחיצה — הטופס המלא. (דירוג: תוכן הטופס — מאומת, נקרא מן הסריקה; שם האב ושם יישוב הלידה — לא פוענחו; שיוך לענף הגיברלטרי — טעון אימות.)"),
    dict(crop="docs/evidence/hashkafa_1904-04-15_arwas_gaza_lead.png",
         full="docs/evidence/hashkafa_1904-04-15_arwas_gaza_zoom.png",
         ext="https://www.nli.org.il/he/newspapers/?a=d&d=hsk19040415-01.2.9",
         title="«השקפה», 15.4.1904 — אליהו ארואץ בעדת עזה",
         cap="ידיעה במדור המכתבים: «הגיעו לנו תלונות מהאשכנזים היושבים שם על האדון אליהו ארואץ... האדון ארואץ הביא שוחט ספרדי... גם לא הניח האדון ארואץ לקחת מהמצה ששלח האדון ענתבי לעזה על ידי האדון רוקח מיפו... ארבעים פרנק לחדש הנתנים מהנדיב לעדת עזה». לחיצה — הידיעה במלואה. (דירוג: תוכן הידיעה — מאומת, נקרא בעיניים על תצלום העמוד; זיהויו עם אליהו בן שלמה — טעון אימות, מפני משפחת ארואץ המרוקאית השנייה שבאזור.)"),
    dict(crop="docs/evidence/davar_1981-11-22_p4_farhi_ad_zoom.png",
         full="docs/evidence/davar_1981-11-22_p4_farhi_ad_zoom.png",
         ext="https://www.nli.org.il/he/newspapers/?a=d&d=dav19811122-01.2.68.1",
         title="מודעת השתתפות — «דבר», 22.11.1981, עמ׳ 4",
         cap="«המועצה לשווק פרי הדר משתתפת בצערו של מר ב. צ. פרחי, מנהל סוכנות..., על פטירתו ללא עת של אב המשפחה אהרן צדוק ז´ל». הנמען אינו בן אלא חתן — בן ציון (ביטו) פרחי, בעלה של יעל; עיגון שלישי ובן-זמן למעמדו במשפחה (1943 נישואין · 1981 המודעה · 1992 הקבורה), והפרט התעסוקתי הראשון שיש עליו. ה-OCR של המודעה משובש כמעט לחלוטין; הנוסח פוענח בהגדלה בצפיין. (דירוג: תוכן — מאומת; זיהוי ב.צ. פרחי — כמעט ודאי; שם הסוכנות — טעון אימות.)"),
    dict(crop="docs/evidence/wedding_yael_parchi_1943.png",
         full="docs/evidence/wedding_yael_parchi_1943.png",
         ext="https://www.nli.org.il/he/newspapers/?a=d&d=dav19431128-01.2.62",
         title="מודעת נישואין — יעל צדוק ובן-ציון פרחי («דבר», נובמבר 1943)",
         cap="מקור ראשוני בן-זמן: «א. פרחי | אהרן צדוק ורעיתו — תל-אביב | מקוה ישראל — מתכבדים להזמין... בשמחת כלולות בניהם: בן-ציון עם בת-חיל יעל. החופה תתקיים ביום ראשון כ\"ג חשון תש\"ד (21 לנובמבר)... בבית הכנסת שלום וצדקה». מאשש את נישואי יעל (בת אהרון) עם בן-ציון פרחי (הגיס), 21.11.1943, ומעגן את המשפחה במקווה ישראל. (דירוג: תוכן המודעה — מאומת; זיהויה עם משפחתנו — כמעט ודאי. הערה: הגיליון מ-28.11 מאוחר לחופה — ככל הנראה פרסום חוזר; אנומליה מסומנת.)"),
    dict(crop="docs/evidence/yemenite_workers_council_1934.png",
         full="docs/evidence/yemenite_workers_council_1934.png",
         ext="https://www.nli.org.il/he/newspapers/?a=d&d=dav19341001-01.2.18",
         title="«דבר», 1.10.1934 — המועצה הארצית של העובדים התימנים",
         cap="בכינוס המועצה הארצית של העובדים התימנים בתל אביב (סוכות תרצ\"ה) נבחר מרכז ארצי בן 9 חברים — ובהם «אהרן צדוק» — לצד הקמת מזכירות ומערכת עיתון, בהשתתפות י. שפרינצק מטעם ההסתדרות. תואם לעדות אהרון על היותו «מזכיר הפועלים». (דירוג: כמעט ודאי.)"),
    dict(crop="docs/evidence/mitteiman_letzion_1938.png",
         full="docs/evidence/mitteiman_letzion_1938.png",
         ext="https://www.nli.org.il/he/newspapers/?a=d&d=hzh19380503-01.2.54",
         title="«מתימן לציון» (מסדה, 1938) — «הצפה», 3.5.1938",
         cap="מודעת הקובץ המדעי-תרבותי «מתימן לציון» על יהדות תימן; רשימת המשתתפים (לפי א\"ב) כוללת את «אהרן צדוק» לצד ש\"ד גויטין, ישראל ישעיהו, אברהם יערי ומנשה רבינא. הצמד ישעיהו + אהרן צדוק חוזר גם ב«שבות תימן» (1945) ומלכד את הזיהוי; מקדים אותו בשבע שנים. (דירוג: כמעט ודאי.)"),
    dict(crop="docs/igra/igra_voters1949_mikveh_zadok_rows.png",
         full="docs/igra/igra_scan_1949_mikveh_full.png",
         ext="https://igra-images.genealogy.org.il/1949_National_Elections/1949_NatVotBneiBraq_336.jpg",
         title="פנקס הבוחרים תש\"ט (1949), מקוה ישראל — אהרון ושושנה צדוק (IGRA)",
         cap="«רשימת בעלי זכות בחירה במקוה ישראל» (ארכיון המדינה, גל-45494/6): שורה 140 — «צדוק שושנה, [בת] יצחק, 1903»; שורה 141 — «צדוק אהרן, [בן] אברהם, 1898». רשומת המדינה המאששת את שם אבי-אהרון (אברהם), את שם אבי-רוזה (יצחק פפו פריינטה) ואת שנת לידת רוזה. רשומות IGRA 85741-85742. לחיצה על הראיה פותחת את סריקת המקור באתר IGRA; «העותק המקומי» — עותק מלא של דף הסריקה (שורות 134-159)."),
    dict(crop="docs/montefiore/census1855_jaffa_aruets_row.png",
         full="docs/montefiore/census1855_jaffa_page_scan.jpg",
         ext="https://www.montefioreendowment.org.uk/wp-content/uploads/scans/11800003.pdf",
         title="מפקד מונטיפיורי 1855, יפו — משפחת שלמה ושמחה ארואץ",
         cap="פנקס מפקד יפו תרט\"ו (1855), שורה 18: שלמה ארואץ — בן ל\"ב, עלה בשנת תקצ\"ג (1833), «סוחר ובאנקיר אבל אין לו עתה»; אשתו שמחה; הבנים יוסף· משה· אליהו. הרשומה הסוגרת את פער «אם יוסף» (שמחה). לעניין הגיל: המפקד רושם את יוסף כבן 12 (יליד ~1843) ורשומת הקונסוליה 1869 כבן 24 (יליד ~1845) — פער שנתיים מקובל בין גיל מוצהר במפקד לגיל מוצהר ברישום קונסולרי, מסומן ולא מוכרע. לחיצה על הראיה פותחת את סריקת ה-PDF המקורית באתר מונטיפיורי."),
    dict(crop="docs/archives/gaon1938_aruets_index_p6.png",
         full="docs/archives/gaon1938_aruets_index_p6.png",
         ext="http://www.sephardicstudies.org/pdf/gaon_a.pdf#page=6",
         title="מ\"ד גאון, «יהודי המזרח בארץ ישראל» (1938) — ערכי ארואץ: קברי המשפחה ביפו",
         cap="גוש 14 ערכי ארואץ (Aruets) בלקסיקון של משה דוד גאון (ירושלים 1938; עמ' 119-120 בספר, דרך האינדקס האנגלי באתר sephardicstudies.org). בערך «Aruets Abraham» ההערה המפורשת: «Graves of some of this fam. are in Jaffa old cemetery» — קברי חלק מבני המשפחה בבית העלמין הישן של יפו. בין הערכים: שלמה ארואץ — נפטר יפו ז' אב תרכ\"ח (26.7.1868), ככל הנראה שלמה שלנו, בהלימה להיעדרו מרשומת 1869; יוסף (1894), אליהו ברוך (1906), אברהם (1912), אליעזר (1865 — ההחרגה מן העץ נשענה על הנחה שנחלשה: רשומת Azar נמצאת בגיליון הפתיחה חסר-התאריכים ולא בגיליון 1873) — טעוני אימות; ו«משה יוסף ארואץ — סגן מנהל בנק ביפו לפני מלה\"ע הראשונה». לחיצה על הראיה פותחת את ה-PDF המקורי (עמ' 6). אזהרה: לא לערבב עם משפחת הרב יוסף בן משה ארואץ המרוקאית."),
    dict(crop="docs/igra/igra_salomo_aruas_1839_gibraltar.png",
         full="docs/igra/igra_salomo_aruas_1839_gibraltar.png",
         ext="",
         title="סאלומו ארואס — מוצא: גיברלטר (רישום קונסולרי, 1839)",
         cap="הרשומה הקדומה ביותר בשושלת: «Salomo Aruas — Country of Origin: Gibraltar», 8.4.1839, סדרת רישומי היהודים הבריטיים של ירושלים 1838-1908 (ארכיון המדינה; IGRA 10). חושפת את מוצא משפחת ארואס בגיברלטר ומסבירה את החסות הבריטית של השושלת כולה. הערה: קובץ הסריקה של הסדרה החזיר תחילה שגיאת 403; לאחר פנייה לצוות IGRA (שאישר את הבאג) נמסר העמוד למחקר בדוא\"ל — ראו איור 23 וערך מקור 29. כרטיס הרשומה שלעיל הוא התעתיק הרשמי. הזיהוי כשלמה אבי-יוסף — ככל הנראה (התאמת ציר זמן, שם וחסות). הד לשורש הגיברלטרי/מגרבי של השם פריינטה בצד השני של משפחת האם."),
    dict(crop="docs/evidence/britsub_jaffa_1860_rows1_10.png",
         full="docs/igra/igra_britsub_jaffa_1860_page1.jpg",
         ext="https://igra-images.genealogy.org.il/1860_1914_British_Subjects_Jaff/1860_1914_BritSub_Jaf1.jpg",
         title="\"Register of British Subjects\", יפו — ארואס בשורה הראשונה של גיליון הפתיחה",
         cap="גיליון הפתיחה של פנקס הרישום של נתיני בריטניה ביפו (ארכיון המדינה; IGRA). שורה 1: «Solomon Arruas — Gibraltar — Jaffa — Money Changer»; שורה 10: «Azar Arruas — Gibraltar — Matress Maker». מאששת עצמאית את מוצא גיברלטר, וסוגרת את שרשרת המקצוע: «סוחר ובאנקיר» (מפקד 1855) ← Money Changer (גיליון הפתיחה) ← Saraff אצל הבן יוסף (1869) ← Money Changer אצל הבן אליהו (1873). הערת תיארוך: עמודת ה-Date בעמוד ריקה, ו-IGRA מאנדקס אותו פעמיים — כ-1860 וכ-1873; שנת הרישום אינה נקבעת. באותו עמוד עוד ארבעה יוצאי גיברלטר (בנוליאל, הרוונג, ומכלוף ומנחם כהן) ושלושה צראפים נוספים — עדות למושבה גיברלטרית-מגרבית של חלפנים בנמל יפו תחת חסות בריטית. (דירוג: תוכן העמוד — מאומת; זיהוי Solomon עם שלמה ארואץ של מפקד 1855 — כמעט ודאי; זיהוי Azar עם אלעזר — ככל הנראה; שנת הרישום — טעונה אימות.)"),
    dict(crop="docs/evidence/britconsul_jaffa_1873_eliaho_row12.png",
         full="docs/igra/igra_britconsul_jaffa_1873_p0134.jpg",
         ext="https://igra-images.genealogy.org.il/1838_1919_Reg_BritishConsulate/1855-1919_RegBritConsulPal_0134.jpg",
         title="«In the Year 1873» — אליהו ארואס, יליד הארץ, חלפן (1.1.1873)",
         cap="גיליון שנת 1873 באותו פנקס נתיני בריטניה ביפו (ארכיון המדינה; IGRA 9119), עמ' 5, תאריך 1 בינואר. שורה 12: «Eliaho Arruas — Country of Origin: Palestine — Jaffa — Money Changer». ככל הנראה אליהו, בנו השלישי של שלמה, שבמפקד 1855 היה בן שלוש (יליד ~1852) — ומכאן «יליד הארץ», בניגוד לאביו הגיברלטרי. שני בניו של שלמה עסקו אפוא בחלפנות: יוסף («Saraff», 1.1.1869) ואליהו («Money Changer», 1.1.1873) — כלומר לא שרשרת מקצוע אלא ענף. (דירוג: תוכן הרשומה — מאומת; הזיהוי — ככל הנראה.)"),
    dict(crop="docs/igra/igra_yosef_arwas_1869_record.png",
         full="docs/igra/igra_yosef_arwas_1869_record.png",
         ext="https://igra-images.genealogy.org.il/1838_1919_Reg_BritishConsulate/1855-1919_RegBritConsulPal_0518.jpg",
         title="יוסף ארואס בן שלמה — רישום הקונסוליה הבריטית, יפו 1869 (IGRA)",
         cap="רשומת הרישום בקונסוליה הבריטית (ארכיון המדינה; IGRA 10384): «Yousef Arruas, child of Solomon» — 1.1.1869, יפו, בן 24 (יליד ~1845), מקצוע Saraff (צראף — חלפן), עיר מוצא: ירושלים. הרשומה שמעלה את שלמה ארואס כאבי-יוסף (ככל הנראה) וחושפת את המקצוע, הגיל והשורש הירושלמי של מי שהוא ככל הנראה סבא-רבא של אברהם מצד אם (אבי סבתו מרים; זיהוי — ככל הנראה)."),
    dict(crop="docs/igra/igra_voters1944_prineta_moshe.png",
         full="docs/igra/igra_voters1944_prineta_moshe.png",
         ext="https://igra-images.genealogy.org.il/1944_Voters_List_Knesset_Israel/1943_TA393.jpg",
         title="פנקס הבוגרים תש\"ד (1944) — משה פרינטה בן יצחק (IGRA)",
         cap="פנקס הבוגרים של כנסת ישראל בת\"א וביפו תש\"ד (ארכיון ת\"א-יפו; IGRA 80953): שורה 81409 — «פרינטה, משה בן יצחק (35), השוק 27»; ובשורה העוקבת — «פרינטה, רבקה בת דניאל» באותה כתובת (ככל הנראה אשתו). משה — אחיה של רוזה, בן יצחק פפו. באותו פנקס: בן-ציון פרחי בן חיים בגרוזנברג 29 (IGRA 79898). וברשימת בעלי זכות הבחירה תש\"ט (1949), ת\"א: יעל פרחי בת אהרון, ילידת 1923 (IGRA 212170)."),
    dict(crop="docs/myheritage/mh-1.png",
         full="docs/myheritage/mh-1.png",
         ext="",
         title="עץ MyHeritage המשפחתי — הדורות העמוקים",
         cap="דף Discoveries מעץ המשפחה של המשתמש (מקור משני): שמות הסבים אברהם צדוק (צאלח) וסעדה; יצחק «פפו» פריינטה ואביו אברהם פריינטה; מרים לבית ארואס והוריה יוסף וגרסיה. השם «צאלח» עצמו אומת בינתיים במקור ראשוני (מכתב אהרון); «שלמה ארואס» שמעל יוסף שב והתאשש חלקית ברשומת הקונסוליה הבריטית 1869 (דירוג: ככל הנראה); האח שלמה קרוי ככל הנראה על שם הסב (פרשנות על סמך השם). שמות שמקורם רק כאן טעונים אימות ברשומה ראשונית."),
    dict(crop="docs/geni/miriam_pariente_portrait_original.png",
         full="docs/geni/geni_miriam_pariente_profile.jpg",
         ext="https://www.geni.com/people/Miriam-Pariente/6000000081752002989",
         title="מרים פריינטה לבית ארואס (1875-1916) — תצלום דיוקנה",
         cap="תצלום דיוקנה של מרים פריינטה (ארואס) — סבתו של אברהם מצד אם — קובץ התמונה המקורי כפי שהועלה לפרופיל Geni המשפחתי (מנהל: רון רבינוביץ'; מאלבום גלעד רונן; רזולוציית הקובץ המקורי באתר: 96×128). הפרופיל מאשש את החוליה האימהית: מרים לבית ארואס, ממקוה ישראל, בת ליוסף וגרסיה ארואס, אשת יצחק פריינטה, אם לפלורין בלומברג/חנה ביטרן/רפאל רחמים; תאריכיה 1875-1916. «העותק המקומי» — דף הפרופיל המלא (התיעוד הטקסטואלי). הבהרה: «שלמה ארואס» מופיע שם כאחי מרים — הקרוי, לפי רשומת הקונסוליה 1869, על שם סבו שלמה אבי-יוסף (ככל הנראה)."),
    dict(crop="docs/evidence/voters1949_tzadok_tzalah_rows.png",
         full="docs/igra/igra_voters1949_tzadok_tzalah_jer.jpg",
         ext="https://igra-images.genealogy.org.il/1949_National_Elections/1949_NatVotJeru1_397.jpg",
         title="«צדוק (צאלח)» — פנקס הבוחרים תש\"ט (1949), ירושלים",
         cap="«מדינת ישראל, ועדת הבחירות המרכזית, רשימת בעלי זכות בחירה בירושלים», קלפי ז' (ארכיון המדינה, גל-45497/1; IGRA 314511). שתי השורות הראשונות נושאות את שם המשפחה בשתי צורותיו יחד: «צדוק (צאלח)» — שושנה בת סלמה, ילידת תרמ\"ח (1888), ושלמה בן יוסף, יליד 1903, שניהם ברח' דוד 17. אלה אינם בני משפחת אהרון, אך זהו אישוש חיצוני ברשומת מדינה למשפט שכתב במכתבו לנכדו: «כאן בארץ ישראל הפכנו את הכינוי צאלח לצדוק». (דירוג: קיום הדפוס ברשומות מדינה — מאומת, אומת בעיניים על הסריקה; שכך אירע גם במשפחת אהרון — כמעט ודאי.)"),
    dict(crop="docs/evidence/geni_pariente_zoom.png",
         full="docs/evidence/geni_pariente.jpg",
         ext="https://www.geni.com/search?search_type=people&names=%D7%A4%D7%A8%D7%99%D7%99%D7%A0%D7%98%D7%94",
         title="Geni — השם פריינטה ↔ Pariente (שם ספרדי)",
         cap="חיפוש «פריינטה» במאגר Geni ממפה את השם ל־Pariente/Paryente; בין התוצאות ענף מטנג'יר/טטואן שבמרוקו. מדגים שפריינטה הוא שם משפחה ספרדי (נפוץ בערי מרוקו). זהו מוצא השם ברמה הרחבה; הענף של רוזה עצמו היה ארץ־ישראלי ותיק (ראו הכתבה מ־1970)."),
    dict(crop="docs/evidence/uss_tennessee_1914_pariente_row.png",
         full="docs/igra/igra_uss_tennessee_1914_p25.jpg",
         ext="https://igra-images.genealogy.org.il/1914_15_USS_Tennessee/USS_Tenn_25.jpg",
         title="אסתר פריינטה בפינוי יפו — פנקסי ה-USS Tennessee (28.12.1914)",
         cap="רשימת המפונים מיפו לאלכסנדריה באניית הצי האמריקני USS Tennessee, בראשית מלחמת העולם הראשונה (ארכיון הלאומי, ארה\"ב; IGRA 1694). שורה 37: «Esther Pariente and one child ......... French, no papers». השם פריינטה ביפו של 1914 בנתינות צרפתית — בהלימה למוצא מגרבי מחוסה-צרפת. (דירוג: תוכן השורה — מאומת; זיהוי אישה זו עם השושלת — טעון אימות.)"),
    dict(crop="docs/igra/igra_yafo_1918_rows685_zoom.png",
         full="docs/igra/igra_yafo_residents_1918_aharon_tzalah.jpg",
         ext="https://igra-images.genealogy.org.il/1918_19_Tel_Aviv_Register/1917_TLV_08-1178a_144.jpg",
         title="פנקס תושבי ועד העיר ליהודי יפו, 1918-1919 — «אהרן צאלח», בן 23",
         cap="דף 144, שתי השורות התחתונות: משק בית 685 (גיל 35) ומשק בית 685/2 (גיל 23, בעמודת היחס «רוק» = רווק). ארכיון תל אביב-יפו, מספר מערכת 08-1178; IGRA 4307. אם הזיהוי נכון, זו הרשומה החיצונית המוקדמת ביותר של אהרון צדוק — ארבע-חמש שנים אחרי נחיתתו בחוף יפו, בשם המשפחה המקורי צאלח, ולפני נישואיו. (דירוג: ככל הנראה — הגיל גוזר לידה ב-1895/96 מול 1898 שבפנקס תש\"ט, ואילו רשומת אהרן צאלח השנייה (ירושלים 1926, גיל 28) גוזרת בדיוק 1898; והשם על הסריקה טרם אושר בעיניים.)"),
    dict(crop="docs/igra/igra_britconsul_jerusalem_1839_aruas_zoom.png",
         full="docs/igra/igra_britconsul_jerusalem_1838_1908_p173.jpg",
         ext="https://genealogy.org.il/AID/index.php",
         title="פנקס נתיני בריטניה של ירושלים — «10 · Apr. 8 · Salomo Aruas · Gibraltar» (1839)",
         cap="עמוד הפתיחה של פנקס נתיני בריטניה (ארכיון המדינה, סדרה 1838_1908_BritHebNabJer, קובץ סריקה 173). מתחת לכותרת השנה «1839»: שורה 9 — William Tanner Young ורעייתו, «Vice Consul afterwards Consul», ובעמודת ה-Date of arrival 4 בפברואר; ומיד אחריו שורה 10 — «Apr. 8 · Salomo Aruas · Gibraltar», ועמודות המגורים, המקצוע וההערות ריקות שלושתן. העמודה השנייה נושאת את הכותרת «Date of arrival» ולא תאריך רישום, ולכן 8.4.1839 מתנגש ב«עלה 1833» של מפקד מונטיפיורי 1855; שתי השנים נמסרות זו לצד זו. באותו עמוד שני רישומי גיברלטר נוספים, שניהם ממשפחת אמזלג: Joseph Amzalag (1837, ירושלים, «Died leaving 3 sons») ו-Moses Amzalag and Lady (13.7.1840, ירושלים, נפטר 19.10.1858). הסריקה התקבלה מוועדת הוובמאסטר של IGRA לאחר שקובצי הסדרה החזירו שגיאת 403 — באג שאותר בעקבות הפנייה. (דירוג: תוכן העמוד — מאומת, אומת בעיניים; זיהוי «Salomo Aruas» עם שלמה ארואץ של מפקד 1855 — ככל הנראה; יישוב 1833 מול 1839 — טעון אימות.)"),
    dict(crop="docs/family_docs/pariente_birthregister_leaf.png",
         full="docs/family_docs/pariente-family-book-2021.pdf",
         ext="https://www.nli.org.il/he/books/NNL_ALEPH997010400325605171/NLI",
         title="דף רישום הלידות מעיזבון יצחק פריינטה — «31 Decembre 1902 · Rosa Parente»",
         cap="דף שנמצא בעיזבון יצחק פריינטה ובו רשם, בצרפתית, את לידות ילדיו — ובהם אברהם-אברמינו «fils de Isaac Pariente et de Miriam Arwas, 14 Mars 1891», ויקטורין (לאה) 13.3.1901, רוזה 31.12.1902, משה 20.4.1905, גרציה ספטמבר 1894 — ובשורה האחרונה: «mariage 1922 Juillet». צולם בספר המשפחה (2021), עמ' 18; העותק המקומי המלא — הספר כולו. (דירוג: תוכן הדף — מאומת, נקרא בעיניים; ייחוסו ליד יצחק — כמעט ודאי; זהות «mariage 1922» כחתונת רוזה ואהרון — ככל הנראה.)"),
    dict(crop="docs/family_docs/ketubah_aharon_roza_5683.png",
         full="docs/family_docs/ketubah_textzoom.png",
         ext="https://www.nli.org.il/he/books/NNL_ALEPH997010400325605171/NLI",
         title="כתובת אהרן ורוזה — «אהרן... אברהם צדוק» · «רוזא... יצחק פאריינטי»",
         cap="הכתובה, המצולמת בספר המשפחה (עמ' 124) ומתויגת שם «תרפ\"ג». בגוש הטקסט קריאים בבירור, בכתב מודגש: החתן אהרן בן אברהם צדוק, הכלה רוזא בת יצחק פאריינטי, והסכום «שלוש מאות לי\"ם». זהו המסמך הראשוני בן-הזמן הראשון הנוקב בשם אביו של אהרון — אברהם. הערת תיארוך: גוף הספר נוקב «נישאו במקוה ישראל ב-1922», דף הרישום — «mariage 1922 Juillet» (תמוז תרפ\"ב), והכיתוב — תרפ\"ג; שורת התאריך בכתובה עצמה אינה קריאה בצילום — טעון דיוק. הגדלת גוש הטקסט — בקישור העותק המקומי. (דירוג: שמות החתן, הכלה והאבות — מאומת; שנת החתונה 1922/תרפ\"ג — טעון דיוק.)"),
    dict(crop="docs/family_docs/miriam_arwas_grave_trumpeldor.png",
         full="docs/family_docs/pariente-family-book-2021.pdf",
         ext="https://www.nli.org.il/he/books/NNL_ALEPH997010400325605171/NLI",
         title="מצבת מרים ארואס-פריינטה, בית העלמין טרומפלדור — ז' בתמוז התרע\"ו",
         cap="«מ\"ק ... הנפטרת בקצ\"י מ' מרים די פאריינטי, נע' ביום שב\"ק ז' לח' תמוז התרע\"ו, תנצב\"ה» (קיצורי שורות הפתיחה אינם חדים בצילום) — 8 ביולי 1916, במגפת הכולירה. המצבה: לוח שיש סדוק שנטל יצחק ממטבח בית הספר של מקווה ישראל, והיא ניצבת בטרומפלדור עד היום, «בחלקה השמאלי התחתון» כלשון כיתוב הספר (עמ' 23). תאריך הפטירה הראשוני הראשון של סבתא-רבתא של אברהם. (דירוג: תאריך הפטירה ומקום הקבורה — מאומת, המצבה נקראה בעיניים; הנסיבות — ככל הנראה, פרוזת הספר.)"),
    dict(crop="docs/family_docs/yosef_arwas_1892_mikveh.png",
         full="docs/family_docs/pariente-family-book-2021.pdf",
         ext="https://www.nli.org.il/he/books/NNL_ALEPH997010400325605171/NLI",
         title="יוסף ארואס בתצלום סגל מקווה ישראל, 1892 — הדור השישי, פנים אל פנים",
         cap="כיתוב הספר (עמ' 56): «מקוה ישראל, 1892. עומדים בשורה העליונה מימין יצחק פריינטה, לידו עומד יוסף ארוואץ (אבי מרים ארוואץ-פריינטה), במרכז מנהל בית-הספר החקלאי מקוה ישראל, יוסף נייגו וצוות העובדים». יוסף ארואס — «סוחר מיפו» וסוכן הקניות של מקווה ישראל לפי הספר, הצראף של רשומת הקונסוליה מ-1869 לפי הקורפוס — לצד חתנו. (דירוג: זיהוי הדמויות — ככל הנראה, על אחריות כיתוב הספר.)"),
dict(crop="docs/family_docs/israelalbum/ia_012_yitzhak_grandchildren_1936.jpg",
         full="docs/family_docs/israelalbum/ia_012_yitzhak_grandchildren_1936.jpg",
         ext="https://israelalbum.org.il/image-page/?type=objects&id=9700.0004.012",
         title="יצחק פריינטה עם נכדיו, מקווה ישראל 1936 — צילומו המוקדם ביותר של אברהם",
         cap="פריט 9700.0004.012 באוסף האלבום של ישראל. הסב יצחק «הפפו» במרכז, מוקף נכדיו; לפי רישום האתר עומדים מימין: מיקו בכר, «אברהם צדוק» — נושא המחקר, בן עשר או אחת-עשרה (חודש הצילום אינו ידוע) — «יעל צדוק», עמנואל ביטרן, מרים בלומברג, גאולה ביטרן, בנימין בלומברג; בשורה השנייה, לצד הסב: «מרים צדוק» (קיקה) ומרים בכר; למטה: דוד בלומברג ועליזה ביטרן. עמנואל ביטרן נפל לימים במלחמת העצמאות. (דירוג: זיהוי הדמויות — ככל הנראה, על אחריות כיתוב האתר.)"),
    dict(crop="docs/family_docs/israelalbum/ia_008_miriam_grave_trumpeldor.jpg",
         full="docs/family_docs/israelalbum/ia_008_miriam_grave_trumpeldor.jpg",
         ext="https://israelalbum.org.il/image-page/?type=objects&id=9700.0004.008",
         title="מצבת מרים — צילום ישיר מטרומפלדור (אוסף האלבום של ישראל)",
         cap="פריט 9700.0004.008: צילום ישיר של המצבה — לצד הצילום שבספר (איור קודם): «מ' מרים די פאריינטי נ\"ע יום שב\"ק ז' לח' תמוז התרע\"ו תנצב\"ה». בדיקת לוח השנה: ז' בתמוז תרע\"ו חל בשבת, 8.7.1916 — «יום שב\"ק» שעל האבן מתאשש. (דירוג: מאומת — נקרא בעיניים משני צילומים בלתי-תלויים.)"),
    dict(crop="docs/family_docs/israelalbum/ia_036_abramino_postcard_back.jpg",
         full="docs/family_docs/israelalbum/ia_036_abramino_postcard_back.jpg",
         ext="https://israelalbum.org.il/image-page/?type=objects&id=9700.0004.036",
         title="גלוית «אברמינו» לדודה סמוחה — חתימת Albert Pariente (1913-1915)",
         cap="פריט 9700.0004.036: גב תצלומו של אברהם-אברמינו, בלאדינו באותיות לטיניות: «Souvenir a ma très chère tante Samouha afin qu'il voit que Abramino no se olvidé de ella y siempre se acuerda — Albert Pariente» — «מזכרת לדודתי היקרה מאוד סמוחה, שתראה שאברמינו לא שכח אותה ותמיד זוכר». כתב ידו וחתימתו של הבכור שירד לארגנטינה — הגשר בין «אברמינו» של דף הרישום ל«אלברט» של ארגנטינה. (דירוג: המסמך — מאומת; תיארוך 1913-1915 — כיתוב האתר, ככל הנראה.)"),
]

_fig_n = [0]
def evid_fig(e):
    _fig_n[0] += 1
    # image click opens the ORIGINAL document (external) when available; local copy always linked
    click = e.get('ext') or e['full']
    title = _html.escape(e['title'])
    alt   = _html.escape(e.get('alt') or ('צילום הראיה: ' + e['title']))
    ext_link = (f' · <a href="{_html.escape(e["ext"])}" target="_blank" rel="noopener" '
                f'aria-label="המסמך המקורי באתר המקור — {title}">המסמך המקורי ↗</a>'
                if e.get('ext') else '')
    cls = ''
    if 'portrait' in e['crop']:
        cls = ' class="portrait"'
    elif _PILImage is not None and os.path.exists(e['crop']):
        try:
            with _PILImage.open(e['crop']) as _im:
                if _im.height / _im.width > 1.15: cls = ' class="tall"'
        except Exception: pass
    return f'''<figure class="evi">
  <a href="{_html.escape(click)}" target="_blank" rel="noopener" aria-label="פתיחת המקור של: {title}">
    <img src="{_html.escape(e['crop'])}"{_img_dims(e['crop'])}{cls} alt="איור {_fig_n[0]}: {alt}" decoding="async"></a>
  <figcaption><b>איור {_fig_n[0]} — {title}</b><br>{_html.escape(e['cap'])}<br>
    <a href="{_html.escape(e['full'])}" target="_blank" rel="noopener" aria-label="העותק המקומי — {title}">העותק המקומי</a>{ext_link}</figcaption>
</figure>'''

evidence_html = "\n".join(evid_fig(e) for e in EVID)
# certainty ratings inside figure captions get the same chip as in the body
evidence_html = re.sub(r'\((דירוג:[^()]*(?:\([^()]*\)[^()]*)*)\)',
                       lambda m: '<em class="rank">' + m.group(1).replace('דירוג', '<b>דירוג</b>', 1) + '</em>',
                       evidence_html)

def _toc_label(txt):
    t = txt.split(' — ')[0].strip()
    m = re.match(r'\s*([0-9]+)\.\s*(.*)', t)
    if not m: return t
    num, rest = m.group(1), m.group(2)
    if ':' in rest:                     # "קורות חיים: נעורים" -> keep the distinguishing half
        head, tail = [p.strip() for p in rest.split(':', 1)]
        rest = tail or head
    return f'{num}. {rest}'

_skip = set()
toc_items = "".join(
    f'<a href="#{aid}" title="{_html.escape(txt)}">{_html.escape(_toc_label(txt))}</a>'
    for aid, txt in _toc if aid not in _skip)

PAGE = f'''<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>אברהם צדוק — סיפור משפחה ממקווה ישראל</title>
<meta name="description" content="מסמך מחקר מתועד ומקושר־מקורות על אברהם צדוק (1925-2017), יליד מקווה ישראל, ועל שורשי משפחתו — פריינטה וארואס מיפו וגיברלטר, וצדוק (צאלח) מצנעא.">
<style>
 :root{{--ink:#2b2b2b;--gold:#8a5a00;--accent:#b8860b;--paper:#fbf7ef;--line:#d8ccb0;--soft:#5f5133}}
 *{{box-sizing:border-box}}
 html{{scroll-behavior:smooth;overflow-x:clip}}
 body{{font-family:"Segoe UI",Arial,sans-serif;color:var(--ink);background:#efe9dc;margin:0;
       font-size:17px;line-height:1.75}}
 .doc{{max-width:790px;margin:0 auto;background:#fff;padding:0 0 60px;box-shadow:0 1px 20px rgba(0,0,0,.08)}}
 body{{overflow-x:clip}}
 /* full-bleed: 100vw counts the scrollbar, so subtract its measured width (--sbw) */
 .bleed{{width:calc(100vw - var(--sbw,0px));max-width:none;
     margin-inline:calc(50% - 50vw + var(--sbw,0px)/2)}}
 .hero{{background:linear-gradient(135deg,#3a2f1c,#6b5324);color:#fbf3df;padding:40px 34px 30px}}
 .hero h1{{margin:0 0 6px;font-size:30px}}
 .hero .sub{{font-size:17px;color:#f0e2bd}}
 .hero .meta{{color:#e8d6a8;font-size:14px;margin-top:10px}}
 .body{{padding:8px 34px}}
 h1,h2,h3,h4{{line-height:1.4}}
 section[id]{{scroll-margin-top:56px}}
 h2{{font-size:23px;border-bottom:2px solid var(--line);padding-bottom:6px;margin-top:40px;color:#4a3a1a;
     scroll-margin-top:64px}}
 h3{{font-size:20px;color:#5a4620;margin-top:32px;border-inline-start:4px solid var(--line);
     padding-inline-start:10px;scroll-margin-top:64px}}
 h4{{font-size:18.5px;color:#4a3a1a;margin:28px 0 8px;scroll-margin-top:64px;
     letter-spacing:.01em;border-bottom:1px dotted var(--line);padding-bottom:4px}}
 h4::before{{content:"";display:inline-block;width:14px;border-top:2px solid var(--line);
     vertical-align:middle;margin-inline-end:8px}}
 p{{orphans:3;widows:3}}
 blockquote{{border-inline-start:4px solid var(--accent);background:var(--paper);margin:16px 0;
     padding:12px 18px;border-start-end-radius:8px;border-end-end-radius:8px;color:#4a3f28;font-size:16px}}
 a{{color:var(--gold)}}
 a:focus-visible,summary:focus-visible{{outline:3px solid var(--gold);outline-offset:2px;border-radius:3px}}
 em{{color:var(--soft);font-style:normal;font-size:.92em}}
 em.rank{{display:inline-block;font-size:13px;line-height:1.5;color:#4a3f28;background:#f4efe2;
     border:1px solid var(--line);border-inline-start:3px solid var(--accent);border-radius:4px;
     padding:1px 9px;margin:2px 0;font-style:normal}}
 em.rank b{{color:var(--gold);font-weight:700}}
 ul{{padding-inline-start:24px}}
 /* citations: numbered superscripts that jump to the sources index and back */
 sup.cite{{font-size:.72em;line-height:0;vertical-align:super;white-space:nowrap}}
 sup.cite a{{text-decoration:none;color:var(--gold);background:#f6f0e2;border:1px solid #e2d6ba;
     border-radius:4px;padding:0 3px;margin-inline-start:1px}}
 sup.cite a:hover,sup.cite a:focus{{background:#efe4ca}}
 sup.cite:target a{{background:#f4d58d;color:#4a3000;outline:2px solid var(--gold)}}
 sup.cite{{scroll-margin-top:96px}}
 h3[id^="src-"]{{scroll-margin-top:64px}}
 h3[id^="src-"]:target{{background:#fdf6e3;box-shadow:inset 0 0 0 2px var(--accent)}}
 .srcnum{{display:inline-block;min-width:2.1em;color:var(--gold);font-weight:700}}
 .backlinks{{font-size:13px;color:var(--soft);margin:-4px 0 10px}}
 .backlinks a{{text-decoration:none;padding:0 4px;border:1px solid var(--line);border-radius:4px;
     margin-inline-end:3px;display:inline-block}}
 .backlinks a:hover{{background:#efe4ca}}
 table{{border-collapse:collapse;margin:14px 0;font-size:15.5px;width:100%}}
 .tablewrap table{{min-width:420px}}
 th,td{{border:1px solid var(--line);padding:6px 10px;text-align:start;vertical-align:top}}
 thead th{{background:var(--paper);color:#4a3a1a}}
 tbody tr:nth-child(even){{background:#fdfbf6}}
 .tablewrap{{overflow-x:auto;-webkit-overflow-scrolling:touch}}
 .tablewrap:focus-visible{{outline:3px solid var(--gold);outline-offset:2px}}
 /* the tree is the synthesis of the whole document — give it real width and let it scroll */
 .tree-embed{{margin-block:24px;
     border-block:1px solid var(--line);background:#fff;padding:10px 0;
     overflow-x:auto;-webkit-overflow-scrolling:touch}}
 .tree-embed:focus-visible{{outline:3px solid var(--gold);outline-offset:-3px}}
 .tree-embed svg{{width:max(1180px,100%);min-width:1180px;max-width:1648px;height:auto;
     display:block;margin:0 auto}}
 .tree-hint{{font-size:13px;color:var(--soft);text-align:center;margin:-14px 0 18px}}
 .evi{{margin:26px 0;border:1px solid var(--line);border-radius:12px;background:var(--paper);
     padding:12px;text-align:center}}
 .evi img{{width:100%;max-width:100%;height:auto;border:1px solid #cdbf9e;border-radius:8px;cursor:zoom-in}}
 .evi img.portrait{{width:260px;max-width:100%;height:auto;aspect-ratio:192/256}}
 .evi img.tall{{width:min(100%,460px);height:auto}}
 .evi figcaption{{font-size:14px;color:#4a3f28;margin:10px auto 0;text-align:start;line-height:1.65;max-width:64ch}}
 .toc{{background:var(--paper);border-block-end:1px solid var(--line);padding:7px 34px;
     margin:0 -34px 22px;font-size:14px;position:sticky;top:0;z-index:5;
     white-space:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch;
     box-shadow:0 2px 10px rgba(0,0,0,.06);scrollbar-width:thin}}
 .toc b{{color:#4a3a1a}}
 .toc a{{text-decoration:none;display:inline-block;padding:2px 7px;border-radius:5px}}
 .toc a:hover{{background:#efe4ca}}
 .toc .grp{{margin-inline-start:6px;border-inline-start:1px solid var(--line);padding-inline-start:8px}}
 .btn{{display:inline-block;background:var(--gold);color:#fff;padding:8px 16px;border-radius:8px;
     text-decoration:none;font-weight:700;margin:8px 0}}
 .top{{position:fixed;inset-inline-start:max(6px,calc(50% - 460px));inset-block-end:14px;background:#fff;color:var(--gold);
     border:1px solid var(--line);border-radius:50%;width:44px;height:44px;line-height:42px;
     text-align:center;text-decoration:none;font-size:20px;box-shadow:0 2px 10px rgba(0,0,0,.12);z-index:6}}
 footer{{text-align:center;color:#6f6045;font-size:13px;padding:24px}}
 hr{{border:none;border-top:1px solid var(--line);margin:30px 0}}
 hr + h2{{margin-top:14px;border-top:none}}
 @media (max-width:680px){{
   body{{font-size:16.5px}}
   .body{{padding:8px 16px}} .hero{{padding:26px 16px 20px}} .hero h1{{font-size:24px}}
   h2{{font-size:20px;margin-top:30px}} h3{{font-size:18px}} h4{{font-size:17.5px}}
   .tree-embed{{margin-block:20px}}
   .evi{{padding:8px;margin-inline:-6px}} .evi figcaption{{font-size:13.5px}}
   .toc{{font-size:13px;padding:6px 16px;margin:0 -16px 18px}}
   sup.cite a{{padding:0 2px}}
   table{{font-size:14px}} th,td{{padding:5px 7px}}
   .top{{width:36px;height:36px;line-height:34px;font-size:16px;opacity:.9;
        inset-inline-start:auto;inset-inline-end:8px;inset-block-end:8px}}
   .doc{{padding-bottom:76px}}
 }}
 @media print{{
   @page{{size:A4;margin:16mm 14mm}}
   @page landscape{{size:A4 landscape;margin:10mm}}
   html,body{{overflow:visible!important}}   /* clip is for the screen; it crops the print page */
   body{{background:#fff;font-size:11pt;line-height:1.5}}
   .doc{{max-width:none;box-shadow:none;padding-bottom:0}}
   .hero{{background:#fff!important;color:#2b2b2b;border-bottom:3px solid var(--accent);padding:0 0 12px}}
   .hero h1{{color:#2b2b2b}} .hero .sub,.hero .meta{{color:#5a4620!important}}
   .toc,.btn,.top,.tree-hint,.backlinks{{display:none!important}}
   sup.cite a{{background:none;border:none;color:#5a4620;padding:0}}
   .body{{padding:0}}
   blockquote,table,.tree-embed{{break-inside:avoid}}
   figure.evi{{break-inside:auto;page-break-inside:auto;margin:10px 0;padding:0;border:none;background:none}}
   figure.evi img{{max-height:150mm;width:auto;max-width:100%}}
   figure.evi figcaption{{break-before:avoid;font-size:9pt;line-height:1.4}}
   h2,h3,h4{{break-after:avoid}}
   #tree{{break-before:page;break-after:page;page:landscape}}
   .tree-embed,.bleed{{margin:0!important;border:none;overflow:visible;
       width:100%!important;max-width:100%!important}}
   /* Chromium lays out print at the FIRST page's width, so a named landscape page leaves
      ~30% of the sheet unused; scale the tree back up to fill it. */
   /* no transform here: scaling from a corner pushed the lower generations off the sheet.
      A complete tree at 6.6pt beats a cropped one at 8.8pt. */
   .tree-embed svg{{width:100%!important;min-width:0!important;max-width:none!important;height:auto}}
   #tree::after{{content:"התרשים מודפס בגודל מוקטן כדי להיכנס לגיליון אחד. לעותק גדול וקריא יותר: הדפיסו על גיליון A3, או פתחו את עמוד העץ הנפרד.";
       display:block;font-size:8pt;color:#5a4620;text-align:center;margin-top:8px}}
   #tree h2{{font-size:13pt;margin:0 0 4px;border:none}}
   #sources a[href^="http"]::after{{content:" ‹" attr(href) "›";font-size:8pt;color:#5a4620;word-break:break-all}}
   footer{{color:#444}}
 }}
</style></head><body>
<a class="top" href="#top" aria-label="חזרה לראש העמוד">↑</a>
<div class="doc" id="top">
 <header class="hero">
   <h1>שורשיה של משפחה ממקווה ישראל</h1>
   <div class="sub">אברהם צדוק (1925-2017) — מחקר תיעודי מקושר-מקורות בגנאלוגיה משפחתית</div>
   <div class="meta">מהדורה {EDITION} · אלול תשפ״ו / אוגוסט 2026</div>
 </header>
 <main class="body">
   <nav class="toc" aria-label="תוכן עניינים">
     <b>מקטעים:</b>
     <a href="#report">פתיח</a><a href="#tree">עץ המשפחה</a><a href="#evidence">גלריית ראיות</a><a href="#sources">אינדקס מקורות</a>
<span class="grp"><b>פרקים:</b>{toc_items}</span>
   </nav>

   <section id="report">{report_html}</section>

   <hr>
   <section id="tree" aria-labelledby="tree-h">
     <h2 id="tree-h">נספח א: עץ המשפחה</h2>
     <div class="tree-embed bleed" tabindex="0" role="group" aria-label="תרשים עץ המשפחה — ניתן לגלול לצדדים">{tree_svg}</div>
     <p class="tree-hint">במסך צר: גללו את התרשים לצדדים. מקרא מלא וסייגים — בעמוד העץ.</p>
     <a class="btn" href="tree.html" target="_blank" rel="noopener">פתיחת העץ בעמוד מלא ↗</a>
   </section>

   <hr>
   <section id="evidence" aria-labelledby="evidence-h">
     <h2 id="evidence-h">נספח ב: גלריית ראיות</h2>
     <p>{_fig_n[0]} איורים — צילומי המסמכים שעליהם נשען המאמר. לכל איור מקושר עותק מקומי השמור
        בתיקיית המחקר, ולרובם גם המסמך המקורי באתר המקור (לחיצה על התמונה). שני איורים מקושרים
        לעותק המקומי בלבד — סריקה שהמאגר חדל להגיש, ועץ גנאלוגי פרטי; הכיתוב מציין זאת.</p>
     {evidence_html}
   </section>

   <hr>
   <section id="sources">{sources_html}</section>

   <hr>
   <section id="changelog">{changelog_html}</section>
 </main>
 <footer>מסמך זיכרון משפחתי · נבנה ממקורות מתועדים · מהדורה {EDITION} · אוגוסט 2026</footer>
</div>
<script>
(function(){{var r=document.documentElement;
 function m(){{r.style.setProperty('--sbw',(window.innerWidth-r.clientWidth)+'px');}}
 m(); addEventListener('load',m); addEventListener('resize',m);}})();
</script>
</body></html>'''

# wide tables must scroll inside their own box, never the page
PAGE = PAGE.replace('<table>',
    '<div class="tablewrap" tabindex="0" role="group" aria-label="טבלה — ניתן לגלול לצדדים"><table>'
    ).replace('</table>', '</table></div>')

# --- gate: no broken local target may reach disk ---
def _targets_of(*texts):
    t = set()
    for tx in texts:
        t |= set(re.findall(r'(?:href|src)="([^"]+)"', tx))
        t |= set(re.findall(r'\]\(([^)\s]+)\)', tx))
    return t
_changelog_md = open('CHANGELOG.md', encoding='utf-8').read()
_tg = _targets_of(PAGE, report_md, sources_md, _changelog_md)
_miss = [t for t in _tg
         if not t.startswith(('http','#','mailto:','data:','`'))
         and urllib.parse.unquote(t.split('#')[0])
         and not os.path.exists(urllib.parse.unquote(t.split('#')[0]))]
assert not _miss, f"BROKEN LOCAL TARGETS: {_miss}"

# --- gate: every citation marker in the source must survive into the page ---
_markers = len(re.findall(r'\[\[[0-9]+[אבגד]?\]\]', report_md))
_rendered = PAGE.count('<sup class="cite"')
assert _markers == _rendered, (
    f"CITATION LOSS: {_markers} markers in report.md but {_rendered} rendered "
    f"(a marker adjacent to '(' or ']' is swallowed by Markdown link syntax)")
assert '[[' not in PAGE, "UNCONVERTED CITATION MARKER left in the page"
print(f"cite-check: {_rendered} citations rendered from {_markers} markers")

# --- gate: a page with a broken in-page anchor must never reach disk ---
_ids = set(re.findall(r'id="([^"]+)"', PAGE))
_anchors = {t[1:] for t in re.findall(r'href="(#[^"]+)"', PAGE)}
_bad = sorted(a for a in _anchors if a not in _ids)
assert not _bad, f"BROKEN IN-PAGE ANCHORS: {_bad}"
print(f"anchor-check: {len(_anchors)} in-page anchors OK ({len(_ids)} ids)")

# --- gate: declared counts and rendering invariants must match reality ---
_src_n  = len(re.findall(r'<h3 id="src-', PAGE))
_fig_ct = len(re.findall(r'<b>איור \d+ —', PAGE))
_HEB_NUM = {'אפס':0,'אחד':1,'אחת':1,'שניים':2,'שתיים':2,'שלושה':3,'שלוש':3,'ארבעה':4,'ארבע':4,
            'חמישה':5,'חמש':5,'שישה':6,'שש':6,'שבעה':7,'שבע':7,'שמונה':8,'תשעה':9,'תשע':9,
            'עשרה':10,'עשר':10,'אחד עשר':11,'אחת עשרה':11,'שנים עשר':12,'שתים עשרה':12,
            'שלושה עשר':13,'שלוש עשרה':13,'ארבעה עשר':14,'ארבע עשרה':14,'חמישה עשר':15,
            'חמש עשרה':15,'שישה עשר':16,'שש עשרה':16,'שבעה עשר':17,'שבע עשרה':17,
            'שמונה עשר':18,'שמונה עשרה':18,'תשעה עשר':19,'תשע עשרה':19,'עשרים':20,
            'עשרים ואחד':21,'עשרים ואחת':21,'עשרים ושניים':22,'עשרים ושתיים':22,
            'עשרים ושלושה':23,'עשרים ושלוש':23,'עשרים וארבעה':24,'עשרים וארבע':24,
            'עשרים וחמישה':25,'עשרים וחמש':25,'עשרים ושישה':26,'עשרים ושש':26,
            'עשרים ושבעה':27,'עשרים ושבע':27,'עשרים ושמונה':28,'עשרים ותשעה':29,
            'עשרים ותשע':29,'שלושים':30,'שלושים ואחד':31,'שלושים ואחת':31}
# normalise: hyphens between Hebrew number words are a spelling variant of a space
_scan = re.sub(r'(?<=[\u0590-\u05FF])-(?=[\u0590-\u05FF])', ' ', report_md + '\n' + PAGE)
_HEB_ALT = '|'.join(sorted((re.escape(w) for w in _HEB_NUM), key=len, reverse=True))

def _declared(nouns):
    out = []
    pat_d = r'(\d+)\s+(?:' + '|'.join(nouns) + r')'
    out += [int(x) for x in re.findall(pat_d, _scan)]
    pat_w = r'(' + _HEB_ALT + r')\s+(?:' + '|'.join(nouns) + r')'
    out += [_HEB_NUM[w] for w in re.findall(pat_w, _scan)]
    return out

# sources: digits only — Hebrew number words legitimately appear as subset counts
#          ("שני מקורות", "בארבעה ערכים"), so word-form scanning would false-positive.
_decl_src = [int(x) for x in re.findall(r'(\d+)\s+(?:מקורות|ערכים|ערכי מקור)', _scan)]
_decl_fig = _declared(['איורים', 'ראיות מצולמות'])
_bad_counts = []
for d in _decl_src:
    if d != _src_n: _bad_counts.append(f"declared {d} sources but {_src_n} entries exist")
for d in _decl_fig:
    if d != _fig_ct: _bad_counts.append(f"declared {d} figures but {_fig_ct} rendered")
_rank_left = len(re.findall(r'<em>\(דירוג', PAGE)) + len(re.findall(r'(?<!class="rank">)\(דירוג', PAGE))
if _rank_left: _bad_counts.append(f"{_rank_left} certainty ratings did not get a .rank chip")
if '</em><em>' in PAGE: _bad_counts.append("nested emphasis collapsed to </em><em> (bold inside italic)")
assert not _bad_counts, "COUNT/RENDER MISMATCH: " + "; ".join(_bad_counts)
print(f"count-check: {_src_n} sources, {_fig_ct} figures, all ratings chipped")

open(MAIN_HTML,'w',encoding='utf-8').write(PAGE)

# --- site/ copy (self-contained static) ---
site='site'
if os.path.exists(site): shutil.rmtree(site)
os.makedirs(site)
shutil.copy(MAIN_HTML, os.path.join(site, MAIN_HTML))
shutil.copy('tree.html', os.path.join(site,'tree.html'))
shutil.copytree('docs', os.path.join(site,'docs'))
# privacy guard: the full Cohn-2005 PDF (living persons' contact data) must not enter the site copy
_priv=os.path.join(site,'docs','family_docs','israelalbum','cohn2005_pariente_descendant_tree.pdf')
if os.path.exists(_priv): os.remove(_priv)
assert not os.path.exists(_priv), 'PRIVACY GUARD FAILED'
# copy linked md/txt referenced from sources so their links resolve under site/
for extra in ['report.md','sources-index.md','CHANGELOG.md']:
    shutil.copy(extra, os.path.join(site,extra))
# index redirect
redir = f'''<!doctype html><html lang="he" dir="rtl"><meta charset="utf-8"><title>אברהם צדוק — סיפור משפחה</title>
<meta http-equiv="refresh" content="0; url={urllib.parse.quote(MAIN_HTML)}">
<script>location.replace("{urllib.parse.quote(MAIN_HTML)}")</script>
<a href="{urllib.parse.quote(MAIN_HTML)}">אברהם צדוק — סיפור משפחה</a></html>'''
open('index.html','w',encoding='utf-8').write(redir)
shutil.copy('index.html', os.path.join(site,'index.html'))
open(os.path.join(site,'.nojekyll'),'w').close()

# verify targets exist under site/
site_targets = _targets_of(open(os.path.join(site,MAIN_HTML),encoding='utf-8').read())
site_missing=[]
for t in site_targets:
    if t.startswith(('http','#','mailto:','data:','`')): continue
    p=os.path.join(site,urllib.parse.unquote(t.split('#')[0]))
    if not os.path.exists(p): site_missing.append(t)
assert not site_missing, f"BROKEN SITE TARGETS: {site_missing}"
print("site/ built and verified.")
print("MAIN:", MAIN_HTML)
