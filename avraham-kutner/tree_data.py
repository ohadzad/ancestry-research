"""avraham-kutner — the family-tree data; run `python3 tree_data.py` to regenerate the SVG in tree.html."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from treegen import Node, Tree, replace_svg

N = Node
nodes = [
    N('tzvi',     0, 0, 'צבי (הרש) קוטנר', ['אביו של ישראל', 'דף העד של נכדתם שרה']),
    N('chaya',    1, 0, 'חיה',             ['אמו של ישראל', 'דף העד של נכדתם שרה']),
    N('abrahamb', 2, 0, 'אברהם בנדוס',     ['אביה של צביה', 'דף העד של נכדתם שרה']),
    N('sarahb',   3, 0, 'שרה',             ['אמה של צביה', 'דף העד של נכדתם שרה']),
    N('israel',   0.5, 1, 'ישראל קוטנר',   ['1892 / 1897, סטריקוב · סוחר תבואה', 'אוזורקוב · גטו לודז\' · נספה']),
    N('tzviya',   2.5, 1, 'צביה לבית בנדוס', ['1891 / 1895, אוזורקוב', 'גטו לודז\' · נספתה']),
    N('jakob',    3.5, 1, 'יעקב בנדוס',     ['1890 / 1893, אוזורקוב · סוחר', 'אחיה של צביה · מת בגטו לודז\' (ככל הנראה)']),
    N('sara',     0, 2, 'שרה (Sala) מלוטק', ['14.8.1922 · אושוויץ, בוכנוולד', 'שרדה · קריית אונו']),
    N('avraham',  1.5, 2, 'אברהם קוטנר',   ['15.8.1928 (1927 בגטו, 1930 בישראל) – 19.3.1986', 'אוזורקוב · מאוטהאוזן · צאלים'], focus=True),
    N('feiga',    3, 2, 'פייגה',           ['בת 9 · נלקחה מגטו לודז\'', 'למקום בלתי ידוע']),
    N('mlotek',   0, 3, 'מרדכי מלוטק',     ['בעלה של שרה · 1919 – 2010', 'לפי העץ המשפחתי'], dashed=True),
    N('tzipora',  1.5, 3, 'צפורה לבית בלם', ['1932, לובומל – 2006', 'אשתו · מחקר נפרד']),
]
tree = Tree(
    nodes=nodes,
    couples=[('tzvi', 'chaya'), ('abrahamb', 'sarahb'), ('israel', 'tzviya')],
    families=[
        (['tzvi', 'chaya'], ['israel'], 0),
        (['abrahamb', 'sarahb'], ['tzviya', 'jakob'], 0),
        (['israel', 'tzviya'], ['sara', 'avraham', 'feiga'], 0),
    ],
    links=[('sara', 'mlotek'), ('avraham', 'tzipora')],
    ink='#22262b', muted='#5f6670', line='#c9ccd1', accent='#3d5a80', marr='#9aa1ab',
    title='עץ המשפחה — צבי (הרש) וחיה קוטנר, אברהם ושרה בנדוס; ישראל קוטנר וצביה לבית בנדוס, אוזורקוב, ואחיה יעקב בנדוס; ושלושת ילדיהם — שרה (מלוטק), אברהם ופייגה; בעלה של שרה מרדכי מלוטק; אשתו של אברהם צפורה לבית בלם',
)
if __name__ == '__main__':
    replace_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tree.html'), tree.render())
    print('tree.html updated')
