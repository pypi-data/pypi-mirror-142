import os
import copy
import time

import numpy as np

from elastica._calculus import _isnan_check
from elastica.timestepper import extend_stepper_interface
from elastica import *
from elastica.external_forces import (
    UniformTorques,
    #EndPointTorques,
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
        rod_type,
        COLLECT_DATA_FOR_POSTPROCESSING=False,
    ):
        # Integrator type
        self.StatefulStepper = PositionVerlet()

        # Simulation parameters
        self.final_time = final_time
        self.rod_type = rod_type
        time_step = 1.0e-5#3.0e-6  # this is a stable timestep (default : 4.0e-5)
        self.learning_step = 1
        self.total_steps = int(self.final_time / time_step / self.learning_step)
        self.time_step = np.float64(
            float(self.final_time) / (self.total_steps * self.learning_step)
        )
        # Video speed
        self.rendering_fps = 20
        self.step_skip = int(1.0 / (self.rendering_fps * self.time_step))

        # Rod
        self.shearable_rods = {}

        # Collect data is a boolean. If it is true callback function collects
        # rod parameters defined by user in a list.
        self.COLLECT_DATA_FOR_POSTPROCESSING = COLLECT_DATA_FOR_POSTPROCESSING

    def save_state(self):
        pass

    def load_state(self):
        pass

    def reset(self, **kwargs):
        """
        This function, creates the simulation environment.
        First, rod intialized and then rod is modified to make it tapered.
        Second, muscle segments are intialized. Muscle segment position,
        number of basis functions and applied directions are set.
        Finally, friction plane is set and simulation is finalized.
        Returns
        -------

        """
        self.free = FreeAssembly()
        self.simulator = self.free.simulator
        self.tagtime = hash(time.time()) # Reset ID
        self.shearable_rods = {}
        self.rod_name = 'Twist'

        # setting up test params
        n_elem = 41
        direction = np.array([0.0, 1.0, 0.0])  # rod direction
        normal = np.array([0.0, 0.0, 1.0])
        base_length = 0.18
        base_radius = 0.007522
        E = 1e7
        rod_spec = {
            'n_elements':n_elem,
            'start':np.array([0,0,0]),
            'direction':direction,
            'normal':normal,
            'base_length':base_length,  # rod base length
            'base_radius':base_radius,  # rod base radius
            'density':1500,
            'nu':0.7,  # damping coefficient
            'youngs_modulus':E,
            'poisson_ratio':0.5,
        }

        # Define each FREE
        if self.rod_type == 'bending':
            self.free.add_free_bending(self.rod_name, 0.0, **rod_spec)
        elif self.rod_type == 'twist':
            self.free.add_free_twist(self.rod_name, **rod_spec)
        else:
            raise NotImplementedError("rod type {} is not yet implemented".format(self.rod_type))
        self.shearable_rods = self.free.free

        if self.COLLECT_DATA_FOR_POSTPROCESSING:
            # Collect data using callback function for postprocessing
            # set the diagnostics for rod and collect data
            self.data_rod = self.free.add_callback(self.rod_name, self.step_skip)

        # Finalize simulation environment. After finalize, you cannot add
        # any forcing, constrain or call back functions
        self.simulator.finalize()

        # do_step, stages_and_updates will be used in step function
        self.do_step, self.stages_and_updates = extend_stepper_interface(
            self.StatefulStepper, self.simulator
        )

        systems = self.simulator._systems
        return self.total_steps, systems

    def step(self, action, time):
        # Do 200 time step of simulation. Here we are doing multiple Elastica time-steps, because
        # time-step of elastica is much slower than the time-step of control or learning algorithm.

        # DEBUG PARAMETERS
        # nan_check : if true, track the position data and plot when nan if found

        # Setting external load
        actuation = {
            self.rod_name: [action],
        }
        self.free.set_actuation(actuation)

        for _ in range(self.learning_step):
            time = self.do_step(
                self.StatefulStepper,
                self.stages_and_updates,
                self.simulator,
                time,
                self.time_step,
            )

        systems = self.simulator._systems

        # Validate Continuous Condition
        # TODO: Return true if time is passed the total simulation time
        """ Done is a boolean to reset the environment before episode is completed """
        done = False
        # Position of the rod cannot be NaN, it is not valid, stop the simulation
        invalid_values_conditions = [
            _isnan_check(self.shearable_rods[self.rod_name].position_collection),
            _isnan_check(self.shearable_rods[self.rod_name].velocity_collection),
            _isnan_check(self.shearable_rods[self.rod_name].director_collection),
            _isnan_check(self.shearable_rods[self.rod_name].omega_collection),
            _isnan_check(self.shearable_rods[self.rod_name].acceleration_collection),
        ]
        if any(invalid_values_conditions):
            done = True
            print("Nan detected, exiting simulation now")
        if time >= self.final_time:
            done = True

        # Define reward
        reward = 0

        # Check if steady-state
        steady_state = False
        velocity = np.array(self.shearable_rods[self.rod_name].velocity_collection)
        max_velocity = np.linalg.norm(velocity, axis=1).max() 
        #acceleration = np.array(self.shearable_rods[self.rod_name].acceleration_collection)
        #max_acceleration = np.linalg.norm(acceleration, axis=0).max() 
        omega = np.array(self.shearable_rods[self.rod_name].omega_collection)
        max_omega = np.linalg.norm(omega, axis=1).max() 
        if max_velocity < 1e-3 and max_omega < 1e-3:
            steady_state = True

        return time, systems, reward, done, steady_state

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
                [self.data_rod],
                video_name=filename_video,
                fps=self.rendering_fps,
                step=1,
                save_folder=save_folder,
                **kwargs
            )

            return save_folder
        else:
            raise RuntimeError(
                "call back function is not called anytime during simulation, "
                "change COLLECT_DATA=True"
            )

    def save_data(self, path):
        # Transform nodal to elemental positions
        # Save the last position
        position_rod1 = np.array(self.data_rod["position"])
        position_rod1 = 0.5 * (position_rod1[-1,...,1:] + position_rod1[-1,...,:-1])

        # Save rod position (for povray)
        np.savez(
            path,
            position_rod1=position_rod1,
            director_rod1=np.array(self.data_rod["director"])[-1,...],
        )

    def debug(self):
        print(np.linalg.norm(self.shearable_rods[self.rod_name].velocity_collection, axis=0).max())
        print(np.linalg.norm(self.shearable_rods[self.rod_name].omega_collection, axis=0).max())
        print(np.linalg.norm(self.shearable_rods[self.rod_name].acceleration_collection, axis=0).max())

    def clear_callback(self):
        for key in self.data_rod.keys():
            self.data_rod[key].clear()
