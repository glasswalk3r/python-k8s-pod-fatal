# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.join(
    os.path.abspath(
        os.path.join('..', '..')
    ),
    'src'
))

project = 'python-k8s-pod-fatal'
copyright = '2024, Alceu Rodrigues de Freitas Junior'
author = 'Alceu Rodrigues de Freitas Junior'
release = '0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns: list[str] = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

autodoc_default_options = {'members': True, 'undoc-members': True,
                           'private-members': True, 'special-members': True}
autodoc_typehints = 'description'

html_static_path = ['_static']
