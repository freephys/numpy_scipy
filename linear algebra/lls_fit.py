#!/usr/bin/env python
"""
xi, zi are experimental data
The functions to fit is : c1*exp(-x)+c2*x
it has two coefficient to fit
"""
from numpy import *
from scipy import linalg
import matplotlib.pyplot as plt

c1,c2= 5.0,2.0
i = r_[1:11]
xi = 0.1*i
yi = c1*exp(-xi)+c2*xi
zi = yi + 0.05*max(yi)*random.randn(len(yi))
print zi
"""
c_[exp(-x),x]
"""
A = c_[exp(-xi)[:,newaxis],xi[:,newaxis]]

print exp(-xi)[:,newaxis]
print exp(-xi)
print xi[:,newaxis]
print A
c,resid,rank,sigma = linalg.lstsq(A,zi)
print c,resid,sigma
xi2 = r_[0.1:1.0:100j]
yi2 = c[0]*exp(-xi2) + c[1]*xi2

plt.plot(xi,zi,'x',xi2,yi2,'*')
plt.axis([0,1.1,3.0,5.5])
plt.xlabel('$x_i$')
plt.title('Data fitting with linalg.lstsq')
plt.show()

