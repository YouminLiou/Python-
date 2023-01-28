# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 18:29:52 2022

@author: user
"""


dict1 = {"金牌":26, "銀牌":34, "銅牌":30}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("得到的%s數目為%d面"% (listkey[i], listvalue[i]))











