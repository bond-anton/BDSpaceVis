from coordinate_system import *


def euler_color(euler_angles):
    return euler_angles[0] / (np.pi * 2), euler_angles[1] / np.pi, euler_angles[2] / (np.pi * 2)
