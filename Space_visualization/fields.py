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
        self.scalar_volume = None
        self.vector_data = None
        self.vector_field = None
        self.vector_volume = None
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

    def set_scalar_field_visible(self, scalar_field_visible=True):
        self.scalar_field_visible = scalar_field_visible
        self.draw()

    def set_vector_field_visible(self, vector_field_visible=True):
        self.vector_field_visible = vector_field_visible
        self.draw()

    def update_scalar_data(self):
        self.scalar_data = self.space.scalar_field(self.grid)

    def update_vector_data(self):
        self.vector_data = self.space.vector_field(self.grid)

    def draw_volume(self):
        if self.vector_field_visible or self.scalar_field_visible:
            coordinate_system = self.space.basis_in_global_coordinate_system()
            grid = coordinate_system.to_parent(self.grid.reshape(3, -1).T).T.reshape(self.grid.shape)
            if self.vector_field is None:
                mlab.figure(self.fig, bgcolor=self.fig.scene.background)
                self.vector_field = mlab.pipeline.vector_field(grid[0], grid[1], grid[2],
                                                               self.vector_data[0],
                                                               self.vector_data[1],
                                                               self.vector_data[2],
                                                               scalars=self.scalar_data,
                                                               name=self.space.name)
            else:
                origin = np.array([np.min(grid[0]), np.min(grid[1]), np.min(grid[2])])
                spacing = np.array([grid[0, 1, 0, 0] - grid[0, 0, 0, 0],
                                    grid[1, 0, 1, 0] - grid[1, 0, 0, 0],
                                    grid[2, 0, 0, 1] - grid[2, 0, 0, 0]])
                self.vector_field.spacing = spacing
                self.vector_field.origin = origin
                self.vector_field.vector_data = np.rollaxis(self.vector_data, 0, 4)
                self.vector_field.scalar_data = self.scalar_data
            if self.vector_volume is None and self.vector_field_visible:
                self.vector_volume = mlab.pipeline.vectors(self.vector_field, mask_points=20)
            if self.scalar_volume is None and self.scalar_field_visible:
                self.scalar_volume = mlab.pipeline.volume(self.vector_field)
        if not self.vector_field_visible:
            self.remove_vector_field()
        if not self.scalar_field_visible:
            self.remove_scalar_field()

    def remove_vector_field(self):
        if self.vector_volume is not None:
            self.vector_volume.remove()
        self.vector_volume = None

    def remove_scalar_field(self):
        if self.scalar_volume is not None:
            self.scalar_volume.remove()
        self.scalar_volume = None
