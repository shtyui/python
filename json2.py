# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:36:22 2021

@author: USER
"""

import json
file = '123.json'
with open(file, 'r') as obj:
    data = json.load(obj)

print(data)
print(type(data))