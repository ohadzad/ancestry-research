# Build pipeline — one archive, one engine, one skeleton, per-project declarations

The deliverable must be **rebuildable from Markdown with one command**, and the build must
**fail if anything is broken**. Keep source-of-truth in `.md`; generate HTML.

An archive holds one or more research projects. They share a build engine and a page skeleton;
each project declares only what is its own; and a **portal** at the root lists them. A
single-project archive uses the same arrangement with one entry — there is no lighter mode
worth maintaining separately.

---

## Layout

```
<archive>/
  index.html               # the portal — GENERATED from the registry, never edited by hand
  research_registry.json   # the projects, their people, numbers and links
  build_portal.py          # builds index.html; fails if any relative target is missing
  .nojekyll  README.md  .gitignore
  common/
    TEMPLATE.md            # the format spec and the 8-step conversion recipe (gate list drifts; qa.py rules)
    genealogy_site/        # the engine — a Python package every project imports
      __init__.py          #   public API: ProjectConfig, Palette, TreeSource, SpineFact, Person, build
      config.py mdpipe.py figures.py theme.py shell.py bidi.py tree.py qa.py site.py build.py
  <project>/
    build.py               # 200–320 lines: THIS project's declaration + its transforms
    report.md              # chapters only; no h1, no date line, no changelog
    sources-index.md       # every file: provenance, what it is, what it proves
    CHANGELOG.md           # the ascending edition log
    open-targets.md / THREADS.md …   # the ledger (research-ledger.md)
    index.html             # redirect stub — GENERATED each build (URL-encoded target)
    <main>.html            # the built report
    docs/                  # originals + evidence crops + thumbnail cache
      <archive>/ evidence/ thumbs/ family_docs/ letters/(gitignored)
    site/                  # the publishable mirror (gitignored; rebuilt from scratch)
```

## Environment

- The build needs `markdown` and `pillow`, from a **virtualenv outside the archive folder**
  (`~/.venvs/<archive>/bin/python`). The archive lives in Dropbox; a venv inside it syncs
  thousands of files for nothing. Never move an existing venv — its absolute paths are baked
  in; build a new one and delete the old.
- Run every build from the project directory (`cd <project> && $PY build.py`), then the portal
  from the root.
- A project resolves the engine through a short candidate list — `$GENEALOGY_COMMON`,
  `../common`, the archive's absolute path, a local `_common` mirror — and sets
  `qa_strict = (engine is not the local mirror)`: strict inside the archive, where every relative
  target (the breadcrumb to the portal included) can resolve; report-only outside it.

## What a project declares

One `ProjectConfig` in `<project>/build.py`. The fields that carry the work:

