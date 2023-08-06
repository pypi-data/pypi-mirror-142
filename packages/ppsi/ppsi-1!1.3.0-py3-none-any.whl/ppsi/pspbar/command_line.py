#!/usr/bin/env python3
# -*- coding:utf-8; mode:python -*-
#
# Copyright 2020-2021 Pradyumna Paranjape
# This file is part of ppsi.
#
# ppsi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ppsi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ppsi.  If not, see <https://www.gnu.org/licenses/>.
#
'''
Command line parser for pspbar

'''

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from pathlib import Path
from sys import version_info
from typing import Optional, Tuple

from ppsi import __version__


def cli() -> Tuple[Optional[int], Optional[int]]:
    '''
    Parse command line

    period: fast update period in seconds
    multi: multiple of <period> that yields slow update period

    Returns:
        tuple(period, multiple)

    '''
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s ' + ' '.join(
            (__version__, 'form', str(Path(__file__).resolve().parent.parent),
             f'(python {version_info.major}.{version_info.minor})')))
    parser.add_argument("period",
                        type=int,
                        default=None,
                        nargs='?',
                        help="period between successive updates in seconds")
    parser.add_argument("-m",
                        "--multi",
                        type=int,
                        default=None,
                        help="multple of 'period' to update other stats")
    args = parser.parse_args()
    return args.period, args.multi
