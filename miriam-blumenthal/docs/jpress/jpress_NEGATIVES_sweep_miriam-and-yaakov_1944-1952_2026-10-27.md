# JPress sweep — Miriam Blumenthal née Leibovitz (מרים ליבוביץ) and Yaakov Blumenthal (יעקב בלומנטל), 1944–1952 — queries with per-hit classification, coverage limits and new items — 2026-10-27

**Subjects.**
(1) **Miriam Blumenthal née Leibovitz.** Marriage certificate, Petah Tikva rabbinate, 27.10.1948 (H 99915): "פועלת", 22, Hovevei Zion 12, Petah Tikva; parents "משה הלוי ליבוביץ" and "פרימט", both marked dead; voters' list 1949: b. 1925. Family tradition: Hungary; a relative's tree calls her "מרים מגדה". The project's working identification (`../../report.md`, sections 4.1–4.2): the parents are Moshe (shoemaker, Tököly utca, Balassagyarmat) and Fruma/Frumet/Fanni née Végh; the Yad Vashem pages of 2000, filled by Avraham Aharon (Netanya; probably a son), name Moshe, Fruma, Shimon and Feige-Toybe "Lili", and the archive book adds Manó; **Magda b. 20.1.1922** (Auschwitz – Ravensbrück – Altenburg – Buchenwald; next of kin Rose Lebovits, Budapest) is the open candidate for Miriam.
(2) **Yaakov Blumenthal.** Same certificate: "חייל", 30, residence "אי שם...", parents "משה בן ציון" and "חוה", both marked dead. Probably a son of Benő (Moshe Ben-Zion) and Ida née Deutsch of Nógrádbercel (twelve children); brothers Yitzhak (Ein Ganim 49, Petah Tikva, 1949), Michael, Yehuda; sister Rivka Gombo (`../../../yaakov-blumenthal/report.md`, sections 4.3–4.4 and 4.8).
**Date.** 2026-10-27. **Server.** JPress (National Library of Israel) through `jpress_search` (267 calls, recorded as 266 rows because one query was fetched in two pages), `jpress_get_article` and, once and then abandoned, `jpress_fetch_raw`. Sections opened: 117 directly; 66 Lakrov Velarahok sections, 40 section fetches on the "Moshe Leibovitz" hits and 120 HaTsofeh sections through delegated read-only extraction passes (D-1, C-6, C-7).
**Copyright.** Page images are locked; only OCR text was read. This file records section ids, dates, titles and short quotations (25 words or fewer) per hit, as printed, with the bidirectional control characters dropped. The OCR is noisy.
**Result in one line.** Six flagged findings (B-1 to B-6), all new to the project; no blocker; the full list is in B and in the summary.

## Canaries (run first, all green)
- `jpress_get_article lakkarov19470324-01.2.4` returned the known ship list (page 2 of "מעפילי חיים ארלוזורוב") and contains "קוטנר אברהם, 16, אוזורקוב". PASS: the blocker condition is not met.
- Known-answer controls: every delegated pass opened with a section whose entry was known, and every control was found verbatim. Lakrov passes: `lakkarov19470206-01.2.3` ("בלומנטאל איגנאץ־יאנו (מיכאל בלומנטאל) 4868"), `lakkarov19460519-01.2.3` (three Leibovitz entries), `lakkarov19460331-01.2.10`, `lakkarov19460110-01.2.15` ("בלום יעקב בלומנטאל יושד"), `lakkarov19470109-01.2.3` ("בלומנטאל מיכאל"), `lakkarov19460314-01.2.6` ("בלומנטאל איזידור"). "Moshe Leibovitz" passes: `hzh19481008-01.2.64`, `lakkarov19470324-01.2.8`, `hadoar19440407-01.2.18`. HaTsofeh passes: `hzh19481008-01.2.64`, `hzh19490624-01.2.99`, `hzh19520821-01.2.56`, `hzh19460815-01.2.54`, `hzh19490209-01.2.28`.
- Positive controls for the query engine (exact phrases find the known entries): `"בן משה בלומנטאל"` finds `hzh19481008-01.2.64`; `"מיכאל בלומנטאל"` finds `lakkarov19470206-01.2.3`; `"בלומנטאל מיכאל"` finds `lakkarov19470109-01.2.3`; `"לייבו מרים"` finds `lakkarov19460519-01.2.3`.
- Zero-hit searches are real answers: all 267 `jpress_search` calls returned a normal header ("N results for …"); no error, no timeout, no query repeated because of a fault. The one `jpress_fetch_raw` call (raw Veridian JSON for `"ליבוביץ מרים"`) ignored the date parameters, returned 14 results over all years and only image snippets, and was not used again.

## Coverage limits (measured today)
| Source | Measured | Consequence |
|---|---|---|
| Lakrov Velarahok (`lakkarov`) | sections containing `ישראל`: 559 (1945: 238; 1946: 259; 1947: 62); first `lakkarov19450628-01.2.2` (28.6.1945), last `lakkarov19470917-01.2.2` (17.9.1947) | The relatives-search lists and the ship and camp lists exist only for 28.6.1945 – 17.9.1947; nothing before or after |
| HaTsofeh (`hzh`), registration window | `ישראל` in 1.10–15.11.1948: 940 sections; `נרשמו לנשואין` in the same window: 23 sections (62 for September–December 1948) | The window of the 27.10.1948 wedding is indexed for HaTsofeh (940 sections over 46 days); the notice (B-1) was printed 8.10.1948 |
| Uj Kelet (`ujk`) | `Izrael`: 18,964 sections, of which 13,227 are type PAGE (a whole page of OCR; `jpress_search` lists them with an empty id, so they can be counted but not opened); 1949: 1,229; 1950: 641 | The Hungarian-language Israeli paper is dense from 1949; hidden PAGE hits are a blind spot (counts per query in A14) |
| Date filter | `date_to=1952` includes all of 1952 (hits up to 1952-12-22 appear) | The sweep covers 1944–1952 as asked |

Search behaviour that limits recall, observed in this sweep:
1. Registration lists print "FIRST בן/בת FATHER SURNAME — residence" (1944–1948) and "FIRST SURNAME בן FATHER" (1952). A phrase such as `"מרים ליבוביץ"` can never match them; patronymic phrases (`"בת משה ליבוביץ"`, `"בן משה בלומנטאל"`) do.
2. OCR errors in the very entries sought: "צרים" for מרים, "_גגים" for גנים, "בה" for בת, "משד" and "פשה" for משה, "ליבובי" and "לייבו" (surname cut), "טאגדו" for מאגדה. Every variant needs its own query.
3. A hyphen is part of the token (`איגנאץ־יאנו`: the phrases `"בלומנטאל איגנאץ"` and `"בלומנטל איגנץ"` return 0); an apostrophe splits a token (`ג'רמט` = `גרמט`: 87 noise hits).
4. Unquoted multi-word queries are AND anywhere in a section (`לייבוביץ מרים` in Lakrov: 110 sections).
5. Lakrov lists print "surname, first name, age, parents, country letter" (ה Hungary, ר Romania, פ and ם Poland, צ׳ Czechoslovakia, קר Carpatho-Rus); columns are garbled and several lists are truncated; Hungarian lists in Latin script appear from July 1945.

## How hits were classified
Text: **מאומת** means what the OCR says, quoted as printed. Identification grades: **כמעט ודאי**, **ככל הנראה**, **אפשר ש… (טעון אימות)**, **לא הוכרע**, **נשלל** (with the reason). NEW means the section id is not yet in the project: a search of the repository for every id in B found none (`lakkarov19460519-01.2.3` is held by the Rachel Zadok folder for another question, and `lakkarov19470414-01.2.2` by the Tzipora Kutner log for another person). The only JPress items already in this folder (`docs/jpress/`) are the 1974–1977 death notice, condolence advertisement and memorial advertisements for the son Meir.
Publication codes: hzh HaTsofeh (הצפה), dav Davar, haretz Haaretz, ahr Al HaMishmar, hbkr HaBoker, hmf HaMashkif, hegeh HaGeh, khm Kol HaAm, ytz HaTsofeh LeYeladim, ydv Davar LeYeladim, hadoar HaDoar (New York), lakkarov Lakarov VeLarahok, ujk Uj Kelet, egy Egyenlőség.

## A. Query tables
Numbering Q-1 … Q-266 follows the order in which the queries were run; the tables are grouped by subject. A merged row lists each query with its own count, in the same order.

### A1. Miriam Leibovitz — name forms (Hebrew), and her married name Blumenthal
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-1 | `"מרים ליבוביץ"` | phrase; 1944–1952 | 0 | – | none |
| Q-2 | `"ליבוביץ מרים"` | phrase; 1944–1952 | 4 | 1946-07-01 – 1951-01-05 | 1 unresolved (hegeh19460701-01.2.35, see B-4); 3 adjacency artefacts (C-1) |
| Q-3 | `"לייבוביץ מרים"` | phrase; 1944–1952 | 4 | 1946-01-31 – 1947-06-03 | lakkarov19460519-01.2.3 → B-4; lakkarov19470507-01.2.3 → B-9; lakkarov19460131-01.2.6 → C-1; hmf19470603-01.2.31 artefact |
| Q-4, Q-16–19 | `"מרים לייבוביץ"`; `"לבוביץ מרים"`; `"מרים לבוביץ"`; `"לאבוביץ מרים"`; `"ליבוביטש מרים"` | phrase; 1944–1952 | 0; 0; 0; 0; 0 | – | none |
| Q-219 | `"לייבו מרים"` | phrase; 1944–1952 | 1 | 1946-05-19 | lakkarov19460519-01.2.3 → B-4 (the only hit) |
| Q-220, Q-221, Q-224, Q-250–253 | `"ליבו מרים"`; `"ייבוביץ מרים"`; `"מרים לייבו"`; `"מרים בלומנטל"`; `"מרים בלומנטאל"`; `"בלומנטל מרים"`; `"בלומנטאל מרים"` | phrase; 1944–1952 | 0; 0; 0; 0; 0; 0; 0 | – | none |

### A2. Magda — spellings and orders (Hebrew)
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-5–7 | `"מגדה ליבוביץ"`; `"ליבוביץ מגדה"`; `"לבוביץ מגדה"` | phrase; 1944–1952 | 0; 0; 0 | – | none |
| Q-8 | `"לייבוביץ מגדה"` | phrase; 1944–1952 | 1 | 1947-04-07 | hzh19470407-01.2.48 → B-9 (Czechoslovakia) |
| Q-9 | `"ליבוביץ מאגדה"` | phrase; 1944–1952 | 0 | – | none |
| Q-10 | `"לייבוביץ מאגדה"` | phrase; 1944–1952 | 1 | 1947-04-14 | lakkarov19470414-01.2.2 → B-9 (age 23, "מונקאץ׳") |
| Q-11–15, Q-222, Q-223 | `"לבוביץ מאגדה"`; `"מאגדה לייבוביץ"`; `"מאגדה ליבוביץ"`; `"מגדה לייבוביץ"`; `"מגדה לבוביץ"`; `"לייבו מגדה"`; `"לייבו מאגדה"` | phrase; 1944–1952 | 0; 0; 0; 0; 0; 0; 0 | – | none |

### A3. Rose / Rozi (the relative named on Magda's camp card)
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-20–22 | `"רוזה ליבוביץ"`; `"ליבוביץ רוזה"`; `"רוזה לייבוביץ"` | phrase; 1944–1952 | 0; 0; 0 | – | none |
| Q-23 | `"לייבוביץ רוזה"` | phrase; 1944–1952 | 1 | 1951-05-16 | hzh19510516-01.2.47 → C-2 (Rosa bat Meir, Haifa) |
| Q-24 | `"לייבוביץ רוזי"` | phrase; 1944–1952 | 1 | 1947-03-24 | lakkarov19470324-01.2.4 (the canary list) → C-2 |
| Q-25, Q-26 | `"ליבוביץ רוזי"`; `"רוזי לייבוביץ"` | phrase; 1944–1952 | 0; 0 | – | none |

