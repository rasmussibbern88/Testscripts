# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 00:30:22 2017

@author: RSF
"""

import numpy as np
import opencv as cv2
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()