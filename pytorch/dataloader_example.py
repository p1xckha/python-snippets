# -*- coding: utf-8 -*-

from torch.utils.data import Dataset, DataLoader
import torch
import numpy as np

class Data(Dataset):
    def __init__(self, x: torch.Tensor, y: torch.Tensor):
        self.x = x
        self.y = y
        self.len = len(x)
    
    def __getitem__(self, index:int):
        return self.x[index], self.y[index]
    
    def __len__(self):
        return self.len

def dataloader_example1():
    x = np.arange(5)
    y = np.arange(5) * 0.1
    data = list(zip(x,y)) # list of tuples
    dl = DataLoader(data, batch_size=2, shuffle=False)
    for xbatch, ybatch in dl:
        print(f"xbatch:{xbatch}")
        print(f"ybatch:{ybatch}")
        print("")
    print("*" * 30)

def dataloader_example2():
    x = torch.arange(8)
    y = torch.arange(8) * 0.1
    data = Data(x, y) # data object
    dl = DataLoader(data, batch_size=4, shuffle=False)
    for xbatch, ybatch in dl:
        print(f"xbatch:{xbatch}")
        print(f"ybatch:{ybatch}")
        print("")
    print("*" * 30)

dataloader_example1()
dataloader_example2()




