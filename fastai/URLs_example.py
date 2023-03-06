# -*- coding: utf-8 -*-
'''
print all urls in URLs

fastai - External data
https://docs.fast.ai/data.external.html
'''

from fastai.vision.all import URLs
import pprint 

# vars(object) returns a mappingproxy object which is similar to a dict
dict_of_urls = {}
for key, value in vars(URLs).items(): 
    if isinstance(value, str) and value.startswith("http"):
        dict_of_urls[key] = value
        
pprint.pprint(dict_of_urls)

