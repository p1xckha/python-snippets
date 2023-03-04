# -*- coding: utf-8 -*-
"""
An index as boolean tensor for another integer tensor can be used 
to divide the integer tensor into two classes(0 and 1) 
based on a threshold value.

e.g. y[bool_tensor]
"""

import torch

threshold_value = 0.2
x = torch.arange(0,1,0.2)
bool_tensor = x > threshold_value # tensor([True, True, False, ..., False])

# x is divided into two classes (0 and 1) based on a threshold value of 0.2.
y = torch.zeros(x.shape[0]) # initialize
y[bool_tensor] = 1

# show the result 
for i in range(len(x)):
    print("x[%d]=%.1f > %.1f is %s" %(i, x[i], threshold_value, bool_tensor[i].item()) )
print("")

print("x:", x)
print("y:", y)
print("bool_tensor:", bool_tensor)



