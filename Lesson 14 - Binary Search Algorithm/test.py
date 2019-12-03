import os
os.getcwd()
os.chdir('/home/tuantcm/gitspace')

import pandas as pd

df = pd.read_csv('vi-vocab', encoding='windows-1252')

import codecs
with codecs.open('vi-vocab', 'r', encoding='utf-8',
                 errors='ignore') as fdata:
    data = fdata.read()