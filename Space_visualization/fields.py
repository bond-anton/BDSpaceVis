from __future__ import division, print_function
import numpy as np
from mayavi import mlab

from Space.Field import Field

from space import SpaceView


class FieldView(SpaceView):

    def __init__(self, fig, field, scale=1, color=None, opacity=None, grid=None,
                 cs_visible=True, scalar_field_visible=True, vector_field_visible=True):
        assert isinstance(field, Field)
        self.grid = None
        self.scalar_data = None
        self.scalar_field = None
        self.vector_data = None
        self.scalar_volume = None
        self.scalar_field_visible = scalar_field_visible
        self.vector_field_visible = vector_field_visible
        super(FieldView, self).__init__(fig, field, scale=scale, color=color, opacity=opacity,
                                        points=None, dims=None,
                                        cs_visible=cs_visible, surface_visible=False, wireframe=False)
        self.set_grid(grid)

    def set_grid(self, grid):
        if grid is None:
            self.grid = np.mgrid[-1:1:10j, -1:1:10j, -1:1:10j]
        else:
            self.grid = grid
        self.update_scalar_data()
        self.update_vector_data()

    def update_scalar_data(self):
        self.scalar_data = self.space.scalar_field(self.grid)

    def update_vector_data(self):
        self.vector_data = self.space.vector_field(self.grid)

    def draw_scalar_field(self):
        if self.scalar_field_visible:
            coordinate_system = self.space.basis_in_global_coordinate_system()
            grid = coordinate_system.to_parent(self.grid.reshape(3, -1).T).T.reshape(self.grid.shape)
            if self.scalar_field is None:
                mlab.figure(self.fig, bgcolor=self.fig.scene.background)
                self.scalar_field = mlab.pipeline.scalar_field(grid[0], grid[1], grid[2],
                                                               self.scalar_data)
            else:
                origin = np.array([np.min(grid[0]), np.min(grid[1]), np.min(grid[2])])
                spacing = np.array([grid[0, 1, 0, 0] - grid[0, 0, 0, 0],
                                    grid[1, 0, 1, 0] - grid[1, 0, 0, 0],
                                    grid[2, 0, 0, 1] - grid[2, 0, 0, 0]])
                self.scalar_field.spacing = spacing
                self.scalar_field.origin = origin
                self.scalar_field.scalar_data = self.scalar_data
            if self.scalar_volume is None:
                self.scalar_volume = mlab.pipeline.volume(self.scalar_field)
        else:
            if self.scalar_volume is not None:
                self.scalar_volume.remove()
            self.scalar_volume = None

    def draw_volume(self):
        self.draw_scalar_field()
