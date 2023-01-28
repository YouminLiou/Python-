# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:47:58 2022

@author: user
"""


import re
phoneList = ["0412345678", "(04)12345678", "(04)-12345678", "(049)2987654", "0937-998877"]

pat = '''
\(\d{2,4}\)-?\d{6,8}
|\d{9,10}
|\d{4}-\d{6,8}
'''

for phone in phoneList:
    phoneNum = re.search(pat, phone, re.VERBOSE)
    if not phoneNum == None:
        print(phoneNum.group())


















