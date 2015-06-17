from pylab import *

'''
Script for executing Euler's Midpoint Method

Author: Amanda Robbins

First Working Version 24 NOV 2014
'''

'''def EulerMidpoint(v,x,y,h):
#where v = aproimation of y(v)
#x and y = original cordinates
#h = step value

    a = x
    b = y
    
    while a<v:
        b = b + h*F(a+ h/2.0,b + (h/2.0)*F(a,b))
        a = a + h 
        
    return b   
    
def F(x,y):
    #return 2*y
    #return x*sin(y)
    return x + y
    #return cos(x + y)
    
v0 = 0.5
x0 = 0.0
y0 = 1.0
h0 = 0.1
ans = EulerMidpoint(v0, x0, y0, h0)
print ans'''

   

def EulerMidpoint(x,y0,h):
    
    y = zeros(shape(x))
    y[0] = y0
    n = x.size
    
    for j in xrange(n-1):
        c = y[j] + (h/2.0)*F(x[j], y[j])
        y[j+1] = y[j] + h * F(x[j] + h/2.0, c)
        x[j+1] =  x[j] + h
    
    return y
    
def F(x,y):
    return 2*y
    #return x*sin(y)
    #return x + y
    #return cos(x + y)
    
x = linspace(0,0.7,10)
y = EulerMidpoint(x,3.0, 0.1)
yx = 3*exp(2*x)
#yx = 2*exp(x)-(1+x)  # exact solution
# norm(x) = sqrt(x0^2 + x1^2 + ... + xn^2)
print norm(y-yx)/norm(yx) # relative error
plot(x,y,'r',x,yx,'b')
#plot(x,abs(y-yx),'r')
show()
