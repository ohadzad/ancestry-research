---
name: documentary-genealogy-research
description: >
  Source-linked documentary family history — Holocaust/Shoah reconstruction, and equally
  Ottoman/Mandate-era, Sephardi, Yemenite and pre-state Israeli families — turning archives,
  vital records, consular registers, press, burial records and testimony into a verified report
  with family tree, evidence gallery and sources index. Use when researching a family's history
  or a person's fate; placing relatives from vital records, censuses, camp records or voter
  rolls; tracing a life in Ottoman Palestine or Israel; mining a testimony or memoir; building a
  family tree; auditing such a report; adding a project to a research archive; or publishing it
  to GitHub Pages. Triggers: "research my grandmother", "find X's birth record", "what happened
  to the family in the Holocaust", "search JewishGen / Yad Vashem / Arolsen / IGRA", and Hebrew
  equivalents ("תחקור על סבתא שלי", "תבנה עץ משפחה", "פנקסי בוחרים"). Not for surname trivia,
  DNA kits, or living-person background checks.
license: For personal/family research use.
---

# Documentary Genealogy & Family-History Research

This skill is a complete method for reconstructing a family's history from primary sources and
delivering it as a **verified, source-linked, publishable research corpus**: a main report, a
graphical family tree, an evidence gallery, and a sources index — every factual claim backed by
an exact external link **and** a local copy of the source.

It was distilled from two real, multi-week projects that share one archive and one build engine:
a Carpathian Shoah reconstruction (44 editions; roughly twenty external audit rounds, numbered
1–13 and then restarted) and a Sephardi–Gibraltarian–Yemenite family in Ottoman and Mandate
Palestine (75 editions; audit rounds numbered to 33 in the changelog while the report's own body
speaks of "the twelfth" — the numbering drifted in both, which is itself a lesson in §6). The
discipline below is what held across both, and it is what separates a trustworthy family archive
from a plausible-sounding story. It is written for a Hebrew RTL deliverable; adapt the ladder and the
conventions to the report's language and keep them uniform.

---

## 0. Prime directives (never violate)

