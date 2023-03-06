# -*- coding: utf-8 -*-
'''
see also https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html
'''

import torch.nn as nn
import matplotlib.pyplot as plt
import torch

relu = nn.ReLU()
x = torch.arange(-1,1,0.01)
y = relu(x)

plt.plot(x.numpy(), y.numpy(), label='y=relu(x)')
plt.legend()
plt.show()
