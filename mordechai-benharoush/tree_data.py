"""mordechai-benharoush — the family-tree data; run `python3 tree_data.py` to regenerate the SVG in tree.html."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from treegen import Node, Tree, replace_svg

N = Node
nodes = [
    N('mordechai0', 3, 0, 'מרדכי בן הרוש', ['אביו של יונה', 'רשימת 1956 (עמודת אב/אם)'], dashed=True),
    N('miriam0',    4, 0, 'מרים בן הרוש',  ['אמו של יונה', 'רשימת 1956 (עמודת אב/אם)'], dashed=True),
    N('davidoh',    5, 0, 'דוד אוחיון',    ['אביה של יקוט', 'כתב העדות, מכנאס 1949'], dashed=True),
    N('yona',       3, 1, 'יונה בן הרוש',  ['1898 (משפחה) / 1912/1918 (רשימה)', 'הורים סוחרים, מכנאס · צפת, ת"א · הר המנוחות']),
    N('yakut',      4, 1, 'יקוט (פנינה) לבית אוחיון', ['1918 · "ארצה" 1956 → צפת', '"פנינה" — משפחה · ת"א · הר המנוחות']),
    N('nissim',     0, 2, 'ניסים (מקסים)', ['הבכור · נשאר במרוקו', 'ילדיו בצרפת · לפי המשפחה'], dashed=True),
    N('miriam1',    1, 2, 'מרים',          ['פריז · נקברה בהר המנוחות', 'לפי המשפחה'], dashed=True),
    N('rouash',     0, 3, 'שמואל רואש',    ['בעלה של מרים · פריז', 'נקבר בקריות · לפי המשפחה'], dashed=True),
    N('mordechai',  2, 2, 'מרדכי בן הרוש', ['1927/28 (מסמכים) / 1931 (משפחה) – 2010', 'מכנאס · "מרדושי" · עזב רווק ולבדו'], focus=True),
    N('yaakov',     3, 2, 'יעקב',          ['1933 · "ארצה" 1956 → צפת']),
    N('gabriel',    4, 2, 'גבריאל (גבי)',   ['1942 · "ארצה" 1956']),
    N('juliette',   5, 2, 'ז\'וליט',        ['1943 · "ארצה" 1956']),
    N('salomon',    6, 2, 'סלומון',        ['1945 · "ארצה" 1956']),
    N('esther',     7, 2, 'אסתר',          ['1948 · "ארצה" 1956', 'פנקס אליאנס מכנאס 1953']),
    N('michael',    8, 2, 'מיכאל מכלוף',    ['צעיר ממרדכי · מקומו בסדר לא ידוע', 'עלה בנפרד, מועד לא ידוע · משפחה'], dashed=True),
    N('hana',       1, 3, 'חנה (אנה?)',     ['אשתו הראשונה', 'לפי המשפחה'], dashed=True),
    N('miriamd',    2, 3, 'מרים לבית דהן',  ['אשתו · 1939, מכנאס', 'נישאו ת"א 9.1960 · מחקר נפרד']),
    N('mari',       3, 3, 'מרי',           ['1936 · אשתו של יעקב', '"ארצה" 1956']),
    N('yoni',       1, 4, 'יוני',           ['בנו של מרדכי וחנה', 'לפי המשפחה'], dashed=True),
]
tree = Tree(
    nodes=nodes,
    couples=[('mordechai0', 'miriam0'), ('yona', 'yakut')],
    families=[
        (['mordechai0', 'miriam0'], ['yona'], 0),
        (['davidoh'], ['yakut'], -8),
        (['yona', 'yakut'], ['nissim', 'miriam1', 'mordechai', 'yaakov', 'gabriel', 'juliette', 'salomon', 'esther', 'michael'], 0),
        (['hana'], ['yoni'], 0),
    ],
    links=[('mordechai', 'miriamd'), ('mordechai', 'hana'), ('yaakov', 'mari'), ('miriam1', 'rouash')],
    ink='#2a2320', muted='#6b5f57', line='#cbc1b6', accent='#8a4a2a', marr='#a89a8e',
    title='עץ המשפחה — מרדכי ומרים בן הרוש, דוד אוחיון; יונה ויקוט (פנינה) בן הרוש לבית אוחיון ותשעת ילדיהם — ניסים (מקסים), מרים, מרדכי, יעקב, גבריאל, ז\'וליט, סלומון, אסתר ומיכאל מכלוף; נשותיו של מרדכי חנה ומרים לבית דהן, ובנו יוני; אשתו של יעקב מרי; בעלה של מרים שמואל רואש',
)
if __name__ == '__main__':
    replace_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tree.html'), tree.render())
    print('tree.html updated')
