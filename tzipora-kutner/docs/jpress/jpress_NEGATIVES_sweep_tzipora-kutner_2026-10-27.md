# JPress sweep — Tzipora Kutner née Blam (Balem) — queries re-run with per-hit classification, coverage limits and one new item — 2026-10-27

**Subject.** Tzipora Kutner née Blam / Balem / "באלן" (b. Luboml (Lubomel), Volhynia, 25.12.1932; "1931" in some postwar lists; father Mendel, mother Zelda; Selvino; ship "Chaim Arlosoroff" 1947; kibbutz Tze'elim; d. 27.1.2006, Beersheba). Husband Avraham Kutner (see `../../../avraham-kutner/docs/jpress/jpress_NEGATIVES_sweep_avraham-kutner_2026-10-27.md`).
**Date.** 2026-10-27. **Server.** JPress (National Library of Israel) through `jpress_search`, `jpress_get_article`, `jpress_fetch_raw`.
**Copyright.** Page images are locked; only OCR text was read. This file records section ids, dates, titles and at most one short quotation (15 words or fewer) per hit. OCR is noisy.

## Canaries (run first, all green)
- `jpress_get_article dav19531021-01.2.56.1` returned the known 1953 notice; `jpress_list_publications` answered (2,365 titles).
- Positive controls: `"באלן צפורה"` finds `lakkarov19470324-01.2.2` (the known ship list page 1: "באלן צפורה, 16, לובומיל"); `לובומיל` restricted to `lakkarov` finds three Lakrov Velarahok issues, including that one (the list spells Luboml with a yod, so queries with `לובומל` cannot hit it).
- Zero-hit searches are real answers (the no-hit JSON fault was fixed on 2026-08-26).

## Coverage limits relevant to Tzipora (measured today, query "ישראל")
| Period | Measured | Consequence |
|---|---|---|
| Jan–Feb 2006 (her death 27.1.2006) | 48 sections: lbf 24, eretzh 17, hakivunmizrah 7 | No daily paper: a mourning notice cannot appear |
| 2001–2005 | 3,003 sections: bamahane, lbf, eretzh, shemhamishak, hakivunmizrah, zim | No dailies |
| After 29.11.1993 | Hadashot ends; Maariv ends 30.4.1992; Davar ends 30.6.1985; Haaretz ends 31.12.1971 | Dailies absent for her adult life in the kibbutz after 1993; thin before |
| 1947 | Lakrov Velarahok present (lists of ma'apilim) | The only place so far where she appears |

## A. Query table
| # | Exact query (as typed) | Filters | Total | Date span | Result |
|---|---|---|---|---|---|
| T-1 | `"צפורה קוטנר"` | phrase | 0 | – | none |
| T-2 | `"ציפורה קוטנר"` | phrase | 0 | – | none |
| T-3 | `בלם לובומל` | AND | 0 | – | none |
| T-4 | `בלם לובאמל` | AND | 0 | – | none |
| T-5 | `"מנדל בלם"` | phrase | 3 | 1958-02-13 – 1979-10-26 | all irrelevant (B-1) |
| T-6 | `בלם סלווינו`; `בלם סלבינו` (Massuah's spelling) | AND | 0; 0 | – | none. Control: `סלבינו` alone = 43 hits (1869–2014), including `ydv19460214-01.2.10` and `hagalgal19470327-01.2.49` on the children's home |
| T-7 | `קוטנר צאלים` | AND | 9 | 1972-02-11 – 2001-11-30 | all irrelevant: one 1972 classified page and eight radio-listing/Bamahane pages of the radio host Yoav Kutner (listed in the Avraham file, B-3) |
| T-8 | `קוטנר`, 2006-01 – 2006-02 | date filter | 0 | – | none; the window holds no daily (coverage table) |
| T-9 | `"באלן צפורה"` (control, her 1947 spelling) | phrase | 1 | 1947-03-24 | **KNOWN** (lakkarov19470324-01.2.2) |
| T-10 | `"צפורה בלם"` | phrase | 3 | 1937-03-31 – 1952-03-18 | 1 **NEW** (hzh19520318-01.2.49); 2 namesake (B-2) |
| T-11 | `"בלם צפורה"` | phrase | 1 | 1993-01-06 | irrelevant (B-3) |
| T-12 | `"קוטנר צפורה"`; `"צפורה קיטנר"`; `"זלדה בלם"` | phrase | 0; 0; 0 | – | none |
| T-13 | `בלם לובומיל` | AND | 1 | 1904-12-20 | irrelevant: `hzfwar19041220-01.2.5` (HaTsefira, Warsaw, an article of over 1,000 words; date impossible for her) |
| T-14 | `לובומיל`, restricted to `lakkarov` | AND | 3 | 1946-03-07 – 1947-04-14 | 1 known; 2 irrelevant (B-4). `לובומל` in `lakkarov`: 0 |

## B. Hit-level classification
### B-1. `"מנדל בלם"` — 3 hits
| Section id | Date, title | Reading | Grade |
|---|---|---|---|
| hbkr19580213-01.2.88 | HaBoker 13.2.1958 (24-word item) | a returned patient "במעבר מנדל־בלם" = a misprint of the Mandelbaum Gate crossing in Jerusalem | irrelevant |
| dav19650201-01.2.52 | Davar 1.2.1965 | burial in Herzliya of "צבי מנדל־בלם", a Warsaw-ghetto fighter killed in a road accident; the name is one hyphenated surname | irrelevant (other person, other place) |
| dav19791026-01.2.81 | Davar 26.10.1979, real-estate classifieds | "מנדל־בלם 1" inside a housing ad | irrelevant |

### B-2. `"צפורה בלם"` — 3 hits
| Section id | Date, title | Reading (OCR, quotation ≤15 words) | Grade |
|---|---|---|---|
| **hzh19520318-01.2.49** | HaTsofeh 18.3.1952, "פרסום הרשומים לנישואין" | block "במשרד הרבנות בבאר שבע": "אברהם קיטנר . צאלים. רוק … צפורה בלם צאלים רוקה" | **NEW, near-certain**: see C-1 |
| haretz19370331-01.2.98 | Haaretz 31.3.1937, Tel Aviv local news | "צפורה בלם בת 6 שנים" scalded by a pot of soup in Kerem HaTeimanim; taken to Hadassah | namesake: a girl in Tel Aviv in 1937; ours lived in Luboml |
| dav19370401-01.2.51 | Davar 1.4.1937, Tel Aviv | the same accident ("צפורה בלם", Kerem HaTeimanim, boiling oil in the OCR) | namesake (same girl) |

### B-3. `"בלם צפורה"` — 1 hit
hadashot19930106-01.2.107 (Hadashot 6.1.1993): a stock-market page, "בל'ם צ'פורה" is OCR noise inside an exchange-rate table. Irrelevant.

### B-4. `לובומיל` in Lakrov Velarahok — 3 hits
| Section id | Date | Reading | Grade |
|---|---|---|---|
| lakkarov19460307-01.2.2 | 7.3.1946, "קרובינו אנו מבקשים" | greetings from a refugee in Shanghai "לאנשי לובומיל" | irrelevant |
| lakkarov19470324-01.2.2 | 24.3.1947 | "באלן צפורה, 16, לובומיל" | **KNOWN** |
| lakkarov19470414-01.2.2 | 14.4.1947, "מעפילי 'מולדת'" | a man aged 28 from Luboml in the ship list | irrelevant (other ship, other person) |

## C. NEW item
| # | Section id | What it says | Why it matters | Grade |
|---|---|---|---|---|
| C-1 | **hzh19520318-01.2.49** (HaTsofeh 18.3.1952) | Marriage registrations at the Be'er Sheva rabbinate: "אברהם קיטנר . צאלים. רוק" and "צפורה בלם צאלים רוקה" (both of Tze'elim, bachelor and spinster; the surname is printed "קיטנר") | The couple's marriage registration about March 1952: place (Be'er Sheva rabbinate), both single, both at Tze'elim. Gives her maiden name as "בלם" (Blam), where the 1947 ship list has "באלן" and the Cyprus list "Balem". Fits the daughter's account that they married in the Be'er Sheva rabbinate and returned to the kibbutz that evening. The earlier sweep missed it because the husband's name is spelled "קיטנר" and "צפורה קוטנר" is not how she is named | near-certain (כמעט ודאי) |

## Not done / blockers
- JPress page images are locked (copyright); OCR only.
- No daily newspaper is indexed for January–February 2006 (nor 1994–2005), so her mourning notice cannot be searched here; the 2006 notice would have to come from Maariv/Haaretz/Yedioth archives outside JPress (a note in the report already says so).
- The Luboml and Blam spelling space (Hebrew, Yiddish, Polish transliterations: בלם, באלן, באלם, בלום; לובומל, לובומיל, לובאמל, ליובומל) was sampled, not exhausted; the Yiddish Luboml press (for example the Volhynia titles in JPress) was not searched for "בלום"/"בלעם".
- Mendel and Zelda Blam (parents) do not appear: `"מנדל בלם"` yields only unrelated items, `"זלדה בלם"` none.

## Summary
JPress yields no item about Tzipora under any of the requested forms: "צפורה קוטנר", "ציפורה קוטנר", Blam with Luboml (both spellings), "מנדל בלם" (three unrelated hits, one a misprint of the Mandelbaum Gate), Blam with Selvino, Kutner with Tze'elim (nine hits, all the radio host Yoav Kutner or a classified ad), and mourning notices for January–February 2006 (no daily is indexed for that period at all). The one result is outside the requested list: a search on her maiden name with her first name, "צפורה בלם", finds the HaTsofeh notice of 18.3.1952 in which she and Avraham, both of Tze'elim and both unmarried, are registered for marriage at the Be'er Sheva rabbinate. Two other hits for that name are a different girl in Tel Aviv in 1937. The known 24.3.1947 ship list (באלן צפורה, 16, לובומיל) is confirmed as the only Lakrov Velarahok entry that fits her.
