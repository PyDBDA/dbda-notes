# dbda-notes

https://pydbda.github.io/dbda-notes/

For chat, we're using [Gitter](https://gitter.im/PyDBDA/Lobby).

Related projects can be found in the [Wiki](https://github.com/PyDBDA/dbda-notes/wiki).

Contributions should follow [PEP8](https://www.python.org/dev/peps/pep-0008/), the official Python style guide.

## Building the GitHub Pages site

You need to have the following python packages installed:

* `nbconvert`
* `nbformat`
* `jinja2`

In the root of this repository, run something like the following:

    python build_docs.py notebooks/*.ipynb

Which will convert all of the .ipynb files in the `notebooks/` directory to
html, build an index page, and stash all the html in the `docs/` folder, which
is where it needs to be for GitHub Pages to work.
