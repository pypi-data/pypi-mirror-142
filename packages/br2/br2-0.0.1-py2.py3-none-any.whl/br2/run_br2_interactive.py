import multiprocessing
from multiprocessing import Process, Queue, Array, Value

import os
import sys
import copy
import time

import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import minimize
from functools import partial

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from tqdm import tqdm

sys.path.append("../") # For elastica
#sys.settrace # For debugging
from set_environment_br2 import (
    Environment,
)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QSlider,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

class ControlWindow(QMainWindow):

    def __init__(self, actuation, kill_process, parent=None):
        super().__init__(parent)
        self.actuation = actuation
        self.kill_process = kill_process
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyElastica BR2 Control")
        self.resize(300, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Create and connect widgets
        self.bendActivationLabel = QLabel("Bend Pressure", self)
        self.bendActivationLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.twist1ActivationLabel = QLabel("twist 1 Pressure", self)
        self.twist1ActivationLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.twist2ActivationLabel = QLabel("twist 2 Pressure", self)
        self.twist2ActivationLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.bendActivationTextbox = QLineEdit(self)
        self.bendActivationTextbox.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.bendActivationTextbox.setText(str(self.actuation[0]))
        #self.bendActivationTextbox.resize(280,40)
        self.twist1ActivationTextbox = QLineEdit(self)
        self.twist1ActivationTextbox.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.twist1ActivationTextbox.setText(str(self.actuation[1]))
        #self.twist1ActivationTextbox.resize(280,40)
        self.twist2ActivationTextbox = QLineEdit(self)
        self.twist2ActivationTextbox.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.twist2ActivationTextbox.setText(str(self.actuation[2]))
        #self.twist2ActivationTextbox.resize(280,40)

        self.applyBtn = QPushButton("Apply", self)
        self.applyBtn.clicked.connect(self.applyActivation)
        self.killBtn = QPushButton("Kill Process", self)
        self.killBtn.clicked.connect(self.killProcess)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.bendActivationLabel)
        layout.addWidget(self.bendActivationTextbox)
        layout.addWidget(self.twist1ActivationLabel)
        layout.addWidget(self.twist1ActivationTextbox)
        layout.addWidget(self.twist2ActivationLabel)
        layout.addWidget(self.twist2ActivationTextbox)
        layout.addStretch()
        layout.addWidget(self.applyBtn)
        layout.addWidget(self.killBtn)
        self.centralWidget.setLayout(layout)

    def applyActivation(self):
        self.actuation[0] = float(str(self.bendActivationTextbox.text()))
        self.actuation[1] = float(str(self.twist1ActivationTextbox.text()))
        self.actuation[2] = float(str(self.twist2ActivationTextbox.text()))
        print('New actuation: {}, {}, {}'.format(self.actuation[0], self.actuation[1], self.actuation[2]))

    def killProcess(self):
        self.kill_process.value = 1
        print('kill signal')


