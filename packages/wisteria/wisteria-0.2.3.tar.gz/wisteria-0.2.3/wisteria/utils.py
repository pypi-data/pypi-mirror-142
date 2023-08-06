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
    Wisteria project : wisteria/utils.py

    BEWARE! Please use only very basic imports since this file is used in
    "step A" section of the program, where no third-party libraries may
    be used.
    ___________________________________________________________________________

    o  get_missing_required_internal_modules()
    o  get_python_version()
    o  normpath(path)
    o  pimydocstr2str(source, replacements=None)
    o  shortenedstr(string, maximallength)
    o  strdigest(string)
    o  trytoimport(module_name)
"""
# BEWARE! Please use only verby basic imports since this file is used in
# "step A" section of the program, where no third-party libraries may
# be used.
import hashlib
import importlib
import os
import os.path
import sys

import wisteria.globs


def get_missing_required_internal_modules():
    """
        get_missing_required_internal_modules()

        Return a list of the missing required modules.
        No debug message here since this function belongs to the 'A' step of the
        program.
        _______________________________________________________________________

        RETURNED VALUE: (list of str) a list of the missing required modules.
    """
    missing_modules = []
    for module_name in ('rich', 'psutil', 'cpuinfo'):
        if not trytoimport(module_name):
            missing_modules.append(module_name)
    return missing_modules


def get_python_version():
    """
        get_python_version()

        Return the Python version on one line.
    """
    return sys.version.replace(chr(0x0A), '- ')


def normpath(path):
    """
        normpath()

        Return a human-readable (e.g. "~" -> "/home/myhome/") normalized
        version of a file path.
        ________________________________________________________________________

        PARAMETER : (str)path

        RETURNED VALUE : the normalized <path>
    """
    res = os.path.normpath(os.path.abspath(os.path.expanduser(path)))
    if res == ".":
        res = os.getcwd()
    return res


def pimydocstr2str(source,
                   replacements=None):
    """
        pimydocstr2str()

        Convert the pimydoc string <source> into a simple Python string.
        Replace in <source> each value found in <replacements> by the
        corresponding key.
        _______________________________________________________________________

        PARAMETERS:
        o  (str)the pimydoc string
        o  (None|dict str:str) replacements

        RETURNED VALUE: (str)a simple Python string
    """
    if replacements:
        for before, after in replacements.items():
            source = source.replace(before, after)

    # let's empty lines and lines containing the pimydoc header:
    #   NB: we use chr(0x22C5) instead of the real character to avoid pimydoc
    #       modifies this line
    return "\n".join(line.lstrip()[len(chr(0x22C5)):] for line in source.split("\n")
                     if line.strip() and '('+'pimy'+'doc'+')' not in line.strip())


def shortenedstr(string,
                 maximallength=40):
    """
        This function reduces a <string> so that the maximum length of the returned
        string is equal to <maximallength>.
        ________________________________________________________________________

        PARAMETERS:
        o  (str)string       : to be string to be shortened
        o  (int)maximallength: the maximal length of <string>

        RETURNED VALUE: (str)<string> or a shortened version of <string>
    """
    # ---- nothing to do, <string> isn't too long. ----------------------------
    if len(string) <= maximallength:
        return string

    # ---- We have to reduce <string>. ----------------------------------------
    suffix = "[…]"

    # a special case: <maximallength> is really too short !
    if len(suffix) > maximallength:
        return string[:maximallength]

    # e.g. if maximallength==10, if string="01234567890"(len=11)  > "0123456[…]" (len=10)
    # e.g. if maximallength==10, if string="012345678901"(len=12) > "0123456[…]" (len=10)
    return string[:maximallength-len(suffix)] + suffix


def strdigest(string):
    """
        strdigest()

        Return the formatted fingerprint of <string>.
        _______________________________________________________________________

        ARGUMENT:
        o  (str)string: the string to be hashed

        RETURNED VALUE: (str)
    """
    return "0x"+hashlib.sha256(string.encode()).hexdigest()[:5]


def trytoimport(module_name):
    """
        trytoimport()

        Try to import <module_name> module.
        _______________________________________________________________________

        ARGUMENT:
        o  (str)module_name: the module to be imported

        RETURNED VALUE: (bool)success
    """
    res = True
    try:
        wisteria.globs.MODULES[module_name] = \
            importlib.import_module(module_name)
    except ModuleNotFoundError:
        res = False
    return res
