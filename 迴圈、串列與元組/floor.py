# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 10:10:59 2022

@author: user
"""


n= eval(input("請輸入大樓的樓層："))
print("本大樓具有的樓層為：")

if(n > 3) :
    n += 1
for i in range(1, n+1):
    if(i == 4) :
        continue   #樓層為4時就以continue跳過
    print(i, end=" ")

print()










