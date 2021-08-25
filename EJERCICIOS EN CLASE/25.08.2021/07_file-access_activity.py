# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:51:11 2021

@author: Dell
"""

file=open('devices.txt','a')
while True:
    newItem = input('Enter device name: ')
    if newItem == 'exit':
        print('All done!')
     
        break
    file.write(newItem + '\n')
file.close()

