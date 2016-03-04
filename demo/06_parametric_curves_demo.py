from __future__ import division
import numpy as np
from mayavi import mlab

from Space.Coordinates import Cartesian
from Space.Curve.Parametric import Helix, Arc
import Space_visualization as Visual

coordinate_system = Cartesian()
fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))
arc_right = Arc(name='Arc', coordinate_system=coordinate_system, radius=1, start=np.pi/3, stop=2*np.pi/3, right=True)
arc_left = Arc(name='Arc', coordinate_system=coordinate_system, radius=1, start=np.pi/3, stop=2*np.pi/3, right=False)
arc_visual_right = Visual.CurveView(fig, arc_right, color=(1, 0, 0))
arc_visual_left = Visual.CurveView(fig, arc_left, color=(0, 0, 1))
arc_visual_right.draw()
arc_visual_left.draw()

mlab.show()
