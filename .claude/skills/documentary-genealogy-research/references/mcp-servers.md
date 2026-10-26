# Archive MCP servers — the fast path (use these before the browser)

A set of purpose-built MCP servers wraps the archives this method depends on. When they are
installed, **they replace almost all browser automation**: no login dance, no in-page `fetch`
scans, no output sanitizing, no screenshot cropping of search cards. Structured JSON comes
back, originals download straight to disk, and rate-limiting/caching are handled for you.

**Always check what is installed before planning the research** (§Availability), and fall
back to `archive-tooling.md` (browser recipes) only for what has no server.

This file covers the European / Holocaust-era servers. **The post-1948 Israeli cluster has
its own file: `mcp-israel.md`.** Arcanum has a third: `arcanum-press-archive.md`.

---

## Availability & loading

- The servers are usually reached **through the user's desktop bridge**, so tool names are
  `mcp__remote-devices__<server>__<tool>` (e.g. `mcp__remote-devices__arolsen__arolsen_search`).
  On a local install they may appear as `<server>__<tool>` — match whatever the tool list shows.
- They are normally **deferred**: load schemas with **one batched `ToolSearch`** call,
  `select:name1,name2,…`. Never one call per tool. With ~20 servers installed this matters:
  three or four batched calls cover the whole roster, forty separate ones waste the turn.
- **Run the health/status tool of each server you intend to use.** Nearly every server has one,
  and each is a real canary (a known query with a known answer), not a ping.

### The full roster and its canaries

| Server | What it holds | Health call | Green looks like |
|---|---|---|---|
| `arolsen` | ITS camp/DP cards, transport & death lists | `arolsen_health` | `ok:true`, canary total, `session_cookie_present:true` |
| `yadvashem` | Shoah Victims' Names, Pages of Testimony, testimony catalogue | `yv_health` | every named check `ok:true` (cluster, PoT, exact-vs-synonym counts, scan host) |
| `auschwitz` | Auschwitz Museum victim DB + 1,187 documented transports | `auschwitz_status` | `ok:true`, canary person found |
| `stutthof` | Stutthof Museum former-prisoner index | `stutthof_status` | `ok:true`, canary count > 0 |
| `degob` | ~3,500 DEGOB survivor protocols, 1945–46 | `degob_status` | `ok:true`, all four search forms present on both sites |
| `ehri-testimony` | EHRI Early Holocaust Testimony edition (~160 curated) | `ehri_et_status` | `ok:true`, canary identifier found |
| `ehri` | EHRI Portal — archival descriptions across ~2,000 repositories | `ehri_status` | `ok:true`, `api_status:"PRODUCTION"` |
| `jewishgen` | Unified Search over all JewishGen databases | `jewishgen_status` | session cookie present / `Logged in as …` |
| `hungaricana` | Hungarian archival record databases (prisoner registers, notarial, probate…) | `hungaricana_status` | `ok:true`, canary total ≥ expected |
| `radixindex` | Hungarian surname/place meta-index (5.5M records, 1.06M free) | `radix_status` | `ok:true`, canary place lists the canary surname |
| `macse` | Hungarian Society for Family History meta-index | `macse_status` | `ok:true`, canary sections non-zero |
| `familysearch` | FamilySearch tree + indexed records + full-text | `fs_status(ping=true)` | `access_token:"set"` **and** `ping.ok:true` |
| `jdc-names` | JDC Archives Names DB — 568,778 relief/migration records | `jdc_status` | `ok:true`, `cloudflare_passed:true` |
| `arcanum` | ADT press & registry archive (subscription) | `arcanum_account_status` | `loggedIn:true` + username |
| `internetarchive` | archive.org — books, periodicals, OCR full text | `ia_status` | `ok:true`, canary hits > 0 |
| `tna-discovery` | UK National Archives Discovery, 37M descriptions | `tna_status` | `ok:true`, canary record found |
| `gibraltar` | Gibraltar National Archives censuses 1784–1914 | `gibraltar_status` | `ok:true`, dropdown + GridView present |

The Israeli cluster (`igra`, `jpress`, `nli`, `archives-gov-il`, `pinpoint`, `tlvarchive`,
`infocenters`, `montefiore-census`) has its own canary table in `mcp-israel.md`.

