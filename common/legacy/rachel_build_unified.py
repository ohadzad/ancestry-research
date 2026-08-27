# -*- coding: utf-8 -*-
"""Build the unified document: report + evidence figures + family tree + sources index, one HTML file."""
import base64, re, os

# always build relative to this script's own directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

INDEX_STUB = '<!DOCTYPE html>\n<html lang="he" dir="rtl">\n<head>\n<meta charset="UTF-8">\n<meta http-equiv="refresh" content="0; url=%D7%A8%D7%97%D7%9C_%D7%A6%D7%93%D7%95%D7%A7_%D7%94%D7%9E%D7%97%D7%A7%D7%A8_%D7%94%D7%9E%D7%9C%D7%90.html">\n<title>רחל צדוק — המחקר המלא</title>\n</head>\n<body style="font-family:Georgia,serif; background:#faf7f2; color:#2b2620; text-align:center; padding-top:80px;">\n<p>מעביר אל <a href="%D7%A8%D7%97%D7%9C_%D7%A6%D7%93%D7%95%D7%A7_%D7%94%D7%9E%D7%97%D7%A7%D7%A8_%D7%94%D7%9E%D7%9C%D7%90.html">רחל_צדוק_המחקר_המלא.html</a>…</p>\n<script>location.replace(\'%D7%A8%D7%97%D7%9C_%D7%A6%D7%93%D7%95%D7%A7_%D7%94%D7%9E%D7%97%D7%A7%D7%A8_%D7%94%D7%9E%D7%9C%D7%90.html\');</script>\n</body>\n</html>\n'

def thumb_file(path, width=340):
    """Create (once) a small JPEG under docs/thumbs/ and return its relative path."""
    from PIL import Image
    os.makedirs('docs/thumbs', exist_ok=True)
    base = os.path.splitext(os.path.basename(path))[0]
    out = f'docs/thumbs/{base}_{width}.jpg'
    if not os.path.exists(out):
        im = Image.open(path)
        r = width / im.width
        im = im.resize((width, int(im.height*r)), Image.LANCZOS).convert('RGB')
        im.save(out, 'JPEG', quality=78)
    return out

def fig(img_src, caption, link_local=None, link_online=None, maxw=760):
    target = link_local or img_src
    links = [f'<a href="{target}">המסמך המלא (בתיקייה)</a>']
    if link_online: links.append(f'<a href="{link_online}" target="_blank">מקור מקוון</a>')
    ln = ' · '.join(links)
    return (f'<figure style="margin:18px auto; text-align:center; max-width:{maxw}px;">'
            f'<a href="{target}"><img src="{img_src}" loading="lazy" style="max-width:100%; border:1px solid #d8d0c2; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,.08);"></a>'
            f'<figcaption style="font-size:.82rem; color:#6a6154; margin-top:6px;">{caption}' + (f'<br>{ln}' if ln else '') + '</figcaption></figure>')

# ---------- evidence figures ----------
EV = 'docs/evidence/'
AR = 'docs/arolsen_stutthof/'
figs = {}
figs['koblasa'] = fig(EV+'koblasa_1928_row_zoom.png',
    'שורת אוקרמזו (וולובה) בטבלת האחוזות הגדולות של רוס הקרפטית, 1928: 4,515 הקטר — בעלים: Krausz, Farkas, Rappaport',
    'docs/koblasa_1928_estates_podkarpatska_rus.pdf', 'https://www.nacr.cz/wp-content/uploads/2024/04/PH_23_2_2015_Koblasa.pdf')
figs['vater'] = fig(EV+'stutthof_vater_auschwitz_zoom.png',
    'מכרטיס האסירה של רחל בשטוטהוף: "Wohnort d. Angehörigen: Vater Lajos S. z.Zt. Auschwitz" — "מקום מגורי הקרובים: האב לאיוש ס׳, כעת אושוויץ"',
    'docs/arolsen_stutthof/105591047_001.jpg', 'https://collections.arolsen-archives.org/en/search/?s=Strulowits%20Ruci')
figs['einge'] = fig(EV+'stutthof_eingewiesen_zoom.png',
    'שם: "Eingewiesen am 29.6.44, durch KL. Auschwitz, in KL. Stutthof" — נקלטה בשטוטהוף ב-29.06.1944, מאושוויץ',
    'docs/arolsen_stutthof/105591047_001.jpg')
figs['sig'] = fig(EV+'bogen_signature_zoom.png',
    'חתימתה של רחל, בת 15, בתחתית שאלון הקליטה בשטוטהוף: "Sztrulovics Ruci"',
    'docs/arolsen_stutthof/105591037_001.jpg')
