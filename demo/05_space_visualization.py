import numpy as np
from mayavi import mlab

from Space import Space
from Space.Coordinates import Cartesian
import Space_visualization as Visual


solar_system = Space('Solar System')
mercury = Space('Mercury', Cartesian(origin=[1, 1, 1]))
venus = Space('Venus')
earth = Space('Earth')
mars = Space('Mars')

solar_system.add_element(mercury)
solar_system.add_element(venus)
solar_system.add_element(earth)
solar_system.add_element(mars)

moon = Space('Moon')
earth.add_element(moon)
lunohod = Space('Lunohod')
moon.add_element(lunohod)

phobos = Space('Phobos')
phobos2 = Space('Phobos')
phobos3 = Space('Phobos')
deimos = Space('Deimos')
mars.add_element(phobos)
mars.add_element(phobos2)
mars.add_element(phobos3)
mars.add_element(deimos)

phobos.detach_from_parent()
earth.add_element(phobos)
phobos.detach_from_parent()
mars.add_element(phobos)
solar_system.print_tree()

fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))  # Create the mayavi figure
Visual.draw_space(fig, solar_system)
mlab.show()
