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
from set_environment_br2 import (
    Environment,
)

PATH = 'run11'
os.makedirs(PATH, exist_ok=1)

# Position Data (From Experiment)
data = np.load(r'/media/skim0119/Data/BR2 - 2021-04-13/postprocess/run1-position.npz')
target_position = data['position']
print(f'original target position data shape: {target_position.shape}')

# Downsampling
recorded_fps = 60
target_fps = 20  # Targeted frames per second: comparison made at each frames
recorded_time = np.arange(target_position.shape[0], dtype=np.float64) * (1.0/recorded_fps)
target_time = np.arange(int(target_position.shape[0]*target_fps/recorded_fps), dtype=np.float64) * (1.0/target_fps)
target_position = interp1d(recorded_time, target_position, axis=0)(target_time)
print(f'recorded FPS: {recorded_fps}, targeted fps: {target_fps}')
print(f'downsampled target position shape: {target_position.shape}')

simulation_frames = target_position.shape[0]
simulation_time = simulation_frames / target_fps
print(f'simulation time (sec): {simulation_time}')
print(f'simulation frames: {simulation_frames}')


def loss(systems, target, idx=None, initial_r=None, show=False):
    """
    systems : rods
    target : [3, N]
    """

    info = {}
    num_target = target.shape[1]
    system_positions = np.concatenate([r.position_collection[:,:-1] for r in systems], axis=1)
    system_Q = np.concatenate([r.director_collection for r in systems], axis=2)

    # Find closest index if not given
    if idx is None:
        # find closest index
        idx = []
        for i in range(num_target):
            p = target[:,i].reshape([3,1])
            argmin = np.argmin(np.linalg.norm(p-system_positions, axis=0))
            idx.append(argmin) 
        info['index'] = idx

    if initial_r is None:
        rs = []
        for i in range(num_target):
            q = system_Q[:,:,idx[i]]
            x = system_positions[:,idx[i]]
            p = target[:,i]
            rs.append(q@(p-x)) 
        info['r'] = rs

    loss_total = 0
    loss_x = 0
    loss_z = 0
    if initial_r is not None:
        loss_vec = []
        rps = []
        for i in range(num_target):
            q = system_Q[:,:,idx[i]]
            x = system_positions[:,idx[i]]
            p = target[:,i]
            rp = x + (np.linalg.inv(q) @ initial_r[i])

            loss_vec.append(rp - p)
            norm = np.linalg.norm(rp - p)
            loss_total += norm
            loss_x = p[0] - rp[0]
            loss_z = p[2] - rp[2]

            rps.append(rp)
        info['sim targets'] = np.array(rps)

    # plot (debug)
    if show:
        fig = plt.figure('diagram')
        plt.cla()
        plt.clf()
        ax = fig.add_subplot(111, projection='3d')
        gposition = system_positions.copy()
        gtarget = target.copy()
        gtarget[[1,2]] = gtarget[[2,1]]
        gposition[[1,2]] = gposition[[2,1]]
        ax.scatter(*gtarget, label='experiment')
        ax.scatter(*gposition, 'r', label='simulation')
        ax.scatter(0,0,0,marker='^')
        ax.scatter(*gtarget[:,0], marker='^')
        ax.view_init(elev=25, azim=-60, )
        ax.set_xlim(-0.1,0.1)
        ax.set_ylim(-0.1, 0.1)
        ax.set_zlim(-0.0, 0.25)
        plt.legend()

        fig = plt.figure('loss guide')
        plt.cla()
        plt.clf()
        ax = fig.add_subplot(111, projection='3d')
        grs = np.array(loss_vec).copy()
        gx = target.copy()
        grs[:,[1,2]] = grs[:,[2,1]]
        gx[[1,2]] = gx[[2,1]]
        #ax.scatter(*gx, 'k', label='base')
        ax.quiver(gx[0], gx[1], gx[2], grs[:,0], grs[:,1], grs[:,2], label='rs')
        ax.view_init(elev=25, azim=-60, )
        ax.set_xlim(-0.05,0.05)
        ax.set_ylim(-0.05, 0.05)
        ax.set_zlim(-0.0, 0.20)
        plt.legend()
        plt.show(block=False)

    return loss_total, info  # Norm 
    #return (loss_x, loss_z), info  # Delta for x and z

