# Audit — Round 3 (edition-4 additions: Frainte maternal deep-dive)

Independent QA of the edition-4 additions to the source-linked Hebrew family-history
report in `/root/tzadok-family`. Scope: the new פרק ג׳ Frainte material based on the
1970 «למרחב» feature, the new tree founder generation, sources items 6–8, the changelog,
link integrity, the two new evidence images, certainty grading, and copyright.

Date of audit: 2026-08-20. No project files were edited; this file is the only output.

---

## Verdict summary

The edition-4 work is in good shape. The Meknes/Morocco Pariente branch is cleanly
walled off from Roza's line; the baker= Aharon and Miriam="קיקה" cross-references are
correctly labelled as inference, not fact; certainty vocabulary is uniform and contains
no forbidden "טעון אישוש"; the changelog is ascending and gap-free; edition "4" is
consistent everywhere; every relative link resolves on disk and under `site/`; the two
new images plausibly show what their captions claim; and quotation is short and attributed.

**One medium overclaim** survives: פרק ד׳ grades Roza's parentage "מאומת" while פרק ג׳/ט׳
correctly grade the same fact "כמעט ודאי" with an open which-wife question. Plus a few
minor precision items.

---

## 1. Overclaim / certainty grading

**PASS (with one MEDIUM exception).**

- **Meknes branch not conflated — PASS.** Source item 8 and report §ג׳ (lines 43–45) and
  `docs/archives/frainte-deep-notes.md` all label the מקנס/מרוקו Pariente ma'apil as
  "ענף אחר … אינו משפחת רוזה … מובא לאישוש מוצא השם בלבד, לא כקרבה ישירה." The deep-notes
  even state "חל איסור לחבר בין הענפים ללא ראיה." No conflation anywhere.
- **Article-implied vs. stated — mostly PASS.** The things the 1970 article only *implies*
  are correctly downgraded: "האופה = אהרון צדוק" rests on cross-ref with the Palmach card
  and is graded כמעט ודאי (§ג׳ lines 53–55, 59); Roza = Avraham's mother is כמעט ודאי;
  which of Yitzhak's two wives (Miriam Aruas or her sister) mothered Roza is flagged as
  open (lines 59, 139). Good.
- **Certainty vocabulary — PASS.** Only מאומת / כמעט ודאי / טעון אימות appear in the
  deliverables (report.md, sources-index.md, אברהם-צדוק.html). "ככל הנראה" and "אפשר ש…"
  are allowed but not needed and are correctly absent. **Zero** occurrences of the
  forbidden "טעון אישוש" in any deliverable (it appears only inside prior audit files
  audit-round-1/2.md, which is expected).

- **[MEDIUM] report.md:71 (פרק ד׳) over-grades Roza's parentage as "מאומת."**
  Line 71 reads: "רוזה לבית פריינטה (ילידת מקווה ישראל, **בת ליצחק פריינטה ולמרים ארואס** —
  ראו פרק ג') *(דירוג: מאומת.)*". The blanket "מאומת" also covers the lineage clause, but
  that clause is graded **כמעט ודאי** in §ג׳ (line 55: "זהות רוזה כבת יצחק פריינטה — כמעט
  ודאי") and is listed as an **open gap** in §ט׳ (line 139: which wife is Roza's mother is
  unresolved). The same fact therefore carries "מאומת" in one chapter and "כמעט ודאי /
  open gap" in two others — the exact class of grade inconsistency round 1 fixed for the
  death-date. Also, naming **מרים ארואס specifically** as Roza's mother contradicts the
  report's own statement that it could be her sister.
  *Fix:* split the grade on line 71, e.g. "*(דירוג: זהות ההורים אהרון ורוזה — מאומת; שיוך
  רוזה ליצחק פריינטה ולמרים ארואס/אחותה — כמעט ודאי, ראו פרק ג׳ ופרק ט׳.)*", and soften
  "ולמרים ארואס" to "ולמרים ארואס (או אחותה)".

- **[MINOR/observation] Founder-generation facts graded "מאומת" from a single 1970
  newspaper feature.** §ג׳ line 47 grades the whole founder chapter "מאומת — כתבת למרחב
  1970" (Yitzhak among Netter's first students, leather-dyer→kitchen-manager, Miriam of
  Jaffa died of cholera, nine children). These rest on one oral-history press feature.
  This is defensible under the report's house style (it grades other published secondary
  sources, e.g. חטיבת קרייתי, as מאומת), so not a defect — but a reader may read "מאומת"
  as "documentary-verified." *Optional:* qualify as "מאומת (מקור עיתונאי יחיד, 1970)".

## 2. Consistency across chapters / tree / sources / changelog

**PASS.**

- Names are uniform across report.md, sources-index.md, tree_svg.svg, tree.html and the
  archive notes: **יצחק פריינטה**, **מרים ארואס**, **פלורין (בלומברג)**, **ויקטוריה (בכר)**,
  the baker cross-ref, and Miriam = **"קיקה"**. No spelling or role contradictions found.
- **"9 children" vs "5 siblings" are NOT conflated — PASS (the specific worry).** "תשעה
  ילדים" appears only in the founder-generation context (Yitzhak's household: report.md:51,
  sources:43, HTML:77, lemerhav notes:14). The Aharon+Roza sibling set is separately stated
  as "אחד מחמישה אחים לפחות" (report.md:73). The tree draws exactly **5** child boxes under
  Aharon+Roza (יעל, מרים, אברהם, איציק, יוסי) and contains **no** "9"/"תשע" anywhere. The
  two counts never touch.
