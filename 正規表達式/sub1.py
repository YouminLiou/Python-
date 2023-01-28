# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:56:31 2022

@author: user
"""

import re
pat = r'\d+'
substr = '*'
s = "Password:1234, ID:5678"
result = re.sub(pat, substr, s)
print(result)




















