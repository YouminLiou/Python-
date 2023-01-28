# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 19:53:57 2023

@author: user
"""

content = '''Hello Python
中文字測試
Welcome
'''

content = content.encode("utf-8")
with open('file.bin', 'wb') as f:
    f.write(content)





















