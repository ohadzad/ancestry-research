"""yaakov-blumenthal — the family-tree data; run `python3 tree_data.py` to regenerate the SVG in tree.html."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from treegen import Node, Tree, replace_svg

N = Node
nodes = [
    N('mor',      1.5, 0, 'מאיר (Mór) בלומנטל', ['נוגראדברצל', 'דפי העד']),
    N('rivkaw',   2.5, 0, 'רבקה בלומנטל',      ['(רגינה) לבית ווזנר', 'דפי העד']),
    N('benzion',  2,   1, 'משה בן ציון ("בנו")', ['1888/1892 – 1944 · נוגראדברצל', 'מורה / בעל אחוזה']),
    N('chava',    3,   1, 'חוה (אידה)',          ['לבית דויטש · בורגנלנד', 'אושוויץ, 1944']),
    N('yitzhak',  0,   2, 'יצחק',               ['1915 · פתח תקווה', 'דפי עד, 1956']),
    N('michael',  1,   2, 'מיכאל',              ['פתח תקווה', 'דפי עד, 1995']),
    N('yehuda',   2,   2, 'יהודה',              ['דפי עד']),
    N('rivka',    3,   2, 'רבקה גומבו',          ['פתח תקווה', 'דף עד, 1957?']),
    N('others',   4,   2, 'מאיר, ייטל לאה, פירושקה',  ['ועוד — "10" בדפי העד', 'מן העץ של "מ. בלומנטל"'], dashed=True),
    N('yaakov',   5,   2, 'יעקב',               ['כ-1918 · הונגריה · חייל, 1948', 'ילדיו — אחימאיר'], focus=True, dashed=True),
    N('miriam',   6,   2, 'מרים ליבוביץ',        ['1925 · הונגריה', 'בת משה הלוי ופרימט']),
    N('meir',     4,   3, 'מאיר',               ['11.4.1952 – 21.11.1974', 'חיל האוויר · הפועל פ"ת']),
    N('shimshon', 5,   3, 'שמשון אחימאיר',       ['26.1.1954', 'נשוי לאילנה קוטנר']),
    N('moshe',    6,   3, 'משה',                ['כרטיס ההתאמה'], dashed=True),
    N('nava',     7,   3, 'נאוה',               ['כרטיס ההתאמה'], dashed=True),
    N('ilana',    5,   4, 'אילנה (קוטנר)',       ['21.10.1957, צאלים', 'טל · איל · שירי'], dashed=True),
]
tree = Tree(
    nodes=nodes,
    couples=[('mor', 'rivkaw'), ('benzion', 'chava'), ('yaakov', 'miriam')],
    families=[
        (['mor', 'rivkaw'], ['benzion'], 0),
        (['benzion', 'chava'], ['yitzhak', 'michael', 'yehuda', 'rivka', 'others', 'yaakov'], 0),
        (['yaakov', 'miriam'], ['meir', 'shimshon', 'moshe', 'nava'], 0),
    ],
    links=[('shimshon', 'ilana')],
    ink='#1f2725', muted='#56635f', line='#c9d3cf', accent='#2e6a5f', marr='#8fa39c',
    title='עץ המשפחה — מאיר ורבקה בלומנטל; משה בן ציון וחוה (אידה) בלומנטל מנוגראדברצל וילדיהם יצחק, מיכאל, יהודה ורבקה גומבו, ויעקב — ככל הנראה; יעקב ומרים לבית ליבוביץ וילדיהם מאיר, שמשון, משה ונאוה; אשת שמשון, אילנה',
)
if __name__ == '__main__':
    replace_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tree.html'), tree.render())
    print('tree.html updated')