figs['rose'] = fig(EV+'rose_kl_au_zoom.png',
    'כרטיס ההפניה על שם האם במרשם שטוטהוף: "STRULAWITS geb. FARKAS, Rose — K.L. Au." (מחנה אושוויץ)',
    'docs/arolsen_stutthof/105590980_001.jpg')
figs['leipheim'] = fig(EV+'cni_leipheim_zoom.png',
    'מכרטיס מרשם השמות המרכזי (ארולסן): "Jetzige Adresse: Leipheim Bl. 24" — מחנה העקורים ליפהיים, בלוק 24',
    'docs/arolsen_dp/cni_farkas_rachel_001.jpg', 'https://collections.arolsen-archives.org/en/document/67014250')
figs['sura_leib'] = fig(thumb_file(EV+'jewishgen_sura1876_leib1894_births_zoom.png', 760),
    'שתי רשומות המפתח (JewishGen, ספרי מיז\'יריה): למעלה — "Sura, ינואר 1876, בת Rapaport Gedajlo ואסתר כץ, וולובה" (לידת סבתא שרה); למטה — "Leib, מרס 1894, אוקרמזו, בן Rapaport Szura" (לידת האב אריה-לייב)',
    'docs/evidence/jewishgen_sura1876_leib1894_births_zoom.png')
figs['census1921'] = fig(thumb_file('docs/hungaricana_1921_census_koselovo_house30_full.png', 900),
    'גיליון מפקד 1921 המקורי במלואו — בית מס\' 30 קושלובו, שני עמודי הפנקס: שורות 1–8 (יעקב, שרה, לייבה, רפקה, אסתר, רוחלה, מנדל, גיטלה), שורות 9–15 (סימה, איציק, חיה, נשו, גדל, פאני — ופפי, אחרונה), וחתימת הפוקד: "Koselovo, 16 בפברואר 1921". מקור: ספריית Hungaricana',
    'docs/hungaricana_1921_census_koselovo_house30_full.png', 'https://library.hungaricana.hu/hu/view/KANepszaml_006_Huszt_Keselyumezo__097_Koseleve-Keselymezo/?pg=298&layout=s', maxw=900)
figs['census1921'] += ('<p style="font-size:.82rem; color:#6a6154; text-align:center; margin-top:-8px;">'
    'שני עמודי הגיליון שמורים גם כ-PDF מקורי באיכות מלאה: '
    '<a href="docs/hungaricana_1921_census_koselovo_house30_pages299-300_original.pdf">PDF (עמ׳ 299–300)</a> · '
    '<a href="docs/hungaricana_1921_census_koselovo_house30_page299_hires.jpg">עמוד 1 JPG</a> · '
    '<a href="docs/hungaricana_1921_census_koselovo_house30_page300_hires.jpg">עמוד 2 JPG</a></p>')
figs['gedalya_m'] = fig(thumb_file(EV+'jewishgen_gedajlo_mindje_marriage_1903_zoom.png', 760),
    'הרישום האזרחי של נישואי גדליה רפפורט (04.03.1903, אוקרמזו): נולד 01.04.1846, בן Mozes רפפורט ו-Jenta שפיגל; הכלה מינדל ברקוביץ ילידת 04.01.1865',
    'docs/evidence/jewishgen_gedajlo_mindje_marriage_1903_zoom.png')
figs['gitel_m'] = fig(thumb_file(EV+'jewishgen_gitel_wolf_1933_mendel_1938_marriages_zoom.png', 760),
    'נישואי הדודה גיטל ("Strulovic Githel", בת Jakub ו-Rapaport Serena) לאלכסנדר וולף, איזה 10.02.1933 — העד: אחיה יצחק; ומתחת: נישואי הדוד מנדל (1938)',
    'docs/evidence/jewishgen_gitel_wolf_1933_mendel_1938_marriages_zoom.png')
figs['regina_m'] = fig(thumb_file(EV+'jewishgen_regina_1896_bat_szura_rappaport_birth_zoom.png', 760),
    'רשומת הלידה של הדודה ריבקה/רגינה (24.05.1896): "Regina, בת Rappaport Szura מאוקרמזו, בת 22, עקרת בית" — ללא שם אב: הדוגמה המובהקת לרישום ילדי הזוג על שם האם',
    'docs/evidence/jewishgen_regina_1896_bat_szura_rappaport_birth_zoom.png')
figs['koblasa'] += ('<p style="font-size:.82rem; color:#6a6154; text-align:center; margin-top:-8px;">'
    '<a href="docs/evidence/koblasa_1928_table_context.png">הקשר הטבלה המלא (צילום)</a></p>')

