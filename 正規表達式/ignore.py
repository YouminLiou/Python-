# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 19:55:08 2022

@author: user
"""


import re
pat = r'PYTHON|ANDROID'
s = "I like Python and Android"
m = re.findall(pat, s, re.I)
print(m) 





















