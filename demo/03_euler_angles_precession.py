#!/bin/env python

import numpy as np
from mayavi import mlab

from Space.Coordinates import Cartesian
import Space_visualization as Visual

# Create cartesian coordinate system

# if you don't pass arguments the basis coincide with 'Absolute' (mayavi) coordinate system
CS_1 = Cartesian(origin=np.array([0, 0, 0]))
CS_2 = Cartesian(origin=np.array([0, 0, 0]))
step_prec = 1.0  # in degrees
step_rot = 1.0  # in degrees
direction_prec = 1
direction_rot = 1
Phi = 30  # tilt in degrees
CS_1.set_euler_angles(CS_1.euler_angles + np.array([0, np.deg2rad(Phi), 0]))  # tilt the CS
# to visualise the coordinate system basis the module Visual is used

fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))  # Create the mayavi figure

cs_box_1, arrows_1, labels_1 = Visual.draw_coordinate_system_box(fig, CS_1, draw_labels=True)
arrows_2, labels_2 = Visual.draw_coordinate_system_axes(fig, CS_2, scale=2, draw_labels=True)

@mlab.show
@mlab.animate(delay=10)
def anim():
    while 1:
        delta_eulers = np.array([direction_prec * np.deg2rad(step_prec), 0, direction_rot * np.deg2rad(step_rot)])
        CS_1.set_euler_angles(CS_1.euler_angles + delta_eulers)
        Visual.update_coordinate_system_box(CS_1, cs_box_1, arrows_1, labels_1)
        yield

anim()
