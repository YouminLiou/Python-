# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 18:26:15 2022

@author: user
"""

import re
numStr = "tel:04-12345678"
pat = r'(\d{2})-(\d{8})'

phone = re.search(pat, numStr)
if not phone == None:
    print(phone.group())
    print(phone.group(0))
    print(phone.group(1))
    print(phone.group(2))



















