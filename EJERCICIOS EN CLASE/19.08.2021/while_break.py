# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:26:16 2021

@author: Dell
"""

contar=input("Ingrese el # de veces a contar: ")
contar=int(contar)
contador=1
while True:
    print(contador)
    #contador=contador+1
    contador+=1
    if contador>contar:
        break