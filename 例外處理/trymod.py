# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:27:41 2022

@author: user
"""

try:
    a = int(input("請輸入第一個數字："))
    b = int(input("請輸入第一個數字："))
    r = a % b
except ValueError :
    print("發生輸入非數值的錯誤！")
except Exception as e : #捕捉其他所有例外，並利用e顯示錯誤訊息
    print("發生",e,"的錯誤，包括分母為0的錯誤！")
else :
    print("r = ",r)
finally :
    print("一定會執行的程式區塊")





















