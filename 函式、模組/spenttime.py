# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:19:35 2022

@author: user
"""

import time

start = time.time()  #取得開始時間
print("開始時間：{}".format(start))
for i in range(100):
    time.sleep(0.001) #暫停0.001秒
end = time.time()  #取得結束執行時間
print("結束時間：{}".format(end))
print("使用時間：%7.2f 秒" % (end - start))

















