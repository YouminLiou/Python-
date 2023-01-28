# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:20:34 2022

@author: user
"""

import re
pat = r'.o'
s = "Do your best!"
m = re.findall(pat, s)
print(m)
m2 = re.findall(r'.*o', s)
print(m2)












