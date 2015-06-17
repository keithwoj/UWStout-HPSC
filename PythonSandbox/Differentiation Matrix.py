from pylab import *
from numpy import *
from scipy.sparse import *

def f(x):
    return sin(pi*x)
    #return e**(2*x)
    #return e**(sin(2*x))
    
def firstDer(x):
    return pi*cos(pi*x)
    #return 2*e**(2*x)
    #return pi*cos(pi*x)*e**(sin(pi*x))
    
def secondDer(x):
    return -pi*pi*sin(pi*x)
    #return 4*e**(2*x)
    #return pi*pi*e**sin(pi*x)*(cos**2(pi*x)-sin(pi*x))
    
#num of elements
n = 8
#spacing between elements
h = 0.25

'''
#matrix for first der
stencil = array([0,-1,1])
offsets = array([-1,0,1])
k = diags(stencil, offsets, shape=(n,n)).toarray()
'''

'''
#matrix for first der
stencil = array([-1/2., 0., 1/2.])
offsets = array([-1,0,1])

k = diags(stencil, offsets, shape=(n,n)).toarray()
k[0][0] = -1
k[0][1] = 1

k[n-1][n-2] = -1
k[n-1][n-1] = 1
'''

#matrix for second der
stencil = array([1,-2,1])
offsets = array([-1,0,1])
k = diags(stencil, offsets, shape=(n,n)).toarray()

k[0][0] = 2
k[0][1] = -5
k[0][2] = 4
k[0][3] = -1

k[n-1][n-4] = 2
k[n-1][n-3] = -5
k[n-1][n-2] = 4
k[n-1][n-1] = -1

a = 0
b = (n-1)*h
x = linspace(a,b,n)
y = f(x)

#matrix multiplication foe first der
#yk = dot(k,y)/h

#matrix multiplication foe second der
yk = dot(k,y)/(h**2)

#graph for first der
#plot(x,yk,'ro-', x,firstDer(x),'b')
#show()

#graph for second der
plot(x,yk,'ro-', x,secondDer(x),'b')
show()