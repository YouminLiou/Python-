# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 21:20:57 2022

@author: user
"""

import os
filename = os.path.abspath("osexists.py")
if os.path.exists(filename):
    print("完整路徑名稱：" + filename)
    print("檔案大小：", os.path.getsize(filename))




















