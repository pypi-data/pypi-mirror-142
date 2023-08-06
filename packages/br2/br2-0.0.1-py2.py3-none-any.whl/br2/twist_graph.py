import os
import sys
from collections import deque
import numpy as np
import argparse
import math
import imutils
import cv2
import matplotlib
import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit
from numpy.linalg import eig, inv
from skimage.morphology import skeletonize, thin
from skimage.util import invert
from scipy.spatial import distance
from scipy import interpolate as intp

from PIL import Image

from scipy import optimize
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin
import matplotlib.animation as manimation
from collections import Counter

#datapoint = np.array([114,145,212,144,177,210,205])*np.pi/180.0
#print(datapoint)

SUPPORT_VIDEO_FORMAT = ['mp4']

#path = './batch_twist_100/18'
#path = './batch_twist_100/30'
path = './batch_twist'
t_list = []
angles_list = []
for idx in range(200):
    file_name = os.path.join(path, f'twist_3d_{idx}.npz')
    try:
        log = np.load(file_name)
    except:
        continue
    position = log['position']
    Q = log['Q']
    qo = Q[:,:,0]
    qf = Q[:,:,-1]
    angles = np.arccos((Q[:,:,:-1] * Q[:,:,1:]).sum(axis=1)).sum(axis=1)
    #cos = (qo*qf).sum(axis=1)
    #cos[cos>=1.0] = 1.0 - 1e-6
    #cos[cos<=-1.0] = -1.0 + 1e-6
    #angles = np.arccos(cos)
    #if idx * 0.1 > 5.0:
    #    angles[:2] = 2*np.pi + angles[:2]
    #elif idx * 0.1 > 2.5:
    #    angles[:2] = 2*np.pi - angles[:2]

    t_list.append(idx*0.1)
    angles_list.append(angles)


tau = np.array(t_list)
angles = np.array(angles_list)
datapoint = np.array([248, 380, 455, 504, 555])*np.pi/360.0
print(datapoint)

interp = intp.interp1d(angles[:,0], tau)(datapoint)
for data, pred_tau in zip(datapoint, interp):
    print(f'{data}: {pred_tau}')
np.savez(
    'twist_result.npz',
    video_label_60=[2027,2028,2029,2030,2031],
    simul_torque_60=interp.tolist(),
    pressure_60=[10,15,20,25,30]
)
sys.exit()
applied_p = np.array([10,15,20,25,30])
plt.plot(applied_p, interp, '-o')
plt.title('Applied Pressure vs Simulated Torque')
plt.xlabel('pressure (psi)')
plt.ylabel('torque')
plt.legend(['fa-60'])
plt.savefig('pressure_torque.png')
plt.show()
sys.exit()
print(angles.shape)
plt.plot(tau, angles[:,0], '-o')
plt.plot(tau, angles[:,1], '-x')
plt.plot(tau, angles[:,2], '-*')
plt.legend(['d1', 'd2', 'd3'])
plt.xlabel('tau')
plt.ylabel('angle')
plt.savefig('twist_angle.png')
plt.show()
plt.close(plt.gcf())
