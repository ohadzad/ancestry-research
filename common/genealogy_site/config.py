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

    # publishing
    site_extra_files: tuple = ()
    # other pages that reference this project's thumbnails and must be
    # consulted before the cache is swept (e.g. the archive's own portal)
    thumb_referrers: tuple = ()
    # globs matched against file names while the site copy is made
    privacy_file_patterns: tuple = ()
    # substrings that must not appear anywhere in the finished page
    privacy_text_patterns: tuple = ()
    qa_strict: bool = True

    def p(self, *parts):
        return os.path.join(self.root, *parts)
