import numpy as np
from mayavi import mlab

from Space import Space
from Space.Figure.Spherical import *
from Space.Curve.Parametric import Arc
from Space.Coordinates import Cartesian
import Space_visualization as Visual


solar_system = Space('Solar System')
sun = Sphere('Sun', r_outer=0.2)

mercury = Space('Mercury', Cartesian(origin=[0.5, 0.5, 0.5]))
venus = Space('Venus', Cartesian(origin=[1, 1, 1]))

earth_orbit = Arc(name='Earth orbit', a=1, b=2, start=0, stop=2*np.pi, right=True)
earth = Sphere(name='Earth', coordinate_system=Cartesian(origin=[1.5, 1.5, 1.5]), r_outer=0.02)

mars = Space('Mars', Cartesian(origin=[2, 2, 2]))

solar_system.add_element(sun)
#solar_system.add_element(mercury)
#solar_system.add_element(venus)
solar_system.add_element(earth_orbit)
solar_system.add_element(earth)
#solar_system.add_element(mars)

#moon = SphericalCone('Moon', Cartesian(origin=[0.2, 0.2, 0.2]),
#                     r_inner=0.5, r_outer=1.0, theta=np.pi/6)
#earth.add_element(moon)
#lunohod = SphericalWedge('Lunohod', Cartesian(origin=[0.1, 0.1, 0.1]),
#                         r_inner=0.05, r_outer=0.1, phi=np.pi/2, theta=np.pi/2)
#lunohod = SphericalSection('Lunohod', Cartesian(origin=[0.1, 0.1, 0.1]),
#                           r_inner=0.05, r_outer=0.1, h1=0.01, h2=0.03)
#moon.add_element(lunohod)

#phobos = Space('Phobos', Cartesian(origin=[0.2, 0.2, 0.2]))
#deimos = Space('Deimos', Cartesian(origin=[-0.2, 0, 0]))
#mars.add_element(phobos)
#mars.add_element(deimos)

fig = mlab.figure('CS demo', bgcolor=(0.5, 0.5, 0.5))  # Create the mayavi figure

@mlab.animate(delay=100)
def anim():
    views = Visual.gen_space_views(fig, solar_system)
    views['Solar System'].set_cs_visible(False)
    views['Sun'].set_cs_visible(False)
    views['Earth'].set_cs_visible(False)
    views['Sun'].set_color((1.0, 1.0, 0.2))
    views['Earth'].set_color((0.0, 0.0, 0.5))
    Visual.draw_space(views)
    #views['Lunohod'].set_wireframe(True)
    #views['Moon'].set_wireframe(True)
    #views['Moon'].set_cs_visible(True)
    while True:
        Visual.draw_space(views)
        earth.coordinate_system.rotate_axis_angle([1, 1, 1], np.deg2rad(1))
        #moon.coordinate_system.rotate_axis_angle([0, 0, 1], np.deg2rad(1))
        yield

anim()
mlab.show()
