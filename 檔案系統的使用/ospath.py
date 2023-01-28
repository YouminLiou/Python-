# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 09:01:02 2023

@author: user
"""

import os
filename = os.path.abspath("ospath.py")
if os.path.exists(filename):
    basename = os.path.basename(filename) #傳回最後的檔案或路徑名稱
    print("最後檔案或路徑名稱：" + basename)

    dirname = os.path.dirname(filename)
    print("目前檔案目錄路徑：" + dirname)
    
    print("是否為目錄：", os.path.isdir(filename))
    
    fullpath, fname = os.path.split(filename)
    print("目錄路徑：" + fullpath)
    print("檔名：" + fname)
    
    Drive, fpath = os.path.splitdrive(filename)
    print("磁檔機：" + Drive)
    print("路徑名稱：" + fpath)
    
    fullpath = os.path.join(fullpath, fname)
    print("組合路徑：" + fullpath)




















