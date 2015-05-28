# -*- coding: utf-8 -*-
"""The hashfs library is a content addressable file management system.
"""

from .__meta__ import (
    __title__,
    __summary__,
    __url__,
    __version__,
    __author__,
    __email__,
    __license__
)

from .hashfs import HashFS, HashAddress


__all__ = ('HashFS', 'HashAddress')
