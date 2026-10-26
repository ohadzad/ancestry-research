# Report conventions — RTL/Hebrew, certainty, changelog, sourcing, the sources index

House style for the deliverable. Defaults shown for a Hebrew RTL report; adapt to the
report's language while keeping the discipline.

## Document shape

- **One clean current version.** No "previous scan showed…" narration in the body — the
  body is the present truth. All history goes in the changelog.
- **An opening `::: lede` box**: the sixty-second answer to "who was this and what happened",
  followed by a short "where to start" list linking the timeline, the tree, the person index,
  the evidence gallery and the open actions.
- **Method goes at the end.** One report was rebuilt twice — first as an academic paper, then
  as an encyclopedia entry — because *the reader had to read a third of the document about the
  method before reaching the content*. The chapter "About the research" (sources, coverage,
  conventions, what was not found) is the last chapter, not the second; there is no abstract,
  no keywords, no standalone summary chapter unless asked.
- **Chapters** labelled `פרק א'`, `פרק ב'`, … Status/action lists are **bullet lists**, not
  run-on prose.
- **Process stays out of the body** — no "as this edition established", "our tool", "for the
  purposes of this report", no family-perspective phrasing ("סבתא שרה"). The exception is
  **correspondence status**: addressee, date sent, what was asked, what came back, ticket
  number — that is a published section, because a reader may pick up the thread.
- **Chapter that faces the reader last: open actions**, priority-ranked, generated from the
  ledger's stable ids (see `research-ledger.md`).

## Certainty ladder (use exactly these, consistently)

- `מאומת` — verified directly by a document.
- `כמעט ודאי` — near-certain (strong convergent evidence, one small gap).
- `ככל הנראה` — likely.
- `אפשר ש… — טעון אימות` — possible; needs verification.

Two permitted derivatives: `טרם נבדק`, `טעון בירור`. Written in `**bold**`, each rung
renders as a coloured chip, so use them as **labels** — not as ordinary adjectives mid-sentence.

Rules that took audit rounds to learn:

- **Grade the document separately from the identification that rests on it.** "The record is
  `מאומת`; the identification of this person with our Mendel is `ככל הנראה`" is two grades and
  both belong. Where a corpus has several people of the same name, keep a **two-column grading
  table** (content / identification) and let identification reach `מאומת` only where the
  place, trade or community is printed beside the name. **A byline proves authorship, not
  identity** — four press items went out `מאומת` on a byline in a corpus that already knew four
  other men of that name.
- **Grade per cell, not per table.** Say which cells were read at magnification and which are
  best-effort.
- **An index row is `ככל הנראה` until the scan is read.** Then it is whatever the scan says.
- **A catalogue statement is graded twice**: verified as a quotation of the catalogue,
  unverified as a fact on the ground (a cemetery survey's stone count, a finding aid's town).
- **Relativise a grade that rests on a family source**: `מאומת בכרטיס החבר` — verified in the
  membership card the family filled in — so the reader sees what "verified" rests on.
- **Background knowledge carries no grade.** A sentence of accepted context that was not checked
  against a listed source says so and stays ungraded, so it cannot inherit the chip beside it.
- **The same fact must not carry two different grades in two places**, and comparable facts get
  the same yardstick (don't grade one sibling's death "near-certain" and an identical case
  "likely").
- **An upgrade is a claim.** When an audit or a new record suggests raising a grade, the upgrade
  needs its own evidence and its own edition entry.
- **No grade-laundering across chapters.** A `טעון אימות` population figure was once used as
  support for a `מאומת` conclusion; an unverified fact cannot corroborate a verified one, however
  far apart on the page they sit.
- **The source's scope must cover the claim's subject.** A press item about *religious*
  registers cannot vouch for the *civil* registers kept after 1895.

## Sourcing

- **Dual links on every claim**: exact external (archive URL / DB record / page-line
  citation) **and** a local file copy in `docs/`. Both rendered as real markdown links.
- **The exceptions are enumerated, annotated and counted.** A few sources legitimately have
  one link — no public address, or an online reference with no separate document. Each such
  entry says so, and the sources index states how many there are, so an audit can count them.
  A report that claims "every source carries both links" while a footnote admits otherwise
  cost three audit rounds.
- **A local copy is a copy of the document itself**, not a screenshot of the web page that
  points at it. An entry with no separate archival document is labelled an *online reference
  source*, never given a fabricated "copy".
- **A crop is not the copy.** Save the full page or issue as well; the crop is a pointer into it
  (a review dated from its transcript alone carried the wrong year; the neighbouring issues
  reversed it).
