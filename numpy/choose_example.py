# -*- coding: utf-8 -*-
import numpy as np
import pprint 

def choose_example(index_array, choices):
    print("index_array:")
    pprint.pprint(index_array)
    print("")
    
    print("choices:")
    pprint.pprint(choices)
    print("")
    
    print("choose(a,choices):")
    pprint.pprint(np.choose(index_array,choices))
    print("")

index_array = [0,0,0,1] # array index(=first axis) I'm going to choose
choices = ["win", "draw", "lose"]
choose_example(index_array, choices)
    
matrix = lambda m, n: [[i*10+j for j in range(1, n+1)] for i in range(1, m+1)]
choices = matrix(7,3)
a = [1,3, 0] # row(=first axis) numbers of choices I'm going to choose
choose_example(a, choices) # choices[a[0]][0], choices[a[1]][1],...

array3d = lambda m, n, l: [[[100*i+10*j+k for k in range(1,l+1)] for j in range(1, n+1)] for i in range(1, m+1)]
choices = np.array(array3d(5, 3, 4))
index_array = np.array([0, 2, 1, 3]) # row(=first axis) numbers of choices I'm going to choose
choose_example(index_array, choices) 

# same result as above 
b = choices[0][:,0].reshape(-1,1)
arr = np.hstack((b, choices[2][:,1].reshape(-1,1)))
arr = np.hstack((arr, choices[1][:,2].reshape(-1,1)))
arr = np.hstack((arr, choices[3][:,3].reshape(-1,1)))
print(arr)
