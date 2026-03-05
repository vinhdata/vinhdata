"""Patch MkDocs for working hot reload.

MkDocs 1.6 has a Click CLI bug where livereload defaults to False
instead of True, so file watching never starts. This script forces
livereload=True before calling the serve function.
"""

import sys

import mkdocs.commands.serve as serve_mod
from mkdocs.__main__ import cli

_orig_serve = serve_mod.serve


def _patched_serve(*args, **kwargs):
    kwargs["livereload"] = True
    _orig_serve(*args, **kwargs)


serve_mod.serve = _patched_serve

if __name__ == "__main__":
    sys.argv = ["mkdocs", "serve"] + sys.argv[1:]
    cli()
