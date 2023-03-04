# -*- coding: utf-8 -*-

def say_hello_to(name: str):
    assert isinstance(name, str), "name must be string."
    print("Hello " + name )


say_hello_to("John")

try:
    say_hello_to(1)
except AssertionError as error:
    print(error)



