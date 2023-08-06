#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#    Wisteria Copyright (C) 2021 suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of Wisteria.
#    Wisteria is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Wisteria is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Wisteria.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
    Wisteria project : wisteria/globs.py

    Global definitions.
    ___________________________________________________________________________

    o  ARGS

    o  CWC_MODULES

    o  DATA
    o  UNAVAILABLE_DATA

    o  DEBUG_CONSOLEWIDTH

    o  DEFAULT_CONFIGFILE_NAME
    o  DEFAULT_CONFIGFILE_URL

    o  DISCARDED_DATA
    o  DISCARDED_SERIALIZERS

    o  RICHFILECONSOLE
    o  RICHFILECONSOLE_FILEOBJECT

    o  MODULES

    o  OUTPUT

    o  PLANNED_TRANSCODINGS

    o  PLATFORM_SYSTEM

    o  PROGRESSBAR_LENGTH

    o  REGEX_CMP

    o  REPORTFILE_PATH

    o  REPORT_SHORTCUTS

    o  RICHCONSOLE

    o  SERIALIZERS

    o  STR2REPORTSECTION_KEYS

    o  TIMEITNUMBER

    o  TMPFILENAME

    o  UNITS

    o  VERBOSITY_MINIMAL
    o  VERBOSITY_NORMAL
    o  VERBOSITY_DETAILS
    o  VERBOSITY_DEBUG


The following variables depend on previously defined variables,
hence their location at the end of this list:

    o  DEFAULT_EXPORTREPORT_FILENAME
           (initialized by get_default_exportreport_filename())
    o  DEFAULT_REPORTFILE_NAME
           (initialized by get_default_reportfile_name())
    o  GRAPHS_GENERIC_FILENAME
           (initialized by get_graphs_filename())
    o  GRAPHS_DESCRIPTION
           (initialized by get_graphs_description())


    Function used to create exportreport file name:
    o  get_exportreport_filename(basename)
