# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:57:20 2022

@author: user
"""


innum = 0
list1 = []
while(innum != -1) :
    innum = eval(input("請輸入電費(-1：結束)："))
    list1.append(innum)
list1.pop()  #-1不算輸入的數值所以將其移除
print("共輸入%d個數"% len(list1))
print("最多電費為：%d"% max(list1))
print("最少電費為：%d"% min(list1))
print("電費總和為：%d"% sum(list1))
print("電費由大到小排序為：{}".format(sorted(list1, reverse=True)))















