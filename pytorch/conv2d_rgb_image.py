# -*- coding: utf-8 -*-

import torch
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision
from PIL import Image

# load the image and convert to RGB format to remove alpha channel
image = Image.open('mario.png').convert('RGB')

# convert the image to a tensor and add batch dimension
image_tensor = transforms.ToTensor()(image).unsqueeze(0) # torch.Size([1, 3, 871, 481])

# define the kernel weights for RGB images
blur_kernel = torch.ones(3, 3, 3, dtype=torch.float32) / 9.0 # torch.Size([3, 3, 3])
blur_kernel = blur_kernel.unsqueeze(0) # torch.Size([1, 3, 3, 3])

# apply the convolution operation
output = F.conv2d(image_tensor, blur_kernel, padding=1) # torch.Size([1, 1, 871, 481]) 

torchvision.utils.save_image(output , 'mario_conv.png') 


