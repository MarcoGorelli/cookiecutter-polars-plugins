import polars as pl
from {{ cookiecutter.project_slug }} import pig_latinnify


df = pl.DataFrame(
    {
        "english": ["this", "is", "not", "pig", "latin"],
    }
)
result = df.with_columns(pig_latin=pig_latinnify("english"))
print(result)
