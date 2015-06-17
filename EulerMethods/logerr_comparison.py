from pylab import *

def EulerMidpoint(x0,xf,y0,h):
    
    x = linspace(x0,xf,(xf-x0)/float(h)+1)
    y = zeros(shape(x))
    y[0] = y0
    n = x.size
    
    for j in xrange(n-1):
        c = y[j] + (h/2.0)*F(x[j], y[j])
        y[j+1] = y[j] + h * F(x[j] + h/2.0, c)
    
    return x,y
    
# Insert an ODE solve here for comparison
    
def F(x,y):
    return 2*y

x0 = 0.0
xf = 1.0
y0 = 3.0

hv = array([0.01, 0.1, 0.2, 0.3])
relerr = zeros(len(hv))
n = 0

for h in hv:
    [x,ym] = EulerMidpoint(x0,xf,y0, h)
    yx = 3*exp(2*x)
    relerr[n] = norm(ym-yx)/norm(yx) # relative error
    n += 1
    
semilogy(hv,relerr,'ro-')
xlabel('$h$')
ylabel('log(rel err)')
# grid
show()
