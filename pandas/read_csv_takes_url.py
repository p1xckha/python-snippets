# -*- coding: utf-8 -*-
'''
read_csv takes a url as well as a filepath.
see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
'''

import pandas as pd

filepath_as_url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD" # placeholder
data = pd.read_csv(filepath_as_url)
print(data.iloc[:10])