1. **Every claim is dual-sourced.** Beside each fact: the exact external source (archive URL,
   DB record id, page/volume/line) **and** a local copy of *the document itself* in the repo —
   not a screenshot of the web page that points at it. The rare legitimate exceptions (no
   public address; an online reference with no separate document) are annotated in the sources
   index with their count stated there. If you cannot source it, mark it (`טעון אימות`, "needs
   verification"), never state it plainly.
2. **An index row is not a record until the scan is read.** Three false relatives entered one
   project from index lines whose scans said other names entirely. The same goes for OCR hits,
   catalogue descriptions and finding aids: they locate, they do not testify. Grade an index row
   `ככל הנראה` at most until the page is in hand.
3. **Evidence = crops from the original page, not search-result cards** — and the crop clicks
   through to the full original, which is saved whole (the page, the issue), because the crop
   alone once carried the wrong year.
4. **Uniform certainty grades.** One ladder, applied consistently: `מאומת` (verified by a
   document) · `כמעט ודאי` (near-certain) · `ככל הנראה` (likely) · `אפשר ש… — טעון אימות`
   (possible; needs verification). **Grade the document separately from the identification
   that rests on it**, and per cell, not per table. A byline proves authorship, not identity; a
   family-filled institutional page is graded relativised ("verified *in the membership card*");
   background knowledge that was not checked against a listed source carries no grade at all,
   so it cannot borrow the chip beside it — and an unverified fact never *corroborates* a
   verified one. The ladder, its extensions and the house rules: `references/conventions.md`.
5. **A negative is a finding; an error is not.** Record every empty search with its exact
   coverage — and never write "0 results" from a query that errored or a server whose canary
   was red: no question was asked. A negative never becomes a positive ("not in the marriage
   index" is not "married before the index begins").
6. **One clean final version.** The report is the current truth; history lives in an
   **ascending changelog** (new edition always after the last). Old entries may be *corrected*
   — a miscount, a leaked name — with the correction recorded in the new edition; they are never
   rewritten to look right.
7. **Translate every foreign-language quote** inline. A quote without a translation is a defect.
8. **No plain-text file/URL mentions in the deliverable.** Every archive URL and every "saved in
   the folder" is a real markdown link to a resource that exists on the published site.
9. **The requester is invisible** — not in the report, the changelog, the sources index, a
   linked letter, the build config, or the published folder. Living relatives' contact details
   never reach the site; one whole tree stayed offline for that reason.
10. **Never bypass a block.** A `robots.txt` exclusion, a Cloudflare challenge, a reCAPTCHA, a
    rate limit: each is a hand-off to the user's own browser, logged as a blocker. Find out what
    is actually behind the block first — often it is a bug, a mirror of an open archive, or a
    collection that holds nothing you need.
11. **Material handed to you is a lead, not a source.** A family's scan, a third party's
    research summary, a user-contributed tree: verify each claim live in the archive before it
    enters the report, and say what you could not verify.
12. **This is emotionally heavy material.** Handle victims and survivors with dignity; state
    deaths and fates plainly and respectfully, without embellishment.
13. **Always sweep the press — every person, every project, before the first audit.** The
    newspapers are a standing source, not an optional extra. Search the subject, the spouse,
    both sets of parents, the siblings and the children, in every relevant press archive
    (JPress for Hebrew, Yiddish and Maghrebi French; Arcanum for the historic Kingdom of
    Hungary; the local national archive elsewhere), under every spelling in the name matrix
    (§2). The press is where the living years show up: one sweep found a subject's father
    handing over a memorial cup in 1975, a year after the last document that named him, and
    a ma'apilim list printed in March 1947 that confirmed a ship and a hometown for two
    subjects the archives had left at `ככל הנראה`. A press hit is graded like any record:
    the name alone is `טעון אימות` until age, place, parents or context tie it to the subject.
    Read a list's columns from its own rows before using a number: in the 1940s ship lists
    of "לקרוב ולרחוק" the figure after the name is the **age**, not the birth year — a
    sub-agent once promoted a 32-year-old "Gedalyahu Farkas" to `כמעט ודאי` as a
    15-year-old subject born in '32.
    Save the article (scan if reachable, else the OCR text marked as an exception), and
    record every empty query as a negative with its coverage (titles, years, spellings).
14. **Every European-born person alive in 1939 gets a war-years chapter — and censuses go to
    the start.** For each such person on the page (subject, spouse, parents), reconstruct
    1938–1948: ghetto, deportation transport, camps and sub-camps with prisoner numbers,
    forced-labor service (Hungarian *munkaszolgálat* companies), hiding, liberation and
    survivor lists, DP camps, the route out (ship, Cyprus, Atlit). Sweep the camp and ghetto
    sources in §3 (Arolsen, Auschwitz transports, Stutthof, DEGOB, EHRI, Yad Vashem, JDC,
    ghetto inhabitant lists) and download every card front and back. A page where a survivor
    goes from birth straight to a 1948 marriage certificate is unfinished: either the chapter
    exists, or the report says, with coverage, what was searched and not found. Likewise, go
    up through **every census and register that covers the family's places**: for the
    Hungarian lands the 1828 *Conscriptio*, the 1848 Jewish census, the 1869 census, civil
    registration from October 1895, and the 1921 sheets where Hungaricana's library holds
    them; for other regions the equivalent stack (§3.1). State, per census, whether the
    place is covered — "not in the 1869 census" is a finding only for a covered county.

---

## 1. Workflow overview

```
INTAKE ─► RESEARCH (sources) ─► TESTIMONY MINING ─► BUILD (report+tree+index)
   ─► AUDIT (fresh external agent) ─► FIX ─► DELIVER/MIRROR ─► (optional) PUBLISH
                         ▲                                   │
                         └───────── loop until clean ────────┘
```

- **Tooling check (before anything else).** See §3.0 — find out which archive MCP servers are
  installed and run each one's canary.
- **Intake.** Ask — in **one** `AskUserQuestion` round, not a trickle — for the anchor
  person(s), every known name and spelling variant, places (historical + modern names), dates,
  the deliverable language, and **what the family already holds**: photos, a testimony video, a
  memoir, a printed family book, an old tree, an estate of papers, a cloud folder to mirror to.
  The five largest breakthroughs in one project came from material the family had all along,
  including volumes — and the copyright — a scanning-request plan had been written for. Ask in
  the same round about **subscriptions and credentials** (§3.0) — Arcanum in particular is the difference between
  reading the press record and guessing at it for the historic Kingdom of Hungary.
- **Research.** Sweep the archives in §3, saving originals locally as you go.
- **Press sweep (mandatory).** For every person on the page — not only the subject — run the
  press pass of directive 13: notices (birth, wedding, death, condolence, memorial), court and
  auction notices, lists (ships, deportees, survivors, workers, committees, voters), sports and
  community columns. Delegate it to a mid-tier sub-agent per family with the name matrix and
  the corpus's known facts, and require the OCR saved to `docs/<archive>/` plus a negatives
  list. A project is not ready for audit until its press sweep is logged in the ledger.
- **War years and censuses (mandatory).** Per directive 14: a camp/ghetto/labor-service sweep
  for every European-born person alive in 1939, and a census-and-register sweep up to the
  earliest series covering the family's places. Run them as parallel sub-agents in separate
  lanes (camps, censuses, press) so they don't duplicate each other.
- **Testimony mining.** Transcribe any video/audio, extract facts with timestamps (§4).
- **Build.** Assemble the corpus via the shared build engine (§5).
- **Audit.** Spawn a *fresh* subagent as an independent QA auditor (§6). Fix. Repeat.
- **Deliver.** Mirror files to the user's folder; optionally publish (§7).

**Run this loop autonomously — see §1.1.** Keep the ledger (§1.2) current throughout; it is
what lets the work survive context compaction and hand off to the next session.

### 1.1 Run the loop; don't narrate it

This work is long, and its natural rhythm is dozens of searches per finding. Stopping after each
one to report and ask "shall I continue?" destroys it. The default is **keep going until the
front is exhausted.**

- **Do not announce next steps and wait.** Take them.
- **Loop each phase to saturation, not to a fixed count** — and know that saturation is scoped
  to the material, not the project: every new content edition earns its own audit sub-loop, and
  the worst audit round in one project came *after* saturation had been declared, right after
  the biggest research burst.
- **Batch the questions.** Anything you need from the user — a subscription, a reCAPTCHA, a
  decision about publishing — goes into **one** `AskUserQuestion` round at intake, and
  thereafter into the blockers list, surfaced together at the end of a working session.
- **When a search fails, try the next spelling, the next index, the next archive.** Escalate to
  the user only when the blocker is structurally theirs: a credential, a payment, a
  human-solved challenge, an irreversible or public action.
- **Work the whole front before going deep on one thread.** Twenty archives with a shallow first
  pass beats one archive exhausted while nineteen are untouched.
- **Cross-check every new find against the corpus before calling it new.** One edition
  "discovered" a document the corpus had held for fifteen editions — and read a field
  differently, so both readings shipped `מאומת` three lines apart.
- **Stop and ask only for:** publishing anything publicly, spending the user's money,
  contacting a third party in their name, deleting anything, or a genuine fork where two
  branches lead to materially different reports.

When the user has said they will be away, or the session is scheduled: state the assumptions at
the top, proceed through the whole loop, and leave the ledger and the report readable cold.

**Report at the end, not throughout.** One message: found, ruled out, blocked, next actions.
Deliver files as they are produced — a draft the user can open beats a progress note.

### 1.2 Keep the ledger

Working files in the project folder, updated as you go, never allowed to go stale. Two shapes
have worked: **four files** (`THREADS.md`, `NEGATIVES.md`, `BLOCKERS.md`, `TOOLSTATE.md`) for a
single-front project, or a **numbered target table plus a round journal**
(`open-targets.md`, `research-queue.md`) for a long multi-branch one. In either: stable ids
that are never renumbered, closed items kept with the edition that closed them ("so it is not
chased again"), rejected candidates and disproved inferences recorded for the same reason, and
the report's open-actions chapter generated from it as a priority-ranked subset. **A lead you
noticed and did not write down is a lead you lost.** Format and rules:
`references/research-ledger.md`.

### 1.3 Delegate by the cost of the mistake

Sub-agents take a model override — so transcription and file mechanics go to the cheapest tier,
archive sweeps to the mid tier, and the audits, the testimony analysis and the certainty grading
stay at the top. **Delegate by how expensive the mistake is, not by how long the task takes.**

- **A sub-agent has none of your context.** State the environment, paste the thread, give an
  explicit output format, and say what "nothing found" must look like — otherwise a blocked
  server, an empty archive and a confused agent all come back as the same shrug.
- **MCP servers are reachable from sub-agents**, so a sweep can be pushed down a tier — but the
  brief must say to batch `ToolSearch` and to **run the canary first and report a red one as a
  blocker**, never as an empty result.

Brief templates and the non-Claude-model adjustments: `references/model-split.md`.

---

## 2. The multi-name problem (read first)

Names are the master key and the master trap. A single person can appear under the father's
surname, the mother's (religious-only marriages registered children under the mother's maiden
name across much of Central/Eastern Europe), the married or immigration surname, an
officially changed name (Ṣāleḥ→Zadok), and several transliterations of each — one Carpathian
family appeared as `Strulovits`, `Sztrulovics`, `Struljovic`, `Strulovic`, and the index itself
used a fifth, `SZTRULYOVICS`; one Gibraltarian merchant appeared six ways across one register
series — two of them alternating inside a single volume — with the index cross-referencing
"See Raw…". Given names shift across Hungarian, Yiddish, Hebrew, Ladino and Arabic forms (Aranka=Golda, Lipót=Zisel-Leib, Shlomo=Shalom=Solomon,
Eliezer=Azar=Azor).

- Build a **name/spelling matrix** early and search *every* phonetic bucket separately; the
  `*_variants` tools (§3.0) cover a matrix in one call and say which spelling surfaced each hit.
- **When a surname you are certain about yields zero, suspect the index's orthography before
  concluding absence** — and once the canonical spelling is found, **re-read every record
  already published** through it.
- **Search both sides** — a record missing under the father's name may be filed under the
  mother's; the maternal breakthrough in one project came only after the paternal buckets were
  exhausted. Search **both scripts** in Israeli indexes; they are different indexes.
- **A surname is not an affiliation.** Some surnames exist in two unrelated diasporas
  (Pariente: Maghrebi and Salonikan); a famous rabbinic dynasty of the same name is a trap, not
  a lead. Chain on patronymic, nationality, birthplace and arrival year together.
- **Papponymy cuts both ways.** The grandfather's name recurring is a lead; the *expected* name
  in a branch is background noise, not a discriminator.
- Places carry the same problem: record the Yiddish, Hungarian, Czech and modern names as one
  identity (Volove / Ökörmező / Volové / Mizhhirya) and say so once.

---

## 3. Archive playbook (sources + exact tool quirks)

### 3.0 Check for archive MCP servers first — they are the fast path

Purpose-built MCP servers wrap most of this method's sources: **Arolsen, Yad Vashem, the
Auschwitz and Stutthof museum databases, DEGOB, EHRI (portal and early-testimony edition),
JewishGen, Hungaricana, RadixIndex, MACSE, FamilySearch, JDC Names, Arcanum/ADT, Internet
Archive, TNA Discovery, Gibraltar National Archives** — plus the Israeli cluster: **IGRA,
JPress, NLI, the Israel State Archives, Google Pinpoint, the Tel Aviv archive, the infocenters
tenants (Ghetto Fighters' House among them), and the Montefiore censuses.** Where one is
installed it replaces the browser recipes: structured JSON, originals to disk with citation
sidecars.

Before planning any sweep:

1. List what is installed (`mcp__remote-devices__<server>__<tool>`) and load the schemas with
   **batched `ToolSearch`** calls — three or four calls cover the roster.
2. **Run every server's canary** (table in `references/mcp-servers.md`). An auth wall, a
   Cloudflare interstitial, an expired token and an empty archive all return the same nothing.
   The canary is a *known answer*, not a ping — a server can respond with rows and still be
   wrong. **A changed canary count is a lead to read**: a JPress canary returned 84 where the
   last round logged 66; all 84 were checked against the corpus's item ids, and four were new —
   one of them extending the subject's press record fourteen years forward.
3. Only then decide what still needs the browser or a human — mainly Hungaricana page images
   (reCAPTCHA), JPress issue downloads (reCAPTCHA), camp-museum email, KehilaLinks, USHMM.
4. **Log canary results and failures in the ledger**, and report the blockers together with the
   findings. Naming a blocker converts a dead end into a five-minute task for the user;
   swallowing it converts a resolvable fact into a permanent `טעון אימות`.
5. **Re-test the blockers every round, and date the re-test.** Blocks expire: a server that
   errored one week answered the next; a 403 the archive "would fix soon" was quietly fixed; a
   collection sat labelled blocked for thirteen editions while it was open the whole time. A
   blocker with no re-test date is a permanent `טעון אימות` you chose.

Reach by reflex for **`*_search_variants`** (all spellings, one call, per-spelling breakdown)
and **`*_download_*`** (file plus citation sidecar — dual sourcing in one call). An API
returning clean JSON is still **not** verification: rules 1–5 apply unchanged.

- `references/mcp-servers.md` — the European/Holocaust roster, per tool, with the canary table.
- `references/mcp-israel.md` — the Israeli cluster, post-1948 and pre-state.
- `references/pre-state-and-diaspora.md` — Ottoman, Mandate, consular, Sephardi, Yemenite.
- `references/arcanum-press-archive.md` — the subscription press archive, in full.

### 3.1 The sources

Detail and browser fallbacks in `references/archive-tooling.md`. The high-value sources and
the mechanics that cost time to discover — as **worked examples of a source stack**, not a list
of the archives that exist:

- **No server, no reference for your geography?** Then the first research task is the stack
  itself. Name the civil-registration regime and its start year, the community registers before
  it, the census and conscription series, the emigration port and the arrival country's
  immigration and naturalisation indexes, the burial and press indexes, the diaspora's own
  community records — and write that stack into the ledger before the first search, the way
  `pre-state-and-diaspora.md` does for the Ottoman/Sephardi world. A Polish family that left for
  Argentina needs JRI-Poland and the state archives' scans on one side and CEMLA on the other;
  nothing below names them, but everything below shows how to work such a stack once named.

- **JewishGen** — civil birth/marriage/death + censuses, plus JOWBR burials and the Gibraltar /
  Sephardi sets. The multi-field form silently ignores every filter after the first surname;
  `jewishgen_search_filtered` fixes that. Result sets POST; the two-GET workaround is in the
  reference. **Write to the volunteer index coordinator** — one answered next day with the
  spelling that unlocked the subject's own birth record.
- **Before the civil registry** (Hungarian lands): the 1728–1746 Jewish conscriptions, the 1828
  *Conscriptio regnicolaris*, the 1848 Jewish census — fiscal, name-searchable, and the only way
  up past 1895. **Cemetery photo surveys** (ESJF via the Narkiss Index) read whole cemeteries;
  their decisive payoff may be negative (patronymic-only stones extend no tree).
- **Yad Vashem** — Pages of Testimony + testimony catalogue. Save every PoT **scan**; records
  repeat and contradict each other on purpose — never deduplicate them. `yv_search_by_submitter`
  is the route to living relatives.
- **Arolsen** — two channels: the **free online collections** (searchable now; T/D files browsable
  in blocks of 500; always take the back of the card) and the **formal tracing request** (up to
  13 months; file early, log the ticket).
- **Auschwitz and Stutthof museum databases** — victim indexes plus, for Auschwitz, the
  **transports** with issued number ranges. Both have hard coverage limits that must reach the
  report: most Hungarian arrivals of 1944 were never registered; Stutthof's online index is
  ~81k of ~110k. **Email the museum archive**: Stutthof's head of archive answered next day with
  18 documents — and an interpretation that had to be graded like any other claim.
- **DEGOB and the EHRI early-testimony edition** — ~3,500 protocols of 1945–46, indexed by
  place and camp, not name. Search the town, the ghetto, the assembly point.
- **EHRI Portal** — which fond, in which archive. Read the `scopeAndContent`, not the title.
- **Arcanum / ADT — use it by default for the historic Kingdom of Hungary.** Property, boards,
  auctions, litigation, obituaries, community life, and the paper-trail of persecution; the
  **police wanted bulletin** carries DOB, birthplace, occupation, spouse and both parents. Paid
  subscription — ask at intake, sweep in one month, set the cancellation reminder at once.
  Search per collection and every spelling (a single-*p* `Rapaport` found what `Rappaport` missed).
- **Hungaricana** is two portals — *archives* (prisoner registers, notarial, probate, orphans'
  court; no Máramaros material) and *library* (the 1921 census sheets). Name the portal, or
  "not in Hungaricana" becomes the published error it once was.
- **RadixIndex and MACSE** — which databases and places record a surname at all; MACSE's
  name-change section connects two surnames that look unrelated.
- **JDC Names** — the years between liberation and arrival. **Exact search, not fuzzy**; a row
  with no DOB, birthplace or parents is a lead, not a finding.
- **FamilySearch** — token expires hourly; the tree is user-contributed and never above
  `ככל הנראה` on its own. An errored query is not a negative.
- **The Israeli record — a phase, not a footnote.** Voter rolls (they carry the father's name),
  burial records (JOWBR, BillionGraves, the Chevra Kadisha by phone), JPress obituaries (filed as
  advertisements; plene and defective spellings return different families), the State Archives'
  1948 census and rabbinical-court files, Pinpoint's immigrant lists, NLI and the Israel Archive
  Network's local photo collections. **Search every name twice, transliterated and in Hebrew.**
- **Pre-state and diaspora records** — consular registers of British subjects (ISA, IGRA, TNA
  FO 78/841/847), medal cards (WO 372/329), Montefiore censuses, Ottoman nüfus, Gibraltar's
  resident registers, the family's own estate; and the Yemenite branch that has **no civil
  registration at all** and grows in depth, not height. All in
  `references/pre-state-and-diaspora.md`.
- **When a scan is blocked, write to the archive — and check the source archive.** A 403 is
  usually a bug or a permission, not policy; a mirror's block may hide an open original. A
  short, specific email has produced the file within a day more than once.
- **Cross-refs** — deportation lists (DEGOB Kassa, Glazer/zchor), Braham's notes, USHMM,
  KehilaLinks town pages (a survivor testimony + a local `Nevek` list, usually).

Golden rules for sources:
- **Download the original**, don't screenshot the OCR card. Save the whole page or issue, not
  only the crop.
- Record the precise citation (fund/opus/delo/row, or volume/page/entry) *in* the evidence
  caption. **Distrust the column header** — one field carried nationality in some rows and
  birthplace in others.
- A record's real value is often a biographical detail buried in it — read the whole entry.
- **The finding aid is a source with its own errors** (a train filed under the wrong town, a
  ghetto placed in the wrong province, an OCR'd 54,000 read as 540,000). Grade it separately.
- **Three retellings of one source are not three sources.**
- **A catalogue description aggregates across containers** — the form you want may sit in a
  sibling file.

---

## 4. Testimony mining

If there's a video/audio testimony (YouTube, VHA, a family recording) or a written memoir:
1. Get the audio, chunk it, transcribe to a **timestamped** transcript — cheapest-tier work,
   delegate it (§1.3); the *analysis* in step 2 is not.
2. Produce a structured analysis file: new facts, corroborations, **contradictions**, quotable
   lines (with timestamps), and names/places to chase — the last go straight into the ledger.
3. In the report, link each cited moment to the exact timestamp (a YouTube `&t=SECONDSs` deep
   link), and note the convention once.
4. Treat testimony as **one source among several** — corroborate against documents and surface
   discrepancies rather than smoothing them (memory rounds ages, shifts dates, conflates camps).
   The tension between an oral date and a civil record is itself a finding.
5. **Family oral transmission gets its own log** (who said it, when, what it would close, what
   would confirm it) and is `טעון אימות` until a document arrives — ladder discipline, not doubt;
   the tradition has been right when the document looked wrong. A printed family book is a
   secondary source that *embeds* primary ones: grade the embedded scan, not the prose.

---

## 5. Build pipeline (deterministic, rebuildable)

Keep the **source of truth in Markdown**, generate the deliverables with the shared engine, and
let the gates stop a broken build from being published.

```
<archive>/index.html + research_registry.json + build_portal.py   # the portal — generated
common/TEMPLATE.md            # the format spec and the conversion recipe (qa.py is the gate list)
common/genealogy_site/        # the engine: mdpipe, figures, theme, shell, bidi, tree, qa, site
<project>/build.py            # this project's declaration — palette, files, people, figures
<project>/report.md           # chapters only: no h1, no date line, no changelog
<project>/CHANGELOG.md        # the ascending edition log
<project>/docs/               # originals, evidence crops, thumbnail cache
```

The page: a hero with a verifiable-numbers strip, edition and build version; a sticky nav with
**in-page search**; the report; the family tree; a numbered evidence gallery; a **person
index** with alternative spellings; the sources index; the changelog. Source links open in a
new tab (the page is tens of thousands of pixels long); images ship as display copies with the
link to the full original.

The gates: links resolving on disk **and** under `site/`, anchors, tag balance, **RTL
protection**, unprocessed Markdown, `alt` text, files named in prose, search targets, glyph
coverage, template leakage, image weight, privacy patterns. The edition number is **derived**
from the changelog's highest entry, never typed (it stayed stale for two editions when it was).
**Validate a new gate by fault injection**, and know that in the shipped engine the gates run
*after* the page is written — a failed build leaves a bad page on disk, so never publish on a
red build. Build from a venv *outside* the Dropbox folder. Adding a project to
the portal is a five-step recipe. All of it, and the RTL failure modes that are easy to break and
hard to see: `references/build-pipeline.md`.

---

## 6. The external audit loop (this is where quality comes from)

After each substantial build, spawn a **fresh general-purpose subagent** as an independent QA
auditor. Give it the files and the checklist; have it **write a findings report**
(severity-ranked) and change nothing else; then apply the fixes and record them as the next
edition. `references/audit-checklist.md` has the prompts; `references/conventions.md` the house
rules they check. Three audits, disjoint defects:

- **Evidence** — does the source say what the report says it says? Re-read the sources.
- **Outside world** — do the report's checkable claims agree with independent literature? It
  moves grades both ways.
- **Delivery** — does the page work: RTL, print, mobile, search, contrast, weight.

Every round starts by **verifying the previous editions' own changelog claims against the built
HTML** (five declared fixes once reached nothing) and by a **regression pass on the last fixes**
(a UX fix round's own verification pass found four regressions the fixes had created).
Consistency is checked across **seven surfaces** — body, sources index, captions, tree SVG and
legend, findings files, changelog, and the portal's registry and README — because residue from
an earlier edition on any one of them is a finding class of its own. An audit's proposed
*upgrade* of a grade is itself a claim needing evidence.

Run audits at the **top model tier**; the cheap rounds come back clean because they did not see
the problem. **Number the rounds once, project-wide** — both projects lost count of their own
rounds. Each content edition earns its own sub-loop; the curve is a saw-tooth, not a decay, and the
stop signal is a quiet round on *that* material plus one more to earn it.

---

## 7. Delivering & publishing

- **Mirror** every produced/updated file to the user's connected folder as you go — drafts too.
  Keep heavy working files (raw audio, chunks, `site/`) out of the deliverable set.
- **Publish to GitHub Pages** (or S3) when the user wants a live site. The site is the archive
  root; `.nojekyll` so Pages doesn't filter non-ASCII names; the **build runs inside the publish
  script before `git add`** (a script without it published the previous night's page); ignore
  the audit reports, draft letters, helper scripts and audio — `git add -A` once pushed a folder
  of audit reports and the requester's e-mail. `rsync --exclude` needs `--delete-excluded`; an
  include-only S3 sync cannot leak. Write the ignore rules against the project's *own* file names
  (`דוח_ביקורת_*.md`, not an English pattern that matches nothing). Renaming a Pages repo kills
  the old URL. **A leak already pushed is not fixed by the next commit** — it stays in the git
  history and the Pages cache; rewrite the history or delete and recreate the repo, and treat a
  leaked address as burned.
- **The cloud sandbox usually can't reach GitHub.** Prepare the repo locally and hand the user a
  one-paste script for their own machine; after they push, **verify the live site** — the
  redirect, the main HTML, an image, a JSON.
- **Public repo = publicly searchable.** Confirm public-vs-private for family material before
  publishing (free Pages requires public); minimise living-person data regardless.

---

## 8. Failure modes the directives don't already name

The prime directives (§0), the loop rules (§1) and the audit rules (§6) each stand on a defect
that shipped; these are the *other* ways the two projects went wrong, each caught by an audit
rather than the author.

- **Fixes that break their neighbour** (a bidi fix double-wrapping thirty runs; `overflow-x`
  clipping the search box) → regression pass on every fix round.
- **Writing an inference in the language of a reading** ("the register shows he was first" when
  it shows a row number) → grade per cell; say which cells were read at magnification.
- **Dismissing the competing candidate quietly** → state the case *for* the other one; keep both
  side by side until a record naming the grandfather decides it.
- **Silently widening a claim so new evidence confirms it** ("in Jaffa" → "in Palestine").
- **Calling one source three sources** because three publications repeat it; and **vouching
  for one record class with a source about another** (an 1886 press item on *religious*
  registers cited for the *civil* registers kept after 1895).
- **Reading a partial index as complete** → an empty result from a known-partial source
  supports `ככל הנראה` at best, however thorough the search.
- **Building an external route for material the family owns** → ask what they hold first.
- **Method chapter first** → the reader gave up before the content; method goes last.
- **Finishing at liberation** and never opening the Israeli record → half the life is missing.
- An edition inserted out of order; the edition number typed by hand → append after the last;
  derive the number from the changelog.
- A `.gitignore` glob (`testimony*`) swallowing legitimate records → anchor patterns; and a
  mirror folder holding files under old names while the HTML links to canonical names → 404s.
- Reaching for browser automation when an MCP server already wraps the archive; or trusting a
  server whose canary was never run — its silent failure mode is an empty result set.

---

## References

- `references/mcp-servers.md` — **the archive MCP servers**: per-tool catalogue, parameters,
  the canary table, and the gotchas (start here when they are installed).
- `references/mcp-israel.md` — the Israeli cluster: IGRA, the State Archives, Pinpoint, NLI,
  JPress, Tel Aviv, Ghetto Fighters' House, Montefiore — post-1948 and pre-state.
- `references/pre-state-and-diaspora.md` — **Ottoman, Mandate, consular, Sephardi and
  Yemenite records**; the family as the first archive; the name traps of that world.
- `references/research-ledger.md` — **the working files** (two shapes) that keep a long run
  coherent across sessions, and the rules either shape must obey.
- `references/model-split.md` — which model runs which phase, brief templates, non-Claude notes.
- `references/archive-tooling.md` — per-archive mechanics, the pre-registry layer, cemetery
  surveys, correspondence, browser fallbacks, page-reading craft.
- `references/arcanum-press-archive.md` — **the subscription press archive**: search/URL
  recipes, downloading originals, collection IDs, spelling discipline, evidence cropping.
- `references/build-pipeline.md` — the archive layout, the portal and registry, the engine, the
  per-project config, the gates, RTL protection, weight, print, safe publishing.
- `references/audit-checklist.md` — the three audit prompts, the saw-tooth, the severity rubric,
  the recurring finding classes.
- `references/conventions.md` — report shape, the certainty ladder and its extensions, sourcing
  rules and their exceptions, the changelog, **the sources-index format**.
