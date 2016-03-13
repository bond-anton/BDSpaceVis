from __future__ import division
import numpy as np
from mayavi import mlab

from Space import Space
from Space.Figure.Sphere import *
from Space.Figure.Cylinder import CylindricalWedge, Cylinder
from Space.Figure.Cube import Parallelepiped, ParallelepipedTriclinic, Cuboid, Cube
from Space.Curve.Parametric import Arc
from Space.Coordinates import Cartesian
import Space_visualization as Visual

fig = mlab.figure('CS demo', bgcolor=(0.5, 0.5, 0.5))  # Create the mayavi figure

joint_disc_cs = Cartesian()
joint_disc_cs.set_euler_angles([0, np.pi/2, 0])

joint_disc = Cylinder(name='Moon', coordinate_system=joint_disc_cs,
                      r_inner=0.0, r_outer=1.5, z=[-1.0, 1.0])
rod = Cylinder(name='Moon', coordinate_system=Cartesian(origin=[0.0, 0.0, 0.0]),
               r_inner=0.3, r_outer=0.5, z=[0.0, 4])
box = ParallelepipedTriclinic(name='Parallelepiped', a=1, b=1, c=1, alpha=np.pi/4, beta=np.pi/4, gamma=np.pi/4)
wedge = SphericalWedge(r_inner=0.5, phi=2*np.pi*0.7, theta=[np.pi/4*0, np.pi/3])
print 'V =', wedge.volume()
print 'S = ', wedge.surface_area()
joint_vis = Visual.FigureView(fig, joint_disc, color=(0, 1, 0))
rod_vis = Visual.FigureView(fig, rod)
box_vis = Visual.FigureView(fig, box)
wedge_vis = Visual.FigureView(fig, wedge)

#joint_vis.draw()
#rod_vis.draw()
#box_vis.set_wireframe(True)
#box_vis.draw()

wedge_vis.set_wireframe(True)
wedge_vis.draw()

mlab.show()
