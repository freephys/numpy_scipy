#!/usr/bin/env python
"""
x, y are experimental points
Fit a line y = c1*x +c2*1 through some noisy points
"""
from numpy import *
from scipy import linalg
from matplotlib.pyplot import *

x = array([0,1,2,3])
y = array([-1, 0.2, 0.9, 2.1])
"""
c_[x,1]
"""
A = c_[x[:,newaxis],ones(len(x))]
print A
A1 = vstack([x, ones(len(x))]).T
print A1

c,resid,rank,sigma = linalg.lstsq(A,y)
print c,resid,sigma

m,c,r,s = linalg.lstsq(A1,y)
print m,c,s

plot(x, y, 'o', label='Original data', markersize=5)
plot(x, m*x + c, 'r', label='Fitted line')
legend()
show()