# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:37:57 2021

@author: Dell
"""
lista=[]
file=open('devices.txt','r')
for i in file:
    i=i.strip()
    lista.append(i)
    print (i)
file.close()
print(lista)