# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 08:19:08 2021

@author: Dell
"""


try:
    y=1/0
except ArithmeticError:
    print('Error Aritmético')
except ZeroDivisionError:
    print('Error division para cero')



try:
    y=1/0
except ZeroDivisionError:
    print('Error division para cero')    
except ArithmeticError:
    print('Error Aritmético')