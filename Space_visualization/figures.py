from __future__ import division
import numpy as np

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
