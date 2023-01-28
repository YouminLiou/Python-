# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:22:58 2022

@author: user
"""

listname = ["林大明", "陳阿忠", "張小英"]
listchinese = [100, 74, 82]
listmath = [87, 88, 65]
listenglish = [70, 100, 8]
print("姓名    座號   國文  數學  英文 ")
for i in range(0, 3):
    print(listname[i].ljust(5), str(i+1).rjust(3), str(listchinese[i]).rjust(5), str(listmath[i]).rjust(5), str(listenglish[i]).rjust(5))

#range式重0開始，但座號是從1，所以i+1










