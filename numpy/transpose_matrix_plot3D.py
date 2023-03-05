# -*- coding: utf-8 -*-
'''
create 3D visualizations of all the transposed matrices of A.
It's like a rubik's cube
'''
import matplotlib.pyplot as plt
import numpy as np
from itertools import permutations

# generate 3D plot for matrix A 
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
    
    mycolors=('yellow', 'orange', 'red', 'purple')
    
    # Add labels to points
    for x, y, z, label in zip(X, Y, Z, labels):
        ax.text(x, y, z, label, color=mycolors[int(label/100)])
    
    # Set axis labels
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title(title)

# Define matrix A
matrix = lambda m, n, l: [[[i*100+j*10+k for k in range(1, l+1)] for j in range(1, n+1)] for i in range(1, m+1)] 
A = matrix(2, 3, 4)
A = np.array(A)

fig, axe = plt.subplots(2,3,  subplot_kw={'projection': '3d'}, figsize=(12, 8))
perms = permutations(range(3), 3)

for i, (i1, i2, i3) in enumerate(perms):
    j = i % 3
    i = int(i/3)
    title = "transpose(%d,%d,%d)" % (i1, i2, i3)
    plot_matrix(A.transpose(i1, i2, i3), axe[i, j], title)

plt.show()
fig.savefig('np_transpose_plot3D.svg')