**A server that is merely blocked — auth wall, Cloudflare, expired token — fails exactly the
way an empty database does: with nothing.** Never write "no such record" on the strength of a
call whose canary you did not run. A red canary is not a research finding; it is a blocker to
report to the user, and several of these are five-minute fixes only they can do:

| Symptom | Whose fix |
|---|---|
| `fs_status.access_token: "missing"` | User: FamilySearch OAuth token (expires ~hourly) into `FS_ACCESS_TOKEN` |
| `arcanum_account_status.loggedIn:false` | User: credentials, or the subscription lapsed |
| `jdc_status.cloudflare_passed:false` | User: clear the challenge in the server's browser profile |
| JPress `Cloudflare challenge not cleared` | User: `npm run login` in the server's profile dir |
| `igra_status` not logged in | User: credentials |

Subscription-bound servers carry the same lifecycle discipline as the websites: an Arcanum
MCP still burns the paid subscription, and **Arcanum allows one active device per account** —
if the user is also browsing adt.arcanum.com, page access can block for a few minutes after
switching. Keep the cancellation reminder.

### Two cross-cutting habits

1. **Prefer the `*_variants` tool wherever one exists.** `arolsen_search_variants`,
   `auschwitz_search_people_variants`, `stutthof_search_variants`, `jdc_search_variants`,
   `macse_search_variants` all take a list of spellings and return the **deduplicated union**
   with a per-spelling breakdown. One call replaces N searches and, more importantly, tells you
   *which* spelling surfaced each hit — which is the evidence that the spelling matrix in §2 of
   SKILL.md is doing work.
2. **A `*_download_*` tool is how the dual-sourcing rule gets satisfied cheaply.**
   `arolsen_download_document`, `yv_get_pot_scan`, `jdc_download_scans`,
   `pinpoint_download_page`, `tlv_download_file` all write the file **plus a citation
   sidecar**. Keep the sidecar next to the image; it is the precise-locator half of the rule.

---

## A. Camps, deportations, victims

### arolsen — ITS / Arolsen Archives online collections

Camp intake cards, Hinweiskarten, DP/CNI cards, transport and death lists.

