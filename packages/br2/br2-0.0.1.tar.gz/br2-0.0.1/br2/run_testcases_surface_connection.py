import multiprocessing
from multiprocessing import Process, Pool
import subprocess
from subprocess import call
import os
import sys
import copy
import time

import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import minimize
from functools import partial
from tqdm import tqdm

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

sys.path.append("../") # For elastica
#sys.settrace  # toggle GDB debugging 

from set_environment_testcases import (
    ExperimentSimpleTwoRodConnection,
    ExperimentSimpleThreeTriangleConnection,
    ExperimentFiveCrossConnection,
    ExperimentFiveWallConnection,
    ExperimentFiveWallConnectionMiddleActivation,
    ExperimentSymmetricConnectivityTest,
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


# Path Configuration
WD_PATH = 'result_surface_connection_testcases'  # Working directory path
os.makedirs(WD_PATH, exist_ok=1)

def run(name):
    import os
    print("    PID of process {}: {}".format(name, os.getpid()))
    # Set the designated environment

    # Magnitude (two-arm, triangle, cross)
    shear_force = 250
    normal_force = 600
    axial_torque = 350
    flexural_torque = 120

    #== Two-arm configuration ==#
    if name == 'twoarm-x-linear-force':
        env = ExperimentSimpleTwoRodConnection(
            force=np.array([shear_force,0.0,0.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'twoarm-y-linear-force':
        env = ExperimentSimpleTwoRodConnection(
            force=np.array([0.0,normal_force,0.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'twoarm-z-linear-force':
        env = ExperimentSimpleTwoRodConnection(
            force=np.array([0.0,0.0,shear_force]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'twoarm-x-torque':
        env = ExperimentSimpleTwoRodConnection(
            torque=flexural_torque,
            torque_direction=np.array([1.0,0.0,0.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'twoarm-y-torque':
        env = ExperimentSimpleTwoRodConnection(
            torque=axial_torque,
            torque_direction=np.array([0.0,1.0,0.0]),
            final_time=15.0,
            ramp_up_time=2.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'twoarm-z-torque':
        env = ExperimentSimpleTwoRodConnection(
            torque=flexural_torque,
            torque_direction=np.array([0.0,0.0,1.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )

    #== Three-arm triangle configuration ==#
    elif name == 'triangle-x-linear-force':
        env = ExperimentSimpleThreeTriangleConnection(
            force=np.array([shear_force,0.0,0.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'triangle-y-linear-force':
        env = ExperimentSimpleThreeTriangleConnection(
            force=np.array([0.0,normal_force,0.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'triangle-z-linear-force':
        env = ExperimentSimpleThreeTriangleConnection(
            force=np.array([0.0,0.0,shear_force]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'triangle-x-torque':
        env = ExperimentSimpleThreeTriangleConnection(
            torque=flexural_torque,
            torque_direction=np.array([1.0,0.0,0.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'triangle-y-torque':
        env = ExperimentSimpleThreeTriangleConnection(
            torque=axial_torque,
            torque_direction=np.array([0.0,1.0,0.0]),
            final_time=15.0,
            ramp_up_time=2.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'triangle-z-torque':
        env = ExperimentSimpleThreeTriangleConnection(
            torque=flexural_torque,
            torque_direction=np.array([0.0,0.0,1.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )

    #== Five-arm cross configuration ==#
    elif name == 'cross-x-linear-force':
        env = ExperimentFiveCrossConnection(
            force=np.array([shear_force,0.0,0.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'cross-y-linear-force':
        env = ExperimentFiveCrossConnection(
            force=np.array([0.0,normal_force,0.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'cross-z-linear-force':
        env = ExperimentFiveCrossConnection(
            force=np.array([0.0,0.0,shear_force]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'cross-x-torque':
        env = ExperimentFiveCrossConnection(
            torque=flexural_torque,
            torque_direction=np.array([1.0,0.0,0.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'cross-y-torque':
        env = ExperimentFiveCrossConnection(
            torque=axial_torque,
            torque_direction=np.array([0.0,1.0,0.0]),
            final_time=30.0,
            ramp_up_time=2.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'cross-neg-y-torque':
        env = ExperimentFiveCrossConnection(
            torque=-axial_torque,
            torque_direction=np.array([0.0,1.0,0.0]),
            final_time=30.0,
            ramp_up_time=2.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'cross-z-torque':
        env = ExperimentFiveCrossConnection(
            torque=flexural_torque,
            torque_direction=np.array([0.0,0.0,1.0]),
            final_time=15.0,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )

    #== Five-arm wallconfiguration ==#
    elif name == 'wall-shear-inplane':
        env = ExperimentFiveWallConnection(
            force=500,
            mode='shear-inplane',
            final_time=15.0,
            time_step=1e-6,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'wall-shear-antiplane':
        env = ExperimentFiveWallConnection(
            force=200,
            mode='shear-antiplane',
            final_time=15.0,
            time_step=1e-6,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'wall-peel':
        env = ExperimentFiveWallConnection(
            force=200,
            mode='peel',
            final_time=15.0,
            time_step=1e-6,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'wall-shear-inplane-middle':
        env = ExperimentFiveWallConnectionMiddleActivation(
            force=500,
            mode='shear-inplane',
            final_time=15.0,
            time_step=1e-6,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'wall-shear-antiplane-middle':
        env = ExperimentFiveWallConnectionMiddleActivation(
            force=200,
            mode='shear-antiplane',
            final_time=15.0,
            time_step=1e-6,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    elif name == 'wall-peel-middle':
        env = ExperimentFiveWallConnectionMiddleActivation(
            force=200,
            mode='peel',
            final_time=15.0,
            time_step=1e-6,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )

    #== Special Cases ==#
    elif name == 'glue-symmetric-corner-test':
        env = ExperimentSymmetricConnectivityTest(
            torque=axial_torque,
            direction=np.array([0.0,1.0,0.0]),
            final_time=15.0,
            time_step=1e-6,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
        )
    else:
        raise NotImplementedError("the test id {} is not yet implemented".format(name))

    # Reset the environment 
    total_steps, systems = env.reset()

    # Simulation
    save_time_interval = 5.0 # Save after each interval of time (sec)
    next_save_time = save_time_interval
    stime = time.time()
    simulation_time = np.float64(0.0)
    done = False
    i_sim = 0
    while not done:
        # Simulation
        simulation_time, systems, done = env.step(simulation_time)

        # Post-processing
        if done or simulation_time > next_save_time:
            # Make a video of octopus for current simulation episode. Note that
            # in order to make a video, COLLECT_DATA_FOR_POSTPROCESSING=True
            save_folder = env.post_processing(
                path=WD_PATH,
                filename="{}-simulation".format(name),
                # The following parameters are optional
                x_limits=(-0.53, 0.53),  # Set bounds on x-axis
                y_limits=(-0.10, 1.25),  # Set bounds on y-axis
                z_limits=(-0.53, 0.53),  # Set bounds on z-axis
                dpi=100,  # Set the quality of the image
                vis3D=True,  # Turn on 3D visualization
                vis3D_director=True,  
                vis2D_director_lastelement=True,  
                vis2D=True,  # Turn on projected (2D) visualization
            )
            next_save_time += save_time_interval
        # If done=True, NaN detected in simulation.
        # Exit the simulation loop before, reaching final time
        if done:
            break
        # Iteration step
        i_sim += 1

    # Simulation loop ends
    etime = time.time()

    # Slack message
    if SLACK:
        slack_client = WebClient(os.environ.get('SLACK_BOT_TOKEN'))
        response = slack_client.chat_postMessage(
            username="TeleviMac",
            channel="macbook-pro",
            text='\n'.join([
                'Simulation Finished :',
                '  Program name - {}'.format(name),
                '  Final time of simulation - {}'.format(simulation_time),
                '  Simulation walltime - {}'.format(etime-stime),
                '  PID - {}'.format(os.getpid()),
            ]),
        )
        print(response)

if __name__ == "__main__":
    print("main process ID: {}".format(os.getpid()))
    run_list = [
        #'twoarm-x-linear-force',
        #'twoarm-y-linear-force',
        #'twoarm-z-linear-force',
        #'twoarm-x-torque',
        #'twoarm-y-torque',
        #'twoarm-z-torque',
        #'triangle-x-linear-force',
        #'triangle-y-linear-force',
        #'triangle-z-linear-force',
        #'triangle-x-torque',
        #'triangle-y-torque',
        #'triangle-z-torque',
        #'cross-x-linear-force',
        #'cross-y-linear-force',
        #'cross-z-linear-force',
        #'cross-x-torque',
        'cross-y-torque',
        'cross-neg-y-torque',
        #'cross-z-torque',
        #'wall-shear-inplane',
        #'wall-shear-antiplane',
        #'wall-peel',
        #'wall-shear-inplane-middle',
        #'wall-shear-antiplane-middle',
        #'wall-peel-middle',
        #'glue-symmetric-corner-test',
    ]
    pool = Pool(processes=8)
    results = []
    for name in run_list:
        result = pool.apply_async(run, args=(name,))
        results.append(result)
        time.sleep(1)
    output = [p.get() for p in results]

    print("process done")
