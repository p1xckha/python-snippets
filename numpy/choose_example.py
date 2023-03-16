# -*- coding: utf-8 -*-
import numpy as np
import pprint 

def choose_example(a, choices):
    print("a:")
    pprint.pprint(a)
    print("")
    
    print("choices:")
    pprint.pprint(choices)
    print("")
    
    print("choose(a,choices):")
    pprint.pprint(np.choose(a,choices))
    print("")

a = [0,0,0,1]
choices = ["win", "draw", "lose"]
choose_example(a, choices)
    
matrix = lambda m, n: [[i*10+j for j in range(1, n+1)] for i in range(1, m+1)]
choices = matrix(7,3)
a = [1,3, 0] # row numbers of choices I'm going to choose
choose_example(a, choices)

