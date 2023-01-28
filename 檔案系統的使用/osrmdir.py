# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 20:43:24 2022

@author: user
"""

import os
dir = "myDir"
if os.path.exists(dir):
    os.rmdir(dir)
else:
    print(dir + "目錄未建立！")





















