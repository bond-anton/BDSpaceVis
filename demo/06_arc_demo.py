import numpy as np
from mayavi import mlab

from BDSpace.Coordinates import Cartesian
from BDSpace.Curve.Parametric import Arc
import BDSpaceVis as Visual

coordinate_system = Cartesian()
fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))
arc = Arc(name='Arc', coordinate_system=coordinate_system, a=1, b=2, start=0, stop=2*np.pi, right=True)
arc_visual = Visual.CurveView(fig, arc, color=(1, 0, 0), thickness=None)
arc_visual.draw()
arc_visual.set_thickness(arc_visual.thickness / 2)
print(arc.eccentricity())
print(arc.focus())
mlab.show()
