# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 20:40:38 2022

@author: user
"""

import os
dir = "myDir"
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print(dir + "已經建立！")






















