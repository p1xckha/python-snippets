# -*- coding: utf-8 -*-
"""
unexpected behaviors of lists
"""

a = [2, 4, 6, 8]

# creates a new list with 3 references to the same list a.
b = [a] * 3 # same as [a, a, a] 
print("b:", b)
print("")

a[1] = 44 
print("all second elements in lists in b are changed")
print("b:", b) 
print("")

b[0][0] = 20
print("all first elements in lists in b are changed unexpectedly")
print("b:", b) 
print("")

# another unexpected behavior of lists
b = [a.copy()] * 3
b[1][2] = 88
print("all 3rd elements in lists in b are changed unexpectedly")
print("b:", b)
print("")

# use list comprehension to avoid such unexpected behaviors of lists 
print("b is created by list comprehension")
b = [[0,0,0].copy() for _ in range(3)] 
print("b:", b)
print("")

b[0][0] = 1
print("the first element in the first list in b is changed.")
print("b:", b)