# ---------- key-document gallery (thumbnails) ----------
GAL = [
 ('docs/arolsen_stutthof/105591047_001.jpg', 'docs/arolsen_stutthof/105591047_001.jpg', 'כרטיס האסירה של רחל, שטוטהוף (38444)'),
 ('docs/arolsen_stutthof/105591037_001.jpg', 'docs/arolsen_stutthof/105591037_001.jpg', 'שאלון הקליטה של רחל + חתימתה'),
 ('docs/arolsen_stutthof/105591030_001.jpg', 'docs/arolsen_stutthof/105591030_001.jpg', 'כרטיס האסירה של סימה (38443)'),
 ('docs/arolsen_stutthof/105590980_001.jpg', 'docs/arolsen_stutthof/105590980_001.jpg', 'כרטיס הפניה — האם רוזה'),
 ('docs/arolsen_stutthof/105590973_001.jpg', 'docs/arolsen_stutthof/105590973_001.jpg', 'כרטיס הפניה — האב לאיוש'),
 ('docs/arolsen_dp/cni_farkas_rachel_001.jpg', 'docs/arolsen_dp/cni_farkas_rachel_001.jpg', 'כרטיס העקורים — ליפהיים'),
 ('docs/yadvashem_pot_scans/10846653_04122013_8915_158.jpg', 'docs/yadvashem_pot_scans/10846653_04122013_8915_158.jpg', 'דף עד על האב — בכתב ידה של רחל (2013)'),
 ('docs/yadvashem_pot_scans/10846654_04122013_8915_159.jpg', 'docs/yadvashem_pot_scans/10846654_04122013_8915_159.jpg', 'דף עד על האם — בכתב ידה'),
 ('docs/yadvashem_pot_scans/10846655_04122013_8915_160.jpg', 'docs/yadvashem_pot_scans/10846655_04122013_8915_160.jpg', 'דף עד על גיטה — בכתב ידה'),
 ('docs/yadvashem_pot_scans/13750274_04122013_8915_161.jpg', 'docs/yadvashem_pot_scans/13750274_04122013_8915_161.jpg', 'דף עד על סימה — בכתב ידה'),
 ('docs/hungaricana_1921_census_koselovo_house30_full.png', 'docs/hungaricana_1921_census_koselovo_house30_pages299-300_original.pdf', 'מפקד 1921 — בית 30 קושלובו: הגיליון המלא (מה-PDF המקורי)'),
 ('docs/evidence/jewishgen_rachel_sima_own_birth_records_zoom.png', 'docs/evidence/jewishgen_rachel_sima_own_birth_records_zoom.png', 'רשומות הלידה האזרחיות של רחל וסימה (JewishGen)'),
 ('docs/evidence/stutthof_transport_list_rows802-803_zoom.png', 'docs/stutthof_museum_2026/POL-AMS-I-IIb-10-099.jpg', 'רשימת הטרנספורט המקורית 29.06.1944 — האחיות בשורות 802–803'),
 ('docs/evidence/jewishgen_births_strulyovics_rappaport_children_1897-1902_zoom.png', 'docs/evidence/jewishgen_births_strulyovics_rappaport_children_1897-1902_zoom.png', 'רשומות הלידה של דודי רחל (1897–1902)'),
]
cards = []
for src, devname, cap in GAL:
    cards.append(f'<a href="{devname}" style="text-decoration:none; color:inherit;"><div style="width:180px;">'
                 f'<img src="{thumb_file(src, 180)}" style="width:100%; border:1px solid #d8d0c2; border-radius:6px;">'
                 f'<div style="font-size:.75rem; color:#5a5142; margin-top:4px; text-align:center;">{cap}</div></div></a>')
gallery = '<div style="display:flex; flex-wrap:wrap; gap:14px; justify-content:center; margin:16px 0;">' + ''.join(cards) + '</div>'

# ---------- tree svg (+legend & footnotes) ----------
tree_html = open('עץ_משפחה_מורחב.html', encoding='utf-8').read()
m = re.search(r'(<svg.*?</svg>)', tree_html, re.S)
tree_svg = m.group(1)
m_leg = re.search(r'<div class="legend">(.*?)</div>\s*\n', tree_html, re.S)
tree_legend = '<div style="display:flex; gap:18px; justify-content:center; flex-wrap:wrap; padding:10px 0 2px; font-size:.85rem;">' + m_leg.group(1).replace('class="dot" style="', 'style="display:inline-block;width:11px;height:11px;border-radius:50%;vertical-align:middle;margin-left:6px;') + '</div>' if m_leg else ''
m_foot = re.search(r'<div class="foot">(.*?)</div>', tree_html, re.S)
tree_foot = '<p style="font-size:.8rem; color:#8a8177; text-align:center; max-width:860px; margin:8px auto 0;">' + m_foot.group(1).strip() + '</p>' if m_foot else ''

