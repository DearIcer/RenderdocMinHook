#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# RenderDoc documentation build configuration file, created by
# sphinx-quickstart on Thu May 12 16:59:09 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import re
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

import struct

# path to module libraries for windows
if struct.calcsize("P") == 8:
    binpath = '../x64/'
else:
    binpath = '../Win32/'

# Prioritise release over development builds
sys.path.insert(0, os.path.abspath(binpath + 'Development/pymodules'))
sys.path.insert(0, os.path.abspath(binpath + 'Release/pymodules'))

# Add the build paths to PATH so renderdoc.dll can be located
os.environ["PATH"] += os.pathsep + os.path.abspath(binpath + 'Development/')
os.environ["PATH"] += os.pathsep + os.path.abspath(binpath + 'Release/')

if sys.platform == 'win32' and sys.version_info[1] >= 8:
    os.add_dll_directory(binpath + 'Release/')
    os.add_dll_directory(binpath + 'Development/')

# path to module libraries for linux
sys.path.insert(0, os.path.abspath('../build/lib'))

sys.path.insert(0, os.path.abspath('sphinx_exts'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx_paramlinks']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'RenderDoc'
copyright = '{0}, Baldur Karlsson'.format(datetime.date.today().year)
author = 'Baldur Karlsson'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

major_version = 123
minor_version = 999

with open('../renderdoc/api/replay/version.h') as f:
    for line in f:
        if line.find('#define RENDERDOC_VERSION_MAJOR') >= 0:
            major_version = line.split()[2]
        if line.find('#define RENDERDOC_VERSION_MINOR') >= 0:
            minor_version = line.split()[2]

version = '{0}.{1}'.format(major_version, minor_version)
# The full version, including alpha/beta/rc tags.
release = 'v{0}'.format(version)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'sphinx_exts', 'include']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
html_title = 'RenderDoc documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr', 'zh'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'renderdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'RenderDoc.tex', 'RenderDoc Documentation',
     'Baldur Karlsson', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'renderdoc', 'RenderDoc Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'RenderDoc', 'RenderDoc Documentation',
     author, 'RenderDoc', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# custom theme based on sphinx_rtd_theme
if os.path.isdir('sphinx_rtd_theme_chm_friendly'):
    html_theme = "sphinx_rtd_theme_chm_friendly"
    html_theme_path = ["."]
else:
    html_theme = "sphinx_rtd_theme"

html_context = {
    'show_source': False,
    'html_show_sourcelink': False,
    'display_github': True,
    'github_user': 'baldurk',
    'github_repo': 'renderdoc',
    'github_version': 'v{0}'.format(version),
    'conf_py_path': '/docs/',
}

# We need 1.5 and above for the htmlhelp links to be handled properly without
# needing separate ugly _blank links. If you don't care about that, you can
# disable this
if(tags.has('htmlhelp')):
    print("**** We require sphinx 1.5 for htmlhelp build to have the fix for issue #2550 ****")
    needs_sphinx = '1.5'

def maybe_skip_member(app, what, name, obj, skip, options):
    # Hide these SWIG internals
    if name == "this" or name == "thisown":
        return True
    # Allow hiding free module functions, or only showing free module functions
    if 'exclude-members' in options and what == "module":
        if 'free_functions__' in options['exclude-members'] and 'built-in function' in repr(obj):
            return True
        if 'non_free_functions__' in options['exclude-members'] and 'built-in function' not in repr(obj):
            return True
    # Allow hiding enum constant members (i.e. int constants). These can then be documented explicitly
    # as we don't have a way in SWIG to attach docstrings to constants directly.
    if 'exclude-members' in options and 'enum_constants__' in options['exclude-members'] and isinstance(obj, int):
        return True
    if 'exclude-members' in options and 'properties__' in options['exclude-members'] and 'getset_desc' in str(type(obj)):
        return True
    # Allow arbitrary globbing as a hack to exclude or include members
    if 'exclude-members' in options:
        for exclude in options['exclude-members']:
            # Look for a hack that describes a name match
            if exclude.startswith('name_match__'):
                match = exclude.replace('name_match__', '')

                include_only = False

                # see if it wants to include only matches, or exclude matches (default)
                if match.startswith('include_only__'):
                    match = match.replace('include_only__', '')
                    include_only = True

                objname = ""
                if '__qualname__' in dir(obj):
                    objname = obj.__qualname__
                else:
                    try:
                        objname = obj.__name__
                    except AttributeError:
                        objname = obj.__class__.__name__
                ismatch = False

                # see if we're matching a prefix, or doing just a glob
                if match.startswith('startswith__'):
                    match = match.replace('startswith__', '')
                    ismatch = objname.startswith(match)

                if match.startswith('in__'):
                    match = match.replace('in__', '')
                    ismatch = match in objname

                # if we want to include only matches and it didn't match, skip this
                if include_only and not ismatch:
                    return True

                # If we want to exclude matches and it DID match, skip
                if not include_only and ismatch:
                    return True
    return None

def build_finished(app, exception):
    import renderdoc as rd
    import qrenderdoc as qrd

    from sphinx.domains.python import PythonDomain
    from sphinx.errors import SphinxError

    if exception is not None:
        return

    print(rd)
    print(qrd)

    # Get list of documented/indexed python objects
    pydomain = app.env.get_domain('py')
    if not hasattr(pydomain, 'objects'):
        print("WARNING: Sphinx version is too old to check objects validity. Upgrade to at least Sphinx 2.1.0")
        return
    objs = pydomain.objects

    # Enumerate the namespaced objects in both modules
    items = []
    for module_name in ['renderdoc', 'qrenderdoc']:
        module = sys.modules[module_name]
        entries = dir(module)
        for item in dir(module):
            if 'INTERNAL:' not in str(module.__dict__[item].__doc__):
                items.append('{}.{}'.format(module_name, item))

    items = set(filter(lambda i: re.search('__|SWIG|ResourceId_Null|rdcfixedarray_of|rdcarray_of|Structured.*List', i) is None, items))

    # Remove any documented/indexed python objects
    items -= set(objs.keys())

    # Print an error if any remain
    if len(items) > 0:
        items = sorted(list(items))
        raise SphinxError("These {} global classes/functions are not included in the documentation index:\n* {}".format(len(items), '\n* '.join(items)))

    print("All python objects are linked in the documentation.")

def setup(app):
    app.connect('autodoc-skip-member', maybe_skip_member)
    app.connect('build-finished', build_finished)
