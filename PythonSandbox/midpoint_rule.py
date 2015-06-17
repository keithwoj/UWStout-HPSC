from pylab import *

'''
Script for executing the midpoint rule

Author: K.J. Wojciechowski (KJW)
First Working Version 7 OCT 2014
'''

def numint_midpoint(x):
    # Determine evaluation nodes
    c = (x[1::] + x[0:-1])/2.
    # Compute grid-spacing
    h = (x[-1] - x[0])/(x.size - 1)
    # Define trapezoid bases (function heights) 
    y = f(c)
    # Execute trapezoid rule
    s = 0
    for k in xrange(c.size):
        s += y[k]
    return s*h
    
def f(x):
    #return 2*x
    #return sin(pi*x)/(pi*x)
    #return (2/sqrt(pi))*exp(-x**2)
    #return sin(0.5*pi*x**2)
    return (1/sqrt(2*pi))*exp(-0.5*x**2)
    
# Construct evenly spaced grid
eps = spacing(1) # float zero

aucm = []
for n in range(3,101):
    x = linspace(-1,1,n)
    # Call the midpoint rule FUNCTION
    aucm.append(numint_midpoint(x))
#print 'Midpoint Rule AUC ~ ' + str(aucm)
'''
figure(1)
plot(x,f(x),'bo-')
# Using LaTeX mathematical scripting language to label axes
xlabel('$x$')
ylabel('$f(x) = \sin(\pi x^2/2)$')
show()
'''