# ---------- markdown -> html ----------
import markdown
def md2html(path):
    src = open(path, encoding='utf-8').read()
    src = src.replace('<div dir="rtl">', '').replace('</div>', '')
    return markdown.markdown(src, extensions=['tables'])

report_html = md2html('רחל_צדוק_מחקר_מקיף.md')
# inline any relative <img src="docs/..."> as base64 so the unified file is fully self-contained
import re as _re
def _inline(m):
    alt, path = m.group(1), m.group(2)
    img = f'<img src="{path}" alt="{alt}" loading="lazy" style="max-width:100%; border:1px solid #d8d0c2; border-radius:6px; margin:10px auto 4px; display:block;">'
    cap = f'<span class="imgcap" style="display:block; font-size:.82rem; color:#6a6154; text-align:center; margin:0 0 10px;">{alt}</span>' if alt else ''
    return img + cap
report_html = _re.sub(r'<img alt="([^"]*)" src="(docs/[^"]+)"[^>]*/?>', _inline, report_html)
# drop the alt-caption when an explicit italic caption immediately follows (avoids duplication)
report_html = _re.sub(r'<span class="imgcap"[^>]*>[^<]*</span>(</a></p>\s*<p><em>)', r'\1', report_html)
index_html = md2html('אינדקס_מקורות.md')

# ---------- helper: apply a text substitution only OUTSIDE existing tags/anchors ----------
_TAGSPLIT = re.compile(r'(<a\b[^>]*>.*?</a>|<[^>]+>)', re.S)
def _apply_text(html, fn):
    parts = _TAGSPLIT.split(html)
    for _i in range(0, len(parts), 2):
        parts[_i] = fn(parts[_i])
    return ''.join(parts)

# ---------- source-link transforms ----------
YT = 'https://www.youtube.com/watch?v=GhHKFgl81AU'
def _ts_link(m):
    h, mn, sec = int(m.group(1)), int(m.group(2)), int(m.group(3))
    t = h*3600 + mn*60 + sec
    return f'<a href="{YT}&t={t}s" target="_blank" title="לצפייה ברגע זה בעדות">[{m.group(1)}:{m.group(2)}:{m.group(3)}]</a>'
def _ts_range(m):
    h, mn, sec = int(m.group(1)), int(m.group(2)), int(m.group(3))
    t = h*3600 + mn*60 + sec
    label = ('[<bdi dir="ltr">' + f'{m.group(1)}:{m.group(2)}:{m.group(3)}–{m.group(4)}:{m.group(5)}:{m.group(6)}' + '</bdi>]')
    return f'<a href="{YT}&t={t}s" target="_blank" title="לצפייה בקטע זה בעדות">{label}</a>'
report_html = re.sub(r'\[(\d{2}):(\d{2}):(\d{2})[–-](\d{2}):(\d{2}):(\d{2})\]', _ts_range, report_html)
report_html = re.sub(r'\[(\d{2}):(\d{2}):(\d{2})\]', _ts_link, report_html)

# Yad Vashem name_<id>.json -> internal + external links (index only; skip if already inside a tag attr)
def _yv_link(m):
    i = m.group(1)
    return (f'<a href="docs/yadvashem_records/name_{i}.json">name_{i}.json</a>'
            f' <a href="https://collections.yadvashem.org/en/names/{i}" target="_blank" title="הרשומה באתר יד ושם">↗</a>')
index_html = _apply_text(index_html, lambda _t: re.sub(r'(?<!/)name_(\d+)\.json', _yv_link, _t))
index_html = index_html.replace('testimony_8424116_he/en.json',
    '<a href="docs/yadvashem_records/testimony_8424116_he.json">testimony_8424116_he</a>/<a href="docs/yadvashem_records/testimony_8424116_en.json">en</a>.json '
    '<a href="https://collections.yadvashem.org/en/documents/8424116" target="_blank" title="הרשומה הקטלוגית ביד ושם">↗</a>')

