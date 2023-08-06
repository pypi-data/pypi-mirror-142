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
    Wisteria project : wisteria/filterstr.py

    parse_filterstr() function, required to parse --filter argument.

    ___________________________________________________________________________

    o  parse_filterstr()
"""
from wisteria.serializers import func_serialize
import wisteria


def parse_filterstr(filterstr):
    """
        parse_filterstr()

        Parse the --filter string <filterstr>.

        (pimydoc)filterstr
        ⋅A filter string should be parsed by filterstr.py::parse_filterstr() .
        ⋅
        ⋅filterstr format:
        ⋅o  empty string        : no filter
        ⋅o  'data:oktrans_only' : only the objects that can be successfully
        ⋅                         transcoded are used
        _______________________________________________________________________

        ARGUMENT: (str)filterstr

        RETURNED VALUE: (bool)success,
                        (list of str)data_to_be_discarded,
                        (list of str)serializers_to_be_discarded
    """
    data_to_be_discarded, serializers_to_be_discarded = [], []

    if filterstr == "":
        pass

    elif filterstr == "data:oktrans_only":

        for serializer in wisteria.globs.SERIALIZERS:
            for data_name in wisteria.globs.DATA:
                res = func_serialize(serializer=serializer,
                                     data_name=data_name)
                if not res.reversibility:
                    data_to_be_discarded.append(data_name)

    else:
        return False, None, None

    return True, sorted(data_to_be_discarded), sorted(serializers_to_be_discarded)
