from pylab import *

'''
Script for executing Taylor Polynomials T4(x)

Author: Amanda Robbins

First Working Version 5 NOV 2014
'''

# Tn(x) = f(a) + f'(a)*(x-a) + f''(a)/2! * (x-a)**2 + f'''(a)/3! * (x-a)**3 + f^(4)(a)/4! * (x-a)**4 + .... +f^(n)(a)/n! * (x-a)**n
def Taylor4(a,x):
    
    #Define bases
    t = f(a)
    t1 = f1(a)
    t2 = f2(a)
    t3 = f3(a)
    t4 = f4(a)
    
    answer = t + t1*(x-a) + t2/2*(x-a)**2 + t3/6*(x-a)**3+ t4/24*(x-a)**4
    
    return answer
    
def f(x):
    #return sin(x)
    #return e^(x)
    return (1+x)**-1
    #return x**4-2*x
    #return x**(11/2.0)
    #return cos(3*x)
def f1(x):
    #return cos(x)
    #return e^(x)
    return -1*(1+x)**-2
    #return 4*x**3-2
    #return (11/2.0)*x**(9/2.0)
    #return -3*sin(3*x)
def f2(x):
    #return -sin(x)
    #return e^(x)
    return 2*(1+x)**-3
    #return 12*x**2
    #return (99/4.0)*x**(7/2.0)
    #return -9*cos(3*x)
def f3(x):
    #return -cos(x)
    #return e^(x)
    return -6*(1+x)**-4
    #return 24*x
    #return (693/8.0)*x**(5/2.0)
    #return 27*sin(3*x)
def f4(x):
    #return sin(x)
    #return e^(x)
    return 24*(1+x)**-5
    #return 24
    #return (3465/16.0)*x**(3/2.0)
    #return 81*cos(3*x)

a0 = 2 # Expansion point
#x0 = 3 # Evaluation point(s)
x0 = linspace(1,5)
ans = Taylor4(a0, x0)
plot(x0,ans,'b',x0,f(x0),'r--')
xlabel('$x$')
ylabel('$f(x)$, $p_n(x)$')
legend(['$p_n(x)$','$f(x)$'])
show()
#print str(ans)