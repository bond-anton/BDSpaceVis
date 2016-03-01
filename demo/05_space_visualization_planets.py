import numpy as np
from mayavi import mlab

from Space import Space
from Space.Figures import Figure, generators
from Space.Coordinates import Cartesian
import Space_visualization as Visual


solar_system = Space('Solar System')
sun = Space('Sun')
mercury = Space('Mercury', Cartesian(origin=[0.5, 0.5, 0.5]))
venus = Space('Venus', Cartesian(origin=[1, 1, 1]))
earth = Space('Earth', Cartesian(origin=[1.5, 1.5, 1.5]))

mars = Space('Mars', Cartesian(origin=[2, 2, 2]))

#solar_system.add_element(mercury)
#solar_system.add_element(venus)
solar_system.add_element(earth)
#solar_system.add_element(mars)

moon = Space('Moon', Cartesian(origin=[0.2, 0.2, 0.2]))
earth.add_element(moon)
lunohod = Figure('Lunohod', Cartesian(origin=[0.1, 0.1, 0.1]))
points, dims = generators.generate_cuboid(a=0.1, b=0.2, c=0.05)
lunohod.set_points(points, dims)
dims = (2, 4, 2)
phi = np.linspace(0, np.pi, dims[1])
r = np.linspace(0.1, 0.5, dims[0])
theta = np.linspace(0, 0.5 * np.pi, dims[1])
phi = np.linspace(0, np.pi, dims[2])
#lunohod.set_points(generators.generate_sphere(r, theta, phi))
moon.add_element(lunohod)

phobos = Space('Phobos', Cartesian(origin=[0.2, 0.2, 0.2]))
deimos = Space('Deimos', Cartesian(origin=[-0.2, 0, 0]))
mars.add_element(phobos)
mars.add_element(deimos)

fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))  # Create the mayavi figure

@mlab.animate(delay=100)
def anim():
    views = Visual.gen_space_views(fig, solar_system)
    Visual.draw_space(views)
    while True:
        Visual.draw_space(views)
        earth.coordinate_system.rotate_axis_angle([-1, -1, -1], np.deg2rad(1))
        #mars.coordinate_system.rotate_axis_angle([1, 0, 0], np.deg2rad(1))
        yield

anim()
mlab.show()
