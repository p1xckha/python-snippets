# -*- coding: utf-8 -*-
"""
unexpected behaviors of lists
"""

def are_all_elements_same(a:list[list[int]]) -> bool:
    for i in range(1, len(a)):
        if a[i-1] is not a[i]:
            return False
    return True

def print_message(a:list[list[int]]) -> None:
    if are_all_elements_same(a):
        print(a)
        print("each list references to the same object")
        ids_str = [id(a[i]) for i in range(len(a))]
        print("IDs:", ids_str)
        print("")
    else:
        print(a)
        print("each list does not references to the same object")
        ids_str = [id(a[i]) for i in range(len(a))]
        print("IDs:", ids_str)
    
b = [2, 4, 6, 8]

# creates a new list with 3 references to the same list a.
a = [b] * 3 # same as [b, b, b] 
print_message(a)
a[0][0] = -10
print("a[0][0] = -10")
print("a: ", a)
print("")

# another unexpected behavior of lists
a = [b.copy()] * 3
print_message(a)

# use list comprehension to avoid such unexpected behaviors of lists 
print("a is created by list comprehension")
a = [[0,0,0] for _ in range(3)] 
print_message(a)
print("")

a[0][0] = 1
print("a[0][0] = 1")
print("a:", a) 




