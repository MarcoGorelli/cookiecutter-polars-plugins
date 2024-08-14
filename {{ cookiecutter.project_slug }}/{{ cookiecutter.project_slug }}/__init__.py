from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import polars as pl

from {{ cookiecutter.project_slug }}._internal import __version__ as __version__
from {{ cookiecutter.project_slug }}.utils import register_plugin, parse_version

if TYPE_CHECKING:
    from {{ cookiecutter.project_slug }}.typing import IntoExpr

if parse_version(pl.__version__) < parse_version("0.20.16"):
    from polars.utils.udfs import _get_shared_lib_location  # type: ignore[import-not-found]

    lib: str | Path = _get_shared_lib_location(__file__)
else:
    lib = Path(__file__).parent


def pig_latinnify(expr: IntoExpr) -> pl.Expr:
    return register_plugin(
        args=[expr],
        symbol="pig_latinnify",
        is_elementwise=True,
        lib=lib,
    )

