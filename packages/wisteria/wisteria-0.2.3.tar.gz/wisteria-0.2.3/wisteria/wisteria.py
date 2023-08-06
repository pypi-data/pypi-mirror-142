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
    Wisteria project : wisteria/wisteria.py

    Main file and main entry point into the project.

    (pimydoc)code structure
    ⋅step A: command line arguments, --help message
    ⋅- (A/00) minimal internal imports
    ⋅- (A/01) command line parsing
    ⋅
    ⋅step B: initializations & --checkup
    ⋅- (B/02) normal imports & PLATFORM_SYSTEM initialization
    ⋅- (B/03) wisteria.globs.ARGS initialization
    ⋅- (B/04) a special case: if no argument has been given, we explicit the default values
    ⋅- (B/05) --output string/OUTPUT+RICHCONSOLE init
    ⋅- (B/06) reportfile opening: update REPORTFILE_PATH & co.
    ⋅- (B/07) msgxxx() functions can be used
    ⋅- (B/08) check STR2REPORTSECTION_KEYS and STR2REPORTSECTION
    ⋅- (B/09) project name & version
    ⋅- (B/10) ARGS.report interpretation
    ⋅- (B/11) exit handler installation
    ⋅- (B/12) serializers import
    ⋅- (B/13) temp file opening
    ⋅- (B/14) known data init (to be placed after 'temp file opening')
    ⋅- (B/15) checkup
    ⋅- (B/16) informations about the current machine
    ⋅- (B/17) download default config file
    ⋅
    ⋅step C: main()
    ⋅- (C/18) call to main()
    ⋅       - (C/18.1) main(): debug messages
    ⋅       - (C/18.2) main(): cmp string interpretation
    ⋅       - (C/18.3) main(): config file reading
    ⋅       - (C/18.4) main(): PLANNED_TRANSCODINGS initialization
    ⋅       - (C/18.5) main(): results computing
    ⋅       - (C/18.6) main(): report
    ⋅
    ⋅step D: exit_handler()
    ⋅- (D/01) exported report
    ⋅- (D/02) closing and removing of tempfile
    ⋅- (D/03) closing wisteria.globs.RICHFILECONSOLE_FILEOBJECT
    ⋅- (D/04) reset console cursor
    ⋅

    (pimydoc)exit codes
    ⋅These exit codes try to take into account the standards, in particular this
    ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
    ⋅
    ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
    ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
    ⋅used for this project; these constants are only defined for Linux systems
    ⋅and this project aims Windows/OSX systems.
    ⋅
    ⋅*    0: normal exit code
    ⋅*       normal exit code after --help/--help2
    ⋅*       normal exit code after --checkup
    ⋅*       normal exit code after --downloadconfigfile
    ⋅*       normal exit code after --mymachine
    ⋅*       normal exit code (no data to handle)
    ⋅*       normal exit code (no serializer to handle)
    ⋅*    1: error, given config file can't be read (missing or ill-formed file)
    ⋅*    2: error, ill-formed --cmp string
    ⋅*    3: error, ill-formed --output string
    ⋅*    4: error, missing required module
    ⋅*    5: error: an inconsistency between the data has been detected
    ⋅*    6: error: can't open/create report file
    ⋅*  100: internal error, data can't be loaded
    ⋅*  101: internal error, an error occured while computing the results
    ⋅*  102: internal error, an error occured in main()
    ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
    ___________________________________________________________________________

    o  check_str2reportsection_keys()
    o  exit_handler()
    o  checkup()
    o  main()
