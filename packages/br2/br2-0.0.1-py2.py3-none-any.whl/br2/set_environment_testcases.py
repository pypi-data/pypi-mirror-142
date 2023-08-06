import os
import sys

from elastica._calculus import _isnan_check
from elastica._linalg import _batch_cross, _batch_dot, _batch_norm, _batch_matmul, _batch_matrix_transpose, _batch_matvec

from elastica.external_forces import (
    EndpointForces,
    UniformTorques
)
from elastica.timestepper import extend_stepper_interface
from elastica import *

from surface_connection_parallel_rod_numba import (
    SurfaceJointSideBySide,
)

from elastica._calculus import _clip_array

from custom_constraint import LastEndFixedRod
from custom_activation import PointForces

from free_actuation import FreeTwistActuation
from free_simulator import DefaultCallback as CustomCallBack


from post_processing import (
    plot_video_with_surface,
)

### Set base simulator class ###
class BaseSimulator(BaseSystemCollection, Constraints, Connections, Forcing, CallBacks):
    pass

### General environment preset ###

class _Environment:
    def __init__(
        self,
        final_time,
        dt=4.0e-5,
        COLLECT_DATA_FOR_POSTPROCESSING=False,
        **kwargs
    ):
        super().__init__(**kwargs)
        # Integrator type
        self.StatefulStepper = PositionVerlet()

        # Simulation parameters
        self.final_time = final_time
        time_step = dt  # this is a stable timestep
        self.learning_step = 1
        self.total_steps = int(self.final_time / time_step / self.learning_step)
        self.time_step = np.float64(
            float(self.final_time) / (self.total_steps * self.learning_step)
        )

        # Rod Parameters
        n_elem = 40
        start = np.zeros((3,))
        direction = np.array([0.0, 1.0, 0.0])  # rod direction
        normal = np.array([0.0, 0.0, 1.0])
        binormal = np.cross(direction, normal)
        base_length = 1.0  # rod base length
        base_radius = 0.042  # rod base radius
        base_area = np.pi * base_radius ** 2
        density = 1500
        nu = 10.0 * 2 # 0.5
        E = 1e7  # Young's Modulus
        poisson_ratio = 0.5
        self.rod_parameters = {
            'n_elem' : n_elem,
            'start' : start,
            'direction' : direction,  # rod direction
            'normal' : normal,
            'binormal' : binormal,
            'base_length' : base_length,
            'base_radius' : base_radius,
            'base_area' : base_area,
            'density' : density,
            'nu' : nu,
            'E' : E,
            'poisson_ratio' : poisson_ratio,
        }

        # Glue Parameters
        k_conn = np.pi * base_radius * E / n_elem * 1e1 # 50  # 1e5
        nu_conn = base_length / n_elem * 1e-2 * 0
        kt_conn = base_radius / 2 * 1e4 
        k_contact_conn = k_conn * 0.0
        self.glue_parameters = {
            'k_conn' : k_conn,
            'nu_conn' : nu_conn,
            'kt_conn' : kt_conn,
            'k_contact_conn': k_contact_conn
        }

        # Video speed
        self.rendering_fps = 20
        self.step_skip = int(1.0 / (self.rendering_fps * self.time_step))

        # Collect data is a boolean. If it is true callback function collects
        # rod parameters defined by user in a list.
        self.COLLECT_DATA_FOR_POSTPROCESSING = COLLECT_DATA_FOR_POSTPROCESSING

    def reset(self):
        """
        This function, creates the simulation environment.
        First, rod intialized and then rod is modified to make it tapered.
        Second, muscle segments are intialized. Muscle segment position,
        number of basis functions and applied directions are set.
        Finally, friction plane is set and simulation is finalized.
        Returns
        -------

        """
        self.simulator = BaseSimulator()
        self.build(**self.rod_parameters, **self.glue_parameters)
        self.apply_activations()

        if self.COLLECT_DATA_FOR_POSTPROCESSING:
            # Collect data using callback function for postprocessing
            # step_skip = 500  # collect data every # steps
            self.post_processing_dicts = []
            for rod in self.rods:
                dlist = defaultdict(list) 
                self.simulator.collect_diagnostics(rod).using(
                    CustomCallBack,
                    step_skip=self.step_skip,
                    callback_params=dlist,
                )
                self.post_processing_dicts.append(dlist)

        # Finalize simulation environment. After finalize, you cannot add
        # any forcing, constrain or call back functions
        self.simulator.finalize()

        # do_step, stages_and_updates will be used in step function
        self.do_step, self.stages_and_updates = extend_stepper_interface(
            self.StatefulStepper, self.simulator
        )

        return self.total_steps, self.rods

    def step(self, time):
        # Do 200 time step of simulation. Here we are doing multiple Elastica time-steps, because
        # time-step of elastica is much slower than the time-step of control or learning algorithm.
        for _ in range(self.learning_step):
            time = self.do_step(
                self.StatefulStepper,
                self.stages_and_updates,
                self.simulator,
                time,
                self.time_step,
            )

        """ Done is a boolean to reset the environment before episode is completed """
        done = False

        # Nan check for position, velocity, angular acceleration, and director
        invalid_values_conditions = []
        for rod in self.rods:
            invalid_values_conditions.append(
                _isnan_check(rod.position_collection)
            )
            invalid_values_conditions.append(
                _isnan_check(rod.velocity_collection)
            )
            invalid_values_conditions.append(
                _isnan_check(rod.omega_collection)
            )
            invalid_values_conditions.append(
                _isnan_check(rod.director_collection)
            )

        if any(invalid_values_conditions):
            print(" Nan detected, exiting simulation now")
            done = True
        """ Done is a boolean to reset the environment before episode is completed """

        if self.final_time <= time:
            done = True

        return time, self.rods, done

    def post_processing(self, path, filename, **kwargs):
        """
        Make video 3D rod movement in time.
        Parameters
        ----------
        filename
        Returns
        -------

        """

        if self.COLLECT_DATA_FOR_POSTPROCESSING:
            # Create video
            plot_video_with_surface(
                self.post_processing_dicts,
                video_name=os.path.join(path, filename),
                fps=self.rendering_fps,
                step=1,
                **kwargs
            )

            # Save position and radius data (used for 3d rendering)
            data = {}
            for idx, dlist in enumerate(self.post_processing_dicts):
                position = np.array(dlist["position"])
                position = 0.5 * (position[..., 1:] + position[..., :-1])
                data['position_rod{}'.format(idx)] = position 
                data['radii_rod{}'.format(idx)] = np.array(dlist["radius"])
            np.savez(
                os.path.join(path, filename+'-data.npz'),
                **data
            )

        else:
            raise RuntimeError(
                "call back function is not called anytime during simulation, "
                "change COLLECT_DATA=True"
            )

    def glue_rods_surface_connection(self, rod1, rod2, k_conn, nu_conn, kt_conn, k_contact_conn):
        rod1_pos = 0.5 * (
            rod1.position_collection[..., 1:]
            + rod1.position_collection[..., :-1]
        )
        rod2_pos = 0.5 * (
            rod2.position_collection[..., 1:]
            + rod2.position_collection[..., :-1]
        )
        rod1_Q = rod1.director_collection
        rod2_Q = rod2.director_collection
        distance = _batch_norm(rod2_pos - rod1_pos)
        assert np.allclose(
            distance, rod1.radius+rod2.radius
        ), "Not all elements are touching eachother"
        connection_lab = (rod2_pos - rod1_pos) / distance
        rd1_local = _batch_matvec(rod1_Q, connection_lab) # local frame
        rd2_local = _batch_matvec(rod2_Q, -connection_lab) # local frame

        self.simulator.connect(
            first_rod=rod1, second_rod=rod2
        ).using(
            SurfaceJointSideBySide,
            k=k_conn,
            nu=nu_conn,
            kt=kt_conn,
            k_contact=k_contact_conn,
            rd1_local=rd1_local,
            rd2_local=rd2_local,
        )

