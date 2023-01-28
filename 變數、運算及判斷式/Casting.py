# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:11:12 2022

@author: user
"""

num1 = 5 + 7.8
num2 = 5 + True

#num3 = 23 + "67"  錯誤, 字串無法進行佳法運算
num3 = 23 + int("67")

score = 60
#print("小明的成績為" + score)  錯誤, 數值無法自動轉換為字串
print("小明的成績為" + str(score))












