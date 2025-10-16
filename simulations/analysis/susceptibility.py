#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import gsd.fl to read file type.
import gsd.fl
import argparse
from scipy.stats import kurtosis
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--N")
parser.add_argument("-l", "--activity")
parser.add_argument("-p", "--phi")
parser.add_argument("-f", "--frames")
args = parser.parse_args()

N = int(args.N)
activity = float(args.activity)
phi = float(args.phi)
frame=int(args.frames)
a=4.0

gsd_file = "activity_" + str(activity) +  "_N_" + str(N)+ "_phi_" + "%.3f" % phi + "_asp_"  + "%.3f" % a + ".gsd"

#Now let's read a gsd file!
f = gsd.fl.open(gsd_file, 'r')

#get the number of frames in the file
nsteps= f.nframes
print("number of frames = ",nsteps,flush=True)

#get the number of particles
particles=f.read_chunk(frame=0, name='particles/N')[0]
lengths=f.read_chunk(frame=0, name='configuration/box')

Lx=lengths[0]
Ly=lengths[1]
Lz=lengths[2]

#these are the vectors that will be used to calculate the statisitics in each sub-region of the box.
rhos=[[] for _ in range(8)]
Ns=[[] for _ in range(8)]

#loop of the frames from tstart to nsteps
for t in range(nsteps-frame,nsteps):
    if t%100==0:
        print(t,flush=True)

    Nsub=np.zeros(8)
    rho=np.zeros(8)

    #particle positions format is [particle_number dimensions_in_x(1)_y(2)_Z(3)]

    #get particle positions and the box length at every time.
    pos=f.read_chunk(frame=t, name='particles/position')

    #put positions from 0 to L by adding L/2.
    box = lengths[np.newaxis,:3]
    pos = pos + box/2

    theta = pos[:,2]/Lz * 2*np.pi
    alpha = np.cos(theta)
    beta = np.sin(theta)
    alphabar = np.mean(alpha)
    betabar = np.mean(beta)
    thetabar = np.arctan2(-betabar, -alphabar) + np.pi
    zcom = Lz*thetabar/(2*np.pi)
    zcom = zcom - np.floor(zcom/Lz)*Lz

    xyz = np.copy(pos)
    xyz[:,2] -= zcom
    xyz = xyz - np.floor(xyz/box)*box
    #for time t do another for loop and as ask if the particles are within
    #the subvolumes

    bc = np.array([[Lx*3/4,Lx*3/4,Lx*3/4,Lx*3/4,Lx/4,Lx/4,Lx/4,Lx/4],
        [Ly*3/4,Ly/4,Ly*3/4,Ly/4,Ly*3/4,Ly/4,Ly*3/4,Ly/4],
        [0.*Lz,0.*Lz,Lz/2,Lz/2,0.*Lz,0.*Lz,Lz/2,Lz/2]])
    bc = bc.T
    bc = bc[:,np.newaxis,:]
    for j in range(8):
        dr = xyz[:] - bc[j]
        dr = np.absolute(dr - np.around(dr / box) * box)
        in_box = np.all(dr < Ly / 4, axis=1)
        Nsub[j] = dr[in_box].shape[0]

    #print(Nsub1,Nsub2,Nsub3,Nsub4,Nsub5,Nsub6,Nsub7, Nsub8)
    #calculate the densities at every time.
    for k in range(8):
        rho[k]=Nsub[k]/(Ly**3/8)

    #save each density to the vectors
    for k in range(8):
        rhos[k].append(rho[k])
        Ns[k].append(Nsub[k])

Ns_squared=[[] for _ in range(8)]
for i in range(8):
    for j in range(len(Ns[i])):
        Ns_squared[i].append(Ns[i][j]**2)

chi_array=[]
for _ in range(8):
    chi_array.append(np.average(Ns_squared[_])/np.average(Ns[_])-np.average(Ns[_]))

rho_array=[]
for _ in range(8):
    rho_array.append(np.average(rhos[_]))

print(chi_array,flush=True)
print(np.average(chi_array), flush=True)
#print(rho_array,flush=True)


chi=np.var(np.asarray(Ns).flatten())/np.average(np.asarray(Ns).flatten())
print(chi,flush=True)

