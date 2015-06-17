from pylab import *
from scipy.integrate import odeint

'''
Script for executing Euler's Method

Author: Amanda Robbins

First Working Version 15 NOV 2014
Modified to work with odeint (KJW) 26 FEB 2015
'''

# y(k) = y(k-1) + h*F(x(k-1), y(k-1))

def Euler(y0,x):
    
    y = zeros(shape(x))
    y[0] = y0
    n = x.size
    h = max(abs(diff(x)))
    
    for j in xrange(n-1):
        y[j+1] = y[j] + h * F(y[j],x[j])
        x[j+1] =  x[j] + h
    
    return y
    
def F(y,x):
    return 2*y
    #return x*sin(y)
    #return x + y
    

y0 = 1.0
x = linspace(0,0.7,20)

#y = Euler(y0, x)

y = odeint(F, y0, x)
#print y

plot(x,y0*exp(2*x),'r',x,y,'b')
show()


''' 
#Originally:
     
from pylab import *

def Euler(v,x,y,h):
#where v = aproimation of y(v)
#x and y = original cordinates
#h = step value

    a = x
    b = y
    
    while a<v:
        b = b + h*F(a,b)
        a = a + h 
        
    return b   
    
def F(x,y):
    return 2*y
    #return x*sin(y)
    #return x + y
    
v0 = 0.7
x0 = 0.0
y0 = 3.0
h0 = 0.1
ans = Euler(v0, x0, y0, h0)
print ans   
'''