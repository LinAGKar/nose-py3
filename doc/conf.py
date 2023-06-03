# -*- coding: utf-8 -*-
#
# nose documentation build configuration file, created by
# sphinx-quickstart on Thu Mar 26 16:49:00 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.

# need to be brutal because of easy_install's pth hacks:
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath('.'))

from nose import __versioninfo__ as nose_version

nose_version = tuple(str(x) for x in nose_version)

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx',
              'nose.sphinx.pluginopts']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'nose'
copyright = u'2009, Jason Pellerin, 2020 - 2023, Adam Bilbrough'
maintainer = u'2020 - 2023, Adam Bilbrough'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '.'.join(nose_version[:2])
# The full version, including alpha/beta/rc tags.
release = '.'.join(nose_version[:3])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['.build']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'trac'

# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'nose.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    'index': 'indexsidebar.html'
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {'index': 'index.html'}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
# html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'nosedoc'

"""
footerbgcolor (CSS color): Background color for the footer line.
footertextcolor (CSS color): Text color for the footer line.
sidebarbgcolor (CSS color): Background color for the sidebar.
sidebartextcolor (CSS color): Text color for the sidebar.
sidebarlinkcolor (CSS color): Link color for the sidebar.
relbarbgcolor (CSS color): Background color for the relation bar.
relbartextcolor (CSS color): Text color for the relation bar.
relbarlinkcolor (CSS color): Link color for the relation bar.
bgcolor (CSS color): Body background color.
textcolor (CSS color): Body text color.
linkcolor (CSS color): Body link color.
headbgcolor (CSS color): Background color for headings.
headtextcolor (CSS color): Text color for headings.
headlinkcolor (CSS color): Link color for headings.
codebgcolor (CSS color): Background color for code blocks.
codetextcolor (CSS color): Default text color for code blocks, if not set differently by the highlighting style.
bodyfont (CSS font-family): Font for normal text.
headfont (CSS font-family): Font for headings.
"""
html_theme_options = {
    'rightsidebar': 'true',
    'sidebarbgcolor': '#fff',
    'sidebartextcolor': '#20435c',
    'sidebarlinkcolor': '#355f7c',
    'bgcolor': '#fff',
    'codebgcolor': '#ffe',
    'headbgcolor': '#fff',
    'relbarbgcolor': '#fff',
    'relbartextcolor': '#20435c',
    'relbarlinkcolor': '#355f7c',
}

# the css mostly overrides this:
html_theme = 'default'

# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
    ('index', 'nose.tex', 'nose Documentation', 'Jason Pellerin', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/dev': None}

# Man page
man_pages = [('man', 'nosetests', 'Nicer testing for Python', 'Nose developers', 1)]
