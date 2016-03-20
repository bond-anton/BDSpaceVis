from __future__ import division
import numpy as np

from Space.Field import Field

import generators
from space import SpaceView


class FieldView(SpaceView):

    def __init__(self, fig, field, scale=1, color=None, opacity=None, edge_visible=False,
                 cs_visible=True, surface_visible=True, wireframe=False, resolution=20):
        assert isinstance(field, Field)
        self.resolution = resolution
        self.edge_visible = edge_visible
        points, dims = None, None
        super(FieldView, self).__init__(fig, field, scale=scale, color=color, opacity=opacity,
                                        points=points, dims=dims,
                                        cs_visible=cs_visible, surface_visible=surface_visible, wireframe=wireframe)

    def set_resolution(self, resolution):
        self.resolution = resolution
        #points, dims = generate_points(self.space, resolution)
        #self.set_points(points, dims)
        self.draw()

    def set_edge_visible(self, edge_visible=True):
        self.edge_visible = edge_visible
        self.draw()
