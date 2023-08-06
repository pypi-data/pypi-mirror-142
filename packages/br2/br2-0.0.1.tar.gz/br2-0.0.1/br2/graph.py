import sys
import matplotlib.pyplot as plt
import numpy as np

legend = ['fa-65', 'fa-70', 'fa-75', 'fa-80', 'fa-85']
label_65 = [1795, 1796, 1797, 1798, 1799]
p_65 = [15,20,25,30,35]
f_65 = [300,390,480,600,730]
label_70 = [1801,1802,1803,1804]
p_70 = [15,20,25,30]
f_70 = [390,590,820,970]
label_75 = [1808, 1809]
p_75 = [15,20]
f_75 = [710, 970]
label_80 = [1812, 1813, 1814]
p_80 = [10,15,20]
f_80 = [310,590,840]
label_85 = [1816, 1817]
p_85 = [10,15]
f_85 = [390,750]

np.savez(
    'bending_result.npz',
    video_label_65=label_65,
    pressure_65=p_65,
    simul_force_65=f_65,
    video_label_70=label_70,
    pressure_70=p_70,
    simul_force_70=f_70,
    video_label_75=label_75,
    pressure_75=p_75,
    simul_force_75=f_75,
    video_label_80=label_80,
    pressure_80=p_80,
    simul_force_80=f_80,
    video_label_85=label_85,
    pressure_85=p_85,
    simul_force_85=f_85,
)
sys.exit()


plt.plot(p_65, f_65, 'o-', markersize=8)
plt.plot(p_70, f_70, '+-', markersize=8)
plt.plot(p_75, f_75, '*-', markersize=8)
plt.plot(p_80, f_80, '^-', markersize=8)
plt.plot(p_85, f_85, 'x-', markersize=8)
plt.title('Actuation(psi) vs Simulation(N)')
plt.xlabel('Actuation (psi)')
plt.ylabel('Force (simulated N)')
plt.grid()
plt.legend(legend)
plt.savefig('datapoints.png')
