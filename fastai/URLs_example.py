# -*- coding: utf-8 -*-

'''
fastai - External data
https://docs.fast.ai/data.external.html
'''

from fastai.vision.all import URLs
import pprint 

dict_of_urls = {}
for key, value in vars(URLs).items(): # var(object) is dict
    if isinstance(value, str) and value.startswith("http"):
        dict_of_urls[key] = value
        
pprint.pprint(dict_of_urls)

