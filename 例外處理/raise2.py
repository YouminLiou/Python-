# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 17:49:10 2022

@author: user
"""

class MyException(RuntimeError):
    def __init__(self, arg):
        self.args = arg

def CheckSpeed(speed): #檢查速度
    if speed < 70:
        raise Exception("速度太慢了！") #拋出 Exception 型別例外
    elif speed > 110:
        raise Exception("已經超速了！")
    else:
        raise MyException("快樂駕駛，平安返家！")

def convertTuple(tup):
    str = ''.join(tup)
    return str


for speed in (60, 100, 150):
    try:
        CheckSpeed(speed)
    except MyException as e:
        err = convertTuple(e.args)
        print("目前速度： {} ， {}".format(speed, err))
    except Exception as e:
        print("現在速度： {} ， {}".format(speed, e))






















