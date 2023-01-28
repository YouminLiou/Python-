# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 10:16:06 2022

@author: user
"""



n = eval(input("請輸入大於1的整數："))
if(n == 2) :   #2無法以正常質數判斷方式，所以直接列印
    print("2是質數！")
else :
    for i in range(2, n):
        if(n % i == 0) :
            print("%d 不是質數！"% n)
            break
    else :
        print("%d是質數！"% n)








