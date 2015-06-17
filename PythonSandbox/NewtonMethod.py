from pylab import *

'''
Script for executing Newton's Method

Author: Amanda Robbins
First Working Version 24 OCT 2014
'''

def newton(x):
    # Define bases
    y = float(f(x))
    z = float(g(x))
    
    # Execute Newton's method
    
    #Starting point x sub 0
    nits = 1
    #n = -1
    #rounding to eight point accuracy
    while round(x-y/z,8) != round(x,8):
#    for n in xrange(10):
        y = float(f(x))
        z = float(g(x))
        x = x-y/z
        nits += 1
    
    return x, nits
    
def f(x):
    return x**2+3*x-4
    #return sin(x)
    #x**7-1000
    
#Derivatives corresponding to functions above in f(x)
def g(x):
    return 2*x+3
    #return cos(x)
    #7*x**6
    
x0 = 5
[root, nits] = newton(x0)
print str(root) + ' after ' + str(nits) + ' iterations.'
