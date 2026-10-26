# Archive tooling — endpoints, mechanics, and browser quirks

> **Read `mcp-servers.md` and `mcp-israel.md` first.** Purpose-built MCP servers now cover
> most of this file: Arolsen, Yad Vashem, the Auschwitz and Stutthof museum databases, DEGOB,
> EHRI, JewishGen, Hungaricana metadata, RadixIndex, MACSE, FamilySearch, JDC Names, Arcanum,
> Internet Archive, TNA, Gibraltar — and IGRA, JPress, NLI, the Israel State Archives,
> Pinpoint, the Tel Aviv archive, Ghetto Fighters' House and the Montefiore censuses.
> Where one is installed, use it. This file is the **fallback** for what still has no server
> (Hungaricana **page images**, camp-museum email, KehilaLinks, Glazer/zchor, USHMM) and for
> the days a server's canary comes back red.

Copy-pasteable technical detail for the archives used in Central/Eastern European Jewish
and Holocaust family research. For Ottoman / Mandate / consular / Sephardi / Yemenite record
classes, see `pre-state-and-diaspora.md`. Adapt IDs/paths to the project. Always **save the
original** locally under `docs/<archive>/` and cite the precise record locator in the evidence
caption.

---

## JewishGen (Hungary / Subcarpathia and Vicinity DBs) — *browser fallback*

Civil birth/marriage/death registers (DAZO Fund 1606) + the 1921 Carpathian census.

**Superseded by `jewishgen_search` + `jewishgen_search_filtered` when the MCP is installed.**
Everything below is the manual equivalent.

- The public multi-field search form **ignores extra filters** (given name, town) — only
  the first surname field applies. Don't rely on it.
- Instead: open a specific database, then run an **in-page `fetch` scan** over its detail
  endpoint. Must execute **on the jewishgen.org origin** (cookies + CORS). Pattern:

  ```js
  // window.__scan: loop recstart, pull rows, filter client-side by town + names
  const base = 'https://www.jewishgen.org/databases/jgdetail_2.php'
    + '?df=<DB_GUID>&georegion=00hungary&srch1=<Surname>&srch1v=S&srch1t=Q'
    + '&srchbool=AND&dates=all&newwindow=0&recjump=0&HttpVerb=Post&recstart=';
  for (let rs = 0; rs <= TOTAL; rs += 50) {
    const t = await (await fetch(base + rs, {credentials:'include'})).text();
    // split by '<tr', regex-filter by town (Danilovo|Krajnikovo|…) and parent names
  }
  return out.join(' ||| ').replace(/[?=&;]/g,' ');   // sanitize! see quirk below
  ```

- **Opening a per-DB result list** from the DB picker: the "List records" button loses its
  target; call the form directly and force same-tab:
  `form.target='_self'; HTMLFormElement.prototype.submit.call(form);`
  (a field named `submit` shadows `form.submit`, hence `.prototype.…call`).
- The 1921-census index rows carry a **Hungaricana deep link (`&pg=`)** to the original
  sheet — follow it to download the actual census page.
- DB GUIDs are per-database (births/deaths/marriages/census each differ); discover them
  from the DB-list page rather than hardcoding across projects.

- **The canonical index spelling may be nobody's.** For one family the index held 235 births
  under `SZTRULYOVICS` and none under any spelling the family ever used. Once the canonical
  spelling is found, **re-run and re-read every already-published record through it** — the
  first pass was made through the wrong door.
- **The two-GET workaround, precisely**: results POST to `jgdetail_2.php`; call `jgform.php`
  first (it returns a per-database UUID), then GET `jgdetail_2.php` with that UUID. A second
  criterion is `srch2v=G` for a given name — found by experiment, validated against a known
  record before use. This same GET opens **JOWBR** and the Gibraltar / Sephardi sets.
- **Write to the volunteer index coordinator, not only to archives.** The JewishGen
  Subcarpathia project coordinator answered within a day and supplied the spelling
  (`Struljovic`) that produced the subject's own civil birth record.

## Before the civil registry (Hungarian lands, pre-1895)

The civil registers begin in 1895; the Jewish community registers before them are patchy. The
layer beneath is fiscal and it is name-searchable:

- **The 1728 / 1735 / 1746 Jewish conscriptions** of the county (MNL OL fond C 29), printed in
  *Magyar-Zsidó Oklevéltár* vol. 7 (1963) — read via Arcanum.
- **The 1828 *Conscriptio regnicolaris*** (N 26), name-searchable online.
- **The 1848 Jewish census** (H 15; microfilm 719,825). JewishGen's index of it holds ~178 rows
  for a whole county — a negative there supports nothing.
