# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 17:12:39 2022

@author: user
"""


try:
    a = int(input("請輸入第一個整數："))
    b = int(input("請輸入第二個整數："))
    r = a % b
except (ValueError, ZeroDivisionError):
    print("發生輸入非數值的錯誤或分母為0的錯誤！")
else:
    print("r = ",r)





















