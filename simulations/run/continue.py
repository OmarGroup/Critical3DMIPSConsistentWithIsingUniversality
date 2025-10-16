import os
import argparse
import numpy as np
from pyquaternion import Quaternion
import hoomd
import gsd.hoomd
import time

class Pressure():
    def __init__(self, simulation):
        self.simulation = simulation

    @property
    def time_step(self):
        return self.simulation.timestep

#### HOOMD SCRIPT ####
# initialize
gpu = hoomd.device.GPU()
simulation = hoomd.Simulation(device=gpu, seed=np.random.randint(100))

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--N")
parser.add_argument("-l", "--activity")
#parser.add_argument("-l0", "--activity0")
parser.add_argument("-t", "--time")
parser.add_argument("-p", "--phi")
args = parser.parse_args()

N = int(args.N)
activity = float(args.activity)
#activity0 = float(args.activity0)
phi = float(args.phi)
total_time = float(args.time)
a = 4.0

# assuming radius, friction and velocity are set to unity
U = 1.0
sigma=1.0
zeta=1.0

Rl=activity*sigma
tauR = Rl/U
DR = 1 / tauR
swim_force = zeta * U

#init_file= "../"+str(activity0)+"_ell/activity_" + str(activity0) +  "_N_" + str(N)+ "_phi_" + "%.3f" % phi + "_asp_"  + "%.3f" % a + ".gsd"
gsd_file = "activity_" + str(activity) +  "_N_" + str(N)+ "_phi_" + "%.3f" % phi + "_asp_"  + "%.3f" % a + ".gsd"
table_file = "activity_" + str(activity)  + "_N_" + str(N) + "_phi_" + "%.3f" % phi + "_asp_"  + "%.3f" % a + ".table"

if os.path.isfile(gsd_file):
    simulation.create_state_from_gsd(filename=gsd_file,frame=-1)
else:
    print("Err!")

time_step = 5e-5  # timestep based on shortest relaxation time, assumed to be convective swimming
num_steps = int(total_time/time_step)
output=int(0.5/time_step)

integrator = hoomd.md.Integrator(dt=time_step)
cell = hoomd.md.nlist.Cell(buffer=0.1)
lj = hoomd.md.pair.LJ(nlist=cell)
lj.params[('A', 'A')] = dict(epsilon=50.0*sigma*zeta*U, sigma= sigma)
lj.r_cut[('A', 'A')] = 2.0 ** (1. / 6.) * sigma
integrator.forces.append(lj)

active = hoomd.md.force.Active(filter=hoomd.filter.All())
active.active_force['A'] = (swim_force,0,0)
active.active_torque['A'] = (0,0,0)
rotational_diffusion_updater = active.create_diffusion_updater(trigger=1,rotational_diffusion=2*DR)
integrator.forces.append(active)

overdamped_viscous = hoomd.md.methods.OverdampedViscous(filter=hoomd.filter.All())
overdamped_viscous.gamma['A'] = zeta
overdamped_viscous.gamma_r['A'] = [0.0, 0.0, 0.0]
integrator.methods.append(overdamped_viscous)

simulation.operations.integrator = integrator
simulation.operations+=rotational_diffusion_updater

gsd_writer = hoomd.write.GSD(filename=gsd_file,trigger=hoomd.trigger.Periodic(output),mode='ab',filter=hoomd.filter.All(),dynamic=['property'])

logger = hoomd.logging.Logger(categories=['scalar'])
pressure = Pressure(simulation)
logger['time_step']=(pressure,'time_step','scalar')

table = hoomd.write.Table(trigger=hoomd.trigger.Periodic(period=1000000), logger=logger,output=open(table_file,'w'))

simulation.operations.writers.append(gsd_writer)
simulation.operations.writers.append(table)

simulation.run(num_steps)
