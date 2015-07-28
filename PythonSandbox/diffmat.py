# -*- coding: utf-8 -*-
"""
Module for creating differentiation matrices
Created on Thu Jun 25 14:37:43 2015

@author: Keith J. Wojciechowski (KJW)

yi = INTERPOLATOR(x,y,xi)

Input:
        x -- data grid (nodes)
        y -- data to be interpolated
        xi -- interpolation grid
        
Output:
        yi -- interpolant
        
Notes:
        
Edits:
        24 JUN 2015:
        First working version barylag (KJW)
        Unit test added, f(x) = 1/(1+(5*x)**2) (KJW)
        
Interpolators:
        yi = barylag(x,y,xi)
        interp1.barylag?? to see the unit test and an example
"""
from pylab import *

def difflag(x):
    # Depends on interp1.weight(x) -- Barycentric interpolation weights    
    import interp1

    # Initialize the weights and differentiation matrix
    w = interp1.weight(x)
    n = len(x)
    D = zeros((n,n))
    for j in xrange(n):
        idx = where(arange(n)!=j)
        dx = x[j] - x[idx]
        D[j,idx] = w[idx]/(w[j]*dx)
        D[j,j] = -sum(D[j,idx])
    return D

def testf(x):
    u = exp(sin(pi*x))
    du = pi*cos(pi*x)*u
    
    return du, u

def test():
    n = 31
    x = cos(pi*linspace(0,n,n)/n)
    D = difflag(x)
    du_true, u = testf(x)
    du = dot(D,u)
    clf()
    show(plot(x,du,'r',x,du_true,'b.'))