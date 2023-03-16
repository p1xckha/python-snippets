# -*- coding: utf-8 -*-
"""
@author:  p1xckha

create a matrix Aij = 10*i + j with lambda and list comprehension.

input: print(matrix(4,3))
output: [[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]]

"""

matrix = lambda m, n: [[i*10+j for j in range(1, n+1)] for i in range(1, m+1)]
array3d = lambda m, n, l: [[[100*i+10*j+k for k in range(1,l+1)] for j in range(1, n+1)] for i in range(1, m+1)]

a = matrix(4, 3)
print("4 rows 3 columns matrix aij= 10*i + j as follow:\n", a)

print("3d array:", array3d(3,4,5))


# import numpy as np
# a = np.array(matrix(4,4))
# print("matrix aij= 10*i + j as follow:\n", a)
# print(a.shape)



