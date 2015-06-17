from pylab import *

'''
Script for executing the trapezoidal rule

Author: K.J. Wojciechowski (KJW)
First Working Version 7 OCT 2014
'''

def numint_trapz(x):
    # Compute grid-spacing
    h = (x[-1] - x[0])/(x.size - 1)
    # Define trapezoid bases (function heights)
    y = f(x)
    # Execute trapezoid rule
    s = 0.5*(y[0] + y[-1])
    for k in xrange(1,x.size-1):
        s += y[k]
    return s*h
    
def f(x):
    #return 2*x
    #return sin(pi*x)/(pi*x)
    return (2/sqrt(pi))*exp(-x**2)
    #return sin(0.5*pi*x**2)
    #return sin(x**2)
    #return (1/sqrt(2*pi))*exp(-0.5*x**2)
    
# Construct evenly spaced grid
eps = spacing(1) # float zero
'''
auct = []
for n in range(3,51):
    x = linspace(-2,2,n)
    # Call the midpoint rule FUNCTION
    auct.append(numint_trapz(x))
'''
x = linspace(0,1.5,21)
auct = numint_trapz(x)
print 'Trapezoidal Rule AUC ~ ' + str(auct)