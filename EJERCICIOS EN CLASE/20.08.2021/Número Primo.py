# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:01:34 2021

@author: Dell
"""

def isPrime(x):
    if x<2:
        print('No es primo')
        return False
    elif x==2:
        print('Es primo')
        return True
    for j in range(2,x):
        if x % j==0:
            return False
    return True

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
