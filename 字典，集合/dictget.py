# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 10:58:07 2022

@author: user
"""

#建立4個血型及個性的字典
dict1 = {"A" : "內向穩重", "B" : "外向樂觀", "O" : "堅強自信", "AB" : "聰明自然"}
name = input("輸入要查詢的血型：").upper() #輸入血型並轉大寫
blood = dict1.get(name)  #以get取得個性
if(blood == None) :
    print("沒有%s血型"% name)
else :
    print(name + "血型的個性為" + str(dict1[name]))












