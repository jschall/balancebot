import numpy as np
from scipy.integrate import odeint
from sys import exit
from math import *
from helpers import quatderiv

class BalanceBot:
    def __init__(self):
        self.stalk_len = 1.8
        self.pos_cart_bf = np.asarray(0,0,0)
        self.pos_head_bf = np.asarray(0,0,-self.stalk_len)
        self.pos_stalk_bf = np.asarray(0,0,-self.stalk_len*0.5)


    def getRWheelForce(self):
        pass

    def update(self):
        pass

def dyn(state, t, params):
    quat = state[0:4]
    omega = params[0:3]

    return quatderiv(quat, omega)

from visual import *

dt = 1./60.
t = 0.

state = [1.,0.,0.,0.]
while True:
    rate(1./dt)
    inttime = np.linspace(t,t+dt,3)

    state = odeint(dyn, state, inttime, args=((1.,0.,0.),))[-1]
    t += dt
    print state

#def ecef2vpy(vec):
    #return vector(vec[1], vec[2], vec[0])

#earth = sphere(material = materials.earth, radius = 6.371e6)
#rocket = cylinder(pos=ecef2vpy((6.371e6, 0, 0)), axis=ecef2vpy((21,0,0)), radius=9)

#scene.center = ecef2vpy((6.371e6, 0, 0))
#scene.forward = ecef2vpy((0,0,1))
#scene.range = 10000.
