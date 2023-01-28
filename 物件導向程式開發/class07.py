# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:12:52 2022

@author: user
"""

class Animal():
    def fly(self):
        print("時速20公里！")

class Bird(Animal):
    def fly(self, speed):
        print("時速" + str(speed) + "公里！")

class Plabe():
    def fly(self):
        print("時速1000公里！")

def fly(speed):
    print("時速" + str(speed) + "英哩！")

animal = Animal()
animal.fly()

bird = Bird()
bird.fly(60)

plane = Plabe()
plane.fly()

fly(5)






