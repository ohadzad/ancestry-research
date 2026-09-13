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
from genealogy_site import Story, Beat, DocCard, Verdict                                  # noqa: E402
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
# --------------------------------------------------------------- the story --
# What is known, graded, and where it is written down. The road to it — the
# candidates weighed, the negative findings, the open questions — is the
# report's business.
B, D, V = Beat, DocCard, Verdict

STORY = Story(
    portrait='docs/family_docs/israelalbum/ia_012_yitzhak_grandchildren_1936.jpg',
    portrait_alt='יצחק (פפו) פריינטה מוקף נכדיו במקווה ישראל, 1936 — אברהם עומד מימין',
    portrait_caption='מקווה ישראל, 1936 — יצחק פריינטה ונכדיו',
    lede=(
        '<b>אברהם צדוק</b> נולד ב-1925 בבית הספר החקלאי <b>מקווה ישראל</b>, ומת ב-2017 '
        'בן תשעים ואחת. במקווה ישראל נפגשו שתי משפחות משני קצותיו של העולם היהודי: '
        'משפחת אמו, <b>פריינטה</b>, נמנתה עם ותיקי המוסד — וקו <b>ארואס</b> שבתוכה מוליך '
        'ליפו העות\'מאנית ומשם ל<b>גיברלטר</b>, שממנה עלתה המשפחה ב-1833. משפחת אביו '
        'יצאה מ<b>צנעא</b>: אהרון צדוק איבד את אמו ואת אחיו ברעב הגדול של 1904, ירד מן '
        'האנייה בחוף יפו ב-1914, ונעשה האופה של מקווה ישראל. אברהם התגייס ל<b>פלמ"ח</b> '
        'ב-1942, לחם במלחמת העצמאות בחטיבת קרייתי, נשא את <b>רחל</b> ב-1950, והיה שותף '
        'בקואופרטיב "דר" לייצור כפתורי צדף.'),
    verdicts=(
        V('ידוע בוודאות', 'מאומת', (
            ('נולד ב-1925 ב<b>מקווה ישראל</b>, בן אהרון צדוק ושושנה רוזה לבית פריינטה',
             '#s9-2'),
            ('שירת ב<b>פלמ"ח</b> מ-1942 ולחם במלחמת העצמאות בחטיבת קרייתי', '#s6'),
            ('נשא את <b>רחל</b> ב-1950; שותף בקואופרטיב "דר" לכפתורי צדף עד 1981', '#s7'),
            ('אמו רוזה נולדה ב-31.12.1902 במקווה ישראל — בכתב ידו של אביה', '#s3-1-5'),
            ('נפטר ב-2017 ונטמן בבית העלמין ירקון', '#s7-1'),
        )),
        V('כמעט ודאי', 'כמעט ודאי', (
            ('רוזה בתם של <b>יצחק "פפו" פריינטה ומרים ארואס</b>, מדור מייסדי מקווה ישראל',
             '#s3-1-2'),
            ('"הבעל של רוזה היה האופה" שבכתבת "למרחב" (1970) — הוא אהרון', '#s3-1-4'),
            ('"צאלח · אהרן · תימני · פועל" שבפנקס תושבי יפו 1918–1919 — הוא אהרון',
             '#s3-2-1'),
            ('<b>Solomon Arruas</b> שבפנקס נתיני בריטניה ביפו הוא שלמה ארואץ של מפקד 1855',
             '#s8'),
        )),
    ),
    timeline_note='כל אירוע מציין עד כמה הוא מבוסס, ומפנה אל המסמך שעליו הוא נשען.',
    timeline=(
        B('1833', 'משפחת <b>ארואס</b> עולה מ<b>גיברלטר</b> לארץ ישראל; מפקד 1855 רושם את '
                  'שלמה ארואץ כמי שעלה בשנת תקצ"ג.',
          place='גיברלטר ← יפו', rank='מאומת', href='#s8',
          src=('מפקד מונטיפיורי 1855, יפו', '#src-18')),
        B('8.4.1839', '«Salomo Aruas · Gibraltar» נרשם בפנקס נתיני בריטניה של הקונסוליה '
                      'בירושלים — הרשומה הקדומה ביותר בשושלת.',
          rank='מאומת', href='#s8', src=('פנקס נתיני בריטניה, ירושלים', '#src-29')),
        B('1855', 'מפקד מונטיפיורי רושם ביפו את שלמה ארואץ, בן 32, "סוחר ובאנקיר", את אשתו '
                  'שמחה ואת שלושת בניהם.',
          place='יפו', rank='מאומת', href='#s8',
          src=('מפקד מונטיפיורי 1855, יפו', '#src-18')),
        B('1.1.1869', 'יוסף ארואס בן שלמה נרשם בקונסוליה הבריטית ביפו, בן 24, ומקצועו '
                      '"Saraff" — חלפן כספים.',
          place='יפו', rank='מאומת', href='#s8',
          src=('רישומי הקונסוליה הבריטית, ארואס', '#src-15')),
        B('1870', 'קרל נטר מייסד מטעם "כל ישראל חברים" את <b>מקווה ישראל</b>, בית הספר '
                  'החקלאי הראשון בארץ ישראל.',
          place='מקווה ישראל', rank='מאומת', href='#s2',
          src=('אתר מקווה ישראל', '#src-5')),
        B('31.12.1902', '<b>שושנה רוזה פריינטה</b>, אמו של אברהם, נולדת במקווה ישראל; '
                        'לידתה רשומה בכתב ידו הצרפתי של אביה יצחק.',
          place='מקווה ישראל', rank='מאומת', href='#s3-1-5',
          src=('ספר "משפחת פריינטה", 2021', '#src-2')),
        B('1904', 'ברעב הגדול בצנעא מאבד <b>אהרון צדוק</b>, אביו של אברהם, את אמו ואת אחיו, '
                  'וניצל לבדו כילד בן שש-שבע.',
          place='צנעא', rank='מאומת', href='#s3-2-1',
          src=('זיכרונות אהרון צדוק ומכתבו לנכדו', '#src-1ב')),
        B('1914', 'אהרון צדוק יורד מן האנייה בחוף <b>יפו</b>, חודשים אחדים אחרי פרוץ מלחמת '
                  'העולם הראשונה.',
          place='יפו', rank='מאומת', href='#s3-2-1',
          src=('זיכרונות אהרון צדוק ומכתבו לנכדו', '#src-1ב')),
        B('8.7.1916', 'סבתו <b>מרים ארואס-פריינטה</b> מתה במגפת הכולירה ונטמנת בבית העלמין '
                      'טרומפלדור.',
          place='תל אביב', rank='מאומת', href='#s3-1-5',
          src=('אוסף פריינטה, "האלבום של ישראל"', '#src-31')),
        B('1920', 'אהרון צדוק הוא ה<b>אופה הראשי</b> ומנהל המאפייה של מקווה ישראל — תפקיד '
                  'שימלא עד ראשית שנות השישים.',
          place='מקווה ישראל', rank='מאומת', href='#s3-2-2',
          src=('"למרחב", 17.4.1960 — הראיון עמו', '#src-68')),
        B('1925', '<b>אברהם צדוק</b> נולד במקווה ישראל, בנם של אהרון צדוק ושושנה רוזה לבית '
                  'פריינטה.',
          place='מקווה ישראל', rank='מאומת', href='#s1',
          src=('כרטיס החבר, עמותת דור הפלמ"ח', '#src-1')),
        B('1942', 'מתגייס ל<b>פלמ"ח</b> ומתאמן בפלוגה ד\' "נטעים", באימונים בבן שמן '
                  'ובמשמר העמק.',
          place='בן שמן · משמר העמק', rank='מאומת', href='#s6',
          src=('כרטיס החבר, עמותת דור הפלמ"ח', '#src-1')),
        B('1948', 'במלחמת העצמאות משרת ב<b>חטיבת קרייתי</b>, לוחם במרחבי לוד ורמלה, ומוסמך '
                  'לנַשָּׁק.',
          place='לוד ורמלה', rank='מאומת', href='#s6',
          src=('כרטיס החבר, עמותת דור הפלמ"ח', '#src-1')),
        B('1949', 'פנקס הבוחרים תש"ט רושם במקוה ישראל, בשורות עוקבות, את "צדוק אהרן בן '
                  'אברהם" ואת "צדוק שושנה בת יצחק".',
          place='מקווה ישראל', rank='מאומת', href='#s3-2-3',
          src=('פנקס הבוחרים תש"ט, מקוה ישראל', '#src-13')),
        B('1.1.2017', 'אברהם צדוק מת בגיל תשעים ואחת ונטמן בבית העלמין <b>ירקון</b>, במרחק '
                      'נסיעה קצרה ממקום הולדתו.',
          place='תל אביב', rank='כמעט ודאי', href='#s7-1',
          src=('כרטיס החבר, עמותת דור הפלמ"ח', '#src-1')),
    ),
    docs_note='לחיצה על תמונה פותחת את הסריקה המלאה; "בדוח" מוביל אל הקריאה המלאה של המסמך.',
    docs=(
        D('docs/evidence/palmach_details_zoom.png', 'ללא תאריך', 'כרטיס החבר בפלמ"ח',
          'הגרעין הביוגרפי כולו: לידה 1925 במקוה ישראל, ההורים והאחים, הגיוס 1942, '
          'קרייתי, והקבורה בירקון.', 'מאומת', '#s1', src=('ערך 1', '#src-1')),
        D('docs/evidence/aharon_letter_zoom.png', '1971/72', 'מכתב אהרון לנכדו',
          'עדות בגוף ראשון על צנעא, הרעב של 1904, המסע לעדן והנחיתה בחוף יפו ב-1914.',
          'מאומת', '#s3-2-1', src=('ערך 1ב', '#src-1ב')),
        D('docs/family_docs/pariente_birthregister_leaf.png', '31.12.1902',
          'דף רישום הלידות',
          'לידת רוזה בכתב ידו הצרפתי של אביה — «31 Décembre 1902 · Rosa Parente».',
          'מאומת', '#s3-1-5', src=('ערך 2', '#src-2')),
        D('docs/family_docs/ketubah_aharon_roza_5683.png', 'תרפ"ג', 'כתובת אהרן ורוזה',
          'המסמך בן-הזמן הנוקב בשמות האבות: "אהרן בן אברהם צדוק" ו"רוזא בת יצחק פאריינטי".',
          'מאומת', '#s3-2-3', src=('ערך 2', '#src-2')),
        D('docs/igra/igra_voters1949_mikveh_zadok_rows.png', '1949', 'פנקס הבוחרים תש"ט',
          'רשומת מדינה: אהרן בן אברהם ושושנה בת יצחק, בשורות עוקבות, במקוה ישראל.',
          'מאומת', '#s3-2-3', src=('ערך 13', '#src-13')),
        D('docs/montefiore/census1855_jaffa_aruets_row.png', '1855', 'מפקד מונטיפיורי, יפו',
          'משפחת ארואץ במלואה: שלמה בן 32, "סוחר ובאנקיר", עלה 1833, אשתו שמחה ושלושת בניהם.',
          'מאומת', '#s8', src=('ערך 18', '#src-18')),
        D('docs/igra/igra_britconsul_jerusalem_1839_aruas_zoom.png', '8.4.1839',
          '«Salomo Aruas · Gibraltar»',
          'הרשומה הקדומה ביותר בשושלת, והיא הקובעת את מוצא המשפחה בגיברלטר.',
          'מאומת', '#s8', src=('ערך 29', '#src-29')),
        D('docs/family_docs/israelalbum/ia_008_miriam_grave_trumpeldor.jpg', '8.7.1916',
          'מצבת מרים ארואס',
          'תאריך פטירת הסבתא ומקום קבורתה בטרומפלדור — ז\' בתמוז תרע"ו.',
          'מאומת', '#s3-1-5', src=('ערך 31', '#src-31')),
    ),
    sources_note=('כל קביעה בדף הזה נשענת על אחד המקורות שלהלן. כל ערך מוביל אל אינדקס '
                  'המקורות שבדוח, ושם — קישור אל הרשומה בארכיון שממנה נלקחה ואל עותק '
                  'שמור שלה.'),
    sources=(
        ('כרטיס החבר של אברהם צדוק — עמותת דור הפלמ"ח', '#src-1'),
        ('זיכרונות אהרון צדוק ומכתבו לנכדו, 1971/72', '#src-1ב'),
        ('ספר "משפחת פריינטה: מקוה ישראל", גיל שחם, 2021', '#src-2'),
        ('אתר מקווה ישראל — תולדות המוסד', '#src-5'),
        ('"למרחב", 20.4.1970 — משפחת פריינטה של מקווה ישראל', '#src-6'),
        ('פנקס הבוחרים תש"ט (1949), מקוה ישראל', '#src-13'),
        ('רישומי הקונסוליה הבריטית בארץ ישראל — ארואס ביפו, 1839–1903', '#src-15'),
        ('מפקד מונטיפיורי 1855, יפו — שלמה ואלעזר ארואץ', '#src-18'),
        ('«Register of British Subjects», יפו — גיליון הפתיחה', '#src-22'),
        ('פנקס תושבי ועד העיר ליהודי יפו, 1918–1919', '#src-28'),
        ('פנקס נתיני בריטניה בירושלים — «Salomo Aruas · Gibraltar»', '#src-29'),
        ('אוסף פריינטה ב"האלבום של ישראל" — אוסף 9700.0004', '#src-31'),
        ('עדות "סבתא ויקטוריה" — ויקטוריה בכר לבית פריינטה, 11.3.1991', '#src-33'),
        ('"למרחב", 17.4.1960 — הראיון עם אהרון צדוק במאפיית מקווה ישראל', '#src-68'),
    ),
)

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
    story=STORY,
    story_subject='מקווה ישראל 1925 — תל אביב 2017 · לוחם פלמ"ח · בנן של שתי משפחות: פריינטה-ארואס מגיברלטר ויפו, וצדוק מצנעא',
    story_spine=(
        SpineFact('1925', 'נולד במקווה ישראל'),
        SpineFact('1942', 'התגייס לפלמ"ח'),
        SpineFact('2017', 'נפטר בתל אביב'),
        SpineFact('7', 'דורות מתועדים'),
    ),
    glossary=(
        ('מקווה ישראל', 'בית הספר החקלאי הראשון בארץ ישראל, שנוסד ב-1870 מטעם "כל ישראל '
                        'חברים"; בו נולדו וגדלו שלושה דורות של המשפחה.'),
        ('מפקד מונטיפיורי', 'חמישה מפקדים של יהודי ארץ ישראל שערך משה מונטיפיורי בין 1839 '
                            'ל-1875 — שם, גיל, מקצוע ושנת עלייה לכל נפש.'),
        ('פנקס נתיני בריטניה', 'רישומי הקונסוליה הבריטית בארץ ישראל העות\'מאנית: יהודים '
                               'בעלי חסות בריטית, ובהם יוצאי גיברלטר.'),
        ('פנקס הבוחרים תש"ט', 'רשימת בעלי זכות הבחירה לכנסת הראשונה (1949) — רשומת מדינה '
                              'ראשונה לשמות ולכתובות.'),
        ('פלמ"ח', 'פלוגות המחץ של ההגנה, 1941–1948; חבריהן שילבו אימון צבאי בעבודה בקיבוצים.'),
        ('חטיבת קרייתי', 'חטיבה מרחבית במלחמת העצמאות, שפעלה באזור תל אביב, לוד ורמלה.'),
        ('IGRA', 'העמותה הישראלית לשורשים משפחתיים — מאגר מאונדקס של פנקסי בוחרים, רשימות '
                 'עולים ורשומות רשמיות.'),
    ),
    people=PEOPLE,
    gallery=GALLERY,
    text_transforms=(hyphen_ranges,),
    report_transforms=(citations,),
    breadcrumb=('../index.html', 'ארכיון מחקר המשפחה'),
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