| Tool | Use |
|---|---|
| `arolsen_search(name, phonetic=True, archive_ids, offset, limit≤1000)` | Person search. `name` is free text: surname, "Last First", **prisoner number**, or place. Returns `{total, rows:[PersonHit]}`; each hit has `doc_id` and `citation{url, signature}`; `dob` is a partial date with explicit precision. |
| `arolsen_search_variants(names:[…])` | **The workhorse for the multi-name problem.** Runs every spelling and returns the deduplicated union with `matched_query` per hit and `per_name_totals`. |
| `arolsen_search_facets(name)` | Which collections hold the hits, with counts + ids → feed as `archive_ids`. |
| `arolsen_list_archives(parent_id, query, depth)` | Browse the collection tree; node ids are valid `archive_ids`. |
| `arolsen_get_document(doc_id)` | Archival-unit metadata, collection path, indexed persons, `pages` (this doc's scans: 1=front, 2=back) and `file_pages` (every scan in the same archival file). |
| `arolsen_list_file(desc_id)` | Every document/scan inside one archival unit — how you find *all* cards in one prisoner's file. |
| `arolsen_download_document(doc_id, out_dir, all_pages=True)` | **Downloads JPEGs front AND back plus a `<doc_id>_citation.json` sidecar.** |

Notes that matter:
- A **person-entry id is not always the scan id** — the scans usually live under sibling ids
  listed in `file_pages`. If `pages` is empty, walk `file_pages`.
- **Always download the back of the card.** Reverse sides carry transfer dates, camp numbers
  and remarks, and are the half most often missed.
- The **formal tracing request** (Salesforce form, up to 13 months) is a separate, human
  channel. The MCP covers the free online collections only. File the tracing request early anyway.

### yadvashem — Central DB of Shoah Victims' Names + testimonies

| Tool | Use |
|---|---|
| `yv_search_names(last_name, first_name, maiden_name, place, birth_year, submitter, source, fate, mode, lang)` | `mode='synonym'` (default) applies Yad Vashem's own name expansion; `mode='exact'` is a literal, stateless match — use it to **confirm a precise spelling**, not to sweep. `last_name` matches last **or** maiden name. `lang='both'` runs he+en and tags each hit. |
| `yv_search_by_submitter(last_name/first_name/full_name, place, verify)` | **The living-relatives tool.** Finds every Page of Testimony filed by a given survivor. `verify=True` keeps only records whose submitter really matches — slow but authoritative. |
| `yv_get_name(record_id, include_cluster_members)` | One record or a whole cluster, **normalized but lossless**, with `submitter{names,relationship_to_victim}`, `source_type`, `images`, `raw_details`, `citation`. |
| `yv_get_pot_scan(record_id, out_dir)` | Downloads the Page-of-Testimony scan(s). **The scan is evidence in itself** — it shows whose handwriting reported the death. |
| `yv_search_testimonies(query)` / `yv_get_testimony(catalogue_id)` | Video + written testimony catalogue. `yv_get_testimony` returns `youtube_ids`, which is what makes `&t=<sec>s` deep links possible. |
| `yv_search_collections(query, data_bank, tab)` | Top search across ghettos, righteous, places, deportations, documents, photos. |
| `yv_get_place` / `yv_get_ghetto` / `yv_get_righteous` | Encyclopedia entries. **`yv_get_ghetto` English has returned HTTP 522 upstream — retry with `lang='he'`.** |
| `yv_field_codes()` / `yv_list_filter_values(field)` | Field-code table for `raw_details`, exact facet strings for `source=` / `fate=`. |

Notes that matter:
- **Fields repeat and are never deduplicated — that is the point.** One person's cluster can
  carry four surnames and three spellings of a birthplace, because four different people
  reported her. The disagreement between records is itself a finding; grade it, don't clean it.
- A `record_id` may be a **member record or a cluster id**. Cluster fetches are serial and slow.

### auschwitz — Auschwitz-Birkenau Museum victim database + transports

Two distinct corpora behind one server, and the second is the one people forget.

| Tool | Use |
|---|---|
| `auschwitz_search_people(...)` / `auschwitz_search_people_variants(patterns:[…])` | The victim index. The variants form returns the deduplicated union with `matched_patterns` per person id and `per_pattern_totals`. |
| `auschwitz_get_person(person_id)` | One person by the id in `victims.auschwitz.org/victims/<id>`. |
| `auschwitz_search_transports(search, date_from, date_to, page, limit)` | **Browse the 1,187+ documented transports.** `search` is free text over origin/name (`"Kassa"`, `"Hungary"`); dates accept `DD-MM-YYYY` or `YYYY-MM-DD`. Each hit carries `transport_id`, `arrival_date`, `origins` (place/region/coordinates), `numbers` (deported/registered counts and the **camp-number ranges issued**), and `remarks_en`. |
| `auschwitz_get_transport(transport_id)` | The museum's historical essay and sources for that train. |
| `auschwitz_transport_people(transport_id)` | People registered in the camp from that transport, with camp numbers. |
| `auschwitz_list_origin_cities()` | Every distinct origin place — **check the museum's exact spelling here before searching**, it is often the Hungarian ghetto name rather than the home town. |

Notes that matter:
- **An empty `auschwitz_transport_people` is a genuine answer, not a gap.** On the May–June
  1944 RSHA transports from Hungary most deportees were murdered on arrival without
  registration, so no per-person record exists. Say that in the report rather than leaving a
  silent hole.
- The **issued camp-number range** in `numbers` is the cross-check that ties a survivor's
  tattooed or carded number to a specific train. It is often the only way to connect a person
  with no personal record to a dated transport — and it is an inference, so grade it as one.
- The transport index is **filed by the museum's own naming**, which can be wrong about the
  ghetto a train left from. When four independent counts (Kassa list, museum record, a
  published table, a survivor's testimony) agree on one date and size, that is a strong
  identification — but if all of them ultimately derive from **one** underlying count, say so:
  three retellings of one source are not three sources.

### stutthof — Stutthof Museum former-prisoner index

| Tool | Use |
|---|---|
| `stutthof_search_prisoners(surname, given_name, birth_date, birth_place, residence, occupation, prisoner_number)` | At least one criterion required. `birth_date` matches as an **ISO prefix** (`YYYY`, `YYYY-MM`, `YYYY-MM-DD`) — day-first formats match nothing. Returns English field names plus the raw Polish row. |
| `stutthof_search_variants(surnames:[…], …)` | Deduplicated union across spellings, with `per_surname` counts. `too_many` in that map means the server **refused** that spelling and its hits are missing — re-run it with more criteria. |
| `stutthof_search_by_number(prisoner_number)` | One exact camp number. **There is no range or adjacent-number search**, so transport-mate sweeps by neighbouring numbers are impossible; query each number individually. |

**The caveat that must reach the report:** the online index is **partial — roughly 81,000 of
~110,000 prisoners.** An empty result *never* proves absence from the archive. For a definitive
answer the user (or you, on their behalf) writes to `poszukiwania@stutthof.org`. Two prisoners
whose Arolsen cards exist are documented as absent from this online index — so treat a null
here as "not in the online index", never as "not a prisoner".

---

## B. Early testimony (1945–46)

These are the testimonies taken **within months of liberation**, before memory settled into
narrative. They are the best corroboration available for a family's ghetto and deportation
dates, and they are indexed by place, not only by name.

### degob — the DEGOB protocols (~3,500, Hungary/Carpathia, 1945–46)

| Tool | Use |
|---|---|
| `degob_search(query \| topic_id, lang, offset, limit≤150)` | Full text. `lang='hu'` (default) searches **all ~3,500 protocols** on degob.hu in the original Hungarian; `lang='en'` searches only the translated subset on degob.org. Use **Hungarian place spellings** (`Ökörmező`, not Volove). |
| `degob_search_extended(sex, place_birth, date_birth, occupation, residence, concentration, ghetto, camp, lang)` | **The metadata search — this is the powerful one.** It queries the per-survivor boxes, so you can ask "who from ghetto X ended in camp Y" without a name at all. Place names stay Hungarian even in the English interface. |
| `degob_get_protocol(number, languages, max_chars, offset)` | Survivor metadata + full testimony text, Hungarian and (where it exists) English, plus the scanned-typescript viewer URL. |
| `degob_list_topics()` | The curated topic ids (camps, perpetrators, events, themes) for `degob_search(topic_id=…)`. |

**Survivor names are anonymised to initials on the site.** So do not search surnames — search
*places*: the home town, the ghetto, the assembly point, the camp. A protocol from the same
town and the same transport is corroboration for the route even when it names nobody.

### ehri-testimony — EHRI Early Holocaust Testimony edition

| Tool | Use |
|---|---|
| `ehri_et_search_items(search, page)` | Full text over the **English translation** plus all index metadata. Accent-insensitive with word-prefix matching (`Munkac` finds Munkács), but **no phonetic matching** — sweep variants yourself. |
| `ehri_et_get_item(item_id, include_files)` | All Dublin Core / EHRI fields flattened: subjects, places, persons, organisations, ghettos, camps, sources, plus the **full English text with editorial notes**. |
| `ehri_et_get_item_files(item_id)` | Direct download URLs (S3, no auth): `scan` = JPEG of the original protocol page, `transcription_tei` = TEI-XML, usually one `_EN` and one `_HU`. |

**This is a curated subset of ~160 items, not the whole DEGOB corpus.** Use it for the
scholarly apparatus — the TEI transcription, the indexed places, the English translation you
can quote — and use `degob` for coverage. An empty result here is not evidence of absence.

---

## C. Archival description & finding aids

### ehri — EHRI Portal

The union catalogue of Holocaust-related archival descriptions across some 2,000 repositories.
It does not hold documents; it tells you **which fond, in which archive, in which country**
holds what, which is exactly what you need before writing to an archive or planning a visit.

| Tool | Use |
|---|---|
| `ehri_search(q, type, country, holder, facets, page, limit≤100)` | `type` restricts to `DocumentaryUnit \| Repository \| Country \| HistoricalAgent \| CvocConcept \| VirtualUnit`. `facets` (`type, lang, country, holder, dates`) returns statistics whose values feed straight back as filters. |
| `ehri_get_item(id)` | Everything the portal has for one item, per language: scope and content, system of arrangement, archival history, extent, dates — plus an **ARK persistent id** and a citable `web_url`. Repository items carry address and contact details, which is how you get the email for a records request. |
| `ehri_search_in_holder(holder_id, q)` | Search inside one repository, unit or country (e.g. the State Archive of Transcarpathian Oblast). |
| `ehri_list_children(id)` | Descend the tree: a country's repositories, a repository's fonds, a unit's sub-units. `subitems` says whether a hit can be descended further. |
| `ehri_related(id)` | Descriptions linked to a person authority or a subject keyword. |

**Read the description before citing it.** A fond's title is a label, not a summary; the
`scopeAndContent` is where you learn that the collection you assumed was a deportation register
is in fact a property-confiscation series — the kind of error that survives several editions
because the title sounded right.

### tna-discovery — The National Archives (UK)

37M+ catalogue **descriptions** — not scans. Relevant for consular courts, Mandate Palestine,
prisoner-of-war and refugee files, and anything touching British administration.

| Tool | Use |
|---|---|
| `tna_search_records(query, record_series, departments, date_from, date_to, held_by, sort_by, page, page_size)` | Free text with `AND/OR/NOT`, quoted phrases, brackets, `*`. `held_by`: `TNA` (Kew) / `OTH` / `ALL`. |
| `tna_search_series(series:[…], query)` | Series-scoped, returning compact citation rows — each an orderable file reference for the reading room. |
| `tna_get_record(id)` | One catalogue description in full. |

Two rules specific to this server: cite the `reference` (e.g. `FO 841/208/64`) **and** the
`url`, because the reference is what orders the physical file; and **nothing is cached — the
API terms forbid storing responses**, so a call you need twice must be made twice.

---

## D. Vital records & indexes — Hungary, Subcarpathia, and beyond

### jewishgen — Unified Search over all JewishGen databases

| Tool | Use |
|---|---|
| `jewishgen_search(surname, given_name, town, any_field, country, *_match, boolean)` | Returns **hit counts per database plus the result-set URL of each**. Match types: `phonetic` (Beider-Morse, default for surnames/towns), `soundex` (Daitch-Mokotoff, default for given names), `starts_with`, `exact`, `fuzzy`/`fuzzier`/`fuzziest`. `country` also accepts topical collections: `holocaust`, `jowbr`, `yizkor_names`. |
| `jewishgen_search_filtered(filters, result_url \| criteria, max_pages, max_rows)` | **The tool that solves the old problem.** The website's form silently ignores every filter beyond the first surname; this pulls *all* rows and filters client-side on any column: `{"town":"^(Volove\|Ökörmező)","father":"Moshe\|Moses","year":"18[89]\\d"}`. Keys match by substring of the column header, `"*"` matches any column, all filters AND. |
| `jewishgen_open(url)` | Read the rows of any result/detail page + its "next page" link. |
| `jewishgen_options()` | Valid `country` / match-type / data-type values. |
| `jewishgen_raw(url)` | Debug escape hatch: raw HTML when the parser misses a table. |

Notes that matter:
- **Known gap: the overview page's result sets are POST forms, not links.** `jewishgen_search`
  therefore reports a total while listing **no** result sets, and `jewishgen_search_filtered`
  with no `result_url` returns "scanned 1 rows". Do not read that as zero matches. The GET
  workaround, in order:
  1. `jewishgen_raw("https://www.jewishgen.org/databases/jgform.php?SrchBOOL=AND&allcountry=0*&GeoRegion=0*&dates=all&submitform=submitform&srch1v=S&srch1t=E&srch1=<SURNAME>&srch2v=T&srch2t=Q&srch2=<TOWN>")`
     and read the hidden `df` values and the `List N records` button labels out of the HTML.
     (`srch1t`: `Q`=phonetic, `E`=exact, `S`=starts-with.) Then open rows with
     `jgdetail_2.php?df=<UUID>&georegion=0*&srch1=…&srchbool=AND&dates=all&newwindow=0&recstart=0&recjump=0`.
     **`allcountry` is not honoured over GET** — a country-scoped search must go through the POST.
  2. `WebFetch` the same URL — it converts to markdown but **drops hidden inputs**, so it gives
     names and counts, not `df` ids.
  3. Only then the browser.
- **The index's canonical spelling may not be the family's.** In the source project the entire
  Subcarpathian record set is filed under `SZTRULYOVICS`, and searches under the four spellings
  the family actually used returned nothing until that was discovered. When a surname you are
  certain about yields zero, suspect the index's orthography before concluding absence.
- **Coverage reality check:** `jewishgen_options()` is the definitive statement of what exists.
  A phonetic search on a Sephardi surname returns overwhelmingly **Ashkenazi collisions** that
  look like a rich result set and are not. Read the database names before the counts.

### hungaricana — Hungarian archival record databases

**This server changes what used to be a browser-only source.** Metadata search now works
directly; only the page images remain behind reCAPTCHA.

| Tool | Use |
|---|---|
| `hungaricana_search(query, database, page, per_page≤100, sort)` | Full text across archives.hungaricana.hu. Wildcards `*` `?` `!` and `AND/OR`. Each hit carries the database slug + `record_id`, the **Levéltári jelzet** reference code, year, names, every label→value field, and the query highlights. |
| `hungaricana_list_databases(query)` | Without a query: the database catalogue (`Fogoly` = prisoner registers, `Kozjegyzoi` = notarial deeds, `Hagyateki` = probate, `Polgper` = civil suits, `Arvaszeki` = orphans' court, `Bunteto` = criminal). **With a query: per-database hit counts** — run this first to decide where to search. |
| `hungaricana_get_record(database, record_id \| url)` | Full metadata: reference code, archival series, year, every field pair, and the **participants (Résztvevők) with per-person birth place, age, religion and occupation**. |

Notes that matter:
- **Image and PDF download is still behind reCAPTCHA and is not implemented.** Hand the user
  the record `url` for the scan. The metadata alone is often enough to cite, and it is always
  enough to decide whether the scan is worth the user's minute.
- The **orphans' court and probate series are underused**: they name minors, guardians and
  heirs, which is precisely the generation a vital-records index tends to lose.
- The 1921 census sheets remain a separate, image-only path (see `archive-tooling.md`).

### radixindex — Hungarian surname/place meta-index

5.5M records indexed, ~1.06M of them free. It answers a question no other server does:
**which databases and which places record this surname at all** — a cheap way to find the
neighbouring town you did not know to search.

| Tool | Use |
|---|---|
| `radix_search_surname(surname)` | Per-database sections: title + id, the exact spelling recorded there, per-place occurrence counts, and a `listing_url`. **Exact spelling only — no phonetic matching**, so run your variants yourself. `found:false` with `databases:[]` is a genuine zero. |
| `radix_search_place_names(query)` | Resolve a place to RadixIndex slug(s). Diacritics are ignored (`Ökörmező` == `okormezo`); district (`…i járás`) entries are separate slugs. |
| `radix_get_place(place)` | **Every surname recorded for one place, with counts** — the reverse index, and the useful one for mapping a town's Jewish families. |
| `radix_list_records(database_id, surname, listing_url)` | The free per-record index rows. Two layouts: `rows` (name, birth place, other place, period, kind of information, one row per record) and `summary` (per-place counts only). |

Record *detail* behind the listings needs a paid Radix membership. The links come back so the
user can decide to subscribe; do not treat the free index rows as the full record.

### macse — Hungarian Society for Family History meta-index

| Tool | Use |
|---|---|
| `macse_search_surname(surname, given_name, lang)` | Which sections mention a surname, where and how often: civil and church registries, **name changes (névváltoztatás)**, nobles, family trees, family books, gravestones, memorials, tableaux, millers, obituaries. Diacritics are significant (`Kovács` ≠ `Kovacs`); matching is exact per spelling. |
| `macse_search_variants(surnames:[…], given_name, lang)` | Merges spellings into one meta-index view with `hits_by_surname` per row. |

**Coverage is essentially today's post-Trianon Hungary — verified to have no Subcarpathian or
Máramaros hits.** So it is the wrong tool for the home town and the right tool for the
relatives who moved inward: Budapest (indexed by district), Debrecen, Miskolc. The
**name-change section is its quiet speciality** — a Magyarized surname is a documented event
with a date, and that record is how you connect two names that look unrelated.

### familysearch — tree, indexed records, full text

| Tool | Use |
|---|---|
| `fs_search_persons(...)` | The Family Tree, by GEDCOM X terms: given/surname, sex, birth/death/marriage/residence date and place, **father's and mother's names**, spouse, keyword. Dates take a year, a range (`1860-1875`), or formal dates. |
| `fs_search_records(...)` | Indexed historical records ("personas"), same grammar. Uses the website endpoint because the documented platform resource is unavailable; a response-shape change raises an error rather than returning silence. |
| `fs_full_text_search(...)` | **Experimental.** AI-generated transcripts of ~2 billion record images. The endpoint is undocumented and the wrapper is a thin override — it may break, and it needs a valid session token. |
| `fs_get_person(pid)` | One tree person with facts and relationships. |

**Authentication is the whole story here.** Tokens are short-lived (~1 hour), and with none
configured `fs_status` reports `access_token: "missing"` and every call fails. That is a
blocker to hand the user, not a coverage finding. Also: the Family Tree is **user-contributed**
— a tree hit is a lead to verify against a record, never a source in its own right, and it must
never appear in the report at a certainty above `ככל הנראה` on its own authority.

---

## E. Migration, relief and the years in between

### jdc-names — JDC Archives Names Database (568,778 records)

The Joint's own indexes: index cards, client lists, the **transmigration bureau**, remittances,
migration files, individual case files. This is the archive of *survival logistics* — who was
helped, where they were, where they were going, and who they were travelling with — which
makes it one of the few sources that documents the years between liberation and arrival.

| Tool | Use |
|---|---|
| `jdc_search(q, exact, collection, location, ship_name, sort, page, limit)` | `exact=False` (default) is fuzzy and finds spelling variants **and noise** — one documented surname gives 746 fuzzy hits against 2 exact. Each person carries biographical fields and `related_items[]` with `found_in` (**the list to cite**), the JDC emigration office, destination, `accompanied_by`, scans and an Ancestry link. |
| `jdc_search_variants(names:[…], …)` | Deduplicated union by person uuid, with `matched_query` and `per_name_totals`. |
| `jdc_facets(q, …)` | Valid filter values — collection keys (`index_cards`, `list`, `transmigration_bureau`, `remittances`, `migration_files`, `individual_files`), top locations, top ship names. |
| `jdc_get_person(person_id)` | One record with every related archival item. |
| `jdc_download_scans(out_dir, person_id \| urls)` | Downloads the scans **plus a citation sidecar**, re-deriving fresh signed URLs first. |

**Scan URLs expire in about 24 hours.** Never save a scan URL into the report or the sources
index — download the file with `jdc_download_scans` and cite the record. The
`accompanied_by` field is the one people miss: it reconstructs family groups that no vital
record ever recorded together.

---

## F. Press, books and printed sources

### arcanum — ADT press & registry archive (subscription)

Full playbook in **`arcanum-press-archive.md`**. The tool summary:

| Tool | Use |
|---|---|
| `arcanum_search(query, collections, countries, languages, date_from/to, index, sort, per_page)` | `index` selects the field: `TEXT` (default), `TEXT_EXACT`, `TITLE`, `AUTHOR`, `CAPTION`, `FOOTNOTE`, or named entities `PERSON` / `LOCATION` / `ORGANIZATION` / `EVENT`. Hits are **pages within volumes**: `documentId` + 0-based `page`. |
| `arcanum_get_facets(query, facet)` | `COL` = which titles mention it, `EV` = year ranges, plus `LANG`, `COUNTRY`, `KEYW`. **Run this before a sweep.** |
| `arcanum_find_titles(text, country, language, year, type)` | The ~9,000-title catalogue → `collectionId`s. |
| `arcanum_get_collection` / `arcanum_get_document` / `arcanum_search_in_document` | Volumes of a title; volume metadata + contents; every matching page inside one volume with snippets. |
| `arcanum_get_page_text(document_id, page, max_chars)` | **Full OCR transcript of a page.** Read the entry *before* fetching the image. |
| `arcanum_get_page_image(document_id, page)` | Short-lived signed URL for the full-resolution scan. Download immediately. |
| `arcanum_build_search_url(...)` | Compose the results URL without running it — the clean way to give the report a clickable external link. |

`page` is **0-based and physical within the volume**, not the printed page number. Cite both.
Arcanum does **no** phonetic expansion — the spelling matrix is entirely yours.

### internetarchive — archive.org

The secondary-literature layer: yizkor books, town histories, memorial volumes, interwar
directories, gazetteers. Its value is that it can be **searched inside**, so a family name in
a 400-page community history is findable without reading it.

| Tool | Use |
|---|---|
| `ia_search(query, mediatype, language, year_from/to, collection, sort, offset, limit≤500)` | Lucene syntax; a bare term also matches **OCR full text**, so town and family names work directly. Try diacritic **and** plain spellings — OCR is inconsistent. |
| `ia_search_inside(identifier, query, mode, max_matches)` | Page numbers and context snippets inside one item. Two mechanisms: the BookReader full-text API, or a local search of the downloaded OCR text (the result's `mechanism` field says which ran). Zero matches with a mechanism set is a real negative; a raised error is not. |
| `ia_fetch_text(identifier, offset, max_chars≤100000)` | A window of the OCR full text for quoting, by **byte** offset. |
| `ia_get_item(identifier)` | Item metadata, including `has_fulltext`. |

A yizkor book is testimony, not a register: it is edited memory, decades later, by people with
a stake. Quote it as what it is, and never let it outrank a civil record on a date.

---

## G. Regional and Sephardi

### gibraltar — Gibraltar National Archives

Censuses of 1817, 1834, 1868, 1871, 1878, 1881, 1891, 1901, 1911, 1914, plus the 1784 list of
Jews in town and the 1786 orders to leave. Narrow, but for a Sephardi Mediterranean branch it
is one of the very few indexed pre-1850 population sources.

| Tool | Use |
|---|---|
| `gibraltar_search_inhabitants(surname, year, forename)` | One census year's surname register. Partial matches accepted (`Benoliel` also matches `DE MOSES BENOLIEL`). Every row carries a `source_url`. |
| `gibraltar_get_jews_1784()` / `gibraltar_get_orders_to_leave_1786()` | The two named lists. |
| `gibraltar_search_site(query)` | The archive's own site search. |

---

## What still has no server

Check this list against the canaries before planning a browser session — the set shrinks as
servers are added, and the last update moved **Hungaricana metadata** and **Israel State
Archives catalogue search** out of it.

- **Hungaricana page images / PDF download** — reCAPTCHA, user-solved.
- **Camp-museum archives by email** — Stutthof, Auschwitz and others answer direct requests
  with material that is not online at all. Still the richest single channel, still human.
- **KehilaLinks town pages** — often hide a survivor testimony and a local deportation list.
- **Glazer / zchor deportation tables**, USHMM encyclopedia.
- **Arolsen formal tracing request** — Salesforce form, months of wait.
- **Google Pinpoint collections other than the wired one** — see `mcp-israel.md`.

---

## How the MCPs change the method

- **§2 multi-name problem** — the `*_variants` tools do the phonetic bucketing, but the
  **name/spelling matrix is still yours to build**: the servers expand what you give them, they
  do not guess the fourth transliteration nobody tried. Arcanum, RadixIndex and MACSE do no
  phonetic expansion at all, and JewishGen may file the family under an orthography none of its
  members ever used.
- **§3 archive playbook** — the browser is now the exception. The two questions worth asking
  before any sweep are "which server covers this?" and "what does its canary say?".
- **§5 build** — downloads land as real files with citation sidecars, so evidence crops come
  from originals by default. `arcanum_build_search_url`, `citation.url` and record `url` fields
  supply the external half of every dual link.
- **§6 audit** — nothing changes. A structured API returning JSON is *not* verification; the
  fresh-agent audit round still runs, and a health-check failure is itself an audit finding.
