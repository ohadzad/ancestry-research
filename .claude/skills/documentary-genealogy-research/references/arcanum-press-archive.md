# Arcanum / ADT (adt.arcanum.com) — the subscription press & registry archive

**The primary press source for anything in the historic Kingdom of Hungary** — which
covers Subcarpathia/Carpatho-Ruthenia, Transylvania, Slovakia, Vojvodina, Burgenland and
Hungary proper. Arcanum Digitheca (ADT) holds tens of millions of OCR-searchable pages of
newspapers, official gazettes, yearbooks and registries from the 18th century onward.

Vital records tell you when a person was born, married, and died. **Arcanum tells you what
their life looked like**: property, business, litigation, community standing, death
notices — and the bureaucratic paper-trail of persecution. Use it to corroborate, to enrich,
and to break ties that vital records leave open.

---

## Use the `arcanum` MCP server when it is installed

`arcanum_account_status` confirms the subscription is live. Then the whole flow below has a
structured equivalent, and it is strictly better: `arcanum_find_titles` → collection ids ·
`arcanum_get_facets(query, 'COL'|'EV')` → which titles and years actually mention the family
(run this per spelling variant *before* any sweep; it is cheap) · `arcanum_search` → page hits
as `documentId` + 0-based `page` · `arcanum_search_in_document` → locate the article inside a
known volume · `arcanum_get_page_text` → the **full OCR transcript**, read it before spending
anything · `arcanum_get_page_image` → a short-lived signed URL for the full-resolution scan
(download and stage it immediately) · `arcanum_build_search_url` → the clickable external link
for the report's dual sourcing.

What does **not** change: the paid subscription and its cancellation reminder; **one active
device per account** (browsing the site at the same time can block page access for a few
minutes); the spelling-variant discipline; and citing both the physical page index and the
printed page number. What the server does not do: **no phonetic expansion at all** — every
variant is a separate query, always.

The browser recipes below remain the fallback when no server is installed.

---

## Subscription (ask about this at intake)

Full-page **viewing and downloading requires a paid personal subscription**. Without one you
get search hits and short OCR snippets — enough to *locate* a page, never to read or archive
it. At intake ask whether the user has an active ADT subscription; if the project needs press
sources and they don't, say so plainly: a one-month personal subscription unlocks full-page
downloads and is usually enough for a focused family project.

**Lifecycle discipline — do not skip.** The subscription auto-renews. As soon as the press
sweep is planned, set a cancellation reminder (calendar event **and** a scheduled task) and
add it to the project's open-actions list with its date. Finish the sweep inside that window.

**Session**: work in the **user's own browser**, where the subscription cookie lives. Verify
by loading any collection page and checking the account chip in the header. Don't try to
fetch subscriber pages from the sandbox — they come back paywalled.

---

## URL patterns (build them directly; far faster than clicking)

