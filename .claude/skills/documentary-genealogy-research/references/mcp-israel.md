# The Israeli half — MCP servers for the post-1948 record

Shoah research pulls hard toward European archives and then stops at liberation. These servers
cover what happened **after**: immigration, absorption, work, marriage, death, burial, and the
survivors' own children — which is also how living relatives are found.

Treat this as one research phase, not an afterthought. In the Shoah project it filled a
twenty-year documentary gap and produced the contacts that no European archive could; in the
Sephardi/Yemenite project it was the spine of the whole report. For the **pre-state** record
classes these same servers reach — consular registers, Montefiore, Ottoman-era IGRA sets,
burial societies — and the Sephardi/Yemenite name problems, read `pre-state-and-diaspora.md`.

**The three highest-yield Israeli sets, by experience:** IGRA **voter rolls** (they carry the
father's name — one 1949 line settled a birth year, a patronymic and a residence at once);
**burial records** (JOWBR, BillionGraves, the Chevra Kadisha by phone — death date to the day and
the father's name on the stone); and **JPress obituaries** (filed as advertisements). Start there.

## Canaries

| Server | Health call | Green looks like |
|---|---|---|
| `igra` | `igra_status` | `Logged in …`, record count + last-update date |
| `nli` | `nli_status(ping=true)` | `api_key: set`, `ping.total` > 0 |
| `archives-gov-il` | `isa_search(query="פנקס בוחרים 1949")` | a non-empty `items` list with facets |
| `pinpoint` | `pinpoint_health` | `ok:true`, collection name + document count |
| `tlvarchive` | `tlv_health` | `ok:true` |
| `infocenters` | `infocenters_status(tenant="gfh")` | `tenant_check.ok:true`, `quick_search:true` |
| `jpress` | `jpress_list_publications(filter="דבר")` | a non-empty list including `dav` |
| `montefiore-census` | `census_list_options(field="birthplaces")` | a non-empty dropdown list |

**Search every name twice: transliterated and in Hebrew.** Across IGRA, NLI, the State
Archives, Tel Aviv and the infocenters tenants, the Hebrew and Latin sides are different
indexes over different material, not transliterations of one another. A name that yields
nothing in one can yield hundreds in the other.

---

## igra — IGRA All Israel Database (~4.04M records, ~390 collections)

| Tool | Use |
|---|---|
| `igra_list_databases(query, category)` | The ~390 collections with counts. Categories worth naming: `Immigration`, `Census/registry`, `Burials`. **Browse this first** — it says which record types even exist for your years. |
| `igra_search(surname, given_name, surname_hebrew, given_name_hebrew, location, year, database, record_type, era, country, repository, phonetic, start, include_details)` | Beider-Morse phonetic by default. `*` wildcard works **only with `phonetic=False`**. Paged 40 at a time (`start=40, 80…`). Filters take exact facet values from a previous search's `facets` block. |
| `igra_get_record(record_id)` | All indexed fields, source note and image links. Accepts the internal id, a base64 `recordID`, or a full share URL. |

Field lessons that cost time to learn:
- **An empty result set comes back as HTTP 500**, reported as "0 results". A genuine outage and
  a genuine zero therefore look identical. Canary first.
- **`database` takes ONE exact facet value.** Comma-separating two names returns 0 with no error.
- **Run the Hebrew index with `phonetic=False`.** Beider-Morse is tuned for Ashkenazi names and
  mangles Arabic-script-derived ones.
- **The `facets` block is the discovery tool, not decoration.** Search a surname with no other
  filter and read the `database:` facet: it lists every collection holding the name, with
  counts. That is how you find the collection you did not know to ask for — in one case a
  1918–19 Jaffa residents register surfaced only as a one-record line in a facet list.
- **When a scan URL 403s, email the archive — and check the source archive.**
  `webmaster@genealogy.org.il` answered a documented request in under 24 hours, attached the
  scan, and confirmed the 403 was a bug that the request itself surfaced. Include the record's
  *Share* link. But when a whole *collection* 403s, remember IGRA mirrors other archives'
  volumes: the same British-subject register that was "blocked" for thirteen editions was open
  online at the Israel State Archives all along.
- **An index row is not a record until the scan is read.** Two false relatives entered one
  project from IGRA index lines ("Rebeca Arwas" was Rebecca Aluf; "Bension Arwas" was Bension
  Amzalak), and a third from a State Archives register whose index number was taken for a form
  number (the form belonged to an English missionary). Field semantics also drift inside one collection — `Country of Origin` carried
  nationality in some rows and birthplace in others. Read the form.
- **Name-change database** (post-1948, ילקוט הפרסומים): turns a family's self-reported change
  into a documented pattern (184 `Ṣāleḥ` records made Ṣāleḥ→Zadok common practice).

## archives-gov-il — Israel State Archives

Catalogue search is **working** (an earlier schema bug that dropped `isa_search` and
`isa_search_advanced` from the tool list was fixed). If those two tools are ever missing from
the list again while the rest of the server loads, that is the same bug returning: report it
rather than engineering around it, because every other tool is addressed **by signature** and
without catalogue search there is no way to obtain one.

| Tool | Use |
|---|---|
| `isa_search(query, method, facets, sortBy, page, pageSize)` | Full-texts titles, descriptions **and indexed person-name lists** — the 1948 Jerusalem census files each carry their full resident roster in the index, so a surname query rains such files. `method`: `allTerms` / `exact` / `someTerms`. Facets include `hasGenealogy:"true"`, `onlineAccess:"true"`, `yearRange`, `locations`, `persons`, `depositors`, `contentTypes`. **The facet block that comes back is a map of the archive around your query** — read it before narrowing. |
| `isa_search_advanced(...)` | Fielded boolean (name / source / date / physicalId). |
| `isa_get_record(signature)` | Full catalogue record by signature (`000zm9w`) or details URL. |
| `isa_list_container(physicalId)` | Every folder in a container (`גל-45494`, `ג-5562`) in original order — how you enumerate all volumes of a register series. |
| `isa_fetch_file` → `isa_search_in_file` → `isa_read_pages` | Download the PDF (often 50–200 MB, cached), **fuzzy-scan the whole file's OCR for names** (it tolerates the stray spaces OCR inserts between Hebrew letters), then read the pages it points at. Never read pages blind. |
| `isa_get_file_url(signature)` | Presigned S3 URL (~1h). `null` ⇒ no online access. |
| `isa_ocr_collections(query, genealogyOnly)` | The full-text-searchable collections hosted on Google Pinpoint, as deep links. |
| `isa_request_viewing_info(signature)` | Identifiers + ordering contact for offline records. |

A quietly excellent corner: **rabbinical-court marriage and divorce documents** are indexed
with structured fields (age, community, father's name, residence) and are full-text searchable.

## pinpoint — the immigrant-lists collection, searched properly

The State Archives' scanned collections live on Google Pinpoint, which has no public API. This
server wires one collection directly: **רשימות עולים ומסמכי הגירה** — immigrant and ma'apilim
lists 1919–1975, passports and immigration documents, ~7,800 documents / ~135,000 pages.

| Tool | Use |
|---|---|
| `pinpoint_search(query, collection, page)` | Full text over the OCR of scanned documents, typed **and handwritten**, in Hebrew/English/Polish/German. Quoted phrases work (`"Taub, Szaja"`). Up to 100 docs per page. |
| `pinpoint_locate_mentions(query, doc_id, snippet)` | The exact **page** inside a document where a hit occurs, plus a fractional bounding box and the page image URL. |
| `pinpoint_page_text(doc_id, start_page, end_page≤+20, include_lines)` | The OCR text layer of a page range, in reading order (RTL-safe). `include_lines` gives per-line pixel positions, which is how you match a bounding box to its surrounding lines. |
| `pinpoint_download_page(doc_id, page_number, out_dir)` | One page as PNG **with a citation sidecar**. Pages are 0-based. |
| `pinpoint_collection_info` / `pinpoint_facets` | What the collection is and how it is labelled. |

**Spelling is whatever the OCR produced**, and handwriting OCR is noisy. Always sweep several
variants, and treat the text layer as a finding aid: verify the detail against the page image
before citing it. The 800px render the server can fetch is often too coarse for a dense
handwritten column — cross-check against `pinpoint_page_text` word boxes, and if the detail
still will not resolve, say so and grade it rather than guessing at a letter.

## nli — National Library of Israel catalogue

| Tool | Use |
|---|---|
| `nli_search(query, title, creator, subject, exact, language, start_date, end_date, criteria, material_type, availability_type, page, page_size≤50)` | Free text over any field; Hebrew works. `material_type`: books, journals, images, audio_video, maps, **archives**, manuscripts, NEWSPAPER… `availability_type=online_and_api_access` for fully digitised items. |
| `nli_get_record(record_id)` | Every Dublin Core field, the permalink, and — for digitised records — thumbnails, downloads and the **IIIF manifest** (`https://iiif.nli.org.il/IIIFv21/<recordid>/manifest`) whose canvases hold the page images. |
| `nli_search_rai(query, rai_only)` | Israel Archive Network (רשת הארכיונים בישראל) material — records from partner archives, ids beginning `NNL_ARCHIVE`. Local and institutional archives (a school, a moshava, a workers' council) that hold exactly the everyday paper a family leaves behind. |

Two collections worth knowing by name because they are fully scanned and person-level: the
**1934 Mandatory Palestine telephone book**, and the Palestine-era directories. A subscriber
line is a dated address, which is often the missing link between an immigration record and a
death notice.

Photographs: the Israel Archive Network surfaces **local archives' photo collections** (a
kibbutz archive held eleven family photographs), served at storage resolution through
`iiif.nli.org.il` with no impersonation needed. The API's single `date` field can contradict the
item page's date *range* — cite the range. Exclude a same-name performer's `material_type` before
sweeping (140 of 141 hits for one name were a singer's recordings). Grade a photograph in three
layers — metadata, visual content, who is depicted — and claim the third only when the catalogue
names them.

## jpress — Historical Jewish Press (Hebrew/Yiddish/Ladino, 1783–today)

| Tool | Use |
|---|---|
| `jpress_search(query, publications, date_from/to, type, fields, sort)` | `type=ADVERTISEMENT` is the one to remember: **obituaries and memorial notices (מודעות אבל) are filed as advertisements, not articles.** Codes: `dav`=דבר, `mar`=מעריב, `hrz`=הארץ, `ahr`=על המשמר, `hzf`=הצפה, `lmr`=למרחב, `hbk`=הבקר, `hzh`=הצופה. |
| `jpress_list_publications(filter)` | The full publication-code list. |
| `jpress_get_article(id)` | Full OCR text + metadata, **plus prev/next section ids on the same page** — walk them to read a whole obituary column. |
| `jpress_get_issue(document_id)` | Table of contents of one issue. |
| `jpress_fetch_raw(url)` | Escape hatch through the Cloudflare-cleared browser. |

Hebrew OCR of old newsprint is noisy: try spellings with and without ו/י, and expect
letter-confusions (ם/ס, ן/ז). Quote phrases for exact matches. **Plene and defective spellings
of a given name return different families** (`אהרן` vs `אהרון`) — run both, always. An OCR
transcript is a lower evidentiary tier than the downloaded page image: save the whole issue
(the user's browser downloads it; the API is behind reCAPTCHA), and cite the image. A transcript
alone once gave a review the wrong publication year; the neighbouring issues reversed it.
Rapid request bursts trip Cloudflare — item by item, with delays. **When a block clears, re-run
the canary and compare counts**: a canary meant only to prove the server answered truthfully
returned 84 for «אהרן צדוק» where edition 60 had logged 66; all 84 were checked against the
corpus's item ids — 18 a known Ladino-press collision, about thirty a same-name singer, about
fifteen already held, and four new, one of them extending the subject's press record fourteen
years forward and another six years later than anything held. A changed count is a lead to
read, not a find.

**The Cloudflare failure, and why it stops everything.** NLI's JPress sits behind a Cloudflare
interstitial. When the server's browser profile has not cleared it, **every** tool — including
`jpress_fetch_raw`, documented as the escape hatch — fails with `Cloudflare challenge not
cleared`. Retrying does not help; nor does driving the user's own Chrome to the same URL. There
is no automated way around it and **you must not try to defeat bot detection.** The one fix is
the user's: `npm run login` in the server's profile directory, or a `cf_clearance` cookie via
`JPRESS_COOKIE`. Ask early — JPress is often the only source that can date a death from a
contemporary מודעת אבל, so a blocked JPress silently converts a resolvable question into an
unverified grade.

## tlvarchive and infocenters — municipal and institutional archives

Both wrap the `infocenters.co.il` platform. `tlvarchive` is the richer, dedicated client for
the Tel Aviv–Yafo municipal archive; `infocenters` reaches the other tenants.

| Tool | Use |
|---|---|
| `tlv_search(query, sort, page, page_size)` | Free text over the whole Tel Aviv archive. **Query in Hebrew** — the catalogue is Hebrew and the site stems words. Each hit carries `item_number`, list-view fields, the attached file path when one is shown, and a stable `record_url`. |
| `tlv_es_search` / `tlv_get_item` | Elasticsearch-side search; one item in full. |
| `tlv_download_file(path, out_dir)` | Download an attached document **with a citation sidecar**. |
| `infocenters_search(tenant, query, sort, page)` | The same over another tenant. Verified: `gfh` (**Ghetto Fighters' House** — Holocaust testimonies, photographs and documents, including Hungarian and Carpathian material), `massuah`, `jabotinsky`, `tel_share`. Any other `infocenters.co.il/<site>` slug can be tried. |
| `infocenters_list_tenants()` / `infocenters_get_item(book_id)` | The registry; one record. |

**Ghetto Fighters' House is the one to remember from this pair** — it is a Holocaust archive in
its own right, with material that is not in Yad Vashem, and it indexes in Hebrew. Search both
scripts (`Rappaport` and `רפפורט`, `אוקרמזו` and `מרמרוש`).

## montefiore-census — Montefiore censuses of Eretz Israel (1839–1875)

Only relevant for families with a pre-Zionist Palestine branch, but decisive when it is.
`census_search` returns families with head, spouse, children, ages, **birthplace and year of
arrival**, occupation and economic status; `census_get_record(id, year)` gives one record.
Dropdown fields (`residence`, `kolel`, `country`, `birthplace`, `institutionType`) must match
site values exactly — get them from `census_list_options(field, filter)`. `language='H'` to
search Hebrew.

**Its birthplace field is searchable and IGRA's is not**, which is reason enough to run both
even when IGRA seems to cover the period. The **scans carry patronymics the index omits**, and
Hebrew-only spellings (`ארואץ`, not `Arruas`). When the server's canary is red: the site's
search is `POST` and wants a browser UA + Referer, while its PDFs reject a spoofed UA — what
was logged as a 403 wall for a round was neither.
