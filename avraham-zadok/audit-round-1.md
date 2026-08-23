# QA Audit — Round 1

**Subject:** אברהם צדוק (1925 מקווה ישראל – 1/1/2017)
**Corpus:** /root/tzadok-family · audit date 2026-08-20 · auditor: independent QA
**Method:** read every deliverable file, both build scripts run, both evidence crops opened and read, link targets resolved on disk (root + site/).

Overall the corpus is in good shape: no broken links, build scripts run clean, evidence images genuinely show the declared facts, facts are internally consistent across report/tree/sources/changelog, and privacy/commissioner discipline is mostly honored. Findings below are mostly medium/minor polish, concentrated in (a) the report's own "linked-sources" promise not being met inside the prose, and (b) one over-stated verification claim in פרק א׳.

---

## 1. Link integrity

### 1a. Every relative link/image target resolves — CLEAN
- **report.md:** contains **zero** markdown links or image targets (see 1b — this is itself a finding, not a pass).
- **sources-index.md:** 12 markdown targets — 5 external (https) + 7 local. All 7 local (`docs/archives/palmach_veteran_86681.txt`, `docs/evidence/palmach_avraham_page.jpg`, `docs/archives/nli_frainte_book.txt`, `docs/evidence/nli_frainte_book.jpg`, `docs/archives/context-notes.md` ×3) exist on disk.
- **אברהם-צדוק.html:** every `href`/`src` checked. Local targets — `docs/evidence/palmach_details_zoom.png`, `docs/evidence/palmach_avraham_page.jpg`, `docs/evidence/nli_frainte_quote_zoom.png`, `docs/evidence/nli_frainte_book.jpg`, `tree.html`, plus the 4 source `docs/…` targets — all exist. Internal anchors `#report #tree #evidence #sources` all have matching `id=` sections.
- **index.html:** redirect target (percent-encoded `אברהם-צדוק.html`) exists.
- **site/ copy:** mirror verified — `site/docs/archives/*`, `site/docs/evidence/*`, `site/tree.html`, `site/index.html`, `site/report.md`, `site/sources-index.md` all present; every relative target resolves under `site/`. The build script's own link-check assertion passes ("8 local targets OK; 5 external", "site/ built and verified").

**Verdict: no broken relative link or image target anywhere (root or site/).**

### 1b. Plain-text mentions that should be markdown links — FINDINGS
- **report.md:5** — *(medium)* — "כל טענה עובדתית מלווה בדירוג ודאות, **בהפניה למקור החיצוני ובעותק מקומי שמור בתיקיית המחקר**." The document promises each claim links to its external source and local copy, but report.md carries **no links at all**, and even in the rendered flagship HTML the report section has no inline links (sources live only in a separate index the reader must scroll to). *Fix: either soften the promise, or hyperlink source names (e.g. "כרטיס החבר", "ספר פריינטה") to `sources-index.md#…` / the `docs/…` copies.*
- **report.md:144** — *(minor)* — "ראו את **אינדקס המקורות**…" is bold text, not a link to `sources-index.md`. *Fix: make it a markdown link.*
- **report.md:132 (נספח א׳) & 138 (נספח ב׳)** — *(minor)* — the tree and evidence gallery are referenced as existing "בגרסה הגרפית של המסמך" with no link to `tree.html` / the gallery. *Fix: add links (in the HTML build these are anchors; in the .md they dead-end).*
- **report.md:119 & 126; sources-index.md:40** — *(minor)* — bare hostnames "kadisha.biz, gravez.co.il" appear as plain text. This is acceptable (they are documented *negative* findings that failed to load, so they should NOT be clickable), but flagged for completeness. *Fix: leave unlinked; optionally wrap in backticks to mark them as non-links.*

