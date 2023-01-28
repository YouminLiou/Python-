# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 17:17:56 2022

@author: user
"""

try:
    a = int(input("請輸入第一個整數："))
    b = int(input("請輸入第二個整數："))
    r = a % b
except (ValueError, ZeroDivisionError) as e:
    print("發生 {} 0 的錯誤！".format(e))
else:
    print("r = ",r)





















