from mayavi import mlab

from BDQuaternions import Conventions, EulerAngles
from BDSpace import Space
from BDSpace.Figure.Sphere import *
from BDSpace.Figure.Cylinder import CylindricalWedge, Cylinder
from BDSpace.Figure.Cone import ConicalWedge
from BDSpace.Figure.Torus import ToricWedge
from BDSpace.Figure.Cube import Parallelepiped, ParallelepipedTriclinic, Cuboid, Cube
from BDSpace.Curve import Arc
from BDSpace.Coordinates import Cartesian
import BDSpaceVis as Visual

fig = mlab.figure('CS demo', bgcolor=(0.5, 0.5, 0.5))  # Create the mayavi figure

convention = Conventions().get_convention('Bunge')
joint_disc_cs = Cartesian(euler_angles_convention=convention)
joint_disc_cs.euler_angles = EulerAngles(np.array([0, np.pi/2, 0], dtype=np.double), convention)

joint_disc = Cylinder(name='Moon', coordinate_system=joint_disc_cs,
                      r_inner=0.0, r_outer=1.5, z=[-1.0, 1.0])
rod = Cylinder(name='Moon', coordinate_system=Cartesian(origin=np.array([0.0, 0.0, 0.0])),
               r_inner=0.3, r_outer=0.5, z=[0.0, 4])
box = ParallelepipedTriclinic(name='Parallelepiped', a=1, b=1, c=1, alpha=np.pi/4, beta=np.pi/4, gamma=np.pi/4)
#wedge = SphericalWedge(r_inner=5, r_outer=7, phi=2*np.pi*0.7, theta=[np.pi/4*0, np.pi/3])
wedge = ConicalWedge(phi=2*np.pi, theta=np.pi/4, z=np.array([0, 1.0]), z_offset=0.4, r_min=0.3)
#wedge = ToricWedge(r_torus=1.0, r_tube=[0.25, 1.5], phi=np.pi, theta=np.array([-np.pi, 0]))
print('V =', wedge.volume())
print('S = ', wedge.surface_area())
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
