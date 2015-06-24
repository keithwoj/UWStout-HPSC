from pylab import *

def weight(x):
    n = len(x)
    w = eye(n)
    w[0,0] = 1
    ww = 0*x
    
    for j in xrange(1,n):
        for k in xrange(j):
            w[j,k] = (x[k]-x[j])*w[j-1,k]
            print "w["+str(j)+","+str(k)+"] = (x["+str(k)+"]-x["+str(j)+"])*w["+str(j-1)+","+str(k)+"]"
        #end k
        w[j,j] = product(x[j] - x[0:j-1])
        print "w["+str(j)+","+str(j)+"] = product(x["+str(j)+"] - x[0:"+str(j-1)+"])"
    #end j
    for j in xrange(n):
        ww[j] = 1/w[-1,j]
    return ww

def myinterp(x,y,xi):
    nx = len(x)
    nxi = len(xi)
    s = ones(nx)
    w = weight(x)
    yi = zeros(nxi)
    
    for k in xrange(nxi):
        fv = w/(xi[k]-x)
        yi[k] = sum(y*fv)/sum(fv)

    return yi
    
def test():
    #Create Points to interpolate
    x = linspace(0,1,9)
    y = sin(pi*x)

    xi = linspace(0.01,0.99,12)
    yi = myinterp(x,y,xi)
    err = sqrt(max(abs(diff(xi))))*norm(sin(pi*xi)-yi)
    print err
    show(plot(x,y,'bo',xi,yi,'r',xi,sin(pi*xi),'g--'))