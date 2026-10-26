# The research ledger — running the work without losing the thread

Documentary genealogy is a long job with a wide front: twenty archives, a dozen name
spellings, four generations, and a context window that will be compacted several times before
it is done. The ledger is what makes the work survive that: **small working files in the
project folder, updated as you go, never allowed to go stale.**

They are working files, not deliverables. Their process narration stays out of the published
report, but their *findings* reach it — and they stay **in the folder**, because their real
audience is the next session, which may be a fresh context with no memory of this one.

Two shapes have been used, and both work. What must hold in either is at the end.

---

## Shape A — four files (a single-front project)

```
THREADS.md      # open leads: what is unresolved, what to do next, what it would cost
NEGATIVES.md    # searches that came back empty — with their exact coverage
BLOCKERS.md     # what only the user can unblock, when it was asked, what is expected back
TOOLSTATE.md    # canary results, quirks discovered, workarounds in force
```

### THREADS.md — the open front

One entry per unresolved question, written to be actionable by someone who was not there — which
is also what makes a thread paste straight into a sub-agent brief.

```markdown
## T-14 · Mendel's disappearance after 1938
- **Question:** Mendel (b. 26.04.1897) has no marriage, death or emigration record after the
  1938 marriage entry. Did he leave the district, or is the record missing?
- **Why it matters:** he is one of two siblings whose fate is entirely untraced; a departure
  would also explain the gap in the 1941 census household.
- **Tried:** JewishGen Subcarpathia D+M, full 1895–1945 run, all four spellings + SZTRULYOVICS
  (nil). Arolsen variants (nil). Auschwitz variants (nil). Yad Vashem synonym (nil).
- **Next action:** JDC transmigration bureau + migration files, both spellings; then
  RadixIndex place index for the neighbouring towns (Huszt, Tecső, Dolha).
- **Cost:** ~20 min. No subscription needed.
- **Status:** open · last touched 27.08.2026
```

### NEGATIVES.md — the searches that found nothing

```markdown
| # | Question | Source & exact coverage | Result | Graded |
|---|---|---|---|---|
| N-3 | Mendel or Herman after 1938 | JewishGen Subcarpathia Deaths + Marriages, delos 215, 216, 445, 493, full 1895–1945 | no entry under any of 5 spellings | ככל הנראה left the district |
```

### BLOCKERS.md — what only the user can clear

```markdown
| # | Blocker | What it costs us | Asked | Expected back |
|---|---|---|---|---|
| B-2 | FamilySearch token missing (`fs_status: access_token missing`) | full-text search of ~2B record images, incl. Subcarpathian civil registers | 27.08 | user, 5 min |
| B-5 | Stutthof archive enquiry (poszukiwania@stutthof.org) — prisoners 38443/38444 absent from the partial online index | the definitive answer on Sima's death | 17.08 | archive — answered next day with 18 documents |
```

### TOOLSTATE.md — what the tools actually did

```markdown
| Server | Canary | When | Note |
|---|---|---|---|
| jewishgen | session cookie present | 27.08 | result sets POST to jgdetail_2.php — two-GET workaround in force; canonical spelling SZTRULYOVICS |
| familysearch | RED — no token | 27.08 | see B-2 |
| jpress | back after Cloudflare · canary 84 hits (ed. 60 logged 66) | 26.08 | 18 unread rows — read them against the corpus |
```

## Shape B — a target table and a round journal (a long, multi-branch project)

The seventy-five-edition Sephardi/Yemenite project kept no separate negatives or tool-state
files. It kept two files that mattered under `docs/archives/` (beside two strays — a
context-notes file and a per-branch plan that never made it into the repo):

**`open-targets.md` — the dashboard.** A table `# | what | how | status` of numbered targets
(the numbered table stopped at T12 while T13–T41 accumulated as prose bullets lower in the
same file — see the decay below), followed by
two prose sections: **institutional approaches** (phone/e-mail targets —
a Chevra Kadisha, a school archive, AIU Paris, CADN Nantes, a Gibraltar synagogue, the ICRC —
which is the blockers list under another name) and **open content questions** (unresolved facts
with no single target: a birth day 16.9 vs 19.9, nine children vs eight). Closed targets stay in
the table with ✅, the finding, and **the edition that closed them** — "so they are not chased
again". A methodological-warning block sits inside the file where the trap lives (the
famous-dynasty trap under the Yemen targets).

