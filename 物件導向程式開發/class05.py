# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 09:45:09 2022

@author: user
"""


class Animal(): #定義父類別
    def __init__(self, name):
        self.name = name  #定義共用屬性
    def fly(self):  #定義共用方法
        print(self.name + "很會飛")

class Bird(Animal):
    def __init__(self, name):
        self.name = "粉紅色" + name #覆寫父類別的建構式
    def sing(self):
        print(self.name + "也愛唱歌！")

pigeon = Animal("小白鴿")
pigeon.fly()

parrot = Bird("小鸚鵡")
parrot.fly()
parrot.sing()
    

















