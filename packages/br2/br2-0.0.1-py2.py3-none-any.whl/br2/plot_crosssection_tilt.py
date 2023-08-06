import os, sys
sys.path.append("../")
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d, Axes3D
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import to_rgb

from scipy import interpolate

import numpy as np
from numpy import cos, sin, sqrt
from elastica.joint import FreeJoint
from elastica.utils import Tolerance

# Join the two rods
from elastica._linalg import _batch_norm, _batch_cross, _batch_matvec, _batch_dot, _batch_matmul, _batch_matrix_transpose
from elastica._rotations import _get_rotation_matrix
from elastica._elastica_numba._interaction import (
    elements_to_nodes_inplace,
    node_to_element_pos_or_vel,
)

from elastica._elastica_numpy._rotations import _inv_skew_symmetrize

from surface_connection_parallel_rod_numba import _inv_rotate2

result_path = 'result_br2_6'
data = np.load(os.path.join(result_path, 'br2_data.npz'))

'''
def normal(a, b, c, direction):
    vec = np.cross(a-b, b-c, 0, 0)
    vec /= np.linalg.norm(vec, axis=1, keepdims=1)
    return vec

# Initial plane vector (t=0)
t = 0
position_rod1 = data['position_rod1']
position_rod2 = data['position_rod2']
position_rod3 = data['position_rod3']
standard_normal = normal(
    position_rod1[t][:,-1:],
    position_rod2[t][:,-1:],
    position_rod3[t][:,-1:],
    np.array([0,1,0])
)

# Last plane vectors (t=-1)
t = -1
position_rod1 = data['position_rod1']
position_rod2 = data['position_rod2']
position_rod3 = data['position_rod3']
plane_normal = normal(
    position_rod1[t],
    position_rod2[t],
    position_rod3[t],
    np.array([0,1,0])
)
print(standard_normal)

# Plot
plt.plot(plane_normal - standard_normal)
plt.show()
'''

director = np.mean([data['director_rod1'], data['director_rod2'], data['director_rod3']], axis=0)
position = np.mean([data['position_rod1'], data['position_rod2'], data['position_rod3']], axis=0)
position[:,[0,1,2],:] = position[:,[2,0,1],:]
director[:,:,[0,1,2],:] = director[:,:,[2,0,1],:]
interpolation_length = np.cumsum([0.0239, 0.03517, 0.03382, 0.03455, 0.0328])
num_frame = director.shape[0]
print(director.shape)
print(position.shape)

# Animation director
for t in range(num_frame):
    p = position[t]
    d = director[t]
    interp_d = interpolate.interp1d(np.linalg.norm(p,axis=0), d)(interpolation_length)
    interp_p = interpolate.interp1d(np.linalg.norm(p,axis=0), p)(interpolation_length)

    fig = plt.figure(1, figsize=(10, 8), frameon=True)
    ax = plt.axes(projection="3d")

    ax.set_xlabel("z")
    ax.set_ylabel("x")
    ax.set_zlabel("y")

    ax.set_xlim((-0.13, 0.13))
    ax.set_ylim((-0.13, 0.13))
    ax.set_zlim((0.00, 0.3))

    _length = 0.02
    ax.quiver(*interp_p, *interp_d[0], length=_length)
    ax.quiver(*interp_p, *interp_d[1], length=_length)
    ax.quiver(*interp_p, *interp_d[2], length=_length)
    plt.savefig('render/image_{:04d}.png'.format(t))
    #plt.show()
    plt.close('all')

sys.exit()
