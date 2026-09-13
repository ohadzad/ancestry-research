# -*- coding: utf-8 -*-
"""The build: one function that turns a ProjectConfig into a finished page."""
import datetime
import os
import re

from . import bidi, figures, mdpipe, qa, shell, site, tree


def _stamp(tz='Asia/Jerusalem'):
    """The build date in the project's own zone, without touching the process.

    The date alone: a clock stamp from another zone crosses midnight and then
    contradicts the changelog entry written the same evening.
    """
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo(tz)).strftime('%d.%m.%Y')
    except Exception:                               # pragma: no cover
        return datetime.datetime.now().strftime('%d.%m.%Y')


_ED = re.compile(r'מהדורה\s+(\d+)')
_ED_HEAD = re.compile(r'^#{1,3}\s*מהדורה\s+(\d+)\s*·\s*([\d.]+)', re.M)


def _edition(text):
    n = [int(m.group(1)) for m in _ED.finditer(text)]
    return f'מהדורה {max(n)}' if n else ''


def _updated_line(changelog_md, stamp):
    """"Last updated" for the story page's hero.

    A reader judges a research page by how current it is (TR-12); an edition
    number alone says nothing to someone who has never seen the previous one.
    """
    heads = [(int(m.group(1)), m.group(2)) for m in _ED_HEAD.finditer(changelog_md or '')]
    if not heads:
        return f'עודכן {stamp}'
    n, date = max(heads)
    return f'עודכן {date} · מהדורה {n}'


def _count_editions(changelog_md):
    return len(set(m.group(1) for m in _ED_HEAD.finditer(changelog_md or ''))) or 0


def _section(sid, title, body, rule=True):
    if not body:
        return ''
    hr = '<hr>' if rule else ''
    head = f'<h2>{title}</h2>' if title else ''
    return f'{hr}<section id="{sid}">{head}{body}</section>'


def _story(cfg, tree_html, updated, warn):
    """Render the reader-facing page from the project's ``Story`` declaration."""
    st = cfg.story
    report = cfg.main_html

    def card_thumb(path):
        if not os.path.exists(cfg.p(path)):
            warn(f'תצלום לכרטיס מסמך אינו קיים: {path}')
            return ''
        return figures.thumb(cfg.root, path, width=440, quality=72)

    def deep(href):
        """A '#anchor' on the story page means 'that place in the report'."""
        return report + href if href.startswith('#') else href

    st = _resolve_hrefs(st, deep)
    if st.portrait:
        from dataclasses import replace
        st = replace(st, portrait=card_thumb(st.portrait) or st.portrait)
    # only the rungs this page actually uses
    used = {v.rank for v in st.verdicts} | {b.rank for b in st.timeline} \
        | {d.rank for d in st.docs}
    present, body = set(), []
    body.append(f'<section id="lede"><div class="lede">{st.lede}</div>'
                f'{shell.verdicts_block(st)}'
                f'{shell.ladder_legend(cfg, rungs=used)}</section>')
    if tree_html:
        present.add('tree')
        body.append(_section('tree', 'עץ המשפחה', tree_html))
    tl = shell.timeline_block(st)
    if tl:
        present.add('timeline')
        body.append(_section('timeline', 'ציר הזמן', tl))
    dc = shell.docs_block(cfg, st, card_thumb)
    if dc:
        present.add('docs')
        body.append(_section('docs', 'המסמכים', dc))
    present.add('sources')
    body.append(_section(
        'sources', 'המקורות',
        shell.sources_block(st, report, 'הדוח המלא — כל הראיות, המקורות והדרך אליהם')))

    html = shell.story_page(cfg, st, updated, report, ''.join(body), present)
    html = mdpipe.wrap_tables(html)
    html = mdpipe.mark_external(html)
    return bidi.fix_document(html, cfg.extra_bidi_rules)


def _deep_src(src, deep):
    return (src[0], deep(src[1]) if src[1] else '') if src else ()


