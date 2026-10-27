# Yaakov Blumenthal: grandparents and great-grandparents sweep, 27.10.2026

Scope: push the line back from Benő (Moshe Ben Zion) Blumenthal b. 20.7.1892 Nógrádbercel and Ida (Chava) Deutsch b. 6.11.1887 Boldogasszony/Frauenkirchen. Targets: Mór Blumenthal and Regina Wozner (Bercel); József Blumenthal and Johanna Klein; Meir Wozner and Fani Fleischmann; Gyula (Juda Julius) Deutsch and Netti Blumenschein (Frauenkirchen).

Method. JewishGen: the MCP detail pages (`jgdetail_2.php`) still return "0 matching record" even when the overview shows hits (re-confirmed today: `jewishgen_open` and `jewishgen_search_filtered` both returned 0 rows for a query whose overview said 4 hits). That zero is a blocker, not a negative. I read the real result lists in a logged-in browser (new tab, read-only searches, tab closed afterwards) through the site's own JSON endpoint `https://www.jewishgen.org/databases/recordlistjson.php?df=<db>&srch1=...` and through `record-list.php?df=...&srch1=...` for the screenshots. Database ids: Hungarian Births (HB) `3185094d-2b06-4838-978d-00a17d1d0460`, Hungarian Marriages (HM) `e2b6c85e-9347-4008-8003-c6ce7887422a`, Hungarian Deaths (HD) `091efbe0-b523-4134-aeff-501a5675d276`, Austria: Burgenland Marriages II (BM2) `97cbf3d8-3c64-4920-abea-22885fcbc6e5`, Burgenland Deaths II (BD2) `6a495931-4405-4780-a326-008fe68b32e0`, 1848 census `C1848N`. Arcanum: MCP `arcanum_search` and `arcanum_get_page_text` (OCR text only). Index rows are graded at most "likely" (ככל הנראה); nothing below was checked against a scan.

---

## A. Findings, most important first

### A1. Netti Blumenschein's parents and siblings (Ida's mother's side): NEW, one generation up

Ida's mother is Netti Blumenschein/Blumschein, b. 7.3.1859 Frauenkirchen, daughter of "Willhelm // Hani" (HB_0823944; already in the earlier Frauenkirchen file via her marriage, BM2_0000020, 11.11.1880, bride's father "Wilhelm BLUMSCHEIN"). Today's sweep finds the parents' own marriage and the family's births.

