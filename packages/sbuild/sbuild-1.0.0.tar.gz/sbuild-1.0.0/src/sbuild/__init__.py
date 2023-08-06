"""A simple build backend for python projects with nuitka and typing support."""

__version__ = "1.0.0"
__author__  = "bit"
__desc__    = __doc__
__all__     = [
    "build_sdist",
    "build_wheel",
    "get_requires_for_build_sdist",
    "get_requires_for_build_wheel",
    "prepare_metadata_for_build_wheel",
]


from .build import (
        build_sdist,
        build_wheel,
        get_requires_for_build_sdist,
        get_requires_for_build_wheel,
        prepare_metadata_for_build_wheel,
)