# Arolsen document numbers (plain text) -> external link; internal file when scan exists
import os as _osx
_AR_DOCS = {'105591037','105591042','105591047','105591025','105591030','105590980','105590973'}
def _ar_link(m):
    n = m.group(1)
    out = f'<a href="https://collections.arolsen-archives.org/en/document/{n}" target="_blank" title="המסמך בארכיון ארולסן">{n}</a>'
    if n in _AR_DOCS and _osx.path.exists(f'docs/arolsen_stutthof/{n}_001.jpg'):
        out += f' <a href="docs/arolsen_stutthof/{n}_001.jpg" title="הסריקה בתיקייה">🗎</a>'
    return out
for _pat in [r'(?<![\w/."])(10559\d{4})(?![\w/])']:
    report_html = _apply_text(report_html, lambda _t, _p=_pat: re.sub(_p, _ar_link, _t))
    index_html  = _apply_text(index_html,  lambda _t, _p=_pat: re.sub(_p, _ar_link, _t))

# evidence / docs filenames as plain text in index -> internal links
_DIRS = ['docs/evidence/', 'docs/', 'docs/stutthof_museum_2026/', 'docs/arolsen_stutthof/', 'docs/arolsen_dp/', 'docs/yadvashem_pot_scans/']
def _file_link(m):
    name = m.group(1)
    for d in _DIRS:
        if _osx.path.exists(d + name):
            return f'<a href="{d}{name}">{name}</a>'
    return name
index_html = _apply_text(index_html, lambda _t: re.sub(r'(?<![\w/."=-])([\w][\w\-]*\.(?:png|jpg|JPG|pdf))(?![\w/])', _file_link, _t))

# ---------- bidi guards: keep numeric runs left-to-right inside RTL text ----------
def _latin_run(m):
    t = m.group(1)
    # never leave an unmatched ')' inside the isolate: it would mirror against an '(' outside
    while t.count(')') > t.count('(') and t.endswith(')'):
        t = t[:-1]
    tail = m.group(1)[len(t):]
    return '<bdi dir="ltr">' + t + '</bdi>' + tail

_BIDI_RULES = [
    # long Latin-script runs (quotations) inside RTL paragraphs: keep the whole run left-to-right
    (re.compile(r'(?<![\w])([A-Za-z\u00C0-\u024F][A-Za-z\u00C0-\u024F0-9 ,.:;\-\u2013()/\u2019\u201C\u201D!?]{28,}[A-Za-z\u00C0-\u024F0-9./)])'),
     _latin_run),
    # month/year ranges: 12/1909–02/1911
    (re.compile(r'(?<![\w֐-׿])(\d{1,2}/\d{4}–\d{1,2}/\d{4})(?![\w֐-׿])'),
     r'<bdi dir="ltr">\1</bdi>'),
    # numeric ranges: 1929–2021, 192–201, 802–803, 24–26.08.1944
    (re.compile(r'(?<![\w֐-׿/])(?<![A-Za-z0-9]-)(\d[\d.,:]*–\d[\d.,:]*)(?![\w֐-׿/])'),
     r'<bdi dir="ltr">\1</bdi>'),
    # archive reference codes: 01014102 129.172 / 01010503 001.495.346
    (re.compile(r'(?<![\w֐-׿])(0\d{7}\s\d{3}\.\d{3}(?:\.\d{3})?)(?![\w֐-׿])'),
     r'<bdi dir="ltr">\1</bdi>'),
    # prisoner numbers written with a thousands space, as on the transport list: 38 443
    (re.compile(r'(?<![\w֐-׿])(\d{2}\s\d{3})(?![\w֐-׿.])'),
     r'<bdi dir="ltr">\1</bdi>'),
]
_TAGONLY = re.compile(r'(<[^>]+>)')
_BDI_SPAN = re.compile(r'(<bdi\b[^>]*>.*?</bdi>)', re.S)
def _bidi_fix(html):
    def _f(t):
        for _rx, _rep in _BIDI_RULES:
            t = _rx.sub(_rep, t)
        return t
    def _pass(chunk):
        # apply to every text node, including the inside of <a>…</a>, but never inside a tag
        parts = _TAGONLY.split(chunk)
        for _i in range(0, len(parts), 2):
            parts[_i] = _f(parts[_i])
        return ''.join(parts)
    # never touch what is already inside a <bdi>…</bdi>
    outer = _BDI_SPAN.split(html)
    for _i in range(0, len(outer), 2):
        outer[_i] = _pass(outer[_i])
    return ''.join(outer)

# ---------- extract changelog appendix from report (moved to end of unified doc) ----------
_clm = re.search(r"<h2>נספח ד' — יומן שינויים \(Changelog\)</h2>.*", report_html, re.S)
changelog_html = _clm.group(0) if _clm else ''
if _clm: report_html = report_html[:_clm.start()].rstrip()
changelog_html = changelog_html.replace("<h2>נספח ד' — יומן שינויים (Changelog)</h2>",
                                        '<h2 id="changelog">נספח ד\' — יומן שינויים (Changelog)</h2>')

