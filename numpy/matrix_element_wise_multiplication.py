# -*- coding: utf-8 -*-

import numpy as np


def element_wise_matrix_multiplication():
    # create two matrices A and B using np.matrix
    A = np.matrix([[1,2], [0,4]]) # 2x2 matrix
    B = np.matrix([[0,1], [3,2]]) # 2x2 matrix
    print(f"matrix A:\n{A}")
    print(f"matrix B:\n{B}")
    print("")
    
    C = np.multiply(A,B)
    print(f"element-wise multiplication between A and B :\n{C}")
    print("*"*30)
 
def unexpected_behavior_of_matrix():
    a = [[1,1]]
    b = [[1],[1]]
    c = [[0],[1]]
    
    A = np.matrix(a) # 1x2 matrix
    B = np.matrix(b) # 2x1 matrix
    C = np.matrix(c) # 2x1 matrix
    
    D = A @ B # 1x1 matrix[[2]], not a number
    
    try:
        print(D*C)
    except:
        print("Error: D*C")
        print(f"matrix D:{type(D)}\n{D}")
        print(f"matrix C:{type(C)}\n{C}")
        print("")
    

    # instead, use item() or np.multiply() 
    print("D.item() * C:\n", D.item()*C)
    print("")
    print(np.multiply(D,C)) 
    print("*"*30)

def matrix_multiplication():
    A = np.matrix([[1,2], [0,4]]) # 2x2 matrix
    B = np.matrix([[0,1], [3,2]]) # 2x2 matrix
    print(f"matrix A:\n{A}")
    print(f"matrix B:\n{B}")
    C=A*B
    print(f"A*B:\n{C}")
    print("")
    print("*"*30)
    
def expected_behavior_of_array():
    a = [[1,1]]
    b = [[1],[1]]
    c = [[0],[1]]
    
    A = np.array(a) # 1x2 matrix
    B = np.array(b) # 2x1 matrix
    C = np.array(c) # 2x1 matrix
    D = A @ B # 2d array [[2]], not a number
    
    E = D * C
    print(f"numpy array D:\n{D}")
    print(f"numpy array C:\n{C}")
    print("")
    print(f"element wise multiplication E=D*C:\n{E}")



element_wise_matrix_multiplication()
unexpected_behavior_of_matrix()
matrix_multiplication()
expected_behavior_of_array()

