# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:52:27 2023

@author: user
"""

def choose():
    str = "你喜歡的球類運動："
    for i in range(0, len(choice)):   #逐一檢查項目是否被選取
        if(choice[i].get() == 1): #若被選取為1,未被選取為0
            str = str + ball[i] + ""
    msg.set(str)



import tkinter as tk

win = tk.Tk()
choice = []
ball = ["足球", "籃球", "羽球"]
msg = tk.StringVar()
label = tk.Label(win, text = "選擇喜歡的球類運動：")
label.pack()
for i in range(0, len(ball)):
    tem = tk.IntVar()
    choice.append(tem)
    item = tk.Checkbutton(win, text = ball[i], variable = choice[i], command = choose)
    item.pack()
lblmsg = tk.Label(win, fg = "red", textvariable = msg)
lblmsg.pack()
win.mainloop()























