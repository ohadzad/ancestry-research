# Auschwitz-Birkenau Museum — RSHA transports of Jews from Balassagyarmat, June 1944

- Source: Auschwitz-Birkenau State Museum, victims database / transports (https://victims.auschwitz.org/en/transports); client `auschwitz_search_transports`, `auschwitz_get_transport`, 2026-10-27.
- IMPORTANT spelling: the museum's origin list spells it **"Balassgyarmat"** (one `a` missing). Searching "Balassagyarmat" returns 0 transports — a spelling trap, not a negative. Neighbouring origin places in the same list: "Salgotarjan" (transport 416), "Hatvan" (transport 336).

| transport_id | museum ref | arrival at Auschwitz | deported | registered | origin / region / zone |
|---|---|---|---|---|---|
| 309 | `94_Balassagyarmat` | **12-06-1944** | **2810** | none | Balassgyarmat / Nograd / zone VII |
| 308 | `102_Balassagyarmat` | **14-06-1944** | **1867** | none | Balassgyarmat / Nograd / zone VII |

- Verbatim museum text: "According to Mikuláš Gaško's list, there were two such transports: 94.Balassagyarmat — Date of passing through Kassa 12.6.1944 — 2810; 102.Balassagyarmat — 14.6.1944 — 1867." (so the 12/14 June dates are the *Kassa* passage dates in the Gaško list; the DB's `arrival_date` field repeats them.)
- `auschwitz_transport_people(309)` = 0 and `(308)` = 0: "most deportees on RSHA transports were never registered" — no per-person list exists for these transports.
- Museum general text: no transport lists survive for deportees from Hungary; ~75% selected for immediate death on the ramp.

## Use for the Blumenthal family
Benő (b. 1888/1892, aged 52-56) and Ida (b. 1885-1890, aged 54-59) from Nógrádbercel (Balassagyarmat district) were, per the Yad Vashem pages of their children, in the "גיארמת (גטו)" and deported to Auschwitz in 1944. The ghetto/transport chronology that fits is the Balassagyarmat one: ghetto 10 May 1944 -> Nyírjes-puszta tobacco barns ~4 June -> entrained 10 June -> arrival Birkenau 14 June (DEGOB 3549 and 3550, see docs/degob/). The 14-06-1944 arrival matches transport **308** (1867 persons) as the best-fit train for a family entrained 10 June; transport 309 (arrival 12 June) is the other candidate. Which of the two carried them cannot be decided from any record found.

Grade: **ככל הנראה** (that the parents travelled on one of the two Balassagyarmat transports of 12/14 June 1944) — chronology only; no name-level record.

---

**עדכון 27.10.2026 (ביקורת).** הדוח (4.7) אינו מזהה את רכבת ההורים עם טרנספורט 308 (14.6, 1,867 איש). התאריכים 12.6 ו-14.6 ברשימת גאשקו הם מועדי המעבר בקאשה, לא מועדי ההגעה; הרכבת שתיארו העדים — כ-2,800 איש, יצאה ב-10.6 והגיעה ב-14.6 — מתאימה לזו של 2,810 (12.6 בקאשה). ועל "מחוז באלאשאג'רמאט": ברשומות הפטירה ב-JewishGen ברצל רשומה במחוז (járás) **סיראק**; שההורים היו בגטו גיארמת — לפי דפי העד של בנם יהודה.
