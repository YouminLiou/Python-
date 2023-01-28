# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:19:16 2022

@author: user
"""


nat = eval(input("請輸入國文成績："))
math = eval(input("請輸入數學成績："))
eng = eval(input("請輸入英文成績："))
sum = nat + math + eng
average = sum/3
print("成績總分：%d，平均成績：%5.2f"%(sum, average))









