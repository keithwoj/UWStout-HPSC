from pylab import *
from scipy.integrate import odeint

'''
Script for executing conventional RK4 Method

Author: Keith J. Wojciechowski (KJW)n

First Working Version 03 JUN 2015
'''
# //////////////////////////////////////////////////////////////////////////////
# Conventional RK4 Solver
def RK4(y0,t0,tf,h):
    
    n = int(1/h)
    y = zeros(n)
    yt = y0
    tt = t0
    
    for j in xrange(n):
        y[j] = yt
        k1 = F(yt,tt)
        k2 = F(yt+h*k1/2,tt+h/2)
        k3 = F(yt+h*k2/2,tt+h/2)
        k4 = F(yt+h*k3,tt+h)
        
        yt = yt + (k1 + 2*k2 + 2*k3 + k4)*h/6
        tt += h
    return y
# //////////////////////////////////////////////////////////////////////////////
# ODE Function, dy/dt = F(y,t)
def F(y,t):
    return -2*y
# //////////////////////////////////////////////////////////////////////////////    
# Initial values and time step
y0 = 1.0
t0 = 0
tf = 1.0
h = 1e-2  # time-step
tv = linspace(t0,tf,1/h) # create time interval for plotting
# //////////////////////////////////////////////////////////////////////////////
# Call RK4 solver
y = RK4(y0, t0, tf, h)

# SciPy Solver
yp = odeint(F, y0, tv)
# //////////////////////////////////////////////////////////////////////////////
plot(tv,y0*exp(-2*tv),'r',tv,y,'b',tv,yp,'g')
show()