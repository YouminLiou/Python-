# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:08:18 2022

@author: user
"""


langs = {"Python", "Java", "Kotlin"}
enum_langs = enumerate(langs) #轉換為enumerate物件
print(type(enum_langs))


#轉成串列
print(list(enum_langs))

#以迴圈輸出
for item in enumerate(langs) :
    print(item)
    
for i,item in enumerate(langs):
    print(i, item)











