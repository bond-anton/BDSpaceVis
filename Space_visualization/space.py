from coordinate_system import *
from Space import Space


def draw_space(fig, space):
    if not isinstance(space, Space):
        raise ValueError('argument has to be of Space class')
    draw_CS_axes(fig, space.coordinates_system)
    for key in space.elements.keys():
        draw_space(fig, space.elements[key])
