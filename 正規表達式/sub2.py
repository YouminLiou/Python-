# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:58:47 2022

@author: user
"""

import re
def multiply(m):
    v = int(m.group())
    return str(v * 2)
result = re.sub('\d+', multiply, "10 20 30 40 50", 3)
print(result)



















