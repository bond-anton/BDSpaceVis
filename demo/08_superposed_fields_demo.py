import numpy as np

from BDSpace import Space
from BDSpace.Figure.Sphere import Sphere
from BDSpace.Curve.Parametric import Arc
from BDSpace.Field import ConstantVectorConservativeField, SuperposedField
from BDSpace.Field import HyperbolicPotentialSphericalConservativeField
from BDSpace.Field import HyperbolicPotentialCurveConservativeField

import BDSpaceVis as Visual

from mayavi import mlab

space = Space('Two charged balls')
pos_ball_position = np.array([5.0, 5.0, 0.0], dtype=np.double)
neg_ball_position = np.array([-5.0, -5.0, 0.0], dtype=np.double)
loop_position = np.array([0.0, 0.0, 0.0], dtype=np.double)

pos_ball_charge = 5.0
pos_ball_radius = 1.0
pos_charged_ball = Sphere(name='Pos Charged Ball', r_outer=pos_ball_radius)
pos_charged_ball.coordinate_system.origin = pos_ball_position

neg_ball_charge = -5.0
neg_ball_radius = 1.0
neg_charged_ball = Sphere(name='Neg Charged Ball', r_outer=neg_ball_radius)
neg_charged_ball.coordinate_system.origin = neg_ball_position

loop_linear_charge = 1.0
loop_radius = 1.0
loop_r = 0.5
loop = Arc(name='charged wire loop', a=loop_radius, b=loop_radius, start=0.0, stop=np.pi * 2, right=True)
loop.coordinate_system.origin = loop_position

space.add_element(pos_charged_ball)
space.add_element(neg_charged_ball)
space.add_element(loop)



pos_electrostatic_field = HyperbolicPotentialSphericalConservativeField(name='Pos Charged ball field',
                                                                        field_type='electrostatic',
                                                                        a=pos_ball_charge, r=pos_ball_radius)
pos_charged_ball.add_element(pos_electrostatic_field)

neg_electrostatic_field = HyperbolicPotentialSphericalConservativeField(name='Neg Charged ball field',
                                                                        field_type='electrostatic',
                                                                        a=neg_ball_charge, r=neg_ball_radius)
neg_charged_ball.add_element(neg_electrostatic_field)

loop_field = HyperbolicPotentialCurveConservativeField(name='Pos Charged Loop field',
                                                       field_type='electrostatic',
                                                       curve=loop, r=loop_r)
loop_field.a = loop_linear_charge

fields_superposition = SuperposedField('Field of two charged balls', [pos_electrostatic_field,
                                                                      neg_electrostatic_field,
                                                                      loop_field])

space.add_element(fields_superposition)

fig = mlab.figure('CS demo', bgcolor=(0.0, 0.0, 0.0))  # Create the mayavi figure

pos_charged_ball_vis = Visual.FigureView(fig, pos_charged_ball)
pos_charged_ball_vis.set_color((1, 0, 0))
pos_charged_ball_vis.draw()

neg_charged_ball_vis = Visual.FigureView(fig, neg_charged_ball)
neg_charged_ball_vis.set_color((0, 0, 1))
neg_charged_ball_vis.draw()

loop_vis = Visual.CurveView(fig, loop)
loop_vis.set_color((1, 0, 0))
loop_vis.set_thickness(loop_r)
loop_vis.draw()

fields_superposition_vis = Visual.FieldView(fig, fields_superposition, scalar_field_visible=False)

# pos_ball_field_vis = Visual.FieldView(fig, pos_electrostatic_field)
# neg_ball_field_vis = Visual.FieldView(fig, neg_electrostatic_field)

grid = np.mgrid[-10:10:40j, -10:10:40j, -5:5:10j]

fields_superposition_vis.set_grid(grid)
fields_superposition_vis.set_cs_visible(False)
fields_superposition_vis.set_scale_factor(2.0)
fields_superposition_vis.draw()
fields_superposition_vis.set_scale_factor(0.5)

# pos_ball_field_vis.set_grid(grid)
# pos_ball_field_vis.set_cs_visible(False)
# pos_ball_field_vis.draw()

# neg_ball_field_vis.set_grid(grid)
# neg_ball_field_vis.set_cs_visible(False)
# neg_ball_field_vis.draw()

mlab.show()