# I haven't set up CI for this repo yet, so here's
# a little thing I run manually to check it's set up
# correctly
rm -rf my_plugin
cookiecutter ~/cookiecutter-polars-plugins --no-input
cd my_plugin
uv venv -p python3.12
. .venv/bin/activate
uv pip install -U polars maturin pytest pip
make install
pytest