| Field | What it is |
|---|---|
| `slug, main_html, title, subject, meta_description` | identity |
| `report_md, sources_md, changelog_md` | the source files (`changelog_md` optional — set it and the changelog lives outside the report) |
| `palette` | **the report's accent** — nine colour tokens. This is the whole visual difference between two reports in one archive |
| `tree` | `TreeSource(kind='html_extract'\|'svg_file', path, page_href, label)`. Both shipped projects use `html_extract`: the tree is authored as a standalone page (SVG + `.legend` + `.foot`) and the engine lifts those three out; `svg_file` exists but is untested |
| `spine` | four `SpineFact` — verifiable numbers, not slogans |
| `people` | `Person(name, dates, role, anchor, aka)`. **`aka` is the alternative-spelling field, and it is what makes the search useful** — every transliteration goes in it |
| `people_legend` | one line under the person index explaining `?` / `~` date marks |
| `search_extra` | non-person search rows: places, camps, archives |
| `figures` + `figure_anchors` | evidence crops and a regex saying which paragraph each follows — the inline-argued strategy |
| `gallery` | `(crop, target, caption)`; the target may differ from the crop. A mature project loads this from a JSON manifest (`docs/evidence/_gallery.json`) instead of hand-listing. **Filter by `os.path.exists`** so a missing scan degrades instead of failing the build |
| `text_transforms` / `report_transforms` / `sources_transforms` | project-specific linkification: testimony timestamps → deep links, archive ids → dual links, `[[13]]` → `#src-13`, bare filenames → local links. Applied outside tags and anchors |
| `extra_bidi_rules` | additional isolate rules. **A project-specific range wrapper is a text transform, not a bidi rule** — the bidi pass runs its rules in sequence over one string, and a range wrapped there nests inside a Latin run wrapped a rule earlier |
| `legacy_anchors` | `{'ch-6': r"^פרק ו'"}` — already-published anchors mapped **by heading regex, not position**; generate the map when numbering is regular |
| `toc_overrides` | heading regex → short nav label, for chapters whose first words are identical |
| `breadcrumb` | `('../index.html', label)` back to the portal |
| `provenance_note`, `footer_note`, `md_extensions` | small text and parser options |
| `site_extra_files` | files to copy into `site/` beside the page (a standalone tree page, its SVG) |
| `thumb_referrers` | other pages that use this project's thumbnails — **always `('../index.html', '../research_registry.json')`**, or the cache sweep deletes the portal's cover image |
| `privacy_file_patterns` / `privacy_text_patterns` | globs kept out of `site/`; substrings that must not appear in the page. Assemble the requester's identifiers (`'ohad'+'z'`) — the config file is published beside the report and a literal would trip the grep |
| `qa_strict` | fail vs report (see Environment) |

## Writing conventions the engine expects

- **`::: lede` … `:::`** — the opening box, one per report. The fence is generic:
  `::: <name>` becomes `<div class="<name>">` with its body rendered as Markdown; `::: note` is
  the caveat box. (A bare `<div>` is stripped by the pipeline; the fence is why.)
- **An evidence figure** is `[![alt](crop)](full-original)` — or a bare `![alt](crop)` line,
  which is auto-wrapped in a link to the full file — followed by **one italic paragraph** that
  is the caption. The caption must be its own paragraph, or the crop and the prose merge into
  one figure and the prose vanishes from the body. Figures are numbered ("איור N") only when
  captioned.
- **The certainty ladder in `**bold**`** becomes a coloured chip. Four rungs plus the two
  derivatives. `*…**bold**…*` — bold inside italics — **does not render**; 25 names lost their
  emphasis twice before it became a gate.
- Tables: empty `<thead>` rows are stripped, `<th>` gets `scope="col"`, and the table is wrapped
  in a keyboard-reachable scroller (WCAG 2.1.1) — only when it actually overflows.
- Heading ids are Hebrew-preserving slugs with collision suffixes.
- **No h1 and no date line in the report Markdown** — the hero carries them, with the edition
  and a build version.

## The gates

`qa.run_all` runs on every build and raises `SystemExit` under `qa_strict`. **In the shipped
engine it runs *after* the page is written and mirrored** (`build.py` writes at the top,
gates below), so a red build leaves a bad page on disk — a corrupt page once shipped exactly
this way. Either move the write below the gates or delete the outputs on failure; until then,
a publish script must refuse to run on a red build. Validate a new gate by **fault injection**
— break the page on purpose and watch it fail. The list, from `qa.py` (the code is
authoritative; `common/TEMPLATE.md §5` lists the gates too but has drifted — it claims
intrinsic image dimensions are gated, and predates the count and edition gates; fix the spec
when they disagree):

- `markup_integrity` — balanced tags; no nested `<a>`, `<em>`, `<figure>`, `<bdi>`; no crossed
  emphasis;
- `bidi_hygiene` — each isolate rule re-run over the finished prose (below);
- `markdown_leftovers`, `entity_hygiene`, `attribute_hygiene` — unprocessed Markdown,
  double-escaped entities, malformed attributes (a value broken by a *pair* of quotes leaves an
  even quote count and silently swallows the attributes after it);
