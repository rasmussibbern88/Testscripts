# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:32:32 2017

@author: RSF
"""

from cryptography.fernet import Fernet

key = Fernet.generate_key()
text = "Mit navn er Rasmus"
f = Fernet(key)
token = f.encrypt(b"tekst")
print(token)
print(text)