def step_wrapper(env, start_time, end_time, action):
    """ Play the environment for a duration with a given action

    Parameters:
    -----------
    env:
    start_time:
    end_time:
    action:
    """
    assert start_time < end_time

    time = start_time
    total_reward = 0.0
    while time < end_time:
        time, systems, reward, done = env.step(action, time, nan_check=1)
        total_reward += reward
        if done:
            break
    return time, systems, total_reward, done

def optimize_action(env, start_time, end_time, initial_action, loss_lambda):
    bounds = [(-800,800), (0,6)]
    ps = []
    env.save_state()
    initial_action = np.array([500,1])
    def f(action):
        env.load_state()
        action[0] *= 1000
        action[1] *= 6
        etime, systems, _, _ = step_wrapper(env, start_time, end_time, action)
        l, info = loss_lambda(systems)
        print(f'action: {action}, loss: {l}')
        print(systems)
        input('')
        return l
    def reporter(p):
        ps.append(p)
    res = minimize(f, initial_action, method='nelder-mead',#bounds=bounds, #tol=1e-2,
            callback=reporter)
    return res.x, ps

def main(actuation):
    # Set simulation final time
    env = Environment(
        simulation_time,
        COLLECT_DATA_FOR_POSTPROCESSING=True,
    )

    # Reset the environment before the new episode and get total number of simulation steps
    total_steps, systems = env.reset()
    print(f'Total simulation steps: {total_steps}')

    # Initial Loss (baseline)
    l, loss_info = loss(systems, target_position[0].T) 
    target_index = loss_info['index']
    initial_r = loss_info['r']

    # Simulation loop starts
    user_defined_condition = False
    reward = 0.0

    # Figure Config
    '''
    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    ax.set_title('Loss - Sim to Phys')
    ax.set_xlabel('Time (sec)')
    ax.set_ylabel('Loss')
    loss_line_bend, = ax.plot([],[],'r-')
    #loss_line_twist, = ax.plot([],[],'b-')
    '''
    fig = plt.figure(0)
    ax1 = fig.add_subplot(411)
    ax2 = fig.add_subplot(412)
    ax3 = fig.add_subplot(413)
    ax4 = fig.add_subplot(414)
    ax1.set_title('x position')
    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('x')
    ax2.set_title('y position')
    ax2.set_xlabel('Time (sec)')
    ax2.set_ylabel('y')
    ax3.set_title('z position')
    ax3.set_xlabel('Time (sec)')
    ax3.set_ylabel('z')
    ax4.set_title('Tlength')
    ax4.set_xlabel('Time (sec)')
    ax4.set_ylabel('L')
    xplot, = ax1.plot([],[],'r-')
    yplot, = ax2.plot([],[],'r-')
    zplot, = ax3.plot([],[],'r-')
    lplot, = ax4.plot([],[],'r-')

    # Simulation
    sync_ratio = simulation_frames / total_steps
    save_interval = 50
    loss_data_bend = []
    #loss_data_twist = []
    sim_target_position = np.zeros_like(target_position)
    with tqdm(total=simulation_time) as pbar:
        prev_time = 0
        time = np.float64(0.0)
        for i_sim in range(1, simulation_frames):
            target_x = target_position[i_sim]
            next_time = target_time[i_sim]

            #if action_o[0] > 0 or action_o[1] > 0:
            if False: # Backward optimization (TODO)
                guess = actuation[i_sim-1]
                action, states = optimize_action(
                    env,
                    time,
                    next_time,
                    guess,
                    loss_lambda=partial(loss, target=target_x.T, idx=target_index, initial_r=initial_r, show=True),
                )
                print(f'optimization steps: {states}')
            else:
                action = actuation[i_sim-1]
            #print(f'initial guessed action: {guess}, optimized action: {action}')

            # Loss Calculation
            delta, loss_info = loss(
                systems,
                target_x.T,
                idx=target_index,
                initial_r=initial_r,
                show=0,#i_sim%save_interval==0,
            )
            loss_data_bend.append(delta)
            sim_target_position[i_sim] = loss_info['sim targets']
            #loss_data_twist.append(delta[1])

            # Simulation
            time, systems, reward, done = step_wrapper(env, time, next_time, action)

            # Progress bar update
            pbar.update(time - prev_time)
            pbar.set_description("Processing {}/{}".format(int(i_sim/sync_ratio), total_steps))
            prev_time = time
            
            # Loss Plot (debug)
            '''
            plt.figure(0)
            loss_line_bend.set_xdata(target_time[:i_sim])
            loss_line_bend.set_ydata(loss_data_bend)
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.show(block=False)
            '''
            _observe = 'velocity'
            _elem = 1
            plt.figure(0)
            xplot.set_xdata(env.data_rod1['time'])
            xplot.set_ydata(np.array(env.data_rod1[_observe])[:,0,_elem])
            yplot.set_xdata(env.data_rod1['time'])
            yplot.set_ydata(np.array(env.data_rod1[_observe])[:,1,_elem])
            zplot.set_xdata(env.data_rod1['time'])
            zplot.set_ydata(np.array(env.data_rod1[_observe])[:,2,_elem])
            lplot.set_xdata(env.data_rod1['time'])
            lplot.set_ydata(np.array(env.data_rod1['lengths']).sum(-1))
            ax1.relim()
            ax1.autoscale_view()
            ax2.relim()
            ax2.autoscale_view()
            ax3.relim()
            ax3.autoscale_view()
            ax4.relim()
            ax4.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.show(block=False)


            # Post-processing
            if done or i_sim % save_interval == save_interval-1:
                # Make a video of octopus for current simulation episode. Note that
                # in order to make a video, COLLECT_DATA_FOR_POSTPROCESSING=True
                env.save_data(os.path.join(PATH, 'br2_data.npz'))
                save_folder = env.post_processing(
                    filename_video="br2_simulation",
                    filename_data=PATH,
                    data_id=0,
                    # The following parameters are optional
                    x_limits=(-0.13, 0.13),  # Set bounds on x-axis
                    y_limits=(-0.00, 0.3),  # Set bounds on y-axis
                    z_limits=(-0.13, 0.13),  # Set bounds on z-axis
                    dpi=100,  # Set the quality of the image
                    vis3D=True,  # Turn on 3D visualization
                    vis2D=True,  # Turn on projected (2D) visualization
                )
                ''' 
                env.overlay_loss(
                    filename_video="br2_tracking",
                    filename_data=PATH,
                    target_time=target_time[:i_sim],
                    target_position=target_position[:i_sim],
                    # The following parameters are optional
                    x_limits=(-0.13, 0.13),  # Set bounds on x-axis
                    y_limits=(-0.00, 0.3),  # Set bounds on y-axis
                    z_limits=(-0.13, 0.13),  # Set bounds on z-axis
                )
                pass
                ''' 

            # If done=True, NaN detected in simulation.
            # Exit the simulation loop before, reaching final time
            if done:
                print(" Episode finished after {} ".format(time))
                break
    # Simulation loop ends
    print("Final time of simulation is : ", time)

    # Post Works
    print(target_position.shape)
    print(sim_target_position.shape)
    np.savez(os.path.join(PATH, 'target_delta.npz'),
             target_position=target_position,
             sim_target_position=sim_target_position)

    # Save Loss Graph
    plt.figure(0)
    plt.savefig(os.path.join(PATH, 'simulation_loss.png'))

