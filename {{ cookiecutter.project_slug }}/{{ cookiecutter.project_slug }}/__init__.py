from __future__ import annotations

from typing import TYPE_CHECKING

import polars as pl

from {{ cookiecutter.project_slug }}.utils import parse_into_expr, register_plugin

if TYPE_CHECKING:
    from polars.type_aliases import IntoExpr

def pig_latinnify(expr: IntoExpr) -> pl.Expr:
    expr = parse_into_expr(expr)
    return register_plugin(
        args=[expr],
        symbol="pig_latinnify",
        is_elementwise=True,
    )

