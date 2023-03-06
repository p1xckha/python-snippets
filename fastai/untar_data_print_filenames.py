# -*- coding: utf-8 -*-
'''
Download pet images using FastDownload.get and print their location.
If there are many filenames, print only the first 3 and last 3.

fastai - External data
https://docs.fast.ai/data.external.html
'''
from fastai.vision.all import untar_data, URLs
import pathlib
import os

def print_filenames(path, first=3, last=3, omit=True):
    print("printing filenames in %s" %(path))
    print("#"*50)
    for root, dirs, files in os.walk(path):
        if len(files) > first+last and omit:
            for file in files[:first]:
                print(os.path.join(root, file))
            print("...")
            for file in files[-last:]:
                print(os.path.join(root, file))
        else:
            for file in files:
                print(os.path.join(root, file))
        print("")
    print("")

# Download url using FastDownload.get
save_dir = untar_data(URLs.PETS) # ~/.fastai/data/oxford-iiit-pet

# print files in ~/.fastai
print_filenames(save_dir)

# message
print("The filenames of cats start with an uppercase letter,")
print("while the filenames of dogs start with a lowercase letter.")


