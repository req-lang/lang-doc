import sys
import os

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Qitab'
copyright = '2021-2026, Sami Dahoux'
author = 'Sami Dahoux'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_theme_options = {
   "logo": {
      "image_light": "_static/qitab-full.svg",
      "image_dark": "_static/qitab-full-dark.svg",
   },
   "footer_end": [],
   "show_nav_level": 2,
   "show_toc_level": 2,
   }
html_favicon = "_static/logo-qitab.ico"
html_css_files = [
    'theme.css',
]
html_show_sphinx = False


def setup(sphinx):
    sys.path.insert(0, os.path.abspath('./source'))
    from reqlexer import ReqLexer
    sphinx.add_lexer("req", ReqLexer)