- **[MINOR] Sign #4 ("daughter Miriam at Hukok") is a weaker discriminator than the text
  implies.** The lemerhav notes themselves (line 19) record that **two** granddaughters of
  Yitzhak named Miriam were members of Kibbutz Hukok — one Roza's, one Victoria's. The
  report presents "בתה מרים … חוקוק = קיקה" as one of four converging signs without noting
  the duplicate. The overall identification is still sound (signs 1–3 — the name Roza whose
  husband the article calls "the baker" — already pin it, and קיקה is Avraham's sister per
  the card, hence Roza's daughter). *Fix (optional):* add half a sentence noting there were
  two Hukok Miriams so the sign is corroborative, not uniquely dispositive.

## 3. Changelog

**PASS.** Editions run **1 → 2 → 3 → 4**, ascending, gap-free, with edition 4 **appended
after** edition 3 (report.md:171–177; identical block at אברהם-צדוק.html:150–153).
Edition number "4" is consistent in the report header (report.md:3), the HTML masthead and
meta (HTML:35, 47), the HTML footer (HTML:371), and the tree footer (tree.html:120). The
SVG has no footer text (by design). No inserted/renumbered entries.

## 4. Link integrity

**PASS.** Every relative target in report.md, sources-index.md and אברהם-צדוק.html was
checked and exists **both** at repo root and under `site/`:

- report.md → `tree.html` ✓; in-page anchors `#sources`, `#evidence` both exist as IDs in
  the HTML (id="sources", id="evidence"; also id="report", id="tree") ✓.
- sources-index.md → 6 archive files + 8 evidence images — all present ✓.
- HTML → 6 archive files + 12 evidence images + tree.html — all present ✓.
- `site/` copies of report.md, sources-index.md, אברהם-צדוק.html, tree.html and index.html
  are **byte-identical** to the root versions (in sync). index.html redirects to the
  URL-encoded Hebrew filename, which exists. No broken links found.

## 5. New evidence images

**PASS — both plausible, captions do not overclaim.**

- `docs/evidence/lemerhav_1970_frainte_zoom.png` — a period newspaper page/spread with a
  byline ("מאת צביה כהן") and multiple family/agricultural photographs, consistent with a
  1970 «למרחב» centenary feature about Mikveh Israel's early women. Nothing in the caption
  claims more than the article attribution.
- `docs/evidence/frainte_shacham_photo.png` — a studio portrait of a young couple; the man
  wears a late-1940s khaki shirt, matching the stated 1947–1949 date and "נעורים" title.
  **Caption is exemplary on overclaim:** both the HTML figcaption (line 283), sources item 7
  ("**הערה:** האנשים בתמונה אינם מזוהים בשמות") and the deep-notes explicitly forbid naming
  the sitters as Roza/Aharon/Avraham. No caption names anyone the record does not name.

## 6. Copyright / quotation length

**PASS.** The report reproduces only short attributed fragments from the 1970 article —
"הבעל של רוזה היה האופה", "אירע מקרה שרוזה נפצעה", "הבת הראשונה שנולדה במקווה ישראל" — each
a few words, in quotation marks, attributed to the כתבה. No long passage is reproduced.
`docs/archives/lemerhav_1970_frainte.md` is paraphrase plus the same short quotes and
carries an explicit rights note ("מובאים ציטוטים קצרים בלבד … הטקסט המלא נשמר כתמלול
פנימי"). No over-long quotation anywhere.

---

## Numbered fix list

1. **[MEDIUM]** report.md:71 (and the mirrored HTML paragraph, אברהם-צדוק.html:88) —
   the "*(דירוג: מאומת.)*" on the parents line wrongly certifies Roza's parentage, which
   §ג׳ (line 55) grades כמעט ודאי and §ט׳ (line 139) lists as an open gap. Split the grade
   (parents identity = מאומת; Roza's lineage to Yitzhak/Miriam = כמעט ודאי) and change
   "ולמרים ארואס" to "ולמרים ארואס (או אחותה)".
2. **[MINOR]** Sign #4 in §ג׳ ("מדוע הזיהוי ודאי", report.md:55) — note that the 1970
   article records two Hukok granddaughters named Miriam (Roza's and Victoria's), so this
   sign corroborates rather than uniquely fixes the identification.
3. **[MINOR]** tree_svg.svg / tree.html — the maternal founder box "יצחק פריינטה ∞ מרים
   ארואס · הורי רוזה" (and the tree.html legend) states מרים ארואס flatly as Roza's mother
   despite the acknowledged which-wife uncertainty; consider "(אם רוזה: מרים ארואס או
   אחותה)" or a legend note, to match the report's own caveat.
4. **[MINOR/optional]** §ג׳ line 47 — qualify the founder-chapter "מאומת" as resting on a
   single 1970 newspaper feature (e.g. "מאומת — מקור עיתונאי יחיד, למרחב 1970") so
   "verified" is not read as documentary confirmation.

Note: if fix #1 is applied to report.md, regenerate `site/` and the HTML so the byte-for-byte
sync is preserved.

---

**Severity count: 0 critical, 1 medium, 3 minor.**
