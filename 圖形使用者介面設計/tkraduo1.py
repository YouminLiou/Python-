# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:39:52 2023

@author: user
"""

def choose():
    msg.set("你最喜歡的球類運動：" + choice.get())

import tkinter as tk

win = tk.Tk()
choice = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win, text = "選擇最喜歡的球類運動：")
label.pack()
item1 = tk.Radiobutton(win, text = "足球", value = "足球", variable = choice, command = choose)
item1.pack()
item2 = tk.Radiobutton(win, text = "藍球", value = "藍球", variable = choice, command = choose)
item2.pack()
item3 = tk.Radiobutton(win, text = "羽球", value = "羽球", variable = choice, command = choose)
item3.pack()
lblmsg = tk.Label(win, fg = "red", textvariable = msg)
lblmsg.pack()
item1.select() #開始時預設選項1
choose()
win.mainloop()




