- Evidence figures are **crops of the original page** that click through to the full
  original; captions carry the precise locator (fund/opus/delo/row, or volume/page/entry).
- **Negative findings are recorded** (a documented absence constrains the story) — with the
  coverage that makes them checkable, and never converted into a positive inference.
- **Photographs are graded in three layers**: the cluster's metadata, the visual content, and
  who is depicted — the last claimed only when the catalogue names them.

## Quotes & languages

- Every foreign-language quote (Hungarian/German/Czech/English/…) gets an **inline
  translation** immediately beside it. A quote without a translation is a defect — and the
  quote carries a `lang` attribute, or a Hebrew screen reader pronounces Hungarian as Hebrew
  (a logged defect in the template).
- Transliterate names faithfully and list variants; place names carry all historical +
  modern forms as one identity.
- **Hebrew and Gregorian dates both**, checked computationally (a stone that says "Sabbath"
  should convert to a Saturday).

## Naming discipline

- Fix each ambiguous name to one canonical spelling in the body and note variants once; the
  record's own spelling goes inside quotes in the caption. Decide project-specific exceptions
  up front and keep them consistent.
- **Never** name the researcher/requester in the report — nor in the changelog, the sources
  index, a linked letter, or the published folder. In the build config, assemble the privacy
  patterns rather than writing them out (`'ohad'+'z'`), because the config file itself is
  published beside the report.

## The changelog

- Its own file (`CHANGELOG.md`), rendered as the report's last section. **Ascending** editions
  1..N; a new edition is appended after the last, never inserted mid-list.
- **Append-only ordering, not append-only content.** Factual miscounts, a body glued to the
  wrong edition, the requester's name, family-perspective phrasing — these were corrected
  *inside* old entries five times in one project, each time recorded in the new edition. What
  is never done is rewriting history to make an old edition look right.
- **Label the kind of each edition** — content / audit fixes / structure / delivery — so a
  reader can see which chapters have been through an audit sub-loop since they were written.
- **Stamp date and time**, not just the date, once several editions ship per day; and give
  every build a build version the page displays, so "the site shows the old text" is diagnosable
  in one glance.
- Audit reports live as separate `audit-round-N.md` files (gitignored or kept out of the
  published mirror) and are summarised in the edition that fixed them; they never enter the
  body.

## The sources index — the second deliverable

`sources-index.md` is not a file list. Two shapes have been used, and the invariants below hold
for both:

- **Shape A — a section per collection or archive** (`###`), opened by a **provenance
  paragraph** (who supplied it, the exact download or receipt date, and for correspondence a
  verbatim quote of the archivist's letter with its translation), then a **three-column table:
  `file | what it is | what came out of it`**. Suits a project whose sources arrive as
  collections — a camp archive's packet, a register series' scans.
- **Shape B — a numbered entry per source** (`### 1 …`, `### 82 …`), anchored `#src-N` so the
  report cites `[[13]]`, each entry a fixed field list: `מהות` (what it is) · `מקור חיצוני`
  (external link) · `עותק מקומי` (local copy) · `מה הוא מוכיח` (what it proves) · `נצפה`
  (date seen) · `הערה` (note). Suits a project of many heterogeneous single sources; the field
  list is where a "no public address / no separate document" exception is written, and the
  edition gate counts those exceptions from it.
- **What it proves is quoted from the document** (`"Eingewiesen am: 19.5.1944 … in KL.:
  Auschwitz"`), not described. It is the field that makes the index auditable.
- **Every filename is a markdown link** to the local copy; the external record link sits beside
  it. (An index with zero links that called itself a links section was a critical finding.)
- **Evidence crops get their own section** with a "how these were made" preamble and the
  columns `crop | cut from (link to the full original) | what is seen`, plus the sentence that
  crops are not standalone documents — the binding document is always the named full source.
- **A links-only section** for online reference sources with no separate document, themed, each
  entry carrying: exact search coverage and counts, date searched, negative results, tool quirks
  (the POST workaround, the reCAPTCHA, the subscription wall, the canonical index spelling),
  and grading caveats.
- **Declared counts match disk** (files per archive, scans, PDFs) — the audit checks — and files
  excluded from the published site (a 100 MB testimony audio) are flagged as excluded.
- **Rejected candidates and mis-indexed records** get a line ("Rebeca Arwas" = Rebecca Aluf) so
  they are not chased again.

## Tone

- Respectful and plain about death, murder, and survival. This is a memorial document; let
  the sourced facts carry the weight. No sensationalism, no invented detail, no filler.
