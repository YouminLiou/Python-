# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:03:37 2023

@author: user
"""

import tkinter as tk
win = tk.Tk()
#第1個視窗區塊
frame1 = tk.Frame(win)
frame1.pack()
label1 = tk.Label(frame1, text = "標籤一：")
entry1 = tk.Entry(frame1)
label1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)
#第2個視窗區塊
frame2 = tk.Frame(win)
frame2.pack()
button1 = tk.Button(frame2, text = "確定")
button2 = tk.Button(frame2, text = "取消")
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
win.mainloop()

















