import numpy as np
from mayavi import mlab

from Space import Space
from Space.Coordinates import Cartesian
import Space_visualization as Visual


solar_system = Space('Solar System')
sun = Space('Sun')
mercury = Space('Mercury', Cartesian(origin=[0.5, 0.5, 0.5]))
venus = Space('Venus', Cartesian(origin=[1, 1, 1]))
earth = Space('Earth', Cartesian(origin=[1.5, 1.5, 1.5]))
mars = Space('Mars', Cartesian(origin=[2, 2, 2]))

solar_system.add_element(mercury)
solar_system.add_element(venus)
solar_system.add_element(earth)
solar_system.add_element(mars)

moon = Space('Moon', Cartesian(origin=[0.2, 0.2, 0.2]))
earth.add_element(moon)
lunohod = Space('Lunohod', Cartesian(origin=[0.01, 0.01, 0.01]))
moon.add_element(lunohod)

phobos = Space('Phobos', Cartesian(origin=[0.2, 0.2, 0.2]))
deimos = Space('Deimos', Cartesian(origin=[0.2, -0.2, 0.2]))
mars.add_element(phobos)
mars.add_element(deimos)

earth.coordinate_system.rotate_axis_angle([1, 1, 1], np.deg2rad(45))

fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))  # Create the mayavi figure

@mlab.animate(delay=10)
def anim():
    Visual.draw_space(fig, solar_system)
    while True:
        #delta_eulers = np.array([direction_prec * np.deg2rad(step_prec), 0, direction_rot * np.deg2rad(step_rot)])
        #CS_1.set_euler_angles(CS_1.euler_angles + delta_eulers)
        #cs_box_1, arrows_1, labels_1 = Visual.update_CS_box(CS_1, cs_box_1, arrows_1, labels_1)
        yield

anim()
mlab.show()
