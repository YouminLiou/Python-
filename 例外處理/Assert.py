# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:32:30 2022

@author: user
"""

class Car():
    def __init__(self, speed):
        self.speed = speed
        
    def Turbo(self, n):
        assert speed >= 0, "速度不可能為負！"
        self.speed += n
        
for speed in (60, -20):
    bus = Car(speed)
    print("初速 = ",bus.speed,end=(" "))
    bus.Turbo(50)
    print("加速後，速度 = ",bus.speed)



