- 1857 and 1869 census sheets mostly do not survive for the region.
- Place trap: Úrmező (Ruszkapolyána) is not Ökörmező; check the county gazetteer before
  attaching a conscription row to the town.

## Cemetery surveys

The **ESJF surveys** (2019, via the Bezalel Narkiss Index, `cja.huji.ac.il`) and
`cdp.jewishgen.org` photograph and read whole cemeteries. Ninety-five photographs across three
cemeteries were read — a fraction of the ~464 stones the catalogue counts, which is why the
negative drawn from them was demoted from `מאומת` to `ככל הנראה`: a survey's coverage caps the
grade of any absence it supports. The payoff was still decisive — local practice was **patronymic-only**, so no
Carpathian tree can be extended from these stones. Also: the survey's own dating of the site
contradicted the researcher's stylistic dating by sixty years, and the survey's dating was
adopted — stylistic dating of stones is logged as a warning, not a method.

## Yad Vashem — *browser fallback (see `mcp-servers.md`)*

- Central DB of Shoah Victims' Names — Pages of Testimony (PoT) and name records. Save each
  PoT **scan** (the handwritten form is itself evidence of who reported whom) and the JSON.
- Testimony catalog records (video testimonies) give birth date, town, maiden name, and a
  structured route summary — a strong spine to hang the archival findings on.
- Place pages and the site search surface related records; the on-site search box needs a
  real click before typing.

## Arolsen Archives — *online collections: use the MCP; the tracing form is still manual*

- Camp intake cards, Hinweiskarten (cross-reference cards), DP/CNI cards. Viewing needs
  accepting terms; document URLs look like `/en/document/<id>`.
- **Online request form is Salesforce (shadow-DOM).** Native `<select>`s respond to a click
  then typing the option text ("Israel", "exact year"); some selects refuse type-ahead
  (leave optional ones blank). Beware: pressing Enter can leak a newline into a textarea;
  the layout shifts after typing, so re-screenshot before clicking. Formal responses can
  take **up to 13 months** (the SLA stated at filing; none had arrived after a month in the
  source project) — submit early and record the ticket.
- **T/D (tracing) files are browsable online in blocks of 500** (collection 6.3.3.2). Check
  there before the tracing answer arrives; it shortcuts the wait.
- **Always take the back of the card.**

## Camp museums (Auschwitz / Stutthof / …) — *databases: use the MCPs; email is still human*

- The online victim databases now have servers (`auschwitz`, `stutthof`), and the Auschwitz
  one also carries the **transport index** with issued camp-number ranges. Both are
  **partial by nature** — most Hungarian deportees of 1944 were never registered, and
  Stutthof's online index holds ~81k of ~110k prisoners — so a null there is not absence.
