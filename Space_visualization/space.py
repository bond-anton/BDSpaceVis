from __future__ import division
from coordinate_system import *
from Space import Space
from Space.Figures import Figure
from Space.Figures.Spherical import SphericalShape, SphericalWedge, SphericalSectionWedge


class SpaceView(object):

    def __init__(self, fig, space, scale=1, color=None, points=None, dims=None,
                 cs_visible=True, surface_visible=True, wireframe=False):
        self.fig = fig
        if not isinstance(space, Space):
            raise ValueError('Only Space class objects supported')
        self.space = space
        self.scale = scale
        self.cs_arrows = None
        self.cs_labels = None
        self.surface = None
        self.edge_visible = False
        self.cs_visible = cs_visible
        self.surface_visible = surface_visible
        self.wireframe = wireframe
        self.points = None
        self.dims = None
        self.set_points(points, dims)
        self.color = None
        self.set_color(color)

    def set_points(self, points=None, dims=None):
        if points is None:
            self.points = None
            self.dims = None
        else:
            self.points = np.array(points, dtype=np.float)
            self.dims = dims

    def set_color(self, color=None):
        if color is None:
            self.color = (1, 0, 0)
        elif isinstance(color, (list, tuple, np.array)):
            self.color = color
        else:
            raise ValueError('color must be an iterable of three color values')
        self.draw()

    def set_cs_visible(self, cs_visible=True):
        self.cs_visible = cs_visible
        self.draw()

    def set_surface_visible(self, surface_visible=True):
        self.surface_visible = surface_visible
        self.draw()

    def set_wireframe(self, wireframe=True):
        self.wireframe = wireframe
        self.draw()

    def draw_cs(self):
        if self.cs_visible:
            coordinate_system = self.space.basis_in_global_coordinate_system()
            if self.cs_arrows is None:
                self.cs_arrows, self.cs_labels = draw_CS_axes(self.fig, coordinate_system, offset=0, scale=self.scale)
            else:
                self.cs_arrows, self.cs_labels = update_CS_axes(coordinate_system, self.cs_arrows, self.cs_labels,
                                                                offset=0, scale=self.scale)
        else:
            if self.cs_labels is not None:
                for cs_label in self.cs_labels:
                    cs_label.remove()
            if self.cs_arrows is not None:
                self.cs_arrows.remove()
            self.cs_arrows = None
            self.cs_labels = None

    def draw_surface(self):
        if self.surface_visible:
            if self.points is not None:
                coordinate_system = self.space.basis_in_global_coordinate_system()
                grid = tvtk.StructuredGrid(dimensions=self.dims)
                grid.points = coordinate_system.to_parent(self.points)
                if self.surface is None:
                    mlab.figure(self.fig, bgcolor=self.fig.scene.background)
                    data_set = mlab.pipeline.add_dataset(grid, self.space.name)
                    self.surface = mlab.pipeline.surface(data_set)
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

    def draw_volume(self):
        """
        empty interface stub
        """

    def draw(self):
        self.draw_cs()
        self.draw_surface()
        self.draw_volume()


class FigureView(SpaceView):

    def __init__(self, fig, figure, scale=1, color=None, edge_visible=False, resolution=20):
        assert isinstance(figure, Figure)
        self.resolution = resolution
        points, dims = generate_points(figure, self.resolution)
        super(FigureView, self).__init__(fig, figure, scale=scale, color=color, points=points, dims=dims)
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


def gen_space_views(fig, space, scale=1):
    if not isinstance(space, Space):
        raise ValueError('argument has to be of Space class')
    if isinstance(space, Figure):
        view = FigureView(fig, space, scale)
    else:
        view = SpaceView(fig, space, scale)
    views = {space.name: view}
    for key in space.elements.keys():
        views.update(gen_space_views(fig, space.elements[key], scale=scale/2))
    return views


def draw_space(views):
    for key in views.keys():
        views[key].draw()
