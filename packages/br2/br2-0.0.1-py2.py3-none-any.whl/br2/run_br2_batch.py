import multiprocessing
from multiprocessing import Process, Pool
import subprocess
from subprocess import call
import os
import time

import sys
import copy

import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import minimize
from functools import partial
from tqdm import tqdm

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

sys.path.append("../") # For elastica
#sys.settrace
from set_environment_br2 import (
    Environment,
)

def main(actuation):
    PATH = 'result_batchrun_br2_1'
    os.makedirs(PATH, exist_ok=1)
    # Downsampling
    target_fps = 20  # Targeted frames per second: comparison made at each frames
    simulation_time = 5  # total simulation time
    simulation_frames = int(simulation_time * target_fps)
    print(f'simulation time (sec): {simulation_time}')
    print(f'simulation frames: {simulation_frames}')

    # Set simulation final time
    env = Environment(
        final_time=simulation_time,
        fps=target_fps,
        COLLECT_DATA_FOR_POSTPROCESSING=True,
    )
    actuation_tag = actuation[3]
    kt_multiplier = actuation[4]
    actuation = actuation[:3]

    # Reset the environment before the new episode and get total number of simulation steps
    total_steps, systems = env.reset(kt_multiplier=kt_multiplier)
    print(f'Total simulation steps: {total_steps}')

    # Simulation loop starts
    reward = 0.0
    done = False

    # Simulation
    save_interval = 500000
    time = np.float64(0.0)
    i_sim = 0
    #for i_sim in range(1, simulation_frames):
    while not done:
        i_sim += 1

        # Simulation
        #time, systems, reward, done = step_wrapper(env, time, next_time, actuation)
        time, systems, reward, done = env.step(actuation, time, nan_check=0)

        # Post-processing
        if done or i_sim % save_interval == save_interval-1:
            # Make a video of octopus for current simulation episode. Note that
            # in order to make a video, COLLECT_DATA_FOR_POSTPROCESSING=True
            env.save_data(os.path.join(PATH, 'br2_data_{}.npz'.format(actuation_tag)))

        # If done=True, NaN detected in simulation.
        # Exit the simulation loop before, reaching final time
        if done:
            print("    Episode finished after {} ".format(time))
            break
    # Simulation loop ends
    print("    Final time of simulation is : ", time)
    return 0

if __name__ == '__main__':
    # Actuation Profile

    actuations = []
    twist = 0.0
    for bend in range(0,1000,50):
        for kt_multiplier in range(0,100, 5):
            actuations.append([bend, 0.0, twist/10.0, '{}_{}'.format(int(bend), int(kt_multiplier)), kt_multiplier])
    # Run
    pool = Pool(processes=6)
    result_objs = []
    for actuation in actuations:
        result = pool.apply_async(main, args=(actuation,))
        #result = pool.apply(main, args=(actuation,))
        result_objs.append(result)
        time.sleep(1.0)
    results = [result.get() for result in result_objs]
    #main(actuation)