### 1c. External-link well-formedness — MOSTLY CLEAN
- No broken `](`, no unbalanced brackets, no stray spaces inside link syntax. All 5 external links use `https://` and render correctly.
- **sources-index.md:23 (and HTML line 264)** — *(minor)* — `https://www.hamichlol.org.il/חטיבת_קרייתי` contains an un-percent-encoded Hebrew path. Browsers resolve it fine, but it is not strictly RFC-3986 encoded. *Fix (optional): percent-encode the path, or leave as-is (works).*

---

## 2. Cross-document consistency

Checked report.md (all chapters), changelog (נספח ד׳), sources-index.md, tree_svg.svg, tree.html, and the source txt against each key fact:

| Fact | report | tree | sources | changelog | card txt | verdict |
|---|---|---|---|---|---|---|
| Birth year **1925** | ✓ (א׳,ה׳,ט׳) | ✓ "נ׳ 1925" | ✓ | ✓ | ✓ | consistent |
| Death **1/1/2017** | ✓ (א׳,ח׳,ט׳) | "נפ׳ 2017" | ✓ "1/1/2017" | ✓ "2017" | ✓ "1/1/2017" | consistent |
| Parents אהרון (אופה) & רוזה née פריינטה | ✓ | ✓ | ✓ | ✓ | ✓ | consistent |
| Siblings יעל, מרים/"קיקה", איציק, יוסי | ✓ (ד׳) | ✓ (4 boxes) | ✓ | ✓ | ✓ | consistent |
| Wife רחל née רפפורט/פרקש, married 1950 | ✓ | ✓ "נישאו 1950" | ✓ | ✓ | ✓ | consistent |
| Sons עדו & זיו | ✓ | ✓ | ✓ | ✓ | ✓ | consistent |
| Palmach פלוגה ד׳ "נטעים" | ✓ | "פלמ״ח" | ✓ | — | ✓ "פל' ד'" | consistent |
| חטיבת קרייתי | ✓ | ✓ | ✓ | ✓ | ✓ | consistent |

Sibling count check: "אברהם היה אחד מחמישה אחים לפחות" (ch ד׳) + the 4 named siblings + Avraham himself = 5. Tree draws 5 children. **Consistent, no contradiction.**

**Findings:**
- **report.md:15 (פרק א׳)** — *(medium)* — "הזהות מבוססת על **הצטלבות מלאה בין הפרטים שנמסרו לבין המקור החיצוני**: שנת הלידה 1925, מקום הלידה…, שמות ההורים…, מערך האחים…, שני הבנים, שנת הפטירה 2017 ומקום הקבורה — כולם תואמים." This **overstates independent verification** and is internally contradictory: (i) the only genuinely independent external source (the NLI פריינטה book) confirms *only* the פריינטה→מקווה-ישראל link and the תימן merge — it does **not** confirm Avraham's birth year, siblings, sons, death year or burial; (ii) line 7 explicitly calls the Palmach card "מקור משפחתי מובהק … אינו רשומה ממשלתית", yet line 15 treats that same card as "המקור החיצוני" it is cross-checked against — a circular cross-check (card vs. card). *Fix: rephrase to "הצטלבות בין הפרטים שמסרו הבנים לבין כרטיס החבר; אישוש חיצוני עצמאי קיים לשורש פריינטה בלבד."*
- **report.md:13 vs 109/117 (death-date certainty grade)** — *(medium)* — פרק א׳ presents the full date "נפטר ב־1 בינואר 2017" under the blanket grade **מאומת**, while פרק ח׳ downgrades the exact day to **כמעט ודאי, טעון אישוש**, and פרק ט׳ lists "אישור תאריך הפטירה המדויק (1/1/2017)" as an **open gap**. The same fact carries two different certainty grades. *Fix: in פרק א׳ mark the day as כמעט ודאי (or drop the day there), so all three chapters agree.*

No other contradictions found. Name spellings, dates, counts and relationships read identically across the tree SVG (identical in `tree_svg.svg` and embedded in the HTML and `tree.html`) and the prose.

---

## 3. House conventions

