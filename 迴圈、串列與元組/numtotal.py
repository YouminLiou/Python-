# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:36:20 2022

@author: user
"""



sum = 0

n = eval(input("請輸入正整數："))  #轉換輸入資料的型別
for i in range(1, n+1) :    #以迴圈計算總合
    sum += i

print("1 到 %d 的整數和為 %d" % (n, sum))