def visualizer(data_q, kill_process):
    # Lambdas
    rod_history_unpacker = lambda history, rod_idx, t_idx: (
        history[rod_idx]["position"][t_idx],
        history[rod_idx]["radius"][t_idx],
    )
    difference = lambda x: x[1] - x[0]

    # Initialize Axes and Show(non-block)
    fig = plt.figure(1, figsize=(10, 8))
    ax = plt.axes(projection="3d")

    ax.set_xlabel("z")
    ax.set_ylabel("x")
    ax.set_zlabel("y")

    xlim = (-0.13, 0.13)
    ylim = (0, 0.3)
    zlim = (-0.13, 0.13)
    ax.set_xlim(*zlim)
    ax.set_ylim(*xlim)
    ax.set_zlim(*ylim)

    plt.show(block=False)
    plt.pause(0.5)

    # Plot Configuration
    max_axis_length = max(difference(xlim), difference(ylim))
    scaling_factor = (2 * 0.1) / max_axis_length  # Octopus head dimension
    scaling_factor *= 2.6e3  # Along one-axis

    # First plot
    print('receive ready')
    rods_history = data_q.get()
    print('received')

    # Set simulation time as title
    sim_time = np.array(rods_history[0]["time"])[-1]
    ax.set_title('simulation time: t={}'.format(sim_time))

    # Initial axes plot
    time_idx = -1
    rod_scatters = [None for _ in range(len(rods_history))]
    for rod_idx in range(len(rods_history)):
        inst_position, inst_radius = rod_history_unpacker(rods_history, rod_idx, time_idx)
        _s = np.pi * (scaling_factor * inst_radius[0]) ** 2
        rod_scatters[rod_idx] = ax.scatter(
            -inst_position[2],
            -inst_position[0],
            inst_position[1],
            s=_s,
        )
    ax.set_aspect("auto")
    plt.show(block=False)
    plt.pause(0.1)

    # Update plot
    while kill_process.value != 1:
        # Fetch data from simulator
        print('receive ready')
        rods_history = data_q.get()
        print('received')

        # Set simulation time as title
        sim_time = np.array(rods_history[0]["time"])[-1]
        ax.set_title('simulation time: t={}'.format(sim_time))

        with plt.style.context("seaborn-whitegrid"):
            time_idx = -1
            for rod_idx in range(len(rods_history)):
                inst_position, inst_radius = rod_history_unpacker(rods_history, rod_idx, time_idx)
                inst_position = 0.5 * (
                    inst_position[..., 1:] + inst_position[..., :-1]
                )
                rod_scatters[rod_idx]._offsets3d = (
                    -inst_position[2],
                    -inst_position[0],
                    inst_position[1],
                )
                rod_scatters[rod_idx].set_sizes(
                    np.pi * (scaling_factor * inst_radius) ** 2,
                )
            plt.show(block=False)
            plt.pause(0.1)

    plt.close(plt.gcf())

def simulator(actuation, data_q, kill_process):
    # Configuration 
    plot_interval = 0.1 # in simulation time
    next_plot_time = plot_interval

    # Set simulation final time
    env = Environment(
            final_time=86400,  # Default 24 hours max
            fps=20,
            COLLECT_DATA_FOR_POSTPROCESSING=True,
            )

    # Reset the environment before the new episode and get total number of simulation steps
    total_steps, systems = env.reset()
    print(f'Total simulation steps: {total_steps}')

    # Simulation
    time = np.float64(0.0)
    i_sim = 0
    done = False
    while not done:
        i_sim += 1

        # Simulation
        time, systems, reward, done = env.step(actuation, time, nan_check=0, steady_state_check=False)

        if kill_process.value == 1:
            done = True

        # If done=True, NaN detected in simulation.
        # Exit the simulation loop before, reaching final time
        if done:
            print(" Episode finished after {} ".format(time))
            break

        # Plot-Send data to visualizer
        if time > next_plot_time:
            print('send visualization data')
            data_q.put_nowait(systems)
            next_plot_time += plot_interval

    # Simulation loop ends
    print("Final time of simulation is : ", time)

# Main Process
if __name__ == "__main__":
    # Prepare Communication
    actuation = Array('d', [500.0, 0.0, 0.0])
    kill_process = Value('i', 0)
    data_queue = Queue()

    # Simulator
    process_simulator = Process(target=simulator, args=(actuation, data_queue, kill_process, ))

    # Visualizer 
    process_visualizer = Process(target=visualizer, args=(data_queue, kill_process, ))

    # Controller
    app = QApplication(sys.argv)
    ex = ControlWindow(actuation, kill_process)
    ex.show()

    # Run
    process_simulator.start()
    process_visualizer.start()
    app_exec = app.exec_()

    # Finalize
    data_queue.close()
    data_queue.join_thread()
    process_simulator.join()
    process_visualizer.join()

    sys.exit(app_exec)
