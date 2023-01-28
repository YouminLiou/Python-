# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 21:25:06 2022

@author: user
"""


class Father():
    def say(self):
        print("明天會更好！")

class Mother():
    def say(self):
        print("包容、尊重！")

class Child(Father, Mother):
    pass

child = Child()
child.say()





















