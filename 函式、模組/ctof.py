# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:24:32 2022

@author: user
"""


def ctof(c) : #攝氏轉華氏
    f = c * 1.8 + 32 #公式：攝氏 * 1.8 + 32
    return f

inputc = float(input("請輸入攝氏溫度："))
print("華氏溫度為：%5.2f 度"% ctof(inputc))











