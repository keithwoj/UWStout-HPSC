from pylab import *

'''
Script for executing the right-hand rule

Author: K.J. Wojciechowski (KJW)
First Working Version 7 OCT 2014
'''

def numint_rhand(x):
    # Compute grid-spacing
    h = (x[-1] - x[0])/(x.size - 1)
    # Define rectangle (function) heights
    y = f(x)
    # Execute right-hand rule
    s = 0
    for k in xrange(1,x.size):
        s += y[k]
    return s*h
    
def f(x):
    return 2*x
    #return sin(pi*x)/(pi*x)
    #return (2/sqrt(pi))*exp(-x**2)
    #return sin(0.5*pi*x**2)

# Construct evenly spaced grid
eps = spacing(1) # float zero
x = linspace(eps,1,11)

# Call the right-hand rule FUNCTION
auc = numint_rhand(x)
print 'Right-hand Rule AUC ~ ' + str(auc)