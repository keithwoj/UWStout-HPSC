# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:55:00 2015

@author: Keith J. Wojciechowski (KJW)
"""

from pylab import *

font = {'family' : 'serif',
        'weight' : 'normal',
        'size' : 16}

# Interval width, h = (b-a)/(n-1), given this grid spacing:
# x[0] = -4, x[100] = -3, x[200] = -2, ..., x[700] = 3, x[800] = 4
n = 601
x = linspace(-3,3,n)

# Normalized standard normal
f = exp(-0.5*(x/(1./4.))**2)

figure()
plot(x,f,linewidth=2)
#xticks([0],['$\mu$'])
yticks([])
axis([-3, 3, -0.1, 1.1])
title('Normal Distribution',fontdict = font)