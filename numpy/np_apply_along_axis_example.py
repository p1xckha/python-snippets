# -*- coding: utf-8 -*-
from typing import Sequence
import numpy as np

# Define a function that operates on 1D arrays
def transform(x: Sequence)-> np.array:
    assert len(x) == 2, "length of x must be 2"
    return np.array([x[0], x[0]*x[1], x[1]])

# Create a 2D array
x = np.array([[0, 1], [2, 3], [4, 5]])

# Apply the transform function to each row of the array
x_transformed = np.apply_along_axis(transform, axis=1, arr=x)
print(x_transformed)  
