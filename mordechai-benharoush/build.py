# -*- coding: utf-8 -*-
"""mordechai-benharoush — the project's own data. The engine lives in ../common/genealogy_site."""
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
from genealogy_site import figures as F                                                   # noqa: E402

R = lambda *p: os.path.join(ROOT, *p)          # noqa: E731

# the accent of this report: the green of Meknes zellij, against the olive-teal
# of avraham-zadok and the Carpathian brown of rachel-zadok
PAL = Palette(
    accent='#8a4a2a', accent_soft='#b0673f', link='#7a3f22',
    paper='#faf7f3', ink='#2a2320', muted='#6b5f57', line='#ddd3c9',
    hero_from='#3a2118', hero_to='#8a4a2a',
)

P = Person
PEOPLE = (
    P('מרדכי בן הרוש', '1928 – 2010', 'נושא הדף; "מרדושי"; בן יונה ויקוט (פנינה) לבית אוחיון; תעודת הקהילה וכתב העדות, מכנאס 1949–1950; עזב רווק ולבדו; לסה-פסה ירושלים 1950 (סנדלר; חזרה למרוקו); מעברת טירת הכרמל 1956; צו בית משפט 1990 — נולד 1928; רשומת רשפים 22.6.1949 (ככל הנראה); ככל הנראה "בנערוש מרדושי" ממגדים 1954',
      '#s5-5', 'Mordechai Mordekhai Mardochée Mardoch Ben Harush Benharoush Benharoch Benharrosh Benarroche בנהרוש בן-הרוש בן הראש בנערוש בנארוש הרוש מרדושי מרדושה מגדים Megadim ירושלים רשפים Reshafim'),
    P('יונה בן הרוש', '1898? (משפחה) / 1912 (רשימה), מכנאס', 'אביו; מקצוע ההורים: סוחר, העיר החדשה (פנקס 1953); עלה ב"ארצה" 11.6.1956 לצפת; בן מרדכי ומרים', '#s5-3', 'Yona Jonas Ben Harush בנארוש Benarroch ארצה צפת'),
    P('יקוט (פנינה) בן הרוש לבית אוחיון', '1918', 'אמו; בת דוד אוחיון (כתב העדות 1949); "יקוט" במסמכים, "פנינה" בפי המשפחה בלבד (ככל הנראה אותה אישה); עלתה עם יונה ב-1956 לצפת', '#s5-3', 'Yakut Yacot Yacoth Yacout יאקוט פנינה אוחיון חיון Ohayon Hayoun Penina Pnina Ben Harush'),
    P('יעקב בן הרוש', '1933', 'אחיו; אשתו מרי (1936); עלו ב"ארצה" 1956 לצפת', '#s5-3', 'Yaakov Jacob Ben Harush מרי'),
    P('אסתר בן הרוש', '1948, מכנאס', 'אחותו; פנקס אליאנס מכנאס 1953 (Yona/Yacot); רשימת 1956', '#s5-2', 'Esther Benarroch בנארוש'),
    P('גבריאל (גבי), ז\'וליט וסלומון בן הרוש', '1942 · 1943 · 1945', 'אחיו ואחותו; רשימת "ארצה" 1956', '#s5-3', 'Gabriel Juliette Salomon Ben Harush'),
    P('ניסים (מקסים) ומרים בן הרוש', '', 'אחיו הבכורים; לא עלו לישראל (משפחה)', '#s6', 'Nissim Maxime Maxim Miriam Ben Harush'),
    P('מיכאל מכלוף בן הרוש', '', 'אחיו הצעיר; עלה בנפרד, מועד לא ידוע (משפחה)', '#s6', 'Michael Michel Makhlouf Maklouf Ben Harush'),
    P('חנה (אנה?) ויוני בן הרוש', '', 'אשתו הראשונה של מרדכי ובנם (משפחה; פרטים מזעריים — 9.6)', '#s6', 'Hana Anna Yoni Ben Harush'),
    P('דוד אוחיון', '', 'סבו — אביה של יקוט (כתב העדות, מכנאס 1949)', '#s5-5', 'David Daoud Ohayon Hayoun אוחיון'),
    P('מרים בן הרוש לבית דהן', 'נ׳ 1939, מכנאס', 'אשתו — נושאת המחקר האחר בארכיון הזה', '#s2', 'Miriam Mary Marie Dahan דהן'),
)

