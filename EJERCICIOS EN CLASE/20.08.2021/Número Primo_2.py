# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:57:09 2021

@author: Dell
"""


def primo(num):
    for i in range(2,int(num*0.5)+1):
        if num%i==0:
            return False    
    return True        
for i in range(1,20):
    if primo(i+1):
        print(i+1,end=" ")
print()
