# -*- coding: utf-8 -*-

import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np

def cross_entropy_loss_one_sample():
    criterion = torch.nn.CrossEntropyLoss()
    x = torch.tensor([[1, 1, 2, 1, -2, -2, -2, -2, -3, 0]],dtype=torch.float32)
    y = torch.tensor([2])
    x_softmax = F.softmax(x, dim=1)
    loss = criterion(x, y)
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"softmax(x): {x_softmax}")
    print(f"loss: {loss}")
    
    n = x.shape[1]
    fig, ax = plt.subplots()
    ax.bar(np.arange(n), x_softmax.numpy()[0])
    ax.set_xlabel('Class')
    ax.set_ylabel('Probability')
    plt.show()
    
