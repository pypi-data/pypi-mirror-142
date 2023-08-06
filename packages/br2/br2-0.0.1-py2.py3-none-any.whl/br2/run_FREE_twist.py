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
from set_environment_single import (
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

PATH = 'result_twist_2'
os.makedirs(PATH, exist_ok=1)

"""
Increment the bending activation until the steady state, and record the position.
Simulation run until it breaks
"""

# Simulation Configuration
target_fps = 20  # Targeted frames per second: comparison made at each frames
print(f'targeted fps: {target_fps}')

def main():
    # Set simulation final time
    env = Environment(
        999999,
        rod_type='twist',
        COLLECT_DATA_FOR_POSTPROCESSING=True,
    )

    # Reset the environment before the new episode and get total number of simulation steps
    total_steps, systems = env.reset()
    print(f'Total simulation steps: {total_steps}')

    # Simulation
    time = np.float64(0.0)
    action = 0
    _action_scale = 100.0
    save_interval = 5
    next_save_time = save_interval
    pbar = tqdm()
    tqdm_interval = 0.5
    next_tqdm_update_time = tqdm_interval
    while True:
        if time > next_tqdm_update_time:
            next_tqdm_update_time += tqdm_interval
            pbar.update(tqdm_interval)
        time, systems, _, done, steady_state = env.step(action/_action_scale, time)

        if steady_state:
            action += 5
            env.save_data(os.path.join(PATH, 'twist_{}.npz'.format(int(action))))
            print('done: {}, time = {} sec'.format(action, time))
            env.clear_callback()
        
        if time > next_save_time:
            next_save_time += save_interval
            env.post_processing(
                filename_video="twist_quasi_static",
                save_folder=PATH,
                # The following parameters are optional
                x_limits=(-0.13, 0.13),  # Set bounds on x-axis
                y_limits=(-0.00, 0.3),  # Set bounds on y-axis
                z_limits=(-0.13, 0.13),  # Set bounds on z-axis
                dpi=100,  # Set the quality of the image
                vis3D=False,  # Turn on 3D visualization
                vis2D=False,  # Turn on projected (2D) visualization
                vis3D_director=True,
                vis2D_director_lastelement=False,
            )
            env.debug()
            print('    rendered')
            print('    callback cleared')

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
                '  Program name - single FREE quasi-static twist',
                '  Final time of simulation - {}'.format(time),
                '  PID - {}'.format(os.getpid()),
            ]),
        )
        print(response)

if __name__ == "__main__":
    main()
