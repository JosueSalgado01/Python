# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 08:32:26 2021

@author: Dell
"""

def Fun(n):
    try: 
        return n/0
    except:
        print('Error en cualquier parte')
        raise
try:
    Fun(0)
except ArithmeticError:
    print('Error lanzado por raise')

print('Final')
    

