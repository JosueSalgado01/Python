# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 11:42:49 2021

@author: Dell
"""
print('Inicio')
try:
    x=(int(input('Ingrese un número:')))
    y=1/x
    print(y)
except ZeroDivisionError:
    print('No puedes dividir para cero')
except ValueError:
    print('Ingresar por favor un valor entero')
except:
    print('Algo salió mal')
print('Fin')

