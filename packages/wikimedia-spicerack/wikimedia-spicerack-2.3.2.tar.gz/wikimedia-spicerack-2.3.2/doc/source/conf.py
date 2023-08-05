# -*- coding: utf-8 -*-
"""Sphynx configuration."""
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use pathlib's resolve() to make it absolute, like shown here.
#
import sys
from pathlib import Path

import sphinx_rtd_theme
from pkg_resources import get_distribution

# Adjust path
sys.path.insert(0, Path(__file__).parent.parent.resolve())

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinxarg.ext",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Spicerack"
title = f"{project} Documentation"
copyright = "2018-2021, Riccardo Coccioli <rcoccioli@wikimedia.org>, Wikimedia Foundation, Inc."
author = "Riccardo Coccioli"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = get_distribution("wikimedia-spicerack").version
# The short X.Y version.
version = release


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Spicerackdoc"


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("cookbook", "cookbook", "Spicerack Cookbook Runner", [author], 1),
]


# -- Options for intersphinx ---------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "ClusterShell": ("https://clustershell.readthedocs.io/en/v1.8.1/", None),
    "cumin": ("https://doc.wikimedia.org/cumin/master/", None),
    "requests": ("https://requests.readthedocs.io/en/master/", None),
    "pymysql": ("https://pymysql.readthedocs.io/en/latest/", None),
    "wmflib": ("https://doc.wikimedia.org/wmflib/master/", None),
    "kafka": ("https://kafka-python.readthedocs.io/en/master/", None),
    "git": ("https://gitpython.readthedocs.io/en/stable/", None),
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True

# Autodoc settings
autodoc_default_options = {
    # Using None as value instead of True to support the version of Sphinx used in Buster
    "members": None,
    "member-order": "groupwise",
    "show-inheritance": None,
}
autoclass_content = "both"


# -- Helper functions -----------------------------------------------------


def filter_namedtuple_docstrings(app, what, name, obj, options, lines):
    """Fix the automatically generated docstrings for namedtuples classes."""
    if what == "property" and len(lines) == 1 and lines[0].startswith("Alias for field number"):
        del lines[:]


# Keep track of documented classes to avoid annotating both class and __init__.
# Necessary when using autoclass_content 'both' and add_abstract_annotations().
_spicerack_documented_classes = set()


def add_abstract_annotations(app, what, name, obj, options, lines):
    """Workaround to add an abstract annotation for ABC abstract classes."""
    if (
        what == "class"
        and len(getattr(obj, "__abstractmethods__", [])) > 0
        and name not in _spicerack_documented_classes
    ):
        lines.insert(0, "``abstract``")
        _spicerack_documented_classes.add(name)


def setup(app):
    """Register the filter_namedtuple_docstrings function."""
    app.connect("autodoc-process-docstring", filter_namedtuple_docstrings)
    app.connect("autodoc-process-docstring", add_abstract_annotations)
    app.add_css_file("theme_overrides.css")  # override wide tables in RTD theme
