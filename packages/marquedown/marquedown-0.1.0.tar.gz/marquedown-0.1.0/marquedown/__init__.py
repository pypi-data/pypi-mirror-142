__version__ = '0.1.0'

import markdown as md

from .citation import citation


def marquedown(document: str, **kwargs):
    """Convert both Marquedown and Markdown into HTML."""

    document = citation(document)
    document = md.markdown(document)
    return document