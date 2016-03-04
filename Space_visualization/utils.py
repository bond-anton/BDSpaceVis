from __future__ import division
from Space import Space
from Space.Figure import Figure
from Space.Curve import Curve
from space import SpaceView
from figures import FigureView
from curves import CurveView


def gen_space_views(fig, space, scale=1):
    if not isinstance(space, Space):
        raise ValueError('argument has to be of Space class')
    if isinstance(space, Figure):
        view = FigureView(fig, space, scale=scale)
    elif isinstance(space, Curve):
        view = CurveView(fig, space, scale=scale)
    else:
        view = SpaceView(fig, space, scale=scale)
    views = {space.name: view}
    for key in space.elements.keys():
        views.update(gen_space_views(fig, space.elements[key], scale=scale/2))
    return views


def draw_space(views):
    for key in views.keys():
        views[key].draw()
