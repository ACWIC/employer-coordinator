project = 'ACWIC Aged Care Provider Microservice Suite'
copyright = '2020, Aged Care Workforce Industry Council Pty Ltd'
author = 'Chris Gough'
release = '0.0'

extensions = [
    'sphinxcontrib.plantuml',
    'sphinx.ext.graphviz',
]
templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.venv'
]
html_theme = 'classic'
html_static_path = ['_static']
