# Splitting the work across models — which agent gets which brain

This research has phases with genuinely different demands. Transcribing a two-hour testimony
in chunks is mechanical and enormous. Sweeping twenty archives is enormous and needs
persistence, not brilliance. Deciding whether a document actually says what the report claims
it says is small, hard, and the whole point. Running all three on the same model is either
wasteful or reckless, depending on which model you picked.

Sub-agents take a `model` override, so the split is available. What follows is how to use it
without losing the quality the method exists to protect.

---

## The split

| Phase | Model | Why |
|---|---|---|
| Audio chunking, transcription, format conversion, file counts, thumbnail generation | **cheapest tier** (Haiku / DeepSeek Flash) | Mechanical, well-defined, high volume. No judgement involved. |
| Archive sweeps over MCP servers; pulling and filtering result sets; downloading originals | **mid tier** (Sonnet / DeepSeek V4) | Token-hungry and repetitive. Needs accuracy and stamina, not insight. |
| Testimony analysis — contradictions, corroborations, what to chase | **top tier** | This is interpretation, and its errors propagate into every later chapter. |
| Evidence audit — does the source say what the report says it says? | **top tier** (or the highest available) | The highest-value finding class in the whole method. |
| Delivery audit — RTL, print, mobile, search, contrast | **top tier with vision** | It must *look* at screenshots, not only measure them. |
| The orchestrator: grading certainty, deciding the next action, writing the report | **top tier** | A single early mis-grade compounds through every subsequent edition. |

Rule of thumb: **delegate by how expensive the mistake is, not by how long the task takes.**
A four-hour transcription that comes back slightly wrong costs one re-run. A certainty grade
that comes back slightly wrong ships, gets cited, and survives seven editions.

---

## The thing that actually breaks: sub-agents have no context

A sub-agent does not inherit the conversation. It gets a prompt and returns text. Everything
you know and did not write down is invisible to it — and the lighter the model, the less it
fills the gap and the more it simply stops.

Observed, in this environment: a Haiku sub-agent was given a path in the cloud container and
replied *"the folder is not currently accessible — connect it in Cowork on your device"*. It
had confused its own filesystem with the device bridge and abandoned a task that had no
obstacle at all. The identical task, prefixed with "this is your own cloud workspace
filesystem, NOT a remote device — use the Bash tool", returned the right answer in one call.

So, for every delegated task:

- **State the environment.** Which filesystem, which tools, whether the device bridge is
  involved. The cheap tiers guess wrong and give up rather than probe.
- **State the output format explicitly.** Do not rely on judgement about what "report back"
  means. In a `Workflow`, pass a `schema` and get a validated object instead.
- **Paste the context it needs.** This is what the ledger is for: a `THREADS.md` entry — or a
  shape-B target row with its journal entry — is written to be actionable by someone who was
  not there, so it pastes straight into a sub-agent brief. That is not a coincidence — it is the reason for the format.
- **Say what "nothing found" looks like.** Otherwise a blocked server, an empty archive and a
  confused agent all come back as the same shrug, and the difference is the whole finding.

## MCP servers are reachable from sub-agents

Verified in this environment: a Sonnet sub-agent loaded two schemas with one `ToolSearch` call
and ran both canaries (`degob_status`, `radix_status`) successfully. So archive sweeps can be
pushed down a tier without losing tool access.

Two caveats to put in the brief:

- **Tell it to batch `ToolSearch`.** A sub-agent that does not know the rule will load schemas
  one at a time and burn its budget on round-trips.
- **Tell it to run the canary first**, and to report a red canary as a blocker rather than as
  an empty result. This is the single most important instruction in an archive-sweep brief:
  without it, a Cloudflare wall becomes a false negative finding in the report.
- Interactively-authenticated servers may be absent in headless or scheduled runs. If a sweep
  is scheduled rather than interactive, verify reachability in the first call rather than
  assuming it.

---

## Brief templates

### Transcription / mechanical (cheapest tier)

> You are working inside a Linux cloud container — your own filesystem, reached with the Bash
> tool. Not a remote device, nothing to connect.
> Task: `<exact command or operation>`.
> Return exactly: `<numbered output format>`. No commentary, no analysis.

### Archive sweep (mid tier)

> You are sweeping one archive for a family-history research project. Do not interpret, do not
> conclude — collect and report.
> **Subject:** `<name, dates, places, all known spellings>`.
> **Server:** `<name>`. Load its schemas with ONE batched `ToolSearch` call
> (`select:tool1,tool2,…`), never one per tool.
> **First, run `<canary tool>`.** If it fails, stop and report the failure verbatim as a
> blocker — do not proceed and do not report "no results".
> **Then:** `<the searches, spelling by spelling; prefer the *_variants tool where one exists>`.
> Download originals with `<download tool>` into `<dir>` — keep the citation sidecars.
> **Return:** for each search, the exact query, the hit count, and the rows. An empty result is
> reported as "0 hits for `<exact query>` in `<exact index and coverage>`" — never as "nothing
> found". Do not deduplicate contradictory records.

### Evidence audit (top tier)

Use the prompt in `audit-checklist.md`. Add: *re-read the sources themselves, not the report's
description of them.* The finding class this audit exists for is a claim that drifted from what
its cited document actually shows, and it is invisible to anyone who only reads the report.

### Delivery audit (top tier, vision)

Use the delivery prompt in `audit-checklist.md`. It must **read the screenshots**, not just
measure the DOM — RTL defects are frequently invisible in the markup and obvious on screen.

---

## Running the method on non-Claude models

The split matters more, not less. Two adjustments:

- **The context ceiling decides the orchestrator.** The report alone runs to tens of thousands
  of tokens, and an audit round reads the report, the sources index and the built page
  together. A 256K-context model cannot hold an audit round on a mature project; put the
  1M-context model in the orchestrator seat and delegate outward.
- **Vision may not be in the same model.** Where the top-tier model has no image input, the
  scan-reading and the delivery audit have to be routed to whichever model does — and that
  agent needs the fullest brief of all, because it is judging something it cannot ask you about.
- **RTL and Hebrew output quality is the unverified risk.** Before committing a model to the
  writing seat, give it one real paragraph to produce: a Hungarian quotation with its Hebrew
  translation, a date range, and an archive reference code. Then render it and look at it.
  The five bidi failure modes in `build-pipeline.md` are ones a Hebrew-fluent model already
  makes; a model with thin Hebrew exposure makes them harder and more silently.

---

## What never gets delegated

- **The certainty grade.** Whatever a sub-agent returns is evidence for a grade, not a grade.
- **The decision that a thread is closed.** A sub-agent reports what it found; the orchestrator
  decides whether that settles the question.
- **Anything irreversible or public** — publishing, spending, writing to a third party. Those
  need the user, not a cheaper model.
