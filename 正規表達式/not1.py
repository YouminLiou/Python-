# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:03:08 2022

@author: user
"""

import re
pat = r'[^a-z. ]+'
s = "John was 18 year old."
m = re.findall(pat, s)
print(m)
















