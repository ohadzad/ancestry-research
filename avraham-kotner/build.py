# -*- coding: utf-8 -*-
"""avraham-kotner — the project's own data. The engine lives in ../common/genealogy_site."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def _engine_path():
    here = os.path.join(os.path.dirname(ROOT), 'common')
    local = os.path.join(ROOT, '_common')
    for p in (os.environ.get('GENEALOGY_COMMON'), here, local):
        if p and os.path.isdir(os.path.join(p, 'genealogy_site')):
            return p
    raise SystemExit('לא נמצא מנוע genealogy_site')


_ENGINE = _engine_path()
sys.path.insert(0, _ENGINE)

from genealogy_site import ProjectConfig, Palette, TreeSource, SpineFact, Person, build  # noqa: E402
from genealogy_site import Story, Beat, DocCard, Verdict                                  # noqa: E402
from genealogy_site import figures as F                                                   # noqa: E402

R = lambda *p: os.path.join(ROOT, *p)          # noqa: E731

# the accent of this report: a slate blue — the Ozorków–Łódź line, against the
# Carpathian brown of rachel-zadok and the Meknes terracotta of the Ben Harush pages
PAL = Palette(
    accent='#3d5a80', accent_soft='#5b7aa3', link='#2f4a6d',
    paper='#f6f7f9', ink='#22262b', muted='#5f6670', line='#d5d8dd',
    hero_from='#1d2838', hero_to='#3d5a80',
)

P = Person
PEOPLE = (
    P('אברהם ("אברמק") קוטנר', '15.8.1928 (1930 בישראל) – 3.1986', 'נושא הדף; אוזורקוב; גטו לודז\'; אושוויץ; מאוטהאוזן, אסיר 133332 (23.2.1945); ילדי סלווינו; קפריסין 1947; קיבוץ צאלים 1952; דימונה',
      '#s4-2', 'Abram Abraham Avraham Avramek Kutner Kotner Kottner אברם אברמק Ozorkow Ozorków Mauthausen 133332 Selvino סלווינו צאלים Tze\'elim Zeelim'),
    P('ישראל קוטנר', '1892, סטריקוב', 'אביו; בן צבי וחיה; סוחר תבואה באוזורקוב; גטו לודז\'; נספה באושוויץ (דף העד)', '#s3-1', 'Israel Izrael Kutner Kotner Strykow Stryków'),
    P('צביה (Cywia) קוטנר לבית בנדוס', '1891 (דף העד) / 10.12.1895 (רשימת הגטו)', 'אמו; בת אברהם ושרה; גטו לודז\', קניגסברג 4; נספתה באושוויץ (דף העד)', '#s3-2', 'Cywia Tzvia Zywia Kutner Bandus Bendos בנדוס'),
    P('שרה (Sala) מלוטק לבית קוטנר', '14.8.1922 (1923 בעץ) – 2009 (העץ)', 'אחותו הבכורה; אושוויץ, ברגן-בלזן, בוכנוולד — אסירה 40821; שרדה; מילאה את דפי העד, קריית אונו, שנות ה-50', '#s3-3', 'Sara Sala Sura Mlotek Malotek Kutner מלוטק סלה Buchenwald 40821'),
    P('פייגה קוטנר', 'בת 9', 'אחותו הצעירה; נלקחה מגטו לודז\' "למקום בלתי ידוע" (דף העד)', '#s3-1', 'Feiga Fela Fajga Kutner פלה'),
    P('צבי (הרש) וחיה קוטנר', '', 'סבו וסבתו — הוריו של ישראל (דף העד)', '#s3-1', 'Tzvi Hersh Hersz Hirsch Chaja Kutner'),
    P('אברהם ושרה בנדוס', '', 'סבו וסבתו — הוריה של צביה (דף העד)', '#s3-2', 'Abraham Sara Bandus Bendos'),
    P('מרדכי מלוטק', '1919 – 2010 (העץ)', 'בעלה של שרה (העץ המשפחתי)', '#s2', 'Mordechai Mlotek Malotek'),
    P('צפורה קוטנר לבית בלם', '25.12.1931/2 – 2006', 'אשתו — נושאת המחקר האחר בארכיון הזה', '#s5-2', 'Tzipora Cipora Zipora Cypora Balem Balam Blam Kotner Kutner'),
)

GALLERY = (
    (F.thumb(ROOT, 'docs/ev_mauthausen_personalkarte.jpg', 440), 'docs/arolsen/mauthausen-personal-file-133332/arolsen_1574341_01_front.jpg', 'כרטיס האסיר האישי ממאוטהאוזן — קוטנר אברם, 15.8.28, אוזורקוב; הוכנס 22.8.44 מאושוויץ; מאוטהאוזן 23.2.45'),
    (F.thumb(ROOT, 'docs/ev_mauthausen_nummernkarte.jpg', 440), 'docs/arolsen/mauthausen-personal-file-133332/arolsen_1574343_01_front.jpg', 'כרטיס המספר — 133332, יהודי פולני, 23 בפברואר 1945, מאושוויץ; תלמיד'),
    (F.thumb(ROOT, 'docs/ev_pot_israel.jpg', 440), 'docs/yadvashem/PoT-parents-submitted-by-Sara-Mlotek/PoT_scan134_Israel-Kutner_No329533_YV-records-453751-8760277-16681235.jpg', 'דף העד על ישראל קוטנר, שנות ה-50 — בן צבי וחיה, סטריקוב 1892, סוחר תבואה באוזורקוב'),
    (F.thumb(ROOT, 'docs/ev_pot_feiga.jpg', 440), 'docs/yadvashem/PoT-parents-submitted-by-Sara-Mlotek/PoT_scan134_Israel-Kutner_No329533_YV-records-453751-8760277-16681235.jpg', 'פייגה קוטנר, בת 9 — "גיטו לודז\' — נלקחה למקום בלתי ידוע"'),
    (F.thumb(ROOT, 'docs/ev_sala_buchenwald.jpg', 440), 'docs/arolsen/Sala-Kutner-Buchenwald-1861737/arolsen_7633159_01_front.jpg', 'אחותו סלה (שרה) קוטנר, 14.8.22 — אושוויץ 10.8.44, ברגן-בלזן, בוכנוולד 18.1.45, אסירה 40821'),
    (F.thumb(ROOT, 'docs/ev_pot_cywia.jpg', 440), 'docs/yadvashem/PoT-parents-submitted-by-Sara-Mlotek/PoT_scan204_Cywia-Kutner_No379532_YV-records-552005-16723180.jpg', 'דף העד על צביה קוטנר, שנות ה-50 — בת אברהם ושרה, אוזורקוב'),
    (F.thumb(ROOT, 'docs/ev_cyprus_balem_kutner.jpg', 440), 'docs/igra/igra_DetentionCampsCyprus-3632_Abram-Kutner_Chaim-Arlozoroff_1947.jpg', 'רשימת קפריסין, 1947 — 452 Balem Cypora 1931 ו-467 Kutner Abram 1930, אונייה "Ch. Arlozorof"'),
    (F.thumb(ROOT, 'docs/ev_tzeelim_1952.jpg', 440), 'docs/igra/igra_1952-Voters-Tzelim_WestNegevLC_313_line8.jpg', 'פנקס הבוחרים של קיבוץ צאלים, 1952 — קוטנר אברהם 1930, קוטנר צפורה 1932'),
)


def citations(t):
    """`[[13]]` in the prose becomes a link into the source index."""
    return re.sub(r'\[\[(\d+)\]\]',
                  lambda m: f'<a href="#src-{m.group(1)}" class="cit" title="אל ערך המקור">[{m.group(1)}]</a>', t)


_HEB = '\u0590-\u05ff'
_RANGE = re.compile(r'(?<![\w' + _HEB + r'/.-])(\d{3,4}-\d{3,4})(?![\w' + _HEB + r'/.-])')


def hyphen_ranges(t):
    return _RANGE.sub(r'<bdi dir="ltr">\1</bdi>', t)


# --------------------------------------------------------------- the story --
B, D, V = Beat, DocCard, Verdict

STORY = Story(
    portrait='docs/ev_mauthausen_personalkarte.jpg',
    portrait_alt='כרטיס האסיר האישי של אברם קוטנר במחנה מאוטהאוזן: נולד 15.8.28 באוזורקוב, הוכנס 22.8.44 מאושוויץ, מאוטהאוזן 23.2.45',
    portrait_caption='מאוטהאוזן, פברואר 1945 — כרטיס האסיר האישי',
    lede=(
        '<b>אברהם ("אברמק") קוטנר</b> נולד ב-15 באוגוסט 1928 ב<b>אוזורקוב</b> שבפולין, '
        'בנם של <b>ישראל קוטנר</b>, סוחר תבואה, ו<b>צביה לבית בנדוס</b>. עם אמו גר '
        'ב<b>גטו לודז\'</b>; משם הובא ל<b>אושוויץ</b>, ובפברואר 1945 נרשם במחנה '
        '<b>מאוטהאוזן</b> כאסיר 133332 — "תלמיד", רווק, "קרובים: לא ידוע". הוריו ואחותו '
        'הקטנה <b>פייגה</b> נספו; אחותו הבכורה <b>שרה</b> שרדה. אחרי המלחמה — לפי אתר הזיכרון '
        'של הבית — היה מ<b>ילדי סלווינו</b> באיטליה, וככל הנראה עבר את מחנות המעצר בקפריסין; '
        'וב-1952 הוא חבר <b>קיבוץ צאלים</b> '
        'עם אשתו <b>צפורה לבית בלם</b>. נפטר במרץ 1986. הדף מספר מה שהמסמכים מראים, '
        'לפי סדר הזמן.'),
    verdicts=(
        V('ידוע בוודאות', 'מאומת', (
            ('אסיר <b>133332</b> במאוטהאוזן מ-23.2.1945, מאושוויץ; כתובתו בגטו לודז\'', '#s4-2'),
                        ('חבר <b>קיבוץ צאלים</b> ב-1952, עם צפורה', '#s5-2'),
        )),
        V('כמעט ודאי / ככל הנראה', 'ככל הנראה', (
            ('בן <b>ישראל וצביה</b>, אחיהן של <b>שרה</b> ו<b>פייגה</b>', '#s3'),
            ('ממחנות קפריסין לארץ ב-1947, ב<b>מכסת הילדים היתומים</b>', '#s5-1'),
            ('מ<b>ילדי סלווינו</b>; מזכיר צאלים; עבד בכור בדימונה', '#s4-3'),
            ('שנת הלידה <b>1928</b> — וב-1930 מאז קפריסין', '#s6'),
        )),
    ),
    timeline_note='כל אירוע מציין עד כמה הוא מבוסס, ומפנה אל המסמך שעליו הוא נשען.',
    timeline=(
        B('1891–1892', '<b>ישראל קוטנר</b>, בן צבי וחיה, נולד בסטריקוב; <b>צביה</b>, בת אברהם '
                        'ושרה בנדוס, באוזורקוב. ישראל — סוחר תבואה באוזורקוב.',
          place='אוזורקוב', rank='כמעט ודאי', href='#s3', src=('דפי העד שמילאה שרה', '#src-2')),
        B('15.8.1928', 'אברהם נולד ב<b>אוזורקוב</b> — השני מבין שלושה: שרה (1922; 1923 בעץ), אברהם, ופייגה.',
          place='אוזורקוב', rank='כמעט ודאי', href='#s6', src=('כרטיס האסיר, מאוטהאוזן', '#src-1')),
        B('גטו לודז\'', 'אברהם ואמו רשומים באותה דירה ב<b>גטו לודז\'</b> — רחוב קניגסברג 4, דירה 35.',
          place='לודז\'', rank='כמעט ודאי', href='#s4-1', src=('מאגר השמות, יד ושם', '#src-4')),
        B('10.8.1944', 'אחותו <b>שרה</b> נכנסת לאושוויץ; משם — ברגן-בלזן, ובינואר 1945 בוכנוולד. היא שורדת.',
          place='אושוויץ', rank='כמעט ודאי', href='#s3-3', src=('תיק האסירה בבוכנוולד', '#src-9')),
        B('1940–1944', 'אחותו הקטנה <b>פייגה</b>, בת תשע, נלקחת מגטו לודז\' "למקום בלתי ידוע".',
          place='לודז\'', rank='מאומת', href='#s3-1', src=('דף העד על ישראל קוטנר', '#src-2')),
        B('22.8.1944', '"הוכנס … Au" — אושוויץ. הוריו נספו שם, לפי עדות אחותו.',
          place='אושוויץ', rank='ככל הנראה', href='#s4-2', src=('כרטיס האסיר', '#src-1')),
        B('23.2.1945', 'נרשם במחנה <b>מאוטהאוזן</b>, אסיר 133332: "יהודי פולני", תלמיד, רווק; '
                       'מקום מגורי הקרובים — "לא ידוע".',
          place='מאוטהאוזן', rank='מאומת', href='#s4-2', src=('התיק האישי בארולסן', '#src-1')),
        B('1945–1947', 'לפי אתר הזיכרון של הבית — מ<b>ילדי סלווינו</b>, בית הילדים היהודי בהרי ברגמו, איטליה.',
          place='סלווינו', rank='ככל הנראה', href='#s4-3', src=('אתר הזיכרון של בית סלווינו', '#src-8')),
        B('1947', 'ברשימת <b>המכסה השנייה של ילדים יתומים</b> שהועברו ממחנות המעצר בקפריסין: '
                  '"Kutner Abram", 1930, אונייה "Ch. Arlozorof". באותו עמוד — "Balem Cypora".',
          place='קפריסין', rank='ככל הנראה', href='#s5-1', src=('רשימת קפריסין, 1947', '#src-5')),
        B('1952', 'חבר <b>קיבוץ צאלים</b> בנגב המערבי; בשורה שאחריו בפנקס הבוחרים — '
                  '<b>צפורה קוטנר</b>, אשתו.',
          place='צאלים', rank='מאומת', href='#s5-2', src=('פנקס הבוחרים, 1952', '#src-6')),
        B('שנות ה-50', 'אחותו <b>שרה מלוטק</b> ממלאת ביד ושם דפי עד על ההורים ועל פייגה.',
          place='קריית אונו', rank='מאומת', href='#s3', src=('דפי העד', '#src-2')),
        B('שנות ה-50–80', 'המזכיר הראשון של צאלים; תפקיד אחראי בכור הגרעיני בדימונה.',
          rank='ככל הנראה', href='#s4-3', src=('אתר הזיכרון של בית סלווינו', '#src-8')),
        B('3.1986', 'נפטר; לפי העץ המשפחתי נקבר בבית הקברות הישן של באר שבע.',
          place='באר שבע', rank='טעון אימות', href='#s2', src=('עץ המשפחה', '#src-7')),
    ),
    docs_note='לחיצה על תמונה פותחת את הסריקה המלאה; "בדוח" מוביל אל הקריאה המלאה של המסמך.',
    docs=(
        D('docs/arolsen/mauthausen-personal-file-133332/arolsen_1574341_01_front.jpg', '23.2.1945',
          'כרטיס האסיר האישי, מאוטהאוזן',
          'שמו, יום ועיר הלידה, כתובתו בגטו לודז\' — ו"הוכנס 22.8.44 מאושוויץ".',
          'מאומת', '#s4-2', src=('ערך 1', '#src-1')),
        D('docs/arolsen/mauthausen-personal-file-133332/arolsen_1574343_01_front.jpg', '23.2.1945',
          'כרטיס המספר 133332', '"23 בפברואר 1945 · אושוויץ" — "תלמיד" (כבן 16).',
          'מאומת', '#s4-2', focus='center 30%', src=('ערך 1', '#src-1')),
        D('docs/yadvashem/PoT-parents-submitted-by-Sara-Mlotek/PoT_scan134_Israel-Kutner_No329533_YV-records-453751-8760277-16681235.jpg',
          'שנות ה-50', 'דף העד על ישראל קוטנר',
          'מאת בתו שרה: אביו צבי, אמו חיה, סוחר תבואה, שלושה ילדים — ופייגה בת התשע.',
          'מאומת', '#s3-1', src=('ערך 2', '#src-2')),
        D('docs/yadvashem/PoT-parents-submitted-by-Sara-Mlotek/PoT_scan204_Cywia-Kutner_No379532_YV-records-552005-16723180.jpg',
          'שנות ה-50', 'דף העד על צביה קוטנר', 'בת אברהם ושרה, אוזורקוב; לודז\'; אושוויץ.',
          'מאומת', '#s3-2', src=('ערך 3', '#src-3')),
        D('docs/igra/igra_DetentionCampsCyprus-3632_Abram-Kutner_Chaim-Arlozoroff_1947.jpg', '1947',
          'רשימת קפריסין — מכסת היתומים',
          '"Kutner Abram, 1930" — ובאותו עמוד "Balem Cypora, 1931", באותה אונייה.',
          'ככל הנראה', '#s5-1', focus='center 75%', src=('ערך 5', '#src-5')),
        D('docs/igra/igra_1952-Voters-Tzelim_WestNegevLC_313_line8.jpg', '1952',
          'פנקס הבוחרים — קיבוץ צאלים', '"קוטנר אברהם 1930 · קוטנר צפורה 1932".',
          'מאומת', '#s5-2', src=('ערך 6', '#src-6')),
    ),
    sources_note=('כל קביעה בדף הזה נשענת על אחד המסמכים שלהלן. כל ערך מוביל אל '
                  'אינדקס המקורות שבדוח, ושם — קישור אל הרשומה בארכיון שממנה נלקחה '
                  'ואל עותק שמור שלה.'),
    sources=(
        ('ארכיון ארולסן — התיק האישי ממאוטהאוזן, אסיר 133332', '#src-1'),
        ('יד ושם — דף העד על ישראל קוטנר, שנות החמישים', '#src-2'),
        ('יד ושם — דף העד על צביה קוטנר, שנות החמישים', '#src-3'),
        ('יד ושם — מאגר השמות: רשימות גטו לודז\'', '#src-4'),
        ('ארכיון ארולסן — תיק האסירה של אחותו, בוכנוולד', '#src-9'),
        ('הארכיון הציוני — רשימת עצורי קפריסין, 1947', '#src-5'),
        ('ארכיון המדינה — פנקס הבוחרים, קיבוץ צאלים, 1952', '#src-6'),
        ('עץ המשפחה ב-MyHeritage', '#src-7'),
        ('Sciesopoli — רשימות ילדי סלווינו', '#src-8'),
    ),
)

cfg = ProjectConfig(
    root=ROOT,
    slug='avraham-kotner',
    main_html='אברהם-קוטנר.html',
    title='אברהם קוטנר',
    subject='15.8.1928, אוזורקוב — 3.1986 · גטו לודז\', אושוויץ, מאוטהאוזן · ילדי סלווינו · קפריסין · קיבוץ צאלים',
    meta_description=('דף מחקר על אברהם ("אברמק") קוטנר, יליד אוזורקוב 1928 — בן ישראל וצביה לבית בנדוס; '
                      'גטו לודז\', אושוויץ, ואסיר 133332 במאוטהאוזן; ילדי סלווינו; רשימת עצורי קפריסין 1947; '
                      'קיבוץ צאלים 1952 עם אשתו צפורה לבית בלם.'),
    report_md='report.md',
    sources_md='sources-index.md',
    changelog_md='CHANGELOG.md',
    tree=TreeSource(kind='html_extract', path='tree.html', page_href='tree.html'),
    palette=PAL,
    md_extensions=('tables',),
    thumb_referrers=('../index.html', '../research_registry.json'),
    spine=(
        SpineFact('133332', 'מספר האסיר במאוטהאוזן'),
        SpineFact('2', 'דפי עד שמילאה אחותו'),
        SpineFact('7', 'מקורות ראשוניים'),
        SpineFact('3', 'גרסאות לשנת הלידה'),
    ),
    people=PEOPLE,
    gallery=GALLERY,
    text_transforms=(hyphen_ranges,),
    report_transforms=(citations,),
    breadcrumb=('../index.html', 'ארכיון מחקר המשפחה'),
    footer_note=('מסמך זיכרון משפחתי · כל קביעה שבו נשענת על מסמך: קישור חיצוני אל המקור '
                 'וקישור פנימי אל עותק שמור. מה שלא אומת — מסומן ככזה.'),
    legacy_anchors={f's{n}': r'^' + str(n) + r'\.' for n in range(1, 10)},
    site_extra_files=('tree.html',),
    search_extra=(
        ('אוזורקוב', '#s3', 'מקום', 'Ozorkow Ozorków אוזורקוב'),
        ('גטו לודז\'', '#s4-1', 'מקום', 'Lodz Łódź Litzmannstadt ליצמנשטט'),
        ('מאוטהאוזן', '#s4-2', 'מקום', 'Mauthausen KL'),
        ('סלווינו', '#s4-3', 'מקום', 'Selvino Sciesopoli מגד Megged'),
        ('קפריסין', '#s5-1', 'מקום', 'Cyprus Arlozorof ארלוזורוב'),
        ('צאלים', '#s5-2', 'מקום', 'Tzeelim Zeelim חבל מעון'),
        ('ממצאים שליליים', '#s9-4', 'נושא', 'ממצא שלילי נשלל'),
    ),
    toc_overrides={
        r'^1\.': '1 · תמצית',
        r'^2\.': '2 · מהמשפחה',
        r'^3\.': '3 · אוזורקוב',
        r'^4\.': '4 · המלחמה',
        r'^5\.': '5 · קפריסין וצאלים',
        r'^6\.': '6 · שנת הלידה',
        r'^7\.': '7 · עץ המשפחה',
        r'^8\.': '8 · פעולות פתוחות',
        r'^9\.': '9 · שיטה ומגבלות',
    },
    glossary=(
        ('דף עד', 'טופס של יד ושם שבו קרוב או מכר רושם נספה: שם, הורים, לידה, מגורים, '
                  'ומה ידוע על מותו. עדות — לא רשומה בת-זמנה.'),
        ('Häftlings-Personal-Karte', 'כרטיס האסיר האישי שנפתח לכל אסיר במחנות הריכוז: '
                                     'פרטים אישיים, מאיפה הגיע ומתי, ומספרו.'),
        ('T/D', 'מספר תיק איתור (Tracing/Documents) בשירות האיתור הבין-לאומי בארולסן.'),
        ('סלווינו', 'בית ילדים ליתומים יהודים ניצולי שואה בהרי ברגמו שבאיטליה, 1945–1948; '
                    'רוב ילדיו עלו לארץ.'),
        ('IGRA', 'העמותה הישראלית לשורשים משפחתיים — מאגר מאונדקס של רשימות עולים, '
                 'פנקסי בוחרים, קבורות ורשומות רשמיות.'),
    ),
    story=STORY,
    story_subject=('אוזורקוב 1928 — באר שבע 1986 · לודז\', אושוויץ, מאוטהאוזן · סלווינו · '
                   'קיבוץ צאלים · בעלה של צפורה לבית בלם'),
    story_spine=(
        SpineFact('1928', 'נולד באוזורקוב'),
        SpineFact('133332', 'אסיר במאוטהאוזן'),
        SpineFact('1952', 'חבר קיבוץ צאלים'),
        SpineFact('1986', 'נפטר'),
    ),
    privacy_text_patterns=('oh' + 'ad', '@' + 'gmail', 'achi' + 'meir', 'Achi' + 'meir', 'אחי' + 'מאיר', 'אי' + 'לנה', 'Il' + 'ana'),
    privacy_file_patterns=('ארכיון_עבודה/*', 'research_findings.md'),
    qa_strict=(_ENGINE != os.path.join(ROOT, '_common')),
)

if __name__ == '__main__':
    print('מנוע:', _ENGINE)
    build(cfg)
