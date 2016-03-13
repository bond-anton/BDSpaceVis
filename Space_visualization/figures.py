from __future__ import division
import numpy as np

from Space.Figure import Figure
from Space.Figure.Sphere import SphericalShape, SphericalWedge, SphericalSegmentWedge
from Space.Figure.Cylinder import CylindricalWedge
from Space.Figure.Cone import ConicalWedge
from Space.Figure.Cube import Parallelepiped

import generators
from space import SpaceView


class FigureView(SpaceView):

    def __init__(self, fig, figure, scale=1, color=None, opacity=None, edge_visible=False,
                 cs_visible=True, surface_visible=True, wireframe=False, resolution=20):
        assert isinstance(figure, Figure)
        self.resolution = resolution
        self.edge_visible = edge_visible
        points, dims = generate_points(figure, self.resolution)
        super(FigureView, self).__init__(fig, figure, scale=scale, color=color, opacity=opacity,
                                         points=points, dims=dims,
                                         cs_visible=cs_visible, surface_visible=surface_visible, wireframe=wireframe)

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
            theta = np.linspace(figure.theta[0], figure.theta[1],
                                angular_resolution(figure.theta[1] - figure.theta[0], resolution), endpoint=True)
            points, dims = generators.generate_sphere(phi, theta, r)
        elif isinstance(figure, SphericalSegmentWedge):
            z = np.array([figure.h1, figure.h2], dtype=np.float)
            points, dims = generators.generate_spherical_section(phi, z, r)
    elif isinstance(figure, CylindricalWedge):
        phi = np.linspace(0.0, figure.phi, angular_resolution(figure.phi, resolution), endpoint=True)
        r = np.array([figure.r_inner, figure.r_outer], dtype=np.float)
        z = np.array(figure.z, dtype=np.float)
        points, dims = generators.generate_cylinder(phi, z, r)
    elif isinstance(figure, ConicalWedge):
        phi = np.linspace(0.0, figure.phi, angular_resolution(figure.phi, resolution), endpoint=True)
        z = np.array(figure.z, dtype=np.float)
        points, dims = generators.generate_cone(phi, z, theta=figure.theta,
                                                z_offset=figure.z_offset, r_min=figure.r_min)
    elif isinstance(figure, Parallelepiped):
        points, dims = generators.generate_parallelepiped(a=figure.vectors[0], b=figure.vectors[1], c=figure.vectors[2],
                                                          origin=np.array([0, 0, 0]))
    return points, dims


def angular_resolution(angle, resolution):
    points_num = int(angle / np.pi * resolution)
    if points_num < 2:
        points_num = 2
    return points_num