**`research-queue.md` — the chronological journal**, one section per research round/edition,
with `closed` / `opened` / `needs the user's browser` / `blocked — needs the user` subsections,
and a glyph vocabulary: ✅✅ decisive · ✅ closed · ❌ true negative · ⏳ waiting · 🎯 open
target · 🔎 lead, no claim · ⚠️/⛔ blocked · ❗ contradiction · 🔁 re-check. **Declare it once
at the top** — the source project never did, and a reader has to infer ✅✅ from context.
Negatives, blockers and tool state are *statuses* here, not files.

Its known weaknesses: the journal decayed (header at edition 40 while the project was at 74)
while the target file stayed current, the target file's own table fell behind its prose, and the same negative ended up worded three ways in
the journal, the report and the sources index. If you choose this shape, the journal needs the
same "never stale" rule as the four files, and each negative is written once and linked from the
other places.

Per-archive **findings files** (`docs/isa/…`, `docs/jpress/…`, `docs/igra/…`) are what the
sources index actually links to in this shape; they hold the reading of each record set with
its coverage and its rejected candidates.

---

## What must hold in either shape

- **Every open item has a next action, or it is not open.** A lead with no concrete next step is
  either closed (say why), a blocker (say who), or an open content question (say what record
  would settle it).
- **Record what was tried precisely enough not to repeat it** — which index, which spellings,
  which years, which delos. "Searched Arolsen" is worthless six weeks later.
- **Ids are stable and never renumbered.** Editions cite them; the report's open-actions
  chapter is generated from them. (One project renumbered its action list twice, and every
  changelog reference by number went stale.)
- **Closed items stay in the file**, with the finding and the edition that absorbed them.
  Disproved inferences, mis-indexed records and rejected candidates are recorded for the same
  reason — "so it is not researched again" — and a decisive negative can even keep its evidence
  in the gallery.
- **A tool error is not a negative finding.** If the canary is red or the query returned an
  error rather than an empty set, *no question was asked*: record a blocker, never "0 results".
  Writing "X — no hits in FamilySearch" from a failed call is fabrication, and one project
  refused to do it in so many words.
- **A negative's coverage must include what the report itself cites.** Before publishing "not in
  any marriage register", check which registers the report quotes weddings from.
- **The grade of a negative reflects the index's completeness, not your effort.** A partial index
  (Stutthof online ≈81k of 110k; JewishGen's 1848 census ≈178 rows for a whole county) supports
  `ככל הנראה` at best. And **a negative never becomes a positive**: "not in the marriage index"
  is not "married before the index begins".
- **A changed result count is a lead.** A canary that returns 84 where the last round logged 66
  has 18 rows to read against the corpus; most will be collisions, and the rest are new.
- **Blockers carry a re-test date, and every round re-tests them.** Blocks expire: a server
  that errored at edition 39 worked at 42; JPress fell at 59 and answered at 60; a collection
  labelled blocked from edition 55 was found open at 68 — it had been open the whole time. A
  `🔁 re-check` status with a date is the difference between a blocker and a superstition.
- **Every blocker names what it costs**, in research terms, and **pending correspondence is a
  blocker with a date.** Archives answer more often than researchers expect — a camp archivist
  answered next day with the original transport list; a volunteer index coordinator answered
  next day with the spelling that unlocked the family's own birth records — but on their own
  schedule. File early, log the date, keep working.
- **Surface the whole blocker list in the same message as the findings**, once per working
  session, not one at a time.
- **The report's open-actions chapter is a priority-ranked subset**, ordered by what a finding
  would change — not a dump of the ledger.

## How the ledger drives the loop

At the start of a working session: read the open items, run the canaries for the servers they
need, log the results, and pick the next actions by what a finding would change.

While working: write the negative the moment a sweep comes back empty (the exact coverage is
only in your head for a few minutes), and open an item the moment a document raises a question
you are not chasing right now. **A lead you noticed and did not write down is a lead you lost.**

At the end: close what was resolved, re-rank what remains, write the edition entry.
