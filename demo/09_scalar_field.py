from __future__ import division
import numpy as np
from mayavi import mlab

from Space.Figure.Sphere import Sphere
from Space.Field import Field

import Space_visualization as Visual


charged_ball = Sphere(name='Charged Ball', r_outer=0.5)
electrostatic_field = Field(name='ball field', field_type='electrostatic')
charged_ball.add_element(electrostatic_field)

fig = mlab.figure('CS demo', bgcolor=(0.5, 0.5, 0.5))  # Create the mayavi figure

charged_ball_vis = Visual.FigureView(fig, charged_ball)
charged_ball_vis.draw()

mlab.show()
