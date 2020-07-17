# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 20:49:51 2017

@author: RSF
"""

import time
import math
import win32api
import win32con
for i in range(500):
    x = int(500+math.sin(math.pi*i/100)*500)
    y = int(500+math.cos(i)*100)
    win32api.SetCursorPos((x,y))
    time.sleep(.01)