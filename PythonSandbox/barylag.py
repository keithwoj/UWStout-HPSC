# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:04:46 2015

@author: Keith J. Wojciechowski (KJW)
"""

from pylab import *

def weight(x):
    n = len(x)
    X = outer(x,ones(n))
    dX = X.T - X + eye(n)
    
    return 1/prod(dX,axis=0)
    
def interp(x,y,xi):
    nx = len(x)
    nxi = len(xi)
    w = weight(x)
    yi = zeros(nxi)
    
    for k in xrange(nxi):
        fv = w/(xi[k]-x)
        yi[k] = sum(y*fv)/sum(fv)

    return yi

def testf(x):
    return 1/(1+(5*x)**2)

def test():
    #Create Points to interpolate
    #x = linspace(-1,1,9)
    n = 31
    x = cos(pi*linspace(0,n,n)/n)
    y = testf(x)

    ni = 96
    xi = linspace(-1+1./n**2,1-1./n**2,ni)
    yi = interp(x,y,xi)
    ytrue = testf(xi)
    err = norm((ytrue[1:]-yi[1:])*abs(diff(xi)))
    print("Discrete L2-norm = %20.15f") % err
    show(plot(x,y,'bo',xi,yi,'r',xi,ytrue,'g--'))