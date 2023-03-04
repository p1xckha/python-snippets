# -*- coding: utf-8 -*-
"""
str.endswith takes a tuple of strings as well as a string

# see also https://docs.python.org/3/library/stdtypes.html
"""

import os

def is_jpg(filename:str) -> bool:
    extensions = ('.jpg', '.jpeg', '.JPG', '.JPEG')
    return filename.endswith(extensions)

# endswith takes a string
print("test.jpg".endswith(".jpg")) # True

# endswith takes a tuple of strings
print("test.jpeg".endswith(('.jpg', '.jpeg'))) # True
print(is_jpg("test.jpeg")) # True
print(is_jpg("test.png")) # False
print("")

for filename in os.listdir():
    if is_jpg(filename):
        print("%s is a jpg file." %(filename))
        


