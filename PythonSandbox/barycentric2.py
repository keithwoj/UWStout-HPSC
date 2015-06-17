import numpy as np
from pylab import *

def weight(x):
    w = zeros((len(x),len(x)))
    w[0][0] = 1
    for j in range(1,len(x)):
        for k in range(0,j-1):
            w[j][k] = (x[k]-x[j])*w[j-1][k]
        
        w[j][j] = np.product(x[j] - x[0:j-1])
    for j in range(0,len(x)):
        w[len(x),j] = 1/w[len(x),j]
    return w[len(x)]

def Barycentric(x,y,xi):
    yi = zeros(len(xi))
    
    
    #for i in range(0,len(xi)):
        
    
    return yi


#Create Points to interpolate
x = linspace(-1,1,7)
y = x**2

figure(1)
plot(x,y,'ro')
xlabel('x')
ylabel('y')
title('Before Interpolation')
show()

#Now use Barycentric formula to find xi's
xi = linspace(-1,1,101)
yi = Barycentric(x,y,xi)


#Plot the results

#figure(2)
#plot(x,y,'ro',xi,yi,'b')
#show()
