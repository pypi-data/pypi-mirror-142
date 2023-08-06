import os
import numpy as np

import glob

import matplotlib.pyplot as plt

PATH = 'result_twist_2/'

'''
actuations = []
thetas = []
for path in glob.glob(os.path.join(PATH, 'twist_*.npz')):
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
'''

data = np.load(os.path.join(PATH, 'twist_50.npz'))
p = data['position_rod1']
Q = data['director_rod1']

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection="3d")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

for i in range(3):
    ax.quiver(*p, *Q[i], length=0.010)
plt.show()



