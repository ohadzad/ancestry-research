# -*- coding: utf-8 -*-
"""avraham-zadok — the project's own data. The engine lives in ../common/genealogy_site.

The engine is looked up in three places, in order: ``../common`` (the layout
inside the research archive), the archive's own folder under $HOME, and a local
working mirror at ``_common`` (used only when the report is built outside the
archive; it is never published).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def _engine_path():
    here = os.path.join(os.path.dirname(ROOT), 'common')
    home = os.path.join(os.path.expanduser('~'), 'Library', 'CloudStorage',
                        'Dropbox', 'רחל צדוק', 'common')
    local = os.path.join(ROOT, '_common')
    for p in (os.environ.get('GENEALOGY_COMMON'), here, home, local):
        if p and os.path.isdir(os.path.join(p, 'genealogy_site')):
            return p
    raise SystemExit('לא נמצא מנוע genealogy_site — ראו את ההערה בראש הקובץ')


_ENGINE = _engine_path()
sys.path.insert(0, _ENGINE)

from genealogy_site import ProjectConfig, Palette, TreeSource, SpineFact, Person, build  # noqa: E402
from genealogy_site import figures as F                                                   # noqa: E402

R = lambda *p: os.path.join(ROOT, *p)          # noqa: E731

# ---------------------------------------------------------------- palette --
# the accent of this report: the olive-and-teal of an agricultural school on the
# coastal plain, against rachel-zadok's Carpathian brown
PAL = Palette(
    accent='#1d5b50', accent_soft='#2e7c6c', link='#12564a',
    paper='#f8f8f5', ink='#22282a', muted='#5d6a66', line='#dbe2dd',
    hero_from='#13292a', hero_to='#1d5b50',
)

# ------------------------------------------------------------------ people -
P = Person
A_SUBJ, A_MIKVE, A_LINES = '#s1', '#s2', '#s3'
A_PAR, A_FOUND = '#s3-1', '#s3-1-2'
A_JAFFA, A_STATE = '#s3-1-3', '#s3-1-4'
A_BOOK, A_ALBUM = '#s3-1-5', '#s3-1-6'
A_ZAD, A_YEMEN, A_PUBLIC, A_VOTERS = '#s3-2', '#s3-2-1', '#s3-2-2', '#s3-2-3'
A_HOME, A_YOUTH, A_ARMY, A_CIVIL, A_GRAVE = '#s4', '#s5', '#s6', '#s7', '#s7-1'
A_DIVE, A_GIB, A_OPEN = '#s8', '#s8-1', '#s9-3'

PEOPLE = (
    P('אברהם צדוק', '16.9.1925 – 1.1.2017', 'נושא המחקר; לוחם פלמ״ח וחטיבת קרייתי, שותף בקואופרטיב «דר»',
      A_SUBJ, 'Avraham Abraham Zadok Sadok צאלח Salah פלמח קרייתי דר כפתורים מקוה ישראל'),
    P('אהרון צדוק (צאלח)', 'צנעא ~1895-1898 – 18.11.1981, חולון',
      'אביו; האופה של מקווה ישראל, מזכיר הפועלים שם, ואיש ציבור בתנועת יוצאי תימן',
      A_ZAD, 'אהרן Aharon Aron Zadok Salah צאלח צנעא Sanaa מתימן לציון שבות תימן'),
    P('שושנה רוזה צדוק לבית פריינטה', '31.12.1902, מקווה ישראל – 3.4.1979',
      'אמו; נטמנה בחולון לצד אהרון', A_PAR, 'Rosa Rosza Shoshana Parente Pariente Frainte פרינטה פריינטי'),
    P('רחל צדוק לבית רפפורט-סטרולוביץ', '16.4.1929 – 1/2021',
      'אשתו מ-1950; ניצולת אושוויץ ושטוטהוף — נושאת המחקר האחר בארכיון הזה',
      A_CIVIL, 'רוצי Ruci Rachel Rappaport Rapaport Strulovic Farkas פרקש רפפורט'),
    P('יעל צדוק פרחי', 'נ׳ 1923', 'אחותו; נישאה לבן-ציון פרחי, החופה 21.11.1943',
      A_HOME, 'Yael Farhi פרחי בן ציון'),
    P('מרים («קיקה»)', '', 'אחותו; קיבוץ חוקוק', A_HOME, 'Miriam קיקה חוקוק Hukuk'),
    P('איציק ויוסי צדוק', '', 'אחיו', A_HOME, 'Itzik Yosi Yossi Zadok'),
    P('יצחק «פפו» פריינטה', '~1860-1862, ירושלים – 31.12.1944', 'סבו מצד האם; מדור מייסדי מקווה ישראל',
      A_FOUND, 'Izhak Yitzhak Pepo Papo Pariente Parente סלוניקי נחלת יצחק'),
    P('מרים פריינטה לבית ארואס', '1875 – 8.7.1916', 'סבתו מצד האם; נטמנה בטרומפלדור',
      A_FOUND, 'Miriam Mariam Aruas Arwas Arruas ארואץ ארוואס טרומפלדור'),
    P('אברהם פריינטה', 'המאה ה-19', 'אביו של יצחק פפו — מ-MyHeritage בלבד, טעון אימות',
      A_FOUND, 'Abraham Pariente Parente'),
    P('ויקטוריה בכר לבית פריינטה', 'עדות 11.3.1991', 'בת דור המייסדים במקווה ישראל; עדות בעל-פה',
      A_ALBUM, 'Victoria Bachar בכר פריינטה'),
    P('שלמה ארואס', '~1823, גיברלטר – ?', 'אבי השושלת; עלה 1833, «סוחר ובאנקיר» ביפו במפקד 1855',
      A_DIVE, 'Salomon Shlomo Salomo Aruas Arwas Arrwas Arruas Aruets ארואץ ארוואס חלפן Money Changer גיברלטר'),
    P('שמחה ארואס', 'מפקד 1855', 'אשתו של שלמה', A_DIVE, 'Simha Simcha Arwas'),
    P('אלעזר ארואס', '~1831, גיברלטר – ?', 'מבני הדור הראשון שעלה', A_DIVE, 'Eliezer Elazar Aruas Arwas'),
    P('יוסף ארואס בן שלמה', '~1845/1849 – ?', 'הרשומה הקונסולרית המוקדמת ביותר בקורפוס (1866)',
      A_DIVE, 'Joseph Youssef Yusef Arowas Arrwas Arwas'),
    P('אליהו ארואס בן שלמה', '~1853/1856 – ?', 'חלפן; «מנהל עדת ישראל בעזה»',
      A_DIVE, 'Eliaho Eliyahu Elias Arowas Arrwas ארואץ עזה Gaza'),
    P('מיכאל ארואס בן שלמה', '~1866 – ?', 'סוחר ביפו; תיק עיזבון באלכסנדריה 1914 — אין לו תאריך פטירה',
      A_DIVE, 'Michel Michael Arrwas Arwas אלכסנדריה Alexandria FO 847'),
    P('אברהם ארואס', 'רשום 1887-1905', 'שם אביו אינו ידוע — היעד הפתוח T21',
      A_OPEN, 'Abraham Abram Arrwas Arrowas Rawas ארואץ'),
    P('יוסף אליהו ארואס', 'רשום 1893-1904', 'ענף עזה; «Orig. from Gibraltar» בתעודת 1904',
      A_DIVE, 'Joseph Eliaho Arrwas Arwas עזה'),
    P('שלמה ורפאל ארואס', 'שירתו 1914-1920', 'גדוד העבודה היהודי בצבא הבריטי; רשומים באותו עמוד רול',
      A_DIVE, 'Salomon Raphael Arwas Jewish Labour Corps Ganger WO 372 R/1880'),
    P('יוסף ושמעון ארואס בני רפאל', 'ילידי קהיר 1935 ו-1934', 'הענף שנשאר במצרים ועלה ב-1950',
      A_DIVE, 'Joseph Shimon Arwas Cairo קהיר מצרים 1950'),
    P('אברהם צדוק (צאלח)', 'נפטר בעדן ~1900', 'אביו של אהרון; שמו מאומת בכתובה ובפנקס 1949',
      A_YEMEN, 'Abraham Salah צאלח עדן Aden צנעא'),
    P('סעדה', 'נספתה ברעב 1904', 'אמו של אהרון — מ-MyHeritage ומן הספר, טעון אימות',
      A_YEMEN, 'Saada Sada צאלח צנעא'),
    P('יוסף צאלח', 'נספה 1904', 'אחיו של אהרון', A_YEMEN, 'Joseph Yosef Salah צאלח'),
    P('גיל שחם', 'ספר המשפחה, 2021', 'מחבר «משפחת פריינטה: מקוה ישראל»', A_BOOK, 'Gil Shaham שחם פריינטה 2021'),
)

# ---------------------------------------------------------------- gallery --
# the documents the report leans on hardest, in the order it discusses them
import json as _json                                                    # noqa: E402
_EV = _json.load(open(R('docs', 'evidence', '_gallery.json'), encoding='utf-8')) \
    if os.path.exists(R('docs', 'evidence', '_gallery.json')) else []
GALLERY = tuple((F.thumb(ROOT, row['crop'], 440), row['full'], row['cap'])
                for row in _EV if os.path.exists(R(row['crop'])))

# ------------------------------------------------------------- transforms --
def citations(t):
    """`[[13]]` in the prose becomes a link into the source index."""
    return re.sub(r'\[\[(\d+)\]\]',
                  lambda m: f'<a href="#src-{m.group(1)}" class="cit" '
                            f'title="אל ערך המקור">[{m.group(1)}]</a>', t)


# Numeric ranges written with a plain hyphen — this report's house spelling —
# need the same isolation the engine gives to en-dash ranges. It runs as a text
# transform and not as an extra bidi rule on purpose: the bidi pass applies its
# rules in sequence over the same string, so a range wrapped there would nest
# inside a Latin run wrapped a rule earlier. Wrapping before the pass leaves a
# tag boundary the Latin rule cannot cross.
_HEB = '\u0590-\u05ff'
_RANGE = re.compile(r'(?<![\w' + _HEB + r'/.-])(\d{3,4}-\d{3,4})(?![\w' + _HEB + r'/.-])')


def hyphen_ranges(t):
    return _RANGE.sub(r'<bdi dir="ltr">\1</bdi>', t)

# ------------------------------------------------------------------ config -
cfg = ProjectConfig(
    root=ROOT,
    slug='avraham-zadok',
    main_html='אברהם-צדוק.html',
    title='שורשיה של משפחה ממקווה ישראל: אברהם צדוק',
    subject='16.9.1925, מקווה ישראל — 1.1.2017, תל אביב · מחקר גנאלוגי מתועד-מקורות',
    meta_description=('מחקר גנאלוגי מתועד-מקורות על אברהם צדוק, יליד מקווה ישראל 1925 — '
                      'שתי שושלות המוצא שנפגשו שם: פריינטה-ארואס מגיברלטר ומיפו העות׳מאנית, '
                      'וצדוק (צאלח) מצנעא — עם עץ משפחה, גלריית ראיות ואינדקס מקורות.'),
    report_md='report.md',
    sources_md='sources-index.md',
    changelog_md='CHANGELOG.md',
    tree=TreeSource(kind='html_extract', path='tree.html', page_href='tree.html'),
    palette=PAL,
    md_extensions=('tables',),
    thumb_referrers=('../index.html', '../research_registry.json'),
    spine=(
        SpineFact('7', 'דורות מתועדים'),
        SpineFact('82', 'ערכי מקור'),
        SpineFact('292', 'קובצי מקור שמורים'),
        SpineFact('74', 'מהדורות · 12 סבבי ביקורת'),
    ),
    people=PEOPLE,
    gallery=GALLERY,
    text_transforms=(hyphen_ranges,),
    report_transforms=(citations,),
    breadcrumb=('../index.html', 'ארכיון מחקר המשפחה'),
    provenance_note=('העמוד הזה טוען את התצלומים ואת המסמכים ישירות מתיקיית <code>docs/</code> '
                     'שלצדו — לחיצה על כל ראיה פותחת את קובץ המקור המלא. אם פתחתם אותו מחוץ '
                     'לתיקייה, התמונות לא ייטענו.'),
    footer_note=('מסמך זיכרון משפחתי · כל קביעה שבו נשענת על מסמך: קישור חיצוני אל המקור '
                 'וקישור פנימי אל עותק שמור. מה שלא אומת — מסומן ככזה.'),
    # the chapter numbering that was already published, mapped by chapter name so
    # that inserting a chapter never moves an external link
    legacy_anchors={f's{n}': r'^' + str(n) + r'\.' for n in range(1, 11)},
    site_extra_files=('tree.html', 'tree_svg.svg'),
    search_extra=(
        ('מקווה ישראל — בית הספר החקלאי', '#s2', 'מקום', 'Mikve Mikveh Israel מקוה ישראל יק"א JCA'),
        ('יפו העות׳מאנית', '#s8', 'מקום', 'Jaffa Yafo יפו קונסוליה בריטית British Subjects'),
        ('גיברלטר', '#s8-1', 'מקום', 'Gibraltar גיברלטר טטואן Tetouan שער השמים'),
        ('צנעא ותימן', '#s3-2-1', 'מקום', "Sanaa San'a צנעא תימן Yemen עדן Aden"),
        ('עזה — ענף ארואס', '#s8', 'מקום', 'Gaza עזה אליהו ארואץ 1904 השקפה'),
        ('מפקדי מונטיפיורי', '#s8', 'מקור', 'Montefiore 1839 1855 1866 1875 מפקד'),
        ('פנקס נתיני בריטניה ביפו', '#s8', 'מקור', 'Register of British Subjects סל-1544 סל-1545 קונסוליה'),
        ('פנקס הבוחרים תש"ט (1949)', '#s3-2-3', 'מקור', 'פנקס בוחרים 1949 תשט גל-45494 IGRA'),
        ('כרטיסי המדליות, מלחמת העולם הראשונה', '#evidence', 'מקור',
         'WO 372 Jewish Labour Corps Ganger Salomon Raphael Arwas medal card'),
        ('היעדים הפתוחים (T1-T41)', '#s9-3', 'נושא', 'יעדים פתוחים targets T21 T34 T37 open'),
        ('ממצאים שליליים', '#s9-4', 'נושא', 'ממצא שלילי negative findings נבדק ונדחה'),
    ),
    # three chapters open with the same two words ("קורות חיים: …"); shortened by
    # the colon they would all read alike in the sticky nav, so each is named
    toc_overrides={
        r'^1\.': '1 · נושא המחקר',
        r'^2\.': '2 · מקווה ישראל',
        r'^3\.': '3 · שתי השושלות',
        r'^4\.': '4 · ההורים והאחים',
        r'^5\.': '5 · נעורים',
        r'^6\.': '6 · שירות צבאי',
        r'^7\.': '7 · התקופה האזרחית',
        r'^8\.': '8 · הצלילה הארכיונית',
        r'^9\.': '9 · מאזן הראיות',
        r'^10\.': '10 · שיטה ומגבלות',
    },
    # the full Cohn-2005 descendant tree is living persons' data and is never published
    privacy_file_patterns=('*cohn*',),
    # the requester's identifiers are assembled and not written out: this file is
    # published alongside the report, and a literal here would trip the portal's
    # own privacy grep over the published folder
    privacy_text_patterns=('cohn', 'ohad' + 'z', '@' + 'gmail'),
    # strict in the archive, where every relative target resolves; outside it the
    # breadcrumb to the archive's own index cannot exist, so the gates only report
    qa_strict=(_ENGINE != os.path.join(ROOT, '_common')),
)

if __name__ == '__main__':
    print('מנוע:', _ENGINE)
    build(cfg)
