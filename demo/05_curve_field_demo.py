import numpy as np

from BDSpace.Coordinates import Cartesian
from BDSpace import Space
from BDSpace.Curve.Parametric import Helix
from BDSpace.Field import HyperbolicPotentialCurveConservativeField

import BDSpaceVis as Visual
from mayavi import mlab


space = Space('Charged helix Space')
coordinate_system = Cartesian()
coordinate_system.rotate_axis_angle(np.ones(3, dtype=np.double), np.deg2rad(45))
coordinate_system.origin = np.array([0.0, 0.0, 0.0]) + -2.0

left_helix = Helix(name='Left Helix', coordinate_system=coordinate_system,
                   radius=5, pitch=10, start=0, stop=np.pi * 4, right=False)
helix_r = 1.5
print('Helix length:', left_helix.length())
pos_electrostatic_field = HyperbolicPotentialCurveConservativeField(name='Pos Charged Helix field',
                                                                    field_type='electrostatic',
                                                                    curve=left_helix, r=helix_r)
pos_electrostatic_field.a = 1.0

space.add_element(left_helix)

fig = mlab.figure('CS demo', bgcolor=(0.0, 0.0, 0.0))  # Create the mayavi figure

space_view = Visual.SpaceView(fig, space)
space_view.set_cs_visible(True)
space_view.draw()

left_helix_view = Visual.CurveView(fig=fig, curve=left_helix)
left_helix_view.set_color((1.0, 0.0, 0.0), 0.9)
left_helix_view.set_thickness(helix_r)
left_helix_view.set_cs_visible(True)
left_helix_view.draw()

pos_field_vis = Visual.FieldView(fig, pos_electrostatic_field)

grid = np.mgrid[-10:10:11j, -10:10:11j, -10:10:11j]
pos_field_vis.set_grid(grid)
pos_field_vis.set_cs_visible(True)
pos_field_vis.draw()

mlab.show()
