import multiprocessing
from multiprocessing import Process, Pool
import subprocess
from subprocess import call
import os
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
sys.settrace
from set_environment_double_br2 import (
    Environment,
)

# Setup Slack
try:
    from slack import WebClient
    if 'SLACK_BOT_TOKEN' in os.environ:
        # SlackBot token is available
        SLACK = True
    else:
        SLACK = False
except ImportError:
    SLACK = False

PATH = 'result_double_br2_4'
os.makedirs(PATH, exist_ok=1)

# Downsampling
target_fps = 20  # Targeted frames per second: comparison made at each frames
simulation_time = 5  # total simulation time
simulation_frames = int(simulation_time * target_fps)
print(f'simulation time (sec): {simulation_time}')
print(f'simulation frames: {simulation_frames}')

def main(actuation):
    # Set simulation final time
    env = Environment(
        final_time=simulation_time,
        fps=target_fps,
        COLLECT_DATA_FOR_POSTPROCESSING=True,
    )

    # Reset the environment before the new episode and get total number of simulation steps
    total_steps, systems = env.reset("config1.json")
    print(f'Total simulation steps: {total_steps}')

    # Simulation loop starts
    user_defined_condition = False
    reward = 0.0
    done = False

    # Simulation
    save_interval = 500000
    pbar_update_interval = 5000
    with tqdm(total=simulation_time) as pbar:
        prev_time = 0
        time = np.float64(0.0)
        i_sim = 0
        #for i_sim in range(1, simulation_frames):
        while not done:
            i_sim += 1

            # Simulation
            #time, systems, reward, done = step_wrapper(env, time, next_time, actuation)
            time, systems, reward, done = env.step(actuation, time, nan_check=0)

            # Progress bar update
            if (i_sim + 1) % pbar_update_interval == 0:
                pbar.update(time - prev_time)
                pbar.set_description("Processing ({}/{})"
                        .format(i_sim, total_steps))
                prev_time = time

            # Post-processing
            if done or i_sim % save_interval == save_interval-1:
                # Make a video of octopus for current simulation episode. Note that
                # in order to make a video, COLLECT_DATA_FOR_POSTPROCESSING=True
                env.save_data(os.path.join(PATH, 'br2_data.npz'))
                env.post_processing(
                    filename_video="br2_simulation",
                    save_folder=PATH,
                    data_id=0,
                    # The following parameters are optional
                    x_limits=(-0.13, 0.13),  # Set bounds on x-axis
                    y_limits=(-0.00, 0.7),  # Set bounds on y-axis
                    z_limits=(-0.13, 0.13),  # Set bounds on z-axis
                    dpi=100,  # Set the quality of the image
                    vis3D=True,  # Turn on 3D visualization
                    vis2D=True,  # Turn on projected (2D) visualization
                    vis3D_director=True,
                    vis2D_director_lastelement=True,
                )

            # If done=True, NaN detected in simulation.
            # Exit the simulation loop before, reaching final time
            if done:
                print(" Episode finished after {} ".format(time))
                break
    # Simulation loop ends
    print("Final time of simulation is : ", time)

    # Slack message
    if SLACK:
        slack_client = WebClient(os.environ.get('SLACK_BOT_TOKEN'))
        response = slack_client.chat_postMessage(
            username="TeleviMac",
            channel="macbook-pro",
            text='\n'.join([
                'Simulation Finished :',
                '  Program name - br2 basic simulation',
                '  Final time of simulation - {}'.format(time),
                '  PID - {}'.format(os.getpid()),
            ]),
        )
        print(response)

if __name__ == "__main__":
    # Actuation Profile
    maxBend = 1000
    maxTorque = 0
    actuation = np.zeros(3)
    actuation[0] = maxBend
    actuation[2] = maxTorque

    # Run
    main(actuation)
