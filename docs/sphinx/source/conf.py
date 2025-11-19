# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Add source folder to path for autodoc
sys.path.insert(0, os.path.abspath("../../../mellea"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Mellea"
copyright = "2025, IBM"
author = "IBM"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.autosummary", "sphinx.ext.napoleon"]

exclude_patterns = []

autosummary_generate = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'python_docs_theme'
html_theme = "sphinx_rtd_theme"

# -- Options for autodoc -----------------------------------------------------
autodoc_default_options = {
    "members": True,  # Document all public members (methods, attributes)
    "undoc-members": True,  # Document members without docstrings
    "show-inheritance": True,  # Show class inheritance
    "special-members": "__init__",  # Document special members like __init__
    "exclude-members": "__weakref__",  # Exclude specific members
    "member-order": "bysource",  # Order members as they appear in source code
}
