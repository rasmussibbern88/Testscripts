# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:12:25 2017

@author: rassi
"""

import urllib2
mp3file = urllib2.urlopen("http://www.example.com/songs/mp3.mp3")
with open('https://image.4sound.com/i/36441/zildjian-asdg-dave-grohl.jpg','wb') as output:
  output.write(mp3file.read())