"""
import os.path
import re


# command line arguments
# will be set to argparse.ArgumentParser(...).parse_args()
ARGS = None

# (pimydoc)cwc modules names
# ⋅
# ⋅cwc modules names start with the "wisteria.cwc" string (cf is_a_cwc_name())
# ⋅
# ⋅moduleininame        : e.g. "wisteria.cwc.pgnreader.cwc_default.chessgames"
# ⋅modulefullrealname   : e.g. "wisteria.cwc.pgnreader.cwc_default.ChessGames"
# ⋅waemodulename        : e.g. "wisteria.cwc.pgnreader.works_as_expected"
# ⋅classname            : e.g. "ChessGames" (NOT "chessgames")
# ⋅modulerealname       : e.g. "wisteria.cwc.pgnreader.cwc_default"
# ⋅
# ⋅- `moduleininame` are defined in config file;
# ⋅- conversion from `moduleininame` to `modulefullrealname` is defined in
# ⋅  data.py:DATA and is made by function
# ⋅  cwc_utils.py:moduleininame_to_modulefullrealname()
# ⋅- conversion from `modulefullrealname` to `modulerealname` is made by
# ⋅  function cwc_utils.py:modulefullrealname_to_modulerealname()
# ⋅- DATA keys (for cwc modules) use `moduleininame`, NOT `modulefullrealname`
CWC_MODULES = (
    ("wisteria.cwc.pgnreader.cwc_default.chessgames",
     "wisteria.cwc.pgnreader.cwc_default.ChessGames"),
    ("wisteria.cwc.pgnreader.cwc_iaswn.chessgames",
     "wisteria.cwc.pgnreader.cwc_iaswn.ChessGames"),

    ("wisteria.cwc.simple.cwc_default.simpleclass",
     "wisteria.cwc.simple.cwc_default.SimpleClass"),
    ("wisteria.cwc.simple.cwc_iaswn.simpleclass",
     "wisteria.cwc.simple.cwc_iaswn.SimpleClass"),
)

# dict storing all data used by the program.
#
# (pimydoc)DATA format
# ⋅Initialized by data.py::init_data()
# ⋅
# ⋅- for Python basic types, DATA values are the real value:
# ⋅    e.g. DATA["bool/false"] = False
# ⋅- for cwc modules, DATA keys are the ini name (not the real name)
# ⋅  and DATA values are the real name:
# ⋅    e.g. DATA["wisteria.cwc.pgnreader.iaswn.ChessGames"] =
# ⋅        "wisteria.cwc.pgnreader.iaswn.chessgames"
# ⋅- for third party types, DATA values are the real value:
# ⋅    e.g. DATA["dateutil(parser.parse)"] = dateutil.parser.parse("2021-03-04")
DATA = {}
# dict storing all data that the program can't use.
#
# * format: UNAVAILABLE_DATA[(str)data name] = string explaining why it's unavailable
# * initialized by data.py::init_data() and updated by data.py::check()
UNAVAILABLE_DATA = {}

# maximal console width used to display some debug messages:
DEBUG_CONSOLEWIDTH = 70

# default name for the config file.
DEFAULT_CONFIGFILE_NAME = "wisteria.ini"
# url of the default config file:
DEFAULT_CONFIGFILE_URL = "https://raw.githubusercontent.com/suizokukan/wisteria/main/wisteria.ini"

# initialized by init_planned_transcodings():
DISCARDED_DATA = []
DISCARDED_SERIALIZERS = []

# value: rich.console.Console(file=...)
RICHFILECONSOLE = None
# Both variables are initialized by main.py()
RICHFILECONSOLE_FILEOBJECT = None

# imported serializers modules
MODULES = {}

# value of the --output argument
#  initialized by parse_output_argument(--output string)
# (pimydoc)OUTPUT format
# ⋅        ((bool)output to the console ?,
# ⋅         (bool)output to the reportfile ?,
# ⋅         (str)reportfile open mode = 'a' or 'w',
# ⋅         (str)reportfile name,
# ⋅        )
OUTPUT = []

# (pimydoc)PLANNED_TRANSCODINGS
# ⋅a list:
# ⋅    - (str)serializer,
# ⋅    - (int)len(serializers)
# ⋅    - (int)len(dataobjs)
# ⋅
# ⋅Initialized by results.py:init_planned_transcodings()
PLANNED_TRANSCODINGS = []

# = platform.system()
PLATFORM_SYSTEM = None

# progress bar length (in characters)
# 'None' is an accepted value and extends the length of the bar
# to the entire width of the terminal.
PROGRESSBAR_LENGTH = None

# (pimydoc)command line help for --cmp(full version)
# ⋅Comparisons details.
# ⋅
# ⋅(I) serializers
# ⋅Test one serializer alone(1) or one serializer against another serializer(2) or
# ⋅a serializer against all serializers(3) or all serializers(4) together.
# ⋅
# ⋅    (1) --cmp="json"
# ⋅    (2) --cmp="json vs pickle"
# ⋅    (3) --cmp="json vs all"
# ⋅    (4) --cmp="all vs all"
# ⋅
# ⋅(II) data types:
# ⋅Instead of 'cwc' (=compare what's comparable)(a) you may want to test all data types
# ⋅but cwc(b) or data types defined in the config file(c) or absolutely all data types(d).
# ⋅
# ⋅    (a) --cmp="json vs pickle (cwc)"
# ⋅    (b) --cmp="json vs pickle (allbutcwc)"
# ⋅    (c) --cmp="json vs pickle (ini)"
# ⋅    (d) --cmp="json vs pickle (all)"
# ⋅
# ⋅NB: You may use 'vs' as well as 'against', as in:
# ⋅    --cmp="json vs pickle (cwc)"
# ⋅NB: globs.py::REGEX_CMP defines exactly the expected format
# regex used to parse the --cmp argument string
REGEX_CMP = re.compile(r"^\s*(?P<serializer1>[^\s\(\)]+)"
                       r"((\svs\s|\sversus\s|\sagainst\s)(?P<serializer2>[^\s\(\)]+))?"
                       r"(\s*\((?P<cmpdata>all|cwc|allbutcwc|ini)\))?\s*$")

# File to report path
REPORTFILE_PATH = "."

# REPORT_SHORTCUTS has two goals:
# (1) it translates a simple, human-readable string into a list of section parts
# (2) it gives all the accepted keywords that --report may understand.
REPORT_SHORTCUTS = {
    "bestof": "B1c;C2b;C2c;graphs;",
    "full": "titles;A;B;C;D1a;graphs;",
    "full+": "titles;A;B;C;D1b;graphs;",
    "full_debug": "titles;A;B;C;D;graphs;",
    "glance": "titles;B1b;C1a;C1b;C2a;C2b;C2c;graphs;",
    "laconic": "C;graphs;",
    "minimal": "C2c;graphs;",
    "none": "",
    }

# value: None or rich.console.Console()
RICHCONSOLE = None

# dict storing all serializers used by the program.
#
# * format: SERIALIZERS[(str)serializer name] = SerializerData object
# * initialized by serializers.py::init_serializers()
SERIALIZERS = {}
# dict storing all serializers that the program can't use.
#
# * format: UNAVAILABLE_SERIALIZERS[(str)serializer name] = SerializerData object
# * initialized by serializers.py::init_serializers()
UNAVAILABLE_SERIALIZERS = {}

#  globs.py:STR2REPORTSECTION_KEYS should be nothing but STR2REPORTSECTION.keys()
#
# Why those two variables ?
# Because the program needs to know STR2REPORTSECTION.keys() at step A
# before STR2REPORTSECTION has been initialized. Since this initialization
# requires modules that can't fit step A, we have to create a distinct list
# of keys.
#
# check_str2reportsection_keys() checks that keys from STR2REPORTSECTION and
# from STR2REPORTSECTION_KEYS are exactly the same.
STR2REPORTSECTION_KEYS = (
    'titles',
    'graphs',
    'A',
    'A1',
    'A2',
    'A3',
    'A4',
    'A5',
    'B',
    'B1',
    'B1a',
    'B1b',
    'B1c',
    'B1d',
    'B2',
    'B2a',
    'B2b',
    'B3',
    'C',
    'C1',
    'C1a',
    'C1b',
    'C2',
    'C2a',
    'C2b',
    'C2c',
    'D',
    'D1',
    'D1a',
    'D1b',
)

# number of times each serializer is called
TIMEITNUMBER = 1

# temp file default name
TMPFILENAME = "wisteria.tmp"

# units used in this project
UNITS = {'time': 'seconds',
         'string length': 'characters',
         'memory': 'bytes',
         }

# values defined for --verbosity:
VERBOSITY_MINIMAL = 0
VERBOSITY_NORMAL = 1
VERBOSITY_DETAILS = 2
VERBOSITY_DEBUG = 3


# =============================================================================
#
# The following variables depend on previously defined variables,
# hence their location at the end of this list.
#
# =============================================================================
def get_default_exportreport_filename():
    """
        get_default_exportreport_filename()

        Return the value expected for DEFAULT_EXPORTREPORT_FILENAME
        _______________________________________________________________________

        RETURNED VALUE: (str)a value for DEFAULT_EXPORTREPORT_FILENAME
    """
    return os.path.join(REPORTFILE_PATH, "exportreport.md")


def get_default_reportfile_name():
    """
        get_default_reportfile_name()

        Return the value expected for DEFAULT_REPORTFILE_NAME
        _______________________________________________________________________

        RETURNED VALUE: (str)a value for DEFAULT_REPORTFILE_NAME
    """
    return os.path.join(REPORTFILE_PATH, "report.txt")


def get_exportreport_filename(basename):
    """
        get_exportreport_filename()

        Return the value expected for the exportreport file.
        _______________________________________________________________________

        PARAMETER: (str)the basename of the exportreport file.

        RETURNED VALUE: (str)a value for exportreport file.
    """
    return os.path.join(REPORTFILE_PATH,
                        basename)


def get_graphs_filename():
    """
        get_graphs_filename()

        Return the value expected for GRAPHS_GENERIC_FILENAME
        _______________________________________________________________________

        RETURNED VALUE: (str)a value for GRAPHS_GENERIC_FILENAME
    """
    return os.path.join(REPORTFILE_PATH, "report__SUFFIX__.png")


def get_graphs_description():
    """
        get_graphs_description()

        Return the value expected for GRAPHS_DESCRIPTION
        _______________________________________________________________________

        RETURNED VALUE: (tupl)a value for GRAPHS_DESCRIPTION

            (pimydoc)GRAPHS_DESCRIPTION format
            ⋅Use GRAPHS_DESCRIPTION to store the description of each graph created by the
            ⋅report; each description is passed to hbar2png(). Note that
            ⋅len(GRAPHS_DESCRIPTION) gives the number of graphs to be created.
            ⋅
            ⋅- (str)attribute   : hbar2png will read results.hall[attribute]
            ⋅- (str)fmtstring   : format string to be applied to each value when printed
            ⋅                     on the graph; e.g. '{0}' or '{0:.1f}'
            ⋅- (int)value_coeff : each value will be multiplied by this number
            ⋅- (str)unit        : x unit
            ⋅- (str)title       : graph title
            ⋅- (str)filename    : file name to be written
    """
    return (('encoding_time', "{0:.3f}", 1, UNITS['time'], 'Slowness',
             GRAPHS_GENERIC_FILENAME.replace("__SUFFIX__", "1")),
            ('mem_usage', "{0}", 1, UNITS['memory'], 'Memory Usage',
             GRAPHS_GENERIC_FILENAME.replace("__SUFFIX__", "2")),
            ('encoding_strlen', "{0}", 1, UNITS['string length'], 'Encoded String Length',
             GRAPHS_GENERIC_FILENAME.replace("__SUFFIX__", "3")),
            ('reversibility', "{0:.1f}", 100, "%", 'Coverage data (Reversibility)',
             GRAPHS_GENERIC_FILENAME.replace("__SUFFIX__", "4")),)


DEFAULT_EXPORTREPORT_FILENAME = get_default_exportreport_filename()
DEFAULT_REPORTFILE_NAME = get_default_reportfile_name()

# generic name for graphs filenames:
#   'generic' since this string contains a '__SUFFIX__' substring to be replaced.
GRAPHS_GENERIC_FILENAME = get_graphs_filename()

# (pimydoc)GRAPHS_DESCRIPTION format
# ⋅Use GRAPHS_DESCRIPTION to store the description of each graph created by the
# ⋅report; each description is passed to hbar2png(). Note that
# ⋅len(GRAPHS_DESCRIPTION) gives the number of graphs to be created.
# ⋅
# ⋅- (str)attribute   : hbar2png will read results.hall[attribute]
# ⋅- (str)fmtstring   : format string to be applied to each value when printed
# ⋅                     on the graph; e.g. '{0}' or '{0:.1f}'
# ⋅- (int)value_coeff : each value will be multiplied by this number
# ⋅- (str)unit        : x unit
# ⋅- (str)title       : graph title
# ⋅- (str)filename    : file name to be written
GRAPHS_DESCRIPTION = get_graphs_description()
