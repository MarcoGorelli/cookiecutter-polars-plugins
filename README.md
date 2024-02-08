# Polars Plugins Cookiecutter

<h1 align="center">
        <img
                width="200"
                alt="image"
                src="https://github.com/MarcoGorelli/cookiecutter-polars-plugins/assets/33491632/283905ec-cbfe-4b89-a8c9-f7a9547ed6d0">
</h1>

Easily get started with Polars Plugins - get the boilerplate
out of the way and start coding!

## Usage

First of all, make sure you have `cookiecutter` installed - see
[here](https://cookiecutter.readthedocs.io/en/stable/installation.html)
for how to do that.

Then, suppose you want to create a Polars Plugin called "polars-minimal-plugin".
Let's also suppose your name is "Maja Anima".

This is how you would do that:

1. In your home directory (or wherever you store your projects), run
   ```console
   cookiecutter https://github.com/MarcoGorelli/cookiecutter-polars-plugins.git
   ```
2. When prompted, enter the following:
   ```
   [1/3] plugin_name (Polars Cookiecutter): Minimal Plugin
   [2/3] project_slug (minimal_plugin):
   [3/3] author (anonymous): Maja Anima
   ```
3. Navigate to the directory you just created. For example, if you named your plugin "Minimal Plugin",
   you would do
   ```
   cd minimal_plugin
   ```
5. Create and activate a new Python 3.8+ [virtual environment](https://docs.python.org/3/library/venv.html).
   For example, on Linux or MacOS this would be
   ```
   python3.11 -m venv .venv
   . .venv/bin/activate
   ```
7. Install Polars and Maturin:
   ```
   pip install -U polars maturin
   ```
8. Start compiling the Rust code! This may take a few minutes the first time you do it, but subsequent
   runs will be fast:
   ```
   maturin develop  # or, if you're benchmarking, maturin develop --release
   ```

Now, writing your plugin is a different story...please go to https://marcogorelli.github.io/polars-plugins-tutorial/
for a tutorial on how to get started.