- `images_have_alt` — `alt` on every image. Intrinsic width/height are added best-effort by
  `figures.dims()` when Pillow is present; **they are not gated**;
- `anchors_resolve`, `duplicate_ids`;
- `search_targets_resolve` — the in-page search index lives inside `<script>`, where the anchor
  gate cannot see it;
- `glyph_coverage` — a hard-coded set of codepoints with no glyph in the theme's font stacks;
  they ship as empty boxes. Add to the list; never assume a symbol renders;
- `template_leakage` — `%%` and `{{` survivors (an f-string vs `%`-format trap);
- `source_links_open_out` — every link to a source file carries `target=_blank`: the report is
  tens of thousands of pixels long and returning from a scan reloads it and loses the place
  ("the heaviest defect in the delivery audit");
- `images_are_light` — `IMAGE_BUDGET` 320 KB per image: an archival scan is not a web asset;
- `local_links_exist` — run **twice**, on disk and again under `site/`;
- `prose_files_exist` — files *named* in the prose, not only files linked;
- `privacy` — the patterns appear nowhere in the page.
- Not a gate but a design rule with the same effect: the hero's edition number is **derived**
  from the changelog's highest `מהדורה N` (`build.py`), never typed — it stayed stale for two
  editions when it was. One project built a **count/render** gate in its pre-engine script (every number
  the text declares — sources, figures, grades, in digits and in words — compared with what the
  page renders); it did not survive the migration to the shared engine. Add it back rather than
  inventing it; until then the audits catch these by hand.

## RTL protection — the part that is easy to break and hard to see

`bidi.py` wraps runs in `<bdi dir="ltr">` by an ordered rule list — at present a long Latin
run, a month/year range, a numeric range with an en-dash, an archive reference code, a number
with a thousands space — plus a project's `extra_bidi_rules`. Two invariants: never wrap what is
already inside a `<bdi>`, and never insert one into `<svg>`, `<style>`, `<script>` or `<pre>`.
Tag boundaries are replaced by NUL, not space, so two fragments either side of `<em>` are not
mistaken for one run.

What actually goes wrong:

- **An en-dash between digits inside an SVG.** No `<bdi>` there — the tree generators convert
  it to a plain hyphen, and a post-render guard over the whole HTML catches the rest.
- **Parentheses.** An unmatched `)` inside an isolate mirrors against the `(` outside it; a regex
  fix for that produced the mirror-image bug. Bracket handling is a **balancing function**, not
  a pattern.
- **Hebrew punctuation trapped inside the isolate.** `<bdi dir="ltr">1898–1918,</bdi>` — the
  comma belongs to the Hebrew sentence. The isolate ends on a digit.
- **Hebrew forced into `dir="ltr"`.** `04.01.1865 – לפני 08/1944` reverses whole and reads as
  death-before-birth. A string containing a Hebrew letter stays in the RTL flow; only the
  numeric runs inside it are wrapped.
- **`<code>` with no explicit direction** inherits `rtl` and every literal reverses.
- **The portal has the same problem in miniature**: a pure numeric range in a life-dates line
  must be isolated or `1929 – 2021` renders as `2021 – 1929`.

The gate re-runs **each** rule over the finished prose: a run that survived unwrapped is a hole
in the rule, not in the text — and a rule that stops matching (a project whose reference codes
use a different separator) is reported instead of shipping reversed.

## Weight and images

- `figures.display_copy` makes a **display copy** at 1400 px (the reading column is 60 rem;
  1400 px covers it at 2× without shipping a 2,500 px scan), re-encoding anything over 200 KB
  down a quality ladder; the *link* still goes to the full original. One project went from
  12.9 MB to 5.2 MB, and a reader who never scrolls downloads 95 KB.
