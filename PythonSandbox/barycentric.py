import numpy as np
from pylab import *

def weight(x):
    w = zeros((len(x), len(x)))
    w[0][0] = 1
    for j in range(1, len(x)):
                
        for k in range (0, j): 
            w[j][k] = (x[k] - x[j]) * w[j-1][k]
            
        w[j][j] = np.product(np.subtract(x[j], x[0:j-1]))
        
    for j in range(0,len(x)):
        w[len(x)-1,j] = 1/w[len(x)-1,j]
    
    return w[len(x)-1]
    
#def Barycentric(x,xi):
#    w = weight(x)
#    yi = zeros(len(x)) 
#    for j in range(0,len(xi)):
#        yi[j] = np.sum(np.multiply(np.divide(w,np.subtract(xi[j],x)),f(x)))/np.sum(np.divide(w,np.subtract(xi[j],x)))
    
#    return yi

def f(x):
    return x*2

#Create Points to interpolate
x = [0,1,2]
xi = [-1,0,1]
w = weight(x)
print w

#figure(1)
#plot(x,y,'ro')
#xlabel('x')
#ylabel('y')
#title('Before Interpolation')
#show()

#Now use Barycentric formula to find xi's
#xi = linspace(-1,1,101)
#yi = Barycentric(x,y,xi)


#Plot the results

#figure(2)
#plot(x,y,'ro',xi,yi,'b')
#show()
