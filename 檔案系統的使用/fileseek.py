# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 20:04:34 2023

@author: user
"""


f = open('file.bin', 'rb')
print("目前文件索引位置：",f.tell())
f.seek(6) #一道索引第6位置(第7個字元)
str1 = f.read(7) #讀取7個字元
print(str1)
print("目前文件索引位置：",f.tell())

f.seek(0) #回文件最前端
print("目前文件索引位置：",f.tell())
str2 = f.read(5)
print(str2)

f.seek(-8, 2) #移至最尾端，向前取8個字元
str3 = f.read()
print(str3)

f.close()

















