import numpy as np
from mayavi import mlab

from BDQuaternions import Conventions
from BDSpace.Coordinates import Cartesian
import BDSpaceVis as Visual

# Create cartesian coordinate system
CS = Cartesian()
convention = Conventions().get_convention('Bunge')
CS.euler_angles_convention = convention


# to visualise the coordinate system basis the module Visual is used

fig = mlab.figure('CS demo', bgcolor=(0.5, 0.5, 00.5))  # Create the mayavi figure
#Visual.draw_coordinate_system_axes(fig, CS)
cube_surface, arrows, labels = Visual.draw_coordinate_system_box(fig, CS, scale=1)
CS.rotate_euler_angles(np.array([np.pi, 0, 0]))
CS.rotate_euler_angles(np.array([np.pi * 0.5, 0, 0]))
CS.rotate_euler_angles(np.array([np.pi * 0.5, 0, 0]))
CS.rotate_euler_angles(np.array([0, np.pi * 0.5, 0]))
CS.rotate_euler_angles(np.array([0, np.pi * 0.5, 0]))
CS.rotate_euler_angles(np.array([0, np.pi * 0.5, 0]))
CS.rotate_euler_angles(np.array([0, np.pi * 0.5, 0]))
CS.rotate_axis_angle(np.array([1, 1, 1], dtype=np.double), np.deg2rad(60))
CS.rotate_axis_angle(np.array([1, 0, 0], dtype=np.double), np.pi * 0.5)
print(CS.euler_angles)
#CS.rotate_axis_angle(np.array([1, 0, 0]), np.pi * 0.5)
#print CS.euler_angles
cube_surface, arrows, labels = Visual.update_coordinate_system_box(CS, cube_surface, arrows, labels, scale=1)
mlab.show()  # start mayavi
