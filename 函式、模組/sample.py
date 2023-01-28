# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:06:18 2022

@author: user
"""

import random as r

list1 = r.sample(range(1, 50), 7)
special = list1.pop()  #取最後一個元素當特別號
list1.sort()  #號碼從小到大排序
print("本期大樂透中獎號碼為：", end="")
for i in range(0, 6):
    if i == 5 :
        print(str(list1[i]))
    else :
        print(str(list1[i]), end=(", "))
print("本期大樂透特別號為：" + str(special))





















