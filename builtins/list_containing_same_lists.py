# -*- coding: utf-8 -*-
"""
unexpected list's behaviors 
"""

a = [2, 4, 6, 8]

# creates a new list with 3 references to the same list a.
b = [a] * 3 # same as [a, a, a] 
print("b:", b)
print("")

a[1] = 44 
print("all second elements in b are changed")
print("b:", b) 
print("")

b[0][0] = 20
print("all first elements in b are changed unexpectedly")
print("b:", b) # all second elements in b are changed 
print("")

# another unexpected list's behavior
b = [a.copy()] * 3
b[1][2] = 88
print("all 3rd elements in b are changed unexpectedly")
print("b:", b)
print("")

# use list comprehension to avoid such unexpected list's behaviors 
print("b is created by list comprehension")
b = [[0,0,0].copy() for _ in range(3)] 
print("b:", b)
print("")

b[0][0] = 1
print("the first element in the first list in b is changed.")
print("b:", b)