GALLERY = (
    (F.thumb(ROOT, 'docs/ev_mordechai_photo_1950.jpg', 440), 'docs/1950-03-07_certificat_communaute.jpg', 'מרדכי בן הרוש, כבן 22 — התצלום המהודק לתעודת הקהילה, מכנאס, מרץ 1950 (באדיבות המשפחה)'),
    (F.thumb(ROOT, 'docs/ev_certificat_1950_text.jpg', 440), 'docs/1950-03-07_certificat_communaute.jpg', 'תעודת ועד הקהילה היהודית במכנאס, 7.3.1950 — בן יונאס בנארוש ויאקות חיון'),
    (F.thumb(ROOT, 'docs/ev_traduction_1950_parents.jpg', 440), 'docs/1950-08-10_traduction_acte_p1.jpg', 'תרגום כתב העדות, 1950 — "מרדכי בן יונה בנהרוש ויאקות בת דאוד אוחיון", יליד מכנאס, רווק עד שעזב לארץ ישראל'),
    (F.thumb(ROOT, 'docs/ev_laissez_passer_1950_text.jpg', 440), 'docs/1950-08-11_laissez-passer_consulat_jerusalem.jpg', 'לסה-פסה של הקונסוליה הצרפתית בירושלים, 11.8.1950 — נולד כמשוער 1928 במכנאס, סנדלר; לנסיעת חזרה למרוקו'),
    (F.thumb(ROOT, 'docs/ev_court_order_1990.jpg', 440), 'docs/1990-12-20_court_order_birth_year.jpg', 'צו בית משפט השלום בת ים–חולון, 20.12.1990 — המבקש נולד בשנת 1928 (מספר הזהות מושחר)'),
    (F.thumb(ROOT, 'docs/ev_envelope_1956_address.jpg', 440), 'docs/1956-08-01_envelope_ben_dor.jpg', 'מעטפה רשומה, 1.8.1956 — בן הרוש מרדכי, צריף 171, מעברת טירת הכרמל'),
    (F.thumb(ROOT, 'docs/1949_reshafim_p12.jpg', 440), 'docs/1949_reshafim_p12.jpg', 'רשימות עולי קיבוץ רשפים, 19.9.1949 — בן-ארוש מרדכי, 1927, מרוקו, הגיע 22.6.49, יצא לצבא'),
    (F.thumb(ROOT, 'docs/ev_benharoush_1956.jpg', 440), 'docs/1956-06-11_artza_p4.jpg', 'ההורים יונה ויקוט והאח יעקב — רשימת העולים של "ארצה", 11.6.1956'),
    (F.thumb(ROOT, 'docs/ev_esther_1953.jpg', 440), 'docs/AIU_MA_240.2_00028.jpg', 'אסתר בנארוש, בת יונה ויקוט — פנקס אליאנס מכנאס 1953'),
    (F.thumb(ROOT, 'docs/ev_yalkut_1954_row.jpg', 440), 'docs/yalkut_407_p647.jpg', 'ילקוט הפרסומים 407 — בנערוש מרדושי ← בן הרוש מרדכי, מגדים 1954'),
    (F.thumb(ROOT, 'docs/ev_yalkut_1964_row.jpg', 440), 'docs/yalkut_1144_p901.jpg', 'ילקוט הפרסומים 1144 — בן הראש מרדושה ← בן הראש מרדכי, ירושלים 1963, מס\' זהות 6419140 — מועמד שני, ככל הנראה נשלל לפי מספר זהות'),
    (F.thumb(ROOT, 'docs/ev_yalkut_1954_row_id.jpg', 440), 'docs/yalkut_407_p647_olaw.jpg', 'אותה שורה בסריקת הגיליון מאתר olaw.org.il — עמודת מספר הזהות גלויה: ז/203321'),
    (F.thumb(ROOT, 'docs/ev_yalkut_1954_header.jpg', 440), 'docs/yalkut_407_p647.jpg', 'כותרת הרשימה — הודעה בדבר שינויי שם, רשימה 10, מחוז חיפה — נפת חדרה'),
    (F.thumb(ROOT, 'docs/ev_row159_1949.jpg', 440), 'docs/1949-10_list_p3.jpg', 'רשימת אוקטובר 1949, שורה 159 — בן-ארוס מחלוף, הורים דוד/פרחה: נשלל'),
    (F.thumb(ROOT, 'docs/1949-03_list_p45.png', 440), 'docs/1949-03_list_p45.png', 'רשימת העולים מ-21.3.1949 — משפחת בן הרוש שנשללה'),
)


