# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'github-actions-experiments'
copyright = '2023, Mason McGough'
author = 'Mason McGough'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',   # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
    'sphinx.ext.duration',  # https://www.sphinx-doc.org/en/master/usage/extensions/duration.html
    'sphinx.ext.napoleon'   # https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
