from __future__ import division
from coordinate_system import *
from Space import Space
from Space.Figures import Figure


class SpaceView(object):

    def __init__(self, fig, space, scale=1, color=None):
        self.fig = fig
        if not isinstance(space, Space):
            raise ValueError('Only Space class objects supported')
        self.space = space
        self.scale = scale
        self.cs_arrows = None
        self.cs_labels = None
        self.color = None
        self.set_color(color)

    def set_color(self, color=None):
        if color is None:
            self.color = (1, 0, 0)
        elif isinstance(color, (list, tuple, np.array)):
            self.color = color
        else:
            raise ValueError('color must be an iterable of three color values')

    def draw_cs(self):
        coordinate_system = self.space.basis_in_global_coordinate_system()
        if self.cs_arrows is None:
            self.cs_arrows, self.cs_labels = draw_CS_axes(self.fig, coordinate_system, offset=0, scale=self.scale)
        else:
            self.cs_arrows, self.cs_labels = update_CS_axes(coordinate_system, self.cs_arrows, self.cs_labels,
                                                            offset=0, scale=self.scale)


class FigureView(SpaceView):

    def __init__(self, fig, figure, scale=1, color=None, edge_visible=False):
        assert isinstance(figure, Figure)
        super(FigureView, self).__init__(fig, figure, scale=scale, color=color)
        self.surface = None
        self.edge_visible = edge_visible

    def draw_surface(self):
        if self.space.points is not None:
            coordinate_system = self.space.basis_in_global_coordinate_system()
            grid = tvtk.StructuredGrid(dimensions=(2, 2, 2))
            grid.points = coordinate_system.to_parent(self.space.points)
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


def gen_space_views(fig, space, scale=1):
    if not isinstance(space, Space):
        raise ValueError('argument has to be of Space class')
    if isinstance(space, Figure):
        views = [FigureView(fig, space, scale)]
    else:
        views = [SpaceView(fig, space, scale)]
    for key in space.elements.keys():
        views += gen_space_views(fig, space.elements[key], scale=scale/2)
    return views


def draw_space(views):
    for view in views:
        view.draw_cs()
        if isinstance(view, FigureView):
            view.draw_surface()
