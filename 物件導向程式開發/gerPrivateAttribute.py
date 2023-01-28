# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 21:16:32 2022

@author: user
"""

class Father():
    def __int__(self, name):
        self.name = name
        self.__eye = "黑色"
    def getEye(self):
        return self.__eye
    
class Child(Father):
    def __init__(self, name, eye):
        super().__int__(name)
        self.eye = eye
        self.fatherEye = super().getEye()

joe = Child("小華", "棕色")
print(joe.name + "眼睛是" + joe.eye + "，他的父親則是" + joe.fatherEye)



















