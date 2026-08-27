# -*- coding: utf-8 -*-
"""rachel-zadok — the project's own data. The engine lives in ../common/genealogy_site."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(ROOT), 'common'))

from genealogy_site import ProjectConfig, Palette, TreeSource, SpineFact, Person, build  # noqa: E402
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
    return (f'<a href="{YT}&t={h*3600+mn*60+s}s" target="_blank" rel="noopener" '
            f'title="לצפייה ברגע זה בעדות">[{m.group(1)}:{m.group(2)}:{m.group(3)}]</a>')


def _ts_range(m):
    h, mn, s = int(m.group(1)), int(m.group(2)), int(m.group(3))
    lbl = (f'[<bdi dir="ltr">{m.group(1)}:{m.group(2)}:{m.group(3)}–'
           f'{m.group(4)}:{m.group(5)}:{m.group(6)}</bdi>]')
    return (f'<a href="{YT}&t={h*3600+mn*60+s}s" target="_blank" rel="noopener" '
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
        out += f' <a href="{AR}{n}_001.jpg" title="הסריקה בתיקייה">🗎</a>'
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
    thumb_referrers=('../index.html', '../research_registry.json'),
    spine=(
        SpineFact('7', 'דורות מתועדים'),
        SpineFact('244', 'קובצי מקור שמורים'),
        SpineFact('18', 'ארכיונים ומאגרים'),
        SpineFact('43', 'מהדורות · 19 סבבי ביקורת'),
    ),
    people=PEOPLE,
    figures=figs,
    figure_anchors=tuple(FIGURE_ANCHORS),
    gallery=GALLERY,
    text_transforms=(arolsen,),
    report_transforms=(timestamps,),
    sources_transforms=(sources_links,),
    breadcrumb=('../index.html', 'ארכיון מחקר המשפחה'),
    provenance_note=('העמוד הזה טוען את התצלומים ואת המסמכים ישירות מתיקיית <code>docs/</code> '
                     'שלצדו — לחיצה על כל תצלום פותחת את קובץ המקור המלא. אם פתחתם אותו מחוץ '
                     'לתיקייה, התמונות לא ייטענו.'),
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