# ---------- anchors + table of contents ----------
_toc_items = []
_ch_counter = [0]
def _add_id(m):
    _ch_counter[0] += 1
    cid = f'ch-{_ch_counter[0]}'
    title = re.sub(r'<[^>]+>', '', m.group(1))
    _toc_items.append((cid, title))
    return f'<h2 id="{cid}">{m.group(1)}</h2>'
report_html = re.sub(r'<h2>(.*?)</h2>', _add_id, report_html)
_toc_links = ''.join(f'<a href="#{cid}" style="display:block; padding:2px 0; color:#5a5142; text-decoration:none;">{t}</a>' for cid, t in _toc_items)
_toc_links += ('<a href="#tree" style="display:block; padding:2px 0; color:#5a5142; text-decoration:none;">נספח א\' — עץ המשפחה</a>'
               '<a href="#gallery" style="display:block; padding:2px 0; color:#5a5142; text-decoration:none;">נספח ב\' — מסמכי המפתח</a>'
               '<a href="#index" style="display:block; padding:2px 0; color:#5a5142; text-decoration:none;">נספח ג\' — אינדקס המקורות</a>'
               '<a href="#changelog" style="display:block; padding:2px 0; color:#5a5142; text-decoration:none;">נספח ד\' — יומן שינויים</a>')
toc_html = ('<nav style="background:#fdfbf7; border:1px solid #d8d0c2; border-radius:8px; padding:12px 18px; margin:14px 0; column-count:2; column-gap:28px; font-size:.9rem;">'
            '<div style="font-weight:bold; margin-bottom:6px; column-span:all;">תוכן העניינים</div>' + _toc_links + '</nav>')
# insert TOC right after the first </h1>
report_html = report_html.replace('</h1>', '</h1>' + toc_html, 1)

# ---------- inject figures at anchor points ----------
def inject_after(html, anchor_regex, insert):
    m = re.search(anchor_regex, html)
    if not m:
        print('WARN anchor not found:', anchor_regex[:50]); return html
    # insert after the nearest closing tag of the enclosing block (</p> or </li>)
    p_pos = html.find('</p>', m.start())
    li_pos = html.find('</li>', m.start())
    cands = [(p_pos, 4), (li_pos, 5)]
    cands = [(i, l) for i, l in cands if i != -1]
    if not cands:
        pos = m.end()
    else:
        i, l = min(cands)
        pos = i + l
    return html[:pos] + insert + html[pos:]

report_html = inject_after(report_html, r'אחוזת רפפורט באוקרמזו לאורך יותר מ-40 שנה', figs['koblasa'])
report_html = inject_after(report_html, r'נשא שלוש נשים', figs['gedalya_m'])
report_html = inject_after(report_html, r'המבוגרים שבהם רשומים', figs['census1921'])
# (figs['sura_leib'] is placed inline in the Markdown itself — no injection needed)
report_html = inject_after(report_html, r'בעל מכולת בטקהאזה; שניהם נרצחו', figs['gitel_m'])
report_html = inject_after(report_html, r'כנראה עיגול גיל, שהיה שכיח', figs['regina_m'])
report_html = inject_after(report_html, r'ההורים היו רשומים כ"נמצאים כעת באושוויץ', figs['vater'])
report_html = inject_after(report_html, r'תאריך ההגעה לשטוטהוף: 29 ביוני 1944', figs['einge'])
report_html = inject_after(report_html, r'החתימה של רחל, בת 15, בשטוטהוף', figs['sig'])
report_html = inject_after(report_html, r'כרטיס הפניה, לא תיק אסירה', figs['rose'])
report_html = inject_after(report_html, r'מחנה העקורים ליפהיים:', figs['leipheim'])


css = """
body{background:#faf7f2; color:#2b2620; font-family:'David Libre','Frank Ruhl Libre',Georgia,serif; margin:0; line-height:1.62;}
.page{max-width:900px; margin:0 auto; padding:34px 22px 80px;}
h1{font-size:1.8rem; text-align:center; border-bottom:3px double #b5aa99; padding-bottom:12px;}
h2{font-size:1.25rem; color:#5a4a33; border-bottom:2px solid #d8d0c2; padding-bottom:5px; margin-top:38px;}
h3{font-size:1.05rem; color:#5a5142;}
table{border-collapse:collapse; margin:14px auto; font-size:.9rem; width:100%;}
th,td{border:1px solid #d8d0c2; padding:6px 10px; text-align:right; vertical-align:top;}
th{background:#efe9df;}
blockquote{border-right:4px solid #b8860b; background:#fdf6e3; margin:14px 0; padding:10px 16px; font-size:.95rem;}
a{color:#7a5c1e;}
hr{border:none; border-top:1px solid #d8d0c2; margin:30px 0;}
#treePreview svg{width:100%; height:auto; display:block;}
#treeModalBody svg{width:2400px; height:auto; display:block;}
.tocnote{font-size:.85rem; color:#8a8177; text-align:center;}
@media print{.page{padding:10px;}}
"""

