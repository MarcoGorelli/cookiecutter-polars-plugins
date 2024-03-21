from __future__ import annotations

from typing import TYPE_CHECKING

import polars as pl
from polars.utils.udfs import _get_shared_lib_location

from {{ cookiecutter.project_slug }}.utils import parse_into_expr, register_plugin

if TYPE_CHECKING:
    from polars.type_aliases import IntoExpr

lib = _get_shared_lib_location(__file__)

def pig_latinnify(expr: IntoExpr) -> pl.Expr:
    expr = parse_into_expr(expr)
    return register_plugin(
        args=[expr],
        lib=lib,
        symbol="pig_latinnify",
        is_elementwise=True,
    )

