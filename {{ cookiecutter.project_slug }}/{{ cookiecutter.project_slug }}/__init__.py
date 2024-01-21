import polars as pl
from polars.utils.udfs import _get_shared_lib_location
from polars.type_aliases import IntoExpr

lib = _get_shared_lib_location(__file__)


@pl.api.register_expr_namespace("{{ cookiecutter.plugin_namespace  }}")
class {{ cookiecutter.plugin_namespace.title() }}Expr:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

