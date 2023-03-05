# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from itertools import permutations

# Define matrix A
matrix = lambda m, n, l: [[[i*100+j*10+k for k in range(1, l+1)] for j in range(1, n+1)] for i in range(1, m+1)] 
A = matrix(2, 3, 4)
A = np.array(A)


def plot_matrix(A, ax, title=None):
    # Flatten A and add labels
    X = []
    Y = []
    Z = []
    labels = []
    for i, row in enumerate(A):
        for j, col in enumerate(row):
            for k, val in enumerate(col):
                X.append(i)
                Y.append(j)
                Z.append(k)
                labels.append(val)
    
    # Create 3D scatter plot with labels
    ax.scatter(X, Y, Z)
    
    # Add labels to points
    for x, y, z, label in zip(X, Y, Z, labels):
        ax.text(x, y, z, label, color='red')
    
    # Set axis labels
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title(title)
    # Show plot
    

fig, axe = plt.subplots(2,3,  subplot_kw={'projection': '3d'}, figsize=(12, 8))

perms = permutations(range(3), 3)

for i, (i1, i2, i3) in enumerate(perms):
    j = i % 3
    i = int(i/3)
    title = "transpose(%d,%d,%d)" % (i1, i2, i3)
    plot_matrix(A.transpose(i1, i2, i3), axe[i, j], title)

plt.show()
fig.savefig('np_transpose_plotted3D.svg')