def _resolve_hrefs(st, deep):
    """Rewrite every in-story '#anchor' into a link to that anchor in the report."""
    from dataclasses import replace
    return replace(
        st,
        verdicts=tuple(replace(v, lines=tuple((t, deep(h) if h else '') for t, h in v.lines))
                       for v in st.verdicts),
        timeline=tuple(replace(b, href=deep(b.href) if b.href else '',
                               src=_deep_src(b.src, deep)) for b in st.timeline),
        docs=tuple(replace(d, href=deep(d.href) if d.href else '',
                           src=_deep_src(d.src, deep)) for d in st.docs),
        sources=tuple((label, deep(h) if h else '') for label, h in st.sources),
    )


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
    # the engine wraps the index in its own <h2>; its headings live under it
    src = mdpipe.demote_headings(src, by=1)
    src = re.sub(r'<h1>(.*?)</h1>', r'<h3>\1</h3>', src, flags=re.S)

    # ---- changelog --------------------------------------------------------
    log = ''
    if changelog_md:
        log = mdpipe.to_html(changelog_md, cfg.md_extensions)
        log = re.sub(r'<h1>(.*?)</h1>', '', log, flags=re.S)
        log, _, _ = mdpipe.anchor_headings(log, seen=ids)
        log = mdpipe.demote_headings(log, by=1)

    # ---- tree / gallery / people -----------------------------------------
    svg, legend, foot = tree.load(cfg, warn)
    # the project's standalone tree page is its own file; what the report links
    # to is a generated copy of it with the same scroll-and-zoom frame
    view_html, view_name = tree.standalone(cfg, warn)
    if view_html:
        open(cfg.p(view_name), 'w', encoding='utf-8').write(view_html)
    tree_html = tree.embed(cfg, svg, legend, foot, page_href=view_name or None)
    # the story page gets the diagram and its colour key, without the footnotes.
    # the svg goes in unmodified: its own <style> is scoped to #famtree, so
    # stripping ids would leave every shape with the default black fill. The two
    # copies live in separate documents, so no id can collide.
    story_tree = tree.embed(cfg, svg, legend, page_href=view_name or None,
                            compact=True)
    gal = figures.gallery(cfg.gallery, cfg.root)

    present = {'report'}
    prov = (f'<p class="note prov">{cfg.provenance_note}</p>' if cfg.provenance_note else '')
    chapters = [(sid, mdpipe.toc_label(full, overrides=cfg.toc_overrides), full)
                for sid, full in chapters_raw]
    body = [_section('report', '',
                     prov + shell.ladder_legend(cfg) + shell.toc(chapters) + rep,
                     rule=False)]
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
        body.append('<hr><section id="changelog"><h2>יומן המהדורות</h2>'
                    '<details class="changelog-wrap"><summary>'
                    f'כל המהדורות ({_count_editions(changelog_md)}) — מה השתנה בכל אחת'
                    f'</summary>{log}</details></section>')

    body_html = ''.join(body)
    body_html, n_figs = mdpipe.number_figures(body_html)
    body_html = mdpipe.rank_chips(body_html)
    body_html = mdpipe.wrap_tables(body_html)
    body_html = mdpipe.mark_external(body_html)

    out = shell.page(cfg, _updated_line(changelog_md, _stamp()), _stamp(),
                     body_html, chapters, present,
                     extra_rows=shell.page_rows(body_html),
                     story_href=cfg.story_name() if cfg.story else '')
    out = bidi.fix_document(out, cfg.extra_bidi_rules)

    open(cfg.p(cfg.main_html), 'w', encoding='utf-8').write(out)

    # ---- the story page ---------------------------------------------------
    story_out, story_name = '', ''
    if cfg.story:
        story_name = cfg.story_name()
        story_out = _story(cfg, story_tree, _updated_line(changelog_md, _stamp()), warn)
        open(cfg.p(story_name), 'w', encoding='utf-8').write(story_out)

    # the folder's front door opens the story when there is one, and the report
    # otherwise; the report itself never changes its filename, so every anchor
    # ever shared still resolves
    front = story_name or cfg.main_html
    open(cfg.p('index.html'), 'w', encoding='utf-8').write(
        shell.index_stub(front, cfg.story_title or cfg.title))

    # ---- gates ------------------------------------------------------------
    problems = qa.run_all(out, cfg.root, cfg.privacy_text_patterns)
    problems += qa.reading_shape(out)
    problems += qa.no_build_paths(out)
    files = [cfg.main_html, 'index.html', cfg.report_md, cfg.sources_md]
    if cfg.changelog_md:
        files.append(cfg.changelog_md)
    files += list(cfg.site_extra_files)
    if view_name:
        files.append(view_name)
    if story_name:
        files.append(story_name)
        problems += [f'בעמוד הסיפור: {p}'
                     for p in (qa.run_all(story_out, cfg.root, cfg.privacy_text_patterns)
                               + qa.reading_shape(story_out, is_story=True)
                               + qa.no_build_paths(story_out))]
        # every link the story makes into the report must land somewhere
        problems += qa.cross_page_anchors(story_out, out, cfg.main_html, 'בעמוד הסיפור: ')
    swept = site.sweep_thumbs(cfg, out, story_out)
    site.mirror(cfg, files)
    problems += qa.local_links_exist(out, cfg.p('site'), 'ב-site/: ', git_check=False)
    if story_out:
        problems += qa.local_links_exist(story_out, cfg.p('site'), 'בסיפור, ב-site/: ',
                                         git_check=False)
    warnings += qa.untracked_link_targets(out, cfg.root)
    problems += qa.ledger_privacy(cfg.root, getattr(cfg, 'published_ids', ()), warn=warnings)

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
