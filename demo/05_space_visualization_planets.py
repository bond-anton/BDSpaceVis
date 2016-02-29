import numpy as np
from mayavi import mlab

from Space import Space
from Space.Coordinates import Cartesian
import Space_visualization as Visual


solar_system = Space('Solar System')
sun = Space('Sun')
mercury = Space('Mercury', Cartesian(origin=[0.5, 0.5, 0.5]))
venus = Space('Venus', Cartesian(origin=[1, 1, 1]))
#earth = Space('Earth', Cartesian(origin=[1.5, 1.5, 1.5]))
earth = Space('Earth', Cartesian(origin=[0, 0, 0]))
mars = Space('Mars', Cartesian(origin=[2, 2, 2]))
#mars = Space('Mars', Cartesian(origin=[0, 0, 0]))

#solar_system.add_element(mercury)
#solar_system.add_element(venus)
solar_system.add_element(earth)
#solar_system.add_element(mars)

moon = Space('Moon', Cartesian(origin=[0.2, 0.2, 0.2]))
earth.add_element(moon)
lunohod = Space('Lunohod', Cartesian(origin=[0.1, 0.1, 0.1]))
moon.add_element(lunohod)

phobos = Space('Phobos', Cartesian(origin=[0.2, 0.2, 0.2]))
deimos = Space('Deimos', Cartesian(origin=[-0.2, 0, 0]))
mars.add_element(phobos)
mars.add_element(deimos)

#earth.coordinate_system.rotate_axis_angle([1, 1, 1], np.deg2rad(45))
#mars.coordinate_system.rotate_axis_angle([1, 1, 1], np.deg2rad(45))

fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))  # Create the mayavi figure

@mlab.animate(delay=100)
def anim():
    views = Visual.gen_space_views(fig, solar_system)
    #views = Visual.gen_space_views(fig, mars)
    Visual.draw_space(views)
    while True:
        Visual.draw_space(views)
        #coordinate_system = phobos.basis_in_global_coordinate_system()
        #print coordinate_system.origin
        earth.coordinate_system.rotate_axis_angle([1, 0, 1], np.deg2rad(1))
        #mars.coordinate_system.rotate_axis_angle([-1, 1, 1], np.deg2rad(-1))
        #mars.coordinate_system.rotate_axis_angle([1, 0, 0], np.deg2rad(1))
        #print deimos.coordinate_system.origin
        yield

anim()
mlab.show()
