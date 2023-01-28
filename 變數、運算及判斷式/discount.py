# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:10:58 2022

@author: user
"""

money = eval(input("請輸入購物金額："))  #輸入的金額還要加以計算，所以轉換資料型別
if(money >= 10000) :
    if(money >= 100000) :
        print(money * 0.8, end=" 元\n") #8折
    elif(money >= 50000) :
        print(money * 0.85, end=" 元\n") #85折
    elif(money >= 30000) :
        print(money * 0.9, end=" 元\n") #9折
    else :
        print(money * 0.95, end=" 元\n") #95折
else :
    print(money, end=" 元\n") #未打折








