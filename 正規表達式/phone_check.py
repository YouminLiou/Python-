# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:45:50 2022

@author: user
"""

def isTaiwanPhone(str):
    if len(str) != 11: #檢查長度
        return False
    #檢查11個字元是否符合手機號碼格式
    for i in range(0, 11):
        if i == 4:
            if str[4] != '-': #檢查第5個字元是不是'-'
                return False
        else:
            if str[i].isdecimal == False:
                return False
    return True

print("0937-123456 是台灣手機號碼：", isTaiwanPhone('0937-123456'))
print("02-12345678 是台灣手機號碼：", isTaiwanPhone('02-12345678'))         























