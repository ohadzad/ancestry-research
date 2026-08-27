# -*- coding: utf-8 -*-
"""Right-to-left protection.

Hebrew prose that embeds Latin script, numeric ranges and archive reference
codes reorders visually under the Unicode bidirectional algorithm. The rules
here wrap the hazardous runs in <bdi dir="ltr"> so each one is isolated.

Two invariants matter and are enforced by the splitters below:
  * never wrap something already inside a <bdi>;
  * never insert <bdi> into <svg>, <style>, <script> or <pre>, where it is
    either invalid or meaningless.
"""
import re

# ---- splitters -------------------------------------------------------------
# treats a whole anchor as opaque: an already-linked filename is never re-linked
_TAGSPLIT = re.compile(r'(<a\b[^>]*>.*?</a>|<[^>]+>)', re.S)
# tags only: descends into anchor text, which the bidi pass must do
# a tag ends at the first '>' that is not inside a quoted attribute value
_TAGONLY = re.compile(r'''(<[a-zA-Z/!][^>"']*(?:(?:"[^"]*"|'[^']*')[^>"']*)*>)''')
_BDI_SPAN = re.compile(r'(<bdi\b[^>]*>.*?</bdi>)', re.S)
_OPAQUE = re.compile(r'(<svg\b.*?</svg>|<style\b.*?</style>|<script\b.*?</script>|<pre\b.*?</pre>)', re.S)


def apply_text(html, fn):
    """Apply a text substitution only outside existing tags and anchors."""
    parts = _TAGSPLIT.split(html)
    for i in range(0, len(parts), 2):
        parts[i] = fn(parts[i])
    return ''.join(parts)


def _latin_run(m):
    t = m.group(1)
    # never leave an unmatched ')' inside the isolate: it would mirror against
    # an '(' that sits outside it
    while t.count(')') > t.count('(') and t.endswith(')'):
        t = t[:-1]
    tail = m.group(1)[len(t):]
    return '<bdi dir="ltr">' + t + '</bdi>' + tail


HEB = r'֐-ֿ'

RULES = [
    # long Latin-script runs (quotations) inside RTL paragraphs
    (re.compile(r'(?<![\w])([A-Za-zÀ-ɏ][A-Za-zÀ-ɏ0-9 ,.:;\-–()/’“”!?]{28,}[A-Za-zÀ-ɏ0-9./)])'),
     _latin_run),
    # month/year ranges: 12/1909–02/1911
    (re.compile(r'(?<![\w' + HEB + r'])(\d{1,2}/\d{4}–\d{1,2}/\d{4})(?![\w' + HEB + r'])'),
     r'<bdi dir="ltr">\1</bdi>'),
    # numeric ranges: 1929–2021, 192–201, 24–26.08.1944
    # the isolate must END on a digit: a trailing comma, colon or full stop
    # belongs to the Hebrew clause around it and would be laid out on the
    # wrong side if it were swallowed into the LTR run
    (re.compile(r'(?<![\w' + HEB + r'/])(?<![A-Za-z0-9]-)(\d[\d.,:]*–\d(?:[\d.,:]*\d)?)(?![\w' + HEB + r'/])'),
     r'<bdi dir="ltr">\1</bdi>'),
    # archive reference codes: 01014102 129.172
    (re.compile(r'(?<![\w' + HEB + r'])(0\d{7}\s\d{3}\.\d{3}(?:\.\d{3})?)(?![\w' + HEB + r'])'),
     r'<bdi dir="ltr">\1</bdi>'),
    # prisoner numbers written with a thousands space: 38 443
    (re.compile(r'(?<![\w' + HEB + r'])(\d{2}\s\d{3})(?![\w' + HEB + r'.])'),
     r'<bdi dir="ltr">\1</bdi>'),
]


def fix_document(html, extra_rules=()):
    """Wrap every hazardous run in the finished document."""
    rules = list(RULES) + list(extra_rules)

    def _f(t):
        for rx, rep in rules:
            t = rx.sub(rep, t)
        return t

    def _pass(chunk):
        parts = _TAGONLY.split(chunk)
        for i in range(0, len(parts), 2):
            parts[i] = _f(parts[i])
        return ''.join(parts)

    def _outside_bdi(chunk):
        outer = _BDI_SPAN.split(chunk)
        for i in range(0, len(outer), 2):
            outer[i] = _pass(outer[i])
        return ''.join(outer)

    parts = _OPAQUE.split(html)
    for i in range(0, len(parts), 2):
        parts[i] = _outside_bdi(parts[i])
    return ''.join(parts)
