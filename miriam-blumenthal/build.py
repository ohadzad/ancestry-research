# -*- coding: utf-8 -*-
"""miriam-blumenthal — the project's own data. The engine lives in ../common/genealogy_site."""
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

# the accent of this report: a warm ochre, beside the orchard green of yaakov-blumenthal —
# a couple shares a temperature, as the other couples' pages do
PAL = Palette(
    accent='#7a5a24', accent_soft='#9a7a44', link='#6a4c18',
    paper='#faf8f4', ink='#2a241c', muted='#695f50', line='#e2dbcc',
    hero_from='#3a2a12', hero_to='#7a5a24',
)

P = Person
PEOPLE = (
    P('מרים (מגדה) בלומנטל לבית ליבוביץ', '1925 – 2003?', 'נושאת הדף; לפי המשפחה — מהונגריה; פועלת, חובבי ציון 12, פתח תקווה, 1948; נישאה ליעקב בלומנטל 27.10.1948; אם מאיר, שמשון, משה ונאוה (ילדיה — אחימאיר)',
      '#s3-1', 'Miriam Magda Leibovitz Leibowitz Lejbowicz Lajbowicz Lebowits Blumenthal Achimeir Ahimeir מגדה לייבוביץ בלומנטל'),
    P('משה הלוי ליבוביץ', 'מת לפני 1948', 'אביה, לפי תעודת הנישואין; לוי', '#s3-2', 'Moshe Mozes Mose Mojzesz HaLevi Halevy Leibovitz Lebowits'),
    P('פרימט ליבוביץ', 'מתה לפני 1948', 'אמה, לפי תעודת הנישואין', '#s3-2', 'Frimet Frimit Frima Frymeta Frumet Fruma'),
    P('משה ופרימה ליבוביץ, באלאשאג\'רמאט', '1890 · 1892 – 1944?', 'מועמדים — טעון אימות: זוג בשמות הוריה, הורים לשבעה, נספו; דפי עד מאת יצחק ליבוביץ, 1957', '#s4-1',
      'Mose Frima Frimit Lebowits Balassagyarmat Balasagyarmat Gyarmat'),
    P('יעקב בלומנטל', 'כ-1918 – אחרי 11.1974', 'בעלה — נושא המחקר האחר בארכיון הזה', '#s3-1', 'Yaakov Blumenthal Achimeir'),
    P('מאיר בלומנטל', '11.4.1952 – 21.11.1974', 'בנה (כמעט ודאי); חייל בחיל האוויר, סמל ראשון לאחר מותו; כדורגלן הפועל פתח תקווה; על שמו — "אחימאיר"',
      '#s5-1', 'Meir Blumenthal Blumi בלומי'),
    P('שמשון אחימאיר', '26.1.1954', 'בנה; נשוי לאילנה לבית קוטנר — ילדיהם טל, איל ושירי', '#s5-3', 'Shimshon Achimeir Blumenthal'),
    P('משה ונאוה', '—', 'ילדיה, לפי כרטיס ההתאמה ב-MyHeritage', '#s5-3', 'Moshe Nava'),
)

GALLERY = (
    (F.thumb(ROOT, 'docs/ev_marriage_wife.jpg', 440), 'docs/igra/marriage_cert_H99915_petah_tikva_1948-10-27.jpg', 'תעודת הנישואין, פתח תקווה, 27.10.1948 — "מרים ליבוביץ, 22, פועלת ... חובבי ציון 12 ... משה הלוי ליבוביץ ... פרימט"'),
    (F.thumb(ROOT, 'docs/ev_voters_1949_row394.jpg', 440), 'docs/igra/voters_1949_petah_tikva_gal-45496-2_line394_leibovitz_miriam.jpg', 'רשימת בעלי זכות הבחירה לכנסת, תש"ט (1949), פתח תקווה — "ליבוביץ מרים משה 1925 חובבי ציון 12"'),
    (F.thumb(ROOT, 'docs/candidates/yv_pot_569649_frima_lebowits_balassagyarmat.jpg', 440), 'docs/candidates/yv_pot_569649_frima_lebowits_balassagyarmat.jpg', 'מועמדת — טעון אימות: דף העד של פרימה ליבוביץ, באלאשאג\'רמאט, 1892; בעלה משה; 7 ילדים'),
    (F.thumb(ROOT, 'docs/izkor/izkor_96850_meir_portrait.jpg', 300), 'docs/izkor/izkor_96850_meir_blumenthal.txt', 'בנה מאיר בלומנטל, 1952–1974 — "בן מרים ויעקב"; מתוך דף ההנצחה באתר יזכור'),
)


