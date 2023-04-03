# -*- coding: utf-8 -*-
import numpy as np


A = np.array([[1, 2],[-1,-1]])
x = np.array([2,4])

print(f"A:\n{A}")
print("")
print(f"x:\n{x}")
print("")
print(f"x.T:\n{x.T}") # same as x
print("")
print(f"x[:, np.newaxis]:\n{x[:, np.newaxis]}") # x is 2x1 array
print("")

print("multiply columns: A*x")
print(A * x) 
print("")

x = np.array([[2],[4]])
print(f"A:\n{A}")
print("")
print(f"x:\n{x}")
print("")
print("multiply rows: A*x")
print(A * x) 
print("")




