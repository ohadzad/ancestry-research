"""mordechai-benharoush — the family-tree data; run `python3 tree_data.py` to regenerate the SVG in tree.html."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from treegen import Node, Tree, replace_svg

N = Node
nodes = [
    N('mordechai0', 2, 0, 'מרדכי בן הרוש', ['אביו של יונה', 'רשימת 1956 (עמודת אב/אם)'], dashed=True),
    N('miriam0',    3, 0, 'מרים בן הרוש',  ['אמו של יונה', 'רשימת 1956 (עמודת אב/אם)'], dashed=True),
    N('yona',       2, 1, 'יונה בן הרוש',  ['1912? · סוחר, מכנאס', '"ארצה" 1956 → צפת']),
    N('yakut',      3, 1, 'יקוט (פנינה) בן הרוש', ['1918 · "ארצה" 1956 → צפת', '"פנינה" בפי המשפחה']),
    N('mordechai',  0, 2, 'מרדכי בן הרוש', ['1931–2010 · מכנאס', 'עלה לבדו 1947/48, בן 16–17'], focus=True),
    N('yaakov',     1, 2, 'יעקב',          ['1933 · "ארצה" 1956 → צפת']),
    N('gabriel',    3, 2, 'גבריאל (גבי)',   ['1942 · "ארצה" 1956']),
    N('juliette',   4, 2, 'ז\'וליט',        ['1943 · "ארצה" 1956']),
    N('salomon',    5, 2, 'סלומון',        ['1945 · "ארצה" 1956']),
    N('esther',     6, 2, 'אסתר',          ['1948 · "ארצה" 1956', 'פנקס אליאנס מכנאס 1953']),
    N('miriamd',    0, 3, 'מרים לבית דהן',  ['אשתו · 1939, מכנאס', 'עלתה 1956 · מחקר נפרד']),
    N('mari',       1, 3, 'מרי',           ['1936 · אשתו של יעקב', '"ארצה" 1956']),
]
tree = Tree(
    nodes=nodes,
    couples=[('mordechai0', 'miriam0'), ('yona', 'yakut')],
    families=[
        (['mordechai0', 'miriam0'], ['yona'], 0),
        (['yona', 'yakut'], ['mordechai', 'yaakov', 'gabriel', 'juliette', 'salomon', 'esther'], 0),
    ],
    links=[('mordechai', 'miriamd'), ('yaakov', 'mari')],
    ink='#2a2320', muted='#6b5f57', line='#cbc1b6', accent='#8a4a2a', marr='#a89a8e',
    title='עץ המשפחה — מרדכי ומרים בן הרוש; יונה ויקוט (פנינה) בן הרוש וילדיהם מרדכי, יעקב, גבריאל, ז\'וליט, סלומון ואסתר; אשתו של מרדכי מרים לבית דהן; אשתו של יעקב מרי',
)
if __name__ == '__main__':
    replace_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tree.html'), tree.render())
    print('tree.html updated')
