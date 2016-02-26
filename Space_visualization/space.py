from __future__ import division
from coordinate_system import *
from Space import Space


class SpaceView(object):

    def __init__(self, fig, space):
        self.fig = fig
        self.space = space


def draw_space(fig, space, scale=1):
    if not isinstance(space, Space):
        raise ValueError('argument has to be of Space class')
    coordinate_system = space.basis_in_global_coordinate_system()
    draw_CS_axes(fig, coordinate_system, scale=scale)
    for key in space.elements.keys():
        draw_space(fig, space.elements[key], scale=scale/2)
