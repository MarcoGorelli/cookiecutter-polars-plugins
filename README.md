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

Then, suppose you want to create a Polars Plugin called "polars-minimal-plugin",
which users will be able to access with the namespace `mp` (so, for example,
`pl.col('a').mp`). Let's also suppose your name is "Maja Anima".

This is how you would do that:

1. In your home directory (or wherever you store your projects), run
   ```console
   $ cookiecutter https://github.com/MarcoGorelli/cookiecutter-polars-plugins.git
   ```
2. When prompted, enter the following:
   ```
   [1/4] plugin_name (Polars Cookiecutter): Polars Minimal Plugin
   [2/4] project_slug (polars_minimal_plugin):
   [3/4] plugin_namespace (pc): mp
   [4/4] author (anonymous): Maja Anima
   ```
3. That's it! You can now do `cd polars_minimal_plugin` (or `cd` to
   whatever you're naming your plugin) and start developing your plugin!

You may want to take a look at https://marcogorelli.github.io/polars-plugins-tutorial/
for how to get started with writing a plugin.

