# -*- coding: utf-8 -*-
"""
Module for implementing ODE integrators
Created on Thu Jun 18 15:56:18 2015

@author: Keith J. Wojciechowski (KJW)

The functions for this module adopt the following convention

[y, t] = SOLVER(F,y0,t0,tf,h)

Input:
        F -- Function to be integrated dy/dt = F(y,t)
        y0 -- initial value
        t0 -- initial time
        tf -- final time
        h -- time-step
        
Output:
        y -- numerical solution as an n-size array
        t -- vector of time steps, linspace(t0,tf,n)
        
Notes:
        n = int((tf-t0)/h)+1 since h = (tf - t0)/(n-1)
        
Edits:
        19 JUN 2015:
        First working version RK4e (KJW)
        Unit test added, dy/dt = -2*t*y, h = 0.1, 0.01, 0.001 (KJW)
        
Solvers:
        [y, t] = RK4e(F,y0,t0,tf,h)
"""

from pylab import *

# Conventional RK4 Solver using evenly-space nodes
def RK4e(F,y0,t0,tf,h):
    # Initialize the number of iterations and the array containing the solution
    # Note: h = (tf - t0)/(n-1)
    n = int((tf-t0)/h)+1
    tv = linspace(t0,tf,n)
    y = 0*tv
    # Initial y and time values
    y[0] = y0
    # Step through the integrator
    for j in xrange(n-1):
        k1 = F(y[j],tv[j])                   # Euler's method
        k2 = F(y[j]+0.5*h*k1,tv[j]+0.5*h)    # Slope at midpoint
        k3 = F(y[j]+0.5*h*k2,tv[j]+0.5*h)    # Slope at midpoint
        k4 = F(y[j]+h*k3,tv[j]+h)            # Slope at next time-step
        # Integrate (Simpson's method) to obtain solution at next time step
        y[j+1] = y[j] + (k1 + 2*(k2 + k3) + k4)*h/6.
    return y, tv

# ODE Test Function, dy/dt = F(y,t)
def testf(y,t):
    return -2.*t*y

def test():
    t0 = -3
    tf = 3
    y0 = sqrt(pi)/2*exp(-t0**2)
    hvec = array([0.1, 0.01, 0.001])
    for h in hvec:
        [y, tv] = RK4e(testf,y0,t0,tf,h)
        ytrue = sqrt(pi)/2*exp(-tv**2)
        delta = sqrt(h)*norm(y-ytrue)
        print("Discrete L2 error is %20.15e for h = %20.15e") % (delta, h)