# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:00:03 2022

@author: user
"""


class Animal(): #定義父類別
    def __init__(self, name):
        self.name = name  #定義共用屬性
    def fly(self):  #定義共用方法
        print(self.name + "很會飛！")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name) #執行父類別的__init__()方法
        self.age = age
    def fly(self):
        print(str(self.age), end=("歲"))
        super().fly()   #執行父類別的fly()方法

pigeon = Animal("小白鴿")
pigeon.fly()

parrot = Bird("小鸚鵡", 2)
parrot.fly()





















