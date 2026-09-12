# -*- coding: utf-8 -*-
"""miriam-benharoush — the project's own data. The engine lives in ../common/genealogy_site."""
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
    accent='#1f6f5b', accent_soft='#2f8a72', link='#155c4a',
    paper='#f9f8f3', ink='#1e2a32', muted='#5e6b73', line='#dbe0d8',
    hero_from='#12302a', hero_to='#1f6f5b',
)

P = Person
PEOPLE = (
    P('מרים (מרי) בן הרוש לבית דהן', 'נ׳ 1939, מכנאס', 'נושאת המחקר; פנקס אליאנס מכנאס 1949; עלתה 1956; חולון',
      '#s1', 'Miriam Mary Marie Mari Dahan Ben Harush Benharoush Benharoch דהאן בנהרוש בן-הרוש מכנאס Meknes'),
    P('שלום דהן', 'נ׳ 1920', 'אביה; חייט במלאח הישן של מכנאס (פנקס 1949); "ירושלים" 1956 → קריית שמונה; ירושלים; נפטר 15.6.1979? (משפחה)',
      '#s6', 'Shalom Chalom Dahan דהאן חייט Tailleur Mellah'),
    P('יקוט דהן לבית אבוטבול', 'נ׳ 1921', 'אמה; בת יצחק ורבקה אבוטבול; "ירושלים" 1956; ירושלים; נפטרה 3.3.1976 (משפחה)', '#s6', 'Yakut Yacot Yacout Yakot Jacot יאקוט יקות אבוטבול Abitbol Dahan'),
    P('חביב דהן', 'נ׳ ~1880', 'סבה; אבי שלום, מכלוף ושלומון; עלה ב"ירושלים" 1956', '#s5-1', 'Habib Dahan חביב'),
    P('צפורה דהן', 'נ׳ ~1880', 'דודתו של שלום; נרשמה "אם" ברשימת 1956; עלתה איתם', '#s5-1', 'Tzipora Zipora צפורה Dahan'),
    P('מכלוף דהן', 'נ׳ 1903', 'דודה; אחיו של שלום; באותה רשימה עם אשתו סמחה וילדיהם, לקריית שמונה; בנותיו רחל, לורט(?) ומסעודי — ברמת הדסה (ככל הנראה)', '#s5-1', 'Makhlouf Maklouf Dahan סמחה שמחה Simha רמת הדסה'),
    P('שלומון דהן', 'נ׳ 1922', 'דודה; אחיו של שלום; באותה רשימה, בבלוק של אביו חביב, לקריית שמונה', '#s5-1', 'Salomon Shlomon Shlomo Dahan'),
    P('רבקה דהן', 'נ׳ 1944', 'אחותה; פנקס אליאנס 1950, עזבה אוקטובר 1955', '#s3-2', 'Rivka Rebecca Rébéca Rebeca Dahan'),
    P('רחל דהן', 'נ׳ 1947', 'אחותה; פנקס אליאנס 1953', '#s3-3', 'Rachel Dahan'),
    P('מרדכי בן הרוש', '1931 – 2010', 'בעלה; בן יונה ויקוט (פנינה), עלה 1947/48 לבדו — דף מחקר נלווה',
      '#s5-2', 'Mordechai Mordekhai Mardochée Ben Harush Benharoush מרדושי'),
)

GALLERY = (
    (F.thumb(ROOT, 'docs/ev_marie_1949.jpg', 440), 'docs/AIU_MA_240.1_40.jpg', 'מרי דהן — פנקס אליאנס מכנאס 1949, מס׳ 1617'),
    (F.thumb(ROOT, 'docs/ev_rebeca_1950.jpg', 440), 'docs/AIU_MA_240.1_51.jpg', 'רבקה דהן — פנקס 1950, מס׳ 1878'),
    (F.thumb(ROOT, 'docs/ev_rachel_1953.jpg', 440), 'docs/AIU_MA_240.2_00028.jpg', 'רחל דהן — פנקס 1953, מס׳ 3054'),
    (F.thumb(ROOT, 'docs/ev_shalom_1956.jpg', 440), 'docs/1956-01-15_yerushalayim_p8.jpg', 'משפחת דהן — רשימת העולים של "ירושלים", 15.1.1956'),
    (F.thumb(ROOT, 'docs/ev_dahan_1956.jpg', 440), 'docs/1956-01-15_yerushalayim_p8.jpg', 'שלוש משפחות דהן באותו עמוד — מכלוף, שלום, שלומון'),
    (F.thumb(ROOT, 'docs/ev_rachel_maklouf_1949.jpg', 440), 'docs/AIU_MA_240.1_41.jpg', 'רחל דהן, בת מכלוף וסמחה — פנקס 1949, מס׳ 1661 (בת-דודתה של מרים, ככל הנראה)'),
    (F.thumb(ROOT, 'docs/ev_header_1949.jpg', 440), 'docs/AIU_MA_240.1_40.jpg', 'כותרות העמודות של הפנקס — "Nom des parents ou des tuteurs des enfants"'),
)