**(a) Foreign-language quotes — CLEAN.** The only Latin-script strings in the deliverable are transliterated names, each labeled/handled in context: "Zadok Avraham" is introduced as "(בלועזית בכרטיס: *Zadok Avraham*)"; "Frainte", "Rappaport / Farkash" appear as parenthetical romanizations beside the Hebrew. The English NLI subject tags ("Jewish families -- Eretz Israel", "Mikve Yisrael (Israel) -- History") exist only in the local archive `docs/archives/nli_frainte_book.txt:13` — they do **not** leak into report.md / sources-index.md, so nothing untranslated reaches the reader.

**(b) Dual sourcing — CLEAN at the index level.** Every source in `sources-index.md` carries both an external reference and a local copy (card: palmach URL + `.txt` + `.jpg`; NLI book: URL + `.txt` + `.jpg`; קרייתי/כפתורים/מקווה-ישראל: URL + `context-notes.md`). Caveat folded into finding M-1b:5 above — the report *prose* does not itself link claims to those pairs.

**(c) Name-spelling consistency — CLEAN (handled).** פריינטה is the standard spelling; the "פרינטה" variant is explicitly acknowledged ("מופיע גם ככתיב 'פרינטה'", ch ג׳). The tree uses the vocalized "פְּרַיינְטֶה" — cosmetic, same name. רפפורט/פרקש is written uniformly with the slash everywhere, and the gaps list already flags the need to settle on one maiden name. No stray/contradictory spellings.

**(d) Changelog (נספח ד׳) — CLEAN.** Single entry "מהדורה 1"; ascending, gap-free, no duplicates by definition.

**(e) Commissioner / requester leakage — one minor finding.**
- **report.md:58 (פרק ד׳) & HTML line 80** — *(minor)* — "(הכינוי 'קיקה' שהוזכר **בפנייה הראשונית** הוא אפוא מרים.)" The phrase "הפנייה הראשונית" points at the commissioning inquiry. No "סבא שלי"/"my grandfather"/named commissioner appears anywhere (checked report, HTML, tree — none), so this is mild framing leakage only. *Fix: drop "שהוזכר בפנייה הראשונית" → "הכינוי 'קיקה' הוא אפוא מרים."*

**(f) Status/gaps lists are bullets — CLEAN.** פרק ט׳ open-gaps and the negative-findings list are markdown bullets; render as `<ul>` in HTML.

**(g) Uniform certainty wording — one minor finding.** Grades used: מאומת (22×), כמעט ודאי (2×), טעון אימות (3×). No stray grades ("סביר", "ככל הידוע", standalone "ודאי", etc.). One deviation:
- **report.md:109 (פרק ח׳)** — *(minor)* — uses "**טעון אישוש**" where the house-standard grade term is "**טעון אימות**". *Fix: change "טעון אישוש" → "טעון אימות" for uniform wording.* (מאומת / כמעט ודאי / ככל הנראה / אפשר ש… — טעון אימות.)

---

## 4. Sanity

- **Chapter numbering — CLEAN.** פרק א׳→ט׳ sequential (1 האיש … 9 סיכום), then נספח א׳→ד׳ sequential. No skips or repeats.
- **Tables — CLEAN.** The deliverables use no markdown tables; the tree is hand-built SVG and renders (drop-lines connect all three generations; verified visually via the embedded/standalone SVG which are byte-identical).
- **Duplicated paragraphs — CLEAN.** report + sources each appear once in the unified HTML; no repeated blocks.
- **Orphaned / renamed files — CLEAN.** All 4 evidence images and all 3 archive files are referenced; no orphans. `tree_svg.svg` is a build artifact embedded into the HTML and matches `tree.html`.
- **Declared facts vs evidence images — CLEAN (both read).**
  - `docs/evidence/palmach_details_zoom.png` — reads "צדוק אברהם ז״ל · בן רוזה ואהרון · נולד במקוה ישראל · 1925 · גויס 1942 · פל׳ ד׳, ארגון ההגנה, חטיבת קרייתי · תפקיד אחרון: נשק · שוחרר 1949 · נפטר 1/1/2017 · נקבר בתל אביב – ירקון". Every one of these matches the report and the caption. ✓
  - **`docs/evidence/nli_frainte_quote_zoom.png` — verified per task instruction: it genuinely shows the family back-cover quote** ("זהו הסיפור המשפחתי שלנו, סיפורה של משפחת פריינטה ממקוה ישראל … שמיזגה לתוכה מזרח ומערב, אשכנז, תימן ומגרב, קיבוץ גלויות נפלא. -- מן הכריכה האחורית"), **not a cookie/consent popup.** Text matches the quoted block in ch ג׳ and the gallery caption verbatim. ✓
