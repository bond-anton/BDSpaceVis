from __future__ import division
import numpy as np
from mayavi import mlab

from Space.Coordinates import Cartesian
from Space.Curve.Parametric import Arc
import Space_visualization as Visual

coordinate_system = Cartesian()
fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))
arc = Arc(name='Arc', coordinate_system=coordinate_system, a=1, b=2, start=0, stop=2*np.pi, right=True)
arc_visual = Visual.CurveView(fig, arc, color=(1, 0, 0), thickness=None)
arc_visual.draw()
arc_visual.set_thickness(arc_visual.thickness / 2)
print arc.get_eccentricity()
print arc.get_focus()
mlab.show()
