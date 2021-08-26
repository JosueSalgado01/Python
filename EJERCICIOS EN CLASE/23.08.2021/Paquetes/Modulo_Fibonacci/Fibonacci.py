# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 09:48:09 2021

@author: Dell
"""

def fibonacci(n):    
    a, b = 0, 1 #a=0 y b=1
    while a < n:
        print(a, end=' ')
        '''
        c=a+b
        a=b
        b=c
        '''
        a, b = b, a+b
    print()

#fibonacci(8)