### Rod Configuration Definitions ###
class _TwoParallelRodAssembly:
    def __init__(self, **kwargs):
        pass

    def build(self, n_elem, start, direction, normal, binormal,
              base_length, base_radius, base_area, density, E, nu, poisson_ratio,
              k_conn, nu_conn, kt_conn, k_contact_conn  # Connection spring constants
    ):
        """
        Function designated to build the arm
        The environment and simulator must be pre-defined.
        Add rod and constraint to the environment.
        """
        # Check if simulator is already defined
        assert hasattr(self, 'simulator') and type(self.simulator) == BaseSimulator

        # First rod
        self.shearable_rod1 = CosseratRod.straight_rod(
            n_elem,
            start,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        # second rod
        self.shearable_rod2 = CosseratRod.straight_rod(
            n_elem,
            start + (2 * base_radius) * normal,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )

        # Now rod is ready for simulation, append rod to simulation
        self.simulator.append(self.shearable_rod1)
        self.simulator.append(self.shearable_rod2)

        # Constrain the rod
        self.simulator.constrain(self.shearable_rod1).using(
            OneEndFixedRod, constrained_position_idx=(0,), constrained_director_idx=(0,)
        )
        self.simulator.constrain(self.shearable_rod2).using(
            OneEndFixedRod, constrained_position_idx=(0,), constrained_director_idx=(0,)
        )

        # Connect the rod
        self.glue_rods_surface_connection(self.shearable_rod1, self.shearable_rod2, k_conn, nu_conn, kt_conn, k_contact_conn)

        # Define rod collection
        self.rods = [self.shearable_rod1, self.shearable_rod2]


class _ThreeTriangleRodAssembly:
    def __init__(self, **kwargs):
        pass

    def build(self, n_elem, start, direction, normal, binormal,
              base_length, base_radius, base_area, density, E, nu, poisson_ratio,
              k_conn, nu_conn, kt_conn, k_contact_conn  # Connection spring constants
    ):
        """
        Function designated to build the arm
        The environment and simulator must be pre-defined.
        Add rod and constraint to the environment.
        """
        # Check if simulator is already defined
        assert hasattr(self, 'simulator') and type(self.simulator) == BaseSimulator

        # Define each FREE
        self.rods = []
        number_of_rod = 3
        angle_btw_rods = np.pi - 2*np.pi / number_of_rod
        to_next_center = np.array([np.cos(angle_btw_rods/2), 0.0, np.sin(angle_btw_rods/2)])
        R = np.array([
            [np.cos(np.pi-angle_btw_rods), 0, np.sin(np.pi-angle_btw_rods)],
            [0,1,0],
            [-np.sin(np.pi-angle_btw_rods), 0, np.cos(np.pi-angle_btw_rods)]])
        start = np.zeros((3,))
        for i in range(number_of_rod):
            # Add shearable rod
            shearable_rod = CosseratRod.straight_rod(
                n_elem,
                start,
                direction,
                normal,
                base_length,
                base_radius=base_radius,
                density=density,
                nu=nu,
                youngs_modulus=E,
                poisson_ratio=poisson_ratio,
            )
            self.rods.append(shearable_rod)
            # Move starting point
            start = start + to_next_center * 2 * base_radius
            to_next_center = R @ to_next_center
        self.shearable_rod1, self.shearable_rod2, self.shearable_rod3 = self.rods

        # Now rod is ready for simulation, append rod to simulation
        # Define rod collection
        self.simulator.append(self.shearable_rod1)
        self.simulator.append(self.shearable_rod2)
        self.simulator.append(self.shearable_rod3)

        # Constrain the rod
        self.simulator.constrain(self.shearable_rod1).using(
            OneEndFixedRod, constrained_position_idx=(0,), constrained_director_idx=(0,)
        )
        self.simulator.constrain(self.shearable_rod2).using(
            OneEndFixedRod, constrained_position_idx=(0,), constrained_director_idx=(0,)
        )
        self.simulator.constrain(self.shearable_rod3).using(
            OneEndFixedRod, constrained_position_idx=(0,), constrained_director_idx=(0,)
        )

        # Connect the rod
        self.glue_rods_surface_connection(self.shearable_rod1, self.shearable_rod2, k_conn, nu_conn, kt_conn, k_contact_conn)
        self.glue_rods_surface_connection(self.shearable_rod2, self.shearable_rod3, k_conn, nu_conn, kt_conn, k_contact_conn)
        self.glue_rods_surface_connection(self.shearable_rod3, self.shearable_rod1, k_conn, nu_conn, kt_conn, k_contact_conn)


class _FiveRodsCrossAssembly:
    def __init__(self,  **kwargs):
        pass

    def build(self, n_elem, start, direction, normal, binormal,
              base_length, base_radius, base_area, density, E, nu, poisson_ratio,
              k_conn, nu_conn, kt_conn, k_contact_conn  # Connection spring constants
    ):
        """
        Function designated to build the arm
        The environment and simulator must be pre-defined.
        Add rod and constraint to the environment.
        """
        # Check if simulator is already defined
        assert hasattr(self, 'simulator') and type(self.simulator) == BaseSimulator

        # Center rod
        self.shearable_rod1 = CosseratRod.straight_rod(
            n_elem,
            start,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        self.shearable_rod2 = CosseratRod.straight_rod(
            n_elem,
            start - (2 * base_radius) * normal,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        self.shearable_rod3 = CosseratRod.straight_rod(
            n_elem,
            start + (2 * base_radius) * normal,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        self.shearable_rod4 = CosseratRod.straight_rod(
            n_elem,
            start - (2 * base_radius) * binormal,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        self.shearable_rod5 = CosseratRod.straight_rod(
            n_elem,
            start + (2 * base_radius) * binormal,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )

        # Now rod is ready for simulation, append rod to simulation
        # Define rod collection
        self.rods = [self.shearable_rod1, self.shearable_rod2, self.shearable_rod3, self.shearable_rod4, self.shearable_rod5]
        for rod in self.rods:
            self.simulator.append(rod)

        # Constrain the rod
        for rod in self.rods:
            self.simulator.constrain(rod).using(
                OneEndFixedRod, constrained_position_idx=(0,), constrained_director_idx=(0,)
            )

        # Connect the rod
        self.glue_rods_surface_connection(self.shearable_rod1, self.shearable_rod2, k_conn, nu_conn, kt_conn, k_contact_conn)
        self.glue_rods_surface_connection(self.shearable_rod1, self.shearable_rod3, k_conn, nu_conn, kt_conn, k_contact_conn)
        self.glue_rods_surface_connection(self.shearable_rod1, self.shearable_rod4, k_conn, nu_conn, kt_conn, k_contact_conn)
        self.glue_rods_surface_connection(self.shearable_rod1, self.shearable_rod5, k_conn, nu_conn, kt_conn, k_contact_conn)


class _FiveRodsWallAssembly:
    def __init__(self, **kwargs):
        pass

    def build(self, n_elem, start, direction, normal, binormal,
              base_length, base_radius, base_area, density, E, nu, poisson_ratio,
              k_conn, nu_conn, kt_conn, k_contact_conn  # Connection spring constants
    ):
        """
        Function designated to build the arm
        The environment and simulator must be pre-defined.
        Add rod and constraint to the environment.
        """
        # Check if simulator is already defined
        assert hasattr(self, 'simulator') and type(self.simulator) == BaseSimulator

        self.rods = []
        num_rod = 5
        for idx in range(num_rod):
            rod = CosseratRod.straight_rod(
                n_elem,
                start + idx * (2*base_radius) * normal,
                direction,
                normal,
                base_length,
                base_radius=base_radius,
                density=density,
                nu=nu,
                youngs_modulus=E,
                poisson_ratio=poisson_ratio,
            )
            self.simulator.append(rod)
            self.rods.append(rod)

            # Constrain the rod
            self.simulator.constrain(rod).using(
                OneEndFixedRod, constrained_position_idx=(0,), constrained_director_idx=(0,)
            )
        # Constrain both end for the first rod
        self.simulator.constrain(self.rods[0]).using(
            LastEndFixedRod, constrained_position_idx=(-1,), constrained_director_idx=(-1,)
        )

        # Connect the rod
        for rod1, rod2 in zip(self.rods[:-1], self.rods[1:]):
            self.glue_rods_surface_connection(rod1, rod2, k_conn, nu_conn, kt_conn, k_contact_conn)

class _TwoParallelRodAssemblySymmetricTestSetup:
    """
    Special Case:
    Connectivity function must be parallel.
    The configuration provide four pairs of two parallel rod.
    Two (out of four) pairs have activation on left rod, and other two pairs have 
    activation on right-rod. Each set has one connection defined such that 
    'connect rod1->rod2' other connection defined such that 'connect rod2->rod1.'
    All four pair must behave same to confirm the symmetric implementation.
    """
    def __init__(self, **kwargs):
        pass

    def build(self, n_elem, start, direction, normal, binormal,
              base_length, base_radius, base_area, density, E, nu, poisson_ratio,
              k_conn, nu_conn, kt_conn, k_contact_conn  # Connection spring constants
    ):
        """
        Function designated to build the arm
        The environment and simulator must be pre-defined.
        Add rod and constraint to the environment.
        """
        # Check if simulator is already defined
        assert hasattr(self, 'simulator') and type(self.simulator) == BaseSimulator

        # First Row (1,2)
        self.shearable_rod1 = CosseratRod.straight_rod(
            n_elem,
            start,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        self.shearable_rod2 = CosseratRod.straight_rod(
            n_elem,
            start + (2 * base_radius) * normal,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        # Second Row (3,4)
        start += (5*base_radius*binormal)
        self.shearable_rod3 = CosseratRod.straight_rod(
            n_elem,
            start,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        self.shearable_rod4 = CosseratRod.straight_rod(
            n_elem,
            start + (2 * base_radius) * normal,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        # Third Row (5,6)
        start += (5*base_radius*binormal)
        self.shearable_rod5 = CosseratRod.straight_rod(
            n_elem,
            start,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        self.shearable_rod6 = CosseratRod.straight_rod(
            n_elem,
            start + (2 * base_radius) * normal,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        # Fourth Row (7,8)
        start += (5*base_radius*binormal)
        self.shearable_rod7 = CosseratRod.straight_rod(
            n_elem,
            start,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )
        self.shearable_rod8 = CosseratRod.straight_rod(
            n_elem,
            start + (2 * base_radius) * normal,
            direction,
            normal,
            base_length,
            base_radius=base_radius,
            density=density,
            nu=nu,
            youngs_modulus=E,
            poisson_ratio=poisson_ratio,
        )

        # Define rod collection
        self.rods = [self.shearable_rod1, self.shearable_rod2, self.shearable_rod3, self.shearable_rod4,
                self.shearable_rod5, self.shearable_rod6, self.shearable_rod7, self.shearable_rod8]
        for rod in self.rods:
            self.simulator.append(rod)

        # Constrain the rod
        for rod in self.rods:
            self.simulator.constrain(rod).using(
                OneEndFixedRod, constrained_position_idx=(0,), constrained_director_idx=(0,)
            )

        # Connect the rod
        self.glue_rods_surface_connection(self.shearable_rod1, self.shearable_rod2, k_conn, nu_conn, kt_conn, k_contact_conn)
        self.glue_rods_surface_connection(self.shearable_rod4, self.shearable_rod3, k_conn, nu_conn, kt_conn, k_contact_conn)
        self.glue_rods_surface_connection(self.shearable_rod5, self.shearable_rod6, k_conn, nu_conn, kt_conn, k_contact_conn)
        self.glue_rods_surface_connection(self.shearable_rod8, self.shearable_rod7, k_conn, nu_conn, kt_conn, k_contact_conn)

class _ThreeTriangleRodFloatingAssembly:
    """
    Special Case: Floating (Without any constraint) mode
    """
    def __init__(self, **kwargs):
        pass

    def build(self, n_elem, start, direction, normal, binormal,
              base_length, base_radius, base_area, density, E, nu, poisson_ratio,
              k_conn, nu_conn, kt_conn, k_contact_conn  # Connection spring constants
    ):
        """
        Function designated to build the arm
        The environment and simulator must be pre-defined.
        Add rod and constraint to the environment.
        """
        # Check if simulator is already defined
        assert hasattr(self, 'simulator') and type(self.simulator) == BaseSimulator

        # Define each FREE
        self.rods = []
        number_of_rod = 3
        angle_btw_rods = np.pi - 2*np.pi / number_of_rod
        to_next_center = np.array([np.cos(angle_btw_rods/2), 0.0, np.sin(angle_btw_rods/2)])
        R = np.array([
            [np.cos(np.pi-angle_btw_rods), 0, np.sin(np.pi-angle_btw_rods)],
            [0,1,0],
            [-np.sin(np.pi-angle_btw_rods), 0, np.cos(np.pi-angle_btw_rods)]])
        start = np.zeros((3,))
        for i in range(number_of_rod):
            # Add shearable rod
            shearable_rod = CosseratRod.straight_rod(
                n_elem,
                start,
                direction,
                normal,
                base_length,
                base_radius=base_radius,
                density=density,
                nu=nu,
                youngs_modulus=E,
                poisson_ratio=poisson_ratio,
            )
            self.rods.append(shearable_rod)
            # Move starting point
            start = start + to_next_center * 2 * base_radius
            to_next_center = R @ to_next_center
        self.shearable_rod1, self.shearable_rod2, self.shearable_rod3 = self.rods

        # Now rod is ready for simulation, append rod to simulation
        # Define rod collection
        self.simulator.append(self.shearable_rod1)
        self.simulator.append(self.shearable_rod2)
        self.simulator.append(self.shearable_rod3)

        # Connect the rod
        self.glue_rods_surface_connection(self.shearable_rod1, self.shearable_rod2, k_conn, nu_conn, kt_conn, k_contact_conn)
        self.glue_rods_surface_connection(self.shearable_rod2, self.shearable_rod3, k_conn, nu_conn, kt_conn, k_contact_conn)
        self.glue_rods_surface_connection(self.shearable_rod3, self.shearable_rod1, k_conn, nu_conn, kt_conn, k_contact_conn)

### Experiment Setup ###
class ExperimentSimpleTwoRodConnection(_Environment, _TwoParallelRodAssembly):
    def __init__(self, force=None, torque=None, torque_direction=None, **kwargs):
        super().__init__(**kwargs)
        self.force = force
        self.torque = torque
        self.torque_direction = torque_direction

    def apply_activations(self):
        rod = self.shearable_rod1
        # Apply Forces
        if self.force is not None:
            self.simulator.add_forcing_to(rod).using(
                EndpointForces,
                start_force=np.array([0.0, 0.0, 0.0]),
                end_force=self.force,
                ramp_up_time=1.0
            )
        # Apply Torque
        if self.torque is not None:
            # Apply Torque
            self.simulator.add_forcing_to(rod).using(
                UniformTorques,
                #FreeTwistActuation,
                torque = self.torque,
                direction = self.torque_direction,
            )

class ExperimentSimpleThreeTriangleConnection(_Environment, _ThreeTriangleRodAssembly):
    def __init__(self, force=None, torque=None, torque_direction=None, **kwargs):
        super().__init__(**kwargs)
        self.force = force
        self.torque = torque
        self.torque_direction = torque_direction

    def apply_activations(self):
        rod = self.shearable_rod1
        # Apply Forces
        if self.force is not None:
            self.simulator.add_forcing_to(rod).using(
                EndpointForces,
                start_force=np.array([0.0, 0.0, 0.0]),
                end_force=self.force,
                ramp_up_time=1.0
            )
        # Apply Torque
        if self.torque is not None:
            # Apply Torque
            self.simulator.add_forcing_to(rod).using(
                UniformTorques,
                #FreeTwistActuation,
                torque = self.torque,
                direction = self.torque_direction,
            )


class ExperimentFiveCrossConnection(_Environment, _FiveRodsCrossAssembly):
    def __init__(self, force=None, torque=None, torque_direction=None, **kwargs):
        super().__init__(**kwargs)
        self.force = force
        self.torque = torque
        self.torque_direction = torque_direction

    def apply_activations(self):
        rod = self.shearable_rod1
        # Apply Forces
        if self.force is not None:
            self.simulator.add_forcing_to(rod).using(
                EndpointForces,
                start_force=np.array([0.0, 0.0, 0.0]),
                end_force=self.force,
                ramp_up_time=1.0
            )
        # Apply Torque
        if self.torque is not None:
            # Apply Torque
            self.simulator.add_forcing_to(rod).using(
                UniformTorques,
                #FreeTwistActuation,
                torque = self.torque,
                direction = self.torque_direction,
            )


class ExperimentFiveWallConnection(_Environment, _FiveRodsWallAssembly):
    # Pull two opposite rod in anti-direction
    def __init__(self, force, mode, **kwargs):
        super().__init__(**kwargs)
        self.linear_force = force
        if mode == 'shear-antiplane':
            self.direction = np.array([1.0, 0.0, 0.0])
        elif mode == 'shear-inplane':
            self.direction = np.array([0.0, 1.0, 0.0])
        elif mode == 'peel':
            self.direction = np.array([0.0, 0.0, 1.0])
        else:
            raise NotImplementedError("mode {} is not yet implemented".format(mode))

    def apply_activations(self):
        # Apply Forces
        #self.simulator.add_forcing_to(self.rods[0]).using(
        #    EndpointForces,
        #    start_force=np.array([0.0, 0.0, 0.0]),
        #    end_force=self.linear_force * self.direction,
        #    ramp_up_time=0.5
        #)
        self.simulator.add_forcing_to(self.rods[-1]).using(
            EndpointForces,
            start_force=np.array([0.0, 0.0, 0.0]),
            end_force=self.linear_force * self.direction,
            ramp_up_time=0.5
        )

class ExperimentFiveWallConnectionMiddleActivation(_Environment, _FiveRodsWallAssembly):
    # Pull two opposite rod in anti-direction
    def __init__(self, force, mode, **kwargs):
        super().__init__(**kwargs)
        self.linear_force = force
        if mode == 'shear-antiplane':
            self.direction = np.array([1.0, 0.0, 0.0])
        elif mode == 'shear-inplane':
            self.direction = np.array([0.0, 1.0, 0.0])
        elif mode == 'peel':
            self.direction = np.array([0.0, 0.0, 1.0])
        else:
            raise NotImplementedError("mode {} is not yet implemented".format(mode))

    def apply_activations(self):
        # Apply Forces
        self.simulator.add_forcing_to(self.rods[-1]).using(
            PointForces,
            force=self.linear_force * self.direction,
            location=0.5,
            ramp_up_time=0.5
        )

class ExperimentSymmetricConnectivityTest(_Environment, _TwoParallelRodAssemblySymmetricTestSetup):
    def __init__(self, torque, direction, **kwargs):
        super().__init__(**kwargs)
        self.torque_magnitude = torque
        self.torque_direction = direction

    def apply_activations(self):
        # Apply Torque
        self.simulator.add_forcing_to(self.shearable_rod1).using(
            FreeTwistActuation,
            torque = [self.torque_magnitude],
            direction = self.torque_direction,
            ramp_up_time=0.2,
        )
        self.simulator.add_forcing_to(self.shearable_rod3).using(
            FreeTwistActuation,
            torque = [self.torque_magnitude],
            direction = self.torque_direction,
            ramp_up_time=0.2,
        )
        self.simulator.add_forcing_to(self.shearable_rod6).using(
            FreeTwistActuation,
            torque = [self.torque_magnitude],
            direction = -self.torque_direction,
            ramp_up_time=0.2,
        )
        self.simulator.add_forcing_to(self.shearable_rod8).using(
            FreeTwistActuation,
            torque = [self.torque_magnitude],
            direction = -self.torque_direction,
            ramp_up_time=0.2,
        )