### A4. Balassagyarmat — Hebrew spellings of the town
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-27–30 | `באלאשאג'רמאט`; `באלאשאגיארמאט`; `בלאשגרמט`; `גיארמת` | token; 1944–1952 | 0; 0; 0; 0 | – | none |
| Q-31 | `גיארמאט` | token; 1944–1952 | 1 | 1944-02-28 | dertog19440228-01.2.47 → C-2 (irrelevant) |
| Q-32 | `ג'רמט` | token; 1944–1952 | 87 | 1944-03-13 – 1952-12-22 | noise: the apostrophe splits the token; same 87 hits as Q-34; not read; unverified noise |
| Q-33 | `"ג רמט"` | phrase; 1944–1952 | 1 | 1949-12-15 | khm19491215-01.2.25 not opened (title: a workers' council item) |
| Q-34 | `גרמט` | token; 1944–1952 | 87 | listed 50 of 87: 1944-03-13 – 1949-10-01; all hits by year (facets): 1944–1952 | same set as Q-32; first 50 listed; not read |
| Q-35 | `באלאשאדיארמאט` | token; 1944–1952 | 1 | 1949-09-30 | momenturuguay19490930-01.2.16 → C-2 (irrelevant) |
| Q-36, Q-37 | `באלאשאגארמאט`; `בלשגיארמט` | token; 1944–1952 | 0; 0 | – | none |
| Q-38 | `גיארמאט` | token; all dates | 4 | 1888-08-17 – 1970-08-09 | 1 hit in range (= Q-31); 3 out of range (1888, 1965, 1970) not read |

### A5. Names of Miriam's possible parents and siblings: Moshe, Fruma/Frimet, Avraham Aharon, Feige-Toybe/Lilla
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-39, Q-40 | `"משה ליבוביץ" באלאשא`; `"משה לייבוביץ" באלאשא` | phrase + word; 1944–1952 | 0; 0 | – | none |
| Q-41 | `"משה ליבוביץ"` | phrase; 1944–1952 | 29 | listed 10 of 29: 1944-04-07 – 1945-09-07; all hits by year (facets): 1944–1952 | first run listed 10 of 29; the full list is Q-225 → C-6 |
| Q-42 | `"משה לייבוביץ"` | phrase; 1944–1952 | 12 | listed 10 of 12: 1944-07-21 – 1950-08-10; all hits by year (facets): 1944–1952 | first run listed 10 of 12; the full list is Q-226 → C-6 |
| Q-126–132 | `"פרומה ליבוביץ"`; `"פרימט ליבוביץ"`; `"ליבוביץ פרומה"`; `"לייבוביץ פרומה"`; `"ליבוביץ פרימט"`; `"ליבוביץ אברהם אהרן"`; `"לייבוביץ אברהם אהרן"` | phrase; 1944–1952 | 0; 0; 0; 0; 0; 0; 0 | – | none |
| Q-133 | `"ליבוביץ אסתר"` | phrase; 1948–1949 | 0 | – | none |
| Q-225 | `"משה ליבוביץ"` | phrase; 1944–1952 | 29 | 1944-04-07 – 1952-07-27 | the 29 hits, all classified → C-6 |
| Q-226 | `"משה לייבוביץ"` | phrase; 1944–1952 | 12 | 1944-07-21 – 1952-07-08 | the 12 hits, all classified → C-6 |
| Q-227 | `"פייגה טויבה"` | phrase; 1944–1952 | 0 | – | none |
| Q-228 | `"פייגע טויבע"` | phrase; 1944–1952 | 1 | 1949-01-17 | frw19490117-01.2.41 read: irrelevant (a Vilna family-search column) |
| Q-229, Q-230 | `"ליבוביץ לילה"`; `"לייבוביץ לילה"` | phrase; 1944–1952 | 0; 0 | – | none |

### A6. Mother "Frimam", Nechama and Esther (from the 22.8.1946 Atlit list)
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-138 | `"משה פרימאם"` | phrase; 1944–1952 | 1 | 1946-08-22 | lakkarov19460822-01.2.2 → B-3 |
| Q-139 | `פרימאם` | token; 1944–1952 | 13 | 1945-10-18 – 1948-06-28 | B-3 + 12 other sections (relatives lists 1945–46; Yiddish press 1946–48), 3 of them read for other reasons (D-1); the rest unread |
| Q-140 | `"לייבוביץ נחמה"` | phrase; 1944–1952 | 1 | 1946-08-22 | lakkarov19460822-01.2.2 → B-3 |
| Q-141 | `"ליבוביץ נחמה"` | phrase; 1944–1952 | 0 | – | none |
| Q-142 | `"לייבוביץ אסתר"` | phrase; 1944–1952 | 4 | 1945-10-04 – 1947-03-24 | B-3 + lakkarov19451004-01.2.3, lakkarov19461107-01.2.2, lakkarov19470324-01.2.4 (other Esthers; D-1, D-2) |
| Q-143–145 | `"משה פרימט"`; `"משה פרימאט"`; `"משה פרימא"` | phrase; 1944–1952 | 0; 0; 0 | – | none |
| Q-146 | `"משה פרומה"` | phrase; 1944–1952 | 2 | 1945-05-07 – 1951-10-23 | ahr19450507-01.2.28 and hbkr19511023-01.2.57.2 not read |
| Q-147–149 | `"משה פרומעט"`; `"משה פראמה"`; `"משה פרימה"` | phrase; 1944–1952 | 0; 0; 0 | – | none |
| Q-157 | `"נחמה בת משה" ליבוביץ` | phrase + word; 1946–1952 | 3 | 1949-02-28 – 1950-05-31 | 3 co-occurrence artefacts (hzh19490228-01.2.44, hzh19500424-01.2.34, hzh19500531-01.2.49) → C-5 |
| Q-158 | `"נחמה בת משה" לייבוביץ` | phrase + word; 1946–1952 | 0 | – | none |
| Q-159 | `"אסתר בת משה" ליבוביץ` | phrase + word; 1946–1952 | 6 | 1949-09-09 – 1951-11-21 | 6 co-occurrence artefacts (hzh19490909-01.2.54, hzh19500113-01.2.60, hzh19500205-01.2.51, hzh19500412-01.2.52, hzh19500531-01.2.49, hzh19511121-01.2.54) → C-5 |

### A7. Yaakov Blumenthal and his brothers/sister (Hebrew)
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-43 | `"יעקב בלומנטל"` | phrase; 1944–1952 | 11 | 1944-07-10 – 1950-09-07 | 11 hits → C-3 (all other persons) |
| Q-44 | `"בלומנטל יעקב"` | phrase; 1944–1952 | 2 | 1944-07-10 – 1945-02-05 | 2 hits → C-3 |
| Q-45 | `"בלומנטאל יעקב"` | phrase; 1944–1952 | 0 | – | none |
| Q-46 | `"יעקב בלומנטאל"` | phrase; 1944–1952 | 3 | 1944-07-11 – 1946-01-10 | 3 hits → C-3 |
| Q-47, Q-48 | `"בלומנטל איגנץ"`; `"בלומנטל ינו"` | phrase; 1944–1952 | 0; 0 | – | none |
| Q-49 | `"בלומנטל יוסף"` | phrase; 1944–1952 | 1 | 1949-11-27 | haretz19491127-01.2.37 → C-4 (estate notice, Haifa) |
| Q-50–52 | `"בלומנטל יצחק"`; `"בלומנטל מיקלוש"`; `"בלומנטל מיכאל"` | phrase; 1944–1952 | 0; 0; 0 | – | none |
| Q-53 | `"יוסף בלומנטל"` | phrase; 1944–1952 | 2 | 1945-02-05 – 1946-08-15 | 2 hits → C-4 |
| Q-54 | `"יצחק בלומנטל"` | phrase; 1944–1952 | 1 | 1950-10-02 | hzh19501002-01.2.56 → C-4 |
| Q-55, Q-56 | `"מיכאל בלומנטל"`; `"איגנץ בלומנטל"` | phrase; 1944–1952 | 0; 0 | – | none |
| Q-57 | `"יהודה בלומנטל"` | phrase; 1944–1952 | 4 | 1947-06-30 – 1952-08-21 | 4 hits → C-4; one of them is B-2 |
| Q-58, Q-59, Q-231–233 | `"ינו בלומנטל"`; `"מיקלוש בלומנטל"`; `"בלומנטאל יאנקו"`; `"בלומנטאל יאקאב"`; `"בלומנטאל יאקב"` | phrase; 1944–1952 | 0; 0; 0; 0; 0 | – | none |
| Q-254 | `"יצחק בלומנטאל"` | phrase; 1944–1952 | 1 | 1947-01-09 | lakkarov19470109-01.2.3: adjacency artefact (Barkovici Yitzhak; Blumenthal Michael) → B-5 |
| Q-255 | `"יהודה בלומנטאל"` | phrase; 1944–1952 | 0 | – | none |
| Q-256 | `"עין גנים" בלומנטל` | phrase + word; 1944–1952 | 1 | 1946-12-24 | hzh19461224-01.2.61.1 → B-7 |
| Q-257 | `"רבקה בלומנטל"` | phrase; 1944–1952 | 0 | – | none |

### A8. Patronymics ("ben/bat Moshe", "ben Moshe Ben Zion", "ben Binyamin")
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-60 | `"בלומנטל בן משה בן ציון"` | phrase; 1944–1952 | 1 | 1952-08-21 | hzh19520821-01.2.56 → B-2 |
| Q-61 | `"משה בן ציון בלומנטל"` | phrase; 1944–1952 | 0 | – | none |
| Q-62 | `"בן משה בן ציון" בלומנטל` | phrase + word; 1944–1952 | 1 | 1952-08-21 | hzh19520821-01.2.56 → B-2 |
| Q-76 | `"בת משה ליבוביץ"` | phrase; 1944–1952 | 3 | 1948-10-08 – 1952-07-27 | hzh19481008-01.2.64 → B-1; hzh19511203-01.2.40 and hzh19520727-01.2.35 → B-8 |
| Q-77 | `"בת משה לייבוביץ"` | phrase; 1944–1952 | 1 | 1952-07-08 | hzh19520708-01.2.51 → B-8 (ruled out: widow, Romania) |
| Q-78 | `"בת משה הלוי ליבוביץ"` | phrase; 1944–1952 | 0 | – | none |
| Q-79 | `"בן משה בן ציון"` | phrase; 1944–1952 | 1 | 1952-08-21 | hzh19520821-01.2.56 → B-2 |
| Q-80 | `"בן משה בלומנטל"` | phrase; 1944–1952 | 0 | – | none |
| Q-83 | `"יהודה בן אברהם פרינקל"` | phrase; 1944–1952 | 1 | 1948-10-08 | hzh19481008-01.2.64 → B-1 |
| Q-84 | `"בן משה בלומנטאל"` | phrase; 1944–1952 | 1 | 1948-10-08 | hzh19481008-01.2.64 → B-1 |
| Q-85 | `"עין גנים" בלומנטאל` | phrase + word; 1944–1952 | 0 | – | none |
| Q-86 | `"בת משה ליבובי"` | phrase; 1948–1949 | 0 | – | none |
| Q-164–167 | `"בת משה לבוביץ"`; `"בת משה לבוביטש"`; `"בת משה ליבוביטש"`; `"בת משה לאבוביץ"` | phrase; 1946–1952 | 0; 0; 0; 0 | – | none |
| Q-168 | `"בן משה ליבוביץ" פתח תקוה` | phrase + word; 1946–1952 | 0 | – | none |
| Q-260 | `"בת משה בלומנטל"` | phrase; 1944–1952 | 0 | – | none |
| Q-261 | `"בת משה בלומנטאל"` | phrase; 1944–1952 | 1 | 1946-08-08 | hzh19460808-01.2.30 → B-7 |
| Q-262 | `"בן בנימין" בלומנטל` | phrase + word; 1944–1952 | 7 | 1946-08-15 – 1950-10-02 | hzh19461224-01.2.61.1 → B-7; the others are co-occurrence artefacts (C-7; hbkr19500115-01.2.36 read: Haifa/Tel Aviv news, "Dr Blumenthal's hospital") |
| Q-263 | `"בן בנימין" בלומנטאל` | phrase + word; 1944–1952 | 4 | 1946-05-16 – 1952-05-06 | 4 co-occurrence artefacts (hzh19520506-01.2.50, hzh19460808-01.2.30, lakkarov19460822-01.2.3, lakkarov19460516-01.2.13) |
| Q-264 | `"אהרן בן בנימין"` | phrase; 1944–1952 | 4 | 1946-12-24 – 1950-11-06 | hzh19461224-01.2.61.1 → B-7; hzh19480812-01.2.53 and hzh19501008-01.2.41 read: other Aharons; hrt19501106-01.2.60 not read |
| Q-265 | `"בן משה" בלומנטל פתח` | phrase + word; 1944–1952; HaTsofeh only | 1 | 1952-01-15 | hzh19520115-01.2.51: artefact (Tel Aviv liquor-licence notice, "בלומנטל מאיר") |

### A9. Marriage-registration lists of HaTsofeh, September–December 1948 and later
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-63, Q-64 | `בלומנטל ליבוביץ`; `בלומנטל לייבוביץ` | AND; Sep–Dec 1948 | 0; 0 | – | none |
| Q-65, Q-66 | `"נרשמו לנישואין" בלומנטל`; `"הרשומים לנישואין" בלומנטל` | phrase + word; 1948 | 0; 0 | – | none |
| Q-67 | `נרשמו לנשואין` | AND; Sep–Dec 1948 | 62 | listed 10 of 62 (1948-09-01 – 1948-09-15); all 62 are in Sep–Dec 1948 | coverage: 62 lists, September–December 1948 (not read one by one; the relevant lists are in C-5) |
| Q-68 | `נרשמו לנישואין` | AND; Sep–Dec 1948 | 4 | 1948-09-23 – 1948-12-15 | alternate headline spelling: 4 lists (23.9, 17.10, 15.11, 15.12.1948), not opened; none contains בלומנטאל (Q-135) |
| Q-69 | `ישראל` | token; 1.10–15.11.1948; HaTsofeh only | 940 | listed 5 of 940; all in 1.10–15.11.1948 | coverage: 940 HaTsofeh sections in 1.10–15.11.1948 |
| Q-70 | `רבנות פתח תקוה` | AND; 1.10–15.11.1948 | 0 | – | none (the lists print "הרבנות הראשית בפתח תקווה", Q-137) |
| Q-71 | `"נרשמו לנשואין" בלומנטל` | phrase + word; Sep–Dec 1948 | 0 | – | none |
| Q-72 | `"נרשמו לנשואין" ליבוביץ` | phrase + word; Sep–Dec 1948 | 3 | 1948-10-08 – 1948-12-12 | hzh19481008-01.2.64 → B-1; hzh19481122-01.2.30 and hzh19481212-01.2.33 → C-5 (other persons) |
| Q-73 | `"נרשמו לנשואין" לייבוביץ` | phrase + word; Sep–Dec 1948 | 0 | – | none |
| Q-74 | `בלומנטל` | token; 1.10–15.11.1948; HaTsofeh only | 0 | – | none (the notice spells בלומנטאל, see Q-135) |
| Q-75 | `נרשמו לנשואין` | AND; 1.10–15.11.1948 | 23 | 1948-10-01 – 1948-11-12 | coverage: 23 registration-list sections in the window of the wedding |
| Q-81 | `"בת משה" ליבוביץ מרים` | phrase + word; Sep–Dec 1948 | 3 | 1948-11-11 – 1948-12-12 | 3 co-occurrence artefacts (hzh19481111-01.2.39, hzh19481208-01.2.44, hzh19481212-01.2.33) → C-5 |
| Q-82 | `"אסתר בת משה ליבוביץ"` | phrase; 1944–1952 | 0 | – | none |
| Q-134 | `בלומנטאל ליבוביץ` | AND; Sep–Dec 1948 | 1 | 1948-10-08 | hzh19481008-01.2.64 → B-1 |
| Q-135 | `בלומנטאל` | token; Sep–Dec 1948 | 8 | 1948-09-03 – 1948-12-31 | B-1 + 7 other persons (C-5): ahr19480903-01.2.18, hzh19480923-01.2.37, dav19480923-01.2.29, hzh19480908-01.2.42, hadoar19481119-01.2.8, hadoar19481231-01.2.33; hzh19480909-01.2.10 → B-7 |
| Q-136 | `"נרשמו לנשואין" בלומנטאל` | phrase + word; Sep–Dec 1948 | 1 | 1948-10-08 | hzh19481008-01.2.64 → B-1 |
| Q-137 | `"הרבנות הראשית בפתח תקווה"` | phrase; Sep–Dec 1948 | 2 | 1948-09-28 – 1948-10-08 | hzh19481008-01.2.64 → B-1; hzh19480928-01.2.59 read: other couples |
| Q-150 | `"נרשמו לנשואין" בלומנטל` | phrase + word; 1949–1952 | 2 | 1950-11-08 – 1951-04-18 | 2 hits → C-4 (namesakes) |
| Q-151–153 | `"נרשמו לנשואין" בלומנטאל`; `"הרשומים לנשואין" בלומנטל`; `"הרשומים לנשואין" בלומנטאל` | phrase + word; 1949–1952 | 0; 0; 0 | – | none |
| Q-154 | `בלומנטל פתח תקוה` | AND; 1949–1952; HaTsofeh only | 3 | 1951-06-26 – 1952-11-14 | 3 hits → C-4 (namesakes) |

### A10. Lakrov Velarahok — Blumenthal variants
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-87 | `בלומנטל` | token; 1945–1948; Lakrov only | 2 | 1947-06-30 – 1947-09-17 | both read (D-1 rows 54–55): Nathan of Warsaw; Nachman of Staszów |
| Q-88 | `בלומנטאל` | token; 1945–1948; Lakrov only | 30 | 1945-07-19 – 1947-03-24 | all 30 sections read (D-1, D-2); B-5 found; the rest other persons |
| Q-89–91 | `"בלומנטאל איגנאץ"`; `"בלומנטאל יוזף"`; `"בלומנטאל יוסף"` | phrase; 1944–1952 | 0; 0; 0 | – | none |
| Q-92 | `"בלומנטאל יצחק"` | phrase; 1944–1952 | 1 | 1949-06-24 | hzh19490624-01.2.99: adjacency artefact (court report, Hanan Blumenthal and Yitzhak Schreiber) → B-9 |
| Q-93 | `"בלומנטאל מיכאל"` | phrase; 1944–1952 | 1 | 1947-01-09 | lakkarov19470109-01.2.3 → B-5 |
| Q-94–98 | `"בלומנטאל מיקלוש"`; `"בלומנטאל ינו"`; `"בלומנטאל יאנו"`; `"בלומנטאל יאקוב"`; `"בלומנטאל יהודה"` | phrase; 1944–1952 | 0; 0; 0; 0; 0 | – | none |
| Q-99 | `בלומנטאל הונגריה` | AND; 1945–1948; Lakrov only | 7 | 1945-08-16 – 1947-02-06 | 7 sections, all read; co-occurrence only (D-1) |
| Q-100 | `"מיכאל בלומנטאל"` | phrase; 1944–1952 | 1 | 1947-02-06 | lakkarov19470206-01.2.3 → B-5 |
| Q-101 | `איגנאץ־יאנו` | token; 1944–1952 | 1 | 1947-02-06 | lakkarov19470206-01.2.3 → B-5 |
| Q-102 | `"בלומנטאל איגנאץ־יאנו"` | phrase; 1944–1952 | 1 | 1947-02-06 | lakkarov19470206-01.2.3 → B-5 |
| Q-103, Q-104 | `"בלומנטל מיכאל"`; `"בלומנטאל איגנץ"` | phrase; 1944–1952 | 0; 0 | – | none |

### A11. Lakrov Velarahok — Leibovitz/Magda co-occurrence, ship and camp lists, coverage
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-105 | `לייבוביץ מרים` | AND; 1945–1948; Lakrov only | 110 | listed 5 of 110: 1945-12-06 – 1947-03-24; all hits by year (facets): 1945–1947 | co-occurrence of the two words anywhere in a section; 110 sections, 5 listed; the adjacency forms are Q-2, Q-3, Q-219 |
| Q-106 | `ליבוביץ מרים` | AND; 1945–1948; Lakrov only | 10 | listed 5 of 10: 1945-12-27 – 1946-09-12; all hits by year (facets): 1945–1947 | 5 of 10 listed; 3 read (lakkarov19460822-01.2.2 = B-3; two in D-1); 2 unread (E) |
| Q-107 | `לייבוביץ מאגדה` | AND; 1945–1948; Lakrov only | 36 | listed 5 of 36: 1945-09-20 – 1947-03-24; all hits by year (facets): 1945–1947 | 5 of 36 listed; 3 of the listed ones unread (E) |
| Q-108 | `ליבוביץ מאגדה` | AND; 1945–1948; Lakrov only | 6 | listed 5 of 6: 1946-01-10 – 1946-09-12; all hits by year (facets): 1946–1947 | 5 of 6 listed; 2 of the listed ones unread (E) |
| Q-109 | `לייבוביץ מגדה` | AND; 1945–1948; Lakrov only | 2 | 1945-11-22 – 1946-08-06 | lakkarov19460806-01.2.2 (read, D-1) and lakkarov19451122-01.2.3 (unread, E) |
| Q-110 | `לבוביץ מאגדה` | AND; 1945–1948; Lakrov only | 7 | listed 5 of 7: 1945-08-23 – 1946-04-18; all hits by year (facets): 1945–1946 | 5 of 7 listed, all unread (E) |
| Q-111 | `מעפילי` | token; 1945–1948; Lakrov only | 15 | 1946-03-31 – 1947-05-07 | 15 ship/transfer lists; all read (D-1, D-2) |
| Q-112 | `המעפילים` | token; 1945–1948; Lakrov only | 11 | 1946-01-24 – 1946-08-29 | 11 ship lists; all read (D-1, D-2) |
| Q-113 | `קפריסין` | token; 1945–1948; Lakrov only | 13 | 1946-08-22 – 1947-03-24 | 13 Cyprus-exile lists; all read (D-1) |
| Q-155 | `ישראל` | token; all dates; Lakrov only | 559 | listed 1 of 559: 1947-09-17 (last) | coverage (descending order; proxy = sections containing "ישראל"): last indexed Lakrov section `lakkarov19470917-01.2.2`, 17.9.1947 |
| Q-156 | `ישראל` | token; all dates; Lakrov only | 559 | listed 1 of 559: 1945-06-28 (first) | coverage (ascending order): first indexed Lakrov section `lakkarov19450628-01.2.2`, 28.6.1945; by year 1945: 238, 1946: 259, 1947: 62 |

### A12. Nógrádbercel, Gombo, Hanan Blumenthal
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-114, Q-115 | `נוגראדברצל`; `נוגרדברצל` | token; 1944–1952 | 0; 0 | – | none |
| Q-116 | `"נוגרד ברצל"` | phrase; 1944–1952 | 0 | – | none |
| Q-117 | `בערצעל` | token; 1944–1952 | 0 | – | none |
| Q-118 | `ברצל` | token; 1944–1952 | 16 | listed 10 of 16: 1944-10-06 – 1952-11-25; all hits by year (facets): 1944–1952 | bare token; 10 of 16 listed; not read; not a place hit |
| Q-119–121 | `בלומנטל ברצל`; `בלומנטאל ברצל`; `בלומנטל נוגרד` | AND; 1944–1952 | 0; 0; 0 | – | none |
| Q-122 | `גומבו` | token; 1944–1952 | 9 | 1946-08-22 – 1952-06-10 | 3 hits → B-7 (Gombo); 2 advertisements for okra seedlings (dav19510316-01.2.73, haretz19510316-01.2.67.1); hzh19490125-01.2.61.2 an advertisement name list (`גומבו היים`); dav19461101-01.2.51.4 read, token not found in the OCR; haretz19520418-01.2.68 and ydv19461121-01.2.11 unread |
| Q-123 | `גומבו בלומנטל` | AND; 1944–1952 | 0 | – | none |
| Q-124 | `"בת משה בן ציון"` | phrase; 1944–1952 | 0 | – | none |
| Q-125 | `גומבו פתח תקוה` | AND; 1944–1952 | 1 | 1950-02-14 | hzh19500214-01.2.37 → B-7 |
| Q-160, Q-161 | `"חנן בלומנטל"`; `"חנן בלומנטאל"` | phrase; 1944–1952 | 0; 0 | – | none |
| Q-162 | `"הנן בלומנטאל"` | phrase; 1944–1952 | 1 | 1949-06-24 | hzh19490624-01.2.99 → B-9 |
| Q-163 | `בלומנטאל שרייבר שורצברג` | AND; 1949 | 1 | 1949-06-24 | hzh19490624-01.2.99 → B-9 |

### A13. HaTsofeh — every section with Blumenthal (catalogue)
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-258 | `בלומנטל` | token; 1944–1948; HaTsofeh only | 35 | 1944-03-23 – 1948-12-01 | 35 sections, all read → C-7 |
| Q-259 | `בלומנטאל` | token; 1944–1952; HaTsofeh only | 68 | 1944-02-22 – 1952-06-15 | 68 sections (2 pages), all read → C-7 |
| Q-266 | `בלומנטל` | token; 1949–1952; HaTsofeh only | 36 | 1949-02-09 – 1952-11-14 | 36 sections, all read → C-7 |

### A14. Latin script and Uj Kelet (Hungarian): towns, surnames, first names
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| Q-169 | `Balassagyarmat` | token; 1944–1952 | 14 | listed 10 of 14: 1945-08-02 – 1951-11-23; all hits by year (facets): 1944–1951 | 14 hits, 10 listed on p.1 and 4 on p.2 (see Q-203); 13 readable ids read → C-8 |
| Q-170 | `"Lebovits Magda"` | phrase; 1944–1952 | 3 | 1945-11-22 – 1949-12-29 | 3 hits: ujk19491229-01.2.6, lakkarov19451122-01.2.24, lakkarov19451206-01.2.27 → B-6 |
| Q-171 | `"Blumenthal Jakab"` | phrase; 1944–1952 | 0 | – | none |
| Q-172 | `Nógrádbercel` | token; 1944–1952 | 0 | – | none |
| Q-173 | `"Blumenthal Miriam"` | phrase; 1944–1952 | 2 | 1944-01-20 | not read: 1 English-language item of 20.1.1944 (cgs) and 1 hidden PAGE hit (djc) |
| Q-174 | `Altenburg` | token; 1945–1946 | 8 | 1945-09-16 – 1946-08-09 | 6 listed (1 Lakrov: lakkarov19460331-01.2.7, not read; 5 foreign press) + 2 hidden PAGE hits; the Altenburg lists of Lakrov were read via other queries (D-2) |
| Q-175–180 | `"Lebovics Magda"`; `"Leibovits Magda"`; `"Leibovitz Magda"`; `"Lebovitz Magda"`; `"Lebowitz Magda"`; `"Leibowitz Magda"` | phrase; 1944–1952 | 0; 0; 0; 0; 0; 0 | – | none |
| Q-181 | `"Lebovics Joszéf"` | phrase; 1944–1952 | 1 | 1949-12-29 | ujk19491229-01.2.6 → B-6 |
| Q-182 | `"Lebovics József"` | phrase; 1944–1952 | 0 | – | none |
| Q-183 | `Lebovics` | token; 1944–1952 | 19 | 1944-03-02 – 1951-06-07 | exploratory: 19 hits (1 hidden PAGE hit); read: lakkarov19450712-01.2.13, ujk19491229-01.2.6, ujk19510607-01.2.11.1 → B-6, C-8; the other 15 unread (E) |
| Q-184 | `Lebovits` | token; 1944–1952 | 74 | listed 40 of 74: 1945-07-05 – 1949-10-23; all hits by year (facets): 1945–1952 | exploratory: 74 hits, 40 listed (date order, up to 23.10.1949; 3 PAGE hits among the 74); 6 of the listed read (C-8); the rest unread (E) |
| Q-185 | `Lebovits Balassagyarmat` | AND; 1944–1952 | 3 | 1945-11-22 – 1946-05-30 | co-occurrence: lakkarov19451122-01.2.24 (B-6), lakkarov19451206-01.2.21, lakkarov19460530-01.2.6 (C-8): no Lebovits from Balassagyarmat |
| Q-186, Q-187 | `Lebovics Balassagyarmat`; `Leibovits Balassagyarmat` | AND; 1944–1952 | 0; 0 | – | none |
| Q-188–191 | `"Lebovits Maria"`; `"Lebovics Maria"`; `"Lebovits Miriam"`; `"Lebovics Miriam"` | phrase; 1944–1952 | 0; 0; 0; 0 | – | none |
| Q-192 | `"Lebovits Eszter"` | phrase; 1944–1952 | 1 | 1945-10-18 | lakkarov19451018-01.2.16 (Hafkrug) → C-8 |
| Q-193–196 | `"Lebovics Eszter"`; `"Lebovits Nehama"`; `"Lebovics Mor"`; `"Lebovits Mor"` | phrase; 1944–1952 | 0; 0; 0; 0 | – | none |
| Q-197 | `Blumenthal` | token; 1944–1952; Uj Kelet only | 15 | 1949-04-12 – 1952-03-18 | 15 ujk hits; 8 read (C-8); 7 unread (E) |
| Q-198 | `Lebovits Tikva` | AND; 1944–1952; Uj Kelet only | 3 | 1949-12-23 – 1951-03-07 | 3 hits; 2 read (C-8), 1 hidden PAGE hit |
| Q-199 | `Lebovics Tikva` | AND; 1944–1952; Uj Kelet only | 1 | 1951-06-07 | ujk19510607-01.2.11.1 → C-8 |
| Q-200 | `Blumenthal Tikva` | AND; 1944–1952; Uj Kelet only | 0 | – | none |
| Q-201 | `Izrael` | token; all dates; Uj Kelet only | 18964 | listed 1 of 18,964: 1918-12-19 (first); top years: 1949 (1,229), 1974 (981), 1976 (934), 1977 (838), 1970 (706), 1953 (693), 1950 (641) | coverage: 18,964 sections, of which 13,227 are PAGE-type; first ujk19181219-01.2.29; 1949: 1,229; 1950: 641 |
| Q-202 | `Izrael` | token; all dates; Uj Kelet only | 18964 | listed 0 (the first hit in descending order is a hidden PAGE hit) | coverage (descending order): same totals |
| Q-203 | `Balassagyarmat` | token; 1944–1952 | 14 | listed 4 of 14: 1944-03-02 – 1949-06-23; all hits by year (facets): 1944–1951 | page 2 of Q-169: 3 more ids (ujk19490301-01.2.21, ujk19490623-01.2.22, egy19440302-01.2.9; all read) + 1 hidden PAGE hit → C-8 |
| Q-204 | `Lebovits Gyarmat` | AND; 1944–1952 | 1 | 1945-07-05 | lakkarov19450705-01.2.10 not read (survivors in Slovakia) |
| Q-205 | `Lebovics Gyarmat` | AND; 1944–1952 | 0 | – | none |
| Q-206, Q-207 | `"Lebovits Magdolna"`; `"Lebovics Magdolna"` | phrase; 1944–1952 | 0; 0 | – | none |
| Q-208 | `Nograd` | token; 1944–1952 | 7 | 1944-12-10 – 1951-06-14 | 7 hits, foreign press and Lakrov Sweden lists; not read (E) |
| Q-209 | `Blumenthal Jenő` | AND; 1944–1952 | 2 | 1951-12-13 – 1952-03-05 | ujk19511213-01.2.13, ujk19520305-01.2.28 → C-8 (arrival/tracing lists; no Jenő Blumenthal) |
| Q-210–213 | `"Blumenthal Ignác"`; `"Blumenthal József"`; `"Blumenthal Miklós"`; `"Blumenthal Gyula"` | phrase; 1944–1952 | 0; 0; 0; 0 | – | none |
| Q-214 | `"Blumenthal Jakob"` | phrase; 1944–1952 | 1 | 1945-08-23 | lakkarov19450823-01.2.21 → C-8 (Kowno, 1916: Lithuanian) |
| Q-215 | `"Blumenthal Jaakov"` | phrase; 1944–1952 | 0 | – | none |
| Q-216 | `Blumenthal Nograd` | AND; 1944–1952 | 0 | – | none |
| Q-217 | `Bercel` | token; 1944–1952 | 4 | 1945-07-12 – 1950-05-26 | 4 hits: lakkarov19450712-01.2.14 read (given name Bercel, Kovno list); 3 foreign-press items not read |
| Q-218 | `Blumenthal Bercel` | AND; 1944–1952 | 1 | 1949-04-01 | bbh19490401-01.2.36.2 not read |
| Q-234–249 | `"Lebovits Mózes"`; `"Lebovics Mózes"`; `"Lebovits Moshe"`; `"Lebovics Moshe"`; `"Lebovits Mose"`; `"Lebovics Mose"`; `"Magda Lebovits"`; `"Magda Lebovics"`; `"Magda Leibovits"`; `"Magda Leibovitz"`; `"Magda Lebowitz"`; `"Miriam Lebovits"`; `"Miriam Lebovics"`; `"Miriam Leibovitz"`; `"Mirjam Lebovits"`; `"Lebovits Mirjam"` | phrase; 1944–1952 | 0 each (16 queries) | – | none |

## B. Flagged findings: could be Miriam, Magda, Yaakov or their siblings

### B-1. `hzh19481008-01.2.64` — the registration of Yaakov and Miriam (NEW; near-certain)
- **Where.** HaTsofeh, Tel Aviv, 8.10.1948, 165 words; column "נרשמו לנשואין בירושלים" (OCR "נרשמוי ן לנשוא ב ירושל ים"); block "נרשמו לנשואין אצל הרבנות הראשית בפתח תקווה".
- **OCR, couple 1.** `יעקב בן משה _בלומנטאל — עין _גגים פ"ת צרים בת משה ליבוביץ — _פתח־תקווד.`
- **OCR, couple 2 (same block).** `יהודה בן אברהם פרינקל . אי שמ אסתר בה משד, ליבובי`
- **Reading.** Format "FIRST בן/בת FATHER SURNAME — residence". Yaakov son of Moshe Blumenthal, residence Ein Ganim, Petah Tikva ("_גגים" is גנים), registers with "צרים" (OCR for מרים), daughter of Moshe Leibovitz, Petah Tikva. Couple 2: Yehuda son of Avraham Frenkel, residence "אי שם" (the soldier's residence; it belongs to this groom, not to Yaakov), and Esther ("בה" is בת, "משד" is משה, the surname is cut at "ליבובי"), daughter of Moshe L[eibovitz], Petah Tikva (the closing line reads "פתח־תקווה").
- **What it adds.** (a) A printed registration 19 days before the wedding date on the certificate (27.10.1948), at the same rabbinate. (b) Both fathers are named Moshe, as on the certificate; the epithets "הלוי" and "בן ציון" are not printed. (c) Yaakov's residence is Ein Ganim, Petah Tikva, the neighbourhood of his brother Yitzhak (Ein Ganim 49 in the voters' list of 1949; Yaakov report 4.3); the certificate gives "אי שם", a soldier's residence, so the two sources differ and the notice shows the home address. (d) A second bride, Esther bat Moshe Leibovitz, registers in the same block on the same day: a lead for a sister (B-3). Not added: ages, occupations, origin, mothers' names.
- **Grade.** Text מאומת. That the couple is the certificate couple: **כמעט ודאי** (given names, fathers' names, rabbinate, city and date window agree; no printed age contradicts). That Esther is Miriam's sister: **ככל הנראה** (טעון אימות).
- **Found by.** Q-84, Q-136, Q-134, Q-83, Q-76, Q-72, Q-137. Missed by every adjacency query of the form `"מרים ליבוביץ"` (Q-1, Q-4) and `"יעקב בלומנטל"` (Q-43 to Q-46) because the list prints בן/בת and the father's name between the names.

### B-2. `hzh19520821-01.2.56` — Yehuda Blumenthal, son of Moshe Ben-Zion (NEW; near-certain for the family)
- **Where.** HaTsofeh, 21.8.1952, 427 words; the block of registrations at the Petah Tikva rabbinate (OCR heading "־כמשדדיהדכנות פתה. תקוה").
- **OCR.** `יהודה 'בלומנטל בן משה בן ציון. י רוק, פ יי ת!עטרה י קרינדל בת שלמה שלזינגר`
- **Reading.** Yehuda Blumenthal, son of Moshe Ben-Zion, bachelor ("רוק"), Petah Tikva ("פ יי ת"), registers to marry Atara Krindel, daughter of Shlomo Schlesinger, spinster, residence "חזורעים" as printed.
- **What it adds.** The patronymic "משה בן ציון", the form on Yaakov's certificate, printed for a Yehuda of Petah Tikva in August 1952: the brother Yehuda of the witness pages (1956, Petah Tikva); a marriage date (registration 21.8.1952) and a wife's name. It does not name Yaakov.
- **Grade.** Text מאומת. That this Yehuda is Yaakov's brother: **כמעט ודאי** (a rare double patronymic with the same surname, Petah Tikva, a brother of that name in the project; no age printed).
- **Found by.** Q-57, Q-60, Q-62, Q-79.

### B-3. `lakkarov19460822-01.2.2` — Nechama (21) and Esther (28), children of Moshe and "Frimam", Hungary (NEW; probable as to the family)
- **Where.** Lakrov Velarahok 22.8.1946, "מעפילי 'החייל העברי' ו'הגנה' שהועברו למחנה עתלית" (4,453 words). One alphabetical list "surname, first name, age, parents (father mother), country letter" (ה Hungary, ר Romania). The text is truncated in the מ-block (letters נ–ת absent); the Next id is a relatives list, so the continuation was not located.
- **OCR.** `לייבוביץ נחמה 21 משה פרימאם ה לייבוביץ אסתר 28 משה פרימאם ה ליבוביץ דויד 20 משה בארסה ר`
- **Reading.** Nechama, 21, and Esther, 28, children of Moshe and a mother printed "פרימאם", from Hungary. The third entry (David, 20, Moshe and "בארסה", Romania) is another family, adjacent only by the alphabet.
- **What it adds.** (a) The same two first names as the certificate's parents, Moshe and Frimet ("פרימט"; the Yad Vashem pages of 1957 print it "Fri'ma"). (b) Hungary. (c) Two daughters unknown to the project. (d) An Esther bat Moshe Leibovitz of Petah Tikva registers with Miriam in B-1. (e) If both are children of the Balassagyarmat couple: the children the project names (Avraham Aharon, Shimon, Manó, Magda, Lili; Rose of Budapest is only a possible sister) are five, and with Esther and Nechama seven; the Yad Vashem pages say seven (1957) and eight (2000).
- **Not on this list.** Miriam and Magda: the ל-block is present in the fetched text (12 Leibovitz entries and one garbled "לבובה") and has neither.
- **Readings.** (i) Esther and Nechama are Miriam's sisters. (ii) Nechama is Miriam under another given name (b. 1924/25 against the voters' list 1925 and the certificate's 22 in October 1948, i.e. 1925/26). (iii) An unrelated family of Moshe and Frima: the weakest, because the phrase `"משה פרימאם"` finds only this section in 1944–1952.
- **Grade.** Text מאומת. That Esther and Nechama are children of the project's Moshe and Frimet: **ככל הנראה**. That the Esther of this list is the Esther of B-1: **אפשר ש… (טעון אימות)**. That Nechama is Miriam: **אפשר ש… (טעון אימות)**.
- **Found by.** Q-138, Q-140, Q-142; co-occurrence in Q-106 and Q-108. Missed by `"לייבוביץ מרים"` because Miriam is not on the list.

### B-4. `lakkarov19460519-01.2.3` — "לייבו מרים 1925" on the Max Nordau list (NEW; possible)
- **Where.** Lakrov 19.5.1946, "הוצאה מיוחדת" (3,543 words): letters ה–ש of the list of the 1,754 ma'apilim of "Max Nordau" (Smyrna), collected in Romania, left Constanța 7.5.1946, entered Haifa 14.5.1946 (page 1 of the list: `lakkarov19460519-01.2.2`). Entries give surname, first name and birth year or age; no parents, no country letter.
- **OCR.** `לאבל טובה •״ 1923 לייבו מרים 1925 לייבו לבגד, 1930 לאזר יואל 1919`
- **Also in the section.** `לייבוביץ טאגדו 1924 י` ("טאגדו" is the OCR of מאגדה) and `לייבוביץ מרים י 1932` (a child b. 1932 in a family with children b. 1931 and 1939).
- **Reading.** A Miriam b. 1925 whose surname is cut to "לייבו" (the next entry, "לבגד" b. 1930, has the same cut). The cut is why the phrase `"לייבוביץ מרים"` misses her; `"לייבו מרים"` (Q-219) finds only this section.
- **Circumstantial item.** `hegeh19460701-01.2.35` (HaGeh, 1.7.1946): letters waiting at the Hitachdut Olei Romania, Tel Aviv: `…ליבוביץ שמואל דוד; … ליבוביץ מרים; פרידמן אברהם…` (names only), six weeks after the Max Nordau landing.
- **Why it matters, and why it is weak.** Year 1925 equals the voters' list. Against: the voyage started in Romania, there are no parents and no country, and the "Magda 1924" of the same section is probably the Magda b. 30.12.1924 of Bătarci already excluded in the project (`../arolsen/lebowicz_magda_1924_postwar/`), not the Magda b. 20.1.1922.
- **Grade.** Text מאומת. That this Miriam is our Miriam: **אפשר ש… (טעון אימות)**.

### B-5. Michael Blumenthal in two Lakrov sections, January–February 1947 (NEW; possible)
- **`lakkarov19470109-01.2.3`** (9.1.1947, "עולי קפריסין שהגיעו בעתלית", 617 words, names only, two per printed row). OCR: `בארקוביצ׳י יצחק; בלומנטאל מיכאל ד בראון ישעיהו;` A Michael Blumenthal among the Cyprus arrivals at Atlit.
- **`lakkarov19470206-01.2.3`** (6.2.1947, "פנה למדור לחיפוש קרובים בחיפה"; entries "name (seeker) file-no."). OCR: `בלומנטאל איגנאץ־יאנו (מיכאל בלומנטאל) 4868` Michael Blumenthal seeks "Ignác-Jenő Blumenthal" (file 4868).
- **Reading.** The Hungarian forms Ignác and Jenő; the hyphen joins two given names and the index treats it as one token. Neither entry gives a father, a town or an age.
- **Why it matters.** The Nógrád archive book lists Ignác (b. 1919, "probably settled in Israel after the war"), Jenő (b. 1922, survived, crossed the border 23.5.1945) and Miklós (b. 1926), whom the book identifies with the "Michael" of the witness page (Yaakov report 4.8). The two entries are four weeks apart.
- **Grade.** Text מאומת. That the Michael of these entries is Yaakov's brother and "Ignác-Jenő" one or two of the Nógrád brothers: **אפשר ש… (טעון אימות)** (names only; Blumenthal is common).
- **Found by.** Q-93, Q-100, Q-101, Q-102; Q-254 is an adjacency artefact on the same section.

### B-6. Magda candidates in the Hungarian lists (NEW; weak or pointing away)
| Section | OCR | Reading | Grade |
|---|---|---|---|
| `lakkarov19451122-01.2.24` (22.11.1945, "WALDHAUS 2", Hungarian women, Latin script, 491 words) | `LEBOVITS Iren 1925, Galocas LEBOVITS Magda 1924, Budapest LEHRER Edit 1928` | A Magda b. 1924 of Budapest among surviving women; the same list has "HEKS Ferencne 1918, Balassagyarmat", which is why the town query matched | **אפשר ש… (טעון אימות)**, weak: 1924 against 20.1.1922; Budapest fits the Budapest relative; no parents, no camp |
| `lakkarov19451206-01.2.27` (6.12.1945, Kaunitz) | `LEBOVITS Cecilia 1920, Marmarosdombo. LEBOVITS Magda 1927, Magyarpeterd.` | b. 1927, Magyarpéterd | **נשלל** (year and town) |
| `ujk19491229-01.2.6` (29.12.1949, Hitachdut Olei Hungaria notice, 415 words) | `2. Lebovics Joszéf Jenő. Bászisz Imunim 3 (Lebovits Magda 292)` | Persons in Israel are called to the Tel Aviv district office of the Aliyah Ministry about a file for a relative in Hungary; in parentheses, the relative and the file number. József Jenő Lebovics (a soldier's address) is the sponsor of a "Lebovits Magda", file 292 | Points against Miriam = Magda (Miriam was married in Petah Tikva from October 1948), but this Magda may be any Lebovits Magda: **לא הוכרע** |
| HASAG-Altenburg lists, `lakkarov19450712-01.2.13` (435 names) and `lakkarov19450802-01.2.19` (245 names) | no Lebovits Magda in either | Altenburg is the Magda b. 1922's camp (Miriam report 4.2) | A name missing from a partial printed list is not a negative |

### B-7. Weak leads for Yaakov's siblings and in-laws (NEW; לא הוכרע)
| Section | OCR | Reading | Why weak |
|---|---|---|---|
| `hzh19461224-01.2.61.1` (24.12.1946, advertisement page; block "נרשמו לנשואין אצל הרבנות הראשית בפתח תקוה") | `אהרן בן בנימין 'אב בלומנטל פתה תקרת & אלד?בת שמואל-הקש פ-תה תקוה` | Aharon son of Binyamin [Ze'ev?] Blumenthal, Petah Tikva (the stray "'אב" may be a damaged "זאב"); the same block lists residents of Ein Ganim | No Aharon among the twelve names of the archive book; "Binyamin" is the Hebrew counterpart of "Benő", the civil name of the Nógrád father, but every other record prints "Moshe" |
| `hzh19460808-01.2.30` (8.8.1946, Tel Aviv list) | `יונה בת משה בלומנטאל ת"א` | Yona daughter of Moshe Blumenthal, Tel Aviv, bride | Tel Aviv; no Yona among the twelve names |
| `hzh19480909-01.2.10` (9.9.1948, news) | `החיילים אליעזר בלומנטאל ושמעון מנהיים שנתמנו על ידי קצין הדת החטיבתי לשמור על כשרות המטבח` | Eliezer Blumenthal, a soldier of a religious company of the Alexandroni Brigade, refusing to cook on the Sabbath | A soldier's name only; no Eliezer among the twelve |
| Gombo: `lakkarov19460822-01.2.2` | `גרינבוים יוכבד 22 יוסף יהודית ר גומבו חיה 20 אליעזר פריידל ה` | Gombo Haya, 20, parents Eliezer and Freidel, Hungary (the Atlit list of B-3) | Rivka Gombo is Yaakov's sister; no link between the two Gombo records and the Blumenthals |
| Gombo: `hzh19500214-01.2.37` (14.2.1950) | `זהבה בת אליעזר גומבו פתה הקוה` | Zehava daughter of Eliezer Gombo, Petah Tikva, bride (registration at the Petah Tikva rabbinate) | same |
| Gombo: `hzh19520610-01.2.76` (10.6.1952) | `גומבו ?'חיים ?בן ; עמנואל מנחם( -'רוק) הונגרקה—חיפה` | Haim son of Emanuel Menachem Gombo, bachelor, Hungary, Haifa | same |

### B-8. Weak leads in the surname Leibovitz: other children of a Moshe Leibovitz, 1950–1952 (NEW; לא הוכרע)
| Section | OCR | Reading | Grade |
|---|---|---|---|
| `hzh19511203-01.2.40` (3.12.1951; the first block of the list is headed "בפתח תקווה") | `רבקה בת משה ליבוביץ רוקה בצבא` | Rivka daughter of Moshe Leibovitz, spinster, residence "בצבא" (the army); groom `משה ב!פסוו גצל פ"ת רוק`; no origin | A younger sister is possible; Moshe Leibovitz is a common name; **לא הוכרע** |
| `hzh19520727-01.2.35` (27.7.1952; registered at the rabbi of Givat Shmuel) | `רחל בת משה ליבוביץ, פרדס רוזנבלום` | Rachel daughter of Moshe Leibovitz, residence as printed | same |
| `hzh19500810-01.2.45` (10.8.1950; heading "בחיפה") | `יוסף בן משה לייבוביץ - שרה בת אליעזר שילר` | Yosef son of Moshe Leibovitz, no origin | same |
| `hzh19520708-01.2.51` (8.7.1952, Haifa) | `לייבו צירלה בת משה לייבוביץ' אלמנה, רומניה' יחפה` | Tzirla, widow, Romania | **נשלל** (Romania; widow) |
| `hzh19481208-01.2.44` (8.12.1948, Tel Aviv) | `יצחק בן משה ליבוביץ רומניה—בצבא` | Yitzhak son of Moshe Leibovitz, Romania, soldier | **נשלל** (Romania) |
| `hzh19490228-01.2.44` (28.2.1949, Tel Aviv) | `עליזה אליס בת פשה ליבוביץ — רומניה — בית־עולים רעננה` | Aliza Alice daughter of Moshe Leibovitz, Romania | **נשלל** (Romania) |

### B-9. Ruled out or nearly (recorded so that they are not re-opened)
| Item | OCR | Reading | Grade |
|---|---|---|---|
| `lakkarov19470414-01.2.2` (14.4.1947, "Moledet" ship list) | `לייבוביץ מאגדה 23מונקאץ׳ … לייבוביץ ריבה 26 מונקאץ … לייבוביץ מארקום 34 מונקאץ׳` | A Leibovitz cluster from Munkács; Magda, 23 | **נשלל ככל הנראה**: age 23 (b. 1923/24, not 1922) and Munkács, not Balassagyarmat |
| `hzh19470407-01.2.48` (7.4.1947, list passed on by the Aliyah department of Hapoel HaMizrahi) | `לייבוביץ יעקב, צס"ר; … לייבוביץ מוארקוס, צס"ר; … לייבוביץ עקיבא, צס"ר; … לייבובי־ץ מגדה, צס"ר` | The same cluster, country "צס"ר" (Czechoslovakia) | **נשלל ככל הנראה** |
| `lakkarov19470507-01.2.3` (7.5.1947, "Theodor Herzl") | `ליכטנשטיין אלארה 16 ה לייבוביץ מרים 19 צ לוגר טובה` | Miriam, 19, Czechoslovakia | **נשלל** (age and country) |
| `hzh19490624-01.2.99` (24.6.1949) and `hzh19510819-01.2.37` (19.8.1951) | `הנן בלומנטאל, יצחק . שרייבר, דוד שורצברג` and `חנן בן גרשון בלומנטל, רוק, פ"ת — גרמניה` | A court report naming four young men of Petah Tikva (24.6.1949); a registration of Hanan son of Gershon, from Germany (19.8.1951) | **נשלל**: the father is Gershon, origin Germany |
| `lakkarov19460519-01.2.3` (Max Nordau) | `לייבוביץ טאגדו 1924` | Magda b. 1924 | probably the Bătarci Magda already excluded (see B-4) |

## C. Hit-level classification of the other relevant-looking hits

### C-1. `"ליבוביץ מרים"` (Q-2) and `"לייבוביץ מרים"` (Q-3): 8 hits
| Query | Section id | Date, title | OCR (as printed) | Grade |
|---|---|---|---|---|
| Q-2 | `hegeh19460701-01.2.35` | HaGeh 1.7.1946, letters waiting at the Hitachdut Olei Romania | `…ליבוביץ שמואל דוד; … ליבוביץ מרים; פרידמן אברהם…` | לא הוכרע (see B-4) |
| Q-2 | `haretz19470820-01.2.49` | Haaretz 20.8.1947, nurses' graduation | `לוציה ליבוביץ, מרים ליבר` | artefact: two different women |
| Q-2 | `ytz19480129-01.2.22` | HaTsofeh LeYeladim, puzzle solvers | `שולמית ליבוביץ, מרים יודנגלובן` | artefact |
| Q-2 | `hadoar19510105-01.2.5.2` | HaDoar (New York), advertisement of teachers | `נעמי ליבוביץ, מרים פרנמאן` | artefact |
| Q-3 | `lakkarov19460131-01.2.6` | Lakrov 31.1.1946, relatives search, Tel Aviv | `לייבוביץ מרים ואריה (ל. אפשטיין, ד״ר). 43907` | לא הוכרע: a Miriam and an Arie sought by a Dr L. Epstein; no age, parents or origin |
| Q-3 | `lakkarov19460519-01.2.3` | Lakrov 19.5.1946 | `לייבוביץ מרים י 1932` | a child b. 1932; see B-4 |
| Q-3 | `lakkarov19470507-01.2.3` | Lakrov 7.5.1947, "Theodor Herzl" | `לייבוביץ מרים 19 צ` | נשלל (B-9) |
| Q-3 | `hmf19470603-01.2.31` | HaMashkif 3.6.1947 | `צפורה לייבוביץ, מרים יצרן` | artefact |

### C-2. Rose, Rozi and the Hebrew spellings of Balassagyarmat
| Query | Section id | Reading | Grade |
|---|---|---|---|
| Q-23 | `hzh19510516-01.2.47` (HaTsofeh 16.5.1951, Haifa registrations) | `ברקוביץ דוב בן מרדכי מרקו — לייבוביץ רוזה בת מאיר, חיפה` | נשלל (father Meir) |
| Q-24 | `lakkarov19470324-01.2.4` (the canary list) | `לייבוביץ רוזי, 28 לייבוביץ לייב, 30, צ׳אכיה` | other (Czechoslovakia) |
| Q-31 | `dertog19440228-01.2.47` (Der Tog, New York, 28.2.1944) | a refugee notice in Yiddish with "גיארמאט, אוננארן" | irrelevant |
| Q-35 | `momenturuguay19490930-01.2.16` (Der Moment, Montevideo, 30.9.1949) | a list of Hungarian rabbis: `דייטש חיים אהרן דוד, באלשאדיארמאט`; `ווייס נתן, באלאשאדיארמאט` | irrelevant (rabbis) |
| Q-33 | `khm19491215-01.2.25` | not opened (title: a workers' council item) | noise |
| Q-32, Q-34 | 87 hits for `ג'רמט` / `גרמט` | the apostrophe splits the token; not read | unverified noise |

### C-3. Yaakov Blumenthal: 16 hits of Q-43, Q-44, Q-46
| Section id | Date, title | OCR | Grade |
|---|---|---|---|
| `hmf19440710-01.2.50`, `haretz19440711-01.2.20` | list of about 282 persons exchanged for Germans, arrival 10.7.1944 | `בלומנטל יעקב, בלומנטל־הכט קלדה …` | other (German/Dutch exchange group) |
| `hzh19450207-01.2.33`, `dav19450218-01.2.33`, `hmf19450205-01.2.31` | lists of Lithuanian survivors | `בלומנטל יעקב, בלומנטל זינאידה` | other (Lithuanian) |
| `ahr19450419-01.2.35`, `hzh19450424-01.2.35` | Vilna survivors | `בלאכר יעקב, בלומנטל דבורה` | artefact (adjacent names) |
| `ydv19460425-01.2.12` | a child's donation | `יעקב בלומנטל (תל־אביב), לרגל הולדתו ה־7` | other (a child) |
| `ahr19461028-01.2.19`, `hmf19461029-01.2.65` | relatives of Rafiah detainees | `ברוך יעקב בלומנטל, ירושלים, בתי האתגרים 180` | other (Jerusalem) |
| `dav19500907-01.2.3`, `hbkr19500907-01.2.10`, `khm19500907-01.2.18.3`, `ahr19500907-01.2.22.1` | re-burial on Mount Herzl, 10.9.1950 | `…בכר יעקב. בלומנטל דוד. בלומנטל ישראל…` | artefact (adjacent names in a list of the fallen) |
| `lakkarov19460110-01.2.15` | letters to Mauritius returnees | `בלום יעקב בלומנטאל יושד` | artefact (Blum Yaakov; Blumenthal Yosha) |

### C-4. Brothers' names and later "Blumenthal" registrations (Q-49, Q-53, Q-54, Q-57, Q-150, Q-154)
| Section id | Reading | Grade |
|---|---|---|
| `haretz19491127-01.2.37` | Administrator General notice, estates of the Haifa district court: `20) בלומנטל יוסף` | other |
| `hzh19460815-01.2.54` | `נפתלי בן יוסף בלומנטל — יהודית בת יצחק ריזברג, נשר־יגור` | other |
| `hzh19501002-01.2.56` | `יהונתן בן יצחק בלומנטל גרמניה — ת"א` | other (Germany) |
| `hmf19470630-01.2.24` | `יהודה בלומנטל מירושלים יצא מביתו ולא חזר` | other |
| `hzh19490209-01.2.28` | `אריה ליב בן יהודה בלומנטל — ולוצלבק — בצבא`; `רחל בת הירש בלומנטל — ברסלאו` | other |
| `hbkr19511016-01.2.45` | a Jerusalem hotel clerk, Yehuda Blumenthal | other |
| `hzh19501108-01.2.34.2` | an advertisement naming a widow Blumenthal, Rishon LeZion | other |
| `hzh19510418-01.2.56`, `hzh19510626-01.2.50` | Haifa: `בלומנטל קרולינה בת מאיר (גרושה)`; `בלומנטל חוה בת פנחס` | other |
| `hzh19520115-01.2.51`, `hzh19521114-01.2.69` | a Tel Aviv liquor-licence notice (`בלומנטל מאיר`); Rabbi Elchanan Blumenthal of South Africa | other |

### C-5. HaTsofeh lists of 1948–1951 that were read, and co-occurrence artefacts
- `hzh19480928-01.2.59` (28.9.1948, Tel Aviv list with a block "אצל הרבנות הראשית בפתח תקווה"): other couples; no Blumenthal, no Leibovitz.
- `hzh19481111-01.2.39`: `לאה בת אברהם ליבוביץ — רמת השרון`; `hzh19481122-01.2.30`: `אברהם בן נתן ליבוביץ' בוקרשט—יפו`; `hzh19481212-01.2.33`: `זליגה ליבוביץ חיפה`: other persons.
- Q-135, the other seven hits of `בלומנטאל` in Sep–Dec 1948: `ahr19480903-01.2.18` (a psychiatrist, Dr K. Blumenthal, as a court witness); `hzh19480923-01.2.37` and `dav19480923-01.2.29` (A. Blumenthal, representative of the greengrocers); `hzh19480908-01.2.42` (a list of the fallen: `בלומנטאל שלמה ב־20.4.48 (זרעין)`); `hadoar19481119-01.2.8` (a contributor to a column of jokes); `hadoar19481231-01.2.33` (Rabbi Aharon Blumenthal, New York); and `hzh19480909-01.2.10` (B-7).
- Co-occurrence artefacts of Q-157 and Q-159 ("נחמה בת משה" or "אסתר בת משה" in a list that also holds a Leibovitz of another family): `hzh19490228-01.2.44`, `hzh19500424-01.2.34`, `hzh19500531-01.2.49`, `hzh19490909-01.2.54`, `hzh19500113-01.2.60`, `hzh19500205-01.2.51`, `hzh19500412-01.2.52`, `hzh19511121-01.2.54`.

### C-6. `"משה ליבוביץ"` (29 hits, Q-225) and `"משה לייבוביץ"` (12 hits, Q-226): all 41 classified
| Group | Sections | Reading |
|---|---|---|
| The New York Hebrew children's poet Moshe Leibovitz (d. 1949) | hadoar: `19440407-01.2.18`, `19440505-01.2.19`, `19440505-01.2.29`, `19440519-01.2.15`, `19440519-01.2.18`, `19440519-01.2.33`, `19440609-01.2.19`, `19461004-01.2.44`, `19480305-01.2.18`, `19491118-01.2.8`, `19491202-01.2.32`; ydv: `19450919-01.2.3`, `19460912-01.2.14`, `19490920-01.2.15`, `19500607-01.2.20`; haretz: `19450511-01.2.45`, `19450821-01.2.25` | irrelevant: book reviews, poem credits, a memorial notice |
| Rabbi Yaakov Moshe Leibovitz, Kamenitz yeshiva | `kolisraeljlm19440917-01.2.19`, `kolisraeljlm19450907-01.2.13`, `hamevaserjlm19490922-01.2.10`, `hzh19440721-01.2.51` | irrelevant (an appeal for the yeshiva) |
| Adjacency artefacts (surname-first lists) | `lakkarov19451101-01.2.19`, `lakkarov19470324-01.2.8`, `hrt19490426-01.2.52`, `hrt19490428-01.2.40`, `hrt19490429-01.2.67`, `dav19490617-01.2.84` | artefacts |
| Other men named Moshe Leibovitz | `yomyom19490512-01.2.16` (a joke), `dav19460211-01.2.39.5` (board of a cooperative settlement group, 6.2.1946), `dav19461020-01.2.8` (a man of 22 killed by an army vehicle, Tel Aviv, 20.10.1946), `ahr19490822-01.2.47` (a committee of immigrant-camp workers), `ahr19520706-01.2.38` (death notice, 69, secretary of the association of immigrants from Latvia and Estonia), `lakkarov19460530-01.2.5` (a sender of radio greetings), `lakkarov19470123-01.2.6` (`וייסמאן גיטלה (אביה משה לייבוביץ׳) 85628`) | other persons |
| Registration lists | `hzh19481008-01.2.64` (B-1), `hzh19481208-01.2.44`, `hzh19511127-01.2.53` (a groom `משה ליבוביץ בן יעקב שלמה`, Poland, Tel Aviv), `hzh19511203-01.2.40`, `hzh19520727-01.2.35`, `hzh19520708-01.2.51`, `hzh19500810-01.2.45` | see B-8 |

### C-7. HaTsofeh sections with Blumenthal (Q-258, Q-259, Q-266): 137 sections, all read
Marriage-list occurrences (22 sections), apart from B-1, B-2 and B-7: `hzh19440323-01.2.51` (`ליורה בת וילי בלומנטל, רעננה`); `hzh19440830-01.2.52` (`עזריאל זליג בן שמעון בלומנטל ת"א`); `hzh19460708-01.2.45` (`אבינועם בלומנטל — ירושלפ`); `hzh19460815-01.2.54` (see C-4); `hzh19470625-01.2.53` (`הוזה בת יואל בלומנטאל שטטין גרמניא — בני ברק`); `hzh19470731-01.2.54` (`יופפינא בת אמיל בלומנטל, לפברג, ת"א`); `hzh19480112-01.2.44` (`יצחק אייזיק בן יהודה יודל בלומנטל ליבוי, לטביא—ת"א`); `hzh19480518-01.2.71` (`אדלה בלומנטל, קרית־מוצקין`); `hzh19480831-01.2.32` (Jerusalem); `hzh19490209-01.2.28`, `hzh19501002-01.2.56`, `hzh19510418-01.2.56`, `hzh19510626-01.2.50` (C-4); `hzh19490729-01.2.57` (`חוה בת אוסקר בלומנטל הנובר—ת"א`); `hzh19510422-01.2.55` (Haifa, `בלומנטל … רבקה בת הירש`); `hzh19510819-01.2.37` (Hanan son of Gershon, B-9); `hzh19520425-01.2.68` (`אגנס בלומנטל בת אנדרם רוקה הונגריה—ת"א`); `hzh19520506-01.2.50` (`בלומנטאל גרשון ג'ורג' בן מאקס גרוש אנגליה חיפה`). None is a son or daughter of a Moshe Blumenthal of Petah Tikva other than B-1 and B-2.
The other 115 sections are not about a possible relative: the private psychiatric hospital of Dr Blumenthal on Mount Carmel, Haifa (strikes, incidents, 1944–1952); the Zion Blumenthal orphanage in Jerusalem (appeals, 1944–1947); lectures and broadcasts by Dr P. Blumenthal (Hapoel HaMizrahi culture centre, adult education, radio, 1944–1952); Tel Aviv liquor-licence notices (Meir and Nachman Blumenthal); court reports (Mr Blumenthal, editor of a German-language bulletin, 1944; Dr Blumenthal's testimony in the 1951 Tripus trial); survivor lists (Kovno, Vilna, Lithuania, Frankfurt, Poland); books received (Nachman Blumenthal's dictionary, 1947; Israel Chaim Blumenthal); a greengrocers' representative, A. Blumenthal (1945, 1948, 1952).

### C-8. Latin script and Uj Kelet: hits read
| Section id | Reading | Grade |
|---|---|---|
| `ujk19491209-01.2.42.1` | engagement notice: `Weisz Edith (Balassagyarmat) Petach-Tikva — Nicolás Fischer (Tunis) Akkó` | other |
| `ujk19510216-01.2.26.2` | marriage notice, Haifa 13.2.1951: `STINER VERA Budapest — Sándor László Balassagyarmat` | other |
| `ujk19510323-01.2.57.1`, `ujk19511123-01.2.16.1` | engagement notices: `Kohn Chaim E. (Ede) (Balassagyarmat) — Breier Elisa (Wien)`; `Deutsch Volvi Balassagyarmat — Chicago` | other |
| `ujk19490303-01.2.17`, `ujk19490301-01.2.21`, `ujk19490623-01.2.22` | Hitachdut Olei Hungaria tracing lists: `Itzkovics Balassagyarmat`; `Weisz Salamon Sándor Balassagyarmat` | other |
| `egy19440302-01.2.9` | Budapest, 2.3.1944, relatives of forced-labour men: `Domonyi László, Balassagyarmat, 1910` | other |
| `ujk19491223-01.2.35.1`, `ujk19510307-01.2.26.4`, `ujk19510607-01.2.11.1` | advertisements: a Tel Aviv Lebovits seeking a bookbinding partner; `Szabadi Magdát keresi Lebovits Kató (Ben Satomné), Safed`; `Lebovics Jákob, Cfát` (a carriage) | other |
| `ujk` Blumenthal (8 of 15 read) | `Blumenthal Jechiel, Kfar Saba` (a lost pram); `Blumenthal Emanuel` (Czech emigrants); `Blumenthal Zoltán` (death notice); `Dávid Blumenthal őrmester`; `Keresem dr. Blumenthal fogorvost és fiát, Danit`; a glove factory; `Blunienthal Andrásné, Ágnes, Blumenthal Ernő, Ernőné, Iván, Anikó` (arrivals, 13.12.1951); `Blumenthal Andorné Budapest` (5.3.1952) | other; no Jenő Blumenthal in Q-209 |
| Lakrov Latin lists | see D-2 | other |

## D. Lakrov scan audit

### D-1. Sixty-six Lakrov sections scanned by delegated passes
Each pass opened with a known-answer control (all found). Counts are tokens beginning with בלומנט, בלומענט, בלומינט (A) and ליבוב, לייבוב, לבוב, לאבוב, לעבוב, לייבאוב, ליבאוב, and standalone לייבו or ליבו (B); "לבוב" is mostly the town Lvov.
| # | Section id | Date | Title (as printed) | Blumenthal-type | Leibovitz-type | Note |
|---|---|---|---|---|---|---|
| 1 | lakkarov19470206-01.2.3 | 6.2.1947 | פנה למדור לחיפוש קרובים בחיפה | 2 (1 entry) | 1 | A = B-5 (control found: "בלומנטאל איגנאץ־יאנו (מיכאל בלומנטאל) 4868"); B = a seeker, "וולף בהלה (וולף לייבוביץ) 4881" |
| 2 | lakkarov19461127-01.2.2 | 27.11.1946 | מעפילי "לטרון" שהוגלו לקפריסין | 1 | 3 | A: "בלומנטהאל גראטה, מדאנציג (חבר)", Greta of Danzig; B: Leibovitz Isidor, Pasha; plus "לבוב" as a town |
| 3 | lakkarov19461127-01.2.3 | 27.11.1946 | מעפילי "כנסת ישראל" בחוף המולדת | 0 | 0 | prose, 72 words |
| 4 | lakkarov19461127-01.2.4 | 27.11.1946 | גולי קפריסין הנמצאים במחנה 62 | 0 | 5 | four Leibovitz entries b. 1926–27 (Avraham, Imra, Zuzo, Clara; parents given for the first three), one "לבוב"; no Miriam, no Magda |
| 5 | lakkarov19461211-01.2.2 | 11.12.1946 | 750 גולי קפריסין שהוחזרו ארצה | 0 | 3 | Dolf 30, Haim 26, "דה ליבו"; near-variants "ייבוביץ רשקה, 28, 8." and "לייבוכיץ שרלוטה, 18, ר." not counted |
| 6 | lakkarov19461225-01.2.2 | 25.12.1946 | גולי קפריסין דורשים בשלום קרוביהם | 0 | 6 words / 4 entries | seekers and sought persons (Tzeza of Netanya, Shmuel of Haifa, Uriel, Silva); no Miriam, no Magda |
| 7 | lakkarov19470109-01.2.2 | 9.1.1947 | גולי קפריסין דורשים בשלום קרוביהם | 0 | 1 | "לייבוביץ גיטל, ת״א, חבר המורים" |
| 8 | lakkarov19470123-01.2.2 | 23.1.1947 | חוזרי קפריסין שהועברו לקרית שמואל | 0 | 1 | "לייבוביץ ראגינה" |
| 9 | lakkarov19470220-01.2.2 | 20.2.1947 | 798 גולי קפריסין שהוחזרו ארצה | 1 | 3 | A: "בלומנטאל ראגאטה" (female); near-variants "בלימנטאל מאשה", "בלומנץ רוזה", "בלומאלם שרה"; B: Arie, Martin, Yeshayahu |
| 10 | lakkarov19470220-01.2.3 | 20.2.1947 | מעפילי "לנגב" ו"המעפיל האלמוני" גורשו לקפריסין | 0 | 0 | prose, 306 words |
| 11 | lakkarov19470220-01.2.6 | 20.2.1947 | חוזרי קפריסין שהועברו לקרית שמואל | 0 | 1 | "לייבוביצי ודלף" |
| 12 | lakkarov19460519-01.2.3 | 19.5.1946 | הוצאה מיוחדת (Max Nordau, letters ה–ש) | 0 | 13 | B-4 (control found: "לייבוביץ מרים י 1932", "לייבוביץ טאגדו 1924", "לייבו מרים 1925") |
| 13 | lakkarov19460124-01.2.2 | 24.1.1946 | 910 המעפילים ב"אנציו סרני" | 0 | 1 | "לייבוביץ רבקה 20" |
| 14 | lakkarov19460328-01.2.2 | 28.3.1946 | המעפילים באניה "וינגייט" | 0 | 2 | "לייבוביץ ברוך, 28, ה"; "פנחסוביץ־לייבוביץ רוזה" |
| 15 | lakkarov19460331-01.2.2 | 31.3.1946 | 733 מעפילי "תל־חי" | 0 | 0 | truncated at the letter ו ("המשך מעבר לדף"): no ל names present |
| 16 | lakkarov19460331-01.2.3 | 31.3.1946 | הגיעו 731 המעפילים | 0 | 1 | a seeker: "בן דודו בן־ציון לייבוביץ׳" |
| 17 | lakkarov19460411-01.2.6 | 11.4.1946 | מעפילי וינגייט ותל־חי מחפשים קרוביהם | 0 | 0 |  |
| 18 | lakkarov19460613-01.2.6 | 13.6.1946 | 466 המעפילים באניה "חביבה רייק" | 0 | 0 | Latin-script list: Hebrew prefixes cannot match; Latin look-alike "Mordohai Lcbovits, Moche Sara, Krosna" not counted |
| 19 | lakkarov19460702-01.2.2 | 2.7.1946 | המעפילים באניה "יאשיה וודג׳ווד" | 0 | 8 | 4 surname hits (Moshe 1915 father Mendel; Leib 1919; Tovia 1923; Fania 1915) + 4 "לבוב"; no Miriam, no Magda |
| 20 | lakkarov19460702-01.2.9 | 2.7.1946 | רשימה נוספת (בלי פרטים) | 0 | 1 | "לייבוביץ מאניה" |
| 21 | lakkarov19460710-01.2.2 | 10.7.1946 | מעפילי "בידיה" מועברים לעתלית | 0 | 6 | 5 surname hits (Yitzhak 33 צ׳, Yehuda 29 ר, Yehudit 22 ל, Zosha 20 צ׳, Papi 21 צ׳) + 1 "לבוב" |
| 22 | lakkarov19470109-01.2.3 | 9.1.1947 | עולי קפריסין שהגיעו בעתלית | 1 | 1 | A = B-5; B: "לייבוביצי הארש" (a man) |
| 23 | lakkarov19460806-01.2.2 | 6.8.1946 | המעפילים שהגיעו באניה "ה…" (2,700 olim) | 0 | 26 | 25 Leibovitz + "לאבובר מאריה 28"; includes "ליבוביץ חוה 20, דאז׳י אטלקה, ה" (Hungary; parents Dezső and Etelka); no Miriam, no Magda; no Moshe + Frima |
| 24 | lakkarov19460822-01.2.2 | 22.8.1946 | מעפילי "החייל העברי" ו"הגנה" שהועברו לעתלית | 0 | 13 | B-3; truncated in the מ-block (letters נ–ת absent) |
| 25 | lakkarov19460822-01.2.6 | 22.8.1946 | רשימת גולי קפריסין תפורסם בימים הקרובים | 0 | 13 | 12 Leibovitz + "לאבוביץ נעמי 18"; no Miriam, no Magda; letters א–ד and ש–ת absent |
| 26 | lakkarov19460829-01.2.2 | 29.8.1946 | מעפילי "יגור" ו"כתריאל יפה" שהועלו לקפריסין | 0 | 1 | "לייבוביץ הארמאן 1926 ר" |
| 27 | lakkarov19460829-01.2.19 | 29.8.1946 | המעפילים באניה "כתריאל יפה" | 0 | 7 | Silka 1921, Avraham 1926, Haya 1926, Zeev 1925, Ragina 1928, Bela 1923, Sara 1925 |
| 28 | lakkarov19460829-01.2.23 | 29.8.1946 | המעפילים באניה "יגור" | 0 | 0 | "לובוביץ רחל 1922 יצחק פ" not counted |
| 29 | lakkarov19461003-01.2.2 | 3.10.1946 | ואלה מבוקשים ע״י גולי קפריסין | 0 | 0 | "זאב לובוביץ" (in parentheses) not counted |
| 30 | lakkarov19461003-01.2.10 | 3.10.1946 | מעפילי עתלית דורשים בשלום משפחתם | 0 | 0 |  |
| 31 | lakkarov19461107-01.2.2 | 7.11.1946 | מעפילי "ברכה פולד" שהוגלו לקפריסין | 0 | 7 | Ela 22, Zvi 25, Eli 20, Lea 17, Esther 14 (Berl and Hana), Clara 19, Alexander 19 |
| 32 | lakkarov19461107-01.2.3 | 7.11.1946 | עזרה לגולי קפריסין | 0 | 0 | prose, 116 words |
| 33 | lakkarov19460331-01.2.10 | 31.3.1946 | דרישות שלום ברדיו ירושלים | 1 | 0 | control found: "…דרוקאר 32630 בלומנטאל שושנה יעקב בלאטנאר 34586" (an "אל: מאת:" list; the entry is Shoshana) |
| 34 | lakkarov19450830-01.2.2 | 30.8.1945 | ברוך בואם של ניצולי גולה (Mauritius) | 1 | 0 | "ד״ר בלומנטאל" (hospital director) |
| 35 | lakkarov19450830-01.2.23 | 30.8.1945 | חיפוש קרובים, ירושלים | 1 | 1 | "ד״ר בלומנטאל לאו (Berlin)"; "לייבוביץ מנדל שיה (ישעיהו), ת״א" |
| 36 | lakkarov19451011-01.2.25 | 11.10.1945 | חיפוש קרובים, ירושלים | 1 | 3 ("לבוב" as a town) | "חיה בלומנטאל לבית מושקאטל, עתה בשבדיה" |
| 37 | lakkarov19451129-01.2.12 | 29.11.1945 | חיפוש קרובים, תל אביב | 1 | 1 | "בלומנטאל משולם"; "לייבוביץ מארטין" |
| 38 | lakkarov19451213-01.2.24 | 13.12.1945 | חיפוש קרובים, תל אביב | 1 | 0 | "בלומנטאל שושנה (מכתב מהצבא)" |
| 39 | lakkarov19451213-01.2.27 | 13.12.1945 | חיפוש קרובים, ירושלים | 1 | 1 (hyphenated) | "בלומנטאל יום (קרובו באנגליה) 16658"; "ליבו־ אברהם" |
| 40 | lakkarov19451227-01.2.5 | 27.12.1945 | שרידי פולין מחפשים קרוביהם | 1 | 0 | "(חיד• בלומנטאל) 7335" |
| 41 | lakkarov19460110-01.2.3 | 10.1.1946 | פליטים מפולין בפראנקפורט | 1 | 0 | "בלומנטאל אהרן" |
| 42 | lakkarov19460124-01.2.20 | 24.1.1946 | דרישות שלום ברדיו ירושלים | 1 | 0 | "בלומנטאל 19368" |
| 43 | lakkarov19460228-01.2.10 | 28.2.1946 | דרישות שלום ברדיו ירושלים | 1 | 0 | "מאקס תיאודור בלומנטאל 30763" |
| 44 | lakkarov19460516-01.2.8 | 16.5.1946 | חיפוש קרובים, תל אביב | 1 | 3 | "בלומנטאל נחמן, מסטאשוב … 50089"; B: a seeker "יוסף לייבוביץ" three times |
| 45 | lakkarov19460110-01.2.15 | 10.1.1946 | מכתבים לעולי מאוריציוס | 1 | 0 | control: "בלום יעקב בלומנטאל יושד" = two adjacent names (Blum Yaakov; Blumenthal Yosha) |
| 46 | lakkarov19460516-01.2.13 | 16.5.1946 | חיפוש קרובים, ירושלים | 1 | 1 ("לבוב" as a town) | "בלומנטאל ארנסט מהאנובאר" |
| 47 | lakkarov19460606-01.2.5 | 6.6.1946 | חיפוש קרובים, תל אביב | 1 | 2 | "סאנה בלומנטאל, ביאלסק"; B: seekers "י. ל. לייבוביץ", "יוסף לייבוביץ" |
| 48 | lakkarov19460613-01.2.5 | 13.6.1946 | דרישות שלום ברדיו ירושלים | 1 | 0 | "שרה רעיה — בלומנטאל 45936" |
| 49 | lakkarov19460710-01.2.10 | 10.7.1946 | דרישות שלום ברדיו ירושלים | 1 | 1 | "בלומנטאל ארטור יוסף … מלבוב 4587"; "מיכאל לייב בן שמואל לייבוביץ 46514" |
| 50 | lakkarov19460725-01.2.10 | 25.7.1946 | חיפוש קרובים, חיפה | 1 | 0 | "בלומנטאל אירמה (ר. ג׳אקסון) 3041" |
| 51 | lakkarov19460822-01.2.3 | 22.8.1946 | חיפוש קרובים, תל אביב | 1 | 1 | "(סאנה בלומנטאל)"; a seeker "פרידה לייבוביץ" |
| 52 | lakkarov19460912-01.2.5 | 12.9.1946 | דרישות שלום ברדיו ירושלים | 1 | 4 | "בלומנטאל יושה, העולי מאוריציוס"; B: "חנה לאבוביץ׳", "יצחק לייבוביץ (בן־דודו יצחק לייבוביץ׳ מראדין)", "חנה ליבוביץ׳" |
| 53 | lakkarov19470324-01.2.7 | 24.3.1947 | חיפוש קרובים, תל אביב | 2 | 0 | "בלומנטאל זיסלה (אחיה, נתן לנדאו) 68044"; "בלומנטאל נחמן מ־סטאשוב" |
| 54 | lakkarov19470630-01.2.2 | 30.6.1947 | חיפוש קרובים, ירושלים | 1 | 0 | "בלומנטל נתן מוארשה" |
| 55 | lakkarov19470917-01.2.2 | 17.9.1947 | חיפוש קרובים, תל אביב (13,671 words) | 1 | 16 (5 surname; 11 "לבוב"/fragments) | "בלומנטל נחמן, שמואל ומוטל מ־סטאשוב"; the text ends mid-list ("שטרנבאום ארנולד מ־לובומיל") and the continuation lakkarov19470917-01.2.3.1 was not fetched |
| 56 | lakkarov19460314-01.2.6 | 14.3.1946 | חיפוש קרובים, תל אביב | 1 | 0 | control: "בלומנטאל איזידור (מכתב מאנגליה). 49914" |
| 57 | lakkarov19470227-01.2.2 | 27.2.1947 | מעפילי "לנגב" ו"המעפיל האלמוני" | 0 (near: "בלומנסאל ישראל, 17, וילנה") | 14 (7 surname, 7 "לבוב") | two ship lists: Simcha 26, Zehava 24, Haim-Yisrael 22; list 2: Halena 30, Yaakov 26, Mordechai 29, Moshe 28; no Miriam, no Magda |
| 58 | lakkarov19470227-01.2.4 | 27.2.1947 | מעפילי "לנגב" ו"המעפיל האלמוני" מבקשים את קרוביהם | 0 | 2 | seekers "שמחה לייבוביץ מ־באטשקאב", "חיים־ישראל לייבוביץ מ־סארנו־מארה" |
| 59 | lakkarov19470324-01.2.2 | 24.3.1947 | מעפילי "חיים ארלוזורוב" ו"אובריל" (page 1) | 0 | 1 (a town) | truncated after the letter ט; letters י–ת are on page 2 = the canary section lakkarov19470324-01.2.4 (D-2) |
| 60 | lakkarov19470324-01.2.8 | 24.3.1947 | 750 חוזרי קפריסין | 0 | 12 | names only: Eliezer, Armand, Bela, David, Zehava, Yissachar, Moshe, Rachel, Reuven, Shlomo, Shmuel, Simcha; no Miriam, no Magda |
| 61 | lakkarov19470324-01.2.9 | 24.3.1947 | מעפילי "אובריל" | 0 | 7 | all "לבוב" as a town |
| 62 | lakkarov19470324-01.2.10 | 24.3.1947 | גולי קפריסין מבקשים את קרוביהם | 0 | 1 | "לייבוביץ ב־ת״א (יצחק גרינבארג מ־אונבר…)" |
| 63 | lakkarov19450719-01.2.12 | 19.7.1945 | מתבקשים אל המדור לחיפוש קרובים, ירושלים | 1 | 0 | "בלומנטאל ברטולד (חיפה…)" |
| 64 | lakkarov19450726-01.2.23 | 26.7.1945 | פליטי פולין בשבאדיד | 1 | 0 | "ברטולד וגרטרוד בלומנטאל" |
| 65 | lakkarov19450809-01.2.19 | 9.8.1945 | מתבקשים למדור לחיפוש קרובים, ת״א | 1 | 0 | "אינג׳ אדם בלומנטאל" |
| 66 | lakkarov19450816-01.2.19 | 16.8.1945 | מתבקשים למדור לחיפוש קרובים, ירושלים | 1 | 1 (hyphen compound) | "חיה בלומנטאל בשבדיה"; "פרידמן־לבוביץ׳" (seeker) |

### D-2. Eighteen further Lakrov sections read directly
| # | Section id | Date | Title | Entries found and reading |
|---|---|---|---|---|
| 1 | lakkarov19450712-01.2.13 | 12.7.1945 | 435 Hungarian Jews freed from HASAG-Altenburg (Latin script) | Lebovits/Lebovics ×8 (Etel 1914 Máramarossziget; Iren 1930 Bpest, Bekesobaba; Cili 1917 Alsóapsa; Etel b. Praschke; Eva 1926; Iren; Irma 1927 Újpest; Katalin 1923 Szabolcsbarka); no Magda, no Miriam; no Blumenthal |
| 2 | lakkarov19450712-01.2.14 | 12.7.1945 | addresses list (Kovno) | Latin: one Blumenthal-type and three Lebov-type tokens, all Lithuanian; "Bercel" is a given name there; unrelated |
| 3 | lakkarov19450802-01.2.19 | 2.8.1945 | 245 women from Hungary freed at HASAG-Altenburg | no Lebovits, no Blumenthal (the section matched only because of "Netzer … Vác, Balassagyarmat") |
| 4 | lakkarov19450823-01.2.21 | 23.8.1945 | refugees in touch with the Brigade, Italy | Latin: "Blumenthal Jakob 1916, Kowno" (Lithuanian): not ours |
| 5 | lakkarov19451004-01.2.3 | 4.10.1945 | relatives search, Tel Aviv | B=3: "לייבוביץ אסתר ואפרים, סצ׳כיה, ת״א (ד״ש מאת שושנה אחות אסתר לייבוביץ בבריסל)"; "לייבוביץ חיים, ת״א, ולייבוביץ צבי, הרצליה": other |
| 6 | lakkarov19451018-01.2.16 | 18.10.1945 | Hungarian speakers at Hafkrug | Lebovits ×4: Frida 1927 and Margit 1918 (Chust); Eszter 1922 (Irhoc); Kisdobrony; Etel 1920 (Mezőszagos): other |
| 7 | lakkarov19451122-01.2.24 | 22.11.1945 | WALDHAUS 2 (Hungarian women, Latin script) | Lebovits ×4: Ernőné; Iren 1930 (Békéscsaba); Iren 1925 (Galócás); Magda 1924 (Budapest): B-6; same list: "HEKS Ferencne 1918, Balassagyarmat" |
| 8 | lakkarov19451206-01.2.21 | 6.12.1945 | Hungarian Jews at Wels | Lebovits ×2: Pál 1925 (Budapest VII), József 1914 (Budapest V): other; "Balassagyarmat" appears for Schwartz Sándor 1928 and Heimann Emanuel |
| 9 | lakkarov19451206-01.2.27 | 6.12.1945 | Hungarian women at Kaunitz | Lebovits ×2: Cecilia 1920 (Máramarosdombó), Magda 1927 (Magyarpéterd): B-6 (excluded) |
| 10 | lakkarov19460131-01.2.6 | 31.1.1946 | relatives search, Tel Aviv | B=2: "לייבוביץ מרים ואריה (ל. אפשטיין, ד״ר). 43907"; "(דויד לייבוביץ)" as a seeker: C-1 |
| 11 | lakkarov19460331-01.2.4 | 31.3.1946 | "פליטי ישראל" (22,427 characters) | 0 / 0; opened by mistake (not a continuation of any list searched) |
| 12 | lakkarov19460519-01.2.2 | 19.5.1946 | Max Nordau, page 1 (letters א–ה) | A=1: "בלומנטאל ראגיי 1923" (given name garbled; b. 1923; other); B=0 |
| 13 | lakkarov19460530-01.2.6 | 30.5.1946 | children and youth in the Strom camp | Lebovits ×1 ("Lebovits Szerena" in a mother-name field); "Balassagyarmat" for Popok Iren 1929, Schulteis Zsuzsa 1931, Weisz Benjamin 1930: other |
| 14 | lakkarov19470324-01.2.4 | 24.3.1947 | "Chaim Arlosoroff" and "Oberil", page 2 = the canary | B=5: Rozi 28; Leib 30, Czechoslovakia; Matityahu 15, Bucharest; Zvi 18, Iași; Esther 18, Sighet: other. The canary entry "קוטנר אברהם, 16, אוזורקוב" present |
| 15 | lakkarov19470414-01.2.2 | 14.4.1947 | "Moledet" ship list | B=35 tokens, including "לייבוביץ מאגדה 23מונקאץ׳": B-9 |
| 16 | lakkarov19470507-01.2.2 | 7.5.1947 | "Theodor Herzl", part 1 | 0 / 0 |
| 17 | lakkarov19470507-01.2.3 | 7.5.1947 | "Theodor Herzl", 2,620 ma'apilim | B=13, including "לייבוביץ מרים 19 צ": B-9 |
| 18 | lakkarov19451122-01.2.21 | 22.11.1945 | "יהודי הונגריה" (Hungarian women, "לפי מפקד הבריגאדה", Latin script; continues the Waldhaus list from "LOW") | no Lebovits, no Blumenthal; "NETZER Ella 1923, Iren 1923, & Valeria 1929, Balassagyarmat": other |

## E. Not done, blockers and follow-ups

**Blockers.** None: the canary passed and no query failed.

**Not done in JPress.**
1. Page images are locked; OCR only.
2. Lakrov Velarahok covers 28.6.1945 – 17.9.1947 only.
3. Lakrov sections not read. The AND queries Q-105 to Q-110 return sections where the two words occur anywhere (110, 10, 36, 6, 2, 7 sections); only 5 per query were listed, and the listed ones still unread are `lakkarov19451206-01.2.2`, `lakkarov19460207-01.2.29`, `lakkarov19451227-01.2.2`, `lakkarov19450920-01.2.21`, `lakkarov19451122-01.2.3`, `lakkarov19460110-01.2.20`, `lakkarov19451227-01.2.12`, `lakkarov19451101-01.2.2`, `lakkarov19450823-01.2.25`, `lakkarov19460221-01.2.14`, `lakkarov19460418-01.2.10`. The adjacency forms (Q-2, Q-3, Q-8, Q-10, Q-219) are complete.
4. Continuations not fetched: the Atlit list of 22.8.1946 after the מ-block; `lakkarov19470917-01.2.3.1`; the part of `lakkarov19460331-01.2.2` after the letter ו (no ל names are present before it).
5. Recall limits of the OCR: surnames cut or damaged ("לייבו", "ייבוביץ", "ל־יבוביץ"), hyphenated names as one token, apostrophes; Leibovitz is a very common surname. The delegated scans count tokens by prefix; an entry whose first letters are damaged escapes them.
6. Latin script and Uj Kelet. `Lebovits` (Q-184): 74 hits; 40 listed (date order, up to 23.10.1949), of which 6 were read and 34 were not; 34 further hits (after 23.10.1949) are not listed. `Lebovics` (Q-183): 19 hits, 3 read, 15 unread (`egy19440302-01.2.19.1`, `lakkarov19450726-01.2.12`, `lakkarov19450802-01.2.16`, `refadv19450803-01.2.13`, `cgs19450809-01.2.28`, `lakkarov19451011-01.2.13`, `lakkarov19451122-01.2.19`, `lakkarov19451206-01.2.14`, `lakkarov19451206-01.2.28`, `lakkarov19460117-01.2.13`, `lakkarov19460117-01.2.17`, `tjm19461003-01.2.23.1`, `ujk19490527-01.2.19`, `ujk19491014-01.2.33.4`, `ujk19510211-01.2.20.4`) and 1 hidden PAGE hit. `Blumenthal` in Uj Kelet (Q-197): 7 of 15 unread (`ujk19510306-01.2.25`, `ujk19510807-01.2.21.2`, `ujk19510812-01.2.18.1`, `ujk19510907-01.2.16`, `ujk19511021-01.2.21.1`, `ujk19511231-01.2.22`, `ujk19520318-01.2.18.1`). Hidden PAGE hits (ids not shown, not openable): Balassagyarmat 1, Lebovics 1, Lebovits 3, Lebovits Tikva 1, Altenburg 2, Nograd 1, Blumenthal Miriam 1. The adjacency queries for the family's names (Q-170, Q-175 to Q-182, Q-188 to Q-196, Q-206, Q-207, Q-234 to Q-249) are complete.
7. Not searched: Shimon and Manó (names too common without an anchor), Yaakov's sisters other than Rivka, and Davar's and Haaretz's registration lists beyond what the surname queries reached. The four HaTsofeh lists headed "נישואין" (23.9, 17.10, 15.11 and 15.12.1948) were not opened; they do not contain `בלומנטאל`, and Leibovitz was not tested in them.
8. Hebrew-spelled Balassagyarmat and Nógrádbercel queries return 0 or noise; the town appears in this sweep only in Latin script.

**Follow-ups outside JPress, suggested by the findings.**
- B-3: the Atlit immigrants index (IGRA) and the Israel State Archives for Esther Leibovitz (b. about 1918) and Nechama Leibovitz (b. about 1925), parents Moshe and Frima, Hungary, August 1946; the voters' list of 1949, Petah Tikva, for both; whether Avraham Aharon's pages of 2000 name them among the eight children.
- B-1: the Petah Tikva rabbinate file for Esther Leibovitz and Yehuda Frenkel (October 1948), which may give her age and mother.
- B-5: JDC and Cyprus lists for Michael and Ignác/Jenő Blumenthal, early 1947; the Zionist Archive file S6/36831 already cited in the Yaakov report.
- B-4: the passenger list of "Max Nordau" (May 1946) in the original, for the surname after "לייבו" and the town.
- B-2: the Petah Tikva rabbinate file for Yehuda Blumenthal and Atara Krindel Schlesinger (August 1952).

## Summary
The sweep (267 queries over 1944–1952, in Hebrew and in Latin script, with the OCR variants found in the entries themselves; 66 Lakrov sections, 41 "Moshe Leibovitz" hits and 137 HaTsofeh sections read through their OCR) yields six flagged findings, all new to the project.
1. **B-1.** The printed registration of Yaakov and Miriam, HaTsofeh 8.10.1948 (`hzh19481008-01.2.64`): near-certain. It gives Yaakov's residence as Ein Ganim, Petah Tikva (his brother's neighbourhood) and shows a second Petah Tikva bride, Esther bat Moshe Leibovitz, registering the same day.
2. **B-2.** The registration of Yehuda Blumenthal, "son of Moshe Ben-Zion", 21.8.1952 (`hzh19520821-01.2.56`): near-certain for the family.
3. **B-3.** An Atlit list of 22.8.1946 (`lakkarov19460822-01.2.2`) with Nechama (21) and Esther (28), children of Moshe and "Frimam" from Hungary: probably Miriam's family, and the most useful lead for the "eight children" and for the question whether Miriam is Magda. Miriam herself is not on that list.
4. **B-4.** A Miriam b. 1925 with the surname cut to "לייבו" on the Max Nordau list (`lakkarov19460519-01.2.3`): possible.
5. **B-5.** A Michael Blumenthal among the Cyprus arrivals at Atlit on 9.1.1947 and seeking "Ignác-Jenő Blumenthal" on 6.2.1947 (`lakkarov19470109-01.2.3`, `lakkarov19470206-01.2.3`): possible, with the Hungarian names of the Nógrád brothers.
6. **B-6.** The Magda candidates are weak (Waldhaus 2: Magda b. 1924, Budapest) or point away (Uj Kelet 29.12.1949: a Magda Lebovits still being brought from Hungary).

No item names Miriam as Magda, none names Yaakov among the twelve Nógrádbercel children, none gives the origin of Miriam or of Yaakov, and nothing connects the families to Nógrádbercel or Balassagyarmat; the only mother's name printed for a possible sister of Miriam is the "Frimam" of B-3. The limits in E decide how far the negatives reach: entries whose surname is cut or damaged by the OCR, sections that JPress indexes only as hidden PAGE hits, and the unread remainders of the surname-only queries in Lakrov and Uj Kelet are not covered; the exact name forms listed in A are.

## Addendum, same day: follow-up of B-1 and B-3 outside JPress
Recorded after the sweep, so that the grades above are read with what followed; the sweep's own grades are left as they were written.
- **B-1, Esther.** The marriage certificate H 99913 (Petah Tikva rabbinate, 26.10.1948; IGRA-17917-Marriages-1032, scan `../igra/marriage_cert_H99913_petah_tikva_1948-10-26_esther_leibovitz_yehuda_frenkel.jpg`) gives the bride "אסתר ליבוביץ", 32, "פועלת", "פתח תקוה, חובבי ציון 12", parents "משה הלוי ליבוביץ" and "פרימט", both dead; the groom "יהודה הלוי פרנקל", 40, soldier, "אי שם...". The bride's address and both parents' names, with "הלוי" and the spelling "פרימט", are those of Miriam's certificate H 99915 of the next day. That Esther is Miriam's sister: raised to **כמעט ודאי** (transcription: `../igra/marriage_cert_H99913_esther_leibovitz_yehuda_frenkel_transcription.md`).
- **Esther's Pages of Testimony.** Yad Vashem, submitter "אסתר פרנקל": 1646775 (Moshe Lebovicz, b. 1890 Balassagyarmat, shoemaker, wife "פני לבית וועג", Auschwitz 1944, a child aged 16 = record 8650894), 569646 (Fani, b. 1890 Budapest, daughter of Avraham and Olga), 333843 (Shimshon/Simson, b. 1914, merchant, single, died 1944 in a labour camp), all dated 6.12.1956; and 3623074 (Moshe Leibovitz, filled 3.7.1995 in Tel Aviv: "TOKAI Str", ghetto "NIRIEGE", Auschwitz). Scans and transcription: `../yadvashem-pot-esther-frenkel/`.
- **B-3.** With the certificate and the pages, the Esther of the Atlit list of 22.8.1946 (28, parents Moshe and "פרימאם", Hungary) is **ככל הנראה** the same Esther (ages differ: 28 in 1946, 32 in 1948). Nechama stays **אפשר ש… (טעון אימות)**, as a sister or as Miriam under another name.
- **IGRA, the same day.** "אסתר פרנקל": 148 records, none in Petah Tikva or Givatayim; "ליבוביץ / לייבוביץ נחמה": 20 records, none that fits: born 1904–1914 or about 1933, a child of three in the Tel Aviv census of 1928 (born there), a scholar of Jerusalem and Tel Aviv, and a name change to Shoham in Haifa, 1973, without a birth year.
