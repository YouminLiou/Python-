# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 19:54:00 2022

@author: user
"""

import re
pat = re.compile(r'[aeiou]+')
s = "John is my best frient."
m = re.findall(pat, s)
print(m)