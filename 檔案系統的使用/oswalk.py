# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 18:34:42 2023

@author: user
"""

import os
cur_path = os.path.dirname(__file__)
sample_tree = os.walk(cur_path)
for dirname, subdir, files in sample_tree:
    print("檔案路徑：", dirname)
    print("目錄串列：", subdir)
    print("檔案串列：", files)
    print()



















