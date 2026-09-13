# -*- coding: utf-8 -*-
"""Per-project configuration for a documentary genealogy report.

One skeleton, one accent per report: everything that differs between the
`rachel-zadok` and `avraham-zadok` reports is declared here as data, and the
rest of `genealogy_site` is shared code.
"""
from dataclasses import dataclass, field
from typing import Callable, Optional
import os


@dataclass
class Palette:
    """The per-report accent. Everything else comes from the shared skeleton."""
    accent: str = '#7a5c1e'        # headings, rules, the hero gradient's warm end
    accent_soft: str = '#b8860b'   # small emphasis, hairline accents
    link: str = '#8a5f12'          # link text — must clear 4.5:1 on paper and on white
    paper: str = '#faf7f2'         # page background behind the reading column
    ink: str = '#2b2620'           # body text
    muted: str = '#6a6154'         # captions, metadata
    line: str = '#e2dbcc'          # hairlines and borders
    hero_from: str = '#3a2f1c'     # hero gradient, dark end
    hero_to: str = '#6b5324'       # hero gradient, warm end


@dataclass
class TreeSource:
    """Where the family-tree SVG comes from."""
    kind: str                       # 'html_extract' | 'svg_file'
    path: str                       # the file to read
    page_href: Optional[str] = None  # a standalone page to link to, if any
    label: str = 'עץ המשפחה'


@dataclass
class SpineFact:
    """One number on the hero's at-a-glance strip."""
    value: str
    label: str


@dataclass
class Beat:
    """One event on the story timeline.

    The timeline is the story page's spine: the life in order, one sentence per
    event, each graded and each linking into the place in the report that argues
    for it. A reader who reads nothing else should still come away with the shape
    of the life.
    """
    when: str                       # '1928', '22.6.1949', 'אוגוסט 1956'
    what: str                       # one sentence; inline HTML allowed
    place: str = ''                 # 'מכנאס', 'מעברת טירה'
    rank: str = ''                  # a rung of the ladder, spelled out
    href: str = ''                  # deep link into the report


@dataclass
class DocCard:
    """One key document on the story page: picture, date, what it proves."""
    img: str                        # path under the project, e.g. 'docs/…jpg'
    when: str
    title: str
    proves: str                     # one sentence — what this document establishes
    rank: str = ''
    href: str = ''                  # the section of the report that reads it
    focus: str = 'center top'       # object-position: what the crop must keep


@dataclass
class Verdict:
    """One column of the three-column "where the research stands" block."""
    title: str                      # 'ידוע בוודאות'
    rank: str                       # the rung this column represents
    lines: tuple = ()               # (text, href) pairs


@dataclass
class Story:
    """The reader-facing page: the same research, told as a life.

    The report is organised by kind of evidence (candidates, rejections, method);
    that is right for an auditor and wrong for a first-time reader, who wants to
    know in ten seconds who this was, what is certain, what is open, and where the
    photographs are. Both pages are generated from the same project.
    """
    lede: str                       # ~120 words, inline HTML allowed
    portrait: str = ''              # the photograph that opens the page
    portrait_alt: str = ''
    portrait_caption: str = ''
    verdicts: tuple = ()            # Verdict ×3
    timeline: tuple = ()            # Beat
    docs: tuple = ()                # DocCard
    open_questions: tuple = ()      # (text, href) — what is still being looked for
    timeline_note: str = ''
    docs_note: str = ''


@dataclass
class Person:
    """One row of the person index."""
    name: str
    dates: str = ''
    role: str = ''
    anchor: str = ''                # in-page anchor, e.g. '#ch-3'
    aka: str = ''                   # alternative spellings, searchable


@dataclass
class ProjectConfig:
    root: str                        # absolute path to the project directory
    slug: str
    main_html: str                   # the built page's filename
    title: str                       # <title> and hero h1
    subject: str                     # hero sub-line: who this is about
    meta_description: str

    report_md: str
    sources_md: str
    changelog_md: Optional[str] = None   # when set, the changelog lives outside the report

    # the reader-facing front page; when set, the project builds two pages and
    # the directory's index.html opens this one
    story: Optional['Story'] = None
    story_html: str = ''             # defaults to '<main_html stem>-הסיפור.html'
    story_title: str = ''            # defaults to cfg.title
    story_subject: str = ''          # hero sub-line on the story page
    story_spine: tuple = ()          # SpineFact — reader facts, not process counts

    tree: Optional[TreeSource] = None
    palette: Palette = field(default_factory=Palette)
    md_extensions: tuple = ('tables',)

    # content data supplied by the project
    spine: tuple = ()                    # SpineFact
    people: tuple = ()                   # Person
    figures: dict = field(default_factory=dict)      # key -> rendered <figure> html
    figure_anchors: tuple = ()           # (anchor_regex, figure_key)
    gallery: tuple = ()                  # (thumb_src, href, caption)

    # text transforms applied outside tags and anchors
    text_transforms: tuple = ()          # both report and sources
    report_transforms: tuple = ()        # report only
    sources_transforms: tuple = ()       # sources index only
    extra_bidi_rules: tuple = ()

    # navigation and shell
    breadcrumb: Optional[tuple] = None   # (href, label)
    provenance_note: str = ''
    footer_note: str = ''
    legacy_anchors: dict = field(default_factory=dict)  # old id -> regex on the h2 text
    toc_overrides: dict = field(default_factory=dict)   # regex on the h2 text -> nav label
    # extra rows for the in-page search that are not people:
    # (label, anchor, kind, alternative spellings)
    search_extra: tuple = ()
    # one line under the person index explaining the date notation it uses
    people_legend: str = ''
    # (term, explanation) — the handful of research words a first-time reader
    # cannot be expected to know; shown beside the certainty ladder
    glossary: tuple = ()

    # publishing
    site_extra_files: tuple = ()
    # other pages that reference this project's thumbnails and must be
    # consulted before the cache is swept (e.g. the archive's own portal)
    thumb_referrers: tuple = ()
    # globs matched against file names while the site copy is made
    privacy_file_patterns: tuple = ()
    # substrings that must not appear anywhere in the finished page
    privacy_text_patterns: tuple = ()
    published_ids: tuple = ()          # identity numbers cleared for publication (appear in an official gazette)
    qa_strict: bool = True

    def p(self, *parts):
        return os.path.join(self.root, *parts)

    def story_name(self):
        """The story page's filename.

        The report keeps the filename it has always had: every anchor shared or
        cited so far points into it, and a research page that moves is a research
        page that breaks. The story is the new file, and the folder's index.html
        is what changes to open it.
        """
        if self.story_html:
            return self.story_html
        stem = os.path.splitext(self.main_html)[0]
        return f'{stem}-הסיפור.html'
