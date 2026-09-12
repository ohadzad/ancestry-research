"""miriam-benharoush — the family-tree data; run `python3 tree_data.py` to regenerate the SVG in tree.html."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from treegen import Node, Tree, replace_svg

N = Node
nodes = [
    # row 0 — the grandparents (family testimony; Habib and Tzipora also in the 1956 list)
    N('habib',   3, 0, 'חביב דהן',          ['~1880 · עלה 1956', 'נקבר בירושלים (משפחה)']),
    N('miriamd', 4, 0, 'מרים דהן',          ['אמו של שלום', 'לא עלתה (משפחה)'], dashed=True),
    N('tzipora', 2, 0, 'צפורה דהן',         ['~1880 · דודתו של שלום', 'עלתה 1956, נרשמה "אם"']),
    N('yitzhak', 7, 0, 'יצחק אבוטבול',      ['אביה של יקוט', 'לא עלה (משפחה)'], dashed=True),
    N('rivkaab', 8, 0, 'רבקה אבוטבול',      ['אמה של יקוט', 'לא עלתה (משפחה)'], dashed=True),
    # row 1 — the three brothers and their wives
    N('makhlouf',0, 1, 'מכלוף דהן',         ['1903 · אחיו של שלום', 'ק. שמונה 1956 · חיפה']),
    N('simha',   1, 1, 'סמחה דהן',          ['1912 · אשתו של מכלוף', 'רשימת 1956']),
    N('shalom',  6, 1, 'שלום דהן',          ['1920 · חייט, מכנאס', 'ירושלים · נפ׳ 1979 · הר המנוחות']),
    N('yakut',   7, 1, 'יקוט דהן לבית אבוטבול', ['1921 · ירושלים', 'נפ׳ 3.3.1976 · הר המנוחות']),
    N('shlomon', 2, 1, 'שלומון דהן',        ['1922 · אחיו של שלום · לא נישא', 'עלה עם אביו חביב, 1956']),
    N('hanaab',  8, 1, 'חנה אבוטבול',       ['אחות יקוט · נישאה לעזוז', 'עלתה ~1948/49 (משפחה)'], dashed=True),
    N('jamila',  9, 1, 'ג\'מילה אבוטבול',    ['אחות יקוט', 'לפי המשפחה'], dashed=True),
    N('michab', 10, 1, 'מיכאל מכלוף אבוטבול', ['אח יקוט · עלה ~1948/49', 'שינוי שם צפת 1972? — טעון אימות'], dashed=True),
    # row 2 — Makhlouf's children (right) and Shalom's daughters (left) + Miriam's husband
    N('haim',    0, 2, 'חיים דהן',          ['1926 · בן מכלוף', 'רשימת 1956']),
    N('miriamm', 1, 2, 'מרים דהן',          ['1938 · בת מכלוף', 'רשימת 1956']),
    N('rachelm', 2, 2, 'רחל דהן',           ['1941 · רמת הדסה · אליאנס 1949', 'בת מכלוף — אישור המשפחה']),
    N('laurette',   3, 2, 'לורט(?) דהן',       ['1942 · רמת הדסה', 'בת מכלוף — אישור המשפחה']),
    N('masoudi', 4, 2, 'מסעודי דהן',        ['1944 · רמת הדסה', 'בת מכלוף — אישור המשפחה']),
    N('geula',   5, 2, 'גאולה דהן',         ['1951 · בת מכלוף', 'רשימת 1956']),
    N('miriam',  6, 2, 'מרים (מרי) בן הרוש', ['לבית דהן · 1939 · מכנאס', 'עלתה 15.1.1956 · חולון'], focus=True),
    N('rivka',   7, 2, 'רבקה דהן',          ['1944 · פנקס אליאנס 1950']),
    N('rachel',  8, 2, 'רחל דהן',           ['1947 · פנקס אליאנס 1953']),
    # row 3 — Miriam's husband
    N('mordechai', 6, 3, 'מרדכי בן הרוש',   ['בעלה · 1931–2010 · נישאו ת"א, ספטמבר 1960', 'בן יונה ויקוט (פנינה) · דף נלווה']),
]
tree = Tree(
    nodes=nodes,
    couples=[('habib', 'miriamd'), ('makhlouf', 'simha'), ('shalom', 'yakut'), ('yitzhak', 'rivkaab')],
    families=[
        (['habib', 'miriamd'], ['makhlouf', 'shalom', 'shlomon'], 0),
        (['yitzhak', 'rivkaab'], ['yakut', 'hanaab', 'jamila', 'michab'], -8),
        (['makhlouf', 'simha'], ['haim', 'miriamm', 'rachelm', 'laurette', 'masoudi', 'geula'], 0),
        (['shalom', 'yakut'], ['miriam', 'rivka', 'rachel'], 0),
    ],
    links=[('tzipora', 'shalom'), ('miriam', 'mordechai')],
    ink='#1e2a32', muted='#5e6b73', line='#c5ccc7', accent='#1f6f5b', marr='#9aa5a0',
    title='עץ המשפחה — חביב ומרים דהן, יצחק ורבקה אבוטבול וילדיהם יקוט, חנה, ג\'מילה ומיכאל מכלוף; שלום ויקוט דהן ובנותיהם מרים, רבקה ורחל; אחיו של שלום מכלוף על משפחתו ושלומון; בעלה של מרים מרדכי בן הרוש',
)
if __name__ == '__main__':
    replace_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tree.html'), tree.render())
    print('tree.html updated')
