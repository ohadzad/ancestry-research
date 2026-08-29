# -*- coding: utf-8 -*-
"""The build: one function that turns a ProjectConfig into a finished page."""
import datetime
import os
import re

from . import bidi, figures, mdpipe, qa, shell, site, tree


def _stamp(tz='Asia/Jerusalem'):
    """The build time in the project's own zone, without touching the process."""
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo(tz)).strftime('%d.%m.%Y, %H:%M')
    except Exception:                               # pragma: no cover
        return datetime.datetime.now().strftime('%d.%m.%Y, %H:%M')


_ED = re.compile(r'מהדורה\s+(\d+)')


def _edition(text):
    n = [int(m.group(1)) for m in _ED.finditer(text)]
    return f'מהדורה {max(n)}' if n else ''


def _section(sid, title, body, rule=True):
    if not body:
        return ''
    hr = '<hr>' if rule else ''
    head = f'<h2>{title}</h2>' if title else ''
    return f'{hr}<section id="{sid}">{head}{body}</section>'


def build(cfg, verbose=True):
    warnings = []

    def warn(x):
        warnings.append(str(x))

    report_md = open(cfg.p(cfg.report_md), encoding='utf-8').read()
    sources_md = open(cfg.p(cfg.sources_md), encoding='utf-8').read()
    changelog_md = ''
    if cfg.changelog_md:
        if os.path.exists(cfg.p(cfg.changelog_md)):
            changelog_md = open(cfg.p(cfg.changelog_md), encoding='utf-8').read()
        else:
            warn(f'יומן המהדורות שהוצהר אינו קיים: {cfg.changelog_md}')

    edition = _edition(changelog_md or report_md)

    # ---- report body ------------------------------------------------------
    rep = mdpipe.to_html(report_md, cfg.md_extensions)
    rep = mdpipe.markdown_images_to_figures(rep, cfg.root)
    rep = mdpipe.apply_transforms(rep, tuple(cfg.text_transforms) + tuple(cfg.report_transforms))
    for anchor, key in cfg.figure_anchors:
        html_fig = cfg.figures.get(key)
        if not html_fig:
            warn(f'אין תצלום למפתח {key}')
            continue
        rep = figures.inject_after(rep, anchor, html_fig,
                                   on_missing=lambda a: warn(f'עוגן תצלום לא נמצא: {a[:48]}'))
    ids = set()
    rep, chapters_raw, orphan = mdpipe.anchor_headings(rep, cfg.legacy_anchors, ids)
    for o in orphan:
        warn(f'עוגן ישן שלא נמצא לו פרק: #{o}')

    # ---- sources ----------------------------------------------------------
    src = mdpipe.to_html(sources_md, cfg.md_extensions)
    src = mdpipe.apply_transforms(src, tuple(cfg.text_transforms) + tuple(cfg.sources_transforms))
    src, _, _ = mdpipe.anchor_headings(src, seen=ids)
    src = re.sub(r'<h1>(.*?)</h1>', r'<h3>\1</h3>', src, flags=re.S)

    # ---- changelog --------------------------------------------------------
    log = ''
    if changelog_md:
        log = mdpipe.to_html(changelog_md, cfg.md_extensions)
        log = re.sub(r'<h1>(.*?)</h1>', '', log, flags=re.S)
        log, _, _ = mdpipe.anchor_headings(log, seen=ids)

    # ---- tree / gallery / people -----------------------------------------
    svg, legend, foot = tree.load(cfg, warn)
    tree_html = tree.embed(cfg, svg, legend, foot)
    gal = figures.gallery(cfg.gallery, cfg.root)

    present = {'report'}
    prov = (f'<p class="note prov">{cfg.provenance_note}</p>' if cfg.provenance_note else '')
    body = [_section('report', '', prov + rep, rule=False)]
    if tree_html:
        present.add('tree')
        body.append(_section('tree', 'עץ המשפחה', tree_html))
    if gal:
        present.add('gallery')
        body.append(_section(
            'gallery', 'מסמכי מפתח',
            '<p class="note">המסמכים שעליהם נשען עיקר הדוח, בסדר שבו הם נדונים בו. '
            'לחיצה פותחת את הסריקה המלאה.</p>' + gal))
    people = shell.people_section(cfg)
    if people:
        present.add('people')
        body.append(people)
    if src:
        present.add('index')
        body.append(_section('index', 'אינדקס המקורות', src))
    if log:
        present.add('changelog')
        body.append(_section('changelog', 'יומן המהדורות', log))

    body_html = ''.join(body)
    body_html, n_figs = mdpipe.number_figures(body_html)
    body_html = mdpipe.rank_chips(body_html)
    body_html = mdpipe.wrap_tables(body_html)
    body_html = mdpipe.mark_external(body_html)

    chapters = [(sid, mdpipe.toc_label(full, overrides=cfg.toc_overrides), full)
                for sid, full in chapters_raw]
    out = shell.page(cfg, edition, _stamp(), body_html, chapters, present)
    out = bidi.fix_document(out, cfg.extra_bidi_rules)

    open(cfg.p(cfg.main_html), 'w', encoding='utf-8').write(out)
    open(cfg.p('index.html'), 'w', encoding='utf-8').write(
        shell.index_stub(cfg.main_html, cfg.title))

    # ---- gates ------------------------------------------------------------
    problems = qa.run_all(out, cfg.root, cfg.privacy_text_patterns)
    files = [cfg.main_html, 'index.html', cfg.report_md, cfg.sources_md]
    if cfg.changelog_md:
        files.append(cfg.changelog_md)
    files += list(cfg.site_extra_files)
    swept = site.sweep_thumbs(cfg, out)
    site.mirror(cfg, files)
    problems += qa.local_links_exist(out, cfg.p('site'), 'ב-site/: ')

    if verbose:
        print(f'{cfg.slug}: {edition} · {len(out) // 1024} KB · {n_figs} איורים · '
              f'{len(chapters)} פרקים · {len(cfg.people)} אנשים באינדקס')
        if swept:
            print(f'  ממוזערות ישנות שנמחקו: {len(swept)}')
        for w in warnings:
            print('  אזהרה:', w)
        if problems:
            print(f'  ליקויי בקרה ({len(problems)}):')
            for p in problems[:40]:
                print('   -', p)
        else:
            print('  בקרה: נקי')
    if cfg.qa_strict and problems:
        raise SystemExit(f'{cfg.slug}: הבנייה נעצרה — {len(problems)} ליקויי בקרה')
    return out, problems
