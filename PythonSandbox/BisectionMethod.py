from pylab import *

'''
Script for executing Bisection Method

Author: Amanda Robbins

First Working Version 2 NOV 2014
Second working Version 5 NOV 2014
'''

def bisect(a,b):
    # Define bases
    fa = float(f(a))
    fb = float(f(b))
    
    #Execute Bisection method

    nits = 0
    maxints= 50

    while abs(b-a) >= 1e-8 and nits < maxints:
        fa = float(f(a))
        fb = float(f(b))
        nits +=1
    
        if sign(fa) * sign(fb) < 0:
            mid = (b-a)/2.0+a
            fm = float(f(mid))
            
            if sign(fb) * sign(fm) < 0:
                a = mid
            else:
                b = mid

        elif fa==0:
            b=a             
        elif fb==0:
            a=b 
        else:
            print 'Bisection Failed'
            break
            
    return a, b, nits
        
def f(x):
    #return x**3 + 6*x**2 + x -8
    #return x**2+3*x-4
    #return sin(x)
    #return x**7-1000
    return x**3-x-3
    
a0 = -2
b0 = 0
[start, end, nits] = bisect(a0,b0)
print 'Zero is between ' + str(start) + ' and ' + str(end) + ' after ' + str(nits) + ' iterations.' 