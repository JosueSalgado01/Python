# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:33:30 2021

@author: Dell
"""
def readint(prompt, min, max):
    try:
        prompt=int(input('Ingresa un número de -10 a 10: '))
        assert prompt >= min and prompt <= max
        return prompt
    except ValueError:
        print("Error: entrada incorrecta")
        return readint(prompt, min, max)
    except AssertionError:
        print("Error: el valor no está dentro del rango permitido (-10 a 10)")
        return readint(prompt, min, max)
  
v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)
