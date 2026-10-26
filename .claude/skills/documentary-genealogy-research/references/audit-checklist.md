# The external audit loop — fresh-agent QA

Quality comes from an **independent** pass. After each substantial build, spawn a *fresh*
general-purpose subagent as a QA auditor over a clean context. It writes a severity-ranked
findings report and changes nothing; you apply the fixes and record them as the next edition.

**Three kinds of audit; they find disjoint defects.**

- **The evidence audit** — does the source say what the report says it says? Re-read the
  *sources*, not the report's description of them.
- **The outside-world audit** — do the report's checkable historical claims (transport sizes,
  camp chronologies, a district's ghetto, a cemetery's dating) agree with independent
  literature and databases? It moves grades *both* ways: in the source project it demoted a
  "1,987 murdered" to an estimate-and-remainder and promoted a transit camp to documented.
- **The delivery audit** (bottom of this file) — does the page actually work: RTL, print,
  mobile, search, contrast?

A build can pass every automated gate and still read reversed on a phone; a beautiful page can
be confidently wrong; a perfectly self-consistent report can contradict the standard history.
None of the three substitutes for another.

## How the rounds actually go

Two projects, well over forty rounds between them, and the curve is a **saw-tooth, not a
decay**. In the Shoah project the consistency rounds went 10 → (a round that found five declared fixes
missing) → 5 → **3**, and saturation was declared at 3, never at 0; a new content chapter then drew **17**, then 4, then 7; the next
content edition drew 12, three of them claims unsupported by their cited source. In the other
project the worst audit round of all (8 critical, 15 high) came *after* saturation had been
declared — it followed the biggest research burst. So:

- **Saturation is scoped to the material audited, not to the project.** Every content edition
  earns its own 3–4-round sub-loop. Label each edition's kind in the changelog ("content, not
  audit" / "structure, not content") so a reader can see which chapters have been through one.
- **A round that finds nothing evidential is the stop signal for *that* material**; run one more
  after a quiet round, because the quiet round is often a tired one.
- **Fixes cause regressions.** A bidi fix produced 30 double-wraps; a parenthesis fix produced
  its mirror image; a UX fix round's verification pass found four regressions the fixes themselves had created (`overflow-x` on the nav clipped the
  search box; a `%%` leaked from a Python format string; promoting lazy images on load killed
  the weight fix). Every fix round gets a regression pass aimed at the fix itself.
- **An audit's proposed *upgrade* is itself a finding.** One round raised an identification to
  `כמעט ודאי` while an unresolved contradiction sat three lines below it. Upgrades need their
  own evidence, exactly like claims.

**Auditing a report you did not build** — no ledger, no engine, no `docs/` tree: run tasks 0, 1,
2, 4 and 5 below as written, run task 3 only on the sources the report links to, and say so in
the findings header. The absence of a ledger and of local copies is itself the first finding.

## Spawn prompt (adapt names/paths)

