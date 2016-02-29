from __future__ import division
from coordinate_system import *
from Space import Space


class SpaceView(object):

    def __init__(self, fig, space, scale=1):
        self.fig = fig
        if not isinstance(space, Space):
            raise ValueError('Only Space class objects supported')
        self.space = space
        self.scale = scale
        self.cs_arrows = None
        self.cs_labels = None
        self.cs_cube = None

    def draw_cs(self):
        coordinate_system = self.space.basis_in_global_coordinate_system()
        if self.cs_arrows is None:
            self.cs_arrows, self.cs_labels = draw_CS_axes(self.fig, coordinate_system, offset=0, scale=self.scale)
        else:
            self.cs_arrows, self.cs_labels = update_CS_axes(coordinate_system, self.cs_arrows, self.cs_labels,
                                                            offset=0, scale=self.scale)


def gen_space_views(fig, space, scale=1):
    if not isinstance(space, Space):
        raise ValueError('argument has to be of Space class')
    views = [SpaceView(fig, space, scale)]
    for key in space.elements.keys():
        views += gen_space_views(fig, space.elements[key], scale=scale/2)
    return views


def draw_space(views):
    for view in views:
        view.draw_cs()