- **Collection browse** — `https://adt.arcanum.com/hu/collection/<CollectionId>/`
  (the browse URL is also how you *discover* a collection's exact ID)
- **Collection-scoped full-text search** — the results URL carries a base64 JSON payload:
  ```python
  import base64, json, urllib.parse
  q   = json.dumps({"filters": {"COL": ["<CollectionId>"]}, "query": "<term>"})
  url = ("https://adt.arcanum.com/hu/search/results/?list="
         + urllib.parse.quote(base64.b64encode(q.encode()).decode()))
  ```
  In-page JS equivalent:
  ```js
  btoa(unescape(encodeURIComponent(JSON.stringify({filters:{COL:['<Col>']}, query:'<term>'}))))
  ```
  Global (all collections): same shape with `"filters": {}`.
- **Page view** — `https://adt.arcanum.com/hu/view/<CollectionId>_<Year>/?query=<term>&pg=<n>&layout=s`
  `pg` is the **physical page index inside the volume**, not the printed page number; the
  printed number appears on the scan itself. Cite both.

---

## Triage a query across variants without leaving the page

Run in-page on an `adt.arcanum.com` tab so the subscription cookie rides along:

```js
window.__hits = async (col, terms) => {
  const out = [];
  for (const q of terms) {
    const j = JSON.stringify({filters:{COL:[col]}, query:q});
    const u = 'https://adt.arcanum.com/hu/search/results/?list='
            + encodeURIComponent(btoa(unescape(encodeURIComponent(j))));
    const t = (await (await fetch(u,{credentials:'include'})).text())
                .replace(/<[^>]+>/g,' ').replace(/\s+/g,' ');
    const n = (t.match(/([\d,]+)\s+találat/)||[])[1] || '0';   // "N results"
    out.push(q + ' -> ' + n);
  }
  return out.join(' | ').replace(/[?=&;]/g,' ');   // MUST sanitize (see below)
};
await window.__hits('BunugyiKorozesekLapja', ['Rappaport','Rapaport','Rapoport']);
```

- To harvest the hit rows and their targets, split the fetched HTML on result blocks and
  regex `href="(\/hu\/view\/[^"]+)"` — each carries the `&pg=` you need.
- **Output sanitizer is mandatory**: the JS tool blocks any result containing `?`, `=`, `&`
  or `;`. End every return with `.replace(/[?=&;]/g,' ')` (or `'§'` if you must keep shape).
- Inside a function you must `return`; only top level has REPL semantics.

---

## Read the page before you spend a download

Open the page view and extract the page text — ADT serves the **full OCR transcript**
alongside the scan. This is how you confirm a hit and read a dense registry column *before*
downloading. In the source project the entire wanted-notice (occupation, spouse, parents'
names and that they were deceased, case number, court, date) was read this way first.

---

## Download the original page (subscriber)

1. Open the page view (`?pg=N&layout=s`).
2. Click the **⤓** download icon in the viewer toolbar → the `Oldalak mentése`
   ("save pages") dialog.
3. From/to default to the current page; **max 50 pages** per request — keep it to the one
   page you actually need.
4. Click **MENTÉS**. The PDF lands in the user's `~/Downloads` as
   `<Collection>_<year>…__pagesN-N.pdf`.
5. Stage it into the project as `docs/arcanum_full/<descriptive_canonical_name>.pdf` and
   record the citation: title, issue date, issue number, printed page.

No CAPTCHA here (unlike Hungaricana) — once subscribed it is a single click, so you can
download a page per claim rather than rationing.

---

## Crop the evidence from the downloaded PDF

```python
import pymupdf as fitz
from PIL import Image
page = fitz.open('docs/arcanum_full/<file>.pdf')[0]
page.search_for('Rapaport')            # locate -> rects
pix = page.get_pixmap(matrix=fitz.Matrix(3,3), clip=fitz.Rect(x0, y0, x1, y1))
Image.frombytes('RGB', (pix.width, pix.height), pix.samples).save('docs/evidence/..._zoom.png')
```

- Stack the **masthead/date line** and the **column header** above the entry so the crop is
  self-evidencing, then link it to the full PDF.
- OCR quirk: some pages render with spaced-out letters and `search_for` misses. Fall back to
  `page.get_text('words')` coordinates, or derive a fixed clip rect from a half-scale
  thumbnail render you eyeball first.

---

## Spelling discipline — this is where hits are won and lost

Period orthography plus OCR means one family appears many ways. Search **every** variant,
separately, per collection:

- Surname variants — `Rappaport` / `Rapaport` / `Rapoport` / `Rappoport`. In the source
  project the decisive 1944 wanted-notice surfaced **only** under the single-p `Rapaport`,
  after the double-p spelling had been searched and declared empty.
- Magyarized given names — `Májer`/`Mór`/`Meir`, `Lipót`, `Aladár`, `Dezső`, `Ferencz`.
- The town in Hungarian **and its inflections** — Hungarian suffixes change the searchable
  string: `Ökörmező`, `Ökörmezőn`, `ökörmezői` return different result sets. Search all three.
- Firm and estate names, not just people.

---

## High-value collections

| Collection | ID | What it yields |
|---|---|---|
| **Bűnügyi Körözések Lapja** (police wanted bulletin, 1923–1950) | `BunugyiKorozesekLapja` ✅ | The densest genealogical source in the whole archive. A *körözés* notice gives DOB **and** birthplace, languages, religion, marital status **plus spouse's name**, occupation, **both parents' names and whether they were deceased**, case number, issuing court and date. Mass-issued against Jews in 1944 — often the last official trace of a person. |
| **Compass yearbooks** (Magyar / Pénzügyi / Nagy Magyar Compass) | `MagyarCompass` ✅ · `MagyarPenzugyiCompass` ✅ | Annual company entries: directors, supervisory boards, capital, workforce, sites. Track a relative's career year by year and pin down which firm/bank they ran. |
| **Gazdacímtár** / landowner & holdings registries (1893, 1897, 1899–1900, 1911, 1925, 1935) | discover from browse URL | Owner, village, holding size in **cadastral hold**, land-use split. Traces property across decades — and its division after death ("heirs of X"). |
| **Budapesti Közlöny** (official gazette) | discover from browse URL | Auctions, bankruptcies, company registrations, name changes, naturalizations. |
| **Központi Értesítő** (company-register gazette) | discover from browse URL | Company foundations with **full founding board lists** — places a relative in a firm on a dated record. |
| **Dailies & community press** (Budapesti Hírlap, Magyar Ujság, Egyenlőség, Görög Katholikus Szemle …) | per-title, from browse URL | Obituaries, local controversies, community lists. *Egyenlőség* (Jewish weekly) is especially good for community life and family notices. |

✅ = ID confirmed in practice; the rest: read the ID off `/hu/collection/<ID>/`.

**Unit note**: registries measure in *hold*. The **cadastral hold** = 1,600 négyszögöl ≈ 5,755 m²
≈ 5.75 dunam (the older Hungarian hold ≈ 4,316 m²). Registry tables usually say which —
check the table header (`Kataszteri holdakban`) before converting, and state the conversion
basis in the report.

---

## What Arcanum is *not*

Not a vital-records archive — births, marriages and deaths come from JewishGen/DAZO and the
state archives. Don't try to force it to answer "when was she born"; ask it "what did this
family own, run, get sued over, and get hunted by".
