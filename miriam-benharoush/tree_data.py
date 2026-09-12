"""miriam-benharoush — the family-tree data; run `python3 tree_data.py` to regenerate the SVG in tree.html."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from treegen import Node, Tree, replace_svg

N = Node
nodes = [
    # row 0 — the grandparents (family testimony; Habib and Tzipora also in the 1956 list)
    N('habib',   1, 0, 'חביב דהן',          ['~1880 · עלה 1956', 'רשימת "ירושלים"']),
    N('miriamd', 2, 0, 'מרים דהן',          ['אמו של שלום', 'לא עלתה (משפחה)'], dashed=True),
    N('tzipora', 0, 0, 'צפורה דהן',         ['~1880 · דודתו של שלום', 'עלתה 1956, נרשמה "אם"']),
    N('yitzhak', 5, 0, 'יצחק אבוטבול',      ['אביה של יקוט', 'לא עלה (משפחה)'], dashed=True),
    N('rivkaab', 6, 0, 'רבקה אבוטבול',      ['אמה של יקוט', 'לא עלתה (משפחה)'], dashed=True),
    # row 1 — the three brothers and their wives
    N('makhlouf',0, 1, 'מכלוף דהן',         ['1903 · אחיו של שלום', 'קריית שמונה 1956']),
    N('simha',   1, 1, 'סמחה דהן',          ['1912 · אשתו של מכלוף', 'רשימת 1956']),
    N('shalom',  3, 1, 'שלום דהן',          ['1920 · חייט, מכנאס', 'ק. שמונה, ירושלים · נפ׳ 1979?']),
    N('yakut',   4, 1, 'יקוט דהן לבית אבוטבול', ['1921 · ירושלים', 'נפ׳ 3.3.1976']),
    N('shlomon', 6, 1, 'שלומון דהן',        ['1922 · אחיו של שלום', 'עלה עם אביו חביב, 1956']),
    # row 2 — Makhlouf's children (right) and Shalom's daughters (left) + Miriam's husband
    N('haim',    0, 2, 'חיים',              ['1926 · בן מכלוף']),
    N('miriamm', 1, 2, 'מרים',              ['1938 · בת מכלוף']),
    N('rachelm', 2, 2, 'רחל',               ['1941 · רמת הדסה', 'בת מכלוף — ככל הנראה']),
    N('lorem',   3, 2, 'לורם(?)',           ['1942 · רמת הדסה', 'בן/בת מכלוף — ככל הנראה']),
    N('masoudi', 4, 2, 'מסעודי',            ['1944 · רמת הדסה', 'בן מכלוף — ככל הנראה']),
    N('geula',   5, 2, 'גאולה',             ['1951 · בת מכלוף']),
    N('miriam',  6, 2, 'מרים (מרי) בן הרוש', ['לבית דהן · 1939 · מכנאס', 'עלתה 15.1.1956 · חולון'], focus=True),
    N('rivka',   7, 2, 'רבקה דהן',          ['1944 · פנקס אליאנס 1950']),
    N('rachel',  8, 2, 'רחל דהן',           ['1947 · פנקס אליאנס 1953']),
    # row 3 — Miriam's husband
    N('mordechai', 6, 3, 'מרדכי בן הרוש',   ['בעלה · 1931–2010 · נישאו ת"א 9.1960', 'בן יונה ויקוט (פנינה) · דף נלווה']),
]
tree = Tree(
    nodes=nodes,
    couples=[('habib', 'miriamd'), ('makhlouf', 'simha'), ('shalom', 'yakut'), ('yitzhak', 'rivkaab')],
    families=[
        (['habib', 'miriamd'], ['makhlouf', 'shalom', 'shlomon'], 0),
        (['yitzhak', 'rivkaab'], ['yakut'], 8),
        (['makhlouf', 'simha'], ['haim', 'miriamm', 'rachelm', 'lorem', 'masoudi', 'geula'], 0),
        (['shalom', 'yakut'], ['miriam', 'rivka', 'rachel'], 8),
    ],
    links=[('tzipora', 'shalom'), ('miriam', 'mordechai')],
    ink='#1e2a32', muted='#5e6b73', line='#c5ccc7', accent='#1f6f5b', marr='#9aa5a0',
    title='עץ המשפחה — חביב ומרים דהן, יצחק ורבקה אבוטבול; שלום ויקוט דהן ובנותיהם מרים, רבקה ורחל; אחיו של שלום מכלוף ושלומון ומשפחותיהם; בעלה של מרים מרדכי בן הרוש',
)
if __name__ == '__main__':
    replace_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tree.html'), tree.render())
    print('tree.html updated')
