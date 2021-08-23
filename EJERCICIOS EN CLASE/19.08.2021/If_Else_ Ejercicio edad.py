# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:33:22 2021

@author: Dell
"""

space=input("Cuál es tu nombre? ")
apellido=input("Cuál es tu apellido? ")
edad=int(input("Cuántos años tienes? "))
if edad>=1 and edad<=12:
    print("Es un niñ@")
elif edad>=13 and edad<=60: 
    print("Es un adulto")
else:
    print("Es adulto mayor")
dirección=input("Dónde vives? ")
print('Hola'+' '+ space+' '+apellido+' '+ 'Bienvenido')