if __name__ == "__main__":
    '''
    # actuation 25 psi
    pressure = 25
    bending = 820.0
    torque = 17.2
    # actuation 20 psi
    pressure = 20
    bending = 590
    torque = 2.5#15.85
    # actuation 15 psi
    pressure = 15
    bending = 390
    torque = 6.0 #13.23
    '''

    '''
    # run1
    # Time
    F_i = 120//3
    T_i = 1382//3
    T_f = 2486//3
    F_f = 2873//3
    # Magnitude
    maxF = 750
    maxT = 1.0
    '''

    '''
    # run2
    # Time
    F_i = 120//3
    F_f = 1388//3
    T_i = 630//3
    T_f = 1095//3
    # Magnitude
    maxF = 460 #250
    maxT = 0.5

    # Step
    step_actuation_dur = 10 # transient length
    # Actuation Profile
    actuation = np.zeros([simulation_frames, 2])
    actuation[F_i:F_f,0] = maxF
    actuation[F_i:F_i+step_actuation_dur,0] = np.linspace(0, maxF, step_actuation_dur)
    actuation[F_f:F_f+step_actuation_dur,0] = np.linspace(maxF, 0, step_actuation_dur)
    actuation[T_i:T_f,1] = maxT
    actuation[T_i:T_i+step_actuation_dur,1] = np.linspace(0, maxT, step_actuation_dur)
    actuation[T_f:T_f+step_actuation_dur,1] = np.linspace(maxT, 0, step_actuation_dur)
    '''

    # run1 2021-04-13
    # Time
    maxF = 550 #250 # Magnitude
    F_i = 120//3
    raise_fp = 2098//3
    F_f = F_i + raise_fp + 305//3
    lower_fp = 2770//3
    ramping = np.linspace(0, maxF, raise_fp, True)
    lowering = np.linspace(maxF, 0, lower_fp, True)

    # Actuation Profile
    actuation = np.zeros([simulation_frames, 3])
    actuation[F_i:F_i+raise_fp,0] = ramping
    actuation[F_i+raise_fp:F_f,0] = maxF
    actuation[F_f:F_f+lower_fp,0] = lowering

    main(actuation)
    sys.exit()

    '''
    # result check
    sim_data = np.load(os.path.join(PATH, 'br2_data_0.npz'))
    system_positions = np.concatenate([
            sim_data['position_rod1'],
            sim_data['position_rod2'],
            sim_data['position_rod3']
        ], axis=2
    )

    frame = 296
    target = target_position[frame]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sposition = system_positions[frame]
    target[[1,2]] = target[[2,1]]
    sposition[[1,2]] = sposition[[2,1]]
    ax.scatter(*target)
    ax.scatter(*sposition, 'r')
    ax.scatter(0,0,0,marker='^')
    ax.view_init(elev=25, azim=-60, )
    ax.set_xlim(-0.1,0.1)
    ax.set_ylim(-0.1, 0.1)
    ax.set_zlim(-0.0, 0.25)
    plt.show()
    sys.exit()
    '''
    for frame in tqdm(range(simulation_frames)):
        target = target_position[frame+5]
    
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        sposition = system_positions[frame]
        target[[1,2]] = target[[2,1]]
        sposition[[1,2]] = sposition[[2,1]]

        ax.scatter(*target, label='experiment')
        ax.scatter(*sposition, 'r', label='simulation')
        #ax.scatter(0,0,0,marker='^')
        ax.view_init(elev=25, azim=-60, )
        ax.set_xlim(-0.1,0.1)
        ax.set_ylim(-0.1, 0.1)
        ax.set_zlim(-0.0, 0.25)
        plt.legend()
        #plt.show()
        plt.savefig(os.path.join(PATH, 'render/Frame_%05d.png'%frame))
        plt.clf()
