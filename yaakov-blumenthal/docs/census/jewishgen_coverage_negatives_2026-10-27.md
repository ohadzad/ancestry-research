# כיסוי, שליליים וחסמים — מפקדי הונגריה ורישומי נוגראדברצל / פראואנקירכן / באלאשאג'רמאט — 27.10.2026

סריקה של מפקדים ורישומים אזרחיים/קהילתיים לשתי המשפחות: **בלומנטל מנוגראדברצל** (עם דויטש מפראואנקירכן) ו**ליבוביץ מבאלאשאג'רמאט**. כל החיפושים: JewishGen ("Hungary Database" + מאגרי Burgenland ו-"Slovak Civil"), בחשבון מחובר, 26–27.10.2026. ממצאים חיוביים — בקבצים הנפרדים; כאן — **מה כוסה ומה לא**.

## 0. בדיקות תקינות (canary) וחסמים

| כלי | תוצאה |
|---|---|
| `jewishgen_status` | "Session cookie (jgcure) present" — אך דפי הרשומות של ה-MCP (`jgdetail_2.php?df=…`) מחזירים **"0 matching record found"** גם כשסקירת ההתאמות הראשית מדווחת 170 (למשל Hungarian Births, Deutsch + Frauenkirchen). **אין לקרוא זאת "אפס"** — נתיב ה-MCP לדפי הרשומות שבור (עיצוב האתר החדש מעביר את ההקשר ב-sessionStorage וקורא `https://www.jewishgen.org/databases/recordlistjson.php`). עקפתי באמצעות הדפדפן (כרום, חשבון מחובר — לשונית חדשה; לשוניות המשתמש לא נגעו) וקריאה ישירה של נקודת ה-JSON. כל מספר "total=" להלן נקרא מהאתר עצמו. |
| `hungaricana_status` | ok (canary Ökörmező = 22) — אבל זה פורטל **ארכיוני** (archives.hungaricana.hu) — **אין בו מאגר מפקדים**; 14 מאגרים: Árvaszéki, Büntető, Fogoly, Hagyatéki, Jegyzőkönyvek, Közjegyzői, Lakásív 1944 (בודפשט), Lakcímjegyzék (בודפשט), Polgári per, Telekkönyv, Topográfia (בודפשט), Végrendelet וכו'. |
| `radix_status` | ok. נוגראדברצל ב-RadixIndex: **22 שמות משפחה בלבד** (Blumenthal ×1, Deutsch ×1 — עקבות). |
| `fs_status` | **`access_token: missing`** — **חסם**: אין FamilySearch. נבדק גם בדפדפן — דף הבית מציג "Sign in" (לא מחובר; לא ניסיתי התחברות). כל סרטי FamilySearch שצוינו להלן (700859, 701094, 4838205/211/569, Hungary Civil Registration 1895–1980) **לא נפתחו**. |
| `ia_status` / אחרים | לא נדרשו. |
| ספריית Hungaricana (library.hungaricana.hu) | נגישה דרך הדפדפן (WebFetch → 403). OCR של כל עמוד זמין; **תמונות/PDF — reCAPTCHA** (לא עקפתי). |

## 1. מפקדים

