# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 10:30:35 2022

@author: user
"""


score = []   #建立空串列
total = inscore = 0  #total總成績  inscore輸入的成績
while(inscore != -1) :
    inscore = eval(input("請輸入學生的成績："))
    score.append(inscore)   #將成績輸入串列
print("共有%d位學生"% (len(score) - 1))  #-1不算成績，所以要-1

for i in range(0, len(score) - 1):  #計算分數
    total += score[i]
    
arg = total / (len(score)-1)
print("本班總成績：%d 分，平均成績：%5.2f 分"% (total, arg))










