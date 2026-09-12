"""treegen — a tiny right-to-left family-tree SVG generator for the archive's tree.html pages.

Layout model: a grid of columns (col 0 = rightmost, as Hebrew reads) and rows (row 0 = top).
Every person is one box. Couples are adjacent boxes joined by a dashed line. A parent (or
couple) feeds a horizontal bus that drops to each child. Colours are passed in so each project
keeps its palette. Output is the <svg> element only; the project's tree.html wraps it.
"""
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

BOX_W, BOX_H, GAP_X, GAP_Y = 138, 60, 14, 62
FONT = "'David Libre','Frank Ruhl Libre',Georgia,serif"


@dataclass
class Node:
    id: str
    col: float
    row: int
    title: str
    sub: List[str] = field(default_factory=list)
    dashed: bool = False      # known from family / parents column only
    focus: bool = False       # the page's subject


@dataclass
class Tree:
    nodes: List[Node]
    couples: List[Tuple[str, str]] = field(default_factory=list)      # dashed link between two ids
    families: List[Tuple[List[str], List[str], int]] = field(default_factory=list)  # (parent ids, child ids, bus offset px)
    links: List[Tuple[str, str]] = field(default_factory=list)        # dotted link (e.g. aunt)
    ink: str = '#1e2a32'; muted: str = '#5e6b73'; line: str = '#c5ccc7'; accent: str = '#1f6f5b'; marr: str = '#9aa5a0'
    title: str = ''

    def _n(self, i):
        return next(n for n in self.nodes if n.id == i)

    def render(self) -> str:
        cols = max(n.col for n in self.nodes) + 1
        rows = max(n.row for n in self.nodes) + 1
        W = int(cols * (BOX_W + GAP_X) + 20)
        H = int(rows * (BOX_H + GAP_Y) + 20)

        def x(n):  # left edge of the box (col 0 is rightmost)
            return W - 10 - (n.col + 1) * (BOX_W + GAP_X) + GAP_X
        def y(n):
            return 10 + n.row * (BOX_H + GAP_Y)
        def cx(n): return x(n) + BOX_W / 2
        def top(n): return y(n)
        def bot(n): return y(n) + BOX_H

        paths, dashes, dots = [], [], []
        for a, b in self.couples:
            na, nb = self._n(a), self._n(b)
            l, r = sorted([na, nb], key=cx)
            dashes.append(f'M{x(l)+BOX_W:g} {y(l)+BOX_H/2:g} H{x(r):g}')
        for a, b in self.links:
            na, nb = self._n(a), self._n(b)
            dots.append(f'M{cx(na):g} {bot(na):g} V{top(nb)-8:g} H{cx(nb):g} V{top(nb):g}')
        for parents, children, off in self.families:
            ps = [self._n(p) for p in parents]
            pcx = sum(cx(p) for p in ps) / len(ps)
            pbot = max(bot(p) for p in ps)
            cs = [self._n(c) for c in children]
            busy = min(top(c) for c in cs) - 22 + off
            xs = [cx(c) for c in cs] + [pcx]
            paths.append(f'M{pcx:g} {pbot:g} V{busy:g} M{min(xs):g} {busy:g} H{max(xs):g}')
            for c in cs:
                paths.append(f'M{cx(c):g} {busy:g} V{top(c):g}')

        out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">']
        if self.title:
            out.append(f' <title>{self.title}</title>')
        out.append(f' <g fill="none" stroke="{self.line}" stroke-width="1.5">')
        for p in paths: out.append(f'  <path d="{p}"/>')
        for p in dashes: out.append(f'  <path d="{p}" stroke-dasharray="4 3" stroke="{self.marr}"/>')
        for p in dots: out.append(f'  <path d="{p}" stroke-dasharray="2 3" stroke="{self.marr}"/>')
        out.append(' </g>')
        out.append(f' <g fill="#ffffff" stroke="{self.line}" stroke-width="1.2">')
        for n in self.nodes:
            extra = ''
            if n.focus: extra = f' stroke="{self.accent}" stroke-width="2"'
            if n.dashed: extra += ' stroke-dasharray="5 3"'
            out.append(f'  <rect x="{x(n):g}" y="{y(n):g}" width="{BOX_W}" height="{BOX_H}" rx="4"{extra}/>')
        out.append(' </g>')
        out.append(f' <g fill="{self.ink}" font-size="15" text-anchor="middle">')
        for n in self.nodes:
            out.append(f'  <text x="{cx(n):g}" y="{y(n)+22:g}">{n.title}</text>')
        out.append(' </g>')
        out.append(f' <g fill="{self.muted}" font-size="10.5" text-anchor="middle">')
        for n in self.nodes:
            for i, s in enumerate(n.sub[:2]):
                out.append(f'  <text x="{cx(n):g}" y="{y(n)+38+i*13:g}">{s}</text>')
        out.append(' </g>')
        out.append('</svg>')
        return '\n'.join(out)


def replace_svg(path: str, svg: str) -> None:
    s = open(path, encoding='utf-8').read()
    a = s.index('<svg'); b = s.index('</svg>') + 6
    open(path, 'w', encoding='utf-8').write(s[:a] + svg + s[b:])