"""
# All the imports are deliberately not placed at the beginning of the file
# so that the --help message may be printed even if all required packages are
# not installed.
import argparse
import atexit
import os
import os.path
import sys

# =============================================================================
# (A/00) minimal internal imports
# =============================================================================
# All the imports are deliberately not placed at the beginning of the file
# so that the --help message may be printed even if all required packages are
# not installed.
#   pylint: disable=wrong-import-position
#   pylint: disable=wrong-import-order
from wisteria.utils import normpath, get_python_version
from wisteria.aboutproject import __projectname__, __version__
from wisteria.helpmsg import help_graphsfilenames, help_cmdline_helpdescription
from wisteria.helpmsg import help_cmdline_filter, help_cmdline_exportreport, help_cmdline_output
from wisteria.helpmsg import help_cmdline_cmp, help_cmdline_report
from wisteria.globs import DEFAULT_REPORTFILE_NAME
from wisteria.globs import VERBOSITY_MINIMAL, VERBOSITY_NORMAL, VERBOSITY_DETAILS, VERBOSITY_DEBUG
from wisteria.globs import REPORT_SHORTCUTS
from wisteria.globs import DEFAULT_CONFIGFILE_NAME
from wisteria.globs import STR2REPORTSECTION_KEYS


# =============================================================================
# (A/01) command line parsing
# =============================================================================
PARSER = \
    argparse.ArgumentParser(
        description='Comparisons of different Python serializers. '
        f'{help_cmdline_helpdescription()}',
        epilog=f"{__projectname__}: {__version__}",
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

PARSER.add_argument(
    '--cfgfile',
    action='store',
    default=DEFAULT_CONFIGFILE_NAME,
    help="Config file to be read. Use --downloadconfigfile "
         "to download the default config file.")

PARSER.add_argument(
    '--checkup',
    action='store_true',
    default=False,
    help="Show available serializers and data objects, try to read current config file and exit. "
    "Use --verbosity to change the quantity of displayed informations.")

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
PARSER.add_argument(
    '--cmp',
    action='store',
    default="all vs all",
    help=help_cmdline_cmp(details=False))

PARSER.add_argument(
    '--downloadconfigfile',
    action='store_true',
    help="Download default config file and exit. See --cfgfile to use a specific config file.")

# (pimydoc)command line help for --exportreport(full version)
# ⋅Export report by creating a new file in which
# ⋅both report text and graphics are put together.
# ⋅- default value: "no export", i.e. no exported report file
# ⋅- otherwise 'md' is the only value or the only acceptable start string
# ⋅  since md format is the only known format for exported report;
# ⋅  you may add the exported report filename after '=',
# ⋅  e.g. 'md=myfile.md';
# ⋅       'md' (in this case the default file name will be used)
# ⋅  the default filename is '$DEFAULT_EXPORTREPORT_FILENAME' . "
# ⋅  Please note that graphs will not be added to the exported file if
# ⋅  --checkup/--downloadconfigfile/--mymachine is set.
PARSER.add_argument(
    '--exportreport',
    action='store',
    default='no export',
    help=help_cmdline_exportreport(details=False))

# (pimydoc)command line help for --filter(full version)
# ⋅The --filter argument allows to select only some serializers or
# ⋅data objects. Currently only two values are accepted:
# ⋅* either a null string (--filter=""): all serializers/data objects are
# ⋅  used;
# ⋅* either 'data:oktrans_only' (--filter='data:oktrans_only'): in this case,
# ⋅  only the objects that can be successfully transcoded are kept;
PARSER.add_argument(
    '--filter',
    action='store',
    default="",
    help=help_cmdline_filter(details=False))

PARSER.add_argument(
    '--help', '-h',
    action='help',
    help="Show this help message and exit. Try --help2 too.")

PARSER.add_argument(
    '--help2',
    action='store_true',
    help="Show detailed help messages about some command line arguments and exit.")

PARSER.add_argument(
    '--mute',
    action='store_true',
    default=False,
    help="Warning: debug/profile only, not normally to be used. "
    "Prevent any console or file output. "
    "If set, set the value of --verbosity to 'minimal' and "
    "--report to 'none'.")

# MEMOVERUSEPARSER.add_argument(
# MEMOVERUSE    '--memoveruse',
# MEMOVERUSE    action='store',
# MEMOVERUSE    default='none',
# MEMOVERUSE    choices=('none', 'Python', 'C++', 'Python/C++'),
# MEMOVERUSE    help="(debug/profile, not normally to be used) Alloc extra memory objects, "
# MEMOVERUSE    "either from Python (='Python') "
# MEMOVERUSE    "either from C++ (='C++') "
# MEMOVERUSE    "either from Python and C++ (='Python/C++') "
# MEMOVERUSE    "Why ? Just to see if memory profilers detect these allocations.")

PARSER.add_argument(
    '--mymachine',
    action='store_true',
    default=False,
    help="Display informations about the current machine and exit. "
    "Use --verbosity to change the quantity of displayed informations.")

# (pimydoc)command line help for --output(full version)
# ⋅A string like '[console;][reportfile/w/a]=subdirectory/myreportfilename'
# ⋅
# ⋅* 'console':
# ⋅  - 'console' : if you want to write output messages to the console
# ⋅
# ⋅* 'reportfile='
# ⋅  - either a simple string like 'report.txt'
# ⋅  - either a string containing 'DATETIME'; in this case, 'DATETIME' will
# ⋅    be replaced by datetime.datetime.now().strftime("%Y-%m-%d.%H.%M.%S");
# ⋅    e.g. "report_DATETIME.txt" would become something like
# ⋅         "report_2021-12-31.23.59.59.txt"
# ⋅  - either a string containing 'TIMESTAMP'; in this case, 'TIMESTAMP' will
# ⋅    be replaced by str(int(time.time()))
# ⋅      e.g. "report_DATETIME.txt" would become something like
# ⋅           "report_1635672267.txt"
# ⋅
# ⋅BEWARE: The path to the report file must exist; e.g. if ./path/ doesn't
# ⋅exist you can't write:
# ⋅     --output="console;reportfile/w=path/myreportfile"
PARSER.add_argument(
    '--output',
    action='store',
    default=f'console;reportfile/w={DEFAULT_REPORTFILE_NAME}',
    help=help_cmdline_output(details=False))

# (pimydoc)command line help for --report(full version)
# ⋅Report format:
# ⋅you may use one of the special keywords ($REPORT_SHORTCUTS_KEYS)
# ⋅or a list of section parts, e.g. 'A1;B1a;'.
# ⋅You may use shorter strings like 'B' (=B1+B2, i.e. B1a+B1b...+B2a+B2b...)
# ⋅or like 'B1' (=B1a+B1b+B1c).
# ⋅Accepted section parts are
# ⋅$STR2REPORTSECTION_KEYS .
# ⋅More informations in the documentation.
# ⋅Please notice that --verbosity has no effect upon --report.
# ⋅See --help2 for more informations.
PARSER.add_argument(
    '--report',
    action='store',
    default="glance",
    help=help_cmdline_report(details=False))

PARSER.add_argument(
    '--verbosity',
    type=int,
    default=VERBOSITY_NORMAL,
    choices=(VERBOSITY_MINIMAL,
             VERBOSITY_NORMAL,
             VERBOSITY_DETAILS,
             VERBOSITY_DEBUG),
    help="Verbosity level: 0(=minimal), 1(=normal), 2(=normal+details), 3(=debug). "
    "Please notice that --verbosity has no effect upon --report. See also the --mute argument.")

PARSER.add_argument(
    '--version', '-v',
    action='version',
    version=f"{__projectname__} {__version__}",
    help="Show the version and exit.")

ARGS = PARSER.parse_args()


if ARGS.help2:
    print("============")
    print("About --cmp:")
    print("============")
    print(help_cmdline_cmp(details=True))
    print()
    print("=====================")
    print("About --exportreport:")
    print("=====================")
    print(help_cmdline_exportreport(details=True))
    print()
    print("===============")
    print("About --filter:")
    print("===============")
    print(help_cmdline_filter(details=True))
    print()
    print("===============")
    print("About --output:")
    print("===============")
    print(help_cmdline_output(details=True))
    # (pimydoc)exit codes
    # ⋅These exit codes try to take into account the standards, in particular this
    # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
    # ⋅
    # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
    # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
    # ⋅used for this project; these constants are only defined for Linux systems
    # ⋅and this project aims Windows/OSX systems.
    # ⋅
    # ⋅*    0: normal exit code
    # ⋅*       normal exit code after --help/--help2
    # ⋅*       normal exit code after --checkup
    # ⋅*       normal exit code after --downloadconfigfile
    # ⋅*       normal exit code after --mymachine
    # ⋅*       normal exit code (no data to handle)
    # ⋅*       normal exit code (no serializer to handle)
    # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
    # ⋅*    2: error, ill-formed --cmp string
    # ⋅*    3: error, ill-formed --output string
    # ⋅*    4: error, missing required module
    # ⋅*    5: error: an inconsistency between the data has been detected
    # ⋅*    6: error: can't open/create report file
    # ⋅*  100: internal error, data can't be loaded
    # ⋅*  101: internal error, an error occured while computing the results
    # ⋅*  102: internal error, an error occured in main()
    # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
    sys.exit(0)

# =============================================================================
# (B/02) normal imports & PLATFORM_SYSTEM initialization
# =============================================================================
from wisteria.utils import get_missing_required_internal_modules  # noqa
from wisteria.reprfmt import fmt_projectversion, fmt_nounplural  # noqa
MISSING_REQUIRED_MODULES = get_missing_required_internal_modules()
if MISSING_REQUIRED_MODULES:
    # Please note that we don't use rprint() here since rich module has not
    # been yet imported.
    print(fmt_projectversion(add_timestamp=True))
    print("The program can't be executed. "
          "At least one required module is missing, namely",
          " and ".join(MISSING_REQUIRED_MODULES),
          ".")
    # (pimydoc)exit codes
    # ⋅These exit codes try to take into account the standards, in particular this
    # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
    # ⋅
    # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
    # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
    # ⋅used for this project; these constants are only defined for Linux systems
    # ⋅and this project aims Windows/OSX systems.
    # ⋅
    # ⋅*    0: normal exit code
    # ⋅*       normal exit code after --help/--help2
    # ⋅*       normal exit code after --checkup
    # ⋅*       normal exit code after --downloadconfigfile
    # ⋅*       normal exit code after --mymachine
    # ⋅*       normal exit code (no data to handle)
    # ⋅*       normal exit code (no serializer to handle)
    # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
    # ⋅*    2: error, ill-formed --cmp string
    # ⋅*    3: error, ill-formed --output string
    # ⋅*    4: error, missing required module
    # ⋅*    5: error: an inconsistency between the data has been detected
    # ⋅*    6: error: can't open/create report file
    # ⋅*  100: internal error, data can't be loaded
    # ⋅*  101: internal error, an error occured while computing the results
    # ⋅*  102: internal error, an error occured in main()
    # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
    sys.exit(4)

# All the imports are deliberately not placed at the beginning of the file
# so that the --help message may be printed even if all required packages are
# not installed.
import platform  # noqa
import rich.console  # noqa
from rich import print as rprint  # noqa

import wisteria.globs  # noqa
wisteria.globs.PLATFORM_SYSTEM = platform.system()

from wisteria.globs import TMPFILENAME  # noqa
from wisteria.report import report, partial_report__data, partial_report__serializers  # noqa
from wisteria.report import open_reportfile  # noqa
from wisteria.results import init_planned_transcodings, compute_results  # noqa
from wisteria.utils import trytoimport  # noqa
import wisteria.serializers  # noqa
import wisteria.data  # noqa
from wisteria.wisteriaerror import WisteriaError  # noqa
from wisteria.msg import msginfo, msgwarning, msgerror, msgdebug, msgreport, msgreporttitle  # noqa
from wisteria.cmdline_output import parse_output_argument  # noqa
from wisteria.cmdline_cmp import read_cmpstring  # noqa
from wisteria.cmdline_mymachine import mymachine  # noqa
from wisteria.cfgfile import read_cfgfile, downloadconfigfile  # noqa
from wisteria.serializers import func_serialize  # noqa
from wisteria.globs import get_graphs_filename, get_graphs_description  # noqa
from wisteria.globs import get_exportreport_filename, get_default_exportreport_filename  # noqa
from wisteria.globs import get_default_reportfile_name  # noqa


# =============================================================================
# (B/03) wisteria.globs.ARGS initialization
# =============================================================================
wisteria.globs.ARGS = ARGS


# ====================================================================================
# (B/04) a special case: if no argument has been given, we explicit the default values
# ====================================================================================
# a special case: if no argument has been given, we modify the output
if len(sys.argv) == 1:
    # no RICHCONSOLE for the moment, hence the call to rprint().
    rprint(
        f"[bold]No argument was passed to {__projectname__}: "
        "by default, "
        f"--verbosity is set to '{wisteria.globs.ARGS.verbosity}', "
        f"--report to '{wisteria.globs.ARGS.report}', "
        f"and --output is equal to '{wisteria.globs.ARGS.output}' ."
        "[/bold]")


# =============================================================================
# (B/05) --output string/OUTPUT+RICHCONSOLE init
# =============================================================================
if wisteria.globs.ARGS.mute:
    # (pimydoc)OUTPUT format
    # ⋅        ((bool)output to the console ?,
    # ⋅         (bool)output to the reportfile ?,
    # ⋅         (str)reportfile open mode = 'a' or 'w',
    # ⋅         (str)reportfile name,
    # ⋅        )
    wisteria.globs.OUTPUT = False, False, "a", DEFAULT_REPORTFILE_NAME
else:
    # (pimydoc)OUTPUT format
    # ⋅        ((bool)output to the console ?,
    # ⋅         (bool)output to the reportfile ?,
    # ⋅         (str)reportfile open mode = 'a' or 'w',
    # ⋅         (str)reportfile name,
    # ⋅        )
    PARSING_SUCCESS, *wisteria.globs.OUTPUT = parse_output_argument(wisteria.globs.ARGS.output)
    if not PARSING_SUCCESS:
        # no report(=log) available, hence the use of rprint():
        rprint("[bold red]Ill-formed --output string. The program has to stop.[/bold red]")
        # (pimydoc)exit codes
        # ⋅These exit codes try to take into account the standards, in particular this
        # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
        # ⋅
        # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
        # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
        # ⋅used for this project; these constants are only defined for Linux systems
        # ⋅and this project aims Windows/OSX systems.
        # ⋅
        # ⋅*    0: normal exit code
        # ⋅*       normal exit code after --help/--help2
        # ⋅*       normal exit code after --checkup
        # ⋅*       normal exit code after --downloadconfigfile
        # ⋅*       normal exit code after --mymachine
        # ⋅*       normal exit code (no data to handle)
        # ⋅*       normal exit code (no serializer to handle)
        # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
        # ⋅*    2: error, ill-formed --cmp string
        # ⋅*    3: error, ill-formed --output string
        # ⋅*    4: error, missing required module
        # ⋅*    5: error: an inconsistency between the data has been detected
        # ⋅*    6: error: can't open/create report file
        # ⋅*  100: internal error, data can't be loaded
        # ⋅*  101: internal error, an error occured while computing the results
        # ⋅*  102: internal error, an error occured in main()
        # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
        sys.exit(3)

    # By default, wisteria.globs.RICHCONSOLE is set to None.
    if wisteria.globs.OUTPUT[0]:
        wisteria.globs.RICHCONSOLE = rich.console.Console()

# =============================================================================
# (B/06) reportfile opening: update REPORTFILE_PATH & co.
# =============================================================================
# It would be great to use something like:
#   with open(...) as wisteria.globs.RICHFILECONSOLE_FILEOBJECT:
# but it's not possible here. Please notice that we check the closing of this
# file in exit handler.
#   pylint: disable=consider-using-with
wisteria.globs.RICHFILECONSOLE_FILEOBJECT, wisteria.globs.REPORTFILE_PATH = open_reportfile()
# what follows depends on wisteria.globs.REPORTFILE_PATH:
wisteria.globs.DEFAULT_REPORTFILE_NAME = get_default_reportfile_name()
wisteria.globs.GRAPHS_GENERIC_FILENAME = get_graphs_filename()
wisteria.globs.GRAPHS_DESCRIPTION = get_graphs_description()
wisteria.globs.DEFAULT_EXPORTREPORT_FILENAME = get_default_exportreport_filename()


if wisteria.globs.RICHFILECONSOLE_FILEOBJECT is None:
    # (pimydoc)exit codes
    # ⋅These exit codes try to take into account the standards, in particular this
    # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
    # ⋅
    # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
    # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
    # ⋅used for this project; these constants are only defined for Linux systems
    # ⋅and this project aims Windows/OSX systems.
    # ⋅
    # ⋅*    0: normal exit code
    # ⋅*       normal exit code after --help/--help2
    # ⋅*       normal exit code after --checkup
    # ⋅*       normal exit code after --downloadconfigfile
    # ⋅*       normal exit code after --mymachine
    # ⋅*       normal exit code (no data to handle)
    # ⋅*       normal exit code (no serializer to handle)
    # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
    # ⋅*    2: error, ill-formed --cmp string
    # ⋅*    3: error, ill-formed --output string
    # ⋅*    4: error, missing required module
    # ⋅*    5: error: an inconsistency between the data has been detected
    # ⋅*    6: error: can't open/create report file
    # ⋅*  100: internal error, data can't be loaded
    # ⋅*  101: internal error, an error occured while computing the results
    # ⋅*  102: internal error, an error occured in main()
    # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
    sys.exit(6)

wisteria.globs.RICHFILECONSOLE = \
    rich.console.Console(file=wisteria.globs.RICHFILECONSOLE_FILEOBJECT)


# =============================================================================
# (B/07) msgxxx() functions can be used
# =============================================================================

# =============================================================================
# (B/08) check STR2REPORTSECTION_KEYS and STR2REPORTSECTION
# =============================================================================
def check_str2reportsection_keys():
    """
        check_str2reportsection_keys()

        Check that all keys in STR2REPORTSECTION_KEYS are defined
        in STR2REPORTSECTION, and vice-versa.
        _______________________________________________________________________

        RETURNED VALUE: (bool)True if all keys are well defined.
    """
    success = True

    for key in STR2REPORTSECTION_KEYS:
        if key not in wisteria.report.STR2REPORTSECTION:
            success = False
            msgerror(f"(ERRORID023) '{key}' is a key defined in STR2REPORTSECTION_KEYS "
                     "but not in STR2REPORTSECTION.")
    for key in wisteria.report.STR2REPORTSECTION:
        if key not in STR2REPORTSECTION_KEYS:
            success = False
            msgerror(f"(ERRORID024) '{key}' is a key defined in STR2REPORTSECTION "
                     "but not in STR2REPORTSECTION_KEYS.")

    return success


if not check_str2reportsection_keys():
    # (pimydoc)exit codes
    # ⋅These exit codes try to take into account the standards, in particular this
    # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
    # ⋅
    # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
    # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
    # ⋅used for this project; these constants are only defined for Linux systems
    # ⋅and this project aims Windows/OSX systems.
    # ⋅
    # ⋅*    0: normal exit code
    # ⋅*       normal exit code after --help/--help2
    # ⋅*       normal exit code after --checkup
    # ⋅*       normal exit code after --downloadconfigfile
    # ⋅*       normal exit code after --mymachine
    # ⋅*       normal exit code (no data to handle)
    # ⋅*       normal exit code (no serializer to handle)
    # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
    # ⋅*    2: error, ill-formed --cmp string
    # ⋅*    3: error, ill-formed --output string
    # ⋅*    4: error, missing required module
    # ⋅*    5: error: an inconsistency between the data has been detected
    # ⋅*    6: error: can't open/create report file
    # ⋅*  100: internal error, data can't be loaded
    # ⋅*  101: internal error, an error occured while computing the results
    # ⋅*  102: internal error, an error occured in main()
    # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
    sys.exit(5)


# =============================================================================
# (B/09) project name & version
# =============================================================================
if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
    msginfo(fmt_projectversion(add_timestamp=True))
    msgreport(f"Running on Python {get_python_version()}")

# =============================================================================
# (B/10) ARGS.report interpretation
# =============================================================================
if wisteria.globs.ARGS.mute:
    wisteria.globs.ARGS.report = ""
    wisteria.globs.ARGS.verbosity = VERBOSITY_MINIMAL
    wisteria.globs.ARGS.output = ""
elif wisteria.globs.ARGS.report in REPORT_SHORTCUTS:
    if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
        msginfo(f"--report '{wisteria.globs.ARGS.report}' "
                f"interpreted as '{REPORT_SHORTCUTS[wisteria.globs.ARGS.report]}'.")
    wisteria.globs.ARGS.report = REPORT_SHORTCUTS[wisteria.globs.ARGS.report]
elif not wisteria.globs.ARGS.report.endswith(";"):
    wisteria.globs.ARGS.report += ";"
    if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
        msginfo("--report: semicolon added at the end; "
                f"--report is now '{wisteria.globs.ARGS.report}'.")

if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
    msgdebug("From now --report (wisteria.globs.ARGS.report) is set "
             f"to '{wisteria.globs.ARGS.report}'.")

# MEMOVERUSEif wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
# MEMOVERUSE    msgdebug(f"--memoveruse has been set to '{wisteria.globs.ARGS.memoveruse}' .")


# =============================================================================
# (B/11) exit handler
# =============================================================================
def exit_handler():
    """
        exit_handler()

        Remove the tmp file if it exists and close the file console file object.
    """
    # =============================================================================
    # (D/01) exported report
    #
    # (pimydoc)command line help for --exportreport(full version)
    # ⋅Export report by creating a new file in which
    # ⋅both report text and graphics are put together.
    # ⋅- default value: "no export", i.e. no exported report file
    # ⋅- otherwise 'md' is the only value or the only acceptable start string
    # ⋅  since md format is the only known format for exported report;
    # ⋅  you may add the exported report filename after '=',
    # ⋅  e.g. 'md=myfile.md';
    # ⋅       'md' (in this case the default file name will be used)
    # ⋅  the default filename is '$DEFAULT_EXPORTREPORT_FILENAME' . "
    # ⋅  Please note that graphs will not be added to the exported file if
    # ⋅  --checkup/--downloadconfigfile/--mymachine is set.
    # =============================================================================
    exportreport = wisteria.globs.ARGS.exportreport
    if exportreport == "no export":
        pass
    elif exportreport.startswith("md"):
        if ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug("(exit_handler/exported report) "
                     "about to create an exported report (type: 'md').")

        if "=" not in exportreport:
            # ---- default name for the exportreport file ----
            exportreport_filename = wisteria.globs.DEFAULT_EXPORTREPORT_FILENAME
            if ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug(
                    "(exit_handler/exported report) exported report will be named, by default, "
                    f"'{exportreport_filename}' .")
        else:
            # ---- name as read in ARGS.exportreport ----
            exportreport_filename = \
                get_exportreport_filename(basename=exportreport[exportreport.index("=")+1:])

            if ARGS.verbosity == VERBOSITY_DEBUG:
                msgdebug("(exit_handler/exported report) exported report will be named "
                         f"'{exportreport_filename}' .")

        try:
            exportedreportfile = open(exportreport_filename, "w", encoding="utf-8")
            reportfile = open_reportfile(mode="r")[0]  # open_reportfile() returns (object, path)
            with exportedreportfile, reportfile:
                # ---- (1/2) exported report: text ----------------------------
                exportedreportfile.write("```\n")
                for line in reportfile.readlines():
                    exportedreportfile.write(line)
                exportedreportfile.write("```\n")
                exportedreportfile.write("\n")

                # ---- (2/2) exported report: graphs --------------------------
                if not wisteria.globs.ARGS.mymachine and \
                   not wisteria.globs.ARGS.checkup and \
                   not wisteria.globs.ARGS.downloadconfigfile:
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
                    for _, _, _, _, title, filename in wisteria.globs.GRAPHS_DESCRIPTION:
                        if not os.path.exists(filename):
                            msgwarning("(exit_handler/exported report) "
                                       f"Didn't add '{filename}' to exported report file "
                                       "since this file doesn't exist.")
                        else:
                            # we use os.path.basename(filename) and not filename directly
                            # since the given path is relative.
                            exportedreportfile.write(f"![{title}]({os.path.basename(filename)})\n")
                            exportedreportfile.write("\n")
        except FileNotFoundError as err:
            msgerror("(ERRORID055) "
                     "Can't find a way to the exported report filename "
                     f"'{exportreport_filename}' ('{normpath(exportreport_filename)}') :"
                     "the path is unreachable; "
                     f"Python error is: {err} .")
    else:
        msgerror("(ERRORID054) An error occured "
                 f"while reading --exportreport string '{ARGS.exportreport}'.")
        msginfo("About --exportreport:")
        msginfo(help_cmdline_exportreport(details=True))

    # =============================================================================
    # (D/02) closing and removing of tempfile
    # =============================================================================
    # it may happen that wisteria.globs.DATA has not been fully
    # initialized, hence the first part of the 'if':
    if 'file descriptor' in wisteria.globs.DATA and \
       not wisteria.globs.DATA['file descriptor'].closed:
        if ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"(exit_handler) About to close the wisteria.globs.DATA['file descriptor'] "
                     "file descriptor"
                     f"('{normpath(wisteria.globs.DATA['file descriptor'].name)}').")
        wisteria.globs.DATA['file descriptor'].close()

    if os.path.exists(wisteria.globs.TMPFILENAME):
        if ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"(exit_handler) About to remove the temp file "
                     f"'{wisteria.globs.TMPFILENAME}' "
                     f"('{normpath(wisteria.globs.TMPFILENAME)}')")

        # The "PermissionError" exception may be raised on Windows system:
        try:
            os.remove(wisteria.globs.TMPFILENAME)
        except PermissionError:
            pass

    # =============================================================================
    # (D/03) closing wisteria.globs.RICHFILECONSOLE_FILEOBJECT
    # =============================================================================
    # this file should be the last one to be closed if we want to use msgxxx() methods:
    if not wisteria.globs.RICHFILECONSOLE_FILEOBJECT.closed:
        if ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"(exit_handler) About to close the console file "
                     f"'{wisteria.globs.RICHFILECONSOLE_FILEOBJECT.name}' "
                     f"('{normpath(wisteria.globs.RICHFILECONSOLE_FILEOBJECT.name)}').")
        wisteria.globs.RICHFILECONSOLE_FILEOBJECT.close()

    # =============================================================================
    # (D/04) reset console cursor
    # =============================================================================
    if wisteria.globs.RICHCONSOLE is not None:
        wisteria.globs.RICHCONSOLE.show_cursor(True)


atexit.register(exit_handler)


# =============================================================================
# (B/12) serializers import
# =============================================================================
wisteria.serializers.init_serializers()


# =============================================================================
# (B/13) temp file opening
# =============================================================================
# Such a file is required to create file descriptor objects.
# The temp. file will be removed at the end of the program.
if not os.path.exists(TMPFILENAME):
    with open(TMPFILENAME, "w", encoding="utf-8") as tmpfile:
        pass


# =============================================================================
# (B/14) known data init
# =============================================================================
wisteria.data.init_data()


# =============================================================================
# (B/15) checkup
# =============================================================================
def checkup():
    """
        checkup()

        Show some informations :
        - configuration file that would be used; does this file exist ?
          can this file be read without errors ?
        - serializers
        - data objects
    """
    # Pylint gets mixed up when reading how we iterate over <serializers>:
    #   pylint: disable=consider-using-dict-items

    # ---- Project name & version, time stamp ---------------------------------
    msgreport(fmt_projectversion(add_timestamp=True))
    msgreport(f"Running on Python {get_python_version()}")

    # (pimydoc)OUTPUT format
    # ⋅        ((bool)output to the console ?,
    # ⋅         (bool)output to the reportfile ?,
    # ⋅         (str)reportfile open mode = 'a' or 'w',
    # ⋅         (str)reportfile name,
    # ⋅        )
    if wisteria.globs.OUTPUT[1]:
        msgreport("The following informations are written in the report file "
                  f"('{wisteria.globs.RICHFILECONSOLE_FILEOBJECT.name}', "
                  f"namely {normpath(wisteria.globs.RICHFILECONSOLE_FILEOBJECT.name)}): "
                  "see the --output argument for more informations about this file. "
                  "--verbosity value [b]has an effect[/b] upon the displayed informations.")
    else:
        msgreport("The following informations ARE NOT written in the report file "
                  f"('{wisteria.globs.RICHFILECONSOLE_FILEOBJECT.name}', "
                  "namely {normpath(wisteria.globs.RICHFILECONSOLE_FILEOBJECT.name)}): "
                  "see the --output argument for more informations about this file. ")
    msgreport()

    # ---- configuration file -------------------------------------------------
    msgreporttitle("Config file")
    if not os.path.exists(ARGS.cfgfile):
        diagnostic = "  [red]Such a file doesn't exist[/red] but " \
            "you may run this program without it. " \
            "You may download this file using the --downloadconfigfile option."
    else:
        config = read_cfgfile(ARGS.cfgfile)
        if config is None:
            diagnostic = "  Such a file exists [bold red]but can't be read correctly[/bold red]."
        else:
            diagnostic = "  Such a file exists [bold]and can be read without errors[/bold]."

    msgreport(f"  With current arguments, configuration file would be '{ARGS.cfgfile}' "
              f"({normpath(ARGS.cfgfile)}), because of the value of --cfgfile. ")
    msgreport(diagnostic)

    # ---- DATA/UNVAILABLE_DATA checks
    if not wisteria.data.check(config):
        msgreport("Config file and installed modules cause at least one error, see lines above.")

    # ---- serializers --------------------------------------------------------
    msgreport()
    partial_report__serializers(show_all_serializers=True,
                                show_planned_serializers=False)

    # ---- data object --------------------------------------------------------
    msgreport()
    partial_report__data(show_all_data=True,
                         show_planned_data=False)

    # check: are DATA keys written in lower case ?
    errors = []
    for object_data_name in wisteria.globs.DATA:
        if object_data_name.lower() != object_data_name:
            errors.append(f"(ERRORID035) '{object_data_name}' is the name of "
                          "a DATA object but "
                          "contains upper case letters, which is forbidden")
    if errors:
        msgreport()
        msgerror("At least one error appeared "
                 "when checking the letter case in DATA keys:")
        for error in errors:
            msgerror(error)

    # check: are UNAVAILABLE_DATA keys written in lower case ?
    errors = []
    for object_data_name in wisteria.globs.UNAVAILABLE_DATA:
        if object_data_name.lower() != object_data_name:
            errors.append(f"(ERRORID036) '{object_data_name}' is the name of "
                          "an UNAVAILABLE_ object but "
                          "contains upper case letters, which is forbidden")
    if errors:
        msgreport()
        msgerror("At least one error appeared "
                 "when checking the letter case in UNAVAILABLE_DATA keys:")
        for error in errors:
            msgerror(error)

    # check: is a key defined in DATA also defined in UNAVAILABLE_DATA ?
    errors = []
    for object_data_name in wisteria.globs.UNAVAILABLE_DATA:
        if object_data_name in wisteria.globs.DATA:
            errors.append(f"(ERRORID040) '{object_data_name}' is defined "
                          "as a DATA key but also as an UNAVAILABLE_DATA key.")
    for object_data_name in wisteria.globs.DATA:
        if object_data_name in wisteria.globs.UNAVAILABLE_DATA:
            errors.append(f"(ERRORID043) '{object_data_name}' is defined "
                          "as a DATA key but also as an UNAVAILABLE_DATA key.")

    if errors:
        msgreport()
        msgerror("At least one error appeared "
                 "when checking if a key is defined in DATA and also in UNAVAILABLE_DATA:")
        for error in errors:
            msgerror(error)

    # check: do all serializers know how to serialize demonstration_dataobj ?
    check_ok = True
    data_name = "demonstration_dataobj"
    for serializer in wisteria.globs.SERIALIZERS:
        res = func_serialize(serializer=serializer, data_name=data_name)
        if not res.reversibility:
            check_ok = False
            msgerror("(ERRORID051) An error occured: "
                     f"the serializer named '{serializer}' "
                     "doesn't how to transcode the demonstration data object, "
                     f"namely {wisteria.globs.DATA[data_name]} ."
                     "This is absolutely abnormal: "
                     "the demonstration data object should always be able to be transcoded."
                     "So there is a serious problem with this serializer, "
                     "you may have to uninstall it.")

    if check_ok and \
       wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
        msgreporttitle("Do all known serializers know how to transcode demonstration data object ?")
        msgreport(f"As expected, all known serializers, namely {tuple(wisteria.globs.SERIALIZERS)} "
                  "know how to encode/decode demonstration data object, namely "
                  f"{wisteria.globs.DATA[data_name]} .")

    msgreport()

    # ---- less common multiple / data objects than can be fully transcoded  --
    if wisteria.globs.ARGS.verbosity >= VERBOSITY_DETAILS:
        msgreporttitle("What data object(s) could be transcoded, if required ?")
        data_name_to_be_discarded = []
        data_name_to_be_kept = []
        for serializer in wisteria.globs.SERIALIZERS:
            for data_name in wisteria.globs.DATA:
                res = func_serialize(serializer=serializer, data_name=data_name)
                if not res.reversibility:
                    data_name_to_be_discarded.append(data_name)
                else:
                    data_name_to_be_kept.append(data_name)
        msgreport(f"* {len(data_name_to_be_discarded)} "
                  f"Data {fmt_nounplural('Object', len(data_name_to_be_discarded))} "
                  "could not be fully transcoded, if required:")
        msgreport(f"{'; '.join(data_name_to_be_discarded)}")
        msgreport()
        msgreport(f"* {len(data_name_to_be_kept)} "
                  f"Data {fmt_nounplural('Object', len(data_name_to_be_kept))} "
                  "could be fully transcoded, if required (=data less common multiple):")
        msgreport(f"{'; '.join(data_name_to_be_kept)}")
        msgreport()

    # ---- graphs -------------------------------------------------------------
    msgreporttitle("graphs")
    if trytoimport("matplotlib.pyplot"):
        msgreport(
            "* Graphs could be created, if required, "
            "since [bold]matplotlib[/bold] is installed. "
            f"They would be called {help_graphsfilenames()}.")
    else:
        msgreport("! [bold]Graphs could NOT be created[/bold], "
                  "if required, since [bold]matplotlib[/bold] isn't installed; "
                  "see https://matplotlib.org/ .")
    msgreport()


if wisteria.globs.ARGS.checkup:
    checkup()
    # (pimydoc)exit codes
    # ⋅These exit codes try to take into account the standards, in particular this
    # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
    # ⋅
    # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
    # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
    # ⋅used for this project; these constants are only defined for Linux systems
    # ⋅and this project aims Windows/OSX systems.
    # ⋅
    # ⋅*    0: normal exit code
    # ⋅*       normal exit code after --help/--help2
    # ⋅*       normal exit code after --checkup
    # ⋅*       normal exit code after --downloadconfigfile
    # ⋅*       normal exit code after --mymachine
    # ⋅*       normal exit code (no data to handle)
    # ⋅*       normal exit code (no serializer to handle)
    # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
    # ⋅*    2: error, ill-formed --cmp string
    # ⋅*    3: error, ill-formed --output string
    # ⋅*    4: error, missing required module
    # ⋅*    5: error: an inconsistency between the data has been detected
    # ⋅*    6: error: can't open/create report file
    # ⋅*  100: internal error, data can't be loaded
    # ⋅*  101: internal error, an error occured while computing the results
    # ⋅*  102: internal error, an error occured in main()
    # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
    sys.exit(0)


# =============================================================================
# (B/16) informations about the current machine
# =============================================================================
if wisteria.globs.ARGS.mymachine:
    msgreport("Informations about the current machine:")
    if wisteria.globs.ARGS.verbosity < VERBOSITY_DETAILS:
        mymachine(detailslevel=1)
        msgreport("\nMore informations are available using --verbosity=2.")
    else:
        mymachine(detailslevel=2)
    # (pimydoc)exit codes
    # ⋅These exit codes try to take into account the standards, in particular this
    # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
    # ⋅
    # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
    # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
    # ⋅used for this project; these constants are only defined for Linux systems
    # ⋅and this project aims Windows/OSX systems.
    # ⋅
    # ⋅*    0: normal exit code
    # ⋅*       normal exit code after --help/--help2
    # ⋅*       normal exit code after --checkup
    # ⋅*       normal exit code after --downloadconfigfile
    # ⋅*       normal exit code after --mymachine
    # ⋅*       normal exit code (no data to handle)
    # ⋅*       normal exit code (no serializer to handle)
    # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
    # ⋅*    2: error, ill-formed --cmp string
    # ⋅*    3: error, ill-formed --output string
    # ⋅*    4: error, missing required module
    # ⋅*    5: error: an inconsistency between the data has been detected
    # ⋅*    6: error: can't open/create report file
    # ⋅*  100: internal error, data can't be loaded
    # ⋅*  101: internal error, an error occured while computing the results
    # ⋅*  102: internal error, an error occured in main()
    # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
    sys.exit(0)


# =============================================================================
# (B/17) download default config file
# =============================================================================
if wisteria.globs.ARGS.downloadconfigfile:
    downloadconfigfile()
    # (pimydoc)exit codes
    # ⋅These exit codes try to take into account the standards, in particular this
    # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
    # ⋅
    # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
    # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
    # ⋅used for this project; these constants are only defined for Linux systems
    # ⋅and this project aims Windows/OSX systems.
    # ⋅
    # ⋅*    0: normal exit code
    # ⋅*       normal exit code after --help/--help2
    # ⋅*       normal exit code after --checkup
    # ⋅*       normal exit code after --downloadconfigfile
    # ⋅*       normal exit code after --mymachine
    # ⋅*       normal exit code (no data to handle)
    # ⋅*       normal exit code (no serializer to handle)
    # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
    # ⋅*    2: error, ill-formed --cmp string
    # ⋅*    3: error, ill-formed --output string
    # ⋅*    4: error, missing required module
    # ⋅*    5: error: an inconsistency between the data has been detected
    # ⋅*    6: error: can't open/create report file
    # ⋅*  100: internal error, data can't be loaded
    # ⋅*  101: internal error, an error occured while computing the results
    # ⋅*  102: internal error, an error occured in main()
    # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
    sys.exit(0)


# =============================================================================
# (C/18) call to main()
# =============================================================================
def main():
    """
        main()

        Main entrypoint in the project. This method is called when Wisteria is called from outside,
        e.g. by the command line.
        _______________________________________________________________________

        RETURNED VALUE:
                (pimydoc)exit codes
                ⋅These exit codes try to take into account the standards, in particular this
                ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
                ⋅
                ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
                ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
                ⋅used for this project; these constants are only defined for Linux systems
                ⋅and this project aims Windows/OSX systems.
                ⋅
                ⋅*    0: normal exit code
                ⋅*       normal exit code after --help/--help2
                ⋅*       normal exit code after --checkup
                ⋅*       normal exit code after --downloadconfigfile
                ⋅*       normal exit code after --mymachine
                ⋅*       normal exit code (no data to handle)
                ⋅*       normal exit code (no serializer to handle)
                ⋅*    1: error, given config file can't be read (missing or ill-formed file)
                ⋅*    2: error, ill-formed --cmp string
                ⋅*    3: error, ill-formed --output string
                ⋅*    4: error, missing required module
                ⋅*    5: error: an inconsistency between the data has been detected
                ⋅*    6: error: can't open/create report file
                ⋅*  100: internal error, data can't be loaded
                ⋅*  101: internal error, an error occured while computing the results
                ⋅*  102: internal error, an error occured in main()
                ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
    """
    data = wisteria.globs.DATA
    serializers = wisteria.globs.SERIALIZERS

    # =========================================================================
    # (C/18.1) main(): debug messages
    # =========================================================================
    if ARGS.verbosity == VERBOSITY_DEBUG:
        msgdebug(f"known data: {list(data.keys())}")
    if ARGS.verbosity == VERBOSITY_DEBUG:
        msgdebug(f"known serializers: {serializers}")

    try:
        # =========================================================================
        # (C/18.2) main(): cmp string interpretation
        # =========================================================================
        success, serializer1, serializer2, cmpdata = read_cmpstring(ARGS.cmp)
        if ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug(f"Result of the call to read_cmpstring('{ARGS.cmp}'): "
                     f"{success}, {serializer1}, {serializer2}, {cmpdata}")

        if not success:
            msgerror("(ERRORID013) An error occured "
                     f"while reading --cmp string '{ARGS.cmp}'.")

            # (pimydoc)exit codes
            # ⋅These exit codes try to take into account the standards, in particular this
            # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
            # ⋅
            # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
            # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
            # ⋅used for this project; these constants are only defined for Linux systems
            # ⋅and this project aims Windows/OSX systems.
            # ⋅
            # ⋅*    0: normal exit code
            # ⋅*       normal exit code after --help/--help2
            # ⋅*       normal exit code after --checkup
            # ⋅*       normal exit code after --downloadconfigfile
            # ⋅*       normal exit code after --mymachine
            # ⋅*       normal exit code (no data to handle)
            # ⋅*       normal exit code (no serializer to handle)
            # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
            # ⋅*    2: error, ill-formed --cmp string
            # ⋅*    3: error, ill-formed --output string
            # ⋅*    4: error, missing required module
            # ⋅*    5: error: an inconsistency between the data has been detected
            # ⋅*    6: error: can't open/create report file
            # ⋅*  100: internal error, data can't be loaded
            # ⋅*  101: internal error, an error occured while computing the results
            # ⋅*  102: internal error, an error occured in main()
            # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
            return 2

        # =========================================================================
        # (C/18.3) main(): config file reading
        # =========================================================================
        config = None
        if cmpdata == 'ini':
            config = read_cfgfile(ARGS.cfgfile)

            if config is None:
                # (pimydoc)exit codes
                # ⋅These exit codes try to take into account the standards, in particular this
                # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
                # ⋅
                # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
                # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
                # ⋅used for this project; these constants are only defined for Linux systems
                # ⋅and this project aims Windows/OSX systems.
                # ⋅
                # ⋅*    0: normal exit code
                # ⋅*       normal exit code after --help/--help2
                # ⋅*       normal exit code after --checkup
                # ⋅*       normal exit code after --downloadconfigfile
                # ⋅*       normal exit code after --mymachine
                # ⋅*       normal exit code (no data to handle)
                # ⋅*       normal exit code (no serializer to handle)
                # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
                # ⋅*    2: error, ill-formed --cmp string
                # ⋅*    3: error, ill-formed --output string
                # ⋅*    4: error, missing required module
                # ⋅*    5: error: an inconsistency between the data has been detected
                # ⋅*    6: error: can't open/create report file
                # ⋅*  100: internal error, data can't be loaded
                # ⋅*  101: internal error, an error occured while computing the results
                # ⋅*  102: internal error, an error occured in main()
                # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
                return 1

            # ---- DATA/UNVAILABLE_DATA checks
            if not wisteria.data.check(config):
                # (pimydoc)exit codes
                # ⋅These exit codes try to take into account the standards, in particular this
                # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
                # ⋅
                # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
                # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
                # ⋅used for this project; these constants are only defined for Linux systems
                # ⋅and this project aims Windows/OSX systems.
                # ⋅
                # ⋅*    0: normal exit code
                # ⋅*       normal exit code after --help/--help2
                # ⋅*       normal exit code after --checkup
                # ⋅*       normal exit code after --downloadconfigfile
                # ⋅*       normal exit code after --mymachine
                # ⋅*       normal exit code (no data to handle)
                # ⋅*       normal exit code (no serializer to handle)
                # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
                # ⋅*    2: error, ill-formed --cmp string
                # ⋅*    3: error, ill-formed --output string
                # ⋅*    4: error, missing required module
                # ⋅*    5: error: an inconsistency between the data has been detected
                # ⋅*    6: error: can't open/create report file
                # ⋅*  100: internal error, data can't be loaded
                # ⋅*  101: internal error, an error occured while computing the results
                # ⋅*  102: internal error, an error occured in main()
                # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
                return 5

        # =========================================================================
        # (C/18.4) main(): PLANNED_TRANSCODINGS initialization
        # =========================================================================
        res_initplanned_transcodings = \
            init_planned_transcodings(serializer1,
                                      serializer2,
                                      cmpdata,
                                      config,
                                      ARGS.filter)

        if not res_initplanned_transcodings[0]:
            # (pimydoc)exit codes
            # ⋅These exit codes try to take into account the standards, in particular this
            # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
            # ⋅
            # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
            # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
            # ⋅used for this project; these constants are only defined for Linux systems
            # ⋅and this project aims Windows/OSX systems.
            # ⋅
            # ⋅*    0: normal exit code
            # ⋅*       normal exit code after --help/--help2
            # ⋅*       normal exit code after --checkup
            # ⋅*       normal exit code after --downloadconfigfile
            # ⋅*       normal exit code after --mymachine
            # ⋅*       normal exit code (no data to handle)
            # ⋅*       normal exit code (no serializer to handle)
            # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
            # ⋅*    2: error, ill-formed --cmp string
            # ⋅*    3: error, ill-formed --output string
            # ⋅*    4: error, missing required module
            # ⋅*    5: error: an inconsistency between the data has been detected
            # ⋅*    6: error: can't open/create report file
            # ⋅*  100: internal error, data can't be loaded
            # ⋅*  101: internal error, an error occured while computing the results
            # ⋅*  102: internal error, an error occured in main()
            # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
            return 103

        if res_initplanned_transcodings[1] == 0:
            msgwarning("No serializer to be used. The program can stop here.")
            # (pimydoc)exit codes
            # ⋅These exit codes try to take into account the standards, in particular this
            # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
            # ⋅
            # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
            # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
            # ⋅used for this project; these constants are only defined for Linux systems
            # ⋅and this project aims Windows/OSX systems.
            # ⋅
            # ⋅*    0: normal exit code
            # ⋅*       normal exit code after --help/--help2
            # ⋅*       normal exit code after --checkup
            # ⋅*       normal exit code after --downloadconfigfile
            # ⋅*       normal exit code after --mymachine
            # ⋅*       normal exit code (no data to handle)
            # ⋅*       normal exit code (no serializer to handle)
            # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
            # ⋅*    2: error, ill-formed --cmp string
            # ⋅*    3: error, ill-formed --output string
            # ⋅*    4: error, missing required module
            # ⋅*    5: error: an inconsistency between the data has been detected
            # ⋅*    6: error: can't open/create report file
            # ⋅*  100: internal error, data can't be loaded
            # ⋅*  101: internal error, an error occured while computing the results
            # ⋅*  102: internal error, an error occured in main()
            # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
            return 0
        if res_initplanned_transcodings[2] == 0:
            msgwarning("No data to be used. The program can stop here.")
            # (pimydoc)exit codes
            # ⋅These exit codes try to take into account the standards, in particular this
            # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
            # ⋅
            # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
            # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
            # ⋅used for this project; these constants are only defined for Linux systems
            # ⋅and this project aims Windows/OSX systems.
            # ⋅
            # ⋅*    0: normal exit code
            # ⋅*       normal exit code after --help/--help2
            # ⋅*       normal exit code after --checkup
            # ⋅*       normal exit code after --downloadconfigfile
            # ⋅*       normal exit code after --mymachine
            # ⋅*       normal exit code (no data to handle)
            # ⋅*       normal exit code (no serializer to handle)
            # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
            # ⋅*    2: error, ill-formed --cmp string
            # ⋅*    3: error, ill-formed --output string
            # ⋅*    4: error, missing required module
            # ⋅*    5: error: an inconsistency between the data has been detected
            # ⋅*    6: error: can't open/create report file
            # ⋅*  100: internal error, data can't be loaded
            # ⋅*  101: internal error, an error occured while computing the results
            # ⋅*  102: internal error, an error occured in main()
            # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
            return 0

        if wisteria.globs.ARGS.verbosity == VERBOSITY_DEBUG:
            msgdebug("wisteria.globs.PLANNED_TRANSCODINGS:")
            for (transcoding_index,
                 planned_transcoding) in enumerate(wisteria.globs.PLANNED_TRANSCODINGS):
                msgdebug(f"- #{transcoding_index+1}: {planned_transcoding}")

        # =========================================================================
        # (C/18.5) main(): results computing
        # =========================================================================
        compute_results__res = compute_results()
        if compute_results__res[0] is None:
            return compute_results__res[1]
        results = compute_results__res[0]

        # =========================================================================
        # (C/18.6) main(): report
        # =========================================================================
        report(results,
               (serializer1, serializer2, cmpdata))

        # (pimydoc)exit codes
        # ⋅These exit codes try to take into account the standards, in particular this
        # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
        # ⋅
        # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
        # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
        # ⋅used for this project; these constants are only defined for Linux systems
        # ⋅and this project aims Windows/OSX systems.
        # ⋅
        # ⋅*    0: normal exit code
        # ⋅*       normal exit code after --help/--help2
        # ⋅*       normal exit code after --checkup
        # ⋅*       normal exit code after --downloadconfigfile
        # ⋅*       normal exit code after --mymachine
        # ⋅*       normal exit code (no data to handle)
        # ⋅*       normal exit code (no serializer to handle)
        # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
        # ⋅*    2: error, ill-formed --cmp string
        # ⋅*    3: error, ill-formed --output string
        # ⋅*    4: error, missing required module
        # ⋅*    5: error: an inconsistency between the data has been detected
        # ⋅*    6: error: can't open/create report file
        # ⋅*  100: internal error, data can't be loaded
        # ⋅*  101: internal error, an error occured while computing the results
        # ⋅*  102: internal error, an error occured in main()
        # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
        return 0

    except WisteriaError as exception:
        # We need to convert exception into a str. so that msgerror() will apply
        # fmt_error() to the string.
        msgerror(str(exception))

        # (pimydoc)exit codes
        # ⋅These exit codes try to take into account the standards, in particular this
        # ⋅one: https://docs.python.org/3/library/sys.html#sys.exit
        # ⋅
        # ⋅Please note that `os` constants like `os.EX_OK` as defined in Python doc
        # ⋅(see https://docs.python.org/3/library/os.html#process-management) are not
        # ⋅used for this project; these constants are only defined for Linux systems
        # ⋅and this project aims Windows/OSX systems.
        # ⋅
        # ⋅*    0: normal exit code
        # ⋅*       normal exit code after --help/--help2
        # ⋅*       normal exit code after --checkup
        # ⋅*       normal exit code after --downloadconfigfile
        # ⋅*       normal exit code after --mymachine
        # ⋅*       normal exit code (no data to handle)
        # ⋅*       normal exit code (no serializer to handle)
        # ⋅*    1: error, given config file can't be read (missing or ill-formed file)
        # ⋅*    2: error, ill-formed --cmp string
        # ⋅*    3: error, ill-formed --output string
        # ⋅*    4: error, missing required module
        # ⋅*    5: error: an inconsistency between the data has been detected
        # ⋅*    6: error: can't open/create report file
        # ⋅*  100: internal error, data can't be loaded
        # ⋅*  101: internal error, an error occured while computing the results
        # ⋅*  102: internal error, an error occured in main()
        # ⋅*  103: internal error, can't initialize PLANNED_TRANSCODINGS
        return 102


if __name__ == '__main__':
    sys.exit(main())
