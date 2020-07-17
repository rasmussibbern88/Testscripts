# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:34:12 2017
@author: rassi
"""
F0, F1 = 0, 1
for i in range(100):
    F0,F1 = F1,F1 + F0
    print(F1)