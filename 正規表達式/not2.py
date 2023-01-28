# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:05:53 2022

@author: user
"""

import re
pat = r'^\d+'
s = "2020 is coming soon"
m = re.findall(pat, s)
print(m)
m2 = re.findall(r'\w+$', s)
print(m2)

















