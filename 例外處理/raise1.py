# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 17:27:00 2022

@author: user
"""

def CheckSpeed(speed): #檢查速度
    if speed < 70:
        raise Exception("速度太慢了！") #拋出 Exception 型別例外
    elif speed > 110:
        raise Exception("已經超速了！")

for speed in (60, 100, 150):
    try:
        CheckSpeed(speed)
    except Exception as e:
        print("現在速度： {} ， {}".format(speed, e))
    else:
        print("目前速度： {}".format(speed))



















