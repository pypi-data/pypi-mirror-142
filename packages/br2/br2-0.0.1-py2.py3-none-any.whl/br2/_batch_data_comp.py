import numpy as np
import scipy as sp
import os, sys
import glob

from scipy.interpolate import interp1d

from matplotlib import pyplot as plt
from matplotlib.colors import to_rgb
from mpl_toolkits.mplot3d import proj3d, Axes3D

"""
Compare batch run data to get k and kt for each bending experiment
"""
def rotate_point_around_point_2D(point, center, angle_ccw):
    s = np.sin(angle_ccw)
    c = np.cos(angle_ccw)

    point -= center
    point = np.array([point[0] * c - point[1] * s, point[0] * s + point[1] * c])
    point += center
    return point

def three_ring_xz_converter(loc_idx):
    # Geometry
    thickness = 0.002
    r = 0.006522 + thickness
    up = np.array([-r, 0.0])
    left = np.array([0.0, -r])
    right= np.array([0.0, r])
    center = np.array([r/np.cos(np.pi/6), 0])

    # Location
    if loc_idx == 1:
        pz = left
    elif loc_idx == 2:
        pz = rotate_point_around_point_2D(right, center, 2*np.pi/3)
    elif loc_idx == 3:
        pz = rotate_point_around_point_2D(up, center, 2*np.pi/3)
    elif loc_idx == 4:
        pz = rotate_point_around_point_2D(left, center, 2*np.pi/3)
    elif loc_idx == 5:
        pz = rotate_point_around_point_2D(right, center, -2*np.pi/3)
    elif loc_idx == 6:
        pz = rotate_point_around_point_2D(up, center, -2*np.pi/3)
    elif loc_idx == 7:
        pz = rotate_point_around_point_2D(left, center, -2*np.pi/3)
    elif loc_idx == 8:
        pz = right
    else:
        raise NotImplementedError
    return pz

def three_ring_xyz_converter(label):
    """
    Three-ring cross-sectional plane on BR2 (07/05/21)
    """
    # Geometry
    thickness = 0.001
    r = 0.007522 + thickness # Radius of tube
    R = 0.016 # Radius of disc holder
    up = np.array([-R+r/np.cos(np.pi/6), 0.0])
    center = np.array([r/np.cos(np.pi/6), 0])
    
    vec = np.zeros([3])

    base_char = label[0]; label = label[1:]
    if base_char == 'R':
        y_idx, loc_idx = label.split('-')
        y_idx = int(y_idx) - 1
        loc_idx = int(loc_idx)
        # y
        pz = three_ring_xz_converter(loc_idx)
        vec[0] = pz[0]
        vec[2] = pz[1]
    elif base_char == 'S':
        loc_idx = int(label)
        vec[1] = 0
        if loc_idx == 0:
            pz = rotate_point_around_point_2D(up, center, np.pi/3)
        elif loc_idx == 1:
            pz = rotate_point_around_point_2D(up, center, np.pi)
        vec[0] = pz[0]
        vec[2] = pz[1]
    else:
        raise NotImplementedError

    return vec

def get_coordf(labels:list, ps, Qs):
    # Return comparable dictionary 
    return_points = []
    for label in labels:
        y_idx = int(label[1])-1
        p = ps[...,y_idx]
        Q = Qs[...,y_idx]
        local_position = three_ring_xyz_converter(label)
        return_points.append((Q.T @ local_position) + p)
    return np.array(return_points)

ring_space=np.cumsum([0.0239, 0.03517, 0.03382, 0.03455, 0.03280])

runid = 2

PATH = 'result_batchrun_br2_1'
result_paths = glob.glob(os.path.join(PATH, 'br2_data_*_*.npz'))
experiment_path = '../../br2-dlt/data_070521/postprocess/run-{}-position.npz'.format(runid)
experiment_data = np.load(experiment_path)
ref_points_exp = experiment_data['position'][:,-1,:] # Last timestamp data
ref_tags = experiment_data['tags']

ref_center_point = experiment_data['cross_section_center_position'][-1]
ref_center_normal = experiment_data['cross_section_normal_vector'][-1]

result_tuples = []
for result_path in result_paths:
    data = np.load(result_path)
    basename = os.path.basename(result_path)
    kt_idx = int(basename.split('.')[0].split('_')[-1])
    positions_rod1 = data['position_rod1']
    directors_rod1 = data['director_rod1']
    if positions_rod1.shape[0] < 20: # Run at least 1 sec of simulation
        continue

    # Define loss function : find simulated reference point (primary comparison)
    # Find reference length for each position
    initial_space = data['position_rod1'][0,1,:]
    sim_rod_cs_position = interp1d(initial_space, positions_rod1[-1,...])(ring_space)
    sim_rod_cs_director = interp1d(initial_space, directors_rod1[-1,...])(ring_space)
    sim_rod_cs_tangent = sim_rod_cs_director[2,...]

    ref_points_sim = get_coordf(ref_tags, sim_rod_cs_position, sim_rod_cs_director)
    loss = np.linalg.norm(ref_points_exp - ref_points_sim, axis=1).mean()
    #result_tuples.append((loss, basename, positions_rod1.shape[0]))

    # Interpolate position and director and ring_space (secondary comparison)
    #compare position and tangent vector to simulated result
    positions_mean = np.mean([data['position_rod1'], data['position_rod2'], data['position_rod3']], axis=0)
    directors_mean = np.mean([data['director_rod1'], data['director_rod2'], data['director_rod3']], axis=0)
    sim_rod_cs_center_position = interp1d(initial_space, positions_mean[-1,...])(ring_space)
    sim_rod_cs_center_director = interp1d(initial_space, directors_mean[-1,...])(ring_space)
    sim_rod_cs_center_normal = sim_rod_cs_center_director[2,...]
    result_tuples.append([
        np.linalg.norm(sim_rod_cs_center_position - ref_center_point, axis=1).mean(),
        basename,
        positions_rod1.shape[0]
    ])
    ''' 
    fig = plt.figure(1, figsize=(10, 8))
    ax = plt.axes(projection="3d")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.scatter(*sim_rod_cs_center_position)
    ax.scatter(*ref_center_point)
    plt.show()
    break
    ''' 

result_tuples.sort()
for e in result_tuples[::-1]:
    print(e)