out = f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>רחל צדוק לבית סטרולוביץ-רפפורט — המחקר המלא</title>
<style>{css}</style></head>
<body><div class="page">
<p style="font-size:.85rem; color:#8a8177; margin:0 0 14px;"><a href="../index.html" style="color:#7a4a2b; text-decoration:none;">&#8594; ארכיון מחקר המשפחה</a> · רחל צדוק</p>
<p style="background:#efe9df; border:1px solid #d8d0c2; border-radius:8px; padding:8px 14px; font-size:.85rem; color:#5a5142;">מסמך זה הוא חלק מתיקיית המחקר: תצלומי הראיות שבו נטענים ישירות מקובצי המקור שבתיקיות docs/‏ (לחיצה על כל תצלום פותחת את הקובץ המקורי המלא), ולכן יש לפתוח אותו מתוך התיקייה "רחל צדוק" — או מהאתר הסטטי שאליו הועלתה. קישורי המקור הם משני סוגים: קישורים חיצוניים (יוטיוב, יד ושם, ארולסן, JewishGen ועוד) וקישורים יחסיים לעותקי המקור שבתיקייה. חותמות הזמן בפרק העדות הן קישורים לרגע המדויק בעדות המצולמת.</p>
{report_html}
<hr>
<h2 id="tree">נספח א' — עץ המשפחה</h2>
{tree_legend}
<div id="treePreview" title="לחיצה לפתיחת העץ בתצוגה מלאה" style="position:relative; cursor:zoom-in; background:#fff; border:1px solid #d8d0c2; border-radius:10px; padding:8px; margin:14px 0 6px; box-shadow:0 2px 8px rgba(0,0,0,.06);">
  <div style="pointer-events:none;">{tree_svg}</div>
  <div style="position:absolute; bottom:14px; left:50%; transform:translateX(-50%); background:rgba(43,38,32,.78); color:#faf7f2; font-size:.9rem; padding:7px 18px; border-radius:999px; white-space:nowrap;">&#128269;&#65038; לחיצה לפתיחת העץ בתצוגה מלאה וניתנת לגלילה</div>
</div>
{tree_foot}
<p style="text-align:center; font-size:.95rem; margin:10px 0 0;"><a href="עץ_משפחה_מורחב.html" target="_blank">🌳 לפתיחת העץ המלא בחלון נפרד</a> · <a href="עץ_משפחה_גרפי.html" target="_blank">גרסה תמציתית</a></p>
<div id="treeModal" style="display:none; position:fixed; inset:0; z-index:1000; background:rgba(28,24,20,.82);">
  <div style="position:absolute; inset:18px; background:#faf7f2; border-radius:12px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 10px 40px rgba(0,0,0,.5);">
    <div style="display:flex; align-items:center; justify-content:space-between; gap:12px; padding:10px 18px; border-bottom:1px solid #d8d0c2; background:#f2ede4;">
      <div style="font-weight:bold;">עץ משפחת סטרולוביץ-רפפורט ופרקש — תצוגה מלאה <span style="font-weight:normal; color:#8a8177; font-size:.85rem;">(גררו/גללו לכל הכיוונים; Esc לסגירה)</span></div>
      <button id="treeModalClose" style="border:1px solid #b5aa99; background:#fff; color:#2b2620; font-size:1.05rem; border-radius:8px; padding:4px 14px; cursor:pointer; font-family:inherit;">סגירה ✕</button>
    </div>
    <div id="treeModalBody" style="flex:1; overflow:auto; padding:10px;">
      <div style="min-width:2400px;">{tree_svg}</div>
    </div>
  </div>