def citations(t):
    """`[[13]]` in the prose becomes a link into the source index."""
    return re.sub(r'\[\[(\d+)\]\]',
                  lambda m: f'<a href="#src-{m.group(1)}" class="cit" title="אל ערך המקור">[{m.group(1)}]</a>', t)


_HEB = '֐-׿'
_RANGE = re.compile(r'(?<![\w' + _HEB + r'/.-])(\d{3,4}-\d{3,4})(?![\w' + _HEB + r'/.-])')


def hyphen_ranges(t):
    return _RANGE.sub(r'<bdi dir="ltr">\1</bdi>', t)


# --------------------------------------------------------------- the story --
B, D, V = Beat, DocCard, Verdict

STORY = Story(
    portrait='docs/ev_marriage_portrait.jpg',
    portrait_alt='תעודת הנישואין, פתח תקווה, 27.10.1948: יעקב בלומנטל, 30, חייל; מרים ליבוביץ, 22, פועלת, חובבי ציון 12',
    portrait_caption='פתח תקווה, 27.10.1948 — תעודת הנישואין',
    lede=(
        '<b>מרים בלומנטל</b> — מרים ליבוביץ מלידה, "מגדה" לפי עץ משפחה — נישאה ל<b>יעקב בלומנטל</b> '
        'ב-27 באוקטובר 1948 ברבנות פתח תקווה. היא הייתה אז <b>פועלת</b> בת 22, גרה ברחוב חובבי ציון 12, '
        'והוריה, <b>משה הלוי ופרימט ליבוביץ</b>, כבר לא היו בחיים; גם הוריו של החתן, חייל באמצע מלחמת העצמאות, '
        'כבר לא היו בחיים. לפי המשפחה, שניהם באו <b>מהונגריה</b>; ברשימת הבוחרים של 1949 — ילידת 1925. '
        'בנה <b>מאיר</b> נולד בפתח תקווה ב-1952; כדורגלן וחייל בחיל האוויר, מת ב-1974, בן 22, '
        'ועל שמו נקראו אחיו <b>אחימאיר</b>. מאיזו עיר בהונגריה באה, ואיך הגיעה ארצה — עוד לא נמצא. '
        'הדף מספר מה שהמסמכים מראים, לפי סדר הזמן.'),
    verdicts=(
        V('ידוע בוודאות', 'מאומת', (
            ('נישאה ל<b>יעקב בלומנטל</b> בפתח תקווה, 27.10.1948', '#s3-1'),
            ('בת <b>משה הלוי ופרימט</b> ליבוביץ, שמתו לפני 1948', '#s3-1'),
            ('לפי המשפחה — <b>מהונגריה</b>', '#s2'),
        )),
        V('כמעט ודאי', 'כמעט ודאי', (
            ('ילידת <b>1925</b> — רשימת הבוחרים, 1949', '#s3-3'),
            ('בנה <b>מאיר</b> — חייל בחיל האוויר, מת ב-1974', '#s5-1'),
        )),
        V('עוד פתוח', 'טעון אימות', (
            ('עיר הולדתה — באלאשאג\'רמאט? (מועמד)', '#s4-1'),
            ('אולי היא מגדה ליבוביץ מבאלאשאג\'רמאט — אושוויץ, רוונסבריק ואלטנבורג, 1944 (מועמדת)', '#s4-2'),
            ('מתי ואיך עלתה ארצה', '#s8'),
            ('פטירתה — 2003, לפי עץ משפחה בלבד', '#s1'),
        )),
    ),
    timeline_note='כל אירוע מציין עד כמה הוא מבוסס, ומפנה אל המסמך שעליו הוא נשען.',
    timeline=(
        B('1925', 'נולדת מרים, בת משה הלוי ופרימט ליבוביץ — בהונגריה, לפי המשפחה; העיר — לא ידועה.',
          rank='כמעט ודאי', href='#s3-3', src=('רשימת הבוחרים, 1949', '#src-2')),
        B('27.10.1948', 'נישאת ל<b>יעקב בלומנטל</b>, חייל בן 30, ברבנות פתח תקווה — כ"ד בתשרי תש"ט. '
                        'היא פועלת, גרה ברחוב חובבי ציון 12; הוריה כבר אינם בחיים.',
          place='פתח תקווה', rank='מאומת', href='#s3-1', src=('תעודת הנישואין', '#src-1')),
        B('1949', 'ברשימת בעלי זכות הבחירה לכנסת — עדיין בשם נעוריה: "ליבוביץ מרים, משה, 1925, חובבי ציון 12".',
          place='פתח תקווה', rank='כמעט ודאי', href='#s3-3', src=('רשימת הבוחרים', '#src-2')),
        B('11.4.1952', 'נולד <b>מאיר</b>, בפתח תקווה.',
          place='פתח תקווה', rank='כמעט ודאי', href='#s5-1', src=('יזכור', '#src-3')),
        B('26.1.1954', 'נולד <b>שמשון</b>. ועוד שניים — משה ונאוה; סדר הלידה — לא ידוע.',
          rank='טעון אימות', href='#s5-3', src=('העץ המשפחתי', '#src-5')),
        B('21.11.1974', 'מאיר, סמל בחיל האוויר ושחקן הפועל פתח תקווה, צונח ומת באימון. המשפחה גרה ברחוב יהוד 2, '
                        'ושנה אחר כך — ברחוב רוטשילד 160א\'.',
          place='פתח תקווה', rank='כמעט ודאי', href='#s5-1', src=('יזכור; "מעריב"', '#src-4')),
        B('אחר כך', 'אחיו של מאיר נקראים <b>אחימאיר</b> — "אחיו של מאיר". מתי — לא ידוע.',
          rank='טעון אימות', href='#s6', src=('מפי המשפחה', '#src-6')),
        B('2003', 'נפטרת — לפי עץ משפחה ב-MyHeritage בלבד.',
          rank='טעון אימות', href='#s1', src=('MyHeritage — התאמה חכמה', '#src-7')),
    ),
    docs_note='לחיצה על תמונה פותחת את הסריקה המלאה; "בדוח" מוביל אל הקריאה המלאה של המסמך.',
    docs=(
        D('docs/igra/marriage_cert_H99915_petah_tikva_1948-10-27.jpg', '27.10.1948', 'תעודת הנישואין',
          '"מרים ליבוביץ, 22, פועלת, חובבי ציון 12" — בת משה הלוי ופרימט.',
          'מאומת', '#s3-1', focus='left 70%', src=('ערך 1', '#src-1')),
        D('docs/igra/voters_1949_petah_tikva_gal-45496-2_line394_leibovitz_miriam.jpg', '1949', 'רשימת הבוחרים',
          '"ליבוביץ מרים, משה, 1925, חובבי ציון 12".',
          'כמעט ודאי', '#s3-3', focus='center 42%', src=('ערך 2', '#src-2')),
        D('docs/candidates/yv_pot_569649_frima_lebowits_balassagyarmat.jpg', '8.1.1957', 'מועמדת: פרימה ליבוביץ',
          'באלאשאג\'רמאט, 1892; בעלה משה; 7 ילדים — אם מרים? לא הוכח.',
          'טעון אימות', '#s4-1', focus='center 30%', src=('ערך 8', '#src-8')),
        D('docs/izkor/izkor_96850_meir_portrait.jpg', '1952–1974', 'מאיר בלומנטל',
          '"בן מרים ויעקב" — חייל בחיל האוויר; נפטר בשירותו.',
          'כמעט ודאי', '#s5-1', src=('ערך 3', '#src-3')),
    ),
    sources_note=('כל קביעה בדף הזה נשענת על אחד המסמכים שלהלן. כל ערך מוביל אל '
                  'אינדקס המקורות שבדוח, ושם — קישור אל הרשומה בארכיון שממנה נלקחה '
                  'ואל עותק שמור שלה.'),
    sources=(
        ('ארכיון המדינה — תעודת הנישואין, פתח תקווה, 1948', '#src-1'),
        ('ארכיון המדינה — רשימת הבוחרים, פתח תקווה, 1949', '#src-2'),
        ('אתר יזכור — מאיר בלומנטל', '#src-3'),
        ('"מעריב" ו"דבר", 1974–1977', '#src-4'),
        ('עץ המשפחה ב-MyHeritage', '#src-5'),
        ('מפי המשפחה, 2026', '#src-6'),
        ('MyHeritage — עץ המשפחה של קרוב ("מ. בלומנטל")', '#src-7'),
        ('ארולסן — תיק האסירה של מגדה ליבוביץ, 1944 (מועמדת)', '#src-9'),
        ('DEGOB — נשים מבאלאשאג\'רמאט, 1945–1946', '#src-10'),
        ('יד ושם — משה ופרימה ליבוביץ, באלאשאג\'רמאט (מועמדים)', '#src-8'),
    ),
)

