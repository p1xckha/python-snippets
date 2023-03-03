# -*- coding: utf-8 -*-
"""
unexpected behaviors of lists
"""

def are_all_elements_same(list_of_lists: list[list[int]]) -> bool:
    for i in range(1, len(list_of_lists)):
        if list_of_lists[i-1] is not list_of_lists[i]:
            return False
    return True

def print_message(list_of_lists: list[list[int]]) -> None:
    """
    Prints a message indicating whether all the lists in the lists are the same object or not.
    If they are the same object, also prints their IDs.
    """
    if are_all_elements_same(list_of_lists):
        print("list_of_lists:", list_of_lists)
        print("All lists reference the same object")
        list_ids = [id(lst) for lst in list_of_lists]
        print("List IDs:", list_ids)
    else:
        print("list_of_lists:", list_of_lists)
        print("Lists do not all reference the same object")
        list_ids = [id(lst) for lst in list_of_lists]
        print("List IDs:", list_ids)
    print("")

    
def print_message(list_of_lists:list[list[int]]) -> None:
    if are_all_elements_same(list_of_lists):
        print("list_of_lists:", list_of_lists)
        print("All lists reference to the same object")
        list_ids = [id(lst) for lst in list_of_lists]
        print("List IDs:", list_ids)
        print("")
    else:
        print("list_of_lists:", list_of_lists)
        print("Lists do not reference to the same object")
        list_ids = [id(lst) for lst in list_of_lists]
        print("List IDs:", list_ids)
        print("")
    
lst = [2, 4, 6, 8]

# creates a new list  with 3 references to the same list b.
list_of_lists = [lst] * 3 # same as [b, b, b] 
print_message(list_of_lists)
list_of_lists[0][0] = -10
print("list_of_lists[0][0] = -10")
print("list_of_lists: ", list_of_lists)
print("")

# another unexpected behavior of lists
list_of_lists = [lst.copy()] * 3
print_message(list_of_lists)

# use list comprehension to avoid such unexpected behaviors of lists 
print("list_of_lists is created by list comprehension:")
list_of_lists = [[0,0,0] for _ in range(3)] 
print_message(list_of_lists)

list_of_lists[0][0] = 1
print("list_of_lists[0][0] = 1")
print("list_of_lists:", list_of_lists) 