- The **direct email to the museum archive** is therefore still the decisive channel, and
  still human. It is often the richest one — the head of the Stutthof archive answered **the
  next day** with 18 documents: the original transport list, colour card copies, two book
  chapters. Always send a specific, cited ask (person, dates, prisoner number, and exactly
  which lists/register you want checked). Two cautions from that reply: the archivist also
  volunteered an *interpretation* ("the parents remained in Auschwitz, so were likely murdered
  there") that had to be graded like any other claim; and she stated a coverage limit ("we do
  not have all the lists of female prisoners sent to the subcamps") that belongs in the
  report's negatives. Other archives in the same project: DAZO never answered two letters;
  Prague logged a ticket; Auschwitz sent an auto-acknowledgement only. **The Auschwitz Museum's
  most useful statement was about absence**: no nominal transport lists survive for the
  Hungarian deportation — the answer to "why will there never be a name list".
- **The finding aid is a source with its own errors.** The Auschwitz Museum files one family's
  train under `10_Kőrösmező` (100 km from Ökörmező); Yad Vashem's ghetto record places
  Szeklence in Transylvania; Arcanum's OCR reads 54,000 as "540.000"; IGRA transcribes רף as
  רך. Grade the finding aid separately from the record it points to.

## Arcanum / ADT (Hungarian press & registries) — **see `arcanum-press-archive.md`**

The subscription press archive is the workhorse for Hungarian-lands research and has its own
full playbook: `references/arcanum-press-archive.md` (subscription + cancellation discipline,
collection-scoped search via a base64 `list=` payload, the ⤓ `Oldalak mentése` download flow,
reading a page's OCR transcript before spending a download, confirmed collection IDs,
spelling-variant discipline, and PDF cropping). Quick reminders only:

- Full-page view/download = **paid subscription**; work in the user's own logged-in browser.
- Collection-scoped search beats global: `.../search/results/?list=<base64 of
  {"filters":{"COL":["<Id>"]},"query":"…"}>`.
- ⤓ → `Oldalak mentése` → MENTÉS → PDF to `~/Downloads` (max 50 pages, **no CAPTCHA**).
- Try every transliteration of a surname and every Hungarian inflection of a place name.

## Hungaricana (1921 Czechoslovak census, "Popisný hárok") — *metadata: use the MCP*

**Hungaricana is two collections, not one.** The *archives* portal (`archives.hungaricana.hu`)
holds no Máramaros material; the *library* portal does (the 1921 census sheets). "Not in
Hungaricana" was a published error, corrected twice — name the portal.

Record **metadata** across the archival databases (prisoner registers, notarial, probate,
orphans' court) is now served by the `hungaricana` MCP. Only the scans need this recipe.

- Original household sheets, free to view; volume ids like `KANepszaml_00N_<place>…`; each
  physical sheet is `?pg=<n>&layout=s`.
- **Download requires solving a reCAPTCHA** in the "save pages" dialog — you cannot solve it;
  open the dialog and **hand off to the user** to check the box and click OK, then pick up the
  PDF from `~/Downloads`.

## Cross-reference sources

- **Deportation lists**: DEGOB Kassa (Košice) transit list (`degob.org/tables/kassa.html`);
  Glazer selection tables (`zchor.org/hungaria.htm`) — train, date, headcount, selection split.
  **These two and the Auschwitz Museum's transport record are not independent of each other**
  — the museum cites Gaško's Kassa count and Glazer's table derives from it. Agreement between
  them is one source retold three times; say so rather than calling it corroboration.
- **DEGOB protocols themselves** have a server (`degob`) — the tables above are a separate,
  static resource.
- **USHMM**: Holocaust survivor/victim DB; Encyclopedia of Camps & Ghettos (camp/subcamp entries).
- **KehilaLinks** (town pages) frequently hide the best local material: a survivor testimony
  and a `Nevek`/Klarsfeld deportation list for the specific town — always open the town's
  "Holocaust" sub-page.
- **Braham's notes** (*The Politics of Genocide*, on `mek.oszk.hu`) name which district went to
  which ghetto; **Kramerius** (Czech National Library) holds the interwar business directories
  that place a trade in a town and a year.
- **JDC Names: exact search, not fuzzy.** Fuzzy returned hundreds of noise rows; exact returned
  six. An index row with no DOB, birthplace or parents cannot be attached to a family — log it
  as a lead, not a finding.

## Reading the page — craft that recurs

- **Contact-sheet a container's pages grouped by page dimensions** to separate the form types
  filed together in one archival file, then crop the surname row from each form.
- **When column OCR interleaves**, `pdftotext -bbox` and search the **reversed** Hebrew token
  (`קודצ` for צדוק) to locate the word; then read the image, not the text layer.
- **Ink under a watermark**: cell-by-cell 12–16× Lanczos upscale plus a computed-threshold
  binarisation.
- **An un-OCR'd thousand-page microfilm**: contact sheets at intervals to find the alphabetical
  index, then render the index page at 300 dpi.
- **Two editions read one field differently**: re-render the archival original at 900 dpi and
  adjudicate; never let both readings ship.
- **Google Pinpoint is a locator, not a source**: its OCR once joined tokens from two columns
  into a name that is on no page. Verify every hit against the page image.
- **When a database mirrors an archive and returns an error, check the source archive** before
  logging a blocker — IGRA's 403 on a whole collection stood for thirteen editions while the
  State Archives had the same volume open online. And when a route is blocked, **find out
  exactly what is behind it** before assuming the block is what separates you from the find
  (a robots-blocked municipal archive turned out to hold only 2000–2008 mayoral mail).

---

## Browser-automation quirks (Claude-in-Chrome + local download bridge)

- **`javascript_tool` output is blocked if it contains `?`, `=`, `&`, `;`** (looks like a
  query string). Always end scans with `.replace(/[?=&;]/g,' ')`.
- The JS tool has **REPL semantics** at top level (last expression returns), but **inside a
  function you must `return`**. Top-level `await` works.
- **Screenshots get cropped to ~1025px after `resize_window`** in some states — if a capture
  is clipped, resize to a normal window (e.g. 1500×940) and re-screenshot.
- Use `find` → `scroll_to(ref)` → `screenshot(save_to_disk:true)` to capture a specific row.
- **Downloads land on the *user's* machine** (`~/Downloads`), reachable via the local-device
  bash bridge; stage them into the sandbox to process, then write outputs back to the user's
  folder. The mounted cloud-storage folder may fail in device-bash while `~/Downloads` works —
  route downloads through `~/Downloads` then move.
- Never trigger `alert/confirm/prompt` dialogs — they freeze the extension.