- Thumbnails are cached under `docs/thumbs/` with the **quality in the cache key** (or a
  re-encode silently returns the heavier cached copy), transparency flattened onto white, and a
  sweep that deletes every thumb not referenced by the page or by `thumb_referrers`.
- Lazy images are promoted to eager on **first scroll** (`requestIdleCallback`) with
  `beforeprint` as backstop — promoting on load would download the whole gallery for a reader
  who never scrolls, and a fetch started inside `beforeprint` is not awaited.
- A crop far wider than its frame (one row out of a transport list) is shown **whole** in the
  gallery (`object-fit: contain` above aspect 2.4), or it is magnified past its own resolution.

## Print

The printed PDF is a real deliverable — families print it. Wrong by default:

- The **family tree** needs its own landscape page (`break-before: page; page: landscape`) and
  the SVG a `max-height` in millimetres (118 mm), not `width:100%` — a near-square diagram fitted
  to the width spills over two pages and gets cropped.
- **Tables switch to `table-layout: fixed; overflow: visible`** in print, or a wide table
  silently loses its last column.
- **Every element hidden off-screen must be `display:none` in print.** A skip link parked at
  `inset-inline-start:-9999px` widened the page box: a 103-page report printed as 53 pages, each
  truncated at its side.
- Expose the **external** URL after each link in print (`a[href^="http"]::after`); not relative
  paths, which only repeat the filename.
- Secondary text keeps a **12.5 px floor** on screen and paper (`.72rem` fails it).

## The portal layer

`build_portal.py` renders `index.html` from `research_registry.json`:

```json
{ "site": { "title", "surnames", "intro", "note" },
  "researches": [ { "slug", "name", "aka", "life", "state", "state_label", "edition", "summary",
                    "cover", "cover_alt", "cover_href",
                    "stats": [ { "n", "l" } ], "links": [ { "label", "href", "primary" } ],
                    "people": [ { "n", "d", "s", "h" } ] } ] }
```

It ends with its own gate — every relative `href`/`src` must exist on disk (directory targets
get `index.html` appended) — and `sys.exit(1)` on a miss; like the project build, it writes
`index.html` *before* gating, so a red portal build also leaves a bad page on disk. The status badge sits **outside** the
heading text, so a screen reader announces the person's name, not the project's status.

**Adding a research project to the archive:**

1. Create `<slug>/` with a `build.py` declaring its `ProjectConfig` (copy the nearest project's
   and change the declaration; the transforms are where its citation dialect lives). Set
   `breadcrumb=('../index.html', …)` and `thumb_referrers=('../index.html', '../research_registry.json')`.
2. Build it; fix what the gates say.
3. Add its entry to `researches` in `research_registry.json` — links, numbers, people, cover.
   The registry **accumulates**; the restructure scripts never overwrite it once it exists.
4. `$PY build_portal.py` from the root; it fails if any relative target is missing.
5. Re-run the project build once more (the portal's thumbnail references are now known to the
   sweep), then publish.

`common/TEMPLATE.md §7` holds the eight-step recipe for converting a *legacy* report — one
built by a project-specific script before the shared engine existed — into a declaration.

## Family-tree SVG (hand-laid drop-line descendant chart)

- One box per person: name + `נ׳`/`נפ׳` years; a legend maps colours to fate, with an explicit
  **"fate undocumented"** bucket as the fourth colour.
- Spouses joined by a marriage line labelled with the year; a drop line to a **sibling bus**;
  children in birth order (RTL: eldest on the right). Siblings' children are packed inside the
  parent's box as `|`-separated sub-lines rather than given boxes of their own.
- Keep the **compact tree** readable; put **everyone** — all children, all wives' offspring,
  infant deaths — in the **full tree**.
- The chart is hand-placed (absolute x/y per box, hand-routed paths): adding a person is a
  re-layout, not a data edit. Budget for that.
