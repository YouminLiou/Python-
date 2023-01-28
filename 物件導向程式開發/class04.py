# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 09:32:54 2022

@author: user
"""


class Animal():
    def __init__(self, name, age):
        self.__name = name  #定義私用屬性
        self.__age = age
    def __sing(self):  #定義私用方法
        print(self.__name + str(self.__age), end=("歲，很會唱歌！"))
    def talk(self):  #定義共用方法
        self.__sing()  #使用私用方法
        print("也會模仿人類說話！")


bird = Animal("鸚鵡", 2)
bird.talk()

bird.__age = -1 #設定無效
bird.talk()
#bird.__sing()   #執行出現錯誤



















