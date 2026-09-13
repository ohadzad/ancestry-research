# -*- coding: utf-8 -*-
"""rachel-zadok — the project's own data. The engine lives in ../common/genealogy_site."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(ROOT), 'common'))

from genealogy_site import ProjectConfig, Palette, TreeSource, SpineFact, Person, build  # noqa: E402
from genealogy_site import Story, Beat, DocCard, Verdict                                  # noqa: E402
from genealogy_site import figures as F                                                   # noqa: E402

R = lambda *p: os.path.join(ROOT, *p)          # noqa: E731

# ---------------------------------------------------------------- palette --
PAL = Palette(
    accent='#7a5c1e', accent_soft='#a8781f', link='#7d5310',
    paper='#faf7f2', ink='#2b2620', muted='#6a6154', line='#e2dbcc',
    hero_from='#33291a', hero_to='#6b5324',
)

# ---------------------------------------------------------------- figures --
EV = 'docs/evidence/'
AR = 'docs/arolsen_stutthof/'
figs = {}


def fig(key, src, cap, local=None, online=None, thumb=None):
    s = F.thumb(ROOT, src, thumb) if thumb else src
    figs[key] = F.figure(ROOT, s, cap, local=local or src, online=online)


fig('koblasa', EV + 'koblasa_1928_row_zoom.png',
    'שורת אוקרמזו (וולובה) בטבלת האחוזות הגדולות של רוס הקרפטית, 1928: 4,515 הקטר — '
    'בעלים: <bdi dir="ltr">Krausz, Farkas, Rappaport</bdi>',
    local='docs/koblasa_1928_estates_podkarpatska_rus.pdf',
    online='https://www.nacr.cz/wp-content/uploads/2024/04/PH_23_2_2015_Koblasa.pdf')
fig('vater', EV + 'stutthof_vater_auschwitz_zoom.png',
    'מכרטיס האסירה של רחל בשטוטהוף: <bdi dir="ltr">"Wohnort d. Angehörigen: Vater Lajos S. z.Zt. Auschwitz"</bdi> '
    '— "מקום מגורי הקרובים: האב לאיוש ס׳, כעת אושוויץ"',
    local=AR + '105591047_001.jpg',
    online='https://collections.arolsen-archives.org/en/search/?s=Strulowits%20Ruci')
fig('einge', EV + 'stutthof_eingewiesen_zoom.png',
    'באותו כרטיס: <bdi dir="ltr">"Eingewiesen am 29.6.44, durch KL. Auschwitz, in KL. Stutthof"</bdi> — '
    'נקלטה בשטוטהוף ב-29.06.1944, מאושוויץ', local=AR + '105591047_001.jpg')
fig('sig', EV + 'bogen_signature_zoom.png',
    'חתימתה של רחל, בת 15, בתחתית שאלון הקליטה בשטוטהוף: <bdi dir="ltr">"Sztrulovics Ruci"</bdi>',
    local=AR + '105591037_001.jpg')
fig('rose', EV + 'rose_kl_au_zoom.png',
    'כרטיס ההפניה על שם האם במרשם שטוטהוף: <bdi dir="ltr">"STRULAWITS geb. FARKAS, Rose — K.L. Au."</bdi> (מחנה אושוויץ)',
    local=AR + '105590980_001.jpg')
fig('leipheim', EV + 'cni_leipheim_zoom.png',
    'מכרטיס מרשם השמות המרכזי בארולסן: <bdi dir="ltr">"Jetzige Adresse: Leipheim Bl. 24"</bdi> — '
    'מחנה העקורים ליפהיים, בלוק 24',
    local='docs/arolsen_dp/cni_farkas_rachel_001.jpg',
    online='https://collections.arolsen-archives.org/en/document/67014250')
fig('census1921', 'docs/hungaricana_1921_census_koselovo_house30_full.png',
    'גיליון מפקד 1921 המקורי במלואו — בית מס\' 30 בקושלובו: יעקב ראש הבית, שרה ("Rapaport Sura") אשתו, '
    'ושלושה-עשר ילדים; וחתימת הפוקד, "Koselovo, 16 בפברואר 1921". '
    'שני העמודים שמורים גם כ<a href="docs/hungaricana_1921_census_koselovo_house30_pages299-300_original.pdf">PDF מקורי</a>.',
    local='docs/hungaricana_1921_census_koselovo_house30_full.png',
    online='https://library.hungaricana.hu/hu/view/KANepszaml_006_Huszt_Keselyumezo__097_Koseleve-Keselymezo/?pg=298&layout=s',
    thumb=900)
fig('gedalya_m', EV + 'jewishgen_gedajlo_mindje_marriage_1903_zoom.png',
    'הרישום האזרחי של נישואי גדליה רפפורט (04.03.1903, אוקרמזו): נולד 01.04.1846, '
    'בן <bdi dir="ltr">Mozes</bdi> רפפורט ו<bdi dir="ltr">Jenta</bdi> שפיגל; הכלה מינדל ברקוביץ ילידת 04.01.1865',
    thumb=760)
fig('gitel_m', EV + 'jewishgen_gitel_wolf_1933_mendel_1938_marriages_zoom.png',
    'נישואי הדודה גיטל ("<bdi dir="ltr">Strulovic Githel</bdi>", בת <bdi dir="ltr">Jakub</bdi> ו-<bdi dir="ltr">Rapaport Serena</bdi>) '
    'לאלכסנדר וולף, איזה 10.02.1933 — העד: אחיה יצחק; ומתחת: נישואי הדוד מנדל (1938)', thumb=760)
fig('regina_m', EV + 'jewishgen_regina_1896_bat_szura_rappaport_birth_zoom.png',
    'רשומת הלידה של הדודה ריבקה/רגינה (24.05.1896): "<bdi dir="ltr">Regina</bdi>, בת '
    '<bdi dir="ltr">Rappaport Szura</bdi> מאוקרמזו, בת 22, עקרת בית" — ללא שם אב: '
    'הדוגמה המובהקת לרישום ילדי הזוג על שם האם', thumb=760)

FIGURE_ANCHORS = [
    (r'אחוזת רפפורט באוקרמזו לאורך יותר מ-40 שנה', 'koblasa'),
    (r'נשא שלוש נשים', 'gedalya_m'),
    (r'המבוגרים שבהם רשומים', 'census1921'),
    (r'בעל מכולת בטקהאזה; שניהם נרצחו', 'gitel_m'),
    (r'כנראה עיגול גיל, שהיה שכיח', 'regina_m'),
    (r'ההורים היו רשומים כ"נמצאים כעת באושוויץ', 'vater'),
    (r'תאריך ההגעה לשטוטהוף: 29 ביוני 1944', 'einge'),
    (r'החתימה של רחל, בת 15, בשטוטהוף', 'sig'),
    (r'כרטיס הפניה, לא תיק אסירה', 'rose'),
    (r'מחנה העקורים ליפהיים:', 'leipheim'),
]

# ---------------------------------------------------------------- gallery --
_G = [
    (AR + '105591047_001.jpg', 'כרטיס האסירה של רחל, שטוטהוף (38444)'),
    (AR + '105591037_001.jpg', 'שאלון הקליטה של רחל, עם חתימתה'),
    (AR + '105591030_001.jpg', 'כרטיס האסירה של סימה (38443)'),
    (AR + '105590980_001.jpg', 'כרטיס הפניה — האם רוזה'),
    (AR + '105590973_001.jpg', 'כרטיס הפניה — האב לאיוש'),
    ('docs/arolsen_dp/cni_farkas_rachel_001.jpg', 'כרטיס העקורים — ליפהיים'),
    ('docs/yadvashem_pot_scans/10846653_04122013_8915_158.jpg', 'דף עד על האב, בכתב ידה (2013)'),
    ('docs/yadvashem_pot_scans/10846654_04122013_8915_159.jpg', 'דף עד על האם, בכתב ידה'),
    ('docs/yadvashem_pot_scans/10846655_04122013_8915_160.jpg', 'דף עד על גיטה, בכתב ידה'),
    ('docs/yadvashem_pot_scans/13750274_04122013_8915_161.jpg', 'דף עד על סימה, בכתב ידה'),
    ('docs/evidence/stutthof_transport_list_rows802-803_zoom.png', 'רשימת הטרנספורט 29.06.1944 — האחיות בשורות 802–803',
     'docs/stutthof_museum_2026/POL-AMS-I-IIb-10-099.jpg'),
    ('docs/hungaricana_1921_census_koselovo_house30_full.png', 'מפקד 1921 — גיליון בית 30 בקושלובו',
     'docs/hungaricana_1921_census_koselovo_house30_pages299-300_original.pdf'),
    ('docs/evidence/jewishgen_rachel_sima_own_birth_records_zoom.png', 'רשומות הלידה של רחל וסימה (JewishGen)'),
    ('docs/evidence/jewishgen_births_strulyovics_rappaport_children_1897-1902_zoom.png', 'רשומות הלידה של דודי רחל (1897–1902)'),
    ('docs/cemeteries/cja_esjf_mizhhiria_484104_landa_dayan_1924_full.jpg', 'מצבת הדיין לאנדא, אוקרמזו (1924)'),
    ('docs/cemeteries/cja_esjf_mizhhiria_484143_cadastral_1864_full.jpg', 'מפת הקדסטר 1864 — בית הקברות היהודי'),
]
# a row is (crop, caption) or (crop, caption, the file the tile opens)
GALLERY = tuple((F.thumb(ROOT, row[0], 440), row[2] if len(row) > 2 else row[0], row[1])
                for row in _G if os.path.exists(R(row[0])))

# ------------------------------------------------------------- transforms --
YT = 'https://www.youtube.com/watch?v=GhHKFgl81AU'


def _ts(m):
    h, mn, s = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return (f'<a href="{YT}&amp;t={h*3600+mn*60+s}s" target="_blank" rel="noopener" '
            f'title="לצפייה ברגע זה בעדות">[{m.group(1)}:{m.group(2)}:{m.group(3)}]</a>')


def _ts_range(m):
    h, mn, s = int(m.group(1)), int(m.group(2)), int(m.group(3))
    lbl = (f'[<bdi dir="ltr">{m.group(1)}:{m.group(2)}:{m.group(3)}–'
           f'{m.group(4)}:{m.group(5)}:{m.group(6)}</bdi>]')
    return (f'<a href="{YT}&amp;t={h*3600+mn*60+s}s" target="_blank" rel="noopener" '
            f'title="לצפייה בקטע זה בעדות">{lbl}</a>')


def timestamps(t):
    t = re.sub(r'\[(\d{2}):(\d{2}):(\d{2})[–-](\d{2}):(\d{2}):(\d{2})\]', _ts_range, t)
    return re.sub(r'\[(\d{2}):(\d{2}):(\d{2})\]', _ts, t)


_AR_DOCS = {'105591037', '105591042', '105591047', '105591025', '105591030', '105590980', '105590973'}


def _ar(m):
    n = m.group(1)
    out = (f'<a href="https://collections.arolsen-archives.org/en/document/{n}" target="_blank" '
           f'rel="noopener" title="המסמך בארכיון ארולסן">{n}</a>')
    if n in _AR_DOCS and os.path.exists(R(AR + f'{n}_001.jpg')):
        out += f' <a class="doclink" href="{AR}{n}_001.jpg" aria-label="הסריקה בתיקייה" title="הסריקה בתיקייה"><span aria-hidden="true">📄</span></a>'
    return out


def arolsen(t):
    return re.sub(r'(?<![\w/."])(10559\d{4})(?![\w/])', _ar, t)


def _yv(m):
    i = m.group(1)
    return (f'<a href="docs/yadvashem_records/name_{i}.json">name_{i}.json</a> '
            f'<a href="https://collections.yadvashem.org/en/names/{i}" target="_blank" '
            f'rel="noopener" title="הרשומה באתר יד ושם">↗</a>')


_DIRS = ['docs/evidence/', 'docs/', 'docs/cemeteries/', 'docs/stutthof_museum_2026/',
         'docs/arolsen_stutthof/', 'docs/arolsen_dp/', 'docs/yadvashem_pot_scans/', 'docs/igra/']


def _file(m):
    name = m.group(1)
    for d in _DIRS:
        if os.path.exists(R(d + name)):
            return f'<a href="{d}{name}">{name}</a>'
    return name


def _testimony(m):
    n = m.group(1)
    he, en = f'docs/testimony_{n}_he.json', f'docs/testimony_{n}_en.json'
    if not (os.path.exists(R(he)) and os.path.exists(R(en))):
        return m.group(0)
    return (f'<a href="{he}">testimony_{n}_he.json</a> / '
            f'<a href="{en}">testimony_{n}_en.json</a>')


def sources_links(t):
    t = re.sub(r'(?<![\w/])testimony_(\d+)_he/en\.json', _testimony, t)
    t = re.sub(r'(?<!/)name_(\d+)\.json', _yv, t)
    return re.sub(r'(?<![\w/."=-])([\w][\w\-]*\.(?:png|jpg|JPG|jpeg|pdf))(?![\w/])', _file, t)


# ------------------------------------------------------------------ people -
P = Person
A_NAME = "#רשומת-הלידה-האזרחית-של-רחל-והפער-בן-ארבעת-הימים"
A_KEHILA = "#הקהילה-היהודית"
A_RAPP = "#משפחת-רפפורט-מבעלי-הקרקעות-הגדולים-של-העיירה"
A_G0 = "#דור-0-אבות-השושלת-תחילת-המאה-ה-19"
A_G1 = "#דור-1-הסבים-של-אריה-ורבקה-סבי-סביה-של-רחל"
A_G2 = "#דור-2-הסבים-של-רחל"
A_G3 = "#דור-3-ההורים-הדודים-והדודות"
A_G4 = "#דור-4-רחל-ואחיה"
A_G5 = "#דור-5-הדור-הבא"
A_CEM = "#בתי-העלמין-95-תצלומים-קריאה-מלאה"
A_GED = "#פרק-ז'-סיפור-ההצלה-של-גדליהו"

PEOPLE = (
    P('רחל ("רוצי") צדוק', '16.04.1929 – 01/2021', 'נושאת המחקר; אסירה 38444 בשטוטהוף',
      A_NAME, 'Ruchlja Ruci Rutzi Struljovic Strulovic Strulowits Sztrulyovics Sztrulovics '
              'Farkas Rappaport Rapaport רוצי רחל פרקש 38444'),
    P('אריה-לייב סטרולוביץ-רפפורט', '03/1894 – 1944', 'אביה; סוחר עורות, מת מרעב באושוויץ',
      A_G3, 'Leib Lajos Lojos Strulovits Strulovic Sztrulyovics Rappaport A-8557'),
    P('רבקה-רוזה פרקש', '25.04.1904 – 1944', 'אמה; נרצחה באושוויץ', A_G3, 'Rifka Rifke Rose Roza Farkas Fuchs'),
    P('סימה (Sari)', '26.12.1926 – 1944/45', 'אחותה; אסירה 38443, מתה בשטוטהוף', A_G4, 'Szima Sari Sary Semo Sima Strulowits 38443'),
    P('גיטה', '26.03.1936 – 1944', 'אחותה הקטנה; נרצחה באושוויץ בת שמונה', A_G4, 'Gizela Gitel Gitta'),
    P('דב', '1924/1926 – 1998', 'אחיה; שרד, בריחה לפרטיזנים', A_G4),
    P('גדליהו רף (גיולה)', '03.03.1931 – 2008', 'אחיה; בוכנוולד וברגה, ממקימי אילניה',
      A_GED, 'Gyula Gyuszi Raf רף פרקש בוכנוולד ברגה'),
    P('אברהם צדוק', '1925 – 2017', 'בעלה; נושא המחקר האחר בארכיון הזה', A_G5),
    P('עדו וזיו צדוק', '', 'בניה', A_G5),
    P('(ישראל) יעקב סטרולוביץ', '15.01.1870 – 1945', 'סב-סבה; הסתתר ביערות ושרד',
      A_G2, 'Jakab Jakob Sztrulyovics Strulovics'),
    P('שרה סטרולוביץ לבית רפפורט', '01/1876 – 1944', 'סבתה; בת גדליה רפפורט',
      A_G2, 'Sura Szura Szerena Rapaport Rappaport'),
    P('בצלאל פרקש', '1873/74 – 1944', 'סבה מצד האם; בעל קרקע בקרייניקובו',
      A_G2, 'Czallo Czulo Calo Bezalel Farkas'),
    P('אסתר פרקש לבית שטיינר', '1879 – 1944', 'סבתה מצד האם', A_G2, 'Eszter Steiner'),
    P('לייב סטרולוביץ וריבקה', 'המאה ה-19', 'סבי אביה, מקושלובו', A_G1, 'Leba Rifke'),
    P('ברל (דב) פרקש וגיטל', 'המאה ה-19', 'סבי אמה, מדנילובו', A_G1),
    P('גדליה רפפורט', '01.04.1846 – 1910', 'אבי השושלת; בעל האחוזות של אוקרמזו',
      A_RAPP, 'Gedajlo Gedalya Gedárló Rapaport Rappaport גדליה'),
    P('מינדל ברקוביץ', '04.01.1865 – לפני 08/1944', 'אשתו השלישית של גדליה',
      A_RAPP, 'Mindje Mingya Berkovics'),
    P('משה (Mozes) רפפורט', 'המאה ה-19', 'אביו של גדליה — קצה השושלת המתועדת', A_G0, 'Mosko'),
    P('יֶנטה לבית שפיגל', 'המאה ה-19', 'אמו של גדליה', A_G0, 'Jenta Spiegel'),
    P('זלמן ברקוביץ ופריידא קאופמן', 'המאה ה-19', 'הוריה של מינדל, מקרצ׳ונפלבה',
      A_G0, 'Zelman Freida Kaufman'),
    P('אלדר רפפורט', '11/1885 – ?', 'בן גדליה; ממועצת בנק החיסכון של אוקרמזו', A_RAPP, 'Aladar'),
    P('מאיר רפפורט', '28.01.1908 – ?', 'בן הזקונים של גדליה; טכנאי שיניים', A_RAPP, 'Majer Mayer'),
    P('נתן רפפורט', '12.11.1879 – ?', 'בן גדליה; סוחר עצים בחוסט', A_RAPP, 'Nuszen Nathan'),
    P('יוסף-דוד רפפורט', '16.10.1891 – 26.05.1942', 'בן גדליה ומינדל; נספה באושוויץ', A_G0),
    P("ר' חיים שלום לאנדא", 'נפטר 15.08.1924', 'דיין ומורה-צדק של אוקרמזו', A_CEM, 'Landa Landau'),
    P("ר' ישראל יעקב יוקל טייטלבוים", 'כיהן 1894–1924', 'רב וולובה', A_KEHILA, 'Teitelbaum'),
    P('משפחת קרשק', '', 'חסידי אומות העולם — הסתירו את גדליהו', A_GED, 'Krsek'),
)

# ------------------------------------------------------------------ config -
# --------------------------------------------------------------- the story --
# What is known, graded, and where it is written down. Source anchors here are
# the Hebrew section ids of אינדקס_מקורות.md; chapter anchors are the frozen
# `ch-N` ids, which external links have pointed at since the first edition.
B, D, V = Beat, DocCard, Verdict
_S = {
    'testimony': '#העדות-של-רחל',
    'transcript': '#קבצים-בתיקייה-הראשית',
    'pot': '#סריקות-דפי-העד-ומסמכי-הניצולים-44-קבצים-הורדו-17-08-2026',
    'stutthof': '#תיקי-שטוטהוף-המקוריים-סריקות-מארכיון-Arolsen-הורדו-17-08-202',
    'buchenwald': '#התיק-האישי-של-גדליה-בבוכנוולד-Arolsen-הורד-25-08-2026',
    'museum': '#תשובת-ארכיון-מוזיאון-שטוטהוף-18-קבצים',
    'dp': '#תקופת-העקורים-Arolsen-הורד-17-08-2026',
    'jewishgen': '#קטעי-ראיות-מצולמים-נוצרו-17-08-27-08-2026',
    'transports': '#מסמכי-מחנות-וטרנספורטים',
    'memorial': '#הנצחה-ועדויות',
    'israel': '#התיעוד-הישראלי-IGRA-ארכיון-המדינה-הורד-26-08-2026',
    'bulletin': '#עלון-יוצאי-קרפטורוס-137-עברית-ואנגלית',
    'census': '#גיליון-מפקד-1921-המקורי-5-קבצים',
}

STORY = Story(
    portrait='docs/arolsen_stutthof/105591037_001.jpg',
    portrait_alt='שאלון הקליטה של רחל בשטוטהוף, 29.6.1944, ובתחתיתו חתימתה "Sztrulovics Ruci"',
    portrait_caption='שטוטהוף, 29.6.1944 — שאלון הקליטה וחתימתה',
    lede=(
        '<b>רחל צדוק</b> — בבית קראו לה "רוצי" — נולדה ב-16 באפריל 1929 ב<b>וולובה</b> '
        'שבהרי הקרפטים, שלישית מבין חמישה ילדים; אביה היה סוחר עורות. באפריל 1944, ימים '
        'אחדים לפני יום הולדתה החמישה-עשר, נאספה המשפחה מביתה: הגטו, רכבת אחת, וב-19 במאי '
        'הרמפה ב<b>אושוויץ</b>. מתוך שבע נפשות הבית שרדו שלוש. רחל עברה את אושוויץ, את '
        '<b>שטוטהוף</b> כאסירה 38444, את מחנה העבודה בטורן ואת צעדת המוות; שוחררה באזור '
        'דנציג, שהתה במחנה העקורים ליפהיים, ועלתה ארצה במאי 1946 — היישר ל<b>מקווה '
        'ישראל</b>, שם פגשה את <b>אברהם צדוק</b>. חיה בחולון, מסרה עדות מצולמת ב-2009 '
        'ונפטרה בינואר 2021.'),
    verdicts=(
        V('ידוע בוודאות', 'מאומת', (
            ('נולדה ב-16.4.1929 ב<b>וולובה</b>, בת אריה-לייב סטרולוביץ ורבקה-רוזה פרקש',
             '#ch-1'),
            ('רשומות הלידה האזרחיות שלה ושל אחותה סימה, מארכיון DAZO', '#ch-1'),
            ('<b>שטוטהוף: 38443 ו-38444</b> — מספרי האחיות, בשתי יחידות ארכיון נפרדות',
             '#ch-5'),
            ('מסלול הרדיפה מן המעצר ב-14.4.1944 ועד הקליטה בשטוטהוף ב-29.6.1944', '#ch-5'),
            ('רכבת אוקרמזו יצאה ב-17.5.1944 ובה 3,052 מגורשים', '#ch-4'),
        )),
        V('כמעט ודאי', 'כמעט ודאי', (
            ('רשומת שטוטהוף 38444 היא רחל — כל פרטי הכרטיס והשאלון תואמים', '#ch-9'),
            ('אחותה <b>סימה</b> מתה בשטוטהוף', '#ch-9'),
            ('אביה <b>אריה-לייב</b> עבר את הסלקציה ומת מרעב באושוויץ', '#ch-9'),
            ('הרישום בפנקס הבוחרים תש"ט במקווה ישראל הוא שלה', '#ch-9'),
        )),
    ),
    timeline_note='כל אירוע מציין עד כמה הוא מבוסס, ומפנה אל המסמך שעליו הוא נשען.',
    timeline=(
        B('1870 · 1876', 'סבה וסבתה נולדים בכפרי הרי הוורחובינה: <b>יעקב סטרולוביץ</b> '
                        'ב<b>קושלובו</b>, בן לייב וריבקה; <b>שרה רפפורט</b> ב<b>וולובה</b>, '
                        'בת גדליה רפפורט ואסתר כץ.',
          place='קושלובו · וולובה', rank='מאומת', href='#ch-3',
          src=('הרשומות האזרחיות של מרמרוש, JewishGen', _S['jewishgen'])),
        B('מרס 1894', 'אביה <b>אריה-לייב</b> נולד ב<b>אוקרמזו</b> — בעיירת אמו — בכור '
                      'ארבעה-עשר ילדיהם של יעקב ושרה. סוחר עורות.',
          place='אוקרמזו', rank='מאומת', href='#ch-3',
          src=('רשומת הלידה האזרחית, JewishGen', _S['jewishgen'])),
        B('16.2.1921', 'מפקד האוכלוסין הצ\'כוסלובקי פוקד את <b>בית מס\' 30 בקושלובו</b>: '
                       'יעקב ראש הבית, שרה אשתו, ושלושה-עשר ילדים — משפחת אביה של רחל '
                       'שמונה שנים לפני לידתה.',
          place='קושלובו', rank='מאומת', href='#ch-3',
          src=('גיליון מפקד 1921, בית 30', _S['census'])),
        B('1923', 'ב<b>וולובה</b> — עיירה שבה 766 יהודים ב-1921, ורוב חנויותיה '
                         'בבעלות יהודית — פועלת "אגודת האשראי היהודית", שנוסדה ב-1923 '
                         'ונרשמה מחדש ב-1941 לפי צו האפליה ההונגרי.',
          place='וולובה', rank='מאומת', href='#ch-2',
          src=('Központi Értesítő, 26.11.1942', _S['bulletin'])),
        B('16.4.1929', 'נולדה ב<b>וולובה</b> שבקרפטורוס, שלישית מבין חמישה ילדים לאריה-לייב '
                       'סטרולוביץ ולרבקה-רוזה פרקש.',
          place='וולובה', rank='מאומת', href='#ch-1',
          src=('רשומת הלידה האזרחית, JewishGen/DAZO', _S['jewishgen'])),
        B('1939', 'הצבא ההונגרי מספח את האזור; חקיקה אנטי-יהודית, ועסק העורות של האב מוחרם.',
          place='וולובה', rank='כמעט ודאי', href='#ch-4',
          src=('עדות הווידאו של רחל', _S['testimony'])),
        B('14.4.1944', 'נעצרת בביתה — "Verhaftet am 14.4.44, am Orte" — יומיים לפני יום '
                       'הולדתה החמישה-עשר.',
          place='וולובה', rank='מאומת', href='#ch-5',
          src=('שאלון הקליטה בשטוטהוף', _S['stutthof'])),
        B('אפריל–מאי 1944', 'שלושה ימים נעולים בבית הכנסת, ואחריהם שבועות ב<b>גטו '
                            'סקלנצה</b> שכפרו רוקן מתושביו.',
          place='גטו סקלנצה', rank='כמעט ודאי', href='#ch-4',
          src=('עדות ריטה שניידר-פולק ופרוטוקול 73', _S['memorial'])),
        B('17.5.1944', 'המשפחה מגורשת ב<b>רכבת אוקרמזו</b>, ובה 3,052 מגורשים, שנרשמה במפקד '
                       'תחנת קושיצה.',
          place='קושיצה', rank='כמעט ודאי', href='#ch-4',
          src=('רשימת תחנת קושיצה (דגו"ב)', _S['transports'])),
        B('19.5.1944', 'הגעה ל<b>אושוויץ-בירקנאו</b>; רחל וסימה נבחרות לעבודה, ואחותן גיטה '
                       'בת השמונה נרצחת.',
          place='אושוויץ-בירקנאו', rank='מאומת', href='#ch-8',
          src=('כרטיס האסיר של גדליה בבוכנוולד', _S['buchenwald'])),
        B('19.5.1944', 'בסלקציה משיבה רחל שהיא בת חמש-עשרה, וקאפו מכריזה למנגלה "בת שמונה '
                       'עשרה" — ומצילה אותה.',
          place='אושוויץ-בירקנאו', rank='כמעט ודאי', href='#ch-7',
          src=('תמליל העדות המלא', _S['transcript'])),
        B('29.6.1944', 'האחיות נקלטות ב<b>שטוטהוף</b> במשלוח הנשים ההונגריות הראשון: סימה '
                       '38443, רחל 38444.',
          place='שטוטהוף', rank='מאומת', href='#ch-5',
          src=('רשימת הטרנספורט וכרטיסי האסירה', _S['museum'])),
        B('29.6.1944', 'בקליטה מוסרת רחל ששני הוריה "כעת באושוויץ", וחותמת בכתב ידה '
                       '"Sztrulovics Ruci".',
          place='שטוטהוף', rank='מאומת', href='#ch-5',
          src=('שאלון הקליטה 105591037', _S['stutthof'])),
        B('סוף קיץ 1944', 'נשלחת למחנה העבודה <b>טורן</b> ונפרדת מסימה החולה — ולא תראה '
                          'אותה עוד.',
          place='טורן', rank='ככל הנראה', href='#ch-4',
          src=('עדות רחל ומחקר ארכיון שטוטהוף', _S['museum'])),
        B('ינואר 1945', 'פינוי מחנות טורן: <b>צעדת מוות</b> בת כעשרה ימים, ובסופה הגעה '
                        'לפראוסט שליד דנציג.',
          place='פראוסט', rank='ככל הנראה', href='#ch-4',
          src=('עדות רחל ומחקר ארכיון שטוטהוף', _S['museum'])),
        B('1946', 'אחרי השחרור נדדה מערבה ושהתה במחנה העקורים <b>ליפהיים</b> שבבוואריה, '
                  'בלוק 24.',
          place='ליפהיים', rank='מאומת', href='#ch-4',
          src=('כרטיס מרשם השמות המרכזי, ארולסן', _S['dp'])),
        B('מאי 1946', 'עולה ארצה בסרטיפיקט, היישר ל<b>מקווה ישראל</b> — שם תפגוש את אברהם '
                      'צדוק.',
          place='מקווה ישראל', rank='כמעט ודאי', href='#ch-7',
          src=('עדות רחל', _S['testimony'])),
        B('1949', 'פנקס הבוחרים תש"ט רושם במקוה ישראל: "פורקוש (רפופורט), רחל, בת אריה, '
                  '1929".',
          place='מקווה ישראל', rank='כמעט ודאי', href='#ch-4',
          src=('פנקס הבוחרים תש"ט, IGRA', _S['israel'])),
        B('23.12.2009', 'מוסרת ל<b>יד ושם</b> עדות מצולמת בת שעתיים וארבעים דקות.',
          rank='מאומת', href='#ch-6', src=('עדות הווידאו, יד ושם O.3/8424116', _S['testimony'])),
        B('ינואר 2021', 'נפטרה בחולון, כבת תשעים ואחת.', place='חולון',
          rank='מאומת', href='#ch-4', src=('עלון יוצאי קרפטורוס 137', _S['bulletin'])),
    ),
    docs_note='לחיצה על תמונה פותחת את הסריקה המלאה; "בדוח" מוביל אל הקריאה המלאה של המסמך.',
    docs=(
        D('docs/arolsen_stutthof/105591047_001.jpg', '29.6.1944', 'כרטיס האסירה 38444',
          'קליטתה בשטוטהוף מאושוויץ, ורישום האב כמי שנמצא "כעת באושוויץ".',
          'מאומת', '#ch-5', src=('תיקי שטוטהוף, ארולסן', _S['stutthof'])),
        D('docs/arolsen_stutthof/105591037_001.jpg', '29.6.1944', 'שאלון הקליטה וחתימתה',
          'תאריך המעצר, שמות שני ההורים ומקומם, וחתימת ידה בת החמש-עשרה.',
          'מאומת', '#ch-5', src=('תיקי שטוטהוף, ארולסן', _S['stutthof'])),
        D('docs/evidence/stutthof_transport_list_rows802-803_zoom.png', '29.6.1944',
          'רשימת הטרנספורט, שורות 802–803',
          'האחיות רשומות בשורות עוקבות במשלוח מאושוויץ — המסמך שממנו נגזרו הכרטיסים.',
          'מאומת', '#ch-5', src=('ארכיון מוזיאון שטוטהוף', _S['museum'])),
        D('docs/arolsen_stutthof/105590973_001.jpg', '1944', 'כרטיס ההפניה על שם האב',
          'האב לא היה אסיר בשטוטהוף; מקומו נרשם "מחנה אושוויץ", בהפניה לתיק בתו.',
          'מאומת', '#ch-5', src=('תיקי שטוטהוף, ארולסן', _S['stutthof'])),
        D('docs/evidence/jewishgen_rachel_sima_own_birth_records_zoom.png', '1926 · 1929',
          'רשומות הלידה של רחל וסימה',
          'הרישום האזרחי של שתי האחיות, בנות Struljovic Leba ו-Farkas Rifka.',
          'מאומת', '#ch-1', src=('JewishGen — פונד 1606, DAZO', _S['jewishgen'])),
        D('docs/hungaricana_1921_census_koselovo_house30_full.png', '16.2.1921',
          'מפקד 1921, בית 30 בקושלובו',
          'בית סבהּ יעקב סטרולוביץ ושרה רפפורט, ושלושה-עשר ילדיהם, בתאריכי לידה מדויקים.',
          'מאומת', '#ch-3', src=('גיליון מפקד 1921, Hungaricana', _S['census'])),
        D('docs/arolsen_dp/cni_farkas_rachel_001.jpg', '1946', 'כרטיס העקורים — ליפהיים',
          'תחנתה האחרונה באירופה: מחנה העקורים ליפהיים, בלוק 24, בוואריה.',
          'מאומת', '#ch-4', src=('תקופת העקורים, ארולסן', _S['dp'])),
        D('docs/yadvashem_pot_scans/10846653_04122013_8915_158.jpg', '22.11.2013',
          'דף עד על האב, בכתב ידה',
          'רחל מנציחה את אביה, סוחר העורות, ומוסרת את כתובתה וחתימתה.',
          'כמעט ודאי', '#ch-9', src=('דפי העד, יד ושם', _S['pot'])),
    ),
    sources_note=('כל קביעה בדף הזה נשענת על אחד המקורות שלהלן. כל ערך מוביל אל אינדקס '
                  'המקורות שבדוח, ושם — קישור אל הרשומה בארכיון שממנה נלקחה ואל עותק '
                  'שמור שלה.'),
    sources=(
        ('עדות הווידאו של רחל, יד ושם O.3/8424116 (23.12.2009)', _S['testimony']),
        ('התמליל המתוזמן המלא של העדות', _S['transcript']),
        ('ארבעה דפי עד בכתב ידה של רחל (22.11.2013), יד ושם', _S['pot']),
        ('תיקי שטוטהוף המקוריים — סריקות מארכיון ארולסן', _S['stutthof']),
        ('התיק האישי של גדליה בבוכנוולד, ארולסן', _S['buchenwald']),
        ('ארכיון מוזיאון שטוטהוף — מסמכי הטרנספורט ומחנות העבודה', _S['museum']),
        ('כרטיס מרשם השמות המרכזי (CNI), ארולסן — ליפהיים', _S['dp']),
        ('JewishGen — רשומות אזרחיות מפונד 1606, ארכיון DAZO', _S['jewishgen']),
        ('מסמכי מחנות וטרנספורטים — רשימת תחנת קושיצה, דגו"ב', _S['transports']),
        ('הנצחה ועדויות — עדות ריטה שניידר-פולק, KehilaLinks', _S['memorial']),
        ('התיעוד הישראלי — IGRA וארכיון המדינה', _S['israel']),
        ('עלון יוצאי קרפטורוס 137 (08/2025)', _S['bulletin']),
        ('גיליון מפקד 1921 המקורי, ספריית Hungaricana', _S['census']),
    ),
)

cfg = ProjectConfig(
    root=ROOT,
    slug='rachel-zadok',
    main_html='רחל_צדוק_המחקר_המלא.html',
    title='רחל צדוק לבית רפפורט-סטרולוביץ',
    subject='16.04.1929, וולובה (Ökörmező) — 01/2021, חולון · מחקר גנאלוגי מתועד-מקורות',
    meta_description=('מחקר גנאלוגי מתועד-מקורות על רחל צדוק לבית רפפורט-סטרולוביץ, '
                      'ילידת וולובה שבקרפטורוס, ניצולת אושוויץ, שטוטהוף וטורן — '
                      'עם עץ משפחה, גלריית ראיות ואינדקס מקורות.'),
    report_md='רחל_צדוק_מחקר_מקיף.md',
    sources_md='אינדקס_מקורות.md',
    changelog_md='CHANGELOG.md',
    tree=TreeSource(kind='html_extract', path='עץ_משפחה_מורחב.html',
                    page_href='עץ_משפחה_מורחב.html'),
    palette=PAL,
    md_extensions=('tables',),
    people_legend=('בתאריכים: <b>?</b> — שנה שלא אותרה; <b>~</b> — שנה משוערת; '
                   'טווח בלא סימון הוא מתועד במסמך.'),
    thumb_referrers=('../index.html', '../research_registry.json'),
    spine=(
        SpineFact('7', 'דורות מתועדים'),
        SpineFact('244', 'קובצי מקור שמורים'),
        SpineFact('18', 'ארכיונים ומאגרים'),
        SpineFact('44', 'מהדורות · 21 סבבי ביקורת'),
    ),
    story=STORY,
    story_subject='וולובה 1929 — חולון 2021 · ניצולת אושוויץ, שטוטהוף וטורן · אשתו של אברהם צדוק',
    story_spine=(
        SpineFact('1929', 'נולדה בוולובה'),
        SpineFact('38444', 'מספרה בשטוטהוף'),
        SpineFact('1946', 'עלתה ארצה בסרטיפיקט'),
        SpineFact('2009', 'מסרה עדות מצולמת'),
    ),
    glossary=(
        ('שטוטהוף', 'מחנה ריכוז ליד דנציג. ביוני 1944 הגיעו אליו מאושוויץ משלוחי נשים '
                    'יהודיות מהונגריה, ובהם רחל ואחותה.'),
        ('טורן (Thorn)', 'מערך מחנות עבודה בפולין שהיה כפוף לשטוטהוף; נשים נשלחו אליו '
                         'לעבודות ביצורים.'),
        ('ארולסן (Arolsen)', 'הארכיון הבין-לאומי לנרדפי הנאצים; מחזיק את תיקי המחנות '
                             'המקוריים ואת כרטיסי העקורים.'),
        ('דף עד', 'טופס הנצחה של יד ושם שממלא קרוב או מכר, ובו פרטי הנספה וסיפור מותו.'),
        ('מחנה עקורים', 'מחנה לניצולים שלא יכלו לשוב לבתיהם; ליפהיים שבבוואריה היה אחד '
                        'מהם.'),
        ('קרפטורוס', 'רוסיה הקרפטית — אזור הרים שעבר בין צ\'כוסלובקיה, הונגריה '
                     'וברית המועצות; וולובה שוכנת בו.'),
    ),
    people=PEOPLE,
    figures=figs,
    figure_anchors=tuple(FIGURE_ANCHORS),
    gallery=GALLERY,
    text_transforms=(arolsen,),
    report_transforms=(timestamps,),
    sources_transforms=(sources_links,),
    breadcrumb=('../index.html', 'ארכיון מחקר המשפחה'),
    footer_note=('מסמך זיכרון משפחתי · כל קביעה שבו נשענת על מסמך: קישור חיצוני אל המקור '
                 'וקישור פנימי אל עותק שמור. מה שלא אומת — מסומן ככזה.'),
    # the numbering published before פרק ג'1 and פרק י' were added, mapped by
    # chapter name so that inserting a chapter never moves an external link
    legacy_anchors={
        'ch-1': r"^פרק א'", 'ch-2': r"^פרק ב'", 'ch-3': r"^פרק ג' ", 'ch-4': r"^פרק ד'",
        'ch-5': r"^פרק ה'", 'ch-6': r"^פרק ו' ", 'ch-7': r"^פרק ו'1", 'ch-8': r"^פרק ז'",
        'ch-9': r"^פרק ח'", 'ch-10': r"^פרק ט'", 'ch-11': r'^מקורות עיקריים',
    },
    site_extra_files=('עץ_משפחה_מורחב.html', 'עץ_משפחה_גרפי.html', 'תמליל_העדות_המלא.txt',
                      'ניתוח_העדות.md'),
    # places, camps and archives a reader is as likely to search for as a name
    search_extra=(
        ('טורן — מחנה העבודה (Thorn)', "#פרק-ד'-ציר-הזמן-מוולובה-לחולון", 'מקום',
         'Thorn Torun טורון Stutthof-Thorn'),
        ('שטוטהוף — המחנה והתיקים', "#פרק-ה'-תיקי-שטוטהוף-המקוריים-מה-הם-מגלים", 'מקום',
         'Stutthof Sztutowo 38443 38444'),
        ('אוקרמזו / וולובה / מיז\'יריה', "#פרק-ב'-העיירה-וולובה-Ökörmező-מיז'יריה", 'מקום',
         'Ökörmező Okormezo Volove Volová Mizhhirya Mizhhiria Volovoe'),
        ('קושלובו', '#דור-2-הסבים-של-רחל', 'מקום', 'Koselovo Keselymezo Keselyumezo Koseleve'),
        ('בתי העלמין — 95 התצלומים', '#בתי-העלמין-95-תצלומים-קריאה-מלאה', 'נושא',
         'ESJF CJA בית קברות מצבות cemetery'),
        ('אושוויץ והמשלוח מ-17.05.1944', "#פרק-ד'-ציר-הזמן-מוולובה-לחולון", 'נושא',
         'Auschwitz Kassa קושיצה טרנספורט 360'),
    ),
    toc_overrides={
        r"^פרק ח'": "ח' · מה מאומת ומה פתוח",
        r"^פרק ג'1": "ג'1 · לפני המרשם",
        r"^פרק ו'1": "ו'1 · התמלול המלא",
        r'^מקורות עיקריים': 'רשימת המקורות של הדוח',
        r"^פרק י'": "י' · שיטה ומגבלות",
        r"^פרק ט'": "ט' · צעדים פתוחים",
    },
    qa_strict=True,
)

if __name__ == '__main__':
    build(cfg)
