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
    accent='#8a4a2a', accent_soft='#b0673f', link='#7a3f22',
    paper='#faf7f3', ink='#2a2320', muted='#6b5f57', line='#ddd3c9',
    hero_from='#3a2118', hero_to='#8a4a2a',
)

P = Person
PEOPLE = (
    P('מרדכי בן הרוש', '1931 – 2010', 'נושא הדף; בן יונה ויקוט, עלה 1947/48; המועמד הפתוח — מגדים 1954',
      '#s1', 'Mordechai Mordekhai Mardochée Ben Harush Benharoush Benharoch בנהרוש בן-הרוש בנערוש בנארוש הרוש מרדושי מגדים Megadim'),
    P('יונה בן הרוש', '', 'אביו (משפחה) — טרם תועד', '#s6', 'Yona Jonas Ben Harush'),
    P('יקוט בן הרוש', '', 'אמו (משפחה) — טרם תועד', '#s6', 'Yakut Yacot Yacout יאקוט Ben Harush'),
    P('מרים בן הרוש לבית דהן', 'נ׳ 1939, מכנאס', 'אשתו — נושאת המחקר האחר בארכיון הזה', '#s2', 'Miriam Mary Marie Dahan דהן'),
)

GALLERY = (
    (F.thumb(ROOT, 'docs/ev_yalkut_1954_row.jpg', 440), 'docs/yalkut_407_p647.jpg', 'ילקוט הפרסומים 407 — בנערוש מרדושי ← בן הרוש מרדכי, מגדים 1954'),
    (F.thumb(ROOT, 'docs/ev_yalkut_1954_header.jpg', 440), 'docs/yalkut_407_p647.jpg', 'כותרת הרשימה — הודעה בדבר שינויי שם'),
    (F.thumb(ROOT, 'docs/1949-03_list_p45.png', 440), 'docs/1949-03_list_p45.png', 'רשימת העולים 24.3.1949 — משפחת בן הרוש שנשללה'),
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
    subject='1931, מרוקו — 2010 · דף נלווה למחקר על מרים בן הרוש · בתחילתו',
    meta_description=('דף מחקר על מרדכי בן הרוש, בן יונה ויקוט, יליד מרוקו 1931 שעלה ב-1947/48 — המועמד הפתוח ממושב מגדים 1954, המועמדים שנשללו, ומה נסרק.'),
    report_md='report.md',
    sources_md='sources-index.md',
    changelog_md='CHANGELOG.md',
    tree=TreeSource(kind='html_extract', path='tree.html', page_href='tree.html'),
    palette=PAL,
    md_extensions=('tables',),
    thumb_referrers=('../index.html', '../research_registry.json'),
    spine=(
        SpineFact('1', 'מועמד פתוח'),
        SpineFact('6', 'רשומות שנשללו'),
        SpineFact('16/29', 'קובצי עולים 1947–49 שנקראו'),
        SpineFact('9', 'ערכי מקור'),
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