cfg = ProjectConfig(
    root=ROOT,
    slug='miriam-blumenthal',
    main_html='מרים-בלומנטל.html',
    title='מרים בלומנטל לבית ליבוביץ',
    subject='1925, הונגריה · פועלת בפתח תקווה, 1948 · בת משה הלוי ופרימט · אם מאיר (1952–1974) ושמשון אחימאיר',
    meta_description=('דף מחקר על מרים (מגדה) בלומנטל לבית ליבוביץ, ילידת 1925, הונגריה, אמו של שמשון אחימאיר — תעודת הנישואין עם יעקב בלומנטל, '
                      'פתח תקווה 27.10.1948; הוריה משה הלוי ופרימט; רשימת הבוחרים 1949; '
                      'בנה מאיר, כדורגלן וחייל, 1952–1974, שעל שמו נקראו אחיו אחימאיר.'),
    report_md='report.md',
    sources_md='sources-index.md',
    changelog_md='CHANGELOG.md',
    tree=TreeSource(kind='html_extract', path='tree.html', page_href='tree.html'),
    palette=PAL,
    md_extensions=('tables',),
    thumb_referrers=('../index.html', '../research_registry.json'),
    spine=(
        SpineFact('1948', 'תעודת הנישואין — המסמך הראשון'),
        SpineFact('1925', 'שנת הלידה, רשימת 1949'),
        SpineFact('4', 'ילדים'),
        SpineFact('11', 'רשומות של "מרים ליבוביץ" ו"פרימט" אחרות — נשללו'),
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
        ('פתח תקווה', '#s3-1', 'מקום', 'Petah Tikva Petach Tikva פתח תקוה חובבי ציון יהוד רוטשילד'),
        ('באלאשאג\'רמאט', '#s4-1', 'מקום', 'Balassagyarmat Balasagyarmat Gyarmat גיארמת נוגראד Nograd'),
        ('קריית שאול', '#s5-1', 'מקום', 'Kiryat Shaul בית העלמין הצבאי'),
        ('ממצאים שליליים', '#s9-4', 'נושא', 'ממצא שלילי נשלל'),
    ),
    toc_overrides={
        r'^1\.': '1 · תמצית',
        r'^2\.': '2 · מהמשפחה',
        r'^3\.': '3 · פתח תקווה, 1948–1949',
        r'^4\.': '4 · מועמדות ומועמד',
        r'^5\.': '5 · הילדים',
        r'^6\.': '6 · השם אחימאיר',
        r'^7\.': '7 · עץ המשפחה',
        r'^8\.': '8 · פעולות פתוחות',
        r'^9\.': '9 · שיטה ומגבלות',
    },
    glossary=(
        ('יזכור', 'אתר ההנצחה של משרד הביטחון לחללי מערכות ישראל, ובהם חיילים שנפטרו בשירות.'),
        ('IGRA', 'העמותה הישראלית לשורשים משפחתיים — מאגר מאונדקס של רשימות עולים, '
                 'פנקסי בוחרים, נישואין ורשומות רשמיות.'),
        ('רשימת הבוחרים 1949', 'רשימת בעלי זכות הבחירה לכנסת הראשונה, תש"ט (1949).'),
    ),
    story=STORY,
    story_subject='הונגריה, 1925 — פתח תקווה · פועלת · מאיר ושמשון · אשתו של יעקב',
    story_spine=(
        SpineFact('1925', 'נולדה'),
        SpineFact('1948', 'נישאה ליעקב'),
        SpineFact('4', 'ילדים'),
        SpineFact('1974', 'מות בנה מאיר'),
    ),
    privacy_text_patterns=('@' + 'gmail',),
    privacy_file_patterns=('ארכיון_עבודה/*', 'research_findings.md'),
    qa_strict=(_ENGINE != os.path.join(ROOT, '_common')),
)

if __name__ == '__main__':
    print('מנוע:', _ENGINE)
    build(cfg)
