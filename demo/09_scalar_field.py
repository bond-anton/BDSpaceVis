from __future__ import division
import numpy as np
from mayavi import mlab

from Space.Figure.Sphere import Sphere
from Space.Field import Field

import Space_visualization as Visual


class ChargedBall(Field):

    def scalar_field(self, xyz):
        #print len(xyz.shape)
        x, y, z = xyz[0], xyz[1], xyz[2]
        r2 = x**2 + y**2 + z**2
        return 1e3 / r2

    def vector_field(self, xyz):
        x, y, z = xyz[0], xyz[1], xyz[2]
        return x+y+z

charged_ball = Sphere(name='Charged Ball', r_outer=0.5)
electrostatic_field = ChargedBall(name='ball field', field_type='electrostatic')
charged_ball.add_element(electrostatic_field)

#fig = mlab.figure('CS demo', bgcolor=(0.5, 0.5, 0.5))  # Create the mayavi figure
fig = mlab.figure('CS demo', bgcolor=(0.0, 0.0, 0.0))  # Create the mayavi figure

charged_ball_vis = Visual.FigureView(fig, charged_ball)
#charged_ball_vis.draw()
ball_field_vis = Visual.FieldView(fig, electrostatic_field)
grid = np.mgrid[-10:10:100j, -20:20:200j, -10:10:100j]
ball_field_vis.set_grid(grid)
ball_field_vis.set_cs_visible(False)
ball_field_vis.draw()
#charged_ball_vis.draw()
ball_field_vis.draw()
#ball_field_vis.draw()

mlab.show()
