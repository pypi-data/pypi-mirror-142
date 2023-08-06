"""
Text automatically generated from 'README.md' .

Wisteria

NOT YET TO BE USED. PLEASE WAIT UNTIL VERSION NUMBER 0.3 !

Use Wisteria to compare different Python serializers.

This is a CLI/GPLv3/Python 3.8+ project, available on Linux/MacOSX/Windows syst
ems.


-------------------------------------------------------------------------------

TABLE OF CONTENTS

- [0] the project in a few words
  - [0.1] What about the name ?
- [1] installation
  - [1.1] poetry and dependencies
- [2] how to use
  - [2.0] overview
  - [2.1] with CLI and with Python interpreter
  - [2.2] more about command line arguments
- [3] if you want to read/test/modify the code
  - [3.0] classes hierarchy and code structure
  - [3.1] exit codes
  - [3.2] checks and tests
    - [3.2.1] check_tools
    - [3.2.2] launch the tests
    - [3.2.3] check code quality
    - [3.2.4] check pip conflicts
    - [3.2.5] search all errors/warnings codes
    - [3.2.6] automatically generate the main __init__py file
  - [3.3] code quality
    - [3.3.1] code quality matters
      - [3.3.1.1] about pylint and pylintrc
    - [3.3.2] how to read and write documentation
      - [3.3.2.1] about markdown files
    - [3.3.3] before committing
  - [3.4] coding conventions
  - [3.5] errors and warnings
  - [3.6] git and poetry and pypi workflow
  - [3.6.2] pypi: ship another version

- [4] FAQ

[0] the project in a few words

Use Wisteria to compare serializers like pickle, json or Django serializers : w
hich one is faster? Which one uses the least amount of memory? Which one produc
es the shortest strings? Which one has the best coverage rate?

You may have a look at some reports already computed by this script:

* By example, how does pickle compare to his competitors? ?
* How to classify serializers' weaknesses and strengths? ?
* Regarding the boolean values, what do the strings encoded by the different se
rializers look like? ?

After installing Wisteria, try $ wisteria --help and $ wisteria --checkup to se
e what can be done on your system; then execute a simple comparison like $ wist
eria --cmp="pickle vs marshal". Have fun discovering the rest of the possibilit
ies!

[0.1] What about the name ?

Wisteria is the project's name; package name is wisteria for Python, pipy and P
oetry.

Wisteria is the name of the beautiful flowers under which some of the code was
written.

!(source: Wikipedia)Wisteria is a genus of flowering plants in the legume famil
y, Fabaceae (Leguminosae), that includes ten species of woody twining vines tha
t are native to China, Korea, Japan, Southern Canada, the Eastern United States
, and north of Iran.

[1] installation

installation with pip

If $ python3 --version is Python3.8+ — you may write:

  |
  | $ pip install wisteria
  |
  | $ wisteria --help
  | $ wisteria --checkup
  |

installation with git/poetry/python3 being a link to Python3.8+

  |
  |     # wisteria:
  |     $ git clone https://github.com/suizokukan/wisteria
  |     $ cd wisteria
  |
  |     # poetry:
  |     $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/mast
er/get-poetry.py | python -
  |
  |     # dependencies' installation & execution:
  |     $ ~/.poetry/bin/poetry env use python3
  |     $ ~/.poetry/bin/poetry install
  |
  |     $ ~/.poetry/bin/poetry run ./bin/wisteria --help
  |     $ ~/.poetry/bin/poetry run ./bin/wisteria --checkup
  |
  |     Beware, install packages in the virtual environment required by the pro
ject.
  |     By example, if you want to install yajl for wisteria:
  |
  |     $ poetry run pip install yajl
  |

installation with git/poetry/a compiled version of Python3.8.11 (if your python
3 isn't Python3.8+)

Feel free to choose another Python's version and another directory where to com
pile Python. Code below for Debian systems:

  |
  |     # Python3.8.11:
  |     $ sudo apt install gcc make git curl
  |     $ cd ~/Desktop
  |     $ wget https://www.python.org/ftp/python/3.8.11/Python-3.8.11.tgz
  |     $ tar -xvzf Python-3.8.11.tgz
  |     $ cd Python-3.8.11
  |     $ ./configure
  |     $ make
  |     $ cd ..
  |
  |     # wisteria:
  |     $ git clone https://github.com/suizokukan/wisteria
  |     $ cd wisteria
  |
  |     # poetry:
  |     $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/mast
er/get-poetry.py | python -
  |
  |     # dependencies' installation & execution:
  |     $ ~/.poetry/bin/poetry env use ~/Desktop/Python-3.8.11/python
  |     $ ~/.poetry/bin/poetry install
  |
  |     $ ~/.poetry/bin/poetry run ./bin/wisteria --help
  |     $ ~/.poetry/bin/poetry run ./bin/wisteria --checkup
  |
  |     Beware, install packages in the virtual environment required by the pro
ject.
  |     By example, if you want to install yajl for wisteria:
  |
  |     $ poetry run pip install yajl
  |

installation with git/venv/a compiled version of Python3.8.11/manually added de
pendencies

Feel free to choose another Python's version and another directory where to com
pile Python. Code below for Debian systems:

  |
  |     $ git clone https://github.com/suizokukan/wisteria
  |     $ cd wisteria
  |     $ ~/Pythons/Python-3.7.9/python -m venv venv
  |     $ ./venv/bin/pip install --upgrade pip
  |     $ ./venv/bin/pip install rich psutil py-cpuinfo matplotlib
  |
  |     $ ./venv/bin/python ./bin/wisteria --help
  |     $ ./venv/bin/python ./bin/wisteria --checkup
  |
  |     Beware, install packages in the virtual environment required by the pro
ject.
  |     By example, if you want to install Iaswn for wisteria:
  |
  |     $ ./venv/bin/python -m pip install iaswn
  |

On Windows systems, don't forget to install WMI package too.

[1.1] poetry and dependencies

This package has been built and published thanks to poetry. Here is the result
of the $ poetry show --tree command.

Please note that installation on Windows systems requires the installation of t
he WMI package, automatically added by poetry and pip.

[2] how to use

[2.0] overview

Wisteria compares serializers based on 4 criteria: (1) speed of encoding and de
coding, (2) length of encoded string, (3) memory footprint of transcoding, (4)
ability to encode/decode different data types.

You want to know what serializers can be compared:

    $ wisteria --checkup

You want to know what data types the serializers can compare:

    $ wisteria --checkup

You want to compare 2 serializers, e.g. json and pickle:

    $ wisteria --cmp="json vs pickle"

You want to compare a serializer (e.g. json) against all serializers:

    $ wisteria --cmp="json vs all"

You want to compare all serializers between them:

    $ wisteria --cmp="all vs all"

You want to compare 2 serializers, e.g. json and pickle but only with the data
objects that can transcoded by both serializers:

    $ wisteria --cmp="json vs pickle" --filter="data:oktrans_only"

[2.1] with CLI and with Python interpreter

You may use Wisteria on the command line or with a Python interpreter:

    from wisteria import wisteria
    wisteria.checkup()
    wisteria.main()

[2.2] more about command line arguments

You want as much informations as possible:

    --report="full+"

You want as little informations as possible:

    --report="minimal"

You want only graphs:

    --report="graphs"

In addition to the console you want to use a specific report file name (opened
in 'write' mode):

    --output="console;reportfile/w=myreportfile.any"

No console: you juste want to use a specific report file name (opened in 'appen
d' mode):

    --output="reportfile/a=myreportfile.any"

In addition to the console you want to use a specific report file name (opened
in 'write' mode)
that contain the special DATETIME string (replaced by "%Y-%m-%d.%H.%M.%S"):

    --output="console;reportfile/w=myreportfile_DATETIME.any"

    which will be create a file named (e.g.) myreportfile_2021-12-31.23.59.59

In addition to the console you want to use a specific report file name (opened
in 'write' mode)
that contain the special TIMESTAMP string (replaced by int(time.time())):

    --output="console;reportfile/w=myreportfile_TIMESTAMP.any"

    which will be create a file named (e.g.) myreportfile_1635672267.any

You just want to see what the encoded string look like:

    --cmp="all" --report="titles;B3"

  |
  | (pimydoc)command line help for --cmp(full version)
  | ⋅Comparisons details.
  | ⋅
  | ⋅(I) serializers
  | ⋅Test one serializer alone(1) or one serializer against another serializer(
2) or
  | ⋅a serializer against all serializers(3) or all serializers(4) together.
  | ⋅
  | ⋅    (1) --cmp="json"
  | ⋅    (2) --cmp="json vs pickle"
  | ⋅    (3) --cmp="json vs all"
  | ⋅    (4) --cmp="all vs all"
  | ⋅
  | ⋅(II) data types:
  | ⋅Instead of 'cwc' (=compare what's comparable)(a) you may want to test all
data types
  | ⋅but cwc(b) or data types defined in the config file(c) or absolutely all d
ata types(d).
  | ⋅
  | ⋅    (a) --cmp="json vs pickle (cwc)"
  | ⋅    (b) --cmp="json vs pickle (allbutcwc)"
  | ⋅    (c) --cmp="json vs pickle (ini)"
  | ⋅    (d) --cmp="json vs pickle (all)"
  | ⋅
  | ⋅NB: You may use 'vs' as well as 'against', as in:
  | ⋅    --cmp="json vs pickle (cwc)"
  | ⋅NB: globs.py::REGEX_CMP defines exactly the expected format
  |

  |
  | (pimydoc)command line help for --exportreport(full version)
  | ⋅Export report by creating a new file in which
  | ⋅both report text and graphics are put together.
  | ⋅- default value: "no export", i.e. no exported report file
  | ⋅- otherwise 'md' is the only value or the only acceptable start string
  | ⋅  since md format is the only known format for exported report;
  | ⋅  you may add the exported report filename after '=',
  | ⋅  e.g. 'md=myfile.md';
  | ⋅       'md' (in this case the default file name will be used)
  | ⋅  the default filename is '$DEFAULT_EXPORTREPORT_FILENAME' . "
  | ⋅  Please note that graphs will not be added to the exported file if
  | ⋅  --checkup/--downloadconfigfile/--mymachine is set.
  |

  |
  | (pimydoc)command line help for --filter(full version)
  | ⋅The --filter argument allows to select only some serializers or
  | ⋅data objects. Currently only two values are accepted:
  | ⋅* either a null string (--filter=""): all serializers/data objects are
  | ⋅  used;
  | ⋅* either 'data:oktrans_only' (--filter='data:oktrans_only'): in this case,
  | ⋅  only the objects that can be successfully transcoded are kept;
  |

  |
  | (pimydoc)command line help for --output(full version)
  | ⋅A string like '[console;][reportfile/w/a]=subdirectory/myreportfilename'
  | ⋅
  | ⋅* 'console':
  | ⋅  - 'console' : if you want to write output messages to the console
  | ⋅
  | ⋅* 'reportfile='
  | ⋅  - either a simple string like 'report.txt'
  | ⋅  - either a string containing 'DATETIME'; in this case, 'DATETIME' will
  | ⋅    be replaced by datetime.datetime.now().strftime("%Y-%m-%d.%H.%M.%S");
  | ⋅    e.g. "report_DATETIME.txt" would become something like
  | ⋅         "report_2021-12-31.23.59.59.txt"
  | ⋅  - either a string containing 'TIMESTAMP'; in this case, 'TIMESTAMP' will
  | ⋅    be replaced by str(int(time.time()))
  | ⋅      e.g. "report_DATETIME.txt" would become something like
  | ⋅           "report_1635672267.txt"
  | ⋅
  | ⋅BEWARE: The path to the report file must exist; e.g. if ./path/ doesn't
  | ⋅exist you can't write:
  | ⋅     --output="console;reportfile/w=path/myreportfile"
  |

pylintrc
--------

  |
  | max-module-lines=1000 > max-module-lines=3000
  | max-returns=6 > max-returns=10
  | max-statements=50 > max-statements=120
  | max-locals=15 > max-locals=20
  | max-branches=12 > max-branches=40
  | max-args=5 > max-args=6
  | max-public-methods=20 > max-public-methods=30
  | max-args=6 > max-args=8
  | max-nested-blocks=5 > max-nested-blocks=6
  | max-attributes=7 > max-attributes=9
  |

Dependencies
------------

matplotlib required only to draw graphs.(https://matplotlib.org/)


Built-in Types coverage
-----------------------

list taken from https://docs.python.org/3/library/stdtypes.html (last update: 2
021-10-05)

Truth Value Testing/Boolean Operations — and, or, not/Comparisons

* bool

        (known by Wisteria as) "bool/false": False,
        (known by Wisteria as) "bool/true": True,

Numeric Types — int, float, complex

* int

        (known by Wisteria as) "int": 123
        (known by Wisteria as) "int_0": 0
        (known by Wisteria as) "int_1": 1
        (known by Wisteria as) "int_0xffff": 0xffff
        (known by Wisteria as) "int_0xffffffff": 0xffffffff
        (known by Wisteria as) "int_0xffffffffffffffff": 0xffffffffffffffff
        (known by Wisteria as) "int_0xffffffffffffffffffffffffffffffff": 0xffff
ffffffffffffffffffffffffffff
        (known by Wisteria as) "int_-1": -1
        (known by Wisteria as) "int_-0xffff": -0xffff
        (known by Wisteria as) "int_-0xffffffff": -0xffffffff
        (known by Wisteria as) "int_-0xffffffffffffffff": -0xffffffffffffffff
        (known by Wisteria as) "int_-0xffffffffffffffffffffffffffffffff": -0xff
ffffffffffffffffffffffffffffff

* float

        (known by Wisteria as) "float": 1.1
        (known by Wisteria as) "float(nan)": float('nan')

* complex

        (known by Wisteria as) "complex": 1+2j

Iterator Types

        (UNKNOWN TO Wisteria)

Sequence Types — list, tuple, range

* lists

        (known by Wisteria as) "list": ["1", "2", ]
        (known by Wisteria as) "list(empty)": []
        (known by Wisteria as) "list(+sublists)": ["1", "2", ["3", ["4", ]]]

* tuples

        (known by Wisteria as) "tuple": ("1", "2",)
        (known by Wisteria as) "tuple(empty)": ()
        (known by Wisteria as) "tuple(+subtuples)": ("1", "2", ("3", ("4",)))

* ranges

        (known by Wisteria as) "range": range(1000)
        (known by Wisteria as) "range(empty)": range(0)

Text Sequence Type — str

        (known by Wisteria as) "str": "abc"
        (known by Wisteria as) "str(empty)": ""
        (known by Wisteria as) "str(long)": "abhg12234"*10000
        (known by Wisteria as) "str(non ascii characters)": "êł¹@"+chr(0x1234)+
chr(0x12345)

Binary Sequence Types — bytes, bytearray, memoryview

* bytes

        (known by Wisteria as) "bytes": b"123"
        (known by Wisteria as) "bytes(empty)": b""

* bytearray

        (known by Wisteria as) "bytearray": bytearray(b"123")
        (known by Wisteria as) "bytearray(empty)": bytearray()

* memoryview

        (known by Wisteria as) "memoryview": memoryview(b"123")

Set Types — set, frozenset

* set

        (known by Wisteria as) "set": set(("1", "2",))
        (known by Wisteria as) "set(empty)": set()

* frozenset

        (known by Wisteria as) "frozenset": frozenset(("1", "2",))
        (known by Wisteria as) "frozenset(empty)": frozenset()

Mapping Types — dict

* dict

        (known by Wisteria as) "dict(keys/bool)": {False: "False", True: "True"
}
        (known by Wisteria as) "dict(keys/float)": {1.1: "value1.1", 2.2: "valu
e2.2"}
        (known by Wisteria as) "dict(keys/int)": {0: "value0", 1: "value1", 2:
"value2"}
        (known by Wisteria as) "dict(keys/str)": {"key1": "value1", "key2": "va
lue2"}
        (known by Wisteria as) "dict(keys/str+subdicts)": {"key1": "value1", "k
ey2": "value2", "key3": {"key4": "key4", }}

Modules

        (known by Wisteria as) "imported module": re
        (known by Wisteria as) "imported module(class)": re.Pattern
        (known by Wisteria as) "imported module(function)": re.sub

Classes and Class Instances

        (known by Wisteria as) "metaclass": MetaClass()
        (known by Wisteria as) "regularclass": RegularClass()
        (known by Wisteria as) "regularclass(async_method)": RegularClass.async
_method
        (known by Wisteria as) "regularclass(class_method)": RegularClass.class
_method
        (known by Wisteria as) "regularclass(generator)": RegularClass.generato
r
        (known by Wisteria as) "regularclass(method)": RegularClass.method
        (known by Wisteria as) "regularclass(static_method)": RegularClass.stat
ic_method
        (known by Wisteria as) "regularclassinheriteddict": RegularClassInherit
edDict()
        (known by Wisteria as) "regularclassinheritedlist": RegularClassInherit
edList()

Functions

        (known by Wisteria as) "function": anyfunc
        (known by Wisteria as) "function(python)": print

Methods

        (UNKNOWN TO Wisteria)

Code Objects

        (UNKNOWN TO Wisteria)

Type Objects

        (known by Wisteria as) "type(str)": str
        (known by Wisteria as) "type(type(str))": type(str)

The Ellipsis Object

        (UNKNOWN TO Wisteria)

The NotImplemented Object

        (known by Wisteria as) "notimplemented": NotImplemented

The Null Object

        (known by Wisteria as) "none": None,

Boolean Values

        (see above)

Internal Objects

        (UNKNOWN TO Wisteria)

stack frame objects, traceback objects, and slice objects

Special Attributes

        (UNKNOWN TO Wisteria)

file descriptor

        (known by Wisteria as) "file descriptor": open(TMPFILENAME, encoding="u
tf-8")

Python exceptions

        (known by Wisteria as) "pythonexception typeerror": TypeError

Python Modules coverage
-----------------------

list taken from https://docs.python.org/3/py-modindex.html (last update: 2021-1
0-05)

    (_)
    * __future__
    * __main__
    * _thread

    (a)
    * abc
    * aifc
    * argparse
    * array
        (known by Wisteria as) "array(b)":  array.array('b', (-1, 2)),
        (known by Wisteria as) "array(b/empty)": array.array('b'),
        (known by Wisteria as) "array(b_unsigned)": array.array('b', (1, 2)),
        (known by Wisteria as) "array(b_unsigned/empty)": array.array('B'),
        (known by Wisteria as) "array(u)": array.array('u', 'hello \u2641'),
        (known by Wisteria as) "array(u/empty)": array.array('u'),
        (known by Wisteria as) "array(h)": array.array('h', (-1, 2)),
        (known by Wisteria as) "array(h/empty)": array.array('h'),
        (known by Wisteria as) "array(h_unsigned)": array.array('H', (1, 2)),
        (known by Wisteria as) "array(h_unsigned/empty)": array.array('H'),
        (known by Wisteria as) "array(i)": array.array('i', (-1, 2)),
        (known by Wisteria as) "array(i/empty)": array.array('i'),
        (known by Wisteria as) "array(i_unsigned)": array.array('I', (1, 2)),
        (known by Wisteria as) "array(i_unsigned/empty)": array.array('I'),
        (known by Wisteria as) "array(l)": array.array('l', [-1, 2, 3, 4, 5]),
        (known by Wisteria as) "array(l/empty)": array.array('l'),
        (known by Wisteria as) "array(l_unsigned)": array.array('L', (1, 2)),
        (known by Wisteria as) "array(l_unsigned/empty)": array.array('L'),
        (known by Wisteria as) "array(q)": array.array('q', (-1, 2)),
        (known by Wisteria as) "array(q/empty)": array.array('q'),
        (known by Wisteria as) "array(q_unsigned)": array.array('Q', (1, 2)),
        (known by Wisteria as) "array(q_unsigned/empty)": array.array('Q'),
        (known by Wisteria as) "array(f)": array.array('f', (1.3, float('nan'))
),
        (known by Wisteria as) "array(f/empty)": array.array('f'),
        (known by Wisteria as) "array(d)": array.array('d', [1.0, 2.0, 3.14]),
        (known by Wisteria as) "array(d/empty)": array.array('d'),
    * ast
    * asynchat
    * asyncio
    * asyncore
    * atexit
    * audioop

    (b)
    * base64
    * bdb
    * binascii
    * binhex
    * bisect
    * builtins
    * bz2

    (c)
    * calendar
        (known by Wisteria as) "calendar(calendar(3))": calendar.Calendar(3)

    * cgi
    * cgitb
    * chunk
    * cmath
    * cmd
    * code
    * codecs
    * codeop
    * collections
        (known by Wisteria as) "collections.chainmap(empty)": collections.Chain
Map()
        (known by Wisteria as) "collections.chainmap": collections.ChainMap({1:
 2}, {2: 3})
        (known by Wisteria as) "collections.counter(empty)": collections.Counte
r()
        (known by Wisteria as) "collections.counter": collections.Counter((1, 2
))
        (known by Wisteria as) "collections.defaultdict(empty)": collections.de
faultdict()
        (known by Wisteria as) "collections.defaultdict": collections.defaultdi
ct(None, {1: 2})
        (known by Wisteria as) "collections.deque(empty)": collections.deque()
        (known by Wisteria as) "collections.deque": collections.deque((1, 2))
        (known by Wisteria as) "collections.ordereddict(empty)": collections.Or
deredDict()
        (known by Wisteria as) "collections.ordereddict": collections.OrderedDi
ct({1: 2})
      * collections.abc
    * colorsys
    * compileall
    * concurrent
      * concurrent.futures
    * configparser
    * contextlib
    * contextvars
    * copy
    * copyreg
    * cProfile
    * crypt
    * csv
    * ctypes
    * curses
      * curses.ascii
      * curses.panel
      * curses.textpad

    (d)
    * dataclasses
    * datetime
        (known by Wisteria as) "datetime(datetime.datetime)": datetime.datetime
(2001, 12, 1)
        (known by Wisteria as) "datetime(datetime.timedelta)":
             datetime.datetime(2001, 12, 1) - datetime.datetime(2000, 12, 1)
    * dbm
      * dbm.dumb
      * dbm.gnu
      * dbm.ndbm
    * decimal
        (known by Wisteria as) "decimal(0.5)": decimal.Decimal(0.5)
        (known by Wisteria as) "decimal(1/7)": decimal.Decimal(1) / decimal.Dec
imal(7)
        (known by Wisteria as) "decimal(nan)": decimal.Decimal('NaN')
        (known by Wisteria as) "decimal(-infinity)": decimal.Decimal("-Infinity
")
        (known by Wisteria as) "decimal(+infinity)": decimal.Decimal("+Infinity
")
    * difflib
    * dis
    * distutils
      * distutils.archive_util
      * distutils.bcppcompiler
      * distutils.ccompiler
      * distutils.cmd
      * distutils.cmd
      * distutils.command
      * distutils.command.bdist
      * distutils.command.bdist_dumb
      * distutils.command.bdist_msi
      * distutils.command.bdist_packager
      * distutils.command.bdist_rpm
      * distutils.command.bdist_wininst
      * distutils.command.build Build
      * distutils.command.build_clib
      * distutils.command.build_ext
      * distutils.command.build_py
      * distutils.command.build_scripts
      * distutils.command.check
      * distutils.command.clean
      * distutils.command.config
      * distutils.command.install
      * distutils.command.install_data
      * distutils.command.install_headers
      * distutils.command.install_lib
      * distutils.command.install_scripts
      * distutils.command.register
      * distutils.command.sdist
      * distutils.core
      * distutils.cygwinccompiler
      * distutils.debug
      * distutils.dep_util
      * distutils.dir_util
      * distutils.dist
      * distutils.errors
      * distutils.extension
      * distutils.fancy_getopt
      * distutils.file_util
      * distutils.filelist
      * distutils.log
      * distutils.msvccompiler
      * distutils.spawn
      * distutils.sysconfig
      * distutils.text_file
      * distutils.unixccompiler
      * distutils.util
      * distutils.version
    * doctest

    (e)
    * email
      * email.charset
      * email.contentmanager
      * email.encoders
      * email.errors
      * email.generator
      * email.header
      * email.headerregistry
      * email.iterators
      * email.message
      * email.mime
      * email.parser
      * email.policy
      * email.utils
    * encodings
      * encodings.idna
      * encodings.mbcs
      * encodings.utf_8_sig
    * ensurepip
    * enum
    * errno

    (f)
    * faulthandler
    * fcntl
    * filecmp
    * fileinput
    * fnmatch
    * formatter
    * fractions
    * ftplib
    * functools

    (g)
    * gc
    * getopt
    * getpass
    * gettext
    * glob
    * graphlib
    * grp
    * gzip

    (h)
    * hashlib
    * heapq
    * hmac
    * html
      * html.entities
      * html.parser
    * http
      * http.client
      * http.cookiejar
      * http.cookies
      * http.server

    (i)
    * imaplib
    * imghdr
    * imp
    * importlib
      * importlib.abc
      * importlib.machinery
      * importlib.metadata
      * importlib.resources
      * importlib.util
    * inspect
    * io
        (known by Wisteria as) "io.string": io.StringIO()
        (known by Wisteria as) "io.string(empty)": io.StringIO().write("string"
)
    * ipaddress
    * itertools

    (j)
    * json
      * json.tool

    (k)
    * keyword

    (l)
    * lib2to3
    * linecache
    * locale
    * logging
      * logging.config
      * logging.handlers
    * lzma

    (m)
    * mailbox
    * mailcap
    * marshal
    * math
    * mimetypes
    * mmap
    * modulefinder
    * msilib
    * msvcrt
    * multiprocessing   Process-based parallelism.
      * multiprocessing.connection
      * multiprocessing.dummy
      * multiprocessing.managers
      * multiprocessing.pool
      * multiprocessing.shared_memory

    (n)
    * netrc
    * nis
    * nntplib
    * numbers
        (known by Wisteria as) "numbers(complex)": numbers.Complex
        (known by Wisteria as) "numbers(integral)": numbers.Integral
        (known by Wisteria as) "numbers(numbers)": numbers.Number()
        (known by Wisteria as) "numbers(real)": numbers.Real

    (o)
    * operator
    * optparse
    * os
      * os.path
    * ossaudiodev

    (p)
    * parser
    * pathlib
    * pdb
    * pickle
    * pickletools
    * pipes
    * pkgutil
    * platform
    * plistlib
    * poplib
    * posix
    * pprint
    * profile
    * pstats
    * pty
    * pwd
    * py_compile
    * pyclbr
    * pydoc

    (q)
    * queue
    * quopri

    (r)
    * random
    * re
        (known by Wisteria as) "re.match": re.match(".*", "abc")
        (known by Wisteria as) "re.match(+flags)": re.match(".*", "abc", re.M)
        (known by Wisteria as) "re.pattern(bytes)": re.compile(".*")
        (known by Wisteria as) "re.pattern(str)": re.compile(b".*")

    * readline
    * reprlib
    * resource
    * rlcompleter
    * runpy

    (s)
    * sched
    * secrets
    * select
    * selectors
    * shelve
    * shlex
    * shutil
    * signal
    * site
    * smtpd
    * smtplib
    * sndhdr
    * socket
    * socketserver
    * spwd
    * sqlite3
    * ssl
    * stat
    * statistics
    * string
    * stringprep
    * struct
    * subprocess
    * sunau
    * symbol
    * symtable
    * sys
    * sysconfig
    * syslog

    (t)
    * tabnanny
    * tarfile
    * telnetlib
    * tempfile
    * termios
    * test
      * test.support .
      * test.support.bytecode_helper
      * test.support.script_helper
      * test.support.socket_helper
    * textwrap
    * threading
    * time
        (known by Wisteria as) "time(time.time)": time.time()
    * timeit
    * tkinter
      * tkinter.colorchooser
      * tkinter.commondialog
      * tkinter.dnd
      * tkinter.filedialog
      * tkinter.font
      * tkinter.messagebox
      * tkinter.scrolledtext
      * tkinter.simpledialog
      * tkinter.tix
      * tkinter.ttk
    * token
    * tokenize
    * trace
    * traceback
    * tracemalloc
    * tty
    * turtle
    * turtledemo
    * types
    * typing

    (u)
    * unicodedata
    * unittest
      *    unittest.mock
    * urllib
      * urllib.error
      * urllib.parse
      * urllib.request
      * urllib.response
      * urllib.robotparser
    * uu
    * uuid

    (v)
    * venv

    (w)
    * warnings
    * wave
    * weakref
    * webbrowser
    * winreg
    * winsound
    * wsgiref
      * wsgiref.handlers
      * wsgiref.headers
      * wsgiref.simple_server
      * wsgiref.util
      * wsgiref.validate

    (x)
    * xdrlib
    * xml
      * xml.dom Document
      * xml.dom.minidom
      * xml.dom.pulldom
      * xml.etree.ElementTree
      * xml.parsers.expat
      * xml.parsers.expat.errors
      * xml.parsers.expat.model
      * xml.sax Package
      * xml.sax.handler
      * xml.sax.saxutils
      * xml.sax.xmlreader
    * xmlrpc
      * xmlrpc.client
      * xmlrpc.server

    (z)
    * zipapp
    * zipfile
    * zipimport
    * zlib
    * zoneinfo

Third-party Modules coverage
----------------------------

dateutil (https://dateutil.readthedocs.io/en/stable/)

        (known by Wisteria as) "dateutil(parser.parse)": dateutil.parser.parse(
"2021-03-04")


[4] FAQ

Q: How to modify the report (=log) file name ?

A: Use --output option (e.g. --output="console;reportfile/w=report.txt). You ma
y use special keywords 'TIMESTAMP' and 'DATETIME' in the filename.

  |
  | (pimydoc)command line help for --output(full version)
  | ⋅A string like '[console;][reportfile/w/a]=subdirectory/myreportfilename'
  | ⋅
  | ⋅* 'console':
  | ⋅  - 'console' : if you want to write output messages to the console
  | ⋅
  | ⋅* 'reportfile='
  | ⋅  - either a simple string like 'report.txt'
  | ⋅  - either a string containing 'DATETIME'; in this case, 'DATETIME' will
  | ⋅    be replaced by datetime.datetime.now().strftime("%Y-%m-%d.%H.%M.%S");
  | ⋅    e.g. "report_DATETIME.txt" would become something like
  | ⋅         "report_2021-12-31.23.59.59.txt"
  | ⋅  - either a string containing 'TIMESTAMP'; in this case, 'TIMESTAMP' will
  | ⋅    be replaced by str(int(time.time()))
  | ⋅      e.g. "report_DATETIME.txt" would become something like
  | ⋅           "report_1635672267.txt"
  | ⋅
  | ⋅BEWARE: The path to the report file must exist; e.g. if ./path/ doesn't
  | ⋅exist you can't write:
  | ⋅     --output="console;reportfile/w=path/myreportfile"
  |

Where is defined in the code the number of graphs?

    globs.py::GRAPHS_DESCRIPTION

How do I add a new cwc class ?

    - create another directory in wisteria/cwc, by example wisteria/cwc/newcwc/
 .
    - A default.py file is required, namely wisteria/cwc/newcwc/default.py
    for all serializers whose 'cwc' attribute is set to 'default'.
    - Add other .py files (iaswn.py, ...) for other SERIALIZERS[].cwc values
    - A works_as_expected.py file is required, namely wisteria/cwc/newcwc/works
_as_expected.py
    with two functions: initialize() and works_as_expected()
    - Modify globs.py:CWC_MODULES to add your new classes
    - Add your classes to wisteria.ini (section data objects)

[3] if you want to read/test/modify the code
g
[3.0] classes hierarchy and code structure

See classes.md.

  |
  | (pimydoc)code structure
  | ⋅step A: command line arguments, --help message
  | ⋅- (A/00) minimal internal imports
  | ⋅- (A/01) command line parsing
  | ⋅
  | ⋅step B: initializations & --checkup
  | ⋅- (B/02) normal imports & PLATFORM_SYSTEM initialization
  | ⋅- (B/03) wisteria.globs.ARGS initialization
  | ⋅- (B/04) a special case: if no argument has been given, we explicit the de
fault values
  | ⋅- (B/05) --output string/OUTPUT+RICHCONSOLE init
  | ⋅- (B/06) reportfile opening: update REPORTFILE_PATH & co.
  | ⋅- (B/07) msgxxx() functions can be used
  | ⋅- (B/08) check STR2REPORTSECTION_KEYS and STR2REPORTSECTION
  | ⋅- (B/09) project name & version
  | ⋅- (B/10) ARGS.report interpretation
  | ⋅- (B/11) exit handler installation
  | ⋅- (B/12) serializers import
  | ⋅- (B/13) temp file opening
  | ⋅- (B/14) known data init (to be placed after 'temp file opening')
  | ⋅- (B/15) checkup
  | ⋅- (B/16) informations about the current machine
  | ⋅- (B/17) download default config file
  | ⋅
  | ⋅step C: main()
  | ⋅- (C/18) call to main()
  | ⋅       - (C/18.1) main(): debug messages
  | ⋅       - (C/18.2) main(): cmp string interpretation
  | ⋅       - (C/18.3) main(): config file reading
  | ⋅       - (C/18.4) main(): PLANNED_TRANSCODINGS initialization
  | ⋅       - (C/18.5) main(): results computing
  | ⋅       - (C/18.6) main(): report
  | ⋅
  | ⋅step D: exit_handler()
  | ⋅- (D/01) exported report
  | ⋅- (D/02) closing and removing of tempfile
  | ⋅- (D/03) closing wisteria.globs.RICHFILECONSOLE_FILEOBJECT
  | ⋅- (D/04) reset console cursor
  | ⋅
  |

[3.1] exit codes

(pimydoc)exit codes
⋅These exit codes try to take into account the standards, in particular this
⋅one: https://docs.python.org/3/library/sys.html#sys.exit
⋅
⋅Please note that os constants like os.EX_OK as defined in Python doc
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

[3.4] coding conventions.

See codingconventions.md.

[3.6] git and poetry and pypi workflow

[3.6.2] pypi: ship another version

  |
  | $ poetry build
  | $ poetry publish
  |
"""
