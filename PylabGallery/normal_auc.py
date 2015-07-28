# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:32:00 2015

@author: Keith J. Wojciechowski (KJW)
"""

from pylab import *

font = {'family' : 'serif',
        'weight' : 'normal',
        'size' : 16}

# Interval width, h = (b-a)/(n-1), given this grid spacing:
# x[0] = -4, x[100] = -3, x[200] = -2, ..., x[700] = 3, x[800] = 4
n = 801
x = linspace(-4,4,n)

# Normalized standard normal
f = exp(-0.5*x**2)
# Filled area function will be zero everywhere except indexed values indicated
# below, e.g. xindx = range(400,500) will fill an area betwenn 0 and 1
fp = zeros(f.size)
xindx = range(400,550)
fp[xindx] = f[xindx]

figure()
plt = plot(x,f) + fill(x,fp,'r')
title('Normal Distribution',fontdict = font)
## *** Set mu, sigma, 2sigma at x = 0, 1, 2
#xticks([0, 1, 2],['$\mu$','$\sigma$','$2\sigma$'])
## *** Set 0, x at x = 0, 1.5 so that the Erf graphic indicates the AUC for some
## *** unknown value of x
#xticks([0,1.5],['$0$','$x$'])
yticks([])