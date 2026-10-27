# JPress sweep — Avraham ("Abram", "Avramek") Kutner — queries re-run with per-hit classification, namesakes, coverage limits and new items — 2026-10-27

**Subject.** Avraham Kutner (b. Ozorków 15.8.1928 per the Mauthausen card, "1930" in postwar lists; Łódź ghetto; Auschwitz 22.8.1944; Mauthausen no. 133332; Selvino; ship "Chaim Arlosoroff" 1947; kibbutz Tze'elim; Dimona; d. 18–19.3.1986, buried Beersheba). Wife Tzipora née Blam (see `../../../tzipora-kutner/docs/jpress/jpress_NEGATIVES_sweep_tzipora-kutner_2026-10-27.md`).
**Date.** 2026-10-27. **Server.** JPress (National Library of Israel, Historical Jewish Press) via `jpress_search`, `jpress_get_article`, and `jpress_fetch_raw` (raw Veridian JSON, used to recover PAGE-type hits whose ids `jpress_search` hides, and to get text snippets).
**Copyright.** Page images are locked; only OCR text was read. This file records article ids, dates, titles and at most one short quotation (15 words or fewer) per hit. All OCR is noisy and unproofread.

## Canaries (run first, all green)
- JPress: `jpress_get_article dav19531021-01.2.56.1` returned the known 21.10.1953 kvutza board notice (item readable); `jpress_list_publications` answered (2,365 titles).
- Positive controls (the engine finds known items by the exact query forms used below): `"קוטנר אברהם"` finds `lakkarov19470324-01.2.4` (the known ship list, page 2); `"באלן צפורה"` finds `lakkarov19470324-01.2.2` (page 1); `"אברהם קוטנר"` finds `dav19531021-01.2.56.1`; `"קוטנער אזאָרקאָוו"` finds `najerfolksblatlodz19370827-01.2.79`.
- Zero-hit searches are real answers: the server strips the invalid JSON NLI returns for a no-hit search (fix of 2026-08-26), so "0" here is not an error.
- Other servers' canaries are listed in `../NEGATIVES_camps-dp-sweep_N-15_2026-10-27.md`.

## JPress coverage limits — measured today (query "ישראל", date and publication filters)
| What | Measured | Consequence |
|---|---|---|
| Maariv `mar` | 525,180 sections; last indexed 30.4.1992 (`mar19920430-01.2.2`). **March 1986: 0 sections** (Feb 1986: 1,387; Apr 1986: 1,409). 19–21.3.1986: 0 | A Maariv death notice for 19–21.3.1986 cannot be found: the month is not in the index |
| Davar `dav` | 485,178 sections; last indexed 30.6.1985 | No Davar for 1986 |
| Haaretz `haretz` | 319,847 sections; last indexed 31.12.1971 | No Haaretz after 1971 |
| Hadashot `hadashot` | 110,215 sections; last indexed 29.11.1993; March 1986 partial (766 sections) | Only daily present in the death window |
| 19–21.3.1986, all titles | 205 sections: hadashot 87, hairtlv 45, ajnm 26, kolhair 21, bamahane 14, kotert 10, dapimramatdavid 2; ADVERTISEMENT-type sections containing "ז"ל": 2 (hadashot 19.3.1986 p.12 col.1; kotert) | Obituary column coverage for the three days after the death is nil/near nil |
| 1992 | 19,686 sections (hadashot 10,777; mar 6,425; bamahane 983; ajnm 946; ...) | Last year with dailies |
| 1996 | 804 sections (bamahane 510; lbf 134; shemhamishak 66; ...) | No dailies |
| 2001–2005 | 3,003 sections (bamahane 1,137; lbf 618; eretzh 481; shemhamishak 421; ...) | No dailies |
| Jan–Feb 2006 | 48 sections: lbf 24, eretzh 17, hakivunmizrah 7 | No dailies: no mourning notice for 27.1.2006 can exist here |

So the earlier row N-5 ("מודעת אבל, מרץ 1986, JPress 'קוטנר' — אפס") is a **coverage gap, not a negative**: JPress holds no Maariv issue for March 1986, no Davar and no Haaretz at all for that year.

## How hits were classified
`"יואב קוטנר"` (Yoav Kutner, Galei Zahal radio host and pop-music figure) is present on 3,046 JPress sections (programme listings in Maariv, Hadashot, Bamahane 1978–2001). Every co-occurrence query for the bare surname is dominated by him. Method for the large sets: (1) fetch the full hit list as raw JSON; (2) subtract the hits that also match the phrase `"יואב קוטנר"` with the same co-term; (3) read the residual through text snippets from a master list of all 1,723 post-1944 sections that contain "קוטנר" and not "יואב" (query `קוטנר -יואב`, 1944–2012). Hits that contain "יואב" and "קוטנר" without the exact phrase (OCR-broken forename, e.g. "•ואב", "1אב", "זאב") are listed as "Yoav Kutner presumed (programme page)". Grades: **ours**, **namesake (reason)**, **irrelevant**, **unresolved (לא הוכרע)**, **NEW**.

## A. Query table
| # | Exact query (as typed) | Filters | Total | Date span of hits | Result |
|---|---|---|---|---|---|
| A-1 | `"אברהם קוטנר"` | phrase, all | 16 | 1920-04-27 – 1979-01-02 | 1 known; 15 other; 1 new lead (lakkarov19470403-01.2.7); rest namesakes (B-1) |
| A-2 | `"קוטנר אברהם"` | phrase, all | 4 | 1929-06-19 – 1968-06-13 | 1 known; 3 other (B-2) |
| A-3 | `אברמק קוטנר` | AND, all | 0 | – | none |
| A-4 | `אברמק צאלים` | AND, all | 0 | – | none |
| A-5 | `אברמק` (control, nickname alone) | all | 40 | 1910-03-09 – 1982-12-17 | 23 Al HaMishmar (ahr), 3 Maariv; none contains "קוטנר" (A-3 = 0); not classified individually: irrelevant (common nickname; kibbutz news, a comic strip) |
| A-6 | `קוטנר צאלים` | AND, all | 9 | 1972-02-11 – 2001-11-30 | all irrelevant (B-3) |
| A-7 | `קוטנר סלווינו` | AND, all | 0 | – | none |
| A-7b | `קוטנר סלבינו` (spelling used by Massuah) | AND, all | 0 | – | none. Control: `סלבינו` alone = 43 hits (1869–2014), including `ydv19460214-01.2.10` and `hagalgal19470327-01.2.49` about the children's home, so Selvino items are indexed; none with Kutner |
| A-8 | `קוטנר דימונה` | AND, all | 40 | 1959-02-02 – 1990-02-16 | all irrelevant (B-4) |
| A-9 | `קוטנר "באר שבע"` | AND (phrase for the town), all | 140 | 1949-05-09 – 1992-01-24 | 1 NEW lead (hzh19490509-01.2.31); rest irrelevant/namesakes (B-5) |
| A-10 | `קוטנר` | 1986-03-01 – 1986-04-30 | 48 | 1986-03-02 – 1986-04-29 | no death notice; all irrelevant (B-6) |
| A-11 | `קוטנער` (Yiddish, bare) | all | 3,386 | 1871-02-17 (`iva18710217-01.2.10`) – 2010-09-01 (`lbf20100901-01.2.23`) | not reviewable hit by hit: "קוטנער" is the Yiddish adjective "of Kutno" as well as a surname. Top years 1927 (182), 1928 (180), 1930 (148), 1931 (141), 1936 (126); top titles frw 434, frim 359, dertog 255, tjm 223, hyt 187, dishtimemexico 183. From 1944 on: 831 (frw 218, dertog 216, dishtimemexico 177, dernayermoment 56, tjm 33, ajnm 19, ...). Narrowed in A-12 – A-18 (B-7) |
| A-12 | `קוטנער אזאָרקאָוו` (identical 5 hits for the diacritic-free `קוטנער אזארקאוו`) | AND | 5 | 1930-08-01 – 1937-08-27 | 1 known (najerfolksblatlodz19370827-01.2.79); 4 irrelevant (B-7) |
| A-13 | `קוטנער אזורקוב` / `קוטנער אזארקוב` / `קוטנר אזארקאוו` / `קוטנר אזורקוב` | AND | 0 / 0 / 0 / 0 | – | none |
| A-14 | `קוטנר אוזורקוב` | AND | 3 | 1919-05-01 – 1947-03-24 | 2 irrelevant (1919 Warsaw donor lists) + 1 known (lakkarov19470324-01.2.4) |
| A-15 | `"אברם קוטנר"`, `"קוטנר אברם"` | phrase | 0 / 0 | – | none |
| A-16 | `"אברהם קוטנער"` | phrase | 7 | 1907-07-19 – 1963-03-22 | namesake(s): US, Warsaw, Brazil Yiddish press (B-7) |
| A-17 | `"אבראם קוטנער"` | phrase | 1 | 1946-08-24 | irrelevant: fiction serial (B-7). `"אברם קוטנער"`, `"אברום קוטנער"`: 0 |
| A-18 | `קיטנר` (spelling variant found in the 1952 and 1947 items), 1944–2012 | all | 228 | 1944-08-09 – 1992-12-30 | **2 NEW** (hbkr19470120-01.2.32; hzh19520318-01.2.49); the rest: Yoav Kutner programme pages, a Tel Aviv dressmaker "שרה קיטנר", other people (screened by snippet) |
| A-18b | `"אברהם קיטנר"` / `"קיטנר אברהם"` / `קיטנר צאלים` / `"צפורה קיטנר"` | phrase/AND | 2 / 3 / 1 / 0 | see B-8 | NEW items B-8 |
| A-19 | `קוטינר` (variant), 1944–2012; `"אברהם קוטינר"`; `קוטינר צאלים` | all | 41; 0; 0 | 1944-05-14 – 1988-12-07 | nothing relevant: a Tel Aviv weaver's ads, a Bnei Brak wig seller, a Gur hasid, and the already-known 1976 notice (dav19761227-01.2.67.2) |

## B. Hit-level classification

### B-1. `"אברהם קוטנר"` — 16 hits
| # | Section id | Date, title | Reading (quotation ≤15 words, OCR) | Grade |
|---|---|---|---|---|
| 1 | dhy19200427-01.2.20 | Doar HaYom (Jerusalem) 27.4.1920 | candidate list for the Assembly of Representatives: "ו) אברהם קוטנר" | namesake: adult candidate in Jerusalem 1920 (ours b. 1928) |
| 2 | hzh19450925-01.2.50 | HaTsofeh 25.9.1945, marriage notices | "ברונו … בן אברהם קוטנר ת"א" | namesake: father of a groom, Tel Aviv |
| 3 | hzh19461227-01.2.72.2 | HaTsofeh 27.12.1946, Jerusalem rabbinate list | "אברהם קוטנר. ירושלים" | namesake: Jerusalem resident registering to marry; ours was in Italy |
| 4 | lakkarov19470403-01.2.7 | Lakrov Velarahok 3.4.1947, relatives-search list | entries 44956–44958: "(האניה בת אברהם קוטנר)" | namesake as to Avraham (an adult father of a girl Hania of Łódź); **NEW lead for kin search**, see D-8 |
| 5 | dav19531021-01.2.56.1 | Davar 21.10.1953 | kvutza board election | **KNOWN** (not new) |
| 6 | dav19561021-01.2.89.5 | Davar 21.10.1956, greeting ad | one of ~70 signatories, workers of the Ata textile works | namesake/unlikely: ours lived at Tze'elim (children born there 21.10.1957 and 16.3.1959) |
| 7 | shar19580521-01.2.6 | Sha'arim 21.5.1958, Shmita-fund chain | "הרב אברהם קוטנר [רב] דלוד" | namesake: Rabbi of Lod (same man in the hits of 1960–1968 below) |
| 8 | lmrv19601101-01.2.23.2 | Lamerhav 1.11.1960, Ahdut HaAvoda condolence | "קוטנר [OCR: דיבטשה] ואברהם" | namesake: couple; the same group's 1964 notice (lmrv19641009-01.2.15.4) reads "קוטנר רבקה ואברהם" — the Tel Aviv Poalei-Zion man and wife Rivka; ours has wife Tzipora |
| 9 | hzh19610804-01.2.72 | HaTsofeh 4.8.1961, rabbis' greeting | "הרב אברהם קוטנר רב העיר לוד" | namesake: Rabbi of Lod |
| 10 | mar19610814-01.2.61 | Maariv 14.8.1961, same list | same | namesake: Rabbi of Lod |
| 11 | haretz19630624-01.2.124 | Haaretz 24.6.1963, pensioners' club | "מר אברהם קוטנר, פועל־דפוס שפרש לפנסיה" (amateur painter) | namesake: retired printer, Tel Aviv; ours was 34 |
| 12 | mar19761226-01.2.73.2 | Maariv 26.12.1976, death notice | b. Warsaw, aliyah 1921, "מותיקי פועלי ציון"; wife Rivka, daughter Rachel, son Menachem; Kiryat Shaul | namesake: d. 26.12.1976 (ours d. 1986) |
| 13 | dav19761227-01.2.67.2 | Davar 27.12.1976 | condolences, same man | namesake |
| 14 | dav19761230-01.2.60.1 | Davar 30.12.1976 | neighbours, Ibshitz 4 (Workers' Housing, Tel Aviv) | namesake |
| 15 | dav19770123-01.2.52.1 | Davar 23.1.1977 | 30-day memorial and unveiling 24.1.1977 | namesake |
| 16 | mar19790102-01.2.144.4 | Maariv 2.1.1979 | death notice of his widow Rivka Kutner | namesake |

### B-2. `"קוטנר אברהם"` — 4 hits
| Section id | Date, title | Reading | Grade |
|---|---|---|---|
| dav19290619-01.2.36 | Davar 19.6.1929, subscribers whose addresses are sought | "קוטנר אברהם — שכ' העובד" | namesake: adult in Palestine 1929 |
| lakkarov19470324-01.2.4 | Lakrov Velarahok 24.3.1947 | ship list page 2 | **KNOWN** |
| letstenayestlv19501204-01.2.2 | Letste Nayes (Yiddish, Tel Aviv) 4.12.1950, prize-draw winners | "1414 קוטנר אברהם, הרצליה" | **unresolved (לא הוכרע)**: Herzliya, no other identifier; ours was probably in army service then (Tzipora: they came to Tze'elim as a Nahal group after three years of army) |
| haretz19680613-01.2.130 | Haaretz 13.6.1968, Tel Aviv University graduates | "מינה קוטנר, אברהם קופינסקי" | irrelevant: two different graduates adjacent in a list |

**The "eight other Avraham Kutners" of the earlier report.** The exact-name queries (A-1, A-2, A-16) resolve into the following distinct namesakes, so the earlier count of eight cannot be matched one for one; all are listed here with the reason: (1) Jerusalem candidate 1920; (2) Tel Aviv father of a groom 1945; (3) Jerusalem groom 1946; (4) Rabbi Avraham Alter Kutner of Lod, 1958–1968 (also in B-4/B-5); (5) Tel Aviv Poalei-Zion Avraham, b. Warsaw, aliyah 1921, wife Rivka, d. 26.12.1976 (hits 1960–1979; Yiddish 1947–1963 Brazil/US notices name a brother Avraham, "active labour Zionist"); (6) retired printer, Tel Aviv 1963 (possibly the same as 5; not resolved); (7) Ata textile worker 1956; (8) Tel Aviv subscriber 1929; (9) Herzliya prize-draw 1950 (unresolved); (10) father of Hania, Łódź, 1947 (new lead). None is established as our man.

### B-3. `קוטנר צאלים` — 9 hits
| Section id | Date, title | Reading | Grade |
|---|---|---|---|
| mar19720211-01.2.192 | Maariv 11.2.1972, classifieds | apartment ad signed "קוטנר" (Givatayim) and, in another ad on the same page, a flat on "רח' צאלים" in Holon | irrelevant: co-occurrence in classifieds |
| mar19881104-01.2.357, mar19881202-01.2.337, mar19900126-01.2.354, mar19900413-01.2.296, mar19900824-01.2.341, hadashot19911220-01.2.155 | Maariv/Hadashot radio and TV listings | "קוטנר" = Yoav Kutner (OCR "•ואב" in 19881202 and 19900126); "צאלים למזכרת" is a radio programme | irrelevant (Yoav Kutner presumed) |
| mar19900406-01.2.401 | Maariv 6.4.1990, listings | phrase "יואב קוטנר" confirmed | irrelevant |
| bamahane20011130-01.1.27 (PAGE) | Bamahane 30.11.2001 | article on soldiers on Galei Zahal programmes: host Yoav Kutner; a gunner "מבסיס צאלים" | irrelevant (IDF base, radio host) |

### B-4. `קוטנר דימונה` — 40 hits
26 are Yoav Kutner programme pages (`"יואב קוטנר" דימונה` = 26: bamahane19780308-01.1.26; mar 1982 ×11; dav19820513-01.2.101; hadashot 1984 ×6; mar19860207-01.2.262; mar19860211-01.2.93; mar19860425-01.2.278; mar19870227-01.2.281; bamahane19890301-01.1.35; kolhair19890714-01.2.140; hadashot19900216-01.2.182), where "דימונה" comes from other items (post-office hours, the TV item "מבט אל דימונה"). The other 14:
| Section id | Reading | Grade |
|---|---|---|
| hzh19590202-01.2.40; hzh19590614-01.2.58; hzh19600804-01.2.37 | HaTsofeh marriage-registration lists: "יוסף קוטנר בן שייבוש, גרוש, פולין, ת"א"; "אלדד קוטנר בן צבי, ת"א—הרצליה"; "זונאידה קוטנר בת יוסף" | namesakes (other first names, residences) |
| hzh19600701-01.2.107.2; haretz19601030-01.2.90.1; mar19601103-01.2.73; hzh19680922-01.2.142.1 | "הרב קוטנר", "אברהם א. קוטנר — רב העיר לוד" | namesake: Rabbi of Lod |
| seferhaketovot19631001-01.1.61; seferhaketovot19651001-01.1.67 (PAGE) | directory index pages: "קוטנר, סלמה" | irrelevant: index entries, no residence |
| dav19650212-01.2.148.7 | "קבלנים אחים קוטנר, רח' בלפור 8, בת־ים" (apartment ad) | namesake (building contractors) |
| hayomisr19691109-01.2.51.1 | "אחים קוטנר" (firm in an ad) | namesake |
| ahr19701102-01.2.77.1 | funeral notice, Tel Aviv, families "איזנשטדט, דדמן, ברזילי, קוטנר, וולפובסקי" | namesake (Tel Aviv family, Kiryat Shaul) |
| mar19730211-01.2.191 | table in a readers' feature: "קוטנר, דגיו" | irrelevant |
| mar19730314-01.2.156 | military honours list: "רב"ט קוטנר גדעון — בית השיטה" | namesake (Beit HaShitta) |
No item places a Kutner at Dimona.

### B-5. `קוטנר "באר שבע"` — 140 hits
79 are Yoav Kutner programme pages (`"יואב קוטנר" "באר שבע"` = 79). The 61 others (12 contain "יואב" apart from the phrase):
| Group | Section ids | Reading | Grade |
|---|---|---|---|
| **NEW** | **hzh19490509-01.2.31** | HaTsofeh 9.5.1949, marriage registrations at the Haifa Chief Rabbinate (plus a block at the Be'er Sheva rabbinate): "מרדכי, מלוטק, חיפה שרר, קוטנר., חיפר" (OCR; "שרר" = שרה) | **NEW lead**, see D-3 |
| dressmaker | haretz19510406-01.2.57; haretz19510518-01.2.48 | "ש. קוטנר, ת"א, צבי גרץ 11א'" (maternity-dress seamstress; same ads 1949–1954 under "שרה קוטנר") | namesake (Tel Aviv, Zvi Graetz 11A) |
| estate | haretz19510521-01.2.44.2 | estate notice: Gershon Kutner of Tel Aviv–Jaffa, d. 21.3.1951 | namesake |
| Gur hasid | shar19510712-01.2.24.2; shar19540326-01.2.19.2; shar19551201-01.2.22.1 | "ר' ליבל קוטנר" greetings | namesake (Reb Leibel Kutner) |
| tutor/stations | mar19521005-01.2.16; mar19550626-01.2.32; mar19560615-01.2.59 | "קוטנר, רח' חובבי ציון ת"א" (bookkeeping tutor); registration-station lists | namesake |
| candidates | hzh19550712-01.2.65 | "ד"ר שמשון קוטנר, מנחלת גנים" withdraws from the Agudat Yisrael list | namesake |
| marriages | hzh19571201-01.2.29; hzh19601228-01.2.44; hzh19700312-01.2.48 | "חיה קוטנר בת זלמן"; "א. קוטנר (רוקה) בסרביה"; "קוטנר אסתר בת אריה (רוקה) צרפת—חיפה" | namesakes (women) |
| sport | hrt19580601-01.2.50 | athletics: "קוטנר מאכ"א חיפה" (the runner Eldad Kutner) | namesake |
| Rabbi of Lod | hzh19590611-01.2.102.5; haretz19601030-01.2.90.1; hrt19601103-01.2.73.1 | "הרב קוטנר" | namesake |
| chess | hzh19590814-01.2.71 | "קוטנר (גרמניה המזרחית)" | irrelevant |
| directory | seferhaketovot19631001-01.1.61 (PAGE) | index page | irrelevant |
| classifieds | mar19640422-01.2.90; mar19651126-01.2.104; haretz19681206-01.2.28.8; haretz19681213-01.2.36.9; mar19721015-01.2.253; mar19721029-01.2.255 | sale/rental ads by "קוטנר", "אחים קוטנר" (contractors, Bat Yam/Tel Aviv) | namesakes |
| list | haretz19690822-01.2.165; lmrv19690826-01.2.95; hayomisr19690827-01.2.103; khm19690827-01.2.62 | numbered name list: "270. קוטנר יעקב, כפר־יונה" next to "271. קוט מאיר, באר־שבע" | namesake (Yaakov, Kfar Yona); the Be'er Sheva name is another surname |
| letter | mar19690916-01.2.175 | letter writer "י. קוטנר" | namesake |
| Yoav (forename broken or separate) | mar19790802-01.2.331; dav19810420-01.2.157; dav19820603-01.2.133; mar19860221-01.2.256; hairtlv19871023-01.2.80; mar19880219-01.2.346; mar19880401-01.2.424; hadashot19880810-01.2.122.2; mar19881104-01.2.357; mar19881111-01.2.393; mar19881202-01.2.337; mar19881230-01.2.271; mar19881230-01.2.291; mar19890106-01.2.358; mar19890210-01.2.329; mar19890217-01.2.355; mar19900105-01.2.339; mar19900112-01.2.397; mar19900126-01.2.354; mar19900309-01.2.346; mar19900413-01.2.296; mar19900629-01.2.352; mar19900727-01.2.378; mar19900824-01.2.341; mar19900919-01.2.312; mar19920124-01.2.251; mar19820531-01.1.15 (PAGE, "ישעיהו קוטנר") | radio/TV listing pages and features | irrelevant (Yoav Kutner presumed); the PAGE item names a "Yeshayahu Kutner", unidentified |
| other | mar19870123-01.2.252; hadashot19880225-01.2.87; bamahane19891213-01.1.56 | puzzle winner "אסף קוטנר, ראשל"צ"; address list "קוטנר ישראל ושושנה, הגליל 79, גניה תקוה"; crossword clue | irrelevant / namesake |

### B-6. `קוטנר`, 1.3.1986 – 30.4.1986 — 48 hits
44 = phrase "יואב קוטנר" (Maariv, Hadashot, Hair, Kotert, Bamahane, radio/TV listings and interviews, 2.3 – 29.4.1986). The other four: hadashot19860302-01.2.201 (programme "רדיו רדיו — קוטנר": Yoav), kolhair19860418-01.2.91 (a column on a radio character "מאקס קוטנר, הפרופסור המטורף"), hadashot19860429-01.2.80 (a letter on the radio), bamahane19860409-01.1.21 (interview page of Yoav). **There is no ADVERTISEMENT-type hit (the type of death notices) at all**, and the only hits between 19.3.1986 and 31.3.1986 are two weekly magazines (kotert19860319-01.2.19, hairtlv19860321-01.2.148), both about Yoav Kutner. Given the coverage table above (no Maariv for March 1986; no Davar/Haaretz; Hadashot partial), the March window is an absent source, not evidence of absence. For April 1986 the Maariv index is present (1,409 sections, 273 of them advertisements) and holds no advertisement-type section with "קוטנר" (the 30-day memorial would fall about 17–18.4.1986).

### B-7. Yiddish
| Section id | Date, title | Reading | Grade |
|---|---|---|---|
| jugntweker19300801-01.2.15 | Yugnt Veker (Warsaw) 1.8.1930 | Tsukunft regional gathering at Kutno; Ozorków among 17 towns | irrelevant ("קוטנער" = of Kutno) |
| bajsjakow19330823-01.2.15 | Beis Yaakov (Łódź) 23.8.1933 | teachers' conference; a delegate "Barzhitski (Ozorków)"; "Miss Kutner — Łuków" | irrelevant |
| dosyudishetogblat19341126-01.2.33 | Das Yidishe Tageblat 26.11.1934 | press campaign; "Kutno youth"; Ozorków in a list of silent towns | irrelevant |
| frw19360709-01.2.28 | Forverts 9.7.1936 | anti-Jewish riots in Poland (Kutno; Ozorków cemetery) | irrelevant |
| najerfolksblatlodz19370827-01.2.79 | Naye Folksblat (Łódź) 27.8.1937 | Yosef Kutner of Ozorków | **KNOWN** |
| erecisrael19190501-01.2.29; erecisrael19190601-01.2.27 | Eretz Israel (Warsaw) 1.5.1919, 1.6.1919 | issue-sized donor lists (50,352 and 34,745 words): "Kutner" appears in other towns' entries and "אוזורקוב" in separate Zionist youth-society entries | irrelevant |
| idisheradvokat19070719-01.2.15; hyt19261121-01.2.17.1; dertog19471111-01.2.67; frw19471112-01.2.65; frw19540507-01.2.79; dertog19590418-01.2.66.3; dernayermoment19630322-01.2.33.2 | Cape Town 1907; Warsaw Haynt 1926; New York 1947, 1954, 1959; São Paulo 1963 | `"אברהם קוטנער"`: hospital list, ad, an article on a Yiddish journalist from Brazil meeting his brother Avraham Kutner, "an active labour Zionist", an actress's obituary naming a brother Avraham, an obituary ad, and a São Paulo ad listing "אברהם קוטנער און פאמיליע (תל אביב)" | namesake(s) (Poalei-Zion Avraham of Tel Aviv and unrelated Americans) |
| frw19460824-01.2.18 | Forverts 24.8.1946 | fiction serial; names "Kutner Abram, David, Fishel" in a Warsaw scene | irrelevant (fiction) |

### B-8. Spelling variant "קיטנר" — found only after the first sweep
| Section id | Date, title | Reading | Grade |
|---|---|---|---|
| **hzh19520318-01.2.49** | HaTsofeh 18.3.1952, "פרסום הרושמים לנישואין", block "במשרד הרבנות בבאר שבע" | "אברהם קיטנר . צאלים. רוק … צפורה בלם צאלים רוקה" | **NEW, near-certain**: see D-1 |
| **hbkr19470120-01.2.32** | HaBoker 20.1.1947, news and "persons sought" column | "אברהם קיטנר מארזי. מתבקש על ידי קרוביו בחו"ל" | **NEW, probable**: see D-2 |
| dav19281225-01.2.31.1; dav19290127-01.2.35.1 | Davar 25.12.1928, 27.1.1929 | `"קיטנר אברהם"` in ads | namesake (adult in Palestine, before 1929) |
| lmrv19550617-01.2.76 | Lamerhav 17.6.1955, Book-week selling stations | "קיטנר אברהם, רח' קצנלסון 147" (Givatayim) | namesake: bookseller |

## C. Not done / blockers
- JPress page images are locked (copyright): only OCR was read; no page image was viewed.
- `jpress_search` hides the ids of PAGE-type hits (shown as empty titles); all PAGE hits above were recovered through the raw JSON.
- Maariv March 1986, Davar after June 1985, Haaretz after 1971 and any daily after 1993 are not in JPress: death and memorial notices for 1986 and 2006 cannot be searched here. Other sources for the 1986 notice are named in `research_findings.md` (Hebrew obituary pages in the National Library's microfilm of Maariv/Davar, the Beersheba burial society).
- The bare Yiddish "קוטנער" (3,386) and its post-1944 subset (831) were not read item by item.
- OCR spellings other than "קוטנר", "קיטנר", "קוטינר", "קוטנער" were not swept (for example "קוטגר", "קוטנו", "קוטנך").
- Not read: `hzh19490509-01.2.31` beyond the OCR text, and no second newspaper was found carrying the same Haifa list.

## D. NEW items (not in the report or in the "already known" lists), with the reason each might matter
| # | Section id | What it says (OCR) | Why it matters | Grade |
|---|---|---|---|---|
| D-1 | **hzh19520318-01.2.49** (HaTsofeh 18.3.1952) | At the Be'er Sheva rabbinate: "אברהם קיטנר . צאלים. רוק" and "צפורה בלם צאלים רוקה" (both of Tze'elim, bachelor and spinster). Another Tze'elim couple precedes them ("יעקב מריאש", "חנה מיגץ"; OCR) | The couple's marriage registration: date (about March 1952), place (Be'er Sheva rabbinate), both single, both at Tze'elim, Tzipora's maiden name "Blam". Fits the daughter's account that they married at the Be'er Sheva rabbinate and returned to the kibbutz the same evening; the report has no marriage date | near-certain (כמעט ודאי): two rare names together, same kibbutz, marital status; surname printed "קיטנר" |
| D-2 | **hbkr19470120-01.2.32** (HaBoker 20.1.1947) | "אברהם קיטנר מארזי. מתבקש על ידי קרוביו בחו"ל. פרטים אצל: [Fedshman/Shedman], Tel Aviv, HaTachana St. 7" | Relatives abroad were seeking an Avraham Kutner "of Ozorków (?)" in January 1947, a month before the Cyprus deportation, when he was in Italy. A contact in Tel Aviv is named. "מארזי" is probably a truncation of אוזורקוב (OCR/typesetting) | probable (ככל הנראה) |
| D-3 | **hzh19490509-01.2.31** (HaTsofeh 9.5.1949) | Haifa rabbinate marriage registrations: "מרדכי … מלוטק, חיפה" immediately followed by "שרה קוטנר, חיפה" | Possible marriage registration of Avraham's sister Sara (Sala) with Mordechai Mlotek; the report gives their marriage only as "to be verified" with no date. "Mlotek" is an uncommon surname; the adjacency is OCR order only (names in this list run in columns, not necessarily in couples) | probable (ככל הנראה); to be verified against the Haifa rabbinate register |
| D-4 | **dav19460301-01.2.54** (Davar 1.3.1946, notices) | "סלה קוטנר מאוזורקוב (פולין) מחפשת את סימה קורמן פפלויס. לפנות קיבוץ 'גשר' לסלה קוטנר" | Sala Kutner of Ozorków was at kibbutz Gesher in March 1946 and was looking for a Sima Korman (OCR variants in the notice: first mention "קופנר", second "קוטנר"; town "מאוזורקזב"; second surname "פפלויס"). The report has no date for Sara's arrival in Palestine (background knowledge, not from the sources: Gesher belongs to the Hashomer Hatzair / Kibbutz Artzi movement) | near-certain (כמעט ודאי): name, town of origin and the aunt named in D-5 |
| D-5 | **lakkarov19460516-01.2.13** (Lakrov Velarahok 16.5.1946, Jerusalem bureau) | "קורמאן סימה, מפלונסק (בת אחיה שרה קוטנר מאוזורקוב) 30054" | The aunt (Sima Korman of Płońsk, in Palestine) matched with "her brother's daughter Sara Kutner of Ozorków", file 30054: a paternal aunt of Avraham and Sara not in the family tree (the tree has aunts Rivka, Faiga, and uncle Fishel) | probable (ככל הנראה) |
| D-6 | **ahr19460123-01.2.33** (Al HaMishmar 23.1.1946); **hbkr19460123-01.2.29**, **hbkr19460124-01.2.35** (HaBoker 23–24.1.1946) | Lists of the "Enzo Sereni" ma'apilim (reached Haifa, held at Atlit): Al HaMishmar names "שרה קוטנר" among the Hashomer Hatzair group from Poland; HaBoker of 23.1 gives her birth year as 1924 and the full list of 24.1 gives "קוטנר שרה (22)" and, a few lines later, a second Sara Kutner aged 23 | Sara's aliyah (January 1946, 22–23 years old; the report: b. 14.8.1922). Two Sara Kutners were aboard, so which one is she is not settled; the Polish Hashomer Hatzair group fits kibbutz Gesher | probable (ככל הנראה) |
| D-7 | **haretz19421117-01.2.66** (Haaretz 17.11.1942, Jewish Agency information bureau) | "סימה קורמן בסאמארקאנד — אל שלום כהן ויוסף נויפלד" | A Sima Korman was a refugee in Samarkand in 1942, writing to Palestine; plausible the same Sima Korman as D-5 (identity not proven) | to be verified (טעון אימות) |
| D-8 | **lakkarov19470403-01.2.7** (3.4.1947) | entries 44956–44958, e.g. "(בת אחיהם, האניה בת אברהם קוטנר)" (the other entries name Zolberg Noah and Sara née Kutner, Berlinski Dvora née Kutner, Goldschmidt Avraham) | Palestine residents (aunts Sara Zolberg and Dvora Berlinski, both née Kutner) searching "Hania, daughter of Avraham Kutner of Łódź", in Germany. Not our Avraham (a father), but a Kutner family of Łódź not yet in the tree | unlinked; kin not proven |
| D-9 | **shar19450712-01.2.5** (Sha'arim 12.7.1945) and **lakkarov19450712-01.2.27** | "ישראל קוטנר מאלכסנדר ליד לודז, נכדו של הרה"צ ר' ישעיהו … ניצל במחנה דאכאו"; Lakrov: "ידיעה בשבילו מישראל קוטנר ששוחרר בדכאו" | A Dachau-liberated Israel Kutner of Aleksandrów, grandson of a tzaddik, in July 1945. Arolsen has Dachau no. 110139, Israel Kutner b. 14.1.1912 "Alexandrov" (docs 130432428, 10164168, 10690327), which would fit this man; if so he is not the unresolved Dachau Izrael Kutner b. 13.11.1897 Litzmannstadt no. 96029 (docs 130432198, 10690326) | helps narrow the Dachau row: the press item is probably about no. 110139, leaving no. 96029 open |
| D-10 | **dav19670628-01.2.54.3** (Davar 28.6.1967, Six-Day War condolence ad to the Haifa Tzur family) | "צפורה ואברהם קוטנר" among signatories with the Dimentman family and the Burstein family of Montevideo | A couple with exactly our first names; bereaved are Avraham, Pnina and Eitan Tzur (Haifa; the father a former POW in Germany) | low probability: no place, no kibbutz; unresolved |
| D-11 | **ahr19491004-01.2.44** (Al HaMishmar 4.10.1949, HIAS inquiry list) | "קוטנר בנימין נולד ב־1914 בקונסטנטין ע"י לודז, מקודם בקפריסין" | A Kutner from the Łódź region, ex-Cyprus, in Israel in 1949; (also lakkarov19461003-01.2.9: "דוד קוטנר מקונסטאנטינוב") | possible relative; weak |

## Summary
The re-run of the exact-name queries reproduces the known items (24.3.1947 ship list; 21.10.1953 notice; 1937 Ozorków item) and shows that every other "אברהם קוטנר" in JPress is a namesake (a Jerusalem candidate of 1920, the Rabbi of Lod, the Tel Aviv Poalei-Zion Avraham who died on 26.12.1976, a retired printer, an Ata worker, and others); the co-occurrence queries with צאלים, דימונה, באר שבע and March–April 1986 yield nothing about him, because their hits are almost all the radio host Yoav Kutner. The 1986 obituary cannot be found in JPress at all, since the index holds no Maariv for March 1986 and no Davar or Haaretz for that year. The sweep, however, found by the variant spelling "קיטנר" the most useful item so far: HaTsofeh of 18.3.1952 lists Avraham and Tzipora Blam, both of Tze'elim, registering for marriage at the Be'er Sheva rabbinate. It also gave a probable January 1947 notice that relatives abroad sought him as an Avraham of Ozorków, and a chain of items for his sister Sara: ma'apilim list of January 1946, kibbutz Gesher in March 1946, the aunt Sima Korman in May 1946, and a probable 1949 marriage registration with Mordechai Mlotek.
