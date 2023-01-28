# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 09:23:06 2022

@author: user
"""


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self):
        print(self.name + str(self.age) + "歲，很會唱歌！")
    def grow(self, year):
        self.age += year
        
        
bird = Animal("鸚鵡", 1)
bird.grow(1)
bird.sing()



















