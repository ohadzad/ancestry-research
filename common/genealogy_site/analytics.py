"""Google Analytics (GA4) for every published page.

The measurement id lives in one place — `site.analytics_id` in research_registry.json
at the archive root — so the portal and all the research pages carry the same tag.
No id (or a malformed one) means no tag at all.
"""
import json
import os
import re

_REGISTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                         'research_registry.json')
_ID = re.compile(r'G-[A-Z0-9]{4,20}')


def measurement_id():
    try:
        with open(_REGISTRY, encoding='utf-8') as f:
            mid = json.load(f).get('site', {}).get('analytics_id', '') or ''
    except (OSError, ValueError):
        return ''
    return mid if _ID.fullmatch(mid) else ''


def head_tag():
    """The gtag.js snippet for <head>, or '' when no id is configured."""
    mid = measurement_id()
    if not mid:
        return ''
    return (f'<script async src="https://www.googletagmanager.com/gtag/js?id={mid}"></script>\n'
            '<script>window.dataLayer=window.dataLayer||[];'
            'function gtag(){dataLayer.push(arguments);}'
            f"gtag('js',new Date());gtag('config','{mid}');</script>\n")
