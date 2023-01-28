# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 17:54:23 2022

@author: user
"""


import random as r   #匯入亂數模組

while True :  #以while迴圈擲骰子
    inkey = input("按任意鍵再按[Enter]鍵擲骰子，直接按[Enter]鍵結束：")
    if len(inkey) > 0 :
        num = r.randint(1, 6)
        print("你擲的骰子點數為：" + str(num))
    else :
        print("遊戲結束！")
        break
















