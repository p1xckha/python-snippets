# -*- coding: utf-8 -*-

def global_variable_in_lambda():
    muls = []
    for i in range(4):
        muls.append(lambda x: x * i)
    print(muls[0](2)) # 6
    print(muls[1](4)) # 12
    
    i = 1000
    print(muls[1](2)) # 2000
    print("using a global variable in lambda is not recommended")
    
def lambda_taking_global_variable():
    muls = []
    for i in range(4):
        muls.append(lambda x,j=i: x * j)
    print(muls[0](10)) # 0
    print(muls[1](100)) # 100


def multiplier(x):
    def inner_function(y):
        return x * y
    return inner_function


global_variable_in_lambda()
lambda_taking_global_variable()

closure = multiplier(3)
print(closure(5))   # 15




