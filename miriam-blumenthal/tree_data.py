"""miriam-blumenthal — the family-tree data; run `python3 tree_data.py` to regenerate the SVG in tree.html."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from treegen import Node, Tree, replace_svg

N = Node
nodes = [
    N('moshe_l',  4,   0, 'משה הלוי ליבוביץ', ['1890 – 1944, אושוויץ', 'סנדלר, באלאשאג\'רמאט']),
    N('frimet',   5,   0, 'פרימט (פני)',      ['לבית וג · 1890 – 1944', 'אושוויץ']),
    N('david_l',  0,   1, 'דוד, מרטון',       ['שרדו · מרטון ("מנו") 1921', 'דוד — כפר סבא, 1957']),
    N('shim_l',   1,   1, 'שמשון, שאנדור, לילה', ['1914 · כ-1924 · 1927/1930', 'נספו ב-1944 — דפי אסתר ודוד']),
    N('esther',   2,   1, 'אסתר (פרנקל)',     ['כ-1916 · "הגנה", 1946', 'נישאה 26.10.1948']),
    N('sibs',     3,   1, 'אברהם אהרן? נחמה?', ['אברהם אהרן — ככל הנראה', 'נחמה — ככל הנראה "מגדה"'], dashed=True),
    N('miriam',   4,   1, 'מרים (מגדה?)',     ['1925?, הונגריה – 2003?', 'אולי מגדה — אושוויץ, 1944']),
    N('yaakov',   5,   1, 'יעקב בלומנטל',      ['כ-1918 · חייל, 1948', 'בן משה בן ציון וחוה']),
    N('meir',     3,   2, 'מאיר',             ['11.4.1952 – 21.11.1974', 'חיל האוויר · הפועל פ"ת']),
    N('shimshon', 4,   2, 'שמשון אחימאיר',     ['26.1.1954', 'נשוי לאילנה קוטנר']),
    N('moshe',    5,   2, 'משה',              ['כרטיס ההתאמה'], dashed=True),
    N('nava',     6,   2, 'נאוה',             ['כרטיס ההתאמה'], dashed=True),
    N('ilana',    4,   3, 'אילנה (קוטנר)',     ['21.10.1957, צאלים', 'טל · איל · שירי'], dashed=True),
]
tree = Tree(
    nodes=nodes,
    couples=[('moshe_l', 'frimet'), ('miriam', 'yaakov')],
    families=[
        (['moshe_l', 'frimet'], ['david_l', 'shim_l', 'esther', 'sibs', 'miriam'], 0),
        (['miriam', 'yaakov'], ['meir', 'shimshon', 'moshe', 'nava'], 0),
    ],
    links=[('shimshon', 'ilana')],
    ink='#2a241c', muted='#695f50', line='#d8cfbd', accent='#7a5a24', marr='#b3a27f',
    title='עץ המשפחה — משה הלוי ופרימט (פני) ליבוביץ וילדיהם: דוד, מרטון ("מנו"), שמשון, שאנדור, לילה, אסתר, ומרים — אולי מגדה — ואולי אברהם אהרן ונחמה; מרים ויעקב בלומנטל וילדיהם מאיר, שמשון, משה ונאוה; אשת שמשון, אילנה',
)
if __name__ == '__main__':
    replace_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tree.html'), tree.render())
    print('tree.html updated')
