import os
import copy
import time

import numpy as np

from elastica._calculus import _isnan_check
from elastica.timestepper import extend_stepper_interface
from elastica import *
from elastica.external_forces import (
    UniformTorques,
    # EndPointTorques,
)

from post_processing import (
    plot_video_2d,
    plot_video_activation_muscle,
    plot_video_with_surface,
)

from surface_connection_parallel_rod_numba import (
    SurfaceJointSideBySide,
)
from elastica._calculus import _clip_array
from elastica._linalg import _batch_cross, _batch_dot, _batch_norm, _batch_matvec
from elastica._elastica_numba._linalg import _batch_product_i_k_to_ik

from free_simulator import FreeAssembly

np.set_printoptions(precision=4)


class Environment:
    def __init__(
            self,
            final_time,
            fps,
            COLLECT_DATA_FOR_POSTPROCESSING=False,
    ):
        # Integrator type
        self.StatefulStepper = PositionVerlet()

        # Simulation parameters
        self.final_time = final_time
        time_step = 1.0e-5  # this is a stable timestep (default : 4.0e-5)
        self.learning_step = 1
        self.total_steps = int(self.final_time / time_step / self.learning_step)
        self.time_step = np.float64(
            float(self.final_time) / (self.total_steps * self.learning_step)
        )
        # Video speed
        self.rendering_fps = fps
        self.step_skip = int(1.0 / (self.rendering_fps * self.time_step))
        #self.step_skip = 100
        self.time_interval = None#(0., 0.2)

        # Rod
        self.shearable_rods = {}

        # Collect data is a boolean. If it is true callback function collects
        # rod parameters defined by user in a list.
        self.COLLECT_DATA_FOR_POSTPROCESSING = COLLECT_DATA_FOR_POSTPROCESSING

    def save_state(self, directory: str = ''):
        """
        Save state parameters of each rod.

        TODO : environment list variable is not uniform at the current stage of development. 
        It would be nice if we have set list (like env.system) that iterates all the rods.

        Parameters
        ----------
        directory : str
            Directory path name. The path must exist.
        """
        assert self._reset
        for idx, rod in enumerate(self.shearable_rods):
            path = os.path.join(directory, 'rod_{}.npz'.format(idx))
            np.savez(path, **rod.__dict__)

    def load_state(self, directory: str = ''):
        """
        Load the rod-state.
        Compatibale with 'save_state' method.

        If the save-file does not exist, it returns error.

        Parameters
        ----------
        directory : str
            Directory path name. 
        """
        assert self._reset
        for idx, rod in enumerate(self.shearable_rods):
            path = os.path.join(directory, 'rod_{}.npz'.format(idx))
            data = np.load(path)
            for key, value in data.items():
                if value.shape != ():
                    # Copy data into placeholders
                    getattr(rod, key)[:] = value
                else:
                    # For single-value data
                    setattr(rod, key, value)

    def reset(self, config_file, **kwargs):
        """
        This function, creates the simulation environment.
        First, rod intialized and then rod is modified to make it tapered.
        Second, muscle segments are intialized. Muscle segment position,
        number of basis functions and applied directions are set.
        Finally, friction plane is set and simulation is finalized.
        Returns
        -------

        """
        ## Debut
        k_multiplier = kwargs.get('t_multiplier', 1) * 1.0
        kt_multiplier = kwargs.get('kt_multiplier', 1) * 1.0

        self.free = FreeAssembly()
        self.simulator = self.free.simulator
        self.tagtime = hash(time.time())  # Reset ID
        self.shearable_rods = {}
        self.rod_name = ['seg1_Bend1', 'seg1_Twist1', 'seg1_Twist2', 'seg2_Bend1', 'seg2_Twist1', 'seg2_Twist2']

        # setting up test params
        # n_elem = 41
        # direction = np.array([0.0, 1.0, 0.0])  # rod direction
        # normal = np.array([0.0, 0.0, 1.0])
        # base_length = 0.18
        # base_radius = 0.007522
        # E = 1e7
        # rod_spec = {
        #     'n_elements':n_elem,
        #     'direction':direction,
        #     'normal':normal,
        #     'base_length':base_length,  # rod base length
        #     'base_radius':base_radius,  # rod base radius
        #     'density':1500,
        #     'nu':1.0,  # glue dissipation coefficient
        #     'youngs_modulus':E,
        #     'poisson_ratio':0.5,
        # }
        import json

        with open(config_file) as json_data_file:
            rod_spec = json.load(json_data_file)
        rod_spec['nu'] = 0.0891
        rod_spec['direction'] = np.array(rod_spec['direction'])
        rod_spec['normal'] = np.array(rod_spec['normal'])
        n_elem = rod_spec['n_elements']
        base_length = rod_spec['base_length']
        base_radius = rod_spec['base_radius']
        E = rod_spec['youngs_modulus']

        # Define first segment FREE
        number_of_rod = 3
        angle_btw_rods = np.pi - 2 * np.pi / number_of_rod
        to_next_center = np.array([np.cos(angle_btw_rods / 2), 0.0, np.sin(angle_btw_rods / 2)])
        R = np.array([
            [np.cos(np.pi - angle_btw_rods), 0, np.sin(np.pi - angle_btw_rods)],
            [0, 1, 0],
            [-np.sin(np.pi - angle_btw_rods), 0, np.cos(np.pi - angle_btw_rods)]])
        start_position = np.zeros((3,))
        for i in range(number_of_rod):
            # Add shearable rod
            rod_spec['start'] = start_position
            rod_spec['is_first_segment'] = True
            print(f'rod {i} position: {start_position}')
            if i == 0:
                self.free.add_free_bending(self.rod_name[i], z_angle=np.pi, **rod_spec)
            elif i == 1 or i == 2:
                self.free.add_free_twist(self.rod_name[i], **rod_spec)
            # Move starting point
            start_position = start_position + to_next_center * 2 * base_radius
            to_next_center = R @ to_next_center

        # Define second segment FREE
        number_of_rod = 3
        angle_btw_rods = np.pi - 2 * np.pi / number_of_rod
        to_next_center = np.array([np.cos(angle_btw_rods / 2), 0.0, np.sin(angle_btw_rods / 2)])
        R = np.array([
            [np.cos(np.pi - angle_btw_rods), 0, np.sin(np.pi - angle_btw_rods)],
            [0, 1, 0],
            [-np.sin(np.pi - angle_btw_rods), 0, np.cos(np.pi - angle_btw_rods)]])
        start_position = np.zeros((3,))
        start_position[1] = base_length
        for i in range(3, 3+number_of_rod):
            # Add shearable rod
            rod_spec['start'] = start_position
            rod_spec['is_first_segment'] = False
            print(f'rod {i} position: {start_position}')
            if i == 4:
                self.free.add_free_bending(self.rod_name[i], z_angle=5*np.pi/3, **rod_spec)
            elif i == 3 or i == 5:
                self.free.add_free_twist(self.rod_name[i], **rod_spec)
            # Move starting point
            start_position = start_position + to_next_center * 2 * base_radius
            start_position[1] = base_length
            to_next_center = R @ to_next_center
        self.shearable_rods = self.free.free

        # Parallel Connection
        # I do not know what these terms are for, conceivably for the coupling of the arms
        k_connection = np.pi * base_radius * E / n_elem * k_multiplier  # 50  # 1e5
        nu_connection = base_length / n_elem * 1e-3
        kt_connection = base_radius / 2 * kt_multiplier  # 1e-3
        k_contact = k_connection * 1.0 * 0
        self.free.add_parallel_connection(self.rod_name[0], self.rod_name[1],
                k=k_connection, nu=nu_connection, kt=kt_connection, k_contact=k_contact)
        self.free.add_parallel_connection(self.rod_name[1], self.rod_name[2],
                k=k_connection, nu=nu_connection, kt=kt_connection, k_contact=k_contact)
        self.free.add_parallel_connection(self.rod_name[0], self.rod_name[2],
                k=k_connection, nu=nu_connection, kt=kt_connection, k_contact=k_contact)
        self.free.add_parallel_connection(self.rod_name[3], self.rod_name[4],
                k=k_connection, nu=nu_connection, kt=kt_connection, k_contact=k_contact)
        self.free.add_parallel_connection(self.rod_name[4], self.rod_name[5],
                k=k_connection, nu=nu_connection, kt=kt_connection, k_contact=k_contact)
        self.free.add_parallel_connection(self.rod_name[3], self.rod_name[5],
                k=k_connection, nu=nu_connection, kt=kt_connection, k_contact=k_contact)
        print('k connection: ', k_connection)
        print('nu connection: ', nu_connection)
        print('kt connection: ', kt_connection)

        # Serial Connection
        self.free.add_serial_connection(self.rod_name[0:3], self.rod_name[3:6],
                k=k_connection, nu=nu_connection, kt=kt_connection, k_contact=k_contact)

        # Callback
        if self.COLLECT_DATA_FOR_POSTPROCESSING:
            # Collect data using callback function for postprocessing
            # step_skip = 500  # collect data every # steps

            # set the diagnostics for rod and collect data
            self.data_rod1 = self.free.add_callback(self.rod_name[0], self.step_skip, time_interval=self.time_interval)
            self.data_rod2 = self.free.add_callback(self.rod_name[1], self.step_skip, time_interval=self.time_interval)
            self.data_rod3 = self.free.add_callback(self.rod_name[2], self.step_skip, time_interval=self.time_interval)
            self.data_rod4 = self.free.add_callback(self.rod_name[3], self.step_skip, time_interval=self.time_interval)
            self.data_rod5 = self.free.add_callback(self.rod_name[4], self.step_skip, time_interval=self.time_interval)
            self.data_rod6 = self.free.add_callback(self.rod_name[5], self.step_skip, time_interval=self.time_interval)

        # Finalize simulation environment. After finalize, you cannot add
        # any forcing, constrain or call back functions
        self.simulator.finalize()

        # do_step, stages_and_updates will be used in step function
        self.do_step, self.stages_and_updates = extend_stepper_interface(
            self.StatefulStepper, self.simulator
        )

        systems = self.simulator._systems

        return self.total_steps, systems

    def step(self, action, time, nan_check=False, steady_state_check=True):
        # Do 200 time step of simulation. Here we are doing multiple Elastica time-steps, because
        # time-step of elastica is much slower than the time-step of control or learning algorithm.

        # DEBUG PARAMETERS
        # nan_check : if true, track the position data and plot when nan if found

        # Setting external load
        actuation = {
            self.rod_name[0]: [action[0]],
            self.rod_name[1]: [action[1]],
            self.rod_name[2]: [action[2]],
            self.rod_name[3]: [0.0],
            self.rod_name[4]: [action[0]],
            self.rod_name[5]: [0.0],
        }
        self.free.set_actuation(actuation)

        _save_data = []
        for _ in range(self.learning_step):
            time = self.do_step(
                self.StatefulStepper,
                self.stages_and_updates,
                self.simulator,
                time,
                self.time_step,
            )
            if nan_check:
                _save_data.append([self.shearable_rods[name].position_collection.copy() for name in self.rod_name])

        # Validate Continuous Condition
        # TODO: Return true if time is passed the total simulation time
        """ Done is a boolean to reset the environment before episode is completed """
        done = False
        # Position of the rod cannot be NaN, it is not valid, stop the simulation
        invalid_values_conditions = (
                [_isnan_check(self.shearable_rods[name].position_collection) for name in self.rod_name] +
                [_isnan_check(self.shearable_rods[name].velocity_collection) for name in self.rod_name] +
                [_isnan_check(self.shearable_rods[name].director_collection) for name in self.rod_name] +
                [_isnan_check(self.shearable_rods[name].omega_collection) for name in self.rod_name])

        if any(invalid_values_conditions):
            done = True
            print("Nan detected, exiting simulation now")
            if nan_check:
                _save_data = np.array(_save_data)
                for i in range(self.learning_step):
                    if np.any(np.isnan(_save_data[i])):
                        print('first nan at: ', i)
                        break
                print('data size: ', _save_data.shape)
                # Plot last 100 step shape
                import matplotlib.pyplot as plt
                fig = plt.figure('dbg')
                plt.cla()
                plt.clf()
                ax = fig.add_subplot(111)
                ax.set_xlabel('y')
                ax.set_ylabel('x')
                pt, = ax.plot([], [], 'r-o')
                for i in range(self.learning_step):
                    x = _save_data[i, 0, 1, :]
                    y = _save_data[i, 0, 0, :]
                    pt.set_xdata(y)
                    pt.set_ydata(x)
                    ax.relim()
                    ax.autoscale_view()
                    fig.canvas.draw()
                    fig.canvas.flush_events()
                    plt.show(block=False)

                # (debug) Callback Check
                for k, v in self.data_rod1.items():
                    print(k)
                    print('    ', np.array(v).shape)
                for k, v in self.data_rod2.items():
                    print(k)
                    print('    ', np.array(v).shape)
                for k, v in self.data_rod3.items():
                    print(k)
                    print('    ', np.array(v).shape)
                print(self.data_rod1['step'])
                input('')

        # TODO: Define reward
        reward = 0

        # Check if steady-state
        if steady_state_check and time > 0.2:  # minimum simulation time
            velocities = [np.array(self.shearable_rods[name].velocity_collection) for name in self.rod_name]
            max_velocity = max([np.linalg.norm(v, axis=0).max() for v in velocities])
            if max_velocity < 1e-4:
                print("Steady-state, exiting simulation now")
                done = True
                ''' # Average convergence
                average_velocity_history_rod1 = np.linalg.norm(self.data_rod1['velocity'][-10:], axis=1).mean()
                average_velocity_history_rod2 = np.linalg.norm(self.data_rod2['velocity'][-10:], axis=1).mean()
                average_velocity_history_rod3 = np.linalg.norm(self.data_rod3['velocity'][-10:], axis=1).mean()
                if (average_velocity_history_rod1 < 1e-3 and \
                    average_velocity_history_rod2 < 1e-3 and \
                    average_velocity_history_rod3 < 1e-3):
                    done = True
                '''

        if self.final_time < time:
            done = True

        # systems = self.simulator._systems
        systems = [self.data_rod1, self.data_rod2, self.data_rod3, self.data_rod4, self.data_rod5, self.data_rod6]

        return time, systems, reward, done

    def post_processing(self, filename_video, save_folder, data_id=0, **kwargs):
        """
        Make video 3D rod movement in time.
        Parameters
        ----------
        filename_video
        Returns
        -------

        """

        if self.COLLECT_DATA_FOR_POSTPROCESSING:
            import os
            plot_video_with_surface(
                [
                    self.data_rod1,
                    self.data_rod2,
                    self.data_rod3,
                    self.data_rod4,
                    self.data_rod5,
                    self.data_rod6,
                ],
                video_name=filename_video,
                fps=self.rendering_fps,
                step=1,
                save_folder=save_folder,
                **kwargs
            )

            position_data_path = os.path.join(save_folder, f"br2_data_{data_id}.npz")
            self.save_data(position_data_path)

        else:
            raise RuntimeError(
                "call back function is not called anytime during simulation, "
                "change COLLECT_DATA=True"
            )

    def save_data(self, path):
        # Transform nodal to elemental positions
        position_rod1 = np.array(self.data_rod1["position"])
        position_rod1 = 0.5 * (position_rod1[..., 1:] + position_rod1[..., :-1])

        # Transform nodal to elemental positions
        position_rod2 = np.array(self.data_rod2["position"])
        position_rod2 = 0.5 * (position_rod2[..., 1:] + position_rod2[..., :-1])

        # Transform nodal to element positions
        position_rod3 = np.array(self.data_rod3["position"])
        position_rod3 = 0.5 * (position_rod3[..., 1:] + position_rod3[..., :-1])

        # Save rod position (for povray)
        np.savez(
            path,
            position_rod1=position_rod1,
            radii_rod1=np.array(self.data_rod1["radius"]),
            director_rod1=np.array(self.data_rod1["director"]),
            position_rod2=position_rod2,
            radii_rod2=np.array(self.data_rod2["radius"]),
            director_rod2=np.array(self.data_rod2["director"]),
            position_rod3=position_rod3,
            radii_rod3=np.array(self.data_rod3["radius"]),
            director_rod3=np.array(self.data_rod3["director"]),
        )