- Generate in Python, emit a standalone page with `<svg>`, `.legend`, `.foot`; the engine
  extracts those into a horizontal-scroll frame, adds `<title>` and `role="img"` if absent, and
  opens it at a zoom where the smallest text is legible (75%, not 38%), with zoom buttons.
  Readability comes from `--tree-zoom` on the frame, never from font-size.
- After generating, **render it and look at it.** SVG collisions and overflow are invisible in
  the source and obvious in a screenshot.

## Evidence crops

Prefer the **downloaded original** over a browser screenshot whenever the original is in hand.

```python
import pymupdf as fitz
from PIL import Image
p = fitz.open('docs/arcanum_full/<page>.pdf')[0]
# locate: rects = p.search_for('needle')  (OCR text layer; letters may be spaced —
#         fall back to p.get_text('words') coords, or a fixed clip rect)
pix = p.get_pixmap(matrix=fitz.Matrix(3, 3), clip=fitz.Rect(x0, y0, x1, y1))
Image.frombytes('RGB', (pix.width, pix.height), pix.samples).save('docs/evidence/..._zoom.png')
```

Stack a **header/column row** above the **data row** so the crop is self-explanatory. Every
caption is bilingual (foreign quote + translation), carries the exact locator, and clicks
through to the full original. A `<figure>` is injected after `</p>` but *before* `</li>` — it is
not a valid child of a list.

Reading craft that recurs (details in `archive-tooling.md`): contact-sheet a container's pages
grouped by **page dimensions** to separate form types; `pdftotext -bbox` and the **reversed**
Hebrew token when column OCR interleaves; 12–16× Lanczos with a computed threshold to lift ink
off a watermark; **900 dpi to adjudicate handwriting** when two editions read a field
differently.

## Verifying a build

The gates catch structure; they do not catch ugly. After a substantial change, render the page
headless and **read the screenshots**: desktop, 390 px mobile, the tree, the gallery, the person
index, and the print PDF. Measure the things that are quietly wrong — anchor clearance under the
sticky nav, horizontal overflow at 390 px, link contrast, whether a search result actually lands
where it should, whether a fix broke its neighbour (`overflow-x` on the nav clipped the search
box vertically). Each of those has shipped broken at least once behind a clean build.

## Publishing safely

- **The build runs inside the publish script, before `git add`.** A script that only did
  `git add -A` published a page built the night before the last edit — the live site showed the
  pre-edit text and the audit caught it, not the author.
- **`git add -A` publishes everything not ignored.** One push carried the audit reports, a memory
  file, the push script itself and a folder of draft letters to archives. Ignore the
  helper scripts, `audit-round-*.md`, `docs/letters/`, `site/`, `chunks/`, audio, and the working
  archive folder — written against the project's *own* file names (the real audit reports were
  `דוח_ביקורת_סבב6.md`, which an English `audit-round-*.md` pattern never matches) — and
  remember **`.gitignore` does nothing when the project directory is not itself the git
  repository**.
- **A leak already pushed is not undone by the next commit.** It remains in the git history and
  in the Pages cache. Rewrite the history (or delete and recreate the repo), purge the cache by
  republishing, and treat any leaked e-mail address as burned.
- **`rsync --exclude` does not delete files already copied by an earlier run**; use
  `--delete-excluded`. An **include-only** `aws s3 sync` (the S3 variant) structurally cannot
  leak working files, which is the safer shape.
- **Anchor `.gitignore` patterns** where a glob could swallow records (`/testimony.mp3`, not
  `testimony*` — a bare glob excluded legitimate `testimony_*.json` records and broke 29 links).
- `.md` and `.txt` linked from the page render raw on Pages — convert linked Markdown to HTML in
  the build.
- **Renaming a Pages repo kills the old URL**; Pages does not redirect. Rename once, early, or
  never.
- The cloud sandbox usually cannot reach GitHub; prepare the repo and hand the user a one-paste
  script for their own machine, then **verify the live site** after the push: the redirect, the
  main HTML, an image, a JSON.
