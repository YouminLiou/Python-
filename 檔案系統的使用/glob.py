# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 18:43:18 2023

@author: user
"""

import glob
files = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt")
for file in files:
    print(file)



















