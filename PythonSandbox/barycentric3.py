import numpy as np
from pylab import *

def weight(x):
    w = zeros((len(x),len(x)))
    w[0][0] = 1
    for j in range(1,len(x)):
        for k in range(0,j):
            w[j][k] = (x[k]-x[j])*w[j-1][k]
            #print 'w['+ str(j)+ ']['+ str(k) + ' ] = ' + str(w[j][k])
        
        w[j][j] = np.product(np.subtract(x[j], x[0:j-1]))
        #print 'w['+ str(j)+ ']['+ str(j) + ' ] = ' + str(w[j][j])
    for j in range(0,len(x)):
        w[len(x)-1,j] = 1/w[len(x)-1,j]
    return w[len(x)-1]

def Barycentric(x,y,xi):
    w = weight(x)
    yi = zeros(len(xi))
    
    for k in range(0,len(xi)):
        yi[k] = np.sum(np.multiply(np.divide(w,np.subtract(xi[k],x)),y))/np.sum(np.divide(w,np.subtract(xi[k],x)))
    
    return yi


#Create Points to interpolate
x = linspace(-1,1,7)
y = x**2

#Now use Barycentric formula to find yi's
xi = linspace(-1,1,101)
yi = Barycentric(x,y,xi)


#Plot the results

figure(2)
plot(x,y,'ro',xi,yi,'b')
show()

#Testing
#x = [0,1,2]
#w = weight(x)
#print w