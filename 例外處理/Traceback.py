# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:21:34 2022

@author: user
"""

import traceback  #匯入traceback

def CheckSpeed(speed):
    if speed < 70:
        raise Exception("速度太慢了！")
    elif speed > 110:
        raise Exception("已經超速了！")
    
for speed in (60, 100, 150):
    try:
        CheckSpeed(speed)
    except Exception as e:
        with open ("err.txt","a") as f:
            f.write(traceback.format_exc()) #寫入例外過程
        print("錯誤資訊寫入完成！")
    else:
        print("目前時速： {}".format(speed))




















