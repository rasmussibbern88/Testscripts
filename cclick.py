    # -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 09:52:35 2017

@author: rassi
"""
import pyautogui as ptg
import time
time.sleep(1)
try:
    for i in range(400):
        ptg.click(clicks=30, button='left')
except KeyboardInterrupt:   
    print('interrupted!')   