</div>
<hr>
<h2 id="gallery">נספח ב' — מסמכי המפתח (לחיצה פותחת את הקובץ המלא בתיקייה)</h2>
{gallery}
<p class="tocnote">כלל המסמכים — 120+ קבצים — בתיקיות docs/‏; פירוט מלא בנספח ג'.</p>
<hr>
<h2 id="index">נספח ג' — אינדקס המקורות המלא</h2>
{index_html}
<hr>
{changelog_html}
</div>
<script>
(function(){{
  var pv=document.getElementById('treePreview'), md=document.getElementById('treeModal'),
      cl=document.getElementById('treeModalClose'), bd=document.getElementById('treeModalBody');
  if(!pv||!md) return;
  function open(){{ md.style.display='block'; document.body.style.overflow='hidden';
    var el=bd.firstElementChild; bd.scrollLeft=(el.scrollWidth-bd.clientWidth)/2; }}
  function close(){{ md.style.display='none'; document.body.style.overflow=''; }}
  pv.addEventListener('click', open);
  cl.addEventListener('click', close);
  md.addEventListener('click', function(e){{ if(e.target===md) close(); }});
  document.addEventListener('keydown', function(e){{ if(e.key==='Escape') close(); }});
  var dragging=false, sx=0, sy=0, sl=0, st=0;
  bd.addEventListener('mousedown', function(e){{ dragging=true; sx=e.clientX; sy=e.clientY; sl=bd.scrollLeft; st=bd.scrollTop; bd.style.cursor='grabbing'; e.preventDefault(); }});
  window.addEventListener('mousemove', function(e){{ if(dragging){{ bd.scrollLeft=sl-(e.clientX-sx); bd.scrollTop=st-(e.clientY-sy); }} }});
  window.addEventListener('mouseup', function(){{ dragging=false; bd.style.cursor='auto'; }});
}})();
</script>
</body></html>"""

# ---------- sanity: every local href must exist on disk ----------
import os as _os, re as _rechk
_missing = sorted(set(h for h in _rechk.findall(r'href="(docs/[^"]+)"', out) if not _os.path.exists(h)))
_mention = sorted(set(m2 for m2 in _rechk.findall(r'(?:^|[\s|(>])((?:docs|ארכיון_עבודה)/[\w\-./\u0590-\u05FF]+\.(?:jpg|png|pdf|json|mp3|txt))', out) if not _os.path.exists(m2)))
if _mention:
    print('WARN files mentioned in text but missing on disk:')
    for _h in _mention: print('  -', _h)
if _missing:
    print('WARN broken local links:')
    for _h in _missing: print('  -', _h)
else:
    print('link check: all local hrefs exist')

# bidi guards, applied once to the finished document and never inside an <svg> (bdi is not valid there)
_SVG = re.compile(r'(<svg\b.*?</svg>|<style\b.*?</style>|<script\b.*?</script>|<pre\b.*?</pre>)', re.S)
_svg_parts = _SVG.split(out)
for _i in range(0, len(_svg_parts), 2):
    _svg_parts[_i] = _bidi_fix(_svg_parts[_i])
out = ''.join(_svg_parts)

open('רחל_צדוק_המחקר_המלא.html', 'w', encoding='utf-8').write(out)
# index.html = tiny redirect stub to the Hebrew-named document (S3 entry point)
open('index.html', 'w', encoding='utf-8').write(INDEX_STUB)
print('unified written,', len(out)//1024, 'KB')


# ---------- build static site (S3-ready) ----------
import shutil, pathlib, urllib.parse
SITE = 'site'
if os.path.exists(SITE): shutil.rmtree(SITE)
os.makedirs(SITE)
shutil.copy('index.html', os.path.join(SITE, 'index.html'))
shutil.copy('רחל_צדוק_המחקר_המלא.html', os.path.join(SITE, 'רחל_צדוק_המחקר_המלא.html'))
shutil.copytree('docs', os.path.join(SITE, 'docs'))
# root files referenced by relative links
for f in ['תמליל_העדות_המלא.txt', 'ניתוח_העדות.md', 'אינדקס_מקורות.md', 'רחל_צדוק_מחקר_מקיף.md', 'עץ_משפחה_גרפי.html', 'עץ_משפחה_מורחב.html']:
    if os.path.exists(f): shutil.copy(f, SITE)
# drop the huge unreferenced wav/chunks if copied inside docs (they are not in docs) — nothing to do
site_html = open(os.path.join(SITE,'רחל_צדוק_המחקר_המלא.html'), encoding='utf-8').read()
_rel = set(_rechk.findall(r'(?:href|src)="(?!https?:|#|data:|mailto:)([^"]+)"', site_html))
_bad = []
for h in sorted(_rel):
    hp = urllib.parse.unquote(h)
    if not os.path.exists(os.path.join(SITE, hp)):
        _bad.append(h)
if _bad:
    print('WARN site missing targets:')
    for h in _bad: print('  -', h)
else:
    print('site check: all', len(_rel), 'relative link targets exist under site/')
