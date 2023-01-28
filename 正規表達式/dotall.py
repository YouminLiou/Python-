# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:36:47 2022

@author: user
"""

import re
pat = r'.*'
s = "Do your best,\nGo Go Go!"
m = re.search(pat, s)
print(m.group())
m2 = re.search(r'.*', s, re.DOTALL)
print(m2.group())



















