# -*- coding: utf-8 -*-
"""Shared engine for the documentary genealogy reports in this archive.

One skeleton, one accent per report. A project declares its data in a
``ProjectConfig`` and calls ``build``; everything else lives here.
"""
from .config import (ProjectConfig, Palette, TreeSource, SpineFact, Person,
                     Story, Beat, DocCard, Verdict)
from .build import build

__all__ = ['ProjectConfig', 'Palette', 'TreeSource', 'SpineFact', 'Person',
           'Story', 'Beat', 'DocCard', 'Verdict', 'build']