def citations(t):
    """`[[13]]` in the prose becomes a link into the source index."""
    return re.sub(r'\[\[(\d+)\]\]',
                  lambda m: f'<a href="#src-{m.group(1)}" class="cit" title="אל ערך המקור">[{m.group(1)}]</a>', t)


_HEB = '\u0590-\u05ff'
_RANGE = re.compile(r'(?<![\w' + _HEB + r'/.-])(\d{3,4}-\d{3,4})(?![\w' + _HEB + r'/.-])')


def hyphen_ranges(t):
    return _RANGE.sub(r'<bdi dir="ltr">\1</bdi>', t)


cfg = ProjectConfig(
    root=ROOT,
    slug='mordechai-benharoush',
    main_html='מרדכי-בן-הרוש.html',
    title='מרדכי בן הרוש',
    subject='1931, מכנאס — 2010 · דף נלווה למחקר על מרים בן הרוש · שלושה מסמכים שלו ממכנאס, שתי רשומות של משפחתו · מועמד אחד לרשומת שינוי השם',
    meta_description=('דף מחקר על מרדכי בן הרוש, בן יונה ויקוט (פנינה), יליד מכנאס 1928 (צו בית משפט 1990) שעלה לבדו — תעודת הקהילה וכתב העדות ממכנאס 1949–1950, משפחתו בפנקס אליאנס 1953 וברשימת "ארצה" 1956, המועמד ממושב מגדים 1954 (מועמד שני מירושלים 1963 נשלל לפי מספר זהות), ומה נשלל.'),
    report_md='report.md',
    sources_md='sources-index.md',
    changelog_md='CHANGELOG.md',
    tree=TreeSource(kind='html_extract', path='tree.html', page_href='tree.html'),
    palette=PAL,
    md_extensions=('tables',),
    thumb_referrers=('../index.html', '../research_registry.json'),
    spine=(
        SpineFact('8', 'מסמכים של מרדכי עצמו'),
        SpineFact('1', 'רישום — ככל הנראה שלו'),
        SpineFact('7', 'רשומות שנשללו'),
        SpineFact('20/29', 'קובצי עולים 1947–49 שנקראו'),
    ),
    people=PEOPLE,
    gallery=GALLERY,
    text_transforms=(hyphen_ranges,),
    report_transforms=(citations,),
    breadcrumb=('../index.html', 'ארכיון מחקר המשפחה'),
    provenance_note=('העמוד הזה טוען את התצלומים ואת המסמכים ישירות מתיקיית <code>docs/</code> '
                     'שלצדו — לחיצה על כל ראיה פותחת את קובץ המקור המלא.'),
    footer_note=('מסמך זיכרון משפחתי · כל קביעה שבו נשענת על מסמך: קישור חיצוני אל המקור '
                 'וקישור פנימי אל עותק שמור. מה שלא אומת — מסומן ככזה.'),
    legacy_anchors={f's{n}': r'^' + str(n) + r'\.' for n in range(1, 10)},
    site_extra_files=('tree.html',),
    search_extra=(
        ('מושב מגדים', '#s3', 'מקום', 'Megadim מגדים עתלית Atlit'),
        ('ילקוט הפרסומים 407 (1955)', '#s3-1', 'מקור', 'ילקוט הפרסומים שינוי שם 1954 1955'),
        ('רשימות העולים 1947–1949', '#s5-1', 'מקור', 'רשימת עולים ארכיון המדינה Pinpoint גל-15492 גל-15493 גל-15494 קפריסין'),
        ('פנקסי אליאנס מרוקו', '#s5-2', 'מקור', 'Alliance AIU Benharoch Benarroch Harroch'),
        ('ממצאים שליליים', '#s9-4', 'נושא', 'ממצא שלילי נשלל'),
    ),
    toc_overrides={
        r'^1\.': '1 · תמצית',
        r'^2\.': '2 · מהמשפחה',
        r'^3\.': '3 · המועמד הפתוח',
        r'^4\.': '4 · נשללו',
        r'^5\.': '5 · המשפחה במסמכים',
        r'^6\.': '6 · עץ המשפחה',
        r'^7\.': '7 · פעולות פתוחות',
        r'^8\.': '8 · המקורות',
        r'^9\.': '9 · שיטה ומגבלות',
    },
    privacy_text_patterns=('ohad' + 'z', '@' + 'gmail'),
    published_ids=('6419140',),  # ילקוט הפרסומים 1144 — פרסום רשמי
    qa_strict=(_ENGINE != os.path.join(ROOT, '_common')),
)

if __name__ == '__main__':
    print('מנוע:', _ENGINE)
    build(cfg)
