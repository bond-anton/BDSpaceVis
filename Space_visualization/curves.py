from __future__ import division
import numpy as np
from mayavi import mlab
from Space.Figure import Figure
from Space.Figure.Spherical import SphericalShape, SphericalWedge, SphericalSectionWedge

import generators
from space import SpaceView


class FigureView(SpaceView):

    def __init__(self, fig, figure, scale=1, color=None, edge_visible=False,
                 cs_visible=True, surface_visible=True, wireframe=False, resolution=20):
        assert isinstance(figure, Figure)
        self.resolution = resolution
        points, dims = generate_points(figure, self.resolution)
        super(FigureView, self).__init__(fig, figure, scale=scale, color=color, points=points, dims=dims,
                                         cs_visible=cs_visible, surface_visible=surface_visible, wireframe=wireframe)
        self.edge_visible = edge_visible

    def set_resolution(self, resolution):
        self.resolution = resolution
        points, dims = generate_points(self.space, resolution)
        self.set_points(points, dims)
        self.draw()

    def set_edge_visible(self, edge_visible=True):
        self.edge_visible = edge_visible
        self.draw()

    def draw_surface(self):
        if self.surface_visible:
            if self.points is not None:
                coordinate_system = self.space.basis_in_global_coordinate_system()
                curve_points = coordinate_system.to_parent(self.points)
                if self.surface is None:
                    mlab.figure(self.fig, bgcolor=self.fig.scene.background)
                    self.surface = mlab.plot3d(curve_points[:, 0], curve_points[:, 1], curve_points[:, 2], color=(1, 0, 0))
                else:
                    self.surface.parent.parent.data = grid
                self.surface.parent.parent.name = self.space.name
                self.surface.actor.property.color = self.color
                self.surface.actor.property.edge_visibility = self.edge_visible
                self.surface.actor.property.edge_color = self.color
                if self.wireframe:
                    self.surface.actor.property.representation = 'wireframe'
                else:
                    self.surface.actor.property.representation = 'surface'
        else:
            if self.surface is not None:
                self.surface.remove()
            self.surface = None


def generate_points(figure, resolution=20):
    assert isinstance(figure, Figure)
    points = None
    dims = None
    if isinstance(figure, SphericalShape):
        phi = np.linspace(0.0, figure.phi, angular_resolution(figure.phi, resolution), endpoint=True)
        r = np.array([figure.r_inner, figure.r_outer], dtype=np.float)
        if isinstance(figure, SphericalWedge):
            theta = np.linspace(0.0, figure.theta, angular_resolution(figure.theta, resolution), endpoint=True)
            points, dims = generators.generate_sphere(phi, theta, r)
        elif isinstance(figure, SphericalSectionWedge):
            z = np.array([figure.h1, figure.h2], dtype=np.float)
            points, dims = generators.generate_spherical_section(phi, z, r)
    return points, dims


def angular_resolution(angle, resolution):
    points_num = int(angle / np.pi * resolution)
    if points_num < 2:
        points_num = 2
    return points_num
