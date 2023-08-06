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
Load yaml configuration file(s)

Load {action: '--flag', ...} for all available menus
'''

import os
from pathlib import Path

from xdgpspconf import ConfDisc


def read_config(custom_conf: os.PathLike = None) -> dict:
    '''
    Read pspbar configuration from supplied yml file or default

    Args:
        custom_conf: custom path of config file pspbar.yml

    Returns:
        pspbar config
    '''
    return list(
        ConfDisc('sway', shipped=Path(__file__).parent /
                 'config/pspbar.yml').read_config(
                     flatten=True,
                     cname='pspbar',
                     ext='.yml',
                     custom=custom_conf).values())[0]
