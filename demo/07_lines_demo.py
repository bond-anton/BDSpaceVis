from __future__ import division, print_function
import numpy as np
from mayavi import mlab

from Space.Coordinates import Cartesian
from Space.Curve.Parametric import Line
import Space_visualization as Visual

coordinate_system = Cartesian()
fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))
line = Line(name='Line', coordinate_system=coordinate_system, a=1, b=2, c=0, start=0, stop=1)
line_visual = Visual.CurveView(fig, line, color=(1, 0, 0), thickness=None)
line_visual.draw()
line_visual.set_thickness(line_visual.thickness / 2)
mlab.show()
