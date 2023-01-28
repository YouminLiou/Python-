# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 21:07:14 2022

@author: user
"""

import os
cur_path = os.getcwd()
os.system("cls")  #清除螢幕
os.system("mkdir dir2") #建立dir2目錄
os.system("copy ossystem.py dir2\copyfile.py") #複製檔案
file = cur_path + "\dir2\copyfile.py"
os.system("notepad" + file) #以記事本開啟copyfile.py



















