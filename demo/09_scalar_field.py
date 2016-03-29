from __future__ import division
import numpy as np
from mayavi import mlab

from Space.Figure.Sphere import Sphere
from Space.Field import Field, SuperposedField
from Space.Coordinates import transforms as gt

import Space_visualization as Visual

class ChargedBall(Field):

    def __init__(self, q, r, name='Charged ball field', field_type='electrostatic'):
        self.r = r
        self.q = q
        super(ChargedBall, self).__init__(name, field_type)

    def scalar_field(self, xyz):
        rtp = gt.cartesian_to_spherical(xyz)
        rtp[np.where(rtp[:, 0] < self.r), 0] = self.r
        return self.q / rtp[:, 0]

    def vector_field(self, xyz):
        rtp = gt.cartesian_to_spherical(xyz)
        rtp[np.where(rtp[:, 0] < self.r), 0] = self.r
        r = rtp[:, 0] ** 2
        r = np.array([r, r, r]).T
        return -self.q * xyz / r

pos_charged_ball = Sphere(name='Pos Charged Ball', r_outer=1.0)
pos_charged_ball.coordinate_system.origin += np.array([-5, 0, 0])
pos_electrostatic_field = ChargedBall(q=1, r=1, name='pos ball field', field_type='electrostatic')
pos_charged_ball.add_element(pos_electrostatic_field)

neg_charged_ball = Sphere(name='Neg Charged Ball', r_outer=1.0)
neg_charged_ball.coordinate_system.origin += np.array([5, 0, 0])
neg_electrostatic_field = ChargedBall(q=-1, r=1, name='neg ball field', field_type='electrostatic')
neg_charged_ball.add_element(neg_electrostatic_field)



#fig = mlab.figure('CS demo', bgcolor=(0.5, 0.5, 0.5))  # Create the mayavi figure
fig = mlab.figure('CS demo', bgcolor=(0.0, 0.0, 0.0))  # Create the mayavi figure

pos_charged_ball_vis = Visual.FigureView(fig, pos_charged_ball)
pos_charged_ball_vis.set_color((1, 0, 0))
neg_charged_ball_vis = Visual.FigureView(fig, neg_charged_ball)
pos_charged_ball_vis.set_color((0, 0, 1))
pos_charged_ball_vis.draw()
neg_charged_ball_vis.draw()

#pos_ball_field_vis = Visual.FieldView(fig, pos_electrostatic_field)
#neg_ball_field_vis = Visual.FieldView(fig, neg_electrostatic_field)

grid = np.mgrid[-10:10:10j, -5:5:10j, -5:5:10j]

#pos_ball_field_vis.set_grid(grid)
#pos_ball_field_vis.set_cs_visible(False)

#neg_ball_field_vis.set_grid(grid)
#neg_ball_field_vis.set_cs_visible(False)

superposed_field = SuperposedField('Superposed Field', [pos_electrostatic_field, neg_electrostatic_field])
#print superposed_field.scalar_field(np.array([[1,1,1], [2,2,2]]))
superposed_field_vis = Visual.FieldView(fig, superposed_field)
superposed_field_vis.set_grid(grid)
superposed_field_vis.set_cs_visible(False)
superposed_field_vis.draw()

#pos_ball_field_vis.draw()
#neg_ball_field_vis.draw()



mlab.show()
