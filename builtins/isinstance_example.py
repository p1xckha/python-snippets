# -*- coding: utf-8 -*-

def say_hello_to(friend: str):
    assert isinstance(friend, str), "friend must be a string."
    print("Hello " + friend )

if __name__ == "__main__":
    say_hello_to("John")
    
    try:
        say_hello_to(1)
    except AssertionError as error:
        print(error)
