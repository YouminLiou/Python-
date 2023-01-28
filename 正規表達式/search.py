# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 18:17:46 2022

@author: user
"""


import re
pat = re.compile('[a-z]+')
m = pat.search('3tem12po')
print(m)
if not m == None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())

