| מפקד | מאגר / מקור | כיסוי שנמצא | נוגראדברצל | פראואנקירכן |
|---|---|---|---|---|
| **1770–1850 ("Other Hungarian Census Records", מס הסובלנות, רשימות Conscriptio Judaeorum)** | JewishGen `ccd996b4-…` — 123,763 רשומות; הערה בדף המאגר: המחוזות הראשוניים כוללים **Moson ו-Nógrád** | נוגראד: 3,527 שורות (any-field "Nograd"), מושון: 6,872 | **54 שורות** (Bercel): 1771 [Bertzel and Becske], 1774, 1775, 1781, 1794, 1795 — ראשי משקי בית; **אין BLUMENTHAL / WOSNER / DEUTSCH** — מפורט בקובץ הנוגראדברצל §3. Blumenthal בנוגראד: Szügy 1818/9 (Jakob), "—" 1821 (Samuel) — לא ברצל | **62 שורות Deutsch** ב-1792, 1801, 1808, 1817, 1821, 1830/1, 1835, 1838, 1839, 1842, 1844, 1846 — כולל **"DEUTS, Nathan — wife" (1846, 0027342)** |
| **1828 (Vagyonösszeírás / Conscriptio regnicolaris)** | JewishGen `CENSUS1828G` | Nógrád ✓ (סרט LDS 623062), Moson ✓ (623058–623059; 331 שורות "Moson"), Szabolcs ✓ | **Berczel (Nógrád): 22 שורות, מהן 4 BLUMENTAL/BLUMETHAL (Moises, Philippus, Sany, Gaspar)** — **ממצא חיובי** | **Boldog-Asszony: 103 שורות; 6 DEUTSCH** (Ignatius 280, Jacobus 271, Kalmann 311, Mayer 307, Sarlotte 310, Judas 312) |
| **1848 (Conscriptio Judaeorum)** | JewishGen `C1848N` — 115,836 רשומות (לפי דף המאגר) | **מחוזות שבמאגר:** Moson (Boldogaszony 656+ [נסרקו 1,450 מתוך 2,222 שורות "Moson" any-field], Kopcseny 444, Gata 215, Moson 138, Oroszvár 119), Szabolcs, Zemplén, Komárom, Borsod, Heves, Pozsony ועוד. **Nógrád: אין תושבי נוגראד** — "Nograd" מופיע רק כמחוז לידה של תושבי Komlód/Tata/Gyöngyös/Miskolc וכו' (49 שורות, 18 ישובים) | **אין.** שורות "Bercel" — 181, **כולן Szabolcs (Tiszabercel)**. מפקד 1848 של ברצל (112 יהודים) קיים — **NML IV. 7. c, Öi. 986** — לא ממוחשב במאגרים שנבדקו (הספר "Senkiföldjén" נשען עליו) | **ממצא חיובי: Household 38 — Deutsch Nathan (36), Rosalia (30), Juliana (2), Fany (60, אם), Pebi (25, אחות)** — ראו קובץ פראואנקירכן §3 |
| **1857** | JewishGen `2e516a17-…` (18,450 רשומות) | רק Abaúj-Torna (9,472), Kassa (1,321), Zemplén (463, חלקי), Sáros (99, חלקי). לפי דף המאגר ב-FamilySearch יש סרטים שלא נוספו לאינדקס: **Nógrád (54 כפרים — [בחלקם בסלובקיה]; לא ידוע אם ברצל בהם), Sopron (16 כפרים בהונגריה + 51 באוסטריה), Magyaróvár (העיר)**; פראואנקירכן (מחוז Moson) אינה ברשימה | **אין במאגר** | **אין במאגר** |
| **1869** | JewishGen `CENSUS1869K` (89,498) | Abaúj-Torna (Torna), Bars, Esztergom, Fejér (Székesfehérvár בלבד), Győr (העיר בלבד), Hajdú (Debrecen), Komárom, Nyitra, Sáros, Szentes (Csongrád בלבד), Szepes, Zemplén. **Nógrád ו-Moson אינם**; גם רשימת הסרטים של FHL שבדף המאגר אינה כוללת אותם | **אין** (שורות "Bercel" — 21, כולן Zemplén; ילידי Tiszabercel) | **אין** |
| 1880 / 1890 / 1900 / 1910 / 1920–21 / 1930 / 1941 | **אין אינדקס שמי מקוון** שנמצא (בהונגריה שרדו גיליונות שמיים רק לחלקים — בודפשט בעיקר; ליישובי ברצל/באלאשאג'רמאט/פראואנקירכן — לא ידוע). נתונים **מצרפיים** בלבד: ראו להלן | — | — |
| **1921 — "Hungaricana LIBRARY"** | JewishGen "1921 Karpatalja Subcarpathia Census" (5,013 רשומות; `24016ecb-…`) — "אינדקס כל הרשומות היהודיות מתוך **התמונות המקוריות שב-Hungaricana**" | **מפקד 1921 של צ'כוסלובקיה בקרפטורוס (Kárpátalja) בלבד**; יישובים שנוספו לאינדקס: Akli, Alsóremete, Asztély, Badaló, Balazsér, Beregardó, Beregdéda, Beregújfalu, Bulcsú, Csetfalva, Felsőremete, Gát, Halábor, Kígyós, Kovászó, Macsola, Bene, Makkosjánosi, Nagybégány, Alsósárad, Alsóveresmart, Csarnatő, Felsőveresmart, Nagybereg, Rakasz, Kisgút, Lipcsemező, Misztice, Nagyrákóc. **אין גיליונות שמיים של 1921 להונגריה** בספרייה של Hungaricana (חיפוש "egyéni adatlap népszámlálás 1921": 0; "Nógrádbercel": 66 תוצאות — ספרים/אלמנכים; "népszámlálás 1921 Kárpátalja": 242 — ספרות משנית) | **אין כיסוי** | **אין כיסוי** |
| Czechoslovak Population Census **1930** (JewishGen `d9ec007d-…`) | SNA Bratislava | סלובקיה בלבד. בלומנטל + Bercel (20 שורות; 3 משקי בית): Ľudovít b. 2.4.1902 Bercel (Lučenec); Leopold b. 27.3.1887 Bercel ∞ Mária (Dunajská Streda, 1911); Áron b. 15.5.1872 Bercel (Bratislava) — **אף אחד אינו בנו/ילדיו** | — | — |
| נתונים מצרפיים (ספר "Senkiföldjén") | Hungaricana Library `NOGM_AFT_50`/`_45` | ראו קובץ הספר §1 | יהודי ברצל: 1840: 67 · 1848: 112 · 1869: 115 · 1880: 128 · 1900: 118 · 1910: 158 · 1920: 181 · 1930: 179 · 1941: 158/2,277 · 1944: ≈180; באלאשאג'רמאט: 1785…1941 (1,712) | — |

**1938–1941 רישומי יהודים:** ברשימות המקוונות שנבדקו (JewishGen: "Hungary Holocaust Memorials", KMSZ, "Hungarian Jewish Survivors…", "Hungarian-speaking families who wanted to immigrate to Palestine") — אין בלומנטל מברצל (למעט JAKUBOVICS 1907 עם אם Blaumenthal, ו-Miklós Blumenthal נ' 27.11.1920 ברצל, ניצול Hillersleben — בקובץ 26.10). אין רשימות 1941 שמיות של נוגראד מקוונות; המקור: NML IV. 454 (ראשות המחוז; רשימות "zsidótörvény hatálya alá").

## 2. רישומים אזרחיים וקהילתיים (JewishGen) — טווחי שנים שנמצאו

| מאגר | מקור/סרט | רשום | טווח שנים (נמדד) | הערה |
|---|---|---|---|---|
| **Hungarian Births** — פראואנקירכן / בולדוגאסוני (קהילה, מחוז Nezsider, מושון) | LDS 700859 | רישום "Frauenkirchen/…" עד 1884; "Boldogasszony/…" מ-1885 | **1835–1894** (+ חריגות מאוחרות) · 1,831 שורות | **חובה לחפש את שני הכתיבים** |
| **Austria: Burgenland Marriages II / Deaths II** | LDS 700859, 701085, 701094… | חתונות/פטירות של Frauenkirchen | חתונות 1840s–1894; פטירות 1846–1892 ואילך (דוגמאות: 1886, 1892) | — |
| **Hungarian Births / Marriages / Deaths** — באלאשאג'רמאט (Local Gov't, LDS 642840/642841) | פנקסים אזרחיים-קהילתיים | לידות; נישואין; פטירות | **לידות 1850–1880** (2,945 שורות) · **נישואין 1851–1895** (1,068) · **פטירות 1850–1895** (2,352) | **אין לידות 1881+**; אין ליבוביץ מנוגראד (HB/HM/HD) |
| **Hungarian Deaths** — נוגראדברצל (Berczel, מחוז Szirák) | LDS-642840 (1890–1894), LDS#4838205/#4838211/#4838569 (1896–1948) | פטירות | **1890–1948** (220 שורות Berczel/Szirák) | **ממצא עיקרי** — קובץ הנוגראדברצל |
| **Hungarian Births / Marriages** — נוגראדברצל | — | — | לידות: 3 שורות בלבד (בודפשט 1887–1891, "Nogradbercel" כמקום אב); נישואין: 4 (1852–1888, באלאשאג'רמאט) | **אין לידות/נישואין 1895+ של ברצל** |
| **Slovak Civil Marriage / Birth / Death Records** (Hódmezővásárhely: באלאשאג'רמאט; SSA: Šaľa/Galánta, Dunaszerdahely, Kassa, Losonc וכו') | CsCsM Levéltár; SSA | באלאשאג'רמאט: **נישואין 1895–1916** (440 מתוך 499), **פטירות 1895–1915** (872/905), **לידות 1895–1906** (137, עם חריגות 1907–1915) | ראו עמודה | **נישואי בנו ואידה — גלנטה 1912 (נמצא)**; ליבוביץ: 5 נישואין בבאלאשאג'רמאט 1905–1916 (אף אחד אינו משה × Végh) |
| **JOWBR Hungary** — Bercel | — | 37 שורות Blumenthal | — | נגזר מפנקס הפטירות; כולל את Szerén ו-Dezső ובני הזוג Mór/Regina (ראו קובץ הנוגראדברצל §1) |
| **Matricula Online (Diözese Eisenstadt)** | — | **קתולי בלבד** (לפי ההנחיה; לא נבדק מחדש) | — | לא רלוונטי לרישומים יהודיים של פראואנקירכן |
| **Hungary Civil Registration 1895–1980 (FamilySearch)** | תמונות | לידות/נישואין/פטירות 1895+ | — | **חסום** (אין אסימון); זהו המקור לפנקס הלידות 1912–1928 של ברצל ולנישואי בנו |

## 3. שליליים מדויקים (מה נבדק — ואין)

| # | שאלה | מאגר + יישוב + שנים | תוצאה | דירוג |
|---|---|---|---|---|
| N-A | לידת בנו (20.7.1892) | HB — ברצל/באלאשאג'רמאט; רישום באלאשאג'רמאט מסתיים ב-1880; לידות ברצל 1895+ לא באינדקס | אין | אינו שלילה — מחוץ לכיסוי |
| N-B | לידות ילדי בנו (1912–1928), כולל יעקב ≈1917/18, **Ignác 1919** | HB/SB (Slovak Civil Births: Blumenthal — 20 שורות, כולן Losoncz/Dunaszerdahely); פראואנקירכן/גלנטה | אין | אינו שלילה — ברצל 1895+ לא מכוסה |
| N-C | נישואי Mór ו-Regina Wosner (≈1877–1880) | HM: Wosner/Wozner/Wuszner (54+56+46 שורות) סוננו ל-Blumen/Berc/Nograd — רק Jakob × Wuszner Leni, דונסרדהלי 1868 ("Groom resided in Berzel") | אין | אינו שלילה — ייתכן שנישאו בדונסרדהלי/סביבה (עדי חתונות ווזנר 1906, 1913: Mór Blumenthal מברצל; `SM_0012598`, `SM_0013086`) |
| N-D | לידת רגינה ווזנר (≈1856; הורים Mayer // Fleischman Fani) | HB: Wosner/Wozner/Wuszner/Vozner (140+149+101+151) | אין | אינו שלילה |
| N-E | **רשומת פטירה של בנו או אידה** | HD Berczel 1890–1948 (220), BD2 Frauenkirchen | אין (נפטרו 1944 — לא נרשמו בברצל, או לא נאספו) | **ככל הנראה** — לא נרשמו; ראו קובץ הנוגראדברצל |
| N-F | **יעקב בלומנטל נ' 1917/18** ב-HD/JOWBR/Slovak Civil | Blumenthal בכל המאגרים הנ"ל | אין Jakab/Jakob שנולד 1917/18; JOWBR Bercel — 37 שורות, אין | **ככל הנראה** (במסגרת הכיסוי) |
| N-G | **ליבוביץ (Lebovits/Leibovits/Lebovics/Leibovics) בנוגראד** | HB (1,015 שורות), HM (247), HD (291) — פונטי; סינון Nógrád/Balassagyarmat/Szécsény | **0** (כל "Gyarmat" שנמצא — Fehérgyarmat, מחוז Szatmár: משפחת Mór Lebovics ∧ Fogel Borbála מאוסקה — **לא** שלנו) | **ככל הנראה** — בטווח 1850–1895 |
| N-H | משה (b.1890; אב Abraham, אם Feige-Taube) × Frima/Végh Frumet | Slovak Civil Marriage (238 שורות Lebovits) סונן ל-Végh/Frim/Frum/Franci; HM (Végh — 12 שורות) | אין | **ככל הנראה** (נישואין ≈1913–1920 — 1916 הוא סוף כיסוי באלאשאג'רמאט) |
| N-I | Lebovits **Magda/Miriam b. 1925** בנוגראד | לידות 1925 — מחוץ לכיסוי (HB 1880; SB 1906–1915) | — | אינו שלילה |
| N-J | מפקד 1848/1857/1869 — נוגראד ומושון | ראו §1 | נוגראד אינו; מושון 1848 כן | — |

## 4. הערות שיטה
- **פענוח תוצאות:** `srch1t=Q` פונטי (Beider–Morse) לשם משפחה/עיר; `srch1v=X` (כל שדה) + `srch1t=C` (contains) לחיפושי מחוז. התאמה פונטית לעיר "Berczel" מערבבת **Nógrádbercel** עם **Tiszabercel** (Szabolcs) ו-**Ceglédbercel** — כל שורה נבדקה לפי מחוז-על.
- **גבולות האתר:** שתי שורות חיפוש בלבד (ארבע — בתרומה של $180). השתמשתי בשתיים.
- **הקובץ הקודם** `../jewishgen/blumenthal_bercel_2026-10-26.md` — "אין משה בן ציון, חוה (אידה) או ילדיהם" ב-Hungarian Deaths **תוקן** כאן; "N-11 … אין ילדי משה בן ציון וחוה" בדוח יעקב §9.4 — **שגוי** לגבי Szerén (1918), Dezső (1928) ולגבי הוריו.

## 5. מה נותר / צעדים הבאים
1. **FamilySearch (דורש חשבון/אסימון של המשתמש):** (א) סרט 700859 — תמונות 216 (לידת אידה), 62 (לידת Juda), 183, 46; סרט 701094; (ב) "Hungary Civil Registration 1895–1980" — לידות Nógrádbercel (Szirák RD) 1912–1928, ובעיקר **1917–1919** (יעקב / Ignác); (ג) SSA Šaľa Galánta marriages 1912 (תמונה); (ד) Balassagyarmat civil births 1915–1928 (ליבוביץ).
2. **NML (ארכיון מחוז נוגראד, בלשאג'ארמט):** IV. 7. c Öi. 986 (מפקד 1848 ברצל); V. 202. 2 (ברצל 1945–46: שאלונים, נכסים נטושים: 687, 739, 786, 877, 1024, 1058/1945; 875/1946) — **עשויים לשאת את Ignác/Jakab**; NML IV. 454 (רשימות 1941/42).
3. **Magyar Mezőgazdák Szövetkezete** (MOL Z 819–823, 828–829) — תיקים על בנו: פריט 122 (1926–1928, "Blumenthal Benő földbirtokos, berceli lakos elleni per iratai") ופריט 3885 (1931–1943, "Blumenthal Benő Balassagyarmat, peres iratai") — לפי Sárközi Zoltán, *Szövetkezetek és mezőgazdasági vállalatok fondjai* (Levéltári leltárak 79; Budapest, 1983), pp. 209, 319 (Hungaricana Library `MolDigiLib_LevLelt_79`). — **מצביע על מעבר בנו לבאלאשאג'רמאט בשנות ה-30**.
4. ליבוביץ: ראו קובץ מרים.
