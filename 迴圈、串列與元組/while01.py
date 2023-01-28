# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 10:23:00 2022

@author: user
"""

total = person = score =0   #total總數  person學生人數  score成績
while(score != -1) :
    person += 1   #計算人數
    total += score   #計算總成績
    score = eval(input("請輸入第%d位學生的成績："% person))
    
arg = total / (person - 1)  #計算平均分數
print("本班總成績：%d分，平均成績為：%5.2f 分"% (total, arg))











