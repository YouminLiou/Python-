# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 20:26:55 2022

@author: user
"""


import os
file = "myFile.txt"
if os.path.exists(file):
    os.remove(file)
else:
    print(file + "檔案未建立！")



















