# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 08:56:30 2021

@author: Dell
"""

def readint(prompt, min, max):
    try:
        prompt = int(input())
        if prompt < min or prompt > max:
            print("Error: el valor no está en el rango permitido " + str(min) + " hasta " + str(max))
            return readint(print("Ingresa un numero de -10 a 10: " , end=' '))
     
    except ValueError:
        print("Error: entrada incorrecta")
        return readint(print("Ingresa un numero de -10 a 10: " , end=' ')) 
    
    else:
        return prompt


v = readint(print("Ingresa un numero de -10 a 10: ", end=''), -10, 10)

print("El numero es:", v)