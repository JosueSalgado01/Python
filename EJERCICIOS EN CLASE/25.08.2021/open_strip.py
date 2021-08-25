# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:33:51 2021

@author: Dell
"""

file=open('devices.txt')
for i in file:
    i=i.strip()
    print (i)
file.close()