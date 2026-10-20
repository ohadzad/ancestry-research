"""tzipora-kutner — the family-tree data; run `python3 tree_data.py` to regenerate the SVG in tree.html."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from treegen import Node, Tree, replace_svg

N = Node
nodes = [
    N('zecharia', 1.5, 0, 'זכריה בלם',      ['כ-60 · חייט, דוביינקה', 'נרצח בדוביינקה']),
    N('chayab',   2.5, 0, 'חיה בלם',        ['כ-55 · דוביינקה', 'נרצחה']),
    N('yaakov',   3.5, 0, 'יעקב פרימר',     ['כ-65 · סוחר, לובומל', 'נרצח']),
    N('chayap',   4.5, 0, 'חיה פרימר',      ['כ-65 · לובומל', 'נרצחה']),
    N('mendel',   2.5, 1, 'מנדל בלם',       ['יליד דוביינקה · חנווני, לובומל', 'שרד את מאצ\'יוב · נספה']),
    N('zelda',    3.5, 1, 'זלדה (סוניה)',   ['לבית פרימר · לובומל', 'נרצחה במאצ\'יוב · 1942?']),
    N('frida',    5.5, 1, 'פרידה שלוקר',    ['לבית פרימר · כ-1913 – 1943', 'אם לארבעה · לובומל']),
    N('moshe',    0, 2, 'משה',              ['כ-1928 · בן 14', 'נרצח · 1942?']),
    N('tzipora',  1, 2, 'צפורה',            ['1932 – 2006', 'מסתור · סלווינו · צאלים'], focus=True),
    N('raizel',   2, 2, 'רייזל',            ['כ-1935 · בת 7', "נרצחה · מאצ'יוב"]),
    N('shmuel',   3, 2, 'שמואל',            ['כ-1937 · כבן 5', "נרצח · מאצ'יוב"]),
    N('asher',    4, 2, 'אשר',              ['כ-1938 · בן 4', "נרצח · מאצ'יוב"]),
    N('israel',   5, 2, 'ישראל',            ['כ-1939 · בן 3½', "נרצח · מאצ'יוב"]),
    N('chaim',    6, 2, 'חיים',             ['כ-1941 · בן שנה', "נרצח · מאצ'יוב"]),
    N('avraham',  1, 3, 'אברהם קוטנר',      ['15.8.1928 – 19.3.1986', 'בעלה · מחקר נפרד']),
]
tree = Tree(
    nodes=nodes,
    couples=[('zecharia', 'chayab'), ('yaakov', 'chayap'), ('mendel', 'zelda')],
    families=[
        (['zecharia', 'chayab'], ['mendel'], 0),
        (['yaakov', 'chayap'], ['zelda', 'frida'], 0),
        (['mendel', 'zelda'], ['moshe', 'tzipora', 'raizel', 'shmuel', 'asher', 'israel', 'chaim'], 0),
    ],
    links=[('tzipora', 'avraham')],
    ink='#24222b', muted='#625e6e', line='#cfccd8', accent='#5a4e7c', marr='#a29cb3',
    title='עץ המשפחה — זכריה וחיה בלם מדוביינקה, יעקב וחיה פרימר מלובומל; מנדל בלם וזלדה (סוניה) לבית פרימר ושבעת ילדיהם — משה, צפורה, רייזל, שמואל, אשר, ישראל וחיים; פרידה שלוקר לבית פרימר; בעלה של צפורה אברהם קוטנר',
)
if __name__ == '__main__':
    replace_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tree.html'), tree.render())
    print('tree.html updated')
