from numpy import *

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


#Create Points to interpolate
x = linspace(-1,1,9)