# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:50:04 2022

@author: user
"""


person = eval(input("請輸入學生人數："))
apple = eval(input("請輸入蘋果總數："))
ret = divmod(apple, person)
print("每個學生可分得蘋果" + str(ret[0]) + "個")
print("蘋果剩餘" + str(ret[1]) + "個")









