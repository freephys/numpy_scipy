#!/usr/bin/env python
"""
Singular Value Decomposition of matrix A

Factorizes the matrix A into two unitary matrices U and Vh 
and an 1d-array s of singular values (real, non-negative)
such that A == U S Vh
if S is an suitably shaped matrix of zeros
whose main diagonal is s
"""
from scipy import linalg,mat

A = mat('[1 5 2;2 4 1;3 6 2]')
M,N = A.shape
print A

U,s,vh = linalg.svd(A)
print U.shape,s.shape,vh.shape
print U
print s
sig = mat(linalg.diagsvd(s,M,N))
print sig
print U*sig*vh