- **Build scripts — CLEAN.** `python3 build_tree.py` → "tree.html written". `python3 build_unified.py` → "link-check: 8 local targets OK; 5 external / site/ built and verified. / MAIN: אברהם-צדוק.html". Both exit 0, no exceptions; `markdown` dependency present.

---

## Required fixes (numbered)

1. **(medium) report.md:15 (פרק א׳)** — Rephrase "הצטלבות מלאה בין הפרטים שנמסרו לבין המקור החיצוני …" — it overstates independent verification (only the פריינטה book is truly external, confirming the מקווה-ישראל/תימן merge only) and circularly treats the family card as "external". Align with the honest note at line 7 and the gaps in פרק ט׳.
2. **(medium) report.md:13 vs 109/117** — Reconcile the death-date certainty grade: פרק א׳ implies the full date 1/1/2017 is מאומת, while פרק ח׳/ט׳ treat the exact day as כמעט ודאי / open gap. Grade the day consistently (כמעט ודאי) in פרק א׳.
3. **(medium) report.md:5 (+ report prose generally)** — Either soften the "each claim links to external source + local copy" promise or actually hyperlink claim sources; currently report.md has no links and the HTML report section links nothing inline.
4. **(minor) report.md:144** — Turn "אינדקס המקורות" into a link to `sources-index.md`.
5. **(minor) report.md:132 & 138 (נספחים א׳/ב׳)** — Add links to `tree.html` and the evidence gallery instead of "בגרסה הגרפית" plain text.
6. **(minor) report.md:109 (פרק ח׳)** — Change "טעון אישוש" → "טעון אימות" for uniform certainty wording.
7. **(minor) report.md:58 (פרק ד׳)** — Remove "שהוזכר בפנייה הראשונית" to eliminate commissioner-context leakage.
8. **(minor) sources-index.md:23** — Optionally percent-encode the Hebrew path in the hamichlol URL (`חטיבת_קרייתי`); functional as-is.
9. **(minor) report.md:119/126 & sources-index.md:40** — Optionally wrap the bare "kadisha.biz / gravez.co.il" hostnames in backticks to mark them clearly as non-clickable negative findings.

---

## Summary (counts by severity)

- **Critical: 0** — no broken links, no missing files, no evidence/fact mismatch, scripts run clean.
- **Medium: 3** — (1) overstated independent-verification claim in פרק א׳; (2) inconsistent death-date certainty grade across chapters; (3) unmet "linked-sources" promise in the report prose.
- **Minor: 6** — sources reference not linked; tree/evidence references not linked; "טעון אישוש" wording variant; "פנייה הראשונית" commissioner leakage; un-encoded Hebrew URL; bare negative-finding hostnames.

**Total: 9 findings (0 critical / 3 medium / 6 minor).** Sections 1a, 1c (core), 2 (all 8 tracked facts), 3a–3d, 3f, and all of Section 4 are otherwise clean. The single most important item to read past the polish is fix #1 (the "full cross-check against an external source" claim in פרק א׳), because it is the one place the report claims more evidentiary weight than the corpus actually supports.
