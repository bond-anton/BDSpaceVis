import numpy as np
from mayavi import mlab

from BDSpace.Figure.Sphere import Sphere
from BDSpace.Field import Field, SuperposedField
from BDSpace.Coordinates import transforms as gt

import BDSpaceVis as Visual


class ChargedBall(Field):

    def __init__(self, q, r, name='Charged ball field', field_type='electrostatic'):
        self.r = r
        self.q = q
        super(ChargedBall, self).__init__(name, field_type)

    def scalar_field(self, xyz):
        rtp = np.asarray(gt.cartesian_to_spherical(xyz))
        rtp[np.where(rtp[:, 0] < self.r), 0] = self.r
        return self.q / rtp[:, 0]

    def vector_field(self, xyz):
        rtp = np.asarray(gt.cartesian_to_spherical(xyz))
        rtp[np.where(rtp[:, 0] < self.r), 0] = self.r
        r = rtp[:, 0] ** 2
        r = np.array([r, r, r]).T
        return self.q * np.asarray(xyz) / r

pos_charged_ball = Sphere(name='Pos Charged Ball', r_outer=1.0)
pos_charged_ball.coordinate_system.origin += np.array([-5, 0, 0])
pos_electrostatic_field = ChargedBall(q=1, r=1, name='Pos Charged ball field', field_type='electrostatic')
pos_charged_ball.add_element(pos_electrostatic_field)

fig = mlab.figure('CS demo', bgcolor=(0.0, 0.0, 0.0))  # Create the mayavi figure

pos_charged_ball_vis = Visual.FigureView(fig, pos_charged_ball)
pos_charged_ball_vis.set_color((1, 0, 0))
pos_charged_ball_vis.draw()

pos_ball_field_vis = Visual.FieldView(fig, pos_electrostatic_field)

grid = np.mgrid[-10:10:20j, -10:10:20j, -5:5:10j]

pos_ball_field_vis.set_grid(grid)
#pos_ball_field_vis.set_cs_visible(False)

pos_ball_field_vis.draw()

mlab.show()
