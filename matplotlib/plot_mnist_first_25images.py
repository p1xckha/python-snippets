# -*- coding: utf-8 -*-
import gzip
import struct
import numpy as np
import matplotlib.pyplot as plt
import requests
import os


def download_data(url:str=None)-> None:    
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            save_filename = os.path.basename(url)
            with open(save_filename, 'wb') as f:
                f.write(response.content)
                print(f"downloaded: {url}")
        else:
            print('Request failed with status code:', response.status_code)


def plot_mnist_first_25images(filename:str):
    with gzip.open(filename, 'rb') as f:
        # Read the first 16 bytes of metadata
        magic, n_images, n_rows, n_cols = struct.unpack('>IIII', f.read(16))
        print('Magic number:', magic) # magic number assigned to each data
        print('Number of images:', n_images) # 60000
        print('Image size:', n_rows, 'x', n_cols) # 28x28
    
        # Read the image data for the first 25 images
        image_size = n_rows * n_cols
        images_data = f.read(image_size * 25)
        images = np.frombuffer(images_data, dtype=np.uint8)
        images = images.reshape(25, n_rows, n_cols)
    
        # Plot the images
        fig, axes = plt.subplots(nrows=5, ncols=5, figsize=(8, 8))
        for i, ax in enumerate(axes.flat):
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
    
    download_data(urls)
    filenames = list(map(os.path.basename, urls)) 
    filename = filenames[0] # train-images-idx3-ubyte.gz
    plot_mnist_first_25images(filename) 

