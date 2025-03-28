# Polars Plugins Cookiecutter

<h1 align="center">
        <img
                width="200"
                alt="Image from https://chelsweets.com/polar-bear-cookies"
                src="https://github.com/MarcoGorelli/cookiecutter-polars-plugins/assets/33491632/379777d7-0bcb-41d1-8529-ac9bae1e6320"
">
</h1>

Easily get started with Polars Plugins - get the boilerplate
out of the way and start coding!

## Usage

First of all, make sure you have `cookiecutter` installed - see
[here](https://cookiecutter.readthedocs.io/en/stable/installation.html)
for how to do that.

Then, suppose you want to create a Polars Plugin called "minimal-plugin".
Let's also suppose your name is "Maja Anima".

This is how you would do that:

0. Install [Rust](https://rustup.rs/)
1. In your home directory (or wherever you store your projects), run
   ```console
   cookiecutter https://github.com/MarcoGorelli/cookiecutter-polars-plugins.git
   ```
2. When prompted, enter the following:
   ```
   [1/3] plugin_name (My Plugin): Minimal Plugin
   [2/3] project_slug (minimal_plugin):
   [3/3] author (anonymous): Maja Anima
   ```
3. Navigate to the directory you just created. For example, if you named your plugin "Minimal Plugin",
   you would do
   ```
   cd minimal_plugin
   ```
4. Create and activate a new Python 3.9+ virtual environment and install Polars and Maturin.
   If you're new to this, here's one way that we recommend:

   1. Install uv: https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started
   2. Install some version of Python greater than Python3.9. For example, to install
      Python3.11:
      ```
      uv python install 3.11
      ```
   3. Create a virtual environment:
      ```
      uv venv -p python3.11
      ```
   4. Activate your virtual environment:
      ```
      # On macOS and Linux.
      source .venv/bin/activate

      # On Windows.
      .venv\Scripts\activate
      ```
   5. Install Polars and Maturin:
      ```
      uv pip install -U polars maturin pip
      ```
5. Start compiling the Rust code! This may take a few minutes the first time you do it, but subsequent
   runs will be fast:
   ```
   maturin develop  # or, if you're benchmarking, maturin develop --release
   ```
6. Try running
   ```
   python run.py
   ```
   If you see
   ```
   shape: (5, 2)
   ┌─────────┬───────────┐
   │ english ┆ pig_latin │
   │ ---     ┆ ---       │
   │ str     ┆ str       │
   ╞═════════╪═══════════╡
   │ this    ┆ histay    │
   │ is      ┆ siay      │
   │ not     ┆ otnay     │
   │ pig     ┆ igpay     │
   │ latin   ┆ atinlay   │
   └─────────┴───────────┘
   ```
   then it means everything worked correctly! If not, please open an issue, happy
   to help debug.

Now, writing your plugin is a different story...please go to https://marcogorelli.github.io/polars-plugins-tutorial/
for a tutorial on how to get started.

