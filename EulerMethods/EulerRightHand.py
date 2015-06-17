from pylab import *

'''
Script for executing Euler's right hand method

Author: Amanda Robbins

First Working Version 01 DEC 2014
'''
def EulerRight(x,y0,h):
    
    y = zeros(shape(x))
    y[0] = y0
    n = x.size
    
    for j in xrange(n-1):
        c = y[j] + h * F(x[j],y[j])
        y[j+1] = y[j] + h* F(x[j]+h,c)
        x[j+1] =  x[j] + h
    
    return y
    
def F(x,y):
    return 2*y
    #return x*sin(y)
    #return x + y
    
x = linspace(0,0.7,10) #(starting x, stop value, array size)
y = EulerRight(x,3.0, 0.1) #(x, starting y, h) 
print y

'''
#Originally:
#First Working Version 24 NOV 2014


def EulerRight(v,x,y,h):
#where v = aproimation of y(v)
#x and y = original cordinates
#h = step value

    a = x
    b = y
    
    while a<v:
        b = b + h*F(a+h,b+h*F(a,b))
        a = a + h 
        
    return b   
    
def F(x,y):
    #return 2*y
    #return x*sin(y)
    return x + y
    
v0 = 0.7
x0 = 0.0
y0 = 3.0
h0 = 0.1
ans = EulerRight(v0, x0, y0, h0)
print ans
 


#Another way for executing Euler's right hand method:
#First Working Version 01 DEC 2014


def EulerRight(v,x,y,h):
#where v = aproimation of y(v)
#x and y = original cordinates
#h = step value

    a = x
    b = y
   
    
    while a<v:
        #Predictor-corrector with Euler's Method
        c = b + h*F(a,b)
        b = b + h*F(a+h,c)
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
ans = EulerRight(v0, x0, y0, h0)
print ans   
'''