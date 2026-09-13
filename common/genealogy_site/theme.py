# -*- coding: utf-8 -*-
"""The shared visual skeleton. One layout for every report; one accent each."""


def css(pal):
    return f"""
:root {{
  --ink:{pal.ink}; --muted:{pal.muted}; --line:{pal.line};
  --paper:{pal.paper}; --accent:{pal.accent}; --accent-soft:{pal.accent_soft};
  --link:{pal.link};
  --hero-from:{pal.hero_from}; --hero-to:{pal.hero_to};
  --col: 60rem;               /* the reading column */
  --nav-h: 3.25rem;
  --anchor-off: 6.5rem;
  --radius: 6px;
  --serif: 'David Libre','Frank Ruhl Libre','Times New Roman',Georgia,serif;
  --sans: 'Assistant','Segoe UI',Arial,Helvetica,sans-serif;
  --sbw: 0px;
}}
*,*::before,*::after {{ box-sizing:border-box; }}
html {{ scroll-behavior:smooth; }}
@media (prefers-reduced-motion:reduce) {{ html {{ scroll-behavior:auto; }} }}
body {{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:var(--serif); font-size:1.0625rem; line-height:1.75;
  text-rendering:optimizeLegibility; -webkit-text-size-adjust:100%;
  overflow-wrap:break-word; word-break:normal;
}}
img, svg, video {{ max-width:100%; }}

/* ---------- hero ---------- */
.hero {{
  background:linear-gradient(135deg,var(--hero-from),var(--hero-to));
  color:#f6efe2; padding:2.5rem 1.25rem 2rem;
}}
.hero-in {{ max-width:var(--col); margin-inline:auto; }}
.hero .crumb {{ font-family:var(--sans); font-size:.8rem; opacity:.8; margin-block-end:1rem; }}
.hero .crumb a {{ color:#f2e5c8; text-decoration:none; border-block-end:1px solid rgba(242,229,200,.4); }}
.hero h1 {{ font-size:clamp(1.6rem,3.4vw,2.4rem); line-height:1.25; margin:0 0 .5rem; font-weight:700; letter-spacing:-.01em; }}
.hero .subject {{ font-size:1.05rem; opacity:.94; margin:0 0 .35rem; }}
.hero .meta {{ font-family:var(--sans); font-size:.8rem; color:#e8dcc2; }}

.spine {{ display:flex; flex-wrap:wrap; gap:.5rem; margin-block-start:1.5rem; }}
.spine div {{
  background:rgba(255,255,255,.09); border:1px solid rgba(255,255,255,.16);
  border-radius:var(--radius); padding:.5rem .8rem; min-width:7.5rem;
}}
.spine b {{ display:block; font-size:1.3rem; line-height:1.2; font-family:var(--sans); font-weight:700; }}
.spine span {{ /* floor: no supporting text below 12.5px */ font-family:var(--sans); font-size:.78rem; color:#e8dcc2; }}

/* ---------- sticky navigation ---------- */
.nav {{
  position:sticky; top:0; z-index:40; background:rgba(250,247,242,.97);
  backdrop-filter:saturate(150%) blur(6px);
  border-block-end:1px solid var(--line); font-family:var(--sans);
}}
.nav-in {{ max-width:var(--col); margin-inline:auto; padding:0 1.25rem; }}
.nav-row {{ display:flex; align-items:center; gap:.4rem; height:var(--nav-h); }}
/* only the chapter strip scrolls; the first row must not clip the search panel */
.nav-row.chapters {{ overflow-x:auto; scrollbar-width:thin; }}
.nav-row:first-child {{ flex-wrap:wrap; height:auto; padding-block:.4rem; }}
.chapters-wrap {{ border-block-start:1px dotted var(--line); }}
.chapters-wrap > summary {{
  list-style:none; cursor:pointer; padding:.3rem 0; font-size:.78rem; color:var(--muted);
}}
.chapters-wrap > summary::-webkit-details-marker {{ display:none; }}
.chapters-wrap > summary::after {{ content:" ▾"; }}
.chapters-wrap[open] > summary::after {{ content:" ▴"; }}
.nav-row.chapters {{ height:2.4rem; }}
/* the row scrolls horizontally; a fade at the overflowing edge is the only cue */
.chapters-wrap {{ position:relative; }}
.chapters-wrap::after {{
  /* at rest the strip is scrolled to its start, so the hidden chips are at the
     inline-END edge — that is where the cue belongs */
  content:""; position:absolute; inset-block:auto 0; inset-inline-end:0;
  block-size:2.4rem; inline-size:2.2rem; pointer-events:none;
  background:linear-gradient(to left, rgba(250,247,242,0), rgba(250,247,242,.98));
}}
[dir="rtl"] .chapters-wrap::after {{
  background:linear-gradient(to right, rgba(250,247,242,0), rgba(250,247,242,.98));
}}
.chapters-wrap:not([open])::after {{ display:none; }}
.nav a {{
  flex:0 0 auto; color:var(--ink); text-decoration:none; font-size:.82rem;
  padding:.3rem .6rem; border-radius:999px; white-space:nowrap;
}}
.nav a:hover {{ background:rgba(0,0,0,.05); }}
.nav a.on {{ background:var(--accent); color:#fff; }}
.nav .lbl {{ flex:0 0 auto; font-size:.78rem; color:var(--muted); padding-inline-end:.2rem; }}
.nav-row.chapters a:not(.on) {{ font-size:.78rem; color:var(--muted); }}
.nav-row.chapters a.on {{ font-size:.78rem; }}

.qwrap {{ position:relative; flex:0 0 auto; margin-inline-start:auto; }}
#q {{
  font-family:var(--sans); font-size:.8rem;
  padding:.32rem .7rem; border:1px solid var(--line); border-radius:999px;
  background:#fff; color:var(--ink); min-width:9rem;
}}
#q:focus-visible {{ outline:2px solid var(--link); outline-offset:1px; }}
/* out of flow: opening the list must not change the nav's height, or every
   anchor below it would shift while the reader is looking at one */
#qres {{
  position:absolute; inset-block-start:calc(100% + .4rem); inset-inline-end:0;
  min-width:20rem; max-width:min(28rem, 92vw); max-height:60vh; overflow-y:auto;
  background:var(--paper); border:1px solid var(--line); border-radius:var(--radius);
  box-shadow:0 6px 20px rgba(0,0,0,.14); padding:.35rem .8rem .5rem;
  font-family:var(--sans); font-size:.82rem; z-index:60;
}}
#qres[hidden] {{ display:none; }}
#qres a {{
  display:block; white-space:normal; flex:initial; border-radius:0;
  padding:.35rem 0; color:var(--ink); border-block-end:1px dotted var(--line);
}}
#qres a:last-child {{ border-block-end:0; }}
#qres .k {{ color:var(--muted); font-size:.78rem; margin-inline-start:.4rem; }}
#qres .nores {{ margin:.3rem 0; color:var(--muted); }}
#qres .qcount {{
  margin:.1rem 0 .35rem; color:var(--muted); font-size:.78rem;
  border-block-end:1px solid var(--line); padding-block-end:.3rem;
}}

/* ---------- the reading column ---------- */
main {{ max-width:var(--col); margin-inline:auto; padding:1.5rem 1.25rem 4rem; }}
section, .legacy-anchor {{ scroll-margin-top:var(--anchor-off); display:block; }}
.legacy-anchor {{ height:0; }}
h2, h3, h4 {{ scroll-margin-top:var(--anchor-off); }}
h2 {{
  font-size:1.45rem; line-height:1.3; margin:2.6rem 0 .9rem; color:var(--accent);
  border-block-end:2px solid var(--line); padding-block-end:.35rem;
}}
h3 {{ font-size:1.13rem; margin:1.8rem 0 .55rem; color:var(--accent); }}
h4 {{ font-size:1rem; margin:1.3rem 0 .4rem; color:var(--ink); }}
p {{ margin:0 0 1rem; }}
a {{ color:var(--link); text-decoration:none; border-block-end:1px solid rgba(0,0,0,.14); }}
/* a citation marker after a Latin run would otherwise be laid out on the far
   side of it, before the very words it cites */
a.cit {{ unicode-bidi:isolate; }}
.visually-hidden {{
  position:absolute; width:1px; height:1px; margin:-1px; padding:0;
  overflow:hidden; clip:rect(0 0 0 0); clip-path:inset(50%); white-space:nowrap; border:0;
}}
a:hover {{ border-block-end-color:var(--link); }}
a:focus-visible {{ outline:2px solid var(--link); outline-offset:2px; border-radius:2px; }}
ul, ol {{ margin:0 0 1rem; padding-inline-start:1.4rem; }}
li {{ margin-block-end:.4rem; }}
hr {{ border:0; border-block-start:1px solid var(--line); margin:2.5rem 0; }}
strong {{ font-weight:700; }}
blockquote {{
  margin:1.2rem 0; padding:.1rem 1rem; border-inline-start:3px solid var(--line);
  color:var(--muted);
}}
code {{
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:.9em;
  background:rgba(0,0,0,.045); padding:.1em .35em; border-radius:3px;
  direction:ltr; unicode-bidi:isolate;
}}

/* ---------- callouts ---------- */
.lede {{
  background:#fff; border:1px solid var(--line); border-inline-start:4px solid var(--accent);
  border-radius:var(--radius); padding:1.1rem 1.2rem; margin:0 0 1.6rem;
  font-size:1.08rem; line-height:1.72;
}}
.note {{
  background:rgba(0,0,0,.025); border:1px solid var(--line); border-radius:var(--radius);
  padding:.8rem 1rem; margin:1.2rem 0; font-size:.94rem; color:var(--muted);
}}

/* ---------- the certainty ladder, spelled out ---------- */
.ladder {{
  border:1px solid var(--line); border-radius:var(--radius); background:#fff;
  margin:0 0 1.6rem; font-family:var(--sans); font-size:.84rem;
}}
.ladder > summary {{
  cursor:pointer; padding:.5rem .9rem; color:var(--muted); list-style:none;
}}
.ladder > summary::-webkit-details-marker {{ display:none; }}
.ladder > summary::after {{ content:" ▾"; }}
.ladder[open] > summary::after {{ content:" ▴"; }}
.ladder > summary:hover {{ color:var(--ink); }}
.ladder-in {{ padding:.2rem .9rem .9rem; }}
.rungs {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(15rem,1fr)); gap:.4rem .9rem; }}
.rung {{ display:flex; gap:.5rem; align-items:baseline; line-height:1.5; }}
.rung > span {{ color:var(--muted); }}
.terms {{
  margin-block-start:.8rem; padding-block-start:.7rem; border-block-start:1px dotted var(--line);
  display:grid; grid-template-columns:repeat(auto-fit,minmax(17rem,1fr)); gap:.4rem .9rem;
}}
.term {{ line-height:1.5; }}
.term b {{ color:var(--ink); }}
.term span {{ color:var(--muted); }}
.term b::after {{ content:" — "; color:var(--muted); font-weight:400; }}

/* ---------- certainty chips ---------- */
.rank {{
  display:inline-block; font-family:var(--sans); font-size:.78rem; font-style:normal; font-weight:600;
  line-height:1.5; padding:.05rem .5rem; border-radius:999px; white-space:nowrap;
  border:1px solid currentColor; vertical-align:.08em;
}}
.rank.v1 {{ color:#2f6b41; background:rgba(47,107,65,.08); }}   /* מאומת */
.rank.v2 {{ color:#6b5324; background:rgba(107,83,36,.08); }}   /* כמעט ודאי */
.rank.v3 {{ color:#8a5a00; background:rgba(138,90,0,.08); }}    /* ככל הנראה */
.rank.v4 {{ color:#8a3d2e; background:rgba(138,61,46,.08); }}   /* טעון אימות */
.rank.v5 {{ color:#5a5a5a; background:rgba(90,90,90,.10); }}   /* נשלל */
.rank.v6 {{ color:#7a7a7a; background:rgba(122,122,122,.08); }}   /* בוטל */

/* ---------- the story page ---------- */
/* A second page over the same research: the life in order, for a reader who
   arrived without context. Everything auditable stays in the report. */
body.story main {{ padding-block-start:2rem; }}
.story-hero .hero-cols {{ display:flex; gap:1.5rem; align-items:flex-start; }}
.story-hero .hero-text {{ flex:1 1 auto; min-width:0; }}
.story-hero .portrait {{
  flex:0 0 auto; inline-size:9.5rem; margin:0; text-align:start;
}}
.story-hero .portrait img {{
  inline-size:100%; max-block-size:13rem; object-fit:cover; object-position:center top;
  border:1px solid rgba(255,255,255,.35); border-radius:var(--radius);
  box-shadow:0 3px 12px rgba(0,0,0,.28); background:#fff;
}}
.story-hero .portrait figcaption {{
  color:#e8dcc2; font-family:var(--sans); font-size:.76rem; line-height:1.5;
  margin-block-start:.4rem; text-align:start;
}}
.story-hero h1 {{ margin-block-end:.6rem; }}
.story-hero .subject {{ font-size:1.1rem; line-height:1.6; }}

.nav-report {{
  margin-inline-start:auto; font-weight:600;
  color:var(--accent) !important; border:1px solid var(--accent);
}}
.nav-report:hover {{ background:var(--accent); color:#fff !important; }}

/* three columns: certain · probable · open — the whole state of the research */
.verdicts {{
  display:grid; grid-template-columns:repeat(auto-fit,minmax(14rem,1fr));
  gap:.9rem; margin:1.8rem 0 2.4rem;
}}
.verdict {{
  background:#fff; border:1px solid var(--line); border-radius:var(--radius);
  padding:.9rem 1rem 1rem;
}}
.verdict h3 {{
  margin:0 0 .6rem; font-size:1rem; color:var(--ink);
  display:flex; align-items:center; gap:.5rem; flex-wrap:wrap;
}}
.verdict ul {{ margin:0; padding-inline-start:1.1rem; font-size:.95rem; }}
.verdict li {{ margin-block-end:.5rem; line-height:1.6; }}
.verdict a, .openq a {{
  font-family:var(--sans); font-size:.78rem; border:0; white-space:nowrap;
  color:var(--link); opacity:.85;
}}
.verdict a::after, .openq a::after {{ content:" ←"; }}

/* the timeline: the date is the handle the eye scans down */
.timeline {{ list-style:none; margin:1.2rem 0 2rem; padding:0; position:relative; }}
.timeline::before {{
  /* the rail runs through the dots, which sit in the gap between the date
     column and the text — i.e. at the INLINE-START side in an RTL page */
  content:""; position:absolute; inset-block:.6rem 1.4rem;
  inset-inline-start:calc(5.325rem - 1px); inset-inline-end:auto;
  inline-size:2px; background:var(--line);
}}
li.tl {{
  display:flex; gap:1.1rem; margin:0 0 1.15rem; position:relative;
  align-items:flex-start;
}}
.tl-when {{
  flex:0 0 4.5rem; text-align:end; padding-block-start:.15rem;
  font-family:var(--sans); position:relative;
}}
.tl-when::after {{
  /* the node on the rail */
  content:""; position:absolute; inset-block-start:.55rem; inset-inline-end:-1.1rem;
  inline-size:.55rem; block-size:.55rem; border-radius:50%;
  background:var(--paper); border:2px solid var(--accent-soft);
}}
.tl-when b {{ display:block; font-size:.92rem; color:var(--accent); line-height:1.4; }}
.tl-place {{ display:block; font-size:.76rem; color:var(--muted); line-height:1.4; }}
.tl-what {{ flex:1 1 auto; min-width:0; padding-inline-start:.5rem; }}
.tl-what p {{ margin:0 0 .3rem; }}
.tl-foot {{
  display:flex; gap:.6rem; align-items:center; flex-wrap:wrap;
  font-family:var(--sans); font-size:.78rem;
}}
.tl-more a {{ border:0; font-family:var(--sans); font-size:.78rem; }}
.rank-plain {{ font-family:var(--sans); font-size:.78rem; color:var(--muted); }}

/* key documents as cards: picture, date, what it proves, how sure */
.doccards {{
  display:grid; grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));
  gap:1rem; margin:1.2rem 0 2rem;
}}
.doccard {{
  margin:0; background:#fff; border:1px solid var(--line); border-radius:var(--radius);
  overflow:hidden; display:flex; flex-direction:column; text-align:start;
}}
.doccard .doc-img {{ display:block; border:0; line-height:0; background:#f3efe6; }}
.doccard img {{
  inline-size:100%; block-size:9.5rem; object-fit:cover; object-position:center top;
  border:0; border-radius:0; box-shadow:none; display:block;
}}
.doccard figcaption {{
  padding:.7rem .85rem .8rem; font-size:.88rem; color:var(--ink);
  text-align:start; margin:0; display:flex; flex-direction:column; gap:.25rem;
  flex:1 1 auto;
}}
.doc-when {{ font-family:var(--sans); font-size:.78rem; color:var(--muted); }}
.doccard b {{ font-size:.95rem; line-height:1.45; }}
.doc-proves {{ color:var(--muted); font-size:.86rem; line-height:1.55; flex:1 1 auto; }}
.doc-foot {{
  display:flex; gap:.6rem; align-items:center; flex-wrap:wrap;
  margin-block-start:.35rem; font-family:var(--sans); font-size:.78rem;
}}
.doc-foot a {{ border:0; }}

.openq {{ margin:1.1rem 0 1.8rem; padding-inline-start:1.2rem; }}
.openq li {{ margin-block-end:.55rem; }}
.report-cta {{ margin:2rem 0 1rem; }}
.btn.big {{
  font-size:.95rem; padding:.6rem 1.4rem; background:var(--accent); color:#fff;
  border-color:var(--accent);
}}
.btn.big:hover {{ background:var(--hero-from); border-color:var(--hero-from); }}

/* ---------- tables ---------- */
.tablewrap:focus-visible, .tree-embed:focus-visible {{ outline:2px solid var(--link); outline-offset:2px; }}
.tablewrap {{ overflow-x:auto; margin:1.2rem 0; border:1px solid var(--line); border-radius:var(--radius); background:#fff; }}
table {{ border-collapse:collapse; width:100%; font-size:.93rem; }}
th, td {{ padding:.5rem .7rem; border-block-end:1px solid var(--line); text-align:start; vertical-align:top; }}
thead th {{ background:rgba(0,0,0,.035); font-family:var(--sans); font-size:.82rem; }}
tbody tr:last-child td {{ border-block-end:0; }}

/* ---------- figures ---------- */
figure {{ margin:1.6rem auto; text-align:center; max-width:100%; }}
figure img {{
  max-width:100%; height:auto; border:1px solid var(--line); border-radius:var(--radius);
  box-shadow:0 2px 8px rgba(0,0,0,.07); background:#fff;
}}
figcaption {{ font-size:.84rem; color:var(--muted); margin-block-start:.5rem; line-height:1.6; text-align:start; }}
figcaption .fignum {{ font-family:var(--sans); font-weight:700; color:var(--accent); }}
figcaption .figlinks {{ display:block; margin-block-start:.3rem; font-family:var(--sans); font-size:.78rem; }}
.imgcap {{ display:block; font-size:.84rem; color:var(--muted); margin-block-start:.4rem; }}

.ext {{ font-size:.78rem; color:var(--muted); padding-inline-start:.12em; }}
.doclink {{ display:inline-block; min-inline-size:1.5rem; min-block-size:1.5rem; padding:.15rem .2rem; }}

/* ---------- gallery ---------- */
.gallery {{ display:flex; flex-wrap:wrap; gap:.75rem; margin:1.2rem 0 2rem; }}
.gallery a {{
  flex:0 0 auto; width:11rem; border:0; text-align:center; color:var(--muted);
  font-family:var(--sans); font-size:.78rem; line-height:1.4;
}}
.gallery img {{ width:100%; height:8rem; object-fit:cover; border:1px solid var(--line); border-radius:var(--radius); background:#fff; }}
/* a crop far wider than the frame is shown whole rather than magnified */
.gallery img.contain {{ object-fit:contain; padding:.3rem; }}
/* a line strip (wider than 6:1) is a hairline inside a square tile: it takes
   the whole row and keeps its own proportions, so the writing can be read */
.gallery a.wide {{ width:100%; }}
.gallery a.wide img {{ height:auto; max-block-size:11rem; object-fit:contain; }}
.gallery span {{ display:block; margin-block-start:.3rem; }}

/* ---------- family tree ---------- */
.tree-embed {{
  overflow-x:auto; border:1px solid var(--line); border-radius:var(--radius);
  background:#fff; padding:.5rem;
}}
/* zoom 1 == fit to width: the diagram is never wider than the frame unless the
   reader asks for it, on a phone as on a desktop */
.tree-embed svg {{
  width:calc(100% * var(--tree-zoom, 1));
  min-width:min(100%, calc(75rem * var(--tree-zoom, 1)));
  /* the global svg max-width would clamp the zoom away */
  max-width:none;
  height:auto; display:block; margin-inline:auto;
}}
.tree-zoom {{
  display:flex; gap:.4rem; align-items:center; justify-content:flex-end;
  font-family:var(--sans); font-size:.78rem; color:var(--muted); margin-block-start:.5rem;
}}
.tree-zoom button {{
  font:inherit; line-height:1; min-inline-size:2rem; min-block-size:2rem;
  border:1px solid var(--line); border-radius:var(--radius); background:#fff;
  color:var(--ink); cursor:pointer;
}}
.tree-zoom button:hover {{ background:rgba(0,0,0,.04); }}
.tree-zoom button:focus-visible {{ outline:2px solid var(--link); outline-offset:1px; }}
.legend {{
  display:flex; gap:1.1rem; justify-content:center; flex-wrap:wrap;
  padding:.7rem 0 .2rem; font-family:var(--sans); font-size:.8rem; color:var(--muted);
}}
.legend > span {{ display:flex; align-items:center; gap:.35rem; }}
.dot {{ width:.7rem; height:.7rem; border-radius:50%; display:inline-block; flex:0 0 auto; }}
.tree-foot {{
  font-family:var(--sans); font-size:.78rem; color:var(--muted); text-align:center;
  max-width:52rem; margin:.5rem auto 0; line-height:1.6;
}}
.tree-hint {{ font-family:var(--sans); font-size:.78rem; color:var(--muted); margin-block-start:.4rem; }}
.btn {{
  display:inline-block; font-family:var(--sans); font-size:.82rem; border:1px solid var(--accent);
  color:var(--accent); border-radius:999px; padding:.32rem .9rem; margin-block-start:.6rem;
}}
.btn:hover {{ background:var(--accent); color:#fff; }}

/* ---------- person index ---------- */
.people {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(15rem,1fr)); gap:.6rem; margin:1.2rem 0; }}
.person {{
  background:#fff; border:1px solid var(--line); border-radius:var(--radius);
  padding:.6rem .75rem; font-size:.9rem;
}}
.person b {{ display:block; font-size:.97rem; }}
.person .d {{ font-family:var(--sans); font-size:.78rem; color:var(--muted); }}
.person .r {{ display:block; color:var(--muted); font-size:.84rem; margin-block-start:.15rem; }}

.skip {{
  position:absolute; inset-inline-start:-9999px; inset-block-start:0; z-index:99;
  background:var(--paper); color:var(--link); padding:.6rem 1rem;
  border:1px solid var(--accent); border-end-end-radius:var(--radius);
  font-family:var(--sans); font-size:.85rem;
}}
.skip:focus {{ inset-inline-start:0; }}

/* ---------- back to top ---------- */
.top {{
  /* the inline-end edge: in RTL that is the ragged end of the lines, so the
     button never covers the start of a sentence */
  position:fixed; inset-block-end:1.1rem; inset-inline-end:1.1rem; z-index:50;
  width:2.5rem; height:2.5rem; border-radius:50%; border:1px solid var(--line);
  background:#fff; color:var(--accent); display:grid; place-items:center;
  font-size:1.1rem; box-shadow:0 2px 8px rgba(0,0,0,.12); opacity:0; pointer-events:none;
  transition:opacity .2s;
}}
.top.show {{ opacity:1; pointer-events:auto; }}

footer {{
  max-width:var(--col); margin-inline:auto; padding:1.5rem 1.25rem 3rem;
  border-block-start:1px solid var(--line); color:var(--muted);
  font-family:var(--sans); font-size:.8rem;
}}

/* ---------- mobile ---------- */
.qtoggle {{
  display:none; font:inherit; font-size:.82rem; line-height:1; cursor:pointer;
  padding:.35rem .7rem; min-block-size:1.9rem; margin-inline-start:auto;
  border:1px solid var(--line); border-radius:999px; background:#fff; color:var(--ink);
}}
.qtoggle:focus-visible {{ outline:2px solid var(--link); outline-offset:1px; }}

@media (max-width:40rem) {{
  :root {{ --anchor-off: 7rem; --tree-zoom: 1; }}
  body {{ font-size:1rem; overflow-wrap:anywhere; }}
  bdi {{ overflow-wrap:anywhere; }}
  .hero {{ padding:1.75rem 1rem 1.5rem; }}
  main {{ padding:1.25rem 1rem 3rem; }}
  .nav-in {{ padding:0 1rem; }}
  .nav-row {{ height:2.4rem; }}
  /* one scrolling row instead of three wrapped ones: the sticky bar cost a
     quarter of the screen and no link is lost by scrolling it */
  .nav-row:first-child {{
    flex-wrap:nowrap; height:2.4rem; padding-block:0;
    overflow-x:auto; overflow-y:hidden; scrollbar-width:none;
  }}
  .nav-row:first-child::-webkit-scrollbar {{ display:none; }}
  .chapters-wrap > summary {{ padding:.05rem 0; font-size:.72rem; line-height:1.4; }}
  .nav-row.chapters {{ height:2.2rem; }}
  .qtoggle {{ display:block; flex:0 0 auto; position:sticky; inset-inline-end:0;
             box-shadow:-6px 0 8px rgba(250,247,242,.97); }}
  .qwrap {{ display:none; }}
  /* while searching, the row IS the search: the links step aside for it, and
     nothing clips the results panel */
  .nav.qopen .nav-row:first-child {{ overflow:visible; }}
  .nav.qopen .nav-row:first-child > a,
  .nav.qopen .nav-row:first-child > .lbl {{ display:none; }}
  .nav.qopen .qwrap {{ display:block; flex:1 1 auto; margin:0; min-width:0; }}
  #q {{ width:100%; min-width:0; }}
  #qres {{ min-width:0; max-width:none; inline-size:100%; max-height:50vh; }}
  main {{ padding-block-end:4.5rem; }}   /* clearance for the floating button */
  td, th {{ overflow-wrap:break-word; }}
  .tree-embed {{ max-block-size:70vh; overflow-y:auto; }}
  .spine {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(8.5rem,1fr)); }}
  /* an odd last tile would otherwise sit alone at half width */
  .spine div:last-child:nth-child(odd) {{ grid-column:1/-1; }}
  .spine div {{ min-width:0; padding:.45rem .6rem; }}
  .spine b {{ font-size:1.1rem; }}
  .gallery a {{ width:8.5rem; }}
  .gallery img {{ height:6rem; }}
  /* the story page on a phone: the portrait sits beside the title rather than
     costing a screen of its own */
  .story-hero .hero-cols {{ gap:1rem; }}
  .story-hero .portrait {{ inline-size:6.5rem; }}
  .story-hero .portrait figcaption {{ display:none; }}
  .story-hero .subject {{ font-size:.98rem; }}
  .timeline::before {{ inset-inline-start:calc(4.425rem - 1px); }}
  .tl-when {{ flex-basis:3.6rem; }}
  .tl-when b {{ font-size:.85rem; }}
  li.tl {{ gap:.9rem; }}
  .doccards {{ grid-template-columns:1fr 1fr; gap:.7rem; }}
  .doccard img {{ block-size:7rem; }}
  .doccard figcaption {{ padding:.55rem .6rem .65rem; font-size:.84rem; }}
  .verdicts {{ gap:.7rem; margin-block:1.2rem 1.8rem; }}
  .rungs, .terms {{ grid-template-columns:1fr; }}
  /* the link to the full report is the one thing that must never scroll out
     of the phone's navigation row */
  .nav-report {{
    position:sticky; inset-inline-end:0; background:var(--paper);
    box-shadow:6px 0 8px rgba(250,247,242,.97);
  }}
  .top {{ width:2.2rem; height:2.2rem; inset-block-end:.7rem; inset-inline-end:.7rem; font-size:.95rem; }}
}}

/* ---------- print ---------- */
@media print {{
  @page {{ size:A4; margin:16mm 14mm; }}
  @page landscape {{ size:A4 landscape; }}
  body {{ background:#fff; font-size:10.5pt; line-height:1.5; }}
  .nav, .top, #qres, .tree-hint, .btn, .hero .crumb, .prov, .tree-zoom, .skip {{ display:none !important; }}
  /* a collapsed block prints as its summary alone; the script opens every
     <details> for the print run, and this is the belt to that pair of braces */
  .ladder > summary {{ font-weight:700; color:#000; }}
  details:not([open]) > *:not(summary) {{ display:block !important; }}
  .story-hero .portrait img {{ border:1px solid #bbb; box-shadow:none; }}
  .story-hero .portrait figcaption {{ color:#444; }}
  .verdict, .doccard {{ border:1px solid #bbb; break-inside:avoid; }}
  li.tl {{ break-inside:avoid; }}
  .doccards {{ grid-template-columns:1fr 1fr; }}
  .report-cta {{ display:none !important; }}
  .hero {{ background:#fff !important; color:#000; padding:0 0 1rem; border-block-end:2px solid #000; }}
  .hero .meta, .spine span {{ color:#444; }}
  .spine div {{ border:1px solid #bbb; background:#fff; }}
  .spine b {{ color:#000; }}
  main, footer, .hero-in {{ max-width:none; }}
  h2 {{ break-after:avoid; }}
  figure, .tablewrap, .person {{ break-inside:avoid; }}
  figure img {{ max-height:150mm; box-shadow:none; }}
  #tree {{ break-before:page; page:landscape; }}
  #tree .tree-embed {{ overflow:visible; border:0; break-inside:avoid; }}
  /* the diagram is near-square: fitting the width alone spills it over two
     pages, so the height of a landscape A4 is the binding constraint */
  .tree-embed svg {{
    min-width:0; width:auto; height:auto; max-width:100%; max-height:118mm;
    display:block; margin-inline:auto;
  }}
  #tree h2 {{ break-after:avoid; }}
  .tree-foot, .legend {{ font-size:7pt; line-height:1.35; }}
  /* overflow-x has no meaning on paper: a scrolling table would simply lose
     its last column */
  .tablewrap {{ overflow:visible; }}
  .tablewrap table {{ table-layout:fixed; width:100%; }}
  .tablewrap td, .tablewrap th {{ overflow-wrap:anywhere; }}
  a {{ border-block-end:0; color:#000; }}
  /* the external address is what a paper reader cannot otherwise recover;
     a relative path would only repeat the file name the link already shows */
  #index a[href^="http"]::after, #report a[href^="http"]::after,
  #changelog a[href^="http"]::after {{
    content:" ‹" attr(href) "›"; font-size:8pt; color:#555; word-break:break-all;
  }}
}}
"""