> You are an independent QA auditor for a source-linked family-history research report
> (subject: `<PERSON>`). This is audit round `<N>`. Recent editions added `<what changed>`.
> Working dir: `<path>`. Files: `report.md`, `sources-index.md`, `CHANGELOG.md`, the trees,
> the built HTML, and the `docs/` tree on disk. **Do not edit anything except your report.**
> Write findings to `audit-round-<N>.md`: sections matching the tasks below, each finding
> tagged severity (critical / medium / minor) with file+line and a concrete suggested fix,
> and a final numbered list of all required fixes. End your message with a short English
> summary of counts by severity.
>
> **0. Verify the last editions' own claims first.** For each change the last two or three
>    changelog entries say was made, confirm it actually reached the built HTML. (Five fixes
>    declared in one edition had reached nothing; two of the next edition's were partial.)
>    Then check that the fixes did not create regressions in the thing they touched.
>
> **1. Link integrity.**
>   a. Extract EVERY relative link/image target from the md files AND every href/src in the
>      built HTML; verify each exists on disk **and is git-tracked** (i.e. will exist on the
>      published site). List every miss.
>   b. Find every **plain-text** file/path/URL mention that should be a link (bare `docs/…`
>      paths, quoted filenames, "saved in the folder", bare `https://…`). List each with a
>      verified suggested target.
>   c. Check external links are well-formed; check that links to source files open in a new
>      tab (returning from a scan on a very long page loses the reader's place).
>
> **2. Cross-document consistency — the seven surfaces.** For every key fact (each person's
>    dates, name spellings, counts, relationships, grades) verify it reads identically across
>    the report body, the sources index, the evidence captions, the tree SVG and its legend,
>    the per-archive findings files, the changelog, and the portal's registry and README
>    (a README that still lists one project when the portal has two is residue too). **Residue** — earlier-edition text
>    surviving on one surface after the body was updated — is a finding class of its own.
>    Flag any fact carrying two different certainty grades, and any "new" find that the corpus
>    already held (one edition rediscovered a document held since edition 55 and read a field
>    differently; both readings shipped `מאומת`, three lines apart).
>
> **3. Evidence.** Re-read the cited source for every claim in the chapters named `<…>`. The
>    finding class this exists for is a claim that drifted from what its document shows:
>    an index row cited as if the scan had been read; a byline taken as identification; a
>    row number described as a rank; a negative converted into a positive date ("married
>    before 1921" from absence in a partial index); outside knowledge placed beside a
>    `מאומת` grade and inheriting it.
>
> **4. House conventions.** Foreign quotes each have an inline translation; dual sourcing with
>    the enumerated exceptions annotated and their count matching; fixed name-spelling rules;
>    ascending, gap-free, duplicate-free changelog whose old entries are themselves free of the
>    requester's name and of family-perspective phrasing; status lists are bullets; uniform
>    certainty wording (`מאומת`/`כמעט ודאי`/`ככל הנראה`/`אפשר ש… — טעון אימות`), grades used as
>    labels not adjectives; the requester's name and contact appear NOWHERE, including linked
>    files and the published folder.
>
> **5. Sanity.** Mis-numbered lists; broken tables; duplicated paragraphs; orphaned or renamed
>    files; declared counts (sources, figures, editions, files per archive) matching disk and
>    the rendered page; bold-inside-italic that did not render.
>
> **6. Press coverage.** Confirm a press sweep exists for every named person (subject, spouse,
>    parents, siblings, children) in every press archive relevant to their places and years,
>    under every spelling in the name matrix. Missing people, archives, spellings or decades
>    are a medium finding; a press hit graded above `טעון אימות` on the name alone is a
>    critical one.
>
> **7. War years and censuses.** For every European-born person alive in 1939, confirm the
>    report covers 1938–1948 (ghetto, transport, camps with numbers, labor service, hiding,
>    liberation, DP camp, route out) or states with coverage what was searched. Confirm the
>    census stack for the family's places was checked to its earliest covered series, with
>    coverage stated per census. A survivor with no war-years section is a medium finding.

## The outside-world audit — same agent shape, different question

> You are checking a family-history research report against the independent historical record.
> Do not edit anything — report findings only. For every checkable claim about the wider world
> (a transport's size and date, a ghetto's district, a camp's chronology, a cemetery's dating, a
> census's coverage, an institution's founding, a place's administrative history) find the best
> independent source — the standard monographs, the museum's own publications, the archive's
> finding aids, the reference databases — and compare. Report each discrepancy with the two
> figures side by side, and say whether the report's grade should go **down** (a "documented"
> count that is an estimate-and-remainder) or **up** (a transit point the report hedged that the
> literature documents). Report also the claims for which you found no independent source at
> all — those are the ones that carry a grade they have not earned.

It exists because internal consistency is not truth: a report can agree with itself in every
chapter and still repeat a table's error. In the Shoah project this round demoted "1,987
murdered" to an estimate, found the standard reference names only the 507 men, discovered a
museum entry never mentions the transport at all — and promoted a transit camp to documented.

## Severity rubric

- **Critical** — anything that makes the published deliverable wrong or broken for a reader:
  broken links on the live site, a whole file/section with zero links where links are the
  point, a factual contradiction between two places, a claim stated as fact with no source, a
  privacy leak.
- **Medium** — plain-text mentions that should be links, inconsistent dates/grades across
  documents, a missing changelog entry for changes already made, an out-of-date index, residue.
- **Minor** — wording/translation polish, stale header dates, cosmetic tree labels.

## After the audit

- Apply fixes; **rebuild**; run the independent final link check; **re-verify the live site**
  if published (fetch a redirect, the main HTML, and a couple of deep files).
- Record everything as **one new ascending changelog edition** ("round `<N>` fixes: …"). A round
  may produce no edition (nothing to fix) and an edition may absorb several rounds; what must
  hold is that every round is named in some edition. **Number the rounds once, project-wide** —
  one project restarted its ordinals mid-run so that "round 3" names two different rounds, the
  other kept an `audit-rounds-19-27.md` holding rounds 10–17, and nobody could count either
  afterwards.
- Recurring real findings from the source projects (watch for these):
  - **An index row treated as a record.** Three false relatives entered one project from index
    lines whose scans said Amzalak, Aluf, and an English missionary named Bradley.
  - **Byline as identification.** Four press items graded `מאומת` because they carried the
    subject's byline, in a corpus that already knew four other men of that name.
  - **Residue across the seven surfaces** after a body edit.
  - **Publish-pipeline privacy leakage**: audit reports, a memory file, draft letters and the
    requester's e-mail pushed to the public repo by `git add -A`; a tree PDF with living
    relatives' contacts synced to the site.
  - Build/publish out of sync — the site still shows the *pre-edit* text because the HTML
    wasn't rebuilt after the md edit. The build belongs **inside** the publish script.
  - An index/sources file with **zero** markdown links though it's literally a "links" section.
  - A `.gitignore` glob silently excluding legitimate records (anchor the pattern).
  - Mirror folder holding files under old descriptive names vs. canonical names in the HTML.
  - A negative finding whose stated coverage omits a register the report itself cites
    elsewhere ("not in any marriage register" resting on two delos while chapter 3 quotes a
    wedding from a third).

---

## The delivery audit — a second fresh agent, on the rendered page

> You are auditing a rendered right-to-left HTML report for markup, accessibility and
> usability defects. Do not edit anything — report findings only. Load the page headless
> (Playwright/Chromium), take screenshots at 1280×900 and 390×844, **read the screenshots**
> rather than only measuring, and print to A4 PDF.
>
> **1. Markup** — unbalanced tags, nested `<a>`/`<bdi>`, duplicate ids, dead in-page anchors,
> images missing `alt`, raw `<strong>` or `%%` printed as text.
> **2. RTL correctness — the highest-value area.** Reconstruct visual order from per-character
> bounding boxes and hunt for text that renders in the wrong order: dates, numeric ranges,
> archive reference codes, Latin names inside Hebrew sentences, parentheses and quotation
> marks on the wrong side, `<code>` literals, table alignment, SVG labels.
> **3. Accessibility** — heading order, landmarks, focus visibility, keyboard reach of the
> nav, the in-page search and every scrolling table, real contrast ratios, a 12.5px floor for
> secondary text, glyphs that render as tofu boxes.
> **4. Responsive at 390px** — horizontal overflow, elements wider than the viewport, the
> sticky nav's height, whether anchored headings clear it, floating buttons covering text, the
> tree's initial zoom (smallest text on screen must be legible without pinching).
> **5. Print** — does the tree get its own uncropped landscape page, do tables keep every
> column, do images render (lazy images print as empty frames), are external URLs exposed, does
> an off-screen element (a skip link parked at −9999px) cut every page short?
> **6. Search** — type into it, click a result, and measure where the target lands.
> **7. Weight** — page bytes and the largest images; a reader who never scrolls should not
> download the gallery.
>
> Return findings numbered, most severe first, each with the observation and the minimal fix.

Recurring delivery findings worth checking by name: Hebrew punctuation trapped inside a
`<bdi dir="ltr">`; Hebrew forced into an LTR isolate and reading backwards; `<code>` with no
explicit direction; a search result that lands off-screen because the results list collapsed
and shifted the page; a table that loses its last column in print; a near-square family tree
cropped across two landscape pages; a 103-page report that printed as 53 truncated pages because a
hidden skip link was not `display:none` in print; a tree that opens at 38% zoom with 5.5px text.
