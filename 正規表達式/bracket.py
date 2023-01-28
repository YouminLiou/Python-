# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 19:13:31 2022

@author: user
"""

import re
pat = r'[0-9+]+'
s = "Amy was 18 year old,she likes Python and C++"
m = re.findall(pat, s)
print(m)






















