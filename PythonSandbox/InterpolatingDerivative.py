import numpy as np
from pylab import *

def weight(x):
    w = zeros((len(x),len(x)))
    w[0][0] = 1
    for j in range(1,len(x)):
        for k in range(0,j):
            w[j][k] = (x[k]-x[j])*w[j-1][k]
            #print 'w['+ str(j)+ ']['+ str(k) + ' ] = ' + str(w[j][k])
        
        w[j][j] = np.product(np.add(x[j],np.multiply(-1,x[0:j])))
        #print 'w['+ str(j)+ ']['+ str(j) + ' ] = ' + str(w[j][j])
    for j in range(0,len(x)):        
        w[len(x)-1,j] = 1/w[len(x)-1,j]       
    return w[len(x)-1]

def InterDeriv(x,y,xi):
    w = weight(x)
    
    yi = zeros(len(xi))
    
    for k in range(0,len(xi)):
        yi[k] = np.sum(np.divide(y,np.subtract(xi[k],x)))*np.sum(np.divide(w,np.subtract(xi[k],x)))
    
    return yi


#Create Points to interpolate
x = linspace(-1,1,10)
y = x**2
#y = 1/((5*x)**2+1)  
#y = sin(pi*x)

#Now use Interpolating Derivative formula to find yi's
xi = linspace(-1,1,10)
yi = InterDeriv(x,y,xi)


#Plot the results

figure(2)
plot(x,y,'ro:',xi,yi,'b')
show()

#Testing
#x = [0,1,2]
#w = weight(x)
#print w