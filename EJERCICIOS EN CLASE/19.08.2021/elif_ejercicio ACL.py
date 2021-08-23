# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:23:25 2021

@author: Dell
"""

acl=int(input("Ingrese el número de ACL: "))
if acl>=1 and acl<=99:
    print("es una ACL estándar")
elif acl>=100 and acl<=199: 
    print("es una ACL extendida")
else:
    print("El # ingresado no es de una ACL")