# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:47:15 2022

@author: user
"""


import time as t


week = ["一", "二", "三", "四", "五", "六", "日"]  #建立星期幾對應串列
dst = ["無日光節約時間", "有日光節約時間"]    #建立日光節約時間對應串列
time1 = t.localtime()
show = "現在時刻：中華民國 " + str(int(time1.tm_year)-1911) + "年"
show += str(time1.tm_mon) + "月" + str(time1.tm_mday) + "日"
show += str(time1.tm_hour) + "點" + str(time1.tm_min) + "分"
show += str(time1.tm_sec) + "秒 星期" + week[time1.tm_wday] + "\n"
show += "今天是今年的第" + str(time1.tm_yday) + "天，此地" + dst[time1.tm_isdst]


print(show)



















