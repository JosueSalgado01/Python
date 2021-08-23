# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:21:50 2021

@author: Dell
"""
def l100kmtompg(liters):
    gallons=liters/3.78 #gallons
    miles=100*1000/1609.344 #mil
    return(miles/gallons)
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))

def mpgtol100km(miles):
    liters=3.785411784 #gallons
    km100=miles*1609.344/(1000*100)
    return(liters/km100)


print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
