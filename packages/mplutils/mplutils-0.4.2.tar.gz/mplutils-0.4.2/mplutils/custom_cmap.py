#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2016-2018 Cyril Desjouy <cyril.desjouy@univ-lemans.fr>
#
# This file is part of mplutils
#
# mplutils is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# mplutils is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mplutils. If not, see <http://www.gnu.org/licenses/>.
#
#
# Creation Date : mer. 9 avril 2015 10:30:45 CEST
"""
-----------
DOCSTRING

@author: Cyril Desjouy
"""

import matplotlib.pyplot as plt
from matplotlib import colors, cm
from matplotlib.colors import LinearSegmentedColormap
import numpy as np


__all__ = ['modified_jet', 'grayify_cmap', 'MidPointNorm']


def cmap_exists(name):
    """Test if a cmap is already registered. """
    try:
        cm.get_cmap(name)
    except ValueError:
        return False
    return True


def modified_jet():
    """
    Modified jet colormap
    howto : http://matplotlib.org/examples/pylab_examples/custom_cmap.html
    """

    if not cmap_exists('mjet'):
        cdictjet = {'blue': ((0.0, 1., 1.),
                             (0.11, 1, 1),
                             (0.34, 1, 1),
                             (0.48, 1, 1),
                             (0.52, 1, 1),
                             (0.65, 0, 0),
                             (1, 0, 0)),
                    'green': ((0.0, 0.6, 0.6),
                              (0.125, 0.8, 0.8),
                              (0.375, 1, 1),
                              (0.48, 1, 1),
                              (0.52, 1, 1),
                              (0.64, 1, 1),
                              (0.91, 0, 0),
                              (1, 0, 0)),
                    'red': ((0.0, 0, 0),
                            (0.35, 0, 0),
                            (0.48, 1, 1),
                            (0.52, 1, 1),
                            (0.66, 1, 1),
                            (0.8, 1, 1),
                            (1, 0., 0.))
                    }
        cmc = LinearSegmentedColormap('mjet', cdictjet, 1024)
        plt.register_cmap(name='mjet', cmap=cmc)
    else:
        cmc = cm.get_cmap('mjet')

    return cmc


def grayify_cmap(cmap):
    """Return a grayscale version of the colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    # convert RGBA to perceived greyscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return cmap.from_list(cmap.name + "_grayscale", colors, cmap.N)


class MidPointNorm(colors.Normalize):
    """ Adjust cmap.
    From https://stackoverflow.com/questions/
    7404116/defining-the-midpoint-of-a-colormap-in-matplotlib

    """

    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):

        vmin = max(0, 1 / 2 * (1 - abs((self.midpoint - self.vmin) /
                                    (self.midpoint - self.vmax))))

        if self.vmin != 0:
            vmax = min(1, 1 / 2 * (1 + abs((self.vmax - self.midpoint) /
                                        (self.midpoint - self.vmin))))
        else:
            vmax = 1

        mid = 0.5
        x, y = [self.vmin, self.midpoint, self.vmax], [vmin, mid, vmax]
        return np.ma.masked_array(np.interp(value, x, y))
