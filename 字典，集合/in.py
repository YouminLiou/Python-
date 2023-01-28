# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 18:23:08 2022

@author: user
"""

dict1 = {"綾小明":85, "曾山水":93, "鄭美麗":67}
name = input("請輸入學生姓名：")
if name in dict1 :
    print(name + "的成績為" + str(dict1[name]))
else :
    score = eval(input("請輸入學生分數："))
    dict1[name] = score
    print("字典內容：" + str(dict1))











