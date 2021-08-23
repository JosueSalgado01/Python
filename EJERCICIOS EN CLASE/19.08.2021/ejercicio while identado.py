# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:35:04 2021

@author: Dell
"""

while True:
    x=input('ingrese un número para contar: ')
    if x=='q' or x=='quit':
       break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break