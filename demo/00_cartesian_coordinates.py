#!/bin/env python

from __future__ import division, print_function
import numpy as np
from mayavi import mlab

from Space.Coordinates import Cartesian
import Space_visualization as Visual

# Create cartesian coordinate system

CS = Cartesian(euler_angles_convention='Bunge')  # if you don't pass arguments the basis coincide with 'Absolute' (mayavi) coordinate system

# to visualise the coordinate system basis the module Visual is used

fig = mlab.figure('CS demo', bgcolor=(0.5, 0.5, 00.5))  # Create the mayavi figure
#Visual.draw_coordinate_system_axes(fig, CS)
cube_surface, arrows, labels = Visual.draw_coordinate_system_box(fig, CS, scale=1)
CS.rotate_euler_angles([np.pi, 0, 0])
CS.rotate_euler_angles([np.pi * 0.5, 0, 0])
CS.rotate_euler_angles([np.pi * 0.5, 0, 0])
CS.rotate_euler_angles([0, np.pi * 0.5, 0])
CS.rotate_euler_angles([0, np.pi * 0.5, 0])
CS.rotate_euler_angles([0, np.pi * 0.5, 0])
CS.rotate_euler_angles([0, np.pi * 0.5, 0])
CS.rotate_axis_angle(np.array([1, 1, 1]), np.deg2rad(60))
#CS.rotate_axis_angle(np.array([1, 0, 0]), np.pi * 0.5)
print(CS.euler_angles)
#CS.rotate_axis_angle(np.array([1, 0, 0]), np.pi * 0.5)
#print CS.euler_angles
cube_surface, arrows, labels = Visual.update_coordinate_system_box(CS, cube_surface, arrows, labels, scale=1)
mlab.show()  # start mayavi