**Marriage, BM2_0000805** (Burgenland Marriages II; Frauenkirchen; film #700859, image 87, row 79-4; district Rajka; Moson). As shown:
`Frauenkirchen | 10-Jun-1852 | Groom: Wolf BLUMENSCHEIN, 26 | Groom's father/mother: Moses Jakob BLUMENSCHEIN / Eva | Bride: Hanni WOLF, 25 | Bride's father: Josef WOLF | "Groom and bride from Frauenkirchen"`.
URL pattern: `https://www.jewishgen.org/search/record-list.php?df=97cbf3d8-3c64-4920-abea-22885fcbc6e5&srch1=Blumenschein&srch1v=S&srch1t=Q&srch2=Frauenkirchen&srch2v=T&srch2t=Q&srchbool=AND&dates=all&recstart=0&recjump=0`.
Screenshot: `img/jewishgen_BM2_0000805_frauenkirchen_1852_wolf_blumenschein_hanni_wolf_and_1882_fani_gerstel.png` (the same crop shows A1.4).

**Why Wolf = Wilhelm = Vilmos** (the same man under three forms):
1. HB (screenshot `img/jewishgen_HB_frauenkirchen_blumschein_wilhelm_wolf_hani_netti_1859.png`): the father is "Wilhelm" in 1855, 1857 and 1859 (Netti), and "Wolf" in 1861 and 1864; the 1861 baby (Isak) has "Sandak Wolf BLUMSCHEIN".
2. BM2_0000999, Frauenkirchen 3.1.1882: A. Moritz GERSTEL (26, son of Israel) married **Fani BLUMENSCHEIN**, "Bride's father: Wolf BLUMENSCHEIN". Fani b. 24.5.1857 is a daughter of "Wilhelm // Hani" in HB_0823862, so Wolf = Wilhelm.
3. BD2_0002976, Frauenkirchen 2.7.1894: "BLUMENSCHEIN, Johanna, 74 ... Born Frauenkirchen, widow, was married to Vilmos BLUMENSCHEIN, maiden name WOLF" (film #701094, image 342, row 163-9). Johanna = Hani/Hanni (Hanni WOLF of 1852). Screenshot: `img/jewishgen_BD2_frauenkirchen_blumenschein_johanna_1894_widow_of_vilmos_nee_wolf.png`.
4. Husband's death: BD2_0002425, 20.6.1881, "BLUMSCHEIN, Wolf, 56 ... Born Frauenkirchen" (film #700859, image 192, row 33-12): b. about 1825, groom aged 26 in 1852. Fani's wedding (Jan 1882) is after this death, which fits "Wolf Blumenschein" in the bride's father field without comment.

**Children of Wilhelm/Wolf and Hani, from HB Frauenkirchen (film #700859), as shown** (father // mother; record no.):

| id | name | born | father // mother | register ref. |
|---|---|---|---|---|
| HB_0823663 | BLUMENSCHEIN, Regina | 03-Mar-1853 F | Wilhelm // Hany | 91/83-4 |
| HB_0823730 | BLUMENSCHEIN, Josef | 10-Jul-1854 M | W. // Hani ("Sandak M. BLUMENSCHEIN") | 96/88-27 |
| HB_0823786 | BLUMSCHEIN, Ignatz | 09-Nov-1855 M | Wilhelm // Hani ("Sandak Josef TOPF") | 102/94-37 |
| HB_0823862 | BLUMSCHEIN, Fani | 24-May-1857 F | Wilhelm // Hani | 111/103-22 |
| **HB_0823944** | **BLUMSCHEIN, Netti** | **07-Mar-1859 F** | Willhelm // Hani | 120/111-9 |
| HB_0823991 | BLUMENSCHEIN, "--" | 25-May-1860 F | Wolf // Hani ("Unnamed girl. Died.") | 124/115-19 |
| HB_0824052 | BLUMSCHEIN, Isak | 18-Oct-1861 M | Wolf // Hany ("Sandak Wolf BLUMSCHEIN") | 129/120-36 |
| HB_0824093 | BLUMENSCHEIN, Cecilia | 03-Jan-1863 F | Wilhelm // Hani | 136/127-1 |
| HB_0824140 | BLUMSCHEIN, A. / Josef | 30-Mar-1864 M | Wolf // Hanni ("Sandak Josef SCHIMMEL") | 141/132-12 |

The marriage of 10.6.1852 plus a first child on 3.3.1853 fits. Infant deaths in BD2 that fit (parents not named in the rows, so only "consistent"): Regina 26.8.1853 (age 1), Josef 2.12.1855, Ignatz 16.9.1856, Cecilie (Blumenschein) 23.6.1863. Naming pattern: Ida's brother "Ignatz" (b. 1883) and "B. W." = Bernát Vilmos (b. 1885, d. 1886), after Netti's brother Ignatz and her father Vilmos (already in the Frauenkirchen file).

**Grade: ככל הנראה (likely) that this couple are Netti's parents.** Netti's own HB row names "Willhelm // Hani"; BM2_0000020 names "Wilhelm BLUMSCHEIN" as her father; the 1894 death row ties Hani/Johanna née Wolf to "Vilmos". Open point: Johanna's age at death (74, so b. about 1820) does not match "25" in 1852 (b. about 1827); ages in these registers are loose, so not a contradiction, but note it.

**Possible next generation (grade: טעון אימות).**
- BD2_0002608: "BLUMSCHEIN, Eva, 83, d. 12-Jan-1870, Born Frauenkirchen, married" (film #700930, image 297, row 125-3). Possibly Wolf's mother Eva, wife of Moses Jakob.
- BD2_0002727: "BLUMSCHEIN, Jakob, 90, d. 01-Oct-1876, Born Frauenkirchen, widower" (film #701049, image 306, row 132-16). Possibly Moses Jakob. Eva was "married" when she died in 1870 and Jakob a "widower" in 1876: consistent. Nothing states the relationship.

### A2. Bercel, József Blumenthal (Mór's father): 1870 legal notice (Arcanum, OCR)

Budapesti Közlöny, 2 Sept 1870, p. 37 (document `BudapestiKozlony_1870_09`, page index 37; the same notice again 3 Sept, page 59). OCR text as returned:
"HIRDETMÉNY. 375. Berczelly Vilmosnak Blumenthal József elleni két rendbeli, 700 frt és 150 frt haszonbér iránti ügyében 1869. november 11-én és 1870. mártius 15-én Berczelen foganatositott biztosítási végrehajtások alkalmával következő ingóságok foglaltattak le: 30 db birka, becsülve 1050 ftra; 4 db ökör ... 1 fekete ló ... összegen: 1760 frt ... Kelt Szandán, 1870. augustus 28-án. Korodinyi Lajos, szbiró."
Meaning: Vilmos Berczelly sued "Blumenthal József" for 700 and 150 forints of lease rent (haszonbér); on 11.11.1869 and 15.3.1870 distraint was carried out in Berczel (30 sheep, 4 oxen, horses, a cart, grain; total 1,760 fl.). It shows a József Blumenthal leasing land in Bercel in 1869–70. Same name and place as the Senkiföldjén József (b. 1834/36, big landholder, d. 1892/93; HD_0196202 "Landowner ... b. Berczel"), but nothing in the notice gives parents or age. URL: https://adt.arcanum.com/en/view/BudapestiKozlony_1870_09/?pg=37 (and pg=59). **Grade: ככל הנראה** (same man as József of A4/HD_0196202), identity by name and place only. The claimant Berczelly Vilmos is also listed in the 1899–1900 Nógrád landowners list (A5), so Bercel's Berczelly family were landlords of the Blumenthals, which fits a tenant-then-owner trajectory (the book calls Mór "bérlő/tenant" in places).

### A3. Mór Blumenthal: occupations 1883 and 1892 (Arcanum, OCR)

- **Közgazdasági Értesítő, 18 Oct 1883, page index 508** (printed p. 1176; document `BME_KozgazdasagiErtesito_1883_2`): the article is "Magyarország nevezetesebb borkereskedőinek név- és lakjegyzéke 1883-ban" (list of Hungary's notable wine merchants, from the chambers of commerce, compiled by the national viticulture commissioner). Under the Budapest chamber: "**Bérczel. (Nógrád megye.) Blumenthal Mór.**" URL https://adt.arcanum.com/en/view/BME_KozgazdasagiErtesito_1883_2/?pg=508. A wine merchant in Bercel aged about 30.
- **Központi Értesítő, 16 June 1892, page index 807** (document `Kozponti_Ertesito_1892_1`), firm register of the Balassagyarmat court ("gyarmati törvényszék"): "1892. jun. 1. 4225. sz. 459/1 | **Blumenthal Mór** | Főtelep Nógrád-Berczel | Blumenthal Mór, vegyeskereskedő, Berczelen". The line above is the same kind of entry for Rosenfeld Miksa (4227). Meaning: on 1 June 1892 Mór Blumenthal registered a mixed-goods shop firm in Bercel. This is seven weeks before Benő's birth (20.7.1892). URL https://adt.arcanum.com/en/view/Kozponti_Ertesito_1892_1/?pg=807.
Both match the "merchant" Mór of HD_0206772 (Johanna's 1903 death notice: "Reported by son Mór BLUMENTHAL, merchant in Berczel"). **Grade: כמעט ודאי (almost certain) for "a Mór Blumenthal, merchant, in Bercel"; ככל הנראה that he is the Mór of the death record** (only one Mór in Bercel found in these sources).

### A4. Johanna Klein's widowhood (Arcanum, OCR): "Özv. Blumenthal Józsefné", 1899–1900

"Magyarország földbirtokosai és bérlői" (Gazdacímtár), 1899–1900, Nógrád county landowner list, page index 18 (printed 15; document `CimtarakTelefonkonyvek_MagyarorszagGazdacimtara_1899-1900`): the names column reads "Blumenthal Jakab / Özv. Blumenthal Józsefné / Blumenthal Márton". The OCR separates the columns (names, residence, post office, acreage), so her residence and acreage cannot be paired with the name from text; the scan is needed. Same volume, page index 26: "Blumenthal Dávid — Bérczel — Bérczel — 197" (a different Bercel Blumenthal). URL https://adt.arcanum.com/en/view/CimtarakTelefonkonyvek_MagyarorszagGazdacimtara_1899-1900/?pg=18. **Grade: טעון אימות** as to which widow and where, but József's widow is the obvious reading: József d. 13.12.1892 (HD_0196202), Johanna d. 26.2.1903 (HD_0206772).

### A5. Weak, for completeness
- Pesti Hírlap, 30 Mar 1894, page index 592: donation list headed "Nógrád Bercel Veres Ernő úr gyűjtése ... Blumenthal Mór 30 kr". Magyar Nemzet, 21 Jan 1900, page index 371: list including "Blumenthal D 10 kr", "Berczelly V...", "Blumenthal Mórné 25 kr". These show Mór and his wife in Bercel donor lists but give no new facts. טעון אימות.
- Losoncz és Vidéke, 4 Dec 1892, page 125: a list with "Blumenthal Fülöp Csécse" and "Berczelly Vilmos Bérczel": other persons.

### A6. Deutsch Gyula of Boldogasszony: a candidate for Ida's father (Arcanum, OCR)

Központi Értesítő, 1 Mar 1903, page index 310 (`Kozponti_Ertesito_1903`), for the Boldogasszonyi Takarékpénztár (Frauenkirchner Sparkassa): "Oesterreicher Bernát helyébe czégjegyzési jogosultsággal **Deutsch Gyula magánzó boldogasszonyi lakos** választatott meg igazgatósági taggá." The same bank's board lists "Deutsch Gyula" in the Magyar Compass 1903–1917 and Pénzügyi Compass 1905–1918; Központi Értesítő 25 July 1921, page index 738: "a lemondott Deutsch Gyula helyébe dr. Detre Béla kereskedő boldogasszonyi lakost három évre igazgatósági taggá" (Deutsch Gyula resigned; Dr. Béla Detre elected in his place). URLs: https://adt.arcanum.com/en/view/Kozponti_Ertesito_1903/?pg=310 and https://adt.arcanum.com/en/view/Kozponti_Ertesito_1921/?pg=738. A "Deutsch Gyula, magánzó (private means)" of Boldogasszony, alive 1903–1918 and gone from the board by mid-1921, fits Julius b. 1848 (merchant in 1887, rentier at 55). **Grade: טעון אימות**: name and town only; Frauenkirchen could have had another Gyula Deutsch (the Deutsch family there is large). No death notice found.

### A7. Corrections to earlier notes, from today's reading
- The earlier Nógrádbercel file suggests "Zsanka BLUMENTHAL, widow, 80, d. 9-Jan-1894 (HD_0196263)" might be József's mother. **Not plausible**: József is 62 at his death on 13.12.1892 (b. about 1830), so a mother b. about 1814 would be 16. Zsanka is of the generation of József's wife or older relatives. József's mother remains unknown (the book's "Hani Blumenthál, b. 1804 in Batorkeszi (as transcribed in the earlier Senkiföldjén note), d. 1856 Bercel" is a better age fit, still טעון אימות).
- "BLUMENTAL, Mojer, 15-Nov-1853, Simon // WEISZ Juli, born Busa" (HB_0511317, Szécsény Orthodox births) matches Mór's age loosely (Mór was "67" on 6.6.1920, b. between 7.6.1852 and 6.6.1853) but not his parents (József // Johanna Klein) or his birthplace: **excluded**.

---

## B. Negatives (query, database, coverage, result)

"Real zero" = the site returned a results page that said 0 / "No matches found". "Not indexed" = the database does not cover the place and years, so the zero says nothing.

| # | Query | Database | Coverage | Result |
|---|---|---|---|---|
| 1 | Marriage of Mór Blumenthal and Regina Wozner/Wosner/Wuszner (about 1875–1892): surname Blumenthal (phonetic), all 98 rows read; groom age 20–40, years 1872–1892 | HM (Hungarian Marriages) | HM includes Balassagyarmat 1851–1895 and Dunaszerdahely; no Bercel civil marriages after 1895 | 98 rows; the only Blumenthal grooms from Bercel are Jakob (1868, Dunaszerdahely) and Mózes (1881, Dunaszerdahely); **no Mór × Regina**. Real zero for this couple; not conclusive. |
| 2 | Wosner and Wozner (phonetic), all rows (HB 140+149, HM 54+56, HD 30+34), filtered for Nograd, Berc*, Balassagyarmat, Szécsény, Szirák, Vác, Losonc | HB, HM, HD | as above | **No Wosner/Wozner row from Nógrád/Bercel.** Almost all rows are Dunaszerdahely (Pozsony county), Szatmár, Abaújszántó, Budapest. |
| 3 | Birth of a Regina/Rebeka Wosner/Wozner, 1852–1860 | HB, all 289 Wosner/Wozner rows | HB years vary by registry | 0 rows. |
| 4 | Wozner with mother "Fleischman" | HB, HM, HD | | 20 rows with a Fleischman mother, all Dunaszerdahely: Salamon Wozner × Betti Fleischman (children 1878–1890); **no Meir × Fani**. Different family (Fani Fleischmann's husband Meir does not appear). |
| 5 | Wuszner Leni (HM 1868): parents "Marton / Fani" | HM, HB | | The Wuszner/Wozner of Dunaszerdahely (HB: Cheidel 1852, Wilhelm 1855, Johan 1859, all "Marton // Fani") are not Regina's family (hers is Meir // Fani Fleischmann); both Bercel Blumenthal marriages in HM (1868 Jakob × Leni Wuszner; 1881 Mózes × Betti Weiss) were in Dunaszerdahely, so Bercel Blumenthals married into the Dunaszerdahely/Csallóköz area: a regional hint for Regina, no proof. |
| 6 | Births of József's children (Mór about 1852/3, Hermin about 1862, Lina) or of Mór's children with Regina (Dávid Herman 1877, Hanna 1879, Sára 1884/5, etc.) | HB Blumenthal (phonetic, 250 rows); HB with town Bercel (1,715 phonetic rows, 10 Nógrád rows, none Bercel-born Blumenthal); HB any-field "Berczell" (42 rows, 27 Nógrád, all surname Berczeller) | HB has the Szécsény Orthodox births 1852–1867 (Nógrád Megyei Levéltár; 33 Blumenthal-related rows, all villages around Szécsény: Halászi, Locz, Nagyzellő, Busa) and Balassagyarmat 1850–1880 | **No Bercel Blumenthal birth.** The Szécsény register contains Blumenthal births (Joachim × Ulmer, Majer × Oppenheim, Jakob × Gelb, Bernát Kohn × Blumenthal) but no József × Johanna Klein and no Bercel place of birth. |
| 7 | József Blumenthal or Johanna Klein in HB/HM/HD with father József | all | | HB: 11 rows with father József, none from Nógrád. |
| 8 | Julius Deutsch / Netti Blumenschein marriage | BM2_0000020, Bruck an der Leitha 1880 (already known) | | confirmed, nothing new. |
| 9 | Death of Nathan Deutsch (b. 1812) and Sara née Bernath, or Fani Deutsch (mother, "60" in 1848) | BD2 (Frauenkirchen, to about 1894): surname Deutsch + Frauenkirchen (112 rows), contains "Natan"/"Nathan"/"Naten" (17/55/0), Bernath + Frauenkirchen (0 in BD2, 0 in HB, 1 in BM2 = the 1845 marriage) | Frauenkirchen deaths to about 1892 | **No Nathan Deutsch or Sara death in BD2.** Fani widow, 72 (26.4.1865, BD2_0002492) and Fani widow, 85 (14.6.1870, BD2_0002616) are both possible for the 1848 "Fany 60"; no data to choose. Nathan's father ("DEITSCH", name not given on the 1845 marriage) not identified. |
| 10 | 1848 census, Boldogaszony, surname starting "Blum" | C1848N | Moson ✓ | Only "BLUM Marrton, 46" (Szombathely) and "BLUMSAN Rozi, 54" (wife in HAMBURGER Ignacz's household). **Wolf/Wilhelm Blumenschein (b. about 1826) not found**; spelling or household-head variant not located. |
| 11 | JewishGen Family Finder: Blumenthal+Bercel, Blumenthal+Nogradbercel, Blumenthal+Balassagyarmat, Wozner+Bercel, Wosner+Bercel, Wozner+Balassagyarmat, Klein+Csitar, Blumschein+Frauenkirchen, Blumenschein+Frauenkirchen | JGFF | all phonetic | **Real zero ("No matches found") for all nine.** Deutsch+Frauenkirchen: 3 matches (contact details not copied; page blocked the text from being read). |
| 12 | FTJP (family trees): Blumenthal+Bercel | FTJP | | 26 rows: László Blumenthal × Fani Schiller line (Jakob b. 1835, Regina Rosa b. 1826) and David Blumenthál × Mirel Grünbaum line (b. 1834 d. 1904) plus Aron/Fülöp/Szerena etc. **No József, Mór, Benő, Wosner.** FTJP Deutsch+Frauenkirchen: 50 rows, from the 1848 census (Nathan b. 1812 with Rosalia; Julia b. 1846) and others, nothing beyond what the census gives. Wozner/Wosner+Bercel and Blumschein+Frauenkirchen: 0 / 0; Blumenschein+Frauenkirchen: 1 row (Isidor, 1852, other family). |
| 13 | JOWBR Austria, Deutsch + Frauenkirchen | J_AUSTRIA | | 5 rows; the 4 from Frauenkirchen are "DEITSCH, Toiva (LEVINTSER)", "Meir", "Iehuda (also Lib)", "Rivka": undated, no relationships; cannot be linked. |
| 14 | Burgenland Deaths (I), Deutsch+Frauenkirchen | `e6e753db-...` | | 2 rows (1901 Kadlburger Meyer; 1901 Deutsch Izrael, 70, father Lipót): not our family. |
| 15 | Yad Vashem names (exact): Wosner+Bercel; Wozner+Bercel; Wosner+Balassagyarmat; Blumenschein+Frauenkirchen | YV names (place on any of birth/war/death/residence) | | **Real zero**, no error. |
| 16 | MACSE: Wosner/Wozner/Woszner/Wuszner/Vozner/Wasner/Vosner (219 hits) | civil registers, today's Hungary | | Only one Nógrád hit: **civil deaths, Balassagyarmat, "Wosner" ×1** (member login needed; a lead, see C). Other: Budapest districts, Szombathely, Pápa, Csorna. **Church marriages, Nagymaros (Hont county): 33 Wozner/Woszner/Vozner rows** (a Wozner base near Visegrád; lead). MACSE Blumenthal given name Mór: Bercel civil births 4 hits (children named Mór, after 1895; not Mór's own birth). |
| 17 | RadixIndex surname pages Wosner / Wozner | all Radix databases | | Wosner: Dunaszerdahely (21 in RadixRef; 3 in the 1891 trade directory), Miskolc, Szombathely, Késmárk etc.; no Bercel or Nógrád. Wozner: Budapest, Nagymaros (Verlustliste). |
| 18 | Arcanum "Blumenthal Mór" + Bercel (1890–1925); + Berczel (1870–1925); "Blumenthal Mór nógrádberceli" (1890–1925); Blumenthal Berczel + elhunyt/meghalt/gyászjelentés (1900–1925) | Arcanum, all titles | Hungarian press and directories | Exact-phrase searches gave 3, 3, 1 and **0** hits. No obituary or death notice of Mór (d. 6.6.1920) or Regina (d. 30.9.1920). Hits read: A3/A5. |
| 19 | Arcanum "Wosner Bercel" (1860–1925) | all | | 2 hits, both irrelevant (a Wosner Bernát of Dunaszerdahely in a tannery list; a school list). A query using `OR` with Wozner variants returned 7,727 noise hits and was discarded. |
| 20 | Hungaricana archives: "Blumenthal Bercel"; "Wosner OR Wozner Nógrád" | Hungaricana archives (Budapest-city series only) | no Nógrád county series | 1 and 22 hits; the first is a 1921 Budapest notary item for "Blumenthal Dávidné özv. Lengyel Júlia" (Bercel resident; Dávid's widow, another branch); the Wosner hits are Budapest probate/criminal files, none Nógrád. |
| 21 | Arcanum page scans | | | Not viewable (see C2). |

---

## C. Blockers

1. **FamilySearch:** no token. Needed: film 700859 (Frauenkirchen/Boldogasszony Jewish births, marriages, deaths: the 1852 marriage image 87, births images 91–141, deaths 99–192), film 701094 (Johanna's 1894 death, image 342), Hungary Civil Registration for Nógrádbercel/Szirák; the Bercel/Szécsény/Balassagyarmat registers for 1850s–1880s.
2. **Arcanum scans:** opening a page in the browser gave "Your account is being used from another device. Please log out from other devices or try again in a few minutes." The MCP session and the browser share one Arcanum subscription. I did not log anyone out; no scan was viewed and **no Arcanum crop was saved**. All Arcanum text above is OCR only and should be checked against the scan before print (especially A4, where the column order is lost).
3. **JewishGen MCP detail pages** return "0 matching record" (confirmed again); I used the browser endpoint instead. The JGFF contact page for Deutsch+Frauenkirchen (3 matches) was blocked from reading by the browser tool.
4. **MACSE:** record-level detail needs a member login (Balassagyarmat "Wosner" death; Nagymaros church marriages).
5. **Not online, to be asked for:** the Nógrád county archive (NML IV. 7. c Öi. 986, the 1848 Jewish census of Bercel; Jewish community registers of Bercel/Balassagyarmat before 1895; the Gazdacímtár scan); Győr-Moson-Sopron county archive and the Burgenland Landesarchiv (Frauenkirchen Jewish register: Netti's and Ida's family; Nathan Deutsch's death; 1857 census: not online for Moson).
6. **1848 census of Bercel** and **1857 Nógrád/Moson**: confirmed not on JewishGen (see earlier file).

---

## D. Leads and recommended next steps (in order of expected yield)

1. **FamilySearch film 700859, image 87** (Wolf Blumenschein × Hanni Wolf, 1852): the entry should give both sets of parents and may add the Hebrew names. This is the only piece that can turn A1 from "likely" into "verified". Then images 183 and 46 (already in the earlier file) for Julius × Netti (1880) and Nathan × Sara (1845).
2. **Bercel, Mór's marriage.** Not in JewishGen. Candidates, by likelihood: (a) the Jewish community register of Bercel/Balassagyarmat 1870s (NML, Salgótarján), (b) a Dunaszerdahely-area marriage (Bercel Blumenthals married there twice, Wozner/Wosner families are concentrated there; HM has Dunaszerdahely to about 1895 but no Blumenthal × Wosner except Leni 1868), (c) Nagymaros area (MACSE: 33 Wozner church-marriage rows). Ask MACSE (free account) for "Wosner, Balassagyarmat deaths" and the Nagymaros rows.
3. **Senkiföldjén (NOGM_AFT_50, pg 438–439)** gives József's age (b. 1834/36), Johanna's parents (Klein Dávid × Schwartz Julianna, b. Csitár) and siblings Hermin (Gansl Izrael) and Lina (Hirschfeld Mór). Arcanum adds József as a Bercel tenant already in 1869–70. The book says József's parents are unknown; candidate parents are the László Blumenthal × Fani Schiller family (FTJP: Jakob b. 1835, Regina Rosa b. 1826) or Mózes (b. 1801); the FTJP researcher of that tree (David Blumenthál b. 1834) could be contacted through JewishGen/FTJP. **No evidence ties József to either.**
4. **Hermin Gansl (née Blumenthal), b. about 1862, d. Auschwitz 13.6.1944 aged 82** (HD_0206890; HD_0206889 Izrael, 80): the book names her as Mór's sister. Her children's HD rows (Mór b. 1887 d. 1931, Ignác d. 1943, Dávid) name "Hermin" as mother but not her parents. The 1898–1900 Gazdacímtár scan (A4) and the Arcanum 1870 notice can be re-checked on the scans once the Arcanum session is free.
5. **Ida's side**: ask the Frauenkirchen/Moson sources (Győr archive; Burgenland) for Wolf Blumenschein's and Nathan Deutsch's deaths; check Arcanum for a Deutsch Gyula death notice (1918–1925) and for the "Boldogasszonyi Takarékpénztár" board entry of 1921 (scan).
6. Do not rely on the MyHeritage-tree names ("Izsák Ignácz Blumenthál", "Sara Rosalia Deutsch née Brandt") for A1 or the Deutsch line: the registers say Sara Bernath (1845) and, for Netti, Wilhelm Blumschein and Hani/Johanna née Wolf.

## E. Files

- `img/jewishgen_BM2_0000805_frauenkirchen_1852_wolf_blumenschein_hanni_wolf_and_1882_fani_gerstel.png`
- `img/jewishgen_HB_frauenkirchen_blumenschein_wilhelm_hani_children_1853_1863.png` (spelling "Blumenschein": Regina, Josef, unnamed girl, Cecilia; also an unrelated Israel b. 2.1.1853 Joseph × Betty)
- `img/jewishgen_HB_frauenkirchen_blumschein_wilhelm_wolf_hani_netti_1859.png` (spelling "Blumschein": Ignatz, Fani, Netti, Isak, A./Josef; the last row, M. J. 1878, David × Netti, is another family)
- `img/jewishgen_BD2_frauenkirchen_blumenschein_johanna_1894_widow_of_vilmos_nee_wolf.png`
