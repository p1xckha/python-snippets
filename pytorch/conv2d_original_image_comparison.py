# -*- coding: utf-8 -*-
import torch
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision
import matplotlib.pyplot as plt


# Load the MNIST data
mnist_data = torchvision.datasets.MNIST('data', train=True, download=True, transform=transforms.ToTensor())
image, label = mnist_data[0] # torch.Size([1, 28, 28]), integer 5

torchvision.utils.save_image(image, 'mnist_five.png') 

# define the kernel that performs Laplacian edge detection
laplacian_kernel = torch.tensor([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=torch.float32)

# Define the Sobel kernel
sobel_kernel = torch.tensor([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=torch.float32)

# Perform the convolution
# use unsqueeze(0) to add a new dimension to image and kernel as follow
# image: torch.Size([1, 28, 28]) -> torch.Size([1, 1, 28, 28])
# kernel: torch.Size([3,3]) ->  torch.Size([1, 1, 3, 3])

laplacian_conv_output = F.conv2d(image.unsqueeze(0), laplacian_kernel.unsqueeze(0).unsqueeze(0), padding=1, stride=1) # torch.Size([1, 1, 28, 28])
sobel_conv_output = F.conv2d(image.unsqueeze(0), sobel_kernel.unsqueeze(0).unsqueeze(0), padding=1, stride=1) # torch.Size([1, 1, 28, 28])


# Remove the batch dimension 
laplacian_conv_output = laplacian_conv_output.squeeze() # torch.Size([28, 28])
sobel_conv_output = sobel_conv_output.squeeze() # torch.Size([28, 28])

# Plot the original and convolved images
fig, ax = plt.subplots(2, 2)
ax[0][0].imshow(image.squeeze().numpy(), cmap='gray')
ax[0][0].axis('off')
ax[0][0].set_title('Original Image')

ax[0][1].imshow(laplacian_conv_output.squeeze().numpy(), cmap='gray')
ax[0][1].axis('off')
ax[0][1].set_title('Laplacian Edge Detection')

ax[1][0].imshow(image.squeeze().numpy(), cmap='gray')
ax[1][0].axis('off')
ax[1][0].set_title('Original Image')

ax[1][1].imshow(sobel_conv_output.squeeze().numpy(), cmap='gray')
ax[1][1].axis('off')
ax[1][1].set_title('Sobel Edge Detection')

plt.show()