def citations(t):
    """`[[13]]` in the prose becomes a link into the source index."""
    return re.sub(r'\[\[(\d+)\]\]',
                  lambda m: f'<a href="#src-{m.group(1)}" class="cit" title="אל ערך המקור">[{m.group(1)}]</a>', t)


_HEB = '֐-׿'
_RANGE = re.compile(r'(?<![\w' + _HEB + r'/.-])(\d{3,4}-\d{3,4})(?![\w' + _HEB + r'/.-])')


def hyphen_ranges(t):
    return _RANGE.sub(r'<bdi dir="ltr">\1</bdi>', t)


cfg = ProjectConfig(
    root=ROOT,
    slug='miriam-benharoush',
    main_html='מרים-בן-הרוש.html',
    title='ממכנאס לחולון: מרים בן הרוש לבית דהן',
    subject='1939, מכנאס — חולון · מחקר גנאלוגי מתועד-מקורות · בתחילתו',
    meta_description=('מחקר גנאלוגי מתועד-מקורות על מרים בן הרוש לבית דהן, ילידת מכנאס 1939 שעלתה ב-1956 — '
                      'שלוש רשומות בפנקסי אליאנס במכנאס על שם ההורים שלום ויקוט, עץ משפחה, גלריית ראיות ואינדקס מקורות.'),
    report_md='report.md',
    sources_md='sources-index.md',
    changelog_md='CHANGELOG.md',
    tree=TreeSource(kind='html_extract', path='tree.html', page_href='tree.html'),
    palette=PAL,
    md_extensions=('tables',),
    thumb_referrers=('../index.html', '../research_registry.json'),
    spine=(
        SpineFact('1', 'רשומת עלייה, 15.1.1956'),
        SpineFact('3', 'רשומות פנקס אליאנס'),
        SpineFact('16', 'בני משפחה ברשימת 1956'),
        SpineFact('8', 'סריקות מקור שמורות'),
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
        ('מכנאס — המלאח הישן', '#s3', 'מקום', 'Meknes Meknès מקנס מכנס Mellah מלאח'),
        ('בית הספר לבנות של אליאנס במכנאס', '#s3', 'מקור', 'Alliance AIU École de Filles כל ישראל חברים CAHJP AIU-MA-240'),
        ('רשימות העולים 1955–1957', '#s5-1', 'מקור', 'רשימת עולים ארכיון המדינה Pinpoint גל-15498 גל-15499 גל-15500'),
        ('ממצאים שליליים', '#s9-4', 'נושא', 'ממצא שלילי negative נשלל'),
        ('פעולות פתוחות', '#s7', 'נושא', 'צעדים הבאים open actions'),
    ),
    toc_overrides={
        r'^1\.': '1 · תמצית',
        r'^2\.': '2 · מהמשפחה',
        r'^3\.': '3 · פנקסי אליאנס',
        r'^4\.': '4 · הזיהוי',
        r'^5\.': '5 · מה לא נמצא',
        r'^6\.': '6 · עץ המשפחה',
        r'^7\.': '7 · פעולות פתוחות',
        r'^8\.': '8 · המקורות',
        r'^9\.': '9 · שיטה ומגבלות',
    },
    privacy_text_patterns=('ohad' + 'z', '@' + 'gmail'),
    qa_strict=(_ENGINE != os.path.join(ROOT, '_common')),
)

if __name__ == '__main__':
    print('מנוע:', _ENGINE)
    build(cfg)
