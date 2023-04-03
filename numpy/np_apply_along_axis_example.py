# -*- coding: utf-8 -*-

import numpy as np

# Define a function that operates on 1D arrays
def transform(x):
    assert len(x) == 2, "length of x must be 2"
    return np.array([x[0]**2, np.sqrt(2)*x[0]*x[1], x[1]**2])

# Create a 2D array
arr = np.array([[1, 2], [4, 5], [7, 8]])

# Apply the transform function to each row of the array
x_transformed = np.apply_along_axis(transform, axis=1, arr=arr)
print(x_transformed)  

