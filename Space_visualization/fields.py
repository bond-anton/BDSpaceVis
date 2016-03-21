from __future__ import division
import numpy as np
from mayavi import mlab

from Space.Field import Field

from space import SpaceView


class FieldView(SpaceView):

    def __init__(self, fig, field, scale=1, color=None, opacity=None, grid=None,
                 cs_visible=True, surface_visible=True, wireframe=False):
        assert isinstance(field, Field)
        self.grid = None
        self.scalar_data = None
        self.vector_data = None
        super(FieldView, self).__init__(fig, field, scale=scale, color=color, opacity=opacity,
                                        points=None, dims=None,
                                        cs_visible=cs_visible, surface_visible=surface_visible, wireframe=wireframe)
        self.set_grid(grid)

    def set_grid(self, grid):
        if grid is None:
            self.grid = np.mgrid[-1:1:10j, -1:1:10j, -1:1:10j]
        else:
            self.grid = grid
        self.scalar_data = mlab.pipeline.scalar_field(self.grid[0], self.grid[1], self.grid[2],
                                                      self.space.scalar_field(self.grid))
        self.vector_data = self.space.vector_field(self.grid)

    def draw_volume(self):
        mlab.figure(self.fig, bgcolor=self.fig.scene.background)
        mlab.pipeline.volume(self.scalar_data)
