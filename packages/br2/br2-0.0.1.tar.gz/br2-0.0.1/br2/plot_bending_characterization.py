import os
import numpy as np

import glob

import matplotlib.pyplot as plt

PATH = 'result_bending_1/'

actuations = []
thetas = []
for path in glob.glob(os.path.join(PATH, 'bending_*.npz')):
    bending_actuation = int(os.path.basename(path).split('_')[-1].split('.')[0])
    actuations.append(bending_actuation)

    data = np.load(path)
    p = data['position_rod1'][...,-1]
    Q = data['director_rod1'][...,-1]
    tangent = Q[2]
    y_axis = np.array([0,1,0])
    theta = np.arccos(np.dot(tangent, y_axis))
    thetas.append(theta*180/np.pi)

plt.plot(actuations, thetas, '.')
plt.show()



