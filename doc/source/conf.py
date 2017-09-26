# -*- coding: utf-8 -*-
#
# Mapchete documentation build configuration file, created by
# sphinx-quickstart on Fri Feb 24 21:39:27 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from mock import Mock as MagicMock

sys.path.insert(0, os.path.abspath('../../'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'numpydoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['ntemplates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Mapchete'
copyright = u'2015, 2016, 2017, EOX IT Services'
author = u'Joachim Ungar'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
with open('../../mapchete/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue
release = version

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
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['nstatic']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Mapchetedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Mapchete.tex', u'Mapchete Documentation',
     u'Joachim Ungar', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'mapchete', u'Mapchete Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Mapchete', u'Mapchete Documentation',
     author, 'Mapchete', 'Mapchete processes raster and vector geodata.',
     'GIS'),
]

# numpydoc fix
numpydoc_show_class_members = False


# Mocking packages:


class Mock(MagicMock):
    """Pretend the dependencies are installed when building docs."""

    @classmethod
    def __getattr__(cls, name):
        """Need to put a docstring here, otherwise my linter cries."""
        return MagicMock()


MOCK_MODULES = [
    'tilematrix',
    'fiona',
    'pyyaml',
    'flask',
    'Pillow',
    'PIL',
    'PIL.Image',
    'rasterio',
    'rasterio.features',
    'rasterio.warp',
    'rasterio.warp.Resampling',
    'rasterio.windows',
    'rasterio.crs',
    'matplotlib',
    'matplotlib.pyplot',
    'numpy',
    'numpy.ma',
    'cached_property',
    'pyproj',
    'cachetools',
    'shapely',
    'shapely.geometry',
    'shapely.geos',
    'shapely.ops',
    'shapely.wkt',
    'yaml',
    'affine',
    'tqdm'
]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)
