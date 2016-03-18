import numpy as np
from mayavi import mlab

from Space.Coordinates import Cartesian
from Space.Curve.Parametric import Helix
from Space.Pathfinder import line_between_two_points, helix_between_two_points, arc_between_two_points
import Space_visualization as Visual

coordinate_system = Cartesian()
coordinate_system.rotate_axis_angle(np.ones(3), np.deg2rad(45))

fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))
Visual.draw_coordinate_system_axes(fig, coordinate_system)

right_helix = Helix(name='Right Helix', coordinate_system=coordinate_system,
                    radius=2, pitch=0.5, start=0, stop=np.pi * 4, right=True)
left_helix = Helix(name='Left Helix', coordinate_system=coordinate_system,
                   radius=2, pitch=0.5, start=0, stop=np.pi * 2, right=False)

print 'Helix length:', left_helix.length()

right_helix_view = Visual.CurveView(fig=fig, curve=right_helix)
right_helix_view.draw()

left_helix_view = Visual.CurveView(fig=fig, curve=left_helix)
left_helix_view.draw()

point1 = np.array([1, 1, 0])
point2 = np.array([2, 2, 0])
points = np.vstack((coordinate_system.to_parent(point1), coordinate_system.to_parent(point2)))
mlab.points3d(points[:, 0], points[:, 1], points[:, 2], scale_factor=0.1)

shortest_path = line_between_two_points(coordinate_system, point1, point2)
shortest_path_view = Visual.CurveView(fig=fig, curve=shortest_path)
shortest_path_view.set_color((0.3, 0.75, 0.2), 0.5)
shortest_path_view.draw()

helix_path = helix_between_two_points(coordinate_system, point1, point2, radius=1, loops=7, right=True)
helix_path_view = Visual.CurveView(fig=fig, curve=helix_path)
helix_path_view.set_color((1, 1, 0), 0.3)
helix_path_view.draw()
helix_path_view.set_cs_visible(False)

arc_path = arc_between_two_points(coordinate_system, point1, point2, radius=1, right=True)
arc_path_view = Visual.CurveView(fig=fig, curve=arc_path)
arc_path_view.set_color((0, 0, 1), 0.7)
arc_path_view.draw()
arc_path_view.set_cs_visible(True)

mlab.show()
