# -*- coding: utf-8 -*-
'''
download images data from MNIST and plot the image of the first 25
'''

import gzip
import struct
import numpy as np
import matplotlib.pyplot as plt
import requests
import os
import math

class Mnist_plot():
    def __init__(self):
        self.saved_datas = []
    
    def download_data(self, url:str)-> None:
        response = requests.get(url)
        if response.status_code == 200:
            save_filename = os.path.basename(url)
            with open(save_filename, 'wb') as f:
                f.write(response.content)
                print(f"downloaded: {url}")
                self.saved_datas.append(save_filename)
        else:
            print('Request failed with status code:', response.status_code)

    def download_datas(self, urls:list[str]):
        for url in urls:
            self.download_data(url)
    
    
    def least_number_larger_than_n(self, n):
        root_n = math.ceil(math.sqrt(n))
        return root_n 

    def plot_mnist_first_images(self, filename:str=None, head:int=25):

        if filename == None:
            url = 'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz'
            filename = os.path.basename(url)
            if not os.path.exists(filename):
                self.download_data(url)
            
        with gzip.open(filename, 'rb') as f:
            # Read the first 16 bytes of metadata
            magic, n_images, n_rows, n_cols = struct.unpack('>IIII', f.read(16))
            print('Magic number:', magic) # magic number assigned to each data
            print('Number of images:', n_images) # 60000
            print('Image size:', n_rows, 'x', n_cols) # 28x28
        
            # Read the image data for the first 25 images
            image_size = n_rows * n_cols
            images_data = f.read(image_size * n_images)
            images = np.frombuffer(images_data, dtype=np.uint8)
            images = images.reshape(n_images, n_rows, n_cols)
            
            # we are going to create n x n table
            n = self.least_number_larger_than_n(head)
        
            # Plot the images
            fig, axes = plt.subplots(nrows=n, ncols=n, figsize=(8, 8))
            for i, ax in enumerate(axes.flat):
                if i < head:
                    ax.imshow(images[i], cmap='gray')
                ax.axis('off')
            plt.show()


if __name__ == '__main__':
    urls = [
            'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz',
            'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz',
            'http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz',
            'http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz'
            ]
    plotter = Mnist_plot()
    # plotter.download_datas(urls)
    filenames = list(map(os.path.basename, urls)) 
    filename = filenames[0] # train-images-idx3-ubyte.gz
    plotter.plot_mnist_first_images(filename)


