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
.spine span {{ font-family:var(--sans); font-size:.72rem; color:#e8dcc2; }}

/* ---------- sticky navigation ---------- */
.nav {{
  position:sticky; top:0; z-index:40; background:rgba(250,247,242,.97);
  backdrop-filter:saturate(150%) blur(6px);
  border-block-end:1px solid var(--line); font-family:var(--sans);
}}
.nav-in {{ max-width:var(--col); margin-inline:auto; padding:0 1.25rem; }}
.nav-row {{ display:flex; align-items:center; gap:.4rem; height:var(--nav-h); overflow-x:auto; scrollbar-width:thin; }}
.chapters-wrap {{ border-block-start:1px dotted var(--line); }}
.chapters-wrap > summary {{
  list-style:none; cursor:pointer; padding:.3rem 0; font-size:.72rem; color:var(--muted);
}}
.chapters-wrap > summary::-webkit-details-marker {{ display:none; }}
.chapters-wrap > summary::after {{ content:" ▾"; }}
.chapters-wrap[open] > summary::after {{ content:" ▴"; }}
.nav-row.chapters {{ height:2.4rem; }}
.nav a {{
  flex:0 0 auto; color:var(--ink); text-decoration:none; font-size:.82rem;
  padding:.3rem .6rem; border-radius:999px; white-space:nowrap;
}}
.nav a:hover {{ background:rgba(0,0,0,.05); }}
.nav a.on {{ background:var(--accent); color:#fff; }}
.nav .lbl {{ flex:0 0 auto; font-size:.72rem; color:var(--muted); padding-inline-end:.2rem; }}
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
  position:absolute; inset-block-start:calc(100%% + .4rem); inset-inline-start:0;
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
#qres .k {{ color:var(--muted); font-size:.72rem; margin-inline-start:.4rem; }}
#qres .nores {{ margin:.3rem 0; color:var(--muted); }}

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

/* ---------- certainty chips ---------- */
.rank {{
  display:inline-block; font-family:var(--sans); font-size:.72rem; font-style:normal; font-weight:600;
  line-height:1.5; padding:.05rem .5rem; border-radius:999px; white-space:nowrap;
  border:1px solid currentColor; vertical-align:.08em;
}}
.rank.v1 {{ color:#2f6b41; background:rgba(47,107,65,.08); }}   /* מאומת */
.rank.v2 {{ color:#6b5324; background:rgba(107,83,36,.08); }}   /* כמעט ודאי */
.rank.v3 {{ color:#8a5a00; background:rgba(138,90,0,.08); }}    /* ככל הנראה */
.rank.v4 {{ color:#8a3d2e; background:rgba(138,61,46,.08); }}   /* טעון אימות */

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

.ext {{ font-size:.78em; color:var(--muted); padding-inline-start:.12em; }}

/* ---------- gallery ---------- */
.gallery {{ display:flex; flex-wrap:wrap; gap:.75rem; margin:1.2rem 0 2rem; }}
.gallery a {{
  flex:0 0 auto; width:11rem; border:0; text-align:center; color:var(--muted);
  font-family:var(--sans); font-size:.72rem; line-height:1.4;
}}
.gallery img {{ width:100%; height:8rem; object-fit:cover; border:1px solid var(--line); border-radius:var(--radius); background:#fff; }}
/* a crop far wider than the frame is shown whole rather than magnified */
.gallery img.contain {{ object-fit:contain; padding:.3rem; }}
.gallery span {{ display:block; margin-block-start:.3rem; }}

/* ---------- family tree ---------- */
.tree-embed {{
  overflow-x:auto; border:1px solid var(--line); border-radius:var(--radius);
  background:#fff; padding:.5rem;
}}
.tree-embed svg {{ min-width:56rem; height:auto; display:block; margin-inline:auto; }}
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
.person .d {{ font-family:var(--sans); font-size:.75rem; color:var(--muted); }}
.person .r {{ display:block; color:var(--muted); font-size:.84rem; margin-block-start:.15rem; }}

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
@media (max-width:40rem) {{
  :root {{ --anchor-off: 12rem; }}
  body {{ font-size:1rem; overflow-wrap:anywhere; }}
  bdi {{ overflow-wrap:anywhere; }}
  .hero {{ padding:1.75rem 1rem 1.5rem; }}
  main {{ padding:1.25rem 1rem 3rem; }}
  .nav-in {{ padding:0 1rem; }}
  .nav-row {{ height:2.9rem; }}
  .qwrap {{ order:99; margin:0 0 .5rem; width:100%; }}
  #q {{ width:100%; min-width:0; }}
  #qres {{ min-width:0; max-width:none; inline-size:100%; max-height:50vh; }}
  main {{ padding-block-end:4.5rem; }}   /* clearance for the floating button */
  td, th {{ overflow-wrap:break-word; }}
  .nav-row:first-child {{ flex-wrap:wrap; height:auto; padding-block:.5rem 0; overflow:visible; }}
  .nav-row:first-child > a, .nav-row:first-child > .lbl {{ margin-block-end:.35rem; }}
  .spine {{ display:grid; grid-template-columns:1fr 1fr; }}
  .spine div {{ min-width:0; padding:.45rem .6rem; }}
  .spine b {{ font-size:1.1rem; }}
  .gallery a {{ width:8.5rem; }}
  .gallery img {{ height:6rem; }}
  .top {{ width:2.2rem; height:2.2rem; inset-block-end:.7rem; inset-inline-end:.7rem; font-size:.95rem; }}
}}

/* ---------- print ---------- */
@media print {{
  @page {{ size:A4; margin:16mm 14mm; }}
  @page landscape {{ size:A4 landscape; }}
  body {{ background:#fff; font-size:10.5pt; line-height:1.5; }}
  .nav, .top, #qres, .tree-hint, .btn, .hero .crumb, .prov {{ display:none !important; }